---
description: Utilisez la page Serveurs de l’outil d’administration des Audiences Manager pour créer un serveur S3 ou modifier un serveur existant.
seo-description: Use the Servers page in the Audience Manager Admin tool to create a new S3 server or to edit an existing server.
seo-title: Create or Edit an S3 Server
title: Création ou modification d’un serveur S3
uuid: 94fee787-eb26-45aa-b602-d61ab12969ea
exl-id: 89310de0-e24e-4d4b-8171-56faf0b441f6
source-git-commit: 79415eba732c2a6d50f04124774664f788ccc78c
workflow-type: tm+mt
source-wordcount: '207'
ht-degree: 7%

---

# Création ou modification d’un serveur S3 {#create-or-edit-an-s-server}

Utilisez la page [!UICONTROL Servers] de l’outil d’administration des Audiences Manager pour créer un nouveau serveur [!DNL S3] ou modifier un serveur existant.

>[!NOTE]
>
>Vous devez disposer du rôle [!UICONTROL DEXADMIN] pour créer de nouveaux serveurs ou modifier des serveurs existants.

1. Pour créer un nouveau serveur, cliquez sur **[!UICONTROL Servers]** > **[!UICONTROL Create Server]**. Pour éditer un serveur existant, cliquez sur le serveur de votre choix dans la colonne **[!UICONTROL Label]**.
1. Indiquez le libellé souhaité pour ce serveur.
1. Dans la liste déroulante **[!UICONTROL Protocol]**, sélectionnez le protocole souhaité : **[!UICONTROL S3]**.

   >[!NOTE]
   >
   >Nous vous recommandons d’utiliser [!DNL Amazon S3] comme méthode pour obtenir des fichiers à partir de et envoyer des fichiers aux partenaires. [!DNL Amazon S3] fournit une interface de services web simple qui peut être utilisée pour stocker et récupérer n’importe quelle quantité de données, à tout moment, de n’importe où sur le web. Pour plus d’informations, voir [À propos d’Amazon S3](https://experienceleague.adobe.com/docs/audience-manager/user-guide/reference/amazon-s3.html) dans le *Guide de l’utilisateur de l’Audience Manager*.

1. Renseignez les champs suivants :

   * **[!UICONTROL Account]:** indiquez le  [!DNL S3] compte de votre choix.
   * **[!UICONTROL Bucket]:** indiquez le  [!DNL S3] compartiment de votre choix.
   * **[!UICONTROL Directory]:** indiquez le  [!DNL S3] répertoire souhaité.
   * **[!UICONTROL Access Key]:** spécifiez la clé  [!DNL S3] d’accès souhaitée.
   * **[!UICONTROL Secret Key]:** spécifiez la clé  [!DNL S3] secrète de votre choix.

1. Cliquez sur **[!UICONTROL Create]** si vous créez un nouveau serveur ou sur **[!UICONTROL Update]** si vous modifiez un serveur existant.
