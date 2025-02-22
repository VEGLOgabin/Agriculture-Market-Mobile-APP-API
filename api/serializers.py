from rest_framework import serializers
from .models import Utilisateur, Agriculteur, Acheteur, Produit, Commande, CommandeProduit, Paiement, Messagerie, Avis

# Serializer for Utilisateur
class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'

# Serializer for Agriculteur
class AgriculteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agriculteur
        fields = '__all__'

# Serializer for Acheteur
class AcheteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acheteur
        fields = '__all__'

# Serializer for Produit
class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

# Serializer for Commande
class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'

# Serializer for CommandeProduit
class CommandeProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommandeProduit
        fields = '__all__'

# Serializer for Paiement
class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields = '__all__'

# Serializer for Messagerie
class MessagerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messagerie
        fields = '__all__'

# Serializer for Avis
class AvisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avis
        fields = '__all__'