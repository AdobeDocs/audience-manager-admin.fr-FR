---
description: Utilisez la page Serveurs de l'outil d'administration d'Audience Manager pour créer un serveur HTTP ou pour modifier un serveur existant.
seo-description: Utilisez la page Serveurs de l'outil d'administration d'Audience Manager pour créer un serveur HTTP ou pour modifier un serveur existant.
seo-title: Création ou modification d'un serveur HTTP
title: Création ou modification d'un serveur HTTP
uuid: 1 ef 0 e 751-e 239-4 dc 6-a 4 f 6-73 cc 05686807
translation-type: tm+mt
source-git-commit: 57d7a92265e565b6c411e4cfa5c579e40eb837b3

---


# Création ou modification d'un serveur HTTP {#create-or-edit-an-http-server}

Utilisez [!UICONTROL Servers] la page de l'outil d'administration d'Audience Manager pour créer un serveur HTTP ou pour modifier un serveur existant.

>[!NOTE]
>
>Vous devez disposer du [!UICONTROL DEXADMIN] rôle pour créer de nouveaux serveurs ou modifier des serveurs existants.

1. Pour créer un serveur, accédez **[!UICONTROL Servers]** à &gt; **[!UICONTROL Create Server]**. Pour modifier un serveur existant, cliquez sur le serveur de votre choix dans **[!UICONTROL Label]** la colonne.
1. Spécifiez une étiquette pour ce serveur.
1. Dans la liste **[!UICONTROL Protocol]** déroulante, sélectionnez le protocole de votre choix : [!DNL HTTP].
1. Renseignez les champs suivants :

   * **[!UICONTROL Domain]:** Spécifiez le domaine (hôte) de ce serveur.
   * **[!UICONTROL Port]:** Spécifiez le port de votre choix pour ce serveur. Le port par défaut s'affiche pour chaque type de chiffrement. Vous pouvez modifier le port par défaut, si nécessaire
   * **[!UICONTROL Maximum Users Per Request]:** Indiquez le nombre maximal d'utilisateurs par demande autorisée pour ce serveur.
   * **[!UICONTROL URL Prefix]:** Spécifiez le [!DNL URL] préfixe à utiliser pour ce serveur.
   * **[!UICONTROL Authentication URL]:** Spécifiez la [!UICONTROL Authentication URL] valeur de ce `HTTP` serveur.
   * **[!UICONTROL Authentication]:** Définissez la méthode d'authentification souhaitée : **[!UICONTROL None]**, **[!UICONTROL Username/Password]** ou **[!UICONTROL SSH Key]**.
   * **[!UICONTROL HTTP Signature Header]:** nom de l' [!DNL HTTP] en-tête, fourni par le client, qui contient la clé [!DNL HTTP] de signature. La valeur par défaut est [!UICONTROL X-Signature], comme illustré dans l'exemple ci-dessous :

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

   * **[!UICONTROL HTTP Signature Key]:** Clé utilisée pour signer [!DNL HTTP] la requête, fournie par le client.
   * **[!UICONTROL Show Signature Key]:** Permet d'activer ou de désactiver la signature dans le navigateur.
   * **[!UICONTROL HTTP Signature Encryption Method]:** Spécifiez la méthode utilisée pour chiffrer la signature. Sauf [!UICONTROL SHA1] si le client préfère autrement.
   >[!NOTE]
   >
   >Si vous souhaitez activer [l'authentification oauth 2.0 pour les transferts de données en temps réel](https://docs.adobe.com/help/en/audience-manager/user-guide/implemenation-integration-guides/receiving-audience-data/real-time-outbound-transfers/oauth-in-outbound-transfers.html) pour un partenaire, renseignez les champs comme dans le tableau ci-dessous. Les champs en *italiques* doivent être remplis exactement comme dans le tableau.

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
   | [!UICONTROL Username] | [!UICONTROL *Autorisation *] |
   | [!UICONTROL Password] | your_ password_ here |
   | [!UICONTROL HTTP Signature Header] | [!UICONTROL Leave this field blank] |
   | [!UICONTROL HTTP Signature Key] | [!UICONTROL Leave this field blank] |
   | [!UICONTROL HTTP Signature Encryption Method] | [!UICONTROL None] |

1. Cliquez **[!UICONTROL Create]** sur si vous créez un serveur ou si vous **[!UICONTROL Update]** modifiez un serveur existant.