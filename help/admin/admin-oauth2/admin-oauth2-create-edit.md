---
description: Utilisez la page Clients OAuth2 pour afficher la liste des clients OAuth2 dans votre configuration d’Audience Manager. Vous pouvez modifier ou supprimer des clients existants ou créer de nouveaux clients, à condition que les rôles utilisateur appropriés soient attribués à vous.
seo-description: Use the OAuth2 Clients page to view a list of OAuth2 clients in your Audience Manager configuration. You can edit or delete existing clients or create new clients, providing that you have the appropriate user roles assigned.
seo-title: OAuth2 Clients
title: Clients OAuth2
uuid: 3e654053-fb2f-4d8f-a53c-b5c3b8dbdaaa
exl-id: 993eae04-02e8-4554-a6fe-cf599053bfc9
source-git-commit: 79415eba732c2a6d50f04124774664f788ccc78c
workflow-type: tm+mt
source-wordcount: '550'
ht-degree: 1%

---

# Clients OAuth2 {#oauth-clients}

Utilisez la page [!UICONTROL OAuth2 Clients] pour afficher une liste de clients [!UICONTROL OAuth2] dans votre configuration [!DNL Audience Manager]. Vous pouvez modifier ou supprimer des clients existants ou créer de nouveaux clients, à condition que les rôles utilisateur appropriés soient attribués à vous.

## Présentation {#overview}

<!-- c_oauth.xml -->

>[!NOTE]
>
>Assurez-vous que votre client lit la documentation [OAuth2](https://experienceleague.adobe.com/docs/audience-manager/user-guide/api-and-sdk-code/rest-apis/aam-api-getting-started.html?lang=fr#oauth) dans le Guide de l’utilisateur d’Audience Manager.

[!DNL OAuth2] est une norme ouverte d’autorisation d’accorder un accès délégué sécurisé aux ressources [!DNL Audience Manager] pour le compte d’un propriétaire de ressource.

![](assets/oauth.png)

Vous pouvez trier chaque colonne par ordre croissant ou décroissant en cliquant sur l’en-tête de la colonne de votre choix.

Utilisez la zone [!UICONTROL Search] ou les commandes de pagination au bas de la liste pour trouver le client souhaité.

## Création ou modification d’un client OAuth2 {#create-edit-client}

<!-- t_create_edit_auth.xml -->

Utilisez la page [!UICONTROL OAuth2 Clients] de l&#39;outil Audience Manager [!UICONTROL Admin] pour créer un client [!UICONTROL Oauth2] ou modifier un client existant.

1. Pour créer un client [!UICONTROL OAuth2], cliquez sur **[!UICONTROL OAuth2 Clients]** > **[!UICONTROL Add OAuth2 Client]**. Pour modifier un client [!UICONTROL OAuth2] existant, cliquez sur le client souhaité dans la colonne **[!UICONTROL Client ID]**.
1. Indiquez le nom souhaité pour ce client [!UICONTROL OAuth2]. Notez qu’il s’agit d’un nom pour l’enregistrement uniquement.
1. Indiquez l’adresse électronique du client [!UICONTROL OAuth2]. Il existe une limite d’une adresse email.
1. Dans la liste déroulante **[!UICONTROL Partner]**, sélectionnez le partenaire de votre choix.
1. Dans la zone **[!UICONTROL Client ID]**, indiquez l’ID de votre choix. Il s’agit de la valeur utilisée lors de l’envoi de requêtes [!DNL API]. Le préfixe est automatiquement renseigné lorsque vous commencez à saisir une fois que vous avez sélectionné un [!UICONTROL Partner] dans la liste déroulante de l’étape précédente. Le format correct est &lt; *`partner subdomain`*> - &lt; *`Audience Manager username`*>.
1. Cochez ou désélectionnez la case **[!UICONTROL Restrict to Partner Users]** selon vos besoins. Si cette case est cochée, l’utilisateur doit être un utilisateur [!DNL Audience Manager] répertorié pour le partenaire sélectionné. Il est recommandé de sélectionner cette option.
1. Dans la section **[!UICONTROL Scope]** , cochez ou décochez les cases **[!UICONTROL Read]** et **[!UICONTROL Write]** selon vos besoins.
1. Dans la section **[!UICONTROL Grant Type]** , sélectionnez les moyens d’autorisation souhaités. Nous vous recommandons d’utiliser les paramètres par défaut des options [!UICONTROL Password] et [!UICONTROL Refresh-token] .

   * **[!UICONTROL Implicit]** : si vous sélectionnez cette option, la zone [!UICONTROL Redirect URI] est activée. Un jeton d’accès automatique est attribué à l’utilisateur après son authentification. Il est immédiatement envoyé à la redirection [!DNL URI].
   * **[!UICONTROL Authorization Code]** : si vous sélectionnez cette option, la zone [!UICONTROL Redirect URI] est activée. L’utilisateur est renvoyé au client après son authentification et est ensuite envoyé à la redirection [!DNL URI].
   * **[!UICONTROL Password]** : l’utilisateur est authentifié avec un mot de passe saisi par l’utilisateur plutôt qu’avec une tentative de validation automatique via un serveur d’autorisation.
   * **[!UICONTROL Refresh_token]** : utilisé pour actualiser un jeton d’accès expiré pendant une longue période.

1. Dans la zone **[!UICONTROL Redirect URI]**, indiquez le [!DNL URI] souhaité. Cette option est activée uniquement si vous sélectionnez les types d’octroi **[!UICONTROL Implicit]** et **[!UICONTROL Authorization_code]**. La zone **[!UICONTROL Redirect URI]** vous permet de spécifier une valeur [!DNL URI] acceptable, séparée par des virgules. Il s’agit de l’ [!DNL URI] vers lequel un utilisateur d’un client est redirigé après avoir approuvé le client pour l’accès à [!DNL API].
1. Spécifiez le délai d’expiration souhaité (en secondes) pour l’accès et l’actualisation de l’expiration du jeton.

   * **[!UICONTROL Access Token Expiration Time]** : nombre de secondes pendant lesquelles un jeton d’accès est valide après avoir été émis. Peut être nul pour utiliser la valeur par défaut de la plateforme (12 heures). La valeur -1 peut également indiquer que le jeton d’accès n’expire pas.
   * **[!UICONTROL Refresh Token Expiration Time]** : nombre de secondes pendant lesquelles un jeton d’actualisation est valide après avoir été émis. Peut être nul pour utiliser la valeur par défaut de la plateforme (30 jours).

1. Cliquez sur **[!UICONTROL Save]**.

Pour supprimer un client [!UICONTROL OAuth2], cliquez sur **[!UICONTROL OAuth2 Clients]**, puis sur ![](assets/icon_delete.png) dans la colonne **[!UICONTROL Actions]** correspondant au client souhaité.

>[!MORELIKETHIS]
>
>* [Configuration requise et recommandations pour l’API](../admin-oauth2/aam-admin-api-requirements.md)
