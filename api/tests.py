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
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password': 'testpassword123',
            'telephone': '1234567890',
            'adresse': '123 Test Street'
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_create_utilisateur(self):
        url = reverse('utilisateurs-list')  # Updated to match the router URL
        response = self.client.post(url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)  # One already exists from setUp

    def test_login_utilisateur(self):
        url = reverse('jwt-create')  # Updated to match Djoser's JWT login URL
        login_data = {
            'email': 'test@example.com',
            'password': 'testpassword123'
        }
        response = self.client.post(url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)  # JWT returns 'access' and 'refresh' tokens

class AgriculteurTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            first_name='Agriculteur',
            last_name='Test',
            email='agriculteur@example.com',
            password='testpassword123',
            telephone='1234567890',
            adresse='123 Farm Road'
        )
        self.agriculteur = Agriculteur.objects.create(user=self.user)

    def test_publier_produit(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('produits-list')  # Updated to match the router URL
        produit_data = {
            'agriculteur': self.agriculteur.id,
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
        self.user = User.objects.create_user(
            first_name='Acheteur',
            last_name='Test',
            email='acheteur@example.com',
            password='testpassword123',
            telephone='1234567890',
            adresse='123 Buyer Street'
        )
        self.acheteur = Acheteur.objects.create(user=self.user)

    def test_passer_commande(self):
        self.client.force_authenticate(user=self.user)
        agriculteur_user = User.objects.create_user(
            first_name='Farmer',
            last_name='Test',
            email='farmer@example.com',
            password='testpassword123',
            telephone='1234567890',
            adresse='123 Farm Road'
        )
        agriculteur = Agriculteur.objects.create(user=agriculteur_user)
        produit = Produit.objects.create(
            agriculteur=agriculteur,
            nom='Tomates',
            description='Tomates bio',
            prix=10.0,
            quantite_disponible=100,
            categorie='Légumes'
        )

        url = reverse('commandes-list')  # Updated to match the router URL
        commande_data = {
            'acheteur': self.acheteur.id,
            'produits': [produit.id],
            'quantites': [10]
        }
        response = self.client.post(url, commande_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Commande.objects.count(), 1)

class ProduitTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            first_name='Agriculteur',
            last_name='Test',
            email='agriculteur@example.com',
            password='testpassword123',
            telephone='1234567890',
            adresse='123 Farm Road'
        )
        self.agriculteur = Agriculteur.objects.create(user=self.user)
        self.produit = Produit.objects.create(
            agriculteur=self.agriculteur,
            nom='Tomates',
            description='Tomates bio',
            prix=10.0,
            quantite_disponible=100,
            categorie='Légumes'
        )

    def test_list_produits(self):
        url = reverse('produits-list')  # Updated to match the router URL
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class CommandeTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            first_name='Acheteur',
            last_name='Test',
            email='acheteur@example.com',
            password='testpassword123',
            telephone='1234567890',
            adresse='123 Buyer Street'
        )
        self.acheteur = Acheteur.objects.create(user=self.user)
        agriculteur_user = User.objects.create_user(
            first_name='Farmer',
            last_name='Test',
            email='farmer@example.com',
            password='testpassword123',
            telephone='1234567890',
            adresse='123 Farm Road'
        )
        self.agriculteur = Agriculteur.objects.create(user=agriculteur_user)
        self.produit = Produit.objects.create(
            agriculteur=self.agriculteur,
            nom='Tomates',
            description='Tomates bio',
            prix=10.0,
            quantite_disponible=100,
            categorie='Légumes'
        )
        self.commande = Commande.objects.create(acheteur=self.acheteur)
        CommandeProduit.objects.create(commande=self.commande, produit=self.produit, quantite=10)

    def test_valider_commande(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('commandes-detail', args=[self.commande.id])  # Updated to match the router URL
        response = self.client.patch(url, {'statut': 'Confirmée'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Commande.objects.get(id=self.commande.id).statut, 'Confirmée')

class PaiementTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            first_name='Acheteur',
            last_name='Test',
            email='acheteur@example.com',
            password='testpassword123',
            telephone='1234567890',
            adresse='123 Buyer Street'
        )
        self.acheteur = Acheteur.objects.create(user=self.user)
        self.commande = Commande.objects.create(acheteur=self.acheteur)
        self.paiement = Paiement.objects.create(commande=self.commande, montant=100.0, mode_paiement='Mobile Money')

    def test_effectuer_paiement(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('paiements-detail', args=[self.paiement.id])  # Updated to match the router URL
        response = self.client.patch(url, {'statut': 'Validé'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Paiement.objects.get(id=self.paiement.id).statut, 'Validé')

class MessagerieTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create_user(
            first_name='User1',
            last_name='Test',
            email='user1@example.com',
            password='testpassword123',
            telephone='1234567890',
            adresse='123 Street'
        )
        self.user2 = User.objects.create_user(
            first_name='User2',
            last_name='Test',
            email='user2@example.com',
            password='testpassword123',
            telephone='1234567890',
            adresse='456 Street'
        )
        self.message = Messagerie.objects.create(expediteur=self.user1, destinataire=self.user2, contenu='Hello!')

    def test_envoyer_message(self):
        self.client.force_authenticate(user=self.user1)
        url = reverse('messagerie-list')  # Updated to match the router URL
        message_data = {
            'expediteur': self.user1.id,
            'destinataire': self.user2.id,
            'contenu': 'Hi there!'
        }
        response = self.client.post(url, message_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Messagerie.objects.count(), 2)

class AvisTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            first_name='Acheteur',
            last_name='Test',
            email='acheteur@example.com',
            password='testpassword123',
            telephone='1234567890',
            adresse='123 Buyer Street'
        )
        self.acheteur = Acheteur.objects.create(user=self.user)
        agriculteur_user = User.objects.create_user(
            first_name='Farmer',
            last_name='Test',
            email='farmer@example.com',
            password='testpassword123',
            telephone='1234567890',
            adresse='123 Farm Road'
        )
        self.agriculteur = Agriculteur.objects.create(user=agriculteur_user)
        self.produit = Produit.objects.create(
            agriculteur=self.agriculteur,
            nom='Tomates',
            description='Tomates bio',
            prix=10.0,
            quantite_disponible=100,
            categorie='Légumes'
        )
        self.avis = Avis.objects.create(acheteur=self.acheteur, produit=self.produit, note=5, commentaire='Excellent produit!')

    def test_laisser_avis(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('avis-list')  # Updated to match the router URL
        avis_data = {
            'acheteur': self.acheteur.id,
            'produit': self.produit.id,
            'note': 4,
            'commentaire': 'Très bon produit!'
        }
        response = self.client.post(url, avis_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Avis.objects.count(), 2)