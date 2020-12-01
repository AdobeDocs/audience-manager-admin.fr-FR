---
description: Utilisez la page Formats de l’outil d’administration des Audiences Manager pour créer un nouveau format ou pour modifier un format existant.
seo-description: Utilisez la page Formats de l’outil d’administration des Audiences Manager pour créer un nouveau format ou pour modifier un format existant.
seo-title: Création ou modification d’un format
title: Création ou modification d’un format
uuid: ca1b1feb-bcd3-4a41-b1e8-80565f6c23ae
translation-type: tm+mt
source-git-commit: 71bf4cec222428686c1eab0998f66887db06da68
workflow-type: tm+mt
source-wordcount: '449'
ht-degree: 5%

---


# Création ou modification d’un format {#create-or-edit-a-format}

Utilisez la page [!UICONTROL Formats] de l&#39;outil d&#39;administration des Audiences Manager pour créer un nouveau format ou pour modifier un format existant.

<!-- t_create_format.xml -->

>[!TIP]
>
>Lors de la sélection d’un format pour vos données délimitées, il est préférable, si possible, de réutiliser un format existant. L’utilisation d’un format déjà éprouvé permet de garantir que vos données sortantes seront générées avec succès. Pour savoir exactement comment un format existant est formaté, cliquez sur l&#39;option [!UICONTROL Formats] dans la barre de menus et recherchez votre format par nom ou par numéro d&#39;identification. Les formats ou les macros mal formés utilisés dans les formats fourniront une sortie mal formatée ou empêcheront l’affichage complet des informations.

1. Pour créer un nouveau format, cliquez sur **[!UICONTROL Formats]** > **[!UICONTROL Add Format]**. Pour modifier un format existant, cliquez sur le format souhaité dans la colonne **[!UICONTROL Name]**.

   ![](assets/create_format.png)

1. Renseignez les champs suivants :
   * **Nom :** (Obligatoire) Donnez un nom descriptif au format.
   * **Type:** (Obligatoire) Sélectionnez le format de votre choix :
      * **[!UICONTROL File]**: Envoie des données par  [!DNL FTP] fichiers.
      * **[!UICONTROL HTTP]**: Enferme les données dans un  [!DNL JSON] wrapper.

1. (Conditionnel) Si vous sélectionnez **[!UICONTROL File]**, renseignez les champs suivants :

   >[!NOTE]
   >
   >Pour une liste des macros disponibles, voir [Macros au format de fichier](../formats/file-formats.md#concept_A867101505074418A58DE325949E5089) et [Macros au format HTTP](../formats/web-formats.md#reference_C392124A5F3F42E49F8AADDBA601ADFE).

   * **[!UICONTROL File Name]:** Spécifiez le nom du fichier pour le fichier de transfert de données.
   * **En-tête :** spécifiez le texte qui apparaît dans la première ligne du fichier de transfert de données.
   * **[!UICONTROL Data Row]:** spécifiez le texte qui apparaît dans chaque ligne délimitée du fichier.
   * **[!UICONTROL Maximum File Size (In MB)]:** spécifiez la taille maximale de fichier pour les fichiers de transfert de données. Les fichiers compressés doivent être inférieurs à 100 Mo. Il n’existe aucune limite quant à la taille du fichier non compressé.
   * **[!UICONTROL Compression]:** Sélectionnez le type de compression souhaité : gz ou zip pour vos fichiers de données. Pour la diffusion à [!UICONTROL AWS S3], vous devez utiliser des fichiers .gz ou non compressés.
   * **[!UICONTROL .info Receipt]:** Spécifie qu&#39;un fichier de contrôle de transfert ([!DNL .info]) est généré. Le fichier [!DNL .info] fournit des informations de métadonnées sur les transferts de fichiers afin que les partenaires puissent vérifier que l&#39;Audience Manager a géré correctement les transferts de fichiers. Pour plus d&#39;informations, consultez [Fichiers de contrôle de transfert pour les transferts de fichiers journaux](https://marketing.adobe.com/resources/help/en_US/aam/c_s2s_add_transfer_control_files.html).
   * **[!UICONTROL MD5 Checksum Receipt]:** indique qu’un reçu de  [!DNL MD5] somme de contrôle est généré. Le reçu de somme de contrôle [!DNL MD5] afin que les partenaires puissent vérifier que l&#39;Audience Manager a géré correctement le transfert complet.

1. (Conditionnel) Si vous sélectionnez **[!UICONTROL HTTP]**, renseignez les champs suivants :

   * **[!UICONTROL Method]:** Choisissez la  [!DNL API] méthode à utiliser pour votre processus de transfert :
      * **[!UICONTROL POST]:** Si vous sélectionnez  [!DNL POST], sélectionnez le type de contenu ([!DNL XML] ou  [!DNL JSON]le cas échéant), puis spécifiez le corps de la requête.
      * **[!UICONTROL GET]:** Si vous sélectionnez  [!DNL GET], spécifiez les paramètres de requête.

1. Cliquez sur **[!UICONTROL Create]** si vous créez un nouveau format ou sur **[!UICONTROL Save Updates]** si vous modifiez un format existant.

## Supprimer un format {#delete-format}

1. Cliquez sur **[!UICONTROL Formats]**.
2. Cliquez sur ![](assets/icon_delete.png) dans la colonne **[!UICONTROL Actions]** du format souhaité.
3. Cliquez sur **[!UICONTROL OK]** pour confirmer la suppression.
