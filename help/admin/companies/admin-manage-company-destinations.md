---
description: Créez, modifiez et supprimez des destinations Audience Manager.
seo-description: Créez, modifiez et supprimez des destinations Audience Manager.
seo-title: Gérer les destinations d’entreprise
title: Gérer les destinations d’entreprise
uuid: d9a6bfb1-7629-44e0-b7d7-ece44f65ea2b
translation-type: tm+mt
source-git-commit: 57d7a92265e565b6c411e4cfa5c579e40eb837b3

---


# Gérer les destinations d’entreprise {#manage-company-destinations}

Créez, modifiez et supprimez des destinations Audience Manager.

<!-- t_company_destinations.xml -->

Pour plus d’informations, voir [Destinations](https://docs.adobe.com/content/help/en/audience-manager/user-guide/features/destinations/destinations.html) dans le Guide *de l’utilisateur d’* Audience Manager.

## Créer ou modifier des destinations d’entreprise {#create-edit-company-destinations}

Faites défiler les sections pour obtenir des instructions étape par étape sur la création de nouvelles destinations ou la modification de destinations existantes. [!DNL Audience Manager]

<!-- create-edit-company-destinations.xml -->

Consultez la page [d’intégration des partenaires](https://wiki.corp.adobe.com/x/mPIMPw) Experience Cloud avant de configurer des destinations. La page contient les informations spécifiques que vous devez renseigner pour chaque intégration de [!DNL Audience Manager] partenaire.

Si votre client souhaite utiliser [!DNL Adobe Media Optimizer] comme destination dans [!DNL Audience Manager] , vous devez configurer cette configuration dans [!DNL Adobe Media Optimizer].

## Navigate to the Destinations Tab {#navigate-destinations}

1. Cliquez sur **[!UICONTROL Companies]**, puis recherchez et cliquez sur l’entreprise souhaitée pour afficher sa [!UICONTROL Profile] page. Vous pouvez utiliser la [!UICONTROL Search] zone ou les commandes de pagination au bas de la liste pour trouver la société souhaitée. Vous pouvez trier chaque colonne par ordre croissant ou décroissant en cliquant sur l’en-tête de la colonne de votre choix.
1. Click the **[!UICONTROL Destinations]** tab.
1. Pour créer une destination, cliquez sur **[!UICONTROL Add Destination]**. To edit an existing destination, click the destination's name in the **[!UICONTROL Name]** column.

## Paramètres de base {#basic-settings}

Fill in the fields in the **[!UICONTROL Basic Settings]** window.

* **[!UICONTROL Name]** : (Obligatoire) Indiquez le nom de cette destination.
* **[!UICONTROL Description]** : Spécifiez des informations descriptives sur cette destination.
* **[!UICONTROL Type]** : (Obligatoire) Sélectionnez le type de destination souhaité :
   * **[!UICONTROL Bulk ID]**: Synchroniser les ID entre différentes plateformes.
   * **[!UICONTROL Bulk Trait]**: Envoyez des informations de caractéristiques en bloc vers différentes plateformes.
   * **[!UICONTROL Bulk Segment]**: Envoyez des informations de segment en bloc vers différentes plateformes.
   * **[!UICONTROL S2S]**: Utilisez les destinations serveur à serveur pour envoyer des données en temps réel et par lot vers différentes plateformes.
* **[!UICONTROL Auto-Fill Destination Mapping]** : ( [!UICONTROL S2S] uniquement) Sélectionnez une option :
   * **[!UICONTROL Segment ID]** : Si vous sélectionnez ce paramètre, le mappage des valeurs de destination est renseigné par l’ID de [!DNL Audience Manager] segment.
   * **[!UICONTROL Integration Code Value]** : Si vous sélectionnez ce paramètre, le mappage des valeurs de destination est rempli avec le code d’intégration du [!DNL Audience Manager] segment.
* **[!UICONTROL User ID Key]** : (Obligatoire) Sélectionnez la clé d’ID utilisateur souhaitée pour cette destination dans la liste déroulante.

Cet ID est utilisé comme ID de source de données maître. Cela détermine les ID utilisateur à délimiter dans le fichier.

>[!NOTE]
>
>Pour le type de [!UICONTROL Bulk ID] destination, vous ne pouvez pas utiliser l’ [!DNL Audience Manager] ID ou l’ [!UICONTROL User ID] [!DNL Adobe Experience Cloud] ID.

Si votre ID de source de données ( [!UICONTROL DPID]) ne s’affiche pas dans la liste déroulante, vous devez cocher la **[!UICONTROL Outbound]** case au niveau de la source de données sur la page [Paramètres de la source de](https://docs.adobe.com/content/help/en/audience-manager/user-guide/features/data-sources/manage-datasources.html)données.

* **[!UICONTROL Target Data Source]** : (Obligatoire) Sélectionnez la source de données souhaitée pour cette destination dans la liste déroulante. Ce paramètre permet d’étiqueter les données délimitées, ce qui permet l’assimilation dans des systèmes distincts côté client.
* **[!UICONTROL Foreign Account ID]** : Spécifiez l’ID de compte étranger pour cette destination. Il s’agit de la valeur d’identification dans le système du destinataire pour ces données délimitées.
* **[!UICONTROL Outbound Sample Rate Denominator]** : Lorsque la quantité totale de données renvoyées est inconnue, utilisez ce paramètre pour ne renvoyer qu’une quantité d’échantillon de données, plutôt que la quantité totale. Ajustez le nombre ici pour représenter une fraction des données (par exemple, une valeur de "100" renvoie 1/100 de la quantité normale de données, une valeur de "10" renvoie 1/10 de la quantité normale de données). La valeur par défaut est 1, ce qui renvoie toutes les données.

## Données en temps réel (pour les destinations S2S) {#realtime-s2s}

Si vous créez une [!UICONTROL S2S] destination, renseignez les champs ci-dessous :

**[!UICONTROL Servers]**: Sélectionnez le `HTTP` serveur souhaité pour cette destination.
**[!UICONTROL Format]**: Sélectionnez le format souhaité pour cette destination dans la liste déroulante : [!UICONTROL HTTP only].

>[!NOTE]
>
>Pour [!DNL S2S] seulement, vous pouvez activer ou désactiver l’une [!UICONTROL Realtime] ou [!UICONTROL Batch] des destinations à l’aide des curseurs Activé/Désactivé à l’écran. Vous ne pouvez pas désactiver les deux options.

## Données par lot {#batch-data}

Pour [!UICONTROL Bulk ID]les destinations [!UICONTROL Bulk Trait] ou [!UICONTROL Bulk Segment] les destinations, renseignez les champs ci-dessous :

* **[!UICONTROL Protocol]**: (Obligatoire) Sélectionnez le protocole souhaité pour cette destination dans la liste déroulante :
   * **[!UICONTROL FTP]**
   * **[!UICONTROL HTTP]**
   * **[!UICONTROL S3]**
* **[!UICONTROL Servers]**: (Obligatoire) Sélectionnez le serveur souhaité pour cette destination dans la liste déroulante.
* **[!UICONTROL Format]**: (Obligatoire) Sélectionnez le format souhaité pour cette destination dans la liste déroulante : [!DNL HTTP] ou type de fichier, selon le protocole choisi ci-dessus.
* **[!UICONTROL Sync Type]**: (Obligatoire) Sélectionnez le type de synchronisation souhaité pour cette destination. Cela indique le niveau des activités utilisateur que les clients souhaitent inclure dans les commandes sortantes. Sélectionnez **[!UICONTROL Customer]** si les clients souhaitent uniquement analyser les qualifications des segments à partir de leurs propriétés. Sélectionnez **[!UICONTROL Platform]** s’ils souhaitent inclure des qualifications de segment issues d’activités hors site pour tous les [!DNL Audience Manager] clients.
* **[!UICONTROL Customer]**: Le fichier contient des utilisateurs actifs qui ont au moins une prise de conscience de caractéristiques sur les propriétés du client (associées à celle du client [!UICONTROL PID]) pendant la période sélectionnée. Vos clients doivent utiliser cette option pour exporter leurs qualifications de segment en temps *réel* vers les destinations.
* **[!UICONTROL Platform]**: Le fichier contient des utilisateurs actifs qui ont au moins une interaction en temps réel, qu’il s’agisse de la synchronisation des identifiants ou de la réalisation des caractéristiques, n’importe où dans les propriétés de tous les [!DNL Audience Manager] clients (associées à tous les PID client) pendant la période sélectionnée. Vos clients doivent utiliser cette option pour exporter leurs qualifications de segment *total* vers des destinations.
* **[!UICONTROL Lifetime]**: Le fichier contient les utilisateurs actifs qui sont vus n’importe où sur toutes les propriétés de tous les [!DNL Audience Manager] clients depuis la création de la destination.
* **[!UICONTROL Sync Type Lookback Period]**: Si vous sélectionnez [!UICONTROL Customer] ou [!UICONTROL Platform], sélectionnez une période. Les fichiers contiennent des utilisateurs actifs pour la période sélectionnée.
Sélectionnez ensuite le type de commande. Cela indique la fréquence et la portée de chaque intégration sortante avec les partenaires. Sélectionnez entre les commandes incrémentielles et complètes.
* **[!UICONTROL Incremental Scheduled Run]**: Pour chaque exécution, [!DNL Audience Manager] les nouveaux utilisateurs nets sortants seront uniquement qualifiés depuis l’ordre sortant précédent. Sélectionnez la période souhaitée pour [!DNL Audience Manager] effectuer des processus de synchronisation incrémentielle. Par exemple, vous pouvez sélectionner toutes les 24 heures, tous les sept jours, tous les 30 jours ou jamais.

>[!NOTE] {importance="high"}
>
>La première commande incrémentielle équivaut à une commande complète, car aucun utilisateur précédent n’a jamais été envoyé vers la destination.

* **[!UICONTROL Full Sync Scheduled Run]**: A chaque exécution, [!DNL Audience Manager] sortira tous les utilisateurs actifs depuis la première configuration de la destination. Sélectionnez la planification à utiliser [!DNL Audience Manager] pour effectuer des processus de synchronisation complets. Par exemple, vous pouvez sélectionner toutes les 24 heures, tous les sept jours, tous les 30 jours ou jamais.

>[!NOTE] {importance="high"}
>
>Nous vous recommandons d’utiliser des synchronisations incrémentielles plus fréquemment que des synchronisations complètes. Les synchronisations incrémentielles envoient uniquement des fichiers qui contiennent de nouvelles réalisations de caractéristiques ou des synchronisations d’ID. Les synchronisations complètes envoient tous les fichiers, qu’ils incluent de nouvelles réalisations ou des synchronisations d’ID. N'utilisez la [!UICONTROL Full Sync Scheduled Run] configuration que lorsque les clients ont besoin d'une copie complète de tous leurs utilisateurs, pour réduire le volume de données sortantes.

## Configuration des sources de données {#configure-data-sources}

Pour [!UICONTROL Bulk ID]les destinations [!UICONTROL Bulk Trait] ou [!UICONTROL Bulk Segment] les destinations, renseignez les champs ci-dessous. Ces paramètres vous permettent d’envoyer toutes les données (caractéristiques, segments ou ID, selon le type sélectionné) associées aux sources de données.

* **[!UICONTROL All Unrestricted First Party Data]**: Sélectionnez cette option pour utiliser toutes les sources de données propriétaires. Si vous sélectionnez cette option, les [!UICONTROL Available Data Sources] options sont désactivées.
* **[!UICONTROL Available Data Sources]**: Utilisez les flèches pour déplacer les sources de données entre les **[!UICONTROL Available Data Sources]** et **[!UICONTROL In File Data Sources]** les zones.

## Enregistrer et finaliser {#save-and-finalize}

Le **[!UICONTROL Save]** bouton est activé après avoir rempli tous les champs obligatoires. Cliquez sur **[!UICONTROL Save]** pour finaliser le processus de création de destination.

## Supprimer les destinations d’entreprise {#delete-company-destinations}

<!-- delete-company-destinations.xml -->

Pour supprimer une destination :

1. Cliquez sur **[!UICONTROL Companies]**, recherchez et cliquez sur l’entreprise souhaitée, puis sur l’ **[!UICONTROL Destinations]** onglet.
1. Cliquez ![](assets/icon_delete.png) dans la **[!UICONTROL Actions]** colonne de la destination souhaitée.
1. Cliquez sur **[!UICONTROL OK]pour confirmer la suppression.**

>[!NOTE]
>
>Vous ne pouvez pas supprimer une destination si des segments y sont associés.