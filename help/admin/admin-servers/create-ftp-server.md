---
description: Utilisez la page Serveurs de l’outil d’administration Audience Manager pour créer un serveur FTP ou modifier un serveur existant.
seo-description: Use the Servers page in the Audience Manager Admin tool to create a new FTP server or to edit an existing server.
seo-title: Create or Edit an FTP Server
title: Créer ou modifier un serveur FTP
uuid: 9273abb2-963d-4d83-bf5a-b3817f0b90e6
exl-id: 9eae4ecf-ccde-483a-ae53-1cbac033d8d6
TQID: https://experienceleague.adobe.com/vXm5k1APT6BVn0Ub7ntfDCnAdSfOWTLRo6ci-yK5cWk
product_v2:
  - id: df80eeb1-8d72-467e-b0df-9d51c7d3a0a1
source-git-commit: d2bed13a6ac7d38ae79b65d492b6de0ca6b6d488
workflow-type: tm+mt
source-wordcount: 397
ht-degree: 1%

---

# Créer ou modifier un serveur FTP {#create-or-edit-an-ftp-server}

Utilisez la page [!UICONTROL Servers] de l’outil d’administration Audience Manager pour créer un serveur FTP ou modifier un serveur existant.

>[!NOTE]
>
>Vous devez disposer du rôle [!UICONTROL DEXADMIN] pour pouvoir créer de nouveaux serveurs ou modifier des serveurs existants.

1. Pour créer un nouveau serveur, cliquez sur **[!UICONTROL Servers]** > **[!UICONTROL Create Server]**. Pour modifier un serveur existant, cliquez sur le serveur de votre choix dans la colonne **[!UICONTROL Label]**.
1. Spécifiez le libellé souhaité pour ce serveur.
1. Dans la liste déroulante **[!UICONTROL Protocol]** , sélectionnez le protocole souhaité : **FTP**.

   >[!NOTE]
   >
   >Nous vous recommandons d’utiliser la méthode [!DNL Amazon S3] pour récupérer des fichiers et les diffuser auprès des partenaires. [!DNL Amazon S3] fournit une interface de services web simple qui peut être utilisée pour stocker et récupérer n’importe quelle quantité de données, à tout moment et depuis n’importe quel emplacement sur le web. Pour plus d’informations, voir [À propos d’Amazon S3](https://experienceleague.adobe.com/docs/audience-manager/user-guide/reference/amazon-s3.html) dans le *Guide de l’utilisateur d’Audience Manager*.

1. Renseignez les champs suivants :

   * **[!UICONTROL Type]:** sélectionnez le type de chiffrement souhaité : **[!UICONTROL SFTP]** ou **[!UICONTROL FTPs/TLS]**.
   * **[!UICONTROL Domain]:** spécifiez le domaine (hôte) souhaité pour ce serveur.
   * **[!UICONTROL Port]:** spécifiez le port souhaité pour ce serveur. Le port par défaut s’affiche pour chaque type de chiffrement. Vous pouvez modifier le port par défaut, si nécessaire.
   * **[!UICONTROL Remote Path]:** spécifiez le chemin d’accès distant souhaité pour ce serveur. Si vous laissez ce champ vide, Audience Manager place les fichiers dans le répertoire par défaut.
   * **[!UICONTROL .tmp File Rename on Completion]:** activez cette option pour renommer le fichier `.tmp` à la fin de l’opération.
   * **[!UICONTROL Filename Suffix]:** spécifiez le texte à ajouter pour transférer les fichiers.
   * **[!UICONTROL Moved to When Finished]:** spécifiez le chemin d’accès à l’emplacement où vous souhaitez que le fichier de transfert soit déplacé une fois l’opération terminée.
   * **[!UICONTROL Authentication]:** spécifiez la méthode d’authentification du serveur souhaitée : **[!UICONTROL Username/Password]** ou **[!UICONTROL SSH Key]**.

   >[!NOTE]
   >
   >N’oubliez pas d’ajouter notre [!DNL IP] de [!DNL FTP] de sortie à votre liste d’adresses IP autorisées : **54.204.116.43**.

1. Pour l’authentification **[!UICONTROL SSH Key]** :

   >[!NOTE]
   >
   >Lors de la configuration de l’authentification par clé SSH, veillez à toujours générer les clés publiques et privées au format OpenSSH uniquement.

   1. Générez la paire de clés publique/privée à partir de n’importe quel ordinateur [!DNL Linux] ou [!DNL Mac].
   1. Donnez la **clé publique** au client pour qu’il la mette à jour sur son serveur [!DNL SFTP]. Ils doivent inclure tout le texte de la clé publique sur leur serveur, y compris `-----BEGIN RSA PRIVATE KEY-----` et `-----END RSA PRIVATE KEY-----` . En échange, ils doivent fournir le nom d’utilisateur sous lequel ils installent la clé.
   1. Mettez à jour le champ du nom d’utilisateur avec celui fourni par le client et le champ de la clé avec la **clé privée**.

1. Cliquez sur **[!UICONTROL Create]** si vous créez un serveur ou sur **[!UICONTROL Update]** si vous modifiez un serveur existant.
