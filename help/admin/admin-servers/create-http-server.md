---
description: Utilisez la page Serveurs de l’outil d’administration des Audiences Manager pour créer un serveur HTTP ou pour modifier un serveur existant.
seo-description: Utilisez la page Serveurs de l’outil d’administration des Audiences Manager pour créer un serveur HTTP ou pour modifier un serveur existant.
seo-title: Création ou modification d’un serveur HTTP
title: Création ou modification d’un serveur HTTP
uuid: 1ef0e751-e239-4dc6-a4f6-73cc05686807
translation-type: tm+mt
source-git-commit: d518ba4011f203a7d450ce76d8c1924f7d73a815
workflow-type: tm+mt
source-wordcount: '329'
ht-degree: 7%

---


# Création ou modification d’un serveur HTTP {#create-or-edit-an-http-server}

Utilisez la [!UICONTROL Servers] page de l’outil d’administration des Audiences Manager pour créer un serveur HTTP ou pour modifier un serveur existant.

>[!NOTE]
>
>Vous devez avoir le [!UICONTROL DEXADMIN] rôle pour créer de nouveaux serveurs ou modifier des serveurs existants.

1. Pour créer un nouveau serveur, sélectionnez **[!UICONTROL Servers]** > **[!UICONTROL Create Server]**. Pour modifier un serveur existant, cliquez sur le serveur de votre choix dans la **[!UICONTROL Label]** colonne.
1. Indiquez l’étiquette souhaitée pour ce serveur.
1. Dans la liste **[!UICONTROL Protocol]** déroulante, sélectionnez le protocole de votre choix : [!DNL HTTP].
1. Renseignez les champs suivants :

   * **[!UICONTROL Domain]:** Spécifiez le domaine (hôte) souhaité pour ce serveur.
   * **[!UICONTROL Port]:** Spécifiez le port souhaité pour ce serveur. Le port par défaut s’affiche pour chaque type de chiffrement. Si nécessaire, vous pouvez modifier le port par défaut.
   * **[!UICONTROL Maximum Users Per Request]:** Indiquez le nombre maximal d’utilisateurs par requête autorisée pour ce serveur.
   * **[!UICONTROL URL Prefix]:** Spécifiez le [!DNL URL] préfixe à utiliser pour ce serveur.
   * **[!UICONTROL Authentication URL]:** Spécifiez le [!UICONTROL Authentication URL] nom de ce `HTTP` serveur.
   * **[!UICONTROL Authentication]:** Spécifiez la méthode d’authentification de votre choix : **[!UICONTROL None]**, **[!UICONTROL Username/Password]** ou **[!UICONTROL SSH Key]**.
   * **[!UICONTROL HTTP Signature Header]:** Nom de l’ [!DNL HTTP] en-tête, fourni par le client, qui contient la clé de [!DNL HTTP] signature. La valeur par défaut est [!UICONTROL X-Signature], comme indiqué dans l’exemple ci-dessous :

      ```
      * Connected to partner.website.com (127.0.0.1) port 80 (#0)
      > POST /webpage HTTP/1.1
      > Host: partner.host.com
      > Accept: */*
      > Content-Type: application/json
      > Content-Length: 20
      > X-Signature: wxa2ByMWhhP328EvHQsVlOD5jTc=
      POST message content
      ```

   * **[!UICONTROL HTTP Signature Key]:** Clé utilisée pour signer la [!DNL HTTP] demande, fournie par le client.
   * **[!UICONTROL Show Signature Key]:** Active/désactive l’affichage de la signature dans le navigateur.
   * **[!UICONTROL HTTP Signature Encryption Method]:** Spécifiez la méthode utilisée pour chiffrer la signature. À utiliser [!UICONTROL SHA1] sauf si le client préfère le contraire.

   >[!NOTE]
   >
   >Si vous souhaitez activer l’authentification [OAuth 2.0 pour les transferts](https://docs.adobe.com/help/en/audience-manager/user-guide/implemenation-integration-guides/receiving-audience-data/real-time-outbound-transfers/oauth-in-outbound-transfers.html) de données en temps réel pour un partenaire, renseignez les champs comme dans le tableau ci-dessous. Les champs en *italique* doivent être remplis exactement comme dans le tableau.

   | Nom | Valeur |
   |---|---|
   | [!UICONTROL Label] | [!UICONTROL Server with OAuth 2.0 enabled] |
   | [!UICONTROL Protocol] | [!UICONTROL HTTP] |
   | [!UICONTROL Domain] | [!UICONTROL api.partner.com] |
   | [!UICONTROL Port] | [!UICONTROL 443] |
   | [!UICONTROL Maximum Users per Request] | [!UICONTROL 10] |
   | [!UICONTROL URL Prefix] | [!UICONTROL /segments/aam] |
   | [!UICONTROL Authentication URL] | [!UICONTROL api.partner.com/oauth2/token] |
   | [!UICONTROL Authentication] | [!UICONTROL Username/Password] |
   | [!UICONTROL Username] | [!UICONTROL *Autorisation*] |
   | [!UICONTROL Password] | your_password_here |
   | [!UICONTROL HTTP Signature Header] | [!UICONTROL Leave this field blank] |
   | [!UICONTROL HTTP Signature Key] | [!UICONTROL Leave this field blank] |
   | [!UICONTROL HTTP Signature Encryption Method] | [!UICONTROL None] |

1. Cliquez sur **[!UICONTROL Create]** si vous créez un nouveau serveur ou sur **[!UICONTROL Update]** si vous modifiez un serveur existant.
