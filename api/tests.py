from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from .models import Agriculteur, Acheteur, Produit, Commande, CommandeProduit, Paiement, Messagerie, Avis

# Get the custom user model
User = get_user_model()

class UtilisateurTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword123',
            'telephone': '1234567890',
            'adresse': '123 Test Street'
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_create_utilisateur(self):
        url = reverse('utilisateur-list')
        response = self.client.post(url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)  # One already exists from setUp

    def test_login_utilisateur(self):
        url = reverse('login')  # Assuming you have a login endpoint
        login_data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        response = self.client.post(url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)  # Assuming your login returns a token

class AgriculteurTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='agriculteur', password='testpassword123')
        self.agriculteur = Agriculteur.objects.create(user_ptr=self.user, telephone='1234567890', adresse='123 Farm Road')

    def test_publier_produit(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('produit-list')
        produit_data = {
            'nom': 'Tomates',
            'description': 'Tomates bio',
            'prix': 10.0,
            'quantite_disponible': 100,
            'categorie': 'Légumes',
            'image': ''
        }
        response = self.client.post(url, produit_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Produit.objects.count(), 1)

class AcheteurTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='acheteur', password='testpassword123')
        self.acheteur = Acheteur.objects.create(user_ptr=self.user, telephone='1234567890', adresse='123 Buyer Street')

    def test_passer_commande(self):
        self.client.force_authenticate(user=self.user)
        agriculteur = Agriculteur.objects.create(user_ptr=User.objects.create_user(username='farmer', password='testpassword123'), telephone='1234567890', adresse='123 Farm Road')
        produit = Produit.objects.create(agriculteur=agriculteur, nom='Tomates', description='Tomates bio', prix=10.0, quantite_disponible=100, categorie='Légumes')

        url = reverse('commande-list')
        commande_data = {
            'acheteur': self.acheteur.id_user,
            'produits': [produit.id_produit],
            'quantites': [10]
        }
        response = self.client.post(url, commande_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Commande.objects.count(), 1)

class ProduitTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='agriculteur', password='testpassword123')
        self.agriculteur = Agriculteur.objects.create(user_ptr=self.user, telephone='1234567890', adresse='123 Farm Road')
        self.produit = Produit.objects.create(agriculteur=self.agriculteur, nom='Tomates', description='Tomates bio', prix=10.0, quantite_disponible=100, categorie='Légumes')

    def test_list_produits(self):
        url = reverse('produit-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class CommandeTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='acheteur', password='testpassword123')
        self.acheteur = Acheteur.objects.create(user_ptr=self.user, telephone='1234567890', adresse='123 Buyer Street')
        self.agriculteur = Agriculteur.objects.create(user_ptr=User.objects.create_user(username='farmer', password='testpassword123'), telephone='1234567890', adresse='123 Farm Road')
        self.produit = Produit.objects.create(agriculteur=self.agriculteur, nom='Tomates', description='Tomates bio', prix=10.0, quantite_disponible=100, categorie='Légumes')
        self.commande = Commande.objects.create(acheteur=self.acheteur)
        CommandeProduit.objects.create(commande=self.commande, produit=self.produit, quantite=10)

    def test_valider_commande(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('commande-detail', args=[self.commande.id_commande])
        response = self.client.patch(url, {'statut': 'Confirmée'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Commande.objects.get(id_commande=self.commande.id_commande).statut, 'Confirmée')

class PaiementTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='acheteur', password='testpassword123')
        self.acheteur = Acheteur.objects.create(user_ptr=self.user, telephone='1234567890', adresse='123 Buyer Street')
        self.commande = Commande.objects.create(acheteur=self.acheteur)
        self.paiement = Paiement.objects.create(commande=self.commande, montant=100.0, mode_paiement='Mobile Money')

    def test_effectuer_paiement(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('paiement-detail', args=[self.paiement.id_paiement])
        response = self.client.patch(url, {'statut': 'Validé'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Paiement.objects.get(id_paiement=self.paiement.id_paiement).statut, 'Validé')

class MessagerieTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create_user(username='user1', password='testpassword123')
        self.user2 = User.objects.create_user(username='user2', password='testpassword123')
        self.message = Messagerie.objects.create(expediteur=self.user1, destinataire=self.user2, contenu='Hello!')

    def test_envoyer_message(self):
        self.client.force_authenticate(user=self.user1)
        url = reverse('messagerie-list')
        message_data = {
            'expediteur': self.user1.id_user,
            'destinataire': self.user2.id_user,
            'contenu': 'Hi there!'
        }
        response = self.client.post(url, message_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Messagerie.objects.count(), 2)

class AvisTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='acheteur', password='testpassword123')
        self.acheteur = Acheteur.objects.create(user_ptr=self.user, telephone='1234567890', adresse='123 Buyer Street')
        self.agriculteur = Agriculteur.objects.create(user_ptr=User.objects.create_user(username='farmer', password='testpassword123'), telephone='1234567890', adresse='123 Farm Road')
        self.produit = Produit.objects.create(agriculteur=self.agriculteur, nom='Tomates', description='Tomates bio', prix=10.0, quantite_disponible=100, categorie='Légumes')
        self.avis = Avis.objects.create(acheteur=self.acheteur, produit=self.produit, note=5, commentaire='Excellent produit!')

    def test_laisser_avis(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('avis-list')
        avis_data = {
            'acheteur': self.acheteur.id_user,
            'produit': self.produit.id_produit,
            'note': 4,
            'commentaire': 'Très bon produit!'
        }
        response = self.client.post(url, avis_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Avis.objects.count(), 2)