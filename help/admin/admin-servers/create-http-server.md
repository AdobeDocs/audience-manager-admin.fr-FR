---
description: Utilisez la page Serveurs de l’outil d’administration des Audiences Manager pour créer un serveur HTTP ou modifier un serveur existant.
seo-description: Use the Servers page in the Audience Manager Admin tool to create a new HTTP server or to edit an existing server.
seo-title: Create or Edit an HTTP Server
title: Création ou modification d’un serveur HTTP
uuid: 1ef0e751-e239-4dc6-a4f6-73cc05686807
exl-id: 8b3dfb1e-2dee-4a05-835e-3c32643336bc
source-git-commit: c7c5da62b32f6a56152e1c09a965facfc601cade
workflow-type: tm+mt
source-wordcount: '302'
ht-degree: 6%

---

# Création ou modification d’un serveur HTTP {#create-or-edit-an-http-server}

Utilisez la page [!UICONTROL Servers] de l’outil d’administration des Audiences Manager pour créer un serveur HTTP ou modifier un serveur existant.

>[!NOTE]
>
>Vous devez disposer du rôle [!UICONTROL DEXADMIN] pour créer de nouveaux serveurs ou modifier des serveurs existants.

1. Pour créer un nouveau serveur, accédez à **[!UICONTROL Servers]** > **[!UICONTROL Create Server]**. Pour éditer un serveur existant, cliquez sur le serveur de votre choix dans la colonne **[!UICONTROL Label]**.
1. Indiquez le libellé souhaité pour ce serveur.
1. Dans la liste déroulante **[!UICONTROL Protocol]**, sélectionnez le protocole souhaité : [!DNL HTTP].
1. Renseignez les champs suivants :

   * **[!UICONTROL Domain]:** spécifiez le domaine (hôte) souhaité pour ce serveur.
   * **[!UICONTROL Port]:** indiquez le port souhaité pour ce serveur. Le port par défaut s’affiche pour chaque type de chiffrement. Si nécessaire, vous pouvez modifier le port par défaut.
   * **[!UICONTROL Maximum Users Per Request]:** indiquez le nombre maximal d’utilisateurs par demande autorisée pour ce serveur.
   * **[!UICONTROL URL Prefix]:** indiquez le  [!DNL URL] préfixe à utiliser pour ce serveur.
   * **[!UICONTROL Authentication URL]:** indiquez le  [!UICONTROL Authentication URL] pour ce  `HTTP` serveur.
   * **[!UICONTROL Authentication]:** indiquez la méthode d’authentification souhaitée :  **[!UICONTROL None]**,  **[!UICONTROL Username/Password]** ou  **[!UICONTROL SSH Key]**.
   * **[!UICONTROL HTTP Signature Header]:** nom de l’ [!DNL HTTP] en-tête, fourni par le client, qui contient la clé de  [!DNL HTTP] signature. La valeur par défaut est [!UICONTROL X-Signature], comme illustré dans l’exemple ci-dessous :

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

   * **[!UICONTROL HTTP Signature Key]:** clé utilisée pour signer la  [!DNL HTTP] demande, fournie par le client.
   * **[!UICONTROL Show Signature Key]:** basculez pour afficher ou non la signature dans le navigateur.
   * **[!UICONTROL HTTP Signature Encryption Method]:** indiquez la méthode de chiffrement de la signature. Utilisez [!UICONTROL SHA1] sauf si le client préfère le contraire.

   >[!NOTE]
   >
   >Si vous souhaitez activer l’authentification [OAuth 2.0 pour les transferts de données en temps réel](https://experienceleague.adobe.com/docs/audience-manager/user-guide/implementation-integration-guides/receiving-audience-data/real-time-outbound-transfers/oauth-in-outbound-transfers.html?lang=en) pour un partenaire, renseignez les champs comme dans le tableau ci-dessous. Les champs de *italics* doivent être renseignés exactement comme dans le tableau.

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
