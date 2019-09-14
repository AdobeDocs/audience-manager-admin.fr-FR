---
description: Utilisez la page Serveurs de l’outil d’administration d’Audience Manager pour créer un serveur FTP ou modifier un serveur existant.
seo-description: Utilisez la page Serveurs de l’outil d’administration d’Audience Manager pour créer un serveur FTP ou modifier un serveur existant.
seo-title: ' Création ou modification d’un serveur FTP'
title: ' Création ou modification d’un serveur FTP'
uuid: 9273abb2-963d-4d83-bf5a-b3817f0b90e6
translation-type: tm+mt
source-git-commit: 57d7a92265e565b6c411e4cfa5c579e40eb837b3

---


# Création ou modification d’un serveur FTP {#create-or-edit-an-ftp-server}

Utilisez la [!UICONTROL Servers] page de l’outil d’administration d’Audience Manager pour créer un serveur FTP ou modifier un serveur existant.

>[!NOTE]
>
>Vous devez avoir le [!UICONTROL DEXADMIN] rôle pour créer de nouveaux serveurs ou modifier des serveurs existants.

1. Pour créer un nouveau serveur, cliquez sur **[!UICONTROL Servers]** &gt; **[!UICONTROL Create Server]**. Pour modifier un serveur existant, cliquez sur le serveur souhaité dans la **[!UICONTROL Label]** colonne.
1. Indiquez le libellé souhaité pour ce serveur.
1. Dans la liste **[!UICONTROL Protocol]** déroulante, sélectionnez un protocole : **FTP**.

   >[!NOTE]
   >
   >En règle générale, il est recommandé d’utiliser [!DNL Amazon S3] comme méthode pour obtenir des fichiers et les envoyer à des partenaires. [!DNL Amazon S3] fournit une interface de services Web simple qui peut être utilisée pour stocker et récupérer n’importe quelle quantité de données, à tout moment, de n’importe où sur le Web. Pour plus d’informations, voir [A propos d’Amazon S3](https://docs.adobe.com/content/help/en/audience-manager/user-guide/reference/amazon-s3.html) dans le Guide *de l’utilisateur d’* Audience Manager.

1. Renseignez les champs suivants :

   * **[!UICONTROL Type]** : Sélectionnez le type de chiffrement souhaité : **[!UICONTROL SFTP]** ou **[!UICONTROL FTPs/TLS]**.
   * **[!UICONTROL Domain]** : Spécifiez le domaine (hôte) souhaité pour ce serveur.
   * **[!UICONTROL Port]** : Spécifiez le port souhaité pour ce serveur. Le port par défaut s’affiche pour chaque type de chiffrement. Si nécessaire, vous pouvez modifier le port par défaut.
   * **[!UICONTROL Remote Path]** : Spécifiez le chemin d’accès distant souhaité pour ce serveur. Si vous laissez ce champ vide, Audience Manager place les fichiers dans le répertoire par défaut.
   * **[!UICONTROL .tmp File Rename on Completion]** : Activez cette option pour renommer le `.tmp` fichier une fois terminé.
   * **[!UICONTROL Filename Suffix]** : Spécifiez le texte à ajouter pour transférer des fichiers.
   * **[!UICONTROL Moved to When Finished]** : Indiquez le chemin d’accès à l’emplacement où vous souhaitez déplacer le fichier de transfert une fois terminé.
   * **[!UICONTROL Authentication]** : Spécifiez la méthode d’authentification du serveur de votre choix : **[!UICONTROL Username/Password]** ou **[!UICONTROL SSH Key]**.
   >[!NOTE]
   >
   >N'oubliez pas de mettre en liste blanche notre [!DNL FTP] fille [!DNL IP]: **52.44.29.204**.

1. Pour **[!UICONTROL SSH Key]** l'authentification :
   1. Générez la paire de clés publique/privée depuis n’importe quel [!DNL Linux] ordinateur ou [!DNL Mac] ordinateur.
   1. Donnez la clé **** publique au client pour qu’il effectue la mise à jour sur son [!DNL SFTP] serveur. Ils doivent inclure tout le texte de la clé publique sur leur serveur, y compris `-----BEGIN RSA PRIVATE KEY-----` et `-----END RSA PRIVATE KEY-----` . En échange, ils doivent fournir le nom d'utilisateur sous lequel ils installent la clé.
   1. Mettez à jour le champ username avec celui fourni par le client et le champ key avec la clé **privée**.
1. Cliquez sur **[!UICONTROL Create]** si vous créez un nouveau serveur ou sur **[!UICONTROL Update]** si vous modifiez un serveur existant.
