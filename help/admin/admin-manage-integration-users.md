---
description: Utilisez la page Utilisateurs d’intégration pour afficher la liste des utilisateurs dans votre configuration d’Audience Manager. Vous pouvez modifier ou supprimer des utilisateurs existants ou en créer de nouveaux, à condition que les rôles utilisateur appropriés soient attribués à vous.
seo-description: Utilisez la page Utilisateurs d’intégration pour afficher la liste des utilisateurs dans votre configuration d’Audience Manager. Vous pouvez modifier ou supprimer des utilisateurs existants ou en créer de nouveaux, à condition que les rôles utilisateur appropriés soient attribués à vous.
seo-title: Utilisateurs d’intégration
title: Utilisateurs d’intégration
uuid: 13dcb3fb-4561-409c-84da-943d0d390cf3
translation-type: tm+mt
source-git-commit: 10adb6b06160f5a5c4068483b407e5798fc10150

---


# Utilisateurs d’intégration {#integration-users}

Utilisez la [!UICONTROL Integration Users] page pour afficher la liste des utilisateurs dans votre configuration d’Audience Manager. Vous pouvez modifier ou supprimer des utilisateurs existants ou en créer de nouveaux, à condition que les rôles utilisateur appropriés soient attribués à vous.

<!-- c_integration_users.xml -->

Vous pouvez trier chaque colonne par ordre croissant ou décroissant en cliquant sur l’en-tête de la colonne de votre choix.
Utilisez la [!UICONTROL Search] zone ou les commandes de pagination au bas de la liste pour trouver l’utilisateur souhaité.

## Créer ou modifier un utilisateur {#create-edit-user}

Utilisez la [!UICONTROL Integration Users] page de l’outil Audience Manager [!UICONTROL Admin] pour créer un nouvel utilisateur ou modifier le compte d’un utilisateur existant.

<!-- t_create_user.xml -->

>[!NOTE]
>
>Vous devez avoir le [!UICONTROL CREATE_USER] rôle pour créer de nouveaux utilisateurs. Vous devez avoir le [!UICONTROL EDIT_USER] rôle de modifier les utilisateurs existants.

1. Pour créer un utilisateur, cliquez sur **[!UICONTROL Integration Users]** &gt; **[!UICONTROL Create a New User]**. Pour modifier un utilisateur existant, cliquez sur l’utilisateur souhaité dans la **[!UICONTROL Username]** colonne.
2. Renseignez les champs suivants :
   * **[!UICONTROL First Name]**: (Obligatoire) Indiquez le prénom de l’utilisateur.
   * **[!UICONTROL Last Name]**: (Obligatoire) Indiquez le nom de famille de l’utilisateur.
   * **[!UICONTROL Username]**: (Obligatoire) Indiquez le nom d’utilisateur de l’utilisateur.
   * **[!UICONTROL Email Address]**: (Obligatoire) Indiquez l’adresse électronique de l’utilisateur.
   * **[!UICONTROL Phone Number]**: Indiquez le numéro de téléphone de l’utilisateur.
   * **[!UICONTROL IMS ID]**: Indiquez le nom de l’utilisateur [!UICONTROL Internet Messaging Service ID].
   * **[!UICONTROL User Roles]**: Sélectionnez les rôles utilisateur de votre choix :
      * **[!UICONTROL DEXADMIN]**: Permet aux administrateurs d’effectuer des tâches dans l’outil Audience Manager [!UICONTROL Admin] . Si vous ne sélectionnez pas cette option, vous pouvez choisir des rôles individuels. Ces rôles permettent aux utilisateurs d’effectuer des tâches à l’aide d’ [!DNL API] appels, mais pas dans l’outil d’administration.
      * **[!UICONTROL CREATE_USERS]**: Permet aux utilisateurs de créer des utilisateurs à l’aide d’un [!DNL API] appel.
      * **[!UICONTROL DELETE_USERS]**: Permet aux utilisateurs de supprimer des utilisateurs existants à l’aide d’un [!DNL API] appel.
      * **[!UICONTROL EDIT_USERS]**: Permet aux utilisateurs de modifier des utilisateurs existants à l’aide d’un [!DNL API] appel.
      * **[!UICONTROL VIEW_USERS]**: Permet aux utilisateurs d’afficher d’autres utilisateurs dans votre configuration Audience Manager à l’aide d’un [!DNL API] appel.
      * **[!UICONTROL CREATE_PARTNERS]**: Permet aux utilisateurs de créer des partenaires Audience Manager à l’aide d’un [!DNL API] appel.
      * **[!UICONTROL DELETE_PARTNERS]**: Permet aux utilisateurs de supprimer des partenaires Audience Manager à l’aide d’un [!DNL API] appel.
      * **[!UICONTROL EDIT_PARTNERS]**: Permet aux utilisateurs de modifier les partenaires d’Audience Manager à l’aide d’un [!DNL API] appel.
      * **[!UICONTROL VIEW_PARNTERS]**: Permet aux utilisateurs d’afficher les partenaires d’Audience Manager à l’aide d’un [!DNL API] appel.
   * **** État : Sélectionnez **[!UICONTROL Active]** cette option pour activer Audience Manager.
3. Cliquez sur **[!UICONTROL Submit]**.

## Delete a User {#delete-user}

Utilisez la [!UICONTROL Integration Users] page de l’outil Audience Manager [!UICONTROL Admin] pour supprimer un utilisateur existant.

<!-- t_delete_user.xml -->

>[!NOTE]
>
>Vous devez avoir le **[!UICONTROL DELETE_USER]** rôle pour créer de nouveaux utilisateurs.

1. Cliquez sur **[!UICONTROL Integration Users]**.
2. Cliquez ![](assets/icon_delete.png) dans la **[!UICONTROL Actions]** colonne de l’utilisateur souhaité.
3. Cliquez sur **[!UICONTROL OK]pour confirmer la suppression.**