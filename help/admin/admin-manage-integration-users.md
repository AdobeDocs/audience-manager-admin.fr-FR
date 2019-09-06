---
description: Utilisez la page Utilisateurs d'intégration pour afficher la liste des utilisateurs de votre configuration Audience Manager. Vous pouvez modifier ou supprimer des utilisateurs existants ou créer des utilisateurs, à condition de disposer des rôles utilisateur appropriés.
seo-description: Utilisez la page Utilisateurs d'intégration pour afficher la liste des utilisateurs de votre configuration Audience Manager. Vous pouvez modifier ou supprimer des utilisateurs existants ou créer des utilisateurs, à condition de disposer des rôles utilisateur appropriés.
seo-title: Utilisateurs d'intégration
title: Utilisateurs d'intégration
uuid: 13 dcb 3 fb -4561-409 c -84 da -943 d 0 d 390 cf 3
translation-type: tm+mt
source-git-commit: 10adb6b06160f5a5c4068483b407e5798fc10150

---


# Utilisateurs d'intégration {#integration-users}

Utilisez [!UICONTROL Integration Users] la page pour afficher la liste des utilisateurs de votre configuration Audience Manager. Vous pouvez modifier ou supprimer des utilisateurs existants ou créer des utilisateurs, à condition de disposer des rôles utilisateur appropriés.

<!-- c_integration_users.xml -->

Vous pouvez trier chaque colonne par ordre croissant ou décroissant en cliquant sur l'en-tête de la colonne concernée.
Utilisez [!UICONTROL Search] la zone ou les commandes de pagination au bas de la liste pour trouver l'utilisateur souhaité.

## Création ou modification d'un utilisateur {#create-edit-user}

Utilisez [!UICONTROL Integration Users] la page de l'outil Audience Manager [!UICONTROL Admin] pour créer un utilisateur ou pour modifier le compte d'un utilisateur existant.

<!-- t_create_user.xml -->

>[!NOTE]
>
>Vous devez disposer du [!UICONTROL CREATE_USER] rôle pour créer de nouveaux utilisateurs. Vous devez disposer du [!UICONTROL EDIT_USER] rôle pour modifier les utilisateurs existants.

1. Pour créer un utilisateur, cliquez **[!UICONTROL Integration Users]** sur &gt; **[!UICONTROL Create a New User]**. Pour modifier un utilisateur existant, cliquez sur l'utilisateur de votre choix dans **[!UICONTROL Username]** la colonne.
2. Renseignez les champs suivants :
   * **[!UICONTROL First Name]**: (Obligatoire) Indiquez le prénom de l'utilisateur.
   * **[!UICONTROL Last Name]**: (Obligatoire) Indiquez le nom de l'utilisateur.
   * **[!UICONTROL Username]**: (Obligatoire) Indiquez le nom d'utilisateur de l'utilisateur.
   * **[!UICONTROL Email Address]**: (Obligatoire) Indiquez l'adresse électronique de l'utilisateur.
   * **[!UICONTROL Phone Number]**: Indiquez le numéro de téléphone de l'utilisateur.
   * **[!UICONTROL IMS ID]**: Spécifiez [!UICONTROL Internet Messaging Service ID]l'utilisateur.
   * **[!UICONTROL User Roles]**: Sélectionnez les rôles d'utilisateur souhaités :
      * **[!UICONTROL DEXADMIN]**: Permet aux administrateurs d'effectuer des tâches dans [!UICONTROL Admin] l'outil Audience Manager. Si vous ne sélectionnez pas cette option, vous pouvez choisir des rôles individuels. Ces rôles permettent aux utilisateurs d'effectuer des tâches à l'aide [!DNL API] d'appels, mais pas dans l'outil Admin.
      * **[!UICONTROL CREATE_USERS]**: permet aux utilisateurs de créer des utilisateurs à l'aide d' [!DNL API] un appel.
      * **[!UICONTROL DELETE_USERS]**: permet aux utilisateurs de supprimer des utilisateurs existants à l'aide d' [!DNL API] un appel.
      * **[!UICONTROL EDIT_USERS]**: permet aux utilisateurs de modifier des utilisateurs existants à l'aide d' [!DNL API] un appel.
      * **[!UICONTROL VIEW_USERS]**: Permet aux utilisateurs d'afficher d'autres utilisateurs dans votre configuration Audience Manager à l'aide d' [!DNL API] un appel.
      * **[!UICONTROL CREATE_PARTNERS]**: Permet aux utilisateurs de créer des partenaires Audience Manager à l'aide d' [!DNL API] un appel.
      * **[!UICONTROL DELETE_PARTNERS]**: permet aux utilisateurs de supprimer les partenaires Audience Manager à l'aide d' [!DNL API] un appel.
      * **[!UICONTROL EDIT_PARTNERS]**: permet aux utilisateurs de modifier les partenaires Audience Manager à l'aide d' [!DNL API] un appel.
      * **[!UICONTROL VIEW_PARNTERS]**: permet aux utilisateurs d'afficher les partenaires Audience Manager à l'aide d' [!DNL API] un appel.
   * **Etat :** Sélectionnez **[!UICONTROL Active]** cette option pour transformer cet utilisateur en utilisateur Audience Manager activé.
3. Cliquez sur **[!UICONTROL Submit]**.

## Delete a User {#delete-user}

Utilisez [!UICONTROL Integration Users] la page de l'outil Audience Manager [!UICONTROL Admin] pour supprimer un utilisateur existant.

<!-- t_delete_user.xml -->

>[!NOTE]
>
>Vous devez disposer du **[!UICONTROL DELETE_USER]** rôle pour créer de nouveaux utilisateurs.

1. Cliquez sur **[!UICONTROL Integration Users]**.
2. Cliquez ![](assets/icon_delete.png) dans la **[!UICONTROL Actions]** colonne de l'utilisateur souhaité.
3. Cliquez sur **[!UICONTROL OK]pour confirmer la suppression.**