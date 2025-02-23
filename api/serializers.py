from rest_framework import serializers
from .models import Utilisateur, Agriculteur, Acheteur, Produit, Commande, CommandeProduit, Paiement, Messagerie, Avis



# Base Serializer for Utilisateur (used for create/update)
class UtilisateurCreateUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Make password write-only

    class Meta:
        model = Utilisateur
        fields = ["first_name", "last_name", "email", "telephone", "adresse", "password"]

# List Serializer for Utilisateur (used for listing)
class UtilisateurListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ["first_name", "last_name", "email", "telephone", "adresse"]
        depth = 1  # Apply depth=1 for nested relationships

# Base Serializer for Agriculteur (used for create/update)
class AgriculteurCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agriculteur
        fields = '__all__'

# List Serializer for Agriculteur (used for listing)
class AgriculteurListSerializer(serializers.ModelSerializer):
    user = UtilisateurListSerializer()
    class Meta:
        model = Agriculteur
        fields = '__all__'
        depth = 1  # Apply depth=1 for nested relationships

# Base Serializer for Acheteur (used for create/update)
class AcheteurCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acheteur
        fields = '__all__'

# List Serializer for Acheteur (used for listing)
class AcheteurListSerializer(serializers.ModelSerializer):
    user = UtilisateurListSerializer()
    class Meta:
        model = Acheteur
        fields = '__all__'
        depth = 1  # Apply depth=1 for nested relationships

# Base Serializer for Produit (used for create/update)
class ProduitCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

# List Serializer for Produit (used for listing)
class ProduitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'
        depth = 1  # Apply depth=1 for nested relationships

# Base Serializer for Commande (used for create/update)
class CommandeCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'

# List Serializer for Commande (used for listing)
class CommandeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'
        depth = 1  # Apply depth=1 for nested relationships

# Base Serializer for CommandeProduit (used for create/update)
class CommandeProduitCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommandeProduit
        fields = '__all__'

# List Serializer for CommandeProduit (used for listing)
class CommandeProduitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommandeProduit
        fields = '__all__'
        depth = 1  # Apply depth=1 for nested relationships

# Base Serializer for Paiement (used for create/update)
class PaiementCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields = '__all__'

# List Serializer for Paiement (used for listing)
class PaiementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields = '__all__'
        depth = 1  # Apply depth=1 for nested relationships

# Base Serializer for Messagerie (used for create/update)
class MessagerieCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messagerie
        fields = '__all__'

# List Serializer for Messagerie (used for listing)
class MessagerieListSerializer(serializers.ModelSerializer):
    expediteur = UtilisateurListSerializer()
    destinataire = UtilisateurListSerializer()
    class Meta:
        model = Messagerie
        fields = '__all__'
        depth = 1  # Apply depth=1 for nested relationships

# Base Serializer for Avis (used for create/update)
class AvisCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avis
        fields = '__all__'

# List Serializer for Avis (used for listing)
class AvisListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avis
        fields = '__all__'
        depth = 1  # Apply depth=1 for nested relationships