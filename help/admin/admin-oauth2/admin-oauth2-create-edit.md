---
description: Utilisez la page Clients oauth 2 pour afficher la liste des clients oauth 2 dans votre configuration Audience Manager. Vous pouvez modifier ou supprimer des clients existants ou créer des clients, à condition de disposer des rôles utilisateur appropriés.
seo-description: Utilisez la page Clients oauth 2 pour afficher la liste des clients oauth 2 dans votre configuration Audience Manager. Vous pouvez modifier ou supprimer des clients existants ou créer des clients, à condition de disposer des rôles utilisateur appropriés.
seo-title: Clients oauth 2
title: Clients oauth 2
uuid: 3 e 654053-fb 2 f -4 d 8 f-a 53 c-b 5 c 3 b 8 dbdaaa
translation-type: tm+mt
source-git-commit: be661580da839ce6332a0ad827dec08e854abe54

---


# Clients oauth 2 {#oauth-clients}

Utilisez [!UICONTROL OAuth2 Clients] la page pour afficher la liste [!UICONTROL OAuth2] des clients dans [!DNL Audience Manager] votre configuration. Vous pouvez modifier ou supprimer des clients existants ou créer des clients, à condition de disposer des rôles utilisateur appropriés.

## Aperçu {#overview}

<!-- c_oauth.xml -->

>[!NOTE]
>
>Assurez-vous que votre client lit la documentation [oauth 2](https://docs.adobe.com/content/help/en/audience-manager/user-guide/api-and-sdk-code/rest-apis/aam-api-getting-started.html#oauth) dans le [! Guide de l'utilisateur DNL Audience Manager.

[!DNL OAuth2] est une norme ouverte d'autorisation pour fournir un accès délégué garanti aux [!DNL Audience Manager] ressources pour le compte d'un propriétaire de ressources.

![](assets/oauth.png)

Vous pouvez trier chaque colonne par ordre croissant ou décroissant en cliquant sur l'en-tête de la colonne concernée.

Utilisez [!UICONTROL Search] la zone ou les commandes de pagination au bas de la liste pour trouver le client souhaité.

## Création ou modification d'un client oauth 2 {#create-edit-client}

<!-- t_create_edit_auth.xml -->

Utilisez [!UICONTROL OAuth2 Clients] la page de l'outil Audience Manager [!UICONTROL Admin] pour créer un [!UICONTROL Oauth2] nouveau client ou pour modifier un client existant.

1. Pour créer [!UICONTROL OAuth2] un nouveau client, cliquez **[!UICONTROL OAuth2 Clients]** sur &gt; **[!UICONTROL Add OAuth2 Client]**. Pour modifier un [!UICONTROL OAuth2] client existant, cliquez sur le client de votre choix dans **[!UICONTROL Client ID]** la colonne.
1. Indiquez le nom de votre choix pour [!UICONTROL OAuth2] ce client. Notez qu'il s'agit uniquement d'un nom pour l'enregistrement.
1. Indiquez l'adresse électronique [!UICONTROL OAuth2] du client. Il existe une limite d'adresse électronique.
1. Dans la **[!UICONTROL Partner]** liste déroulante, sélectionnez un partenaire.
1. Dans **[!UICONTROL Client ID]** la zone, indiquez l'ID de votre choix. Il s'agit de la valeur utilisée lors de l'envoi [!DNL API] de requêtes. Le préfixe se renseigne automatiquement lorsque vous commencez à saisir une valeur après avoir choisi un [!UICONTROL Partner] élément dans la liste déroulante de l'étape précédente. Le format correct est &lt; *`partner subdomain`*&gt; - &lt; *`Audience Manager username`*&gt;.
1. Cochez ou décochez la **[!UICONTROL Restrict to Partner Users]** case suivant vos besoins. Si cette case est cochée, l'utilisateur doit être un [!DNL Audience Manager] utilisateur répertorié pour le partenaire sélectionné. Il est recommandé de sélectionner cette option.
1. Dans **[!UICONTROL Scope]** la section, activez ou désactivez les cases **[!UICONTROL Read]** et **[!UICONTROL Write]** les cases à cocher, selon vos besoins.
1. Dans **[!UICONTROL Grant Type]** la section, sélectionnez les moyens pour autoriser l'autorisation. Nous vous recommandons d'utiliser les paramètres et [!UICONTROL Password][!UICONTROL Refresh-token] options par défaut.

   * **[!UICONTROL Implicit]**: Si vous sélectionnez cette option, [!UICONTROL Redirect URI] la case est activée. L'utilisateur reçoit un jeton d'accès automatique après l'authentification et est immédiatement envoyé à la redirection [!DNL URI].
   * **[!UICONTROL Authorization Code]**: Si vous sélectionnez cette option, [!UICONTROL Redirect URI] la case est activée. L'utilisateur est renvoyé au client après son authentification puis envoyé à la redirection [!DNL URI].
   * **[!UICONTROL Password]**: L'utilisateur est authentifié avec un mot de passe saisi par l'utilisateur plutôt qu'une tentative de validation automatique via un serveur d'autorisations.
   * **[!UICONTROL Refresh_token]**: Utilisé pour actualiser un jeton d'accès expiré pendant une période prolongée.

1. Dans **[!UICONTROL Redirect URI]** la zone, indiquez le paramètre [!DNL URI]. Cette option est activée uniquement si vous sélectionnez **[!UICONTROL Implicit]** et **[!UICONTROL Authorization_code]** accordez les types. La **[!UICONTROL Redirect URI]** zone vous permet de spécifier une valeur séparée par des virgules de [!DNL URI] valeurs acceptables. Il s'agit de l' [!DNL URI] utilisateur d'un client qui est redirigé après l'approbation du client pour [!DNL API] l'accès.
1. Indiquez l'heure d'expiration souhaitée (en secondes) pour l'accès et l'expiration du jeton.

   * **[!UICONTROL Access Token Expiration Time]**: nombre de secondes pendant lesquelles un jeton d'accès est valide après leur publication. Peut être nul pour utiliser la plateforme par défaut (12 heures). Peut également être -1 pour indiquer que le jeton d'accès n'expire pas.
   * **[!UICONTROL Refresh Token Expiration Time]**: Nombre de secondes pendant lesquelles un jeton d'actualisation est valide après leur publication. Peut être nul pour utiliser la plateforme par défaut (30 jours).

1. Cliquez sur **[!UICONTROL Save]**.

Pour supprimer un [!UICONTROL OAuth2] client, cliquez sur **[!UICONTROL OAuth2 Clients]**, puis sur ![](assets/icon_delete.png) dans la **[!UICONTROL Actions]** colonne pour le client concerné.

>[!MORE_ LIKE_ THIS]
>
>* [Exigences et recommandations relatives à l'API](../admin-oauth2/aam-admin-api-requirements.md)

