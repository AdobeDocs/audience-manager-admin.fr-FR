---
description: Utilisez la page Clients OAuth2 pour afficher la liste des clients OAuth2 dans votre configuration Audience Manager. Vous pouvez modifier ou supprimer des clients existants ou créer de nouveaux clients, à condition que les rôles d’utilisateur appropriés soient attribués.
seo-description: Utilisez la page Clients OAuth2 pour afficher la liste des clients OAuth2 dans votre configuration Audience Manager. Vous pouvez modifier ou supprimer des clients existants ou créer de nouveaux clients, à condition que les rôles d’utilisateur appropriés soient attribués.
seo-title: Clients OAuth2
title: Clients OAuth2
uuid: 3e654053-fb2f-4d8f-a53c-b5c3b8dbda
translation-type: tm+mt
source-git-commit: 2998dc049971b2fac8c45ca6e3118ea607ae3f92

---


# Clients OAuth2 {#oauth-clients}

Utilisez la [!UICONTROL OAuth2 Clients] page pour afficher la liste des [!UICONTROL OAuth2] clients dans votre [!DNL Audience Manager] configuration. Vous pouvez modifier ou supprimer des clients existants ou créer de nouveaux clients, à condition que les rôles d’utilisateur appropriés soient attribués.

## Aperçu {#overview}

<!-- c_oauth.xml -->

>[!NOTE]
>
>Assurez-vous que votre client lit la documentation [OAuth2](https://docs.adobe.com/content/help/en/audience-manager/user-guide/api-and-sdk-code/rest-apis/aam-api-getting-started.html#oauth) dans le [!DNL Audience Manager User Guide.

[!DNL OAuth2] est une norme ouverte pour l'autorisation de fournir un accès délégué sécurisé aux [!DNL Audience Manager] ressources pour le compte d'un propriétaire de ressource.

![](assets/oauth.png)

Vous pouvez trier chaque colonne par ordre croissant ou décroissant en cliquant sur l’en-tête de la colonne de votre choix.

Utilisez la [!UICONTROL Search] zone ou les commandes de pagination au bas de la liste pour trouver le client souhaité.

## Création ou modification d’un client OAuth2 {#create-edit-client}

<!-- t_create_edit_auth.xml -->

Utilisez la [!UICONTROL OAuth2 Clients] page de l’outil Audience Manager [!UICONTROL Admin] pour créer un nouveau [!UICONTROL Oauth2] client ou modifier un client existant.

1. Pour créer un nouveau [!UICONTROL OAuth2] client, cliquez sur **[!UICONTROL OAuth2 Clients]** &gt; **[!UICONTROL Add OAuth2 Client]**. Pour modifier un [!UICONTROL OAuth2] client existant, cliquez sur le client souhaité dans la **[!UICONTROL Client ID]** colonne.
1. Indiquez le nom souhaité pour ce [!UICONTROL OAuth2] client. Notez qu’il s’agit d’un nom pour l’enregistrement uniquement.
1. Indiquez l’adresse électronique du [!UICONTROL OAuth2] client. Une adresse électronique est limitée.
1. Dans la liste **[!UICONTROL Partner]** déroulante, sélectionnez un partenaire.
1. Dans la **[!UICONTROL Client ID]** zone, indiquez l’ID de votre choix. Il s’agit de la valeur utilisée lors de l’envoi de [!DNL API] requêtes. Le préfixe est automatiquement renseigné lorsque vous commencez à saisir du texte après avoir choisi un préfixe [!UICONTROL Partner] dans la liste déroulante de l’étape précédente. Le format correct est &lt; *`partner subdomain`*&gt; - &lt; *`Audience Manager username`*&gt;.
1. Activez ou désactivez la **[!UICONTROL Restrict to Partner Users]** case à cocher, selon vos besoins. Si cette case est cochée, l’utilisateur doit être un [!DNL Audience Manager] utilisateur répertorié pour le partenaire sélectionné. Il est recommandé de sélectionner cette option.
1. Dans la **[!UICONTROL Scope]** section, activez ou désactivez les **[!UICONTROL Read]** cases à cocher et **[!UICONTROL Write]** les cases à cocher, selon vos besoins.
1. Dans la **[!UICONTROL Grant Type]** section, sélectionnez les moyens d’autorisation de votre choix. Nous vous recommandons d’utiliser les paramètres par défaut des [!UICONTROL Password] et [!UICONTROL Refresh-token] options.

   * **[!UICONTROL Implicit]**: Si vous sélectionnez cette option, la [!UICONTROL Redirect URI] zone est activée. Un jeton d’accès automatique est attribué à l’utilisateur après son authentification et est immédiatement envoyé à la redirection [!DNL URI].
   * **[!UICONTROL Authorization Code]**: Si vous sélectionnez cette option, la [!UICONTROL Redirect URI] zone est activée. L’utilisateur est renvoyé au client après avoir été authentifié, puis envoyé à la redirection [!DNL URI].
   * **[!UICONTROL Password]**: L’utilisateur est authentifié avec un mot de passe saisi par l’utilisateur plutôt qu’avec une tentative de validation automatique via un serveur d’autorisation.
   * **[!UICONTROL Refresh_token]**: Permet d’actualiser un jeton d’accès expiré pendant une période prolongée.

1. Dans la **[!UICONTROL Redirect URI]** zone, indiquez la valeur [!DNL URI]. Cette option n’est activée que si vous sélectionnez les types **[!UICONTROL Implicit]** et **[!UICONTROL Authorization_code]** d’octroi. La **[!UICONTROL Redirect URI]** zone vous permet de spécifier une valeur séparée par des virgules de [!DNL URI] valeurs acceptables. Il s’agit de l’ [!DNL URI] utilisateur auquel l’utilisateur d’un client est redirigé après avoir approuvé le client pour [!DNL API] accès.
1. Spécifiez le délai d’expiration souhaité (en secondes) pour l’accès et l’expiration du jeton d’actualisation.

   * **[!UICONTROL Access Token Expiration Time]**: nombre de secondes pendant lesquelles un jeton d’accès est valide après avoir été émis. Peut être nul pour utiliser la plate-forme par défaut (12 heures). Peut également être -1 pour indiquer que le jeton d’accès n’expire pas.
   * **[!UICONTROL Refresh Token Expiration Time]**: nombre de secondes pendant lesquelles un jeton d’actualisation est valide après son émission. Peut être nul pour utiliser la plate-forme par défaut (30 jours).

1. Cliquez sur **[!UICONTROL Save]**.

Pour supprimer un [!UICONTROL OAuth2] client, cliquez sur **[!UICONTROL OAuth2 Clients]**, puis sur ![](assets/icon_delete.png) **[!UICONTROL Actions]** la colonne correspondant au client souhaité.

>[!MORELIKETHIS]
>
>* [Configuration requise et recommandations pour l’API](../admin-oauth2/aam-admin-api-requirements.md)

