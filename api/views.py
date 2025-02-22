from rest_framework import viewsets
from .models import Utilisateur, Agriculteur, Acheteur, Produit, Commande, CommandeProduit, Paiement, Messagerie, Avis
from .serializers import (
    UtilisateurCreateUpdateSerializer, UtilisateurListSerializer,
    AgriculteurCreateUpdateSerializer, AgriculteurListSerializer,
    AcheteurCreateUpdateSerializer, AcheteurListSerializer,
    ProduitCreateUpdateSerializer, ProduitListSerializer,
    CommandeCreateUpdateSerializer, CommandeListSerializer,
    CommandeProduitCreateUpdateSerializer, CommandeProduitListSerializer,
    PaiementCreateUpdateSerializer, PaiementListSerializer,
    MessagerieCreateUpdateSerializer, MessagerieListSerializer,
    AvisCreateUpdateSerializer, AvisListSerializer
)

# Utilisateur ViewSet
class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return UtilisateurListSerializer
        return UtilisateurCreateUpdateSerializer

# Agriculteur ViewSet
class AgriculteurViewSet(viewsets.ModelViewSet):
    queryset = Agriculteur.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return AgriculteurListSerializer
        return AgriculteurCreateUpdateSerializer

# Acheteur ViewSet
class AcheteurViewSet(viewsets.ModelViewSet):
    queryset = Acheteur.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return AcheteurListSerializer
        return AcheteurCreateUpdateSerializer

# Produit ViewSet
class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ProduitListSerializer
        return ProduitCreateUpdateSerializer

# Commande ViewSet
class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CommandeListSerializer
        return CommandeCreateUpdateSerializer

# CommandeProduit ViewSet
class CommandeProduitViewSet(viewsets.ModelViewSet):
    queryset = CommandeProduit.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CommandeProduitListSerializer
        return CommandeProduitCreateUpdateSerializer

# Paiement ViewSet
class PaiementViewSet(viewsets.ModelViewSet):
    queryset = Paiement.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return PaiementListSerializer
        return PaiementCreateUpdateSerializer

# Messagerie ViewSet
class MessagerieViewSet(viewsets.ModelViewSet):
    queryset = Messagerie.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return MessagerieListSerializer
        return MessagerieCreateUpdateSerializer

# Avis ViewSet
class AvisViewSet(viewsets.ModelViewSet):
    queryset = Avis.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return AvisListSerializer
        return AvisCreateUpdateSerializer