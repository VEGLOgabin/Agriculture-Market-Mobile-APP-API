# Agricultural Marketplace API

This is a Django REST Framework (DRF) based API for an agricultural marketplace. The API allows users to manage various entities such as users, farmers, buyers, products, orders, payments, messaging, and reviews.

## Features

- **User Management**: Create, update, retrieve, and list users.
- **Farmer Management**: Manage farmers and their details.
- **Buyer Management**: Manage buyers and their details.
- **Product Management**: Create, update, retrieve, and list products.
- **Order Management**: Manage orders and their details.
- **Order Product Management**: Manage products associated with orders.
- **Payment Management**: Handle payments for orders.
- **Messaging**: Enable communication between users.
- **Reviews**: Allow users to leave reviews.

## Models

The API includes the following models:

- `Utilisateur`: Represents a user in the system.
- `Agriculteur`: Represents a farmer.
- `Acheteur`: Represents a buyer.
- `Produit`: Represents a product.
- `Commande`: Represents an order.
- `CommandeProduit`: Represents the association between an order and a product.
- `Paiement`: Represents a payment.
- `Messagerie`: Represents a message between users.
- `Avis`: Represents a review.

## Serializers

The API uses different serializers for listing and creating/updating entities:

- **Utilisateur**:
  - `UtilisateurListSerializer`: For listing and retrieving users.
  - `UtilisateurCreateUpdateSerializer`: For creating and updating users.

- **Agriculteur**:
  - `AgriculteurListSerializer`: For listing and retrieving farmers.
  - `AgriculteurCreateUpdateSerializer`: For creating and updating farmers.

- **Acheteur**:
  - `AcheteurListSerializer`: For listing and retrieving buyers.
  - `AcheteurCreateUpdateSerializer`: For creating and updating buyers.

- **Produit**:
  - `ProduitListSerializer`: For listing and retrieving products.
  - `ProduitCreateUpdateSerializer`: For creating and updating products.

- **Commande**:
  - `CommandeListSerializer`: For listing and retrieving orders.
  - `CommandeCreateUpdateSerializer`: For creating and updating orders.

- **CommandeProduit**:
  - `CommandeProduitListSerializer`: For listing and retrieving order products.
  - `CommandeProduitCreateUpdateSerializer`: For creating and updating order products.

- **Paiement**:
  - `PaiementListSerializer`: For listing and retrieving payments.
  - `PaiementCreateUpdateSerializer`: For creating and updating payments.

- **Messagerie**:
  - `MessagerieListSerializer`: For listing and retrieving messages.
  - `MessagerieCreateUpdateSerializer`: For creating and updating messages.

- **Avis**:
  - `AvisListSerializer`: For listing and retrieving reviews.
  - `AvisCreateUpdateSerializer`: For creating and updating reviews.

## ViewSets

The API uses Django REST Framework's `ModelViewSet` to handle CRUD operations for each model:

- `UtilisateurViewSet`: Handles operations for `Utilisateur`.
- `AgriculteurViewSet`: Handles operations for `Agriculteur`.
- `AcheteurViewSet`: Handles operations for `Acheteur`.
- `ProduitViewSet`: Handles operations for `Produit`.
- `CommandeViewSet`: Handles operations for `Commande`.
- `CommandeProduitViewSet`: Handles operations for `CommandeProduit`.
- `PaiementViewSet`: Handles operations for `Paiement`.
- `MessagerieViewSet`: Handles operations for `Messagerie`.
- `AvisViewSet`: Handles operations for `Avis`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/agricultural-marketplace-api.git
   cd agricultural-marketplace-api