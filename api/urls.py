from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UtilisateurViewSet, AgriculteurViewSet, AcheteurViewSet, ProduitViewSet, CommandeViewSet, CommandeProduitViewSet, PaiementViewSet, MessagerieViewSet, AvisViewSet

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'utilisateurs', UtilisateurViewSet)
router.register(r'agriculteurs', AgriculteurViewSet)
router.register(r'acheteurs', AcheteurViewSet)
router.register(r'produits', ProduitViewSet)
router.register(r'commandes', CommandeViewSet)
router.register(r'commande-produits', CommandeProduitViewSet)
router.register(r'paiements', PaiementViewSet)
router.register(r'messagerie', MessagerieViewSet)
router.register(r'avis', AvisViewSet)

# Define URL patterns
urlpatterns = [
    path('', include(router.urls)),
]