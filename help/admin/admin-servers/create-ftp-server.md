---
description: Utilisez la page Serveurs de l'outil d'administration d'Audience Manager pour créer un serveur FTP ou pour modifier un serveur existant.
seo-description: Utilisez la page Serveurs de l'outil d'administration d'Audience Manager pour créer un serveur FTP ou pour modifier un serveur existant.
seo-title: Création ou modification d'un serveur FTP
title: Création ou modification d'un serveur FTP
uuid: 9273 abb 2-963 d -4 d 83-bf 5 a-b 3817 f 0 b 90 e 6
translation-type: tm+mt
source-git-commit: 57d7a92265e565b6c411e4cfa5c579e40eb837b3

---


# Création ou modification d'un serveur FTP {#create-or-edit-an-ftp-server}

Utilisez [!UICONTROL Servers] la page de l'outil d'administration d'Audience Manager pour créer un serveur FTP ou pour modifier un serveur existant.

>[!NOTE]
>
>Vous devez disposer du [!UICONTROL DEXADMIN] rôle pour créer de nouveaux serveurs ou modifier des serveurs existants.

1. Pour créer un serveur, cliquez **[!UICONTROL Servers]** sur &gt; **[!UICONTROL Create Server]**. Pour modifier un serveur existant, cliquez sur le serveur de votre choix dans **[!UICONTROL Label]** la colonne.
1. Spécifiez une étiquette pour ce serveur.
1. Dans la liste **[!UICONTROL Protocol]** déroulante, sélectionnez le protocole de votre choix : **FTP**.

   >[!NOTE]
   >
   >En règle générale, nous conseillons d'utiliser [!DNL Amazon S3] comme méthode de récupération des fichiers et de diffusion de fichiers aux partenaires. [!DNL Amazon S3] fournit une interface de services Web simple qui permet de stocker et de récupérer n'importe quelle quantité de données à tout moment, depuis n'importe quel emplacement sur le Web. Pour plus d'informations, voir [A propos d'Amazon S 3](https://docs.adobe.com/content/help/en/audience-manager/user-guide/reference/amazon-s3.html) dans le Guide de l'utilisateur *d'Audience Manager*.

1. Renseignez les champs suivants :

   * **[!UICONTROL Type]:** Sélectionnez le type de chiffrement souhaité : **[!UICONTROL SFTP]** ou **[!UICONTROL FTPs/TLS]**.
   * **[!UICONTROL Domain]:** Spécifiez le domaine (hôte) de ce serveur.
   * **[!UICONTROL Port]:** Spécifiez le port de votre choix pour ce serveur. Le port par défaut s'affiche pour chaque type de chiffrement. Si nécessaire, vous pouvez modifier le port par défaut.
   * **[!UICONTROL Remote Path]:** Spécifiez le chemin distant de votre choix pour ce serveur. Si vous laissez ce champ vide, Audience Manager place les fichiers dans le répertoire par défaut.
   * **[!UICONTROL .tmp File Rename on Completion]:** Activez cette option pour renommer `.tmp` le fichier à la fin.
   * **[!UICONTROL Filename Suffix]:** Indiquez le texte que vous souhaitez ajouter aux fichiers.
   * **[!UICONTROL Moved to When Finished]:** Spécifiez le chemin d'accès à l'emplacement où le fichier de transfert doit être déplacé à la fin.
   * **[!UICONTROL Authentication]:** Spécifiez la méthode d'authentification du serveur souhaitée : **[!UICONTROL Username/Password]** ou **[!UICONTROL SSH Key]**.
   >[!NOTE]
   >
   >Veillez à la liste blanche [!DNL FTP][!DNL IP]: **52.44.29.204**.

1. Pour **[!UICONTROL SSH Key]** l'authentification :
   1. Générez la paire de clés publique/privée à partir d'un [!DNL Linux] ou de [!DNL Mac] plusieurs ordinateurs.
   1. Attribuez à la clé **publique** le client à mettre à jour sur son [!DNL SFTP] serveur. Ils doivent inclure tout le texte de la clé publique sur leur serveur, y compris `-----BEGIN RSA PRIVATE KEY-----` et `-----END RSA PRIVATE KEY-----` . En échange, ils doivent fournir le nom d'utilisateur sous lequel ils installent la clé.
   1. Mettez à jour le champ nom d'utilisateur avec celle fournie par le client et le champ clé avec la clé **privée**.
1. Cliquez **[!UICONTROL Create]** sur si vous créez un serveur ou si vous **[!UICONTROL Update]** modifiez un serveur existant.
