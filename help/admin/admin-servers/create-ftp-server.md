---
description: Utilisez la page Serveurs de l’outil d’administration des Audiences Manager pour créer un serveur FTP ou modifier un serveur existant.
seo-description: Use the Servers page in the Audience Manager Admin tool to create a new FTP server or to edit an existing server.
seo-title: Create or Edit an FTP Server
title: Création ou modification d’un serveur FTP
uuid: 9273abb2-963d-4d83-bf5a-b3817f0b90e6
exl-id: 9eae4ecf-ccde-483a-ae53-1cbac033d8d6
source-git-commit: 8af040e49b881302315e0b66baa73db47c5eee28
workflow-type: tm+mt
source-wordcount: '387'
ht-degree: 1%

---

# Création ou modification d’un serveur FTP {#create-or-edit-an-ftp-server}

Utilisez la page [!UICONTROL Servers] de l’outil d’administration des Audiences Manager pour créer un serveur FTP ou modifier un serveur existant.

>[!NOTE]
>
>Vous devez disposer du rôle [!UICONTROL DEXADMIN] pour créer de nouveaux serveurs ou modifier des serveurs existants.

1. Pour créer un nouveau serveur, cliquez sur **[!UICONTROL Servers]** > **[!UICONTROL Create Server]**. Pour modifier un serveur existant, cliquez sur le serveur de votre choix dans la colonne **[!UICONTROL Label]**.
1. Indiquez le libellé souhaité pour ce serveur.
1. Dans la liste déroulante **[!UICONTROL Protocol]**, sélectionnez le protocole souhaité : **FTP**.

   >[!NOTE]
   >
   >Il est recommandé d’utiliser [!DNL Amazon S3] comme méthode pour obtenir des fichiers à partir de et envoyer des fichiers aux partenaires. [!DNL Amazon S3] fournit une interface de services web simple qui peut être utilisée pour stocker et récupérer n’importe quelle quantité de données, à tout moment, de n’importe où sur le web. Pour plus d’informations, voir [À propos d’Amazon S3](https://experienceleague.adobe.com/docs/audience-manager/user-guide/reference/amazon-s3.html) dans le *Guide de l’utilisateur d’Audience Manager*.

1. Renseignez les champs suivants :

   * **[!UICONTROL Type]:** Sélectionnez le type de chiffrement souhaité : **[!UICONTROL SFTP]** ou **[!UICONTROL FTPs/TLS]**.
   * **[!UICONTROL Domain]:** Spécifiez le domaine (hôte) souhaité pour ce serveur.
   * **[!UICONTROL Port]:** Spécifiez le port souhaité pour ce serveur. Le port par défaut s’affiche pour chaque type de chiffrement. Si nécessaire, vous pouvez modifier le port par défaut.
   * **[!UICONTROL Remote Path]:** Spécifiez le chemin d’accès distant souhaité pour ce serveur. Si vous laissez ce champ vide, l’Audience Manager place les fichiers dans le répertoire par défaut.
   * **[!UICONTROL .tmp File Rename on Completion]:** Activez cette option pour renommer le fichier `.tmp` à la fin de l’opération.
   * **[!UICONTROL Filename Suffix]:** Spécifiez le texte à ajouter pour transférer des fichiers.
   * **[!UICONTROL Moved to When Finished]:** spécifiez le chemin d’accès à l’emplacement où vous souhaitez que le fichier de transfert soit déplacé à la fin.
   * **[!UICONTROL Authentication]:** Spécifiez la méthode d’authentification du serveur souhaitée : **[!UICONTROL Username/Password]** ou **[!UICONTROL SSH Key]**.

   >[!NOTE]
   >
   >N&#39;oubliez pas d&#39;ajouter notre sortie [!DNL FTP] [!DNL IP] à votre liste d&#39;adresses IP autorisées : **54.204.116.43**.

1. Pour l’authentification **[!UICONTROL SSH Key]** :
   >[!NOTE]
   >
   >Lors de la configuration de l&#39;authentification par clé SSH, veillez à toujours générer les clés publique et privée au format OpenSSH uniquement.
   1. Générez la paire de clés publique/privée à partir de n&#39;importe quel ordinateur [!DNL Linux] ou [!DNL Mac].
   1. Donnez la **clé publique** au client pour effectuer la mise à jour sur son serveur [!DNL SFTP]. Ils doivent inclure tout le texte de la clé publique sur leur serveur, y compris `-----BEGIN RSA PRIVATE KEY-----` et `-----END RSA PRIVATE KEY-----` . Dans exchange, il doit indiquer le nom d’utilisateur sous lequel il installe la clé.
   1. Mettez à jour le champ username avec celui fourni par le client et le champ key avec la **clé privée**.
1. Cliquez sur **[!UICONTROL Create]** si vous créez un nouveau serveur ou sur **[!UICONTROL Update]** si vous modifiez un serveur existant.
