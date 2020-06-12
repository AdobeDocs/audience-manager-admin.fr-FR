---
description: Utilisez la page Serveurs de l’outil d’administration d’Audience Manager pour créer un serveur FTP ou pour modifier un serveur existant.
seo-description: Utilisez la page Serveurs de l’outil d’administration d’Audience Manager pour créer un serveur FTP ou pour modifier un serveur existant.
seo-title: Création ou modification d’un serveur FTP
title: Création ou modification d’un serveur FTP
uuid: 9273abb2-963d-4d83-bf5a-b3817f0b90e6
translation-type: tm+mt
source-git-commit: e0dc190f8765ec91431a2c02a62c6bf5458c7e3d
workflow-type: tm+mt
source-wordcount: '404'
ht-degree: 5%

---


# Création ou modification d’un serveur FTP {#create-or-edit-an-ftp-server}

Utilisez la [!UICONTROL Servers] page de l’outil d’administration d’Audience Manager pour créer un nouveau serveur FTP ou pour modifier un serveur existant.

>[!NOTE]
>
>Vous devez avoir le [!UICONTROL DEXADMIN] rôle pour créer de nouveaux serveurs ou modifier des serveurs existants.

1. Pour créer un nouveau serveur, cliquez sur **[!UICONTROL Servers]** > **[!UICONTROL Create Server]**. Pour modifier un serveur existant, cliquez sur le serveur de votre choix dans la **[!UICONTROL Label]** colonne.
1. Indiquez l’étiquette souhaitée pour ce serveur.
1. Dans la liste **[!UICONTROL Protocol]** déroulante, sélectionnez le protocole de votre choix : **FTP**.

   >[!NOTE]
   >
   >En règle générale, il est recommandé d’utiliser [!DNL Amazon S3] comme méthode pour obtenir des fichiers et les distribuer aux partenaires. [!DNL Amazon S3] fournit une interface de services Web simple qui peut être utilisée pour stocker et récupérer n’importe quelle quantité de données, à tout moment, de n’importe où sur le Web. Pour plus d’informations, voir [A propos d’Amazon S3](https://docs.adobe.com/content/help/en/audience-manager/user-guide/reference/amazon-s3.html) dans le Guide *de l’utilisateur d’* Audience Manager.

1. Renseignez les champs suivants :

   * **[!UICONTROL Type]:**Sélectionnez le type de chiffrement souhaité :**[!UICONTROL SFTP]**ou **[!UICONTROL FTPs/TLS]**.
   * **[!UICONTROL Domain]:**Spécifiez le domaine (hôte) souhaité pour ce serveur.
   * **[!UICONTROL Port]:**Spécifiez le port souhaité pour ce serveur. Le port par défaut s’affiche pour chaque type de chiffrement. Si nécessaire, vous pouvez modifier le port par défaut.
   * **[!UICONTROL Remote Path]:**Spécifiez le chemin d’accès distant souhaité pour ce serveur. Si vous laissez ce champ vide, Audience Manager place les fichiers dans le répertoire par défaut.
   * **[!UICONTROL .tmp File Rename on Completion]:**Activez cette option pour renommer le`.tmp`fichier une fois terminé.
   * **[!UICONTROL Filename Suffix]:**Spécifiez le texte à ajouter pour transférer des fichiers.
   * **[!UICONTROL Moved to When Finished]:**Spécifiez le chemin d&#39;accès à l&#39;emplacement où vous souhaitez déplacer le fichier de transfert une fois terminé.
   * **[!UICONTROL Authentication]:**Spécifiez la méthode d’authentification du serveur de votre choix :**[!UICONTROL Username/Password]**ou **[!UICONTROL SSH Key]**.
   >[!NOTE]
   >
   >N&#39;oubliez pas d&#39;ajouter notre adresse [!DNL FTP][!DNL IP] à votre liste d&#39;adresses IP autorisées : **52.44.29.204**.

1. Pour **[!UICONTROL SSH Key]** l&#39;authentification :
   1. Générez la paire de clés publique/privée à partir de n&#39;importe quelle [!DNL Linux] machine ou [!DNL Mac] machine.
   1. Donnez la clé **** publique au client pour qu’il effectue la mise à jour sur son [!DNL SFTP] serveur. Ils doivent inclure tout le texte de la clé publique sur leur serveur, y compris `-----BEGIN RSA PRIVATE KEY-----` et `-----END RSA PRIVATE KEY-----` . En échange, ils doivent fournir le nom d&#39;utilisateur sous lequel ils installent la clé.
   1. Mettez à jour le champ de nom d’utilisateur avec celui fourni par le client et le champ de clé avec la clé **** privée.
1. Cliquez sur **[!UICONTROL Create]** si vous créez un nouveau serveur ou sur **[!UICONTROL Update]** si vous modifiez un serveur existant.
