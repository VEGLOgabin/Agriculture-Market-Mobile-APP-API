from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin,AbstractUser


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, password, email, telephone, adresse,is_active = True,  **kwargs):
        """
        Creates and saves a User with the given email and password.
        """
        email = self.normalize_email(email)
        if not email:
            raise ValueError('Users must have an email')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            telephone=telephone,
            adresse=adresse,
            is_staff=False, 
            is_admin=False,
            is_active = is_active,
            **kwargs
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
        

    def create_staffuser(self, first_name, last_name,password,email, telephone, adresse, is_active = True):

        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            telephone=telephone,
            adresse=adresse,
            password=password,
            is_staff=True,
            is_admin=False,
            is_active = is_active
        )
        return user
    
    def create_superuser(self, first_name, last_name, email, password, telephone, adresse, is_active = True):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            telephone=telephone,
            adresse=adresse,
            password=password,
            is_staff=True,
            is_admin=True,
            is_active = is_active
        )
        return user


# Custom User model (inherits from AbstractUser)
class Utilisateur(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', "telephone", "adresse"]

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'utilisateur'


# Agriculteur model 
class Agriculteur(models.Model):
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name="agriculteur")
    
    class Meta:
        db_table = 'agriculteur'
# Acheteur model
class Acheteur(models.Model):
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name="acheteur")

    class Meta:
        db_table = 'acheteur'


# Produit model
class Produit(models.Model):
    agriculteur = models.ForeignKey(Agriculteur, on_delete=models.CASCADE, related_name='produits')
    nom = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.FloatField()
    quantite_disponible = models.IntegerField()
    categorie = models.CharField(max_length=100)
    image = models.ImageField(upload_to='produits/', blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

    class Meta:
        db_table = 'produit'

# Commande model
class Commande(models.Model):
    STATUS_CHOICES = [
        ('En attente', 'En attente'),
        ('Confirmée', 'Confirmée'),
        ('Annulée', 'Annulée'),
        ('Livrée', 'Livrée'),
    ]
    acheteur = models.ForeignKey(Acheteur, on_delete=models.CASCADE, related_name='commandes')
    date_commande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=50, choices=STATUS_CHOICES, default='En attente')

    class Meta:
        db_table = 'commande'

# CommandeProduit model (for M:N relationship between Commande and Produit)
class CommandeProduit(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='produits_commandes')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()  

    class Meta:
        db_table = 'commande_produit'
        unique_together = ('commande', 'produit')

# Paiement model
class Paiement(models.Model):
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE, related_name='paiement')
    montant = models.FloatField()
    mode_paiement = models.CharField(max_length=50, choices=[('Mobile Money', 'Mobile Money'), ('Espèces', 'Espèces')])
    statut = models.CharField(max_length=50, default='En attente')


    def paiement_en_attente(self):
        self.statut = 'En attente'
        self.save()

    def effectuer_paiement(self):
        self.statut = 'Validé'
        self.save()

    def rembourser(self):
        self.statut = 'Remboursé'
        self.save()

    class Meta:
        db_table = 'paiement'

# Messagerie model
class Messagerie(models.Model):
    expediteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='messages_envoyes')
    destinataire = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='messages_recus')
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'messagerie'

# Avis model
class Avis(models.Model):
    # id_avis = models.AutoField(primary_key=True)
    acheteur = models.ForeignKey(Acheteur, on_delete=models.CASCADE, related_name='avis')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='avis')
    note = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    commentaire = models.TextField()
    date_avis = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'avis'