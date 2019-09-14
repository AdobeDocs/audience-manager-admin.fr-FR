---
description: Utilisez la page Formats de l’outil d’administration d’Audience Manager pour créer un nouveau format ou modifier un format existant.
seo-description: Utilisez la page Formats de l’outil d’administration d’Audience Manager pour créer un nouveau format ou modifier un format existant.
seo-title: Créer ou modifier un format
title: Créer ou modifier un format
uuid: ca1b1feb-bcd3-4a41-b1e8-80565f6c23ae
translation-type: tm+mt
source-git-commit: 71bf4cec222428686c1eab0998f66887db06da68

---


# Créer ou modifier un format {#create-or-edit-a-format}

Utilisez la [!UICONTROL Formats] page de l’outil d’administration d’Audience Manager pour créer un nouveau format ou pour modifier un format existant.

<!-- t_create_format.xml -->

>[!TIP]
>
>Lorsque vous sélectionnez un format pour vos données délimitées, il est préférable, si possible, de réutiliser un format existant. L’utilisation d’un format déjà éprouvé garantit que vos données sortantes seront générées avec succès. Pour savoir exactement comment un format existant est formaté, cliquez sur l’ [!UICONTROL Formats] option dans la barre de menus et recherchez votre format par nom ou par numéro d’ID. Les formats ou macros mal formés utilisés dans les formats fournissent une sortie mal formatée ou empêchent la sortie complète des informations.

1. Pour créer un nouveau format, cliquez sur **[!UICONTROL Formats]** &gt; **[!UICONTROL Add Format]**. Pour modifier un format existant, cliquez sur le format souhaité dans la **[!UICONTROL Name]** colonne.

   ![](assets/create_format.png)

1. Renseignez les champs suivants :
   * **** Nom : (Obligatoire) Attribuez un nom explicite au format.
   * **** Type : (Obligatoire) Sélectionnez le format de votre choix :
      * **[!UICONTROL File]**: Envoie les données par le biais de [!DNL FTP] fichiers.
      * **[!UICONTROL HTTP]**: Enferme les données dans un [!DNL JSON] wrapper.

1. (Conditionnel) Si vous le sélectionnez **[!UICONTROL File]**, renseignez les champs suivants :

   >[!NOTE]
   >
   >Pour obtenir la liste des macros disponibles, voir Macros [au format](../formats/file-formats.md#concept_A867101505074418A58DE325949E5089) de fichier et Macros [au format](../formats/web-formats.md#reference_C392124A5F3F42E49F8AADDBA601ADFE)HTTP.

   * **[!UICONTROL File Name]** : Spécifiez le nom du fichier de transfert de données.
   * **** En-tête : Spécifiez le texte qui apparaît dans la première ligne du fichier de transfert de données.
   * **[!UICONTROL Data Row]** : Spécifiez le texte qui apparaît dans chaque ligne délimitée du fichier.
   * **[!UICONTROL Maximum File Size (In MB)]** : Définissez la taille de fichier maximale pour les fichiers de transfert de données. Les fichiers compressés doivent être inférieurs à 100 Mo. La taille du fichier non compressé n’est pas limitée.
   * **[!UICONTROL Compression]** : Sélectionnez le type de compression souhaité : gz ou zip pour vos fichiers de données. Pour la diffusion vers [!UICONTROL AWS S3], vous devez utiliser des fichiers .gz ou non compressés.
   * **[!UICONTROL .info Receipt]** : Indique qu’un fichier de contrôle de transfert ([!DNL .info]) est généré. Le [!DNL .info] fichier fournit des informations de métadonnées sur les transferts de fichiers afin que les partenaires puissent vérifier que Audience Manager a géré correctement les transferts de fichiers. Pour plus d'informations, reportez-vous à la section Fichiers de contrôle de [transfert pour les transferts](https://marketing.adobe.com/resources/help/en_US/aam/c_s2s_add_transfer_control_files.html)de fichiers journaux.
   * **[!UICONTROL MD5 Checksum Receipt]** : Indique qu’un reçu de [!DNL MD5] somme de contrôle est généré. Le reçu [!DNL MD5] de somme de contrôle afin que les partenaires puissent vérifier que Audience Manager a géré correctement le transfert complet.

1. (Conditionnel) Si vous le sélectionnez **[!UICONTROL HTTP]**, renseignez les champs suivants :

   * **[!UICONTROL Method]** : Choisissez la [!DNL API] méthode à utiliser pour votre processus de transfert :
      * **[!UICONTROL POST]** : Si vous sélectionnez [!DNL POST], sélectionnez le type de contenu ([!DNL XML] ou [!DNL JSON]), puis spécifiez le corps de la requête.
      * **[!UICONTROL GET]** : Si vous sélectionnez [!DNL GET], spécifiez les paramètres de requête.

1. Cliquez sur **[!UICONTROL Create]** si vous créez un nouveau format ou sur **[!UICONTROL Save Updates]** si vous modifiez un format existant.

## Suppression d’un format {#delete-format}

1. Cliquez sur **[!UICONTROL Formats]**.
2. Cliquez ![](assets/icon_delete.png) dans la **[!UICONTROL Actions]** colonne du format souhaité.
3. Cliquez sur **[!UICONTROL OK]pour confirmer la suppression.**
