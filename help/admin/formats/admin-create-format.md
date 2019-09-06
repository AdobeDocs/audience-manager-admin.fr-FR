---
description: Utilisez la page Formats de l'outil Administration d'Audience Manager pour créer un nouveau format ou pour modifier un format existant.
seo-description: Utilisez la page Formats de l'outil Administration d'Audience Manager pour créer un nouveau format ou pour modifier un format existant.
seo-title: Création ou modification d'un format
title: Création ou modification d'un format
uuid: ca 1 b 1 feb-bcd 3-4 a 41-b 1 e 8-80565 f 6 c 23 ae
translation-type: tm+mt
source-git-commit: 71bf4cec222428686c1eab0998f66887db06da68

---


# Création ou modification d'un format {#create-or-edit-a-format}

Utilisez [!UICONTROL Formats] la page de l'outil d'administration d'Audience Manager pour créer un nouveau format ou pour modifier un format existant.

<!-- t_create_format.xml -->

>[!TIP]
>
>Lorsque vous sélectionnez un format pour vos données arrondies, il est préférable, si possible, de réutiliser un format existant. L'utilisation d'un format déjà prouvé garantit la génération réussie de vos données sortantes. Pour afficher exactement le format d'un format existant, cliquez sur l' [!UICONTROL Formats] option dans la barre de menus et recherchez votre format par nom ou par numéro d'identifiant. Les formats ou macros mal formés utilisés dans les formats fournissent une sortie mal formatée ou empêchent la sortie complète des informations.

1. Pour créer un nouveau format, cliquez **[!UICONTROL Formats]** sur &gt; **[!UICONTROL Add Format]**. Pour modifier un format existant, cliquez sur le format de votre choix dans **[!UICONTROL Name]** la colonne.

   ![](assets/create_format.png)

1. Renseignez les champs suivants :
   * **Nom :** (Obligatoire) Attribuez un nom explicite au format.
   * **Type :** (Obligatoire) Sélectionnez le format de votre choix :
      * **[!UICONTROL File]**: Envoie des données par le biais [!DNL FTP] de fichiers.
      * **[!UICONTROL HTTP]**: Renferme les données d'un [!DNL JSON] wrapper.

1. (Conditionnel) Si vous choisissez **[!UICONTROL File]**, renseignez les champs suivants :

   >[!NOTE]
   >
   >Pour obtenir la liste des macros disponibles, reportez-vous à la [page Macros](../formats/file-formats.md#concept_A867101505074418A58DE325949E5089) de format de fichier et [Macros de format HTTP](../formats/web-formats.md#reference_C392124A5F3F42E49F8AADDBA601ADFE).

   * **[!UICONTROL File Name]:** Indiquez le fichier - nom du fichier de transfert de données.
   * **En-tête :** Spécifiez le texte qui apparaît sur la première ligne du fichier de transfert de données.
   * **[!UICONTROL Data Row]:** Spécifiez le texte qui apparaît dans chaque ligne d'affichage du fichier.
   * **[!UICONTROL Maximum File Size (In MB)]:** Spécifiez la taille de fichier maximale pour les fichiers de transfert de données. Les fichiers compressés doivent être inférieurs à 100 Mo. La taille du fichier décompressé n'est pas limitée.
   * **[!UICONTROL Compression]:** Sélectionnez le type de compression souhaité : gz ou zip pour vos fichiers de données. Pour la diffusion, [!UICONTROL AWS S3]vous devez utiliser des fichiers.gz ou décompressés.
   * **[!UICONTROL .info Receipt]:** Indique qu'un fichier de commande de transfert est généré[!DNL .info]. Le [!DNL .info] fichier fournit des informations de métadonnées sur les transferts de fichiers, de sorte que les partenaires puissent vérifier qu'Audience Manager a correctement transféré les transferts de fichiers. Pour plus d'informations, voir [Transfert de fichiers de contrôle pour les transferts de fichiers journaux](https://marketing.adobe.com/resources/help/en_US/aam/c_s2s_add_transfer_control_files.html).
   * **[!UICONTROL MD5 Checksum Receipt]:** Indique qu'un reçu [!DNL MD5] de somme de contrôle est généré. La somme [!DNL MD5] de contrôle de sorte que les partenaires puissent vérifier qu'Audience Manager a géré correctement le transfert complet.

1. (Conditionnel) Si vous choisissez **[!UICONTROL HTTP]**, renseignez les champs suivants :

   * **[!UICONTROL Method]:** Choisissez [!DNL API] la méthode à utiliser pour votre processus de transfert :
      * **[!UICONTROL POST]:** Si vous sélectionnez [!DNL POST], sélectionnez le type de contenu ([!DNL XML] ou [!DNL JSON]), puis indiquez le corps de la requête.
      * **[!UICONTROL GET]:** Si vous sélectionnez [!DNL GET], spécifiez les paramètres de requête.

1. Cliquez **[!UICONTROL Create]** sur si vous créez un nouveau format ou si vous **[!UICONTROL Save Updates]** modifiez un format existant.

## Suppression d'un format {#delete-format}

1. Cliquez sur **[!UICONTROL Formats]**.
2. Cliquez ![](assets/icon_delete.png) dans la **[!UICONTROL Actions]** colonne du format souhaité.
3. Cliquez sur **[!UICONTROL OK]pour confirmer la suppression.**
