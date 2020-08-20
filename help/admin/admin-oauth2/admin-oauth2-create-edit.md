---
description: Utilisez la page Clients OAuth2 pour vue d’une liste de clients OAuth2 dans votre configuration d’Audience Manager. Vous pouvez modifier ou supprimer des clients existants ou créer de nouveaux clients, à condition que les rôles d’utilisateur appropriés vous soient attribués.
seo-description: Utilisez la page Clients OAuth2 pour vue d’une liste de clients OAuth2 dans votre configuration d’Audience Manager. Vous pouvez modifier ou supprimer des clients existants ou créer de nouveaux clients, à condition que les rôles d’utilisateur appropriés vous soient attribués.
seo-title: Clients OAuth2
title: Clients OAuth2
uuid: 3e654053-fb2f-4d8f-a53c-b5c3b8dbdaaa
translation-type: tm+mt
source-git-commit: 0ee7aa9c13f1b9b8fd64dddff4e52d101055e77c
workflow-type: tm+mt
source-wordcount: '596'
ht-degree: 2%

---


# Clients OAuth2 {#oauth-clients}

Utilisez la [!UICONTROL OAuth2 Clients] page pour vue d&#39;une liste de [!UICONTROL OAuth2] clients dans votre [!DNL Audience Manager] configuration. Vous pouvez modifier ou supprimer des clients existants ou créer de nouveaux clients, à condition que les rôles d’utilisateur appropriés vous soient attribués.

## Présentation {#overview}

<!-- c_oauth.xml -->

>[!NOTE]
>
>Assurez-vous que votre client lit la documentation [OAuth2](https://docs.adobe.com/content/help/en/audience-manager/user-guide/api-and-sdk-code/rest-apis/aam-api-getting-started.html#oauth) dans le Guide de l’utilisateur de l’Audience Manager.

[!DNL OAuth2] est une norme ouverte pour l&#39;autorisation de fournir un accès délégué sécurisé aux [!DNL Audience Manager] ressources pour le compte d&#39;un propriétaire de ressources.

![](assets/oauth.png)

Vous pouvez trier chaque colonne par ordre croissant ou décroissant en cliquant sur l’en-tête de la colonne de votre choix.

Utilisez la [!UICONTROL Search] zone ou les commandes de pagination au bas de la liste pour trouver le client souhaité.

## Création ou modification d’un client OAuth2 {#create-edit-client}

<!-- t_create_edit_auth.xml -->

Utilisez la [!UICONTROL OAuth2 Clients] page de l’outil d’Audience Manager [!UICONTROL Admin] pour créer un nouveau [!UICONTROL Oauth2] client ou pour modifier un client existant.

1. Pour créer un nouveau [!UICONTROL OAuth2] client, cliquez sur **[!UICONTROL OAuth2 Clients]** > **[!UICONTROL Add OAuth2 Client]**. Pour modifier un [!UICONTROL OAuth2] client existant, cliquez sur le client de votre choix dans la **[!UICONTROL Client ID]** colonne.
1. Indiquez le nom de ce [!UICONTROL OAuth2] client. Notez qu’il s’agit d’un nom pour l’enregistrement uniquement.
1. Indiquez l’adresse électronique du [!UICONTROL OAuth2] client. Il existe une limite d&#39;une adresse électronique.
1. Dans la liste **[!UICONTROL Partner]** déroulante, sélectionnez un partenaire.
1. Dans la **[!UICONTROL Client ID]** zone, indiquez l’identifiant de votre choix. Il s’agit de la valeur utilisée lors de l’envoi de [!DNL API] requêtes. Le préfixe est automatiquement renseigné lorsque vous début de saisir une valeur après avoir choisi une valeur dans la liste [!UICONTROL Partner] déroulante de l’étape précédente. Le format correct est &lt; *`partner subdomain`*> - &lt; *`Audience Manager username`*>.
1. Cochez ou désélectionnez la **[!UICONTROL Restrict to Partner Users]** case, selon vos besoins. Si cette case est cochée, l&#39;utilisateur doit être un [!DNL Audience Manager] utilisateur répertorié pour le partenaire sélectionné. Il est recommandé de sélectionner cette option.
1. Dans la **[!UICONTROL Scope]** section, activez ou désactivez les **[!UICONTROL Read]** cases à cocher et **[!UICONTROL Write]** les cases à cocher, selon vos besoins.
1. Dans la **[!UICONTROL Grant Type]** section, sélectionnez les moyens d’autorisation de votre choix. Nous vous recommandons d&#39;utiliser les paramètres par défaut des options [!UICONTROL Password] et [!UICONTROL Refresh-token] .

   * **[!UICONTROL Implicit]**: Si vous sélectionnez cette option, la [!UICONTROL Redirect URI] zone est activée. L’utilisateur reçoit un jeton d&#39;accès automatique après son authentification et est immédiatement envoyé à la redirection [!DNL URI].
   * **[!UICONTROL Authorization Code]**: Si vous sélectionnez cette option, la [!UICONTROL Redirect URI] zone est activée. L’utilisateur est renvoyé au client après avoir été authentifié, puis envoyé à la redirection [!DNL URI].
   * **[!UICONTROL Password]**: L’utilisateur est authentifié avec un mot de passe saisi par l’utilisateur plutôt qu’avec une tentative de validation automatique via un serveur d’autorisations.
   * **[!UICONTROL Refresh_token]**: Utilisé pour actualiser un jeton d&#39;accès expiré pendant une longue période.

1. Dans la **[!UICONTROL Redirect URI]** zone, indiquez la valeur [!DNL URI]. Cette option est activée uniquement si vous sélectionnez les types **[!UICONTROL Implicit]** et **[!UICONTROL Authorization_code]** d’octroi. La **[!UICONTROL Redirect URI]** zone vous permet de spécifier une valeur séparée par des virgules de [!DNL URI] valeurs acceptables. Il s’agit [!DNL URI] d’un utilisateur auquel un client est redirigé après avoir approuvé le client pour [!DNL API] accès.
1. Spécifiez la durée d’expiration souhaitée (en secondes) pour l’accès et l’actualisation de l’expiration du jeton.

   * **[!UICONTROL Access Token Expiration Time]**: Nombre de secondes pendant lesquelles un jeton d&#39;accès est valide après avoir été émis. Peut être nul pour utiliser la plate-forme par défaut (12 heures). Peut également être égal à -1 pour indiquer que le jeton d&#39;accès n’expire pas.
   * **[!UICONTROL Refresh Token Expiration Time]**: Nombre de secondes pendant lesquelles un jeton d’actualisation est valide après avoir été émis. Peut être nul pour utiliser la plate-forme par défaut (30 jours).

1. Cliquez sur **[!UICONTROL Save]**.

Pour supprimer un [!UICONTROL OAuth2] client, cliquez sur **[!UICONTROL OAuth2 Clients]**, puis sur ![](assets/icon_delete.png) **[!UICONTROL Actions]** la colonne correspondant au client souhaité.

>[!MORELIKETHIS]
>
>* [Configuration requise et recommandations pour l’API](../admin-oauth2/aam-admin-api-requirements.md)

