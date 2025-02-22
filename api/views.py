from rest_framework import viewsets
from .models import Utilisateur, Agriculteur, Acheteur, Produit, Commande, CommandeProduit, Paiement, Messagerie, Avis
from .serializers import UtilisateurSerializer, AgriculteurSerializer, AcheteurSerializer, ProduitSerializer, CommandeSerializer, CommandeProduitSerializer, PaiementSerializer, MessagerieSerializer, AvisSerializer

# ViewSet for Utilisateur
class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

# ViewSet for Agriculteur
class AgriculteurViewSet(viewsets.ModelViewSet):
    queryset = Agriculteur.objects.all()
    serializer_class = AgriculteurSerializer

# ViewSet for Acheteur
class AcheteurViewSet(viewsets.ModelViewSet):
    queryset = Acheteur.objects.all()
    serializer_class = AcheteurSerializer

# ViewSet for Produit
class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

# ViewSet for Commande
class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer

# ViewSet for CommandeProduit
class CommandeProduitViewSet(viewsets.ModelViewSet):
    queryset = CommandeProduit.objects.all()
    serializer_class = CommandeProduitSerializer

# ViewSet for Paiement
class PaiementViewSet(viewsets.ModelViewSet):
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer

# ViewSet for Messagerie
class MessagerieViewSet(viewsets.ModelViewSet):
    queryset = Messagerie.objects.all()
    serializer_class = MessagerieSerializer

# ViewSet for Avis
class AvisViewSet(viewsets.ModelViewSet):
    queryset = Avis.objects.all()
    serializer_class = AvisSerializer