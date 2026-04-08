---
description: Créer, modifier et supprimer des destinations Audience Manager.
seo-description: Create, edit, and delete Audience Manager destinations.
seo-title: Manage Company Destinations
title: Gérer les destinations d’entreprise
uuid: d9a6bfb1-7629-44e0-b7d7-ece44f65ea2b
exl-id: a2e73613-07cd-4ab8-8c6e-be451ed50bfc
TQID: https://experienceleague.adobe.com/-MWpMACN0bFPIRAWejD0-VV5nG8BGAukmV1QXxXal-E
product_v2:
  - id: df80eeb1-8d72-467e-b0df-9d51c7d3a0a1
feature_v2:
  - id: c814092e-2730-45e8-a12d-e084529f52cb
source-git-commit: d2bed13a6ac7d38ae79b65d492b6de0ca6b6d488
workflow-type: tm+mt
source-wordcount: 1101
ht-degree: 0%

---

# Gérer les destinations d’entreprise {#manage-company-destinations}

Créer, modifier et supprimer des destinations Audience Manager.

<!-- t_company_destinations.xml -->

Pour plus d’informations, voir [Destinations](https://experienceleague.adobe.com/docs/audience-manager/user-guide/features/destinations/destinations.html?lang=fr) dans le *Guide de l’utilisateur d’Audience Manager*.

## Créer ou modifier des destinations d’entreprise {#create-edit-company-destinations}

Faites défiler les sections pour obtenir des instructions détaillées sur la création de destinations [!DNL Audience Manager] ou la modification de destinations existantes.

<!-- create-edit-company-destinations.xml -->

Consultez la page [Intégration des partenaires &#x200B;](https://wiki.corp.adobe.com/x/mPIMPw) avant de configurer des destinations. La page contient les informations spécifiques à renseigner pour chaque intégration de partenaire [!DNL Audience Manager].

Si votre client souhaite utiliser [!DNL Adobe Media Optimizer] comme destination dans [!DNL Audience Manager] , vous devez le configurer dans [!DNL Adobe Media Optimizer].

## Accédez à l’onglet Destinations . {#navigate-destinations}

1. Cliquez sur **[!UICONTROL Companies]**, puis recherchez et cliquez sur la société souhaitée pour afficher sa page [!UICONTROL Profile]. Vous pouvez utiliser la zone de [!UICONTROL Search] ou les commandes de pagination au bas de la liste pour trouver l’entreprise souhaitée. Vous pouvez trier chaque colonne par ordre croissant ou décroissant en cliquant sur l’en-tête de la colonne souhaitée.
1. Cliquez sur l’onglet **[!UICONTROL Destinations]** .
1. Pour créer une nouvelle destination, cliquez sur **[!UICONTROL Add Destination]**. Pour modifier une destination existante, cliquez sur le nom de la destination dans la colonne **[!UICONTROL Name]** .

## Basic Settings {#basic-settings}

Renseignez les champs de la fenêtre de **[!UICONTROL Basic Settings]**.

* **[!UICONTROL Name]:** (obligatoire) spécifiez le nom de cette destination.
* **[!UICONTROL Description]:** spécifiez des informations descriptives sur cette destination.
* **[!UICONTROL Type]:** (obligatoire) sélectionnez le type de destination souhaité :
   * **[!UICONTROL Bulk ID]** : synchroniser les identifiants entre différentes plateformes.
   * **[!UICONTROL Bulk Trait]** : envoyez en bloc des informations sur les caractéristiques à différentes plateformes.
   * **[!UICONTROL Bulk Segment]** : envoyez des informations de segment en bloc à différentes plateformes.
   * **[!UICONTROL S2S]** : utilisez des destinations serveur à serveur pour envoyer des données en temps réel et par lots à différentes plateformes.
* **[!UICONTROL Auto-Fill Destination Mapping]:** ([!UICONTROL S2S] uniquement) Sélectionnez une option :
   * **[!UICONTROL Segment ID]:** si vous sélectionnez ce paramètre, le mappage de la valeur de destination est renseigné avec l’identifiant de segment [!DNL Audience Manager].
   * **[!UICONTROL Integration Code Value]:** si vous sélectionnez ce paramètre, le mappage de la valeur de destination est renseigné avec le code d’intégration de segment [!DNL Audience Manager].
* **[!UICONTROL User ID Key]:** (obligatoire) sélectionnez la clé d’ID utilisateur souhaitée pour cette destination dans la liste déroulante.

Cet identifiant est utilisé comme identifiant de source de données principale. Cela détermine les ID d’utilisateur à émettre dans le fichier.

>[!NOTE]
>
>Pour le type de destination [!UICONTROL Bulk ID], vous ne pouvez pas utiliser l’[!UICONTROL User ID] [!DNL Audience Manager] ou l’identifiant [!DNL Adobe Experience Cloud].

Si votre identifiant de source de données ( [!UICONTROL DPID]) ne s’affiche pas dans la liste déroulante, vous devez cocher la case **[!UICONTROL Outbound]** au niveau de la source de données dans la page [Paramètres de Data Source](https://experienceleague.adobe.com/docs/audience-manager/user-guide/features/data-sources/manage-datasources.html?lang=fr).

* **[!UICONTROL Target Data Source]:** (obligatoire) sélectionnez la source de données de votre choix pour cette destination dans la liste déroulante. Ce paramètre active l’étiquetage des données sortantes, ce qui permet l’ingestion dans des systèmes distincts du côté des clients.
* **[!UICONTROL Foreign Account ID]:** spécifiez l’identifiant de compte étranger pour cette destination. Il s’agit de la valeur d’identification dans le système du destinataire pour ces données sortantes.
* **[!UICONTROL Outbound Sample Rate Denominator]:** Lorsque la quantité totale de données renvoyée est inconnue, utilisez ce paramètre pour renvoyer uniquement un échantillon de données, plutôt que la quantité totale. Ajustez le nombre ici pour représenter une fraction des données (par exemple, une valeur de &#39;100&#39; renvoie 1/100ème de la quantité régulière de données, une valeur de &#39;10&#39; renvoie 1/10ème de la quantité régulière de données). La valeur par défaut est « 1 », qui renvoie toutes les données.

## Données en temps réel (pour les destinations S2S) {#realtime-s2s}

Si vous créez une destination [!UICONTROL S2S], renseignez les champs ci-dessous :

**[!UICONTROL Servers]** : sélectionnez le serveur de `HTTP` de votre choix pour cette destination.
**[!UICONTROL Format]** : sélectionnez le format souhaité pour cette destination dans la liste déroulante : [!UICONTROL HTTP only].

>[!NOTE]
>
>Pour [!DNL S2S] uniquement, vous pouvez activer ou désactiver les destinations [!UICONTROL Realtime] ou [!UICONTROL Batch] à l’aide des curseurs Désactivé/Activé à l’écran. Vous ne pouvez pas désactiver les deux options.

## Données par lot {#batch-data}

Pour les destinations [!UICONTROL Bulk ID], [!UICONTROL Bulk Trait] ou [!UICONTROL Bulk Segment], renseignez les champs ci-dessous :

* **[!UICONTROL Protocol]** : (obligatoire) sélectionnez le protocole souhaité pour cette destination dans la liste déroulante :
   * **[!UICONTROL FTP]**
   * **[!UICONTROL HTTP]**
   * **[!UICONTROL S3]**
* **[!UICONTROL Servers]** : (obligatoire) sélectionnez le serveur souhaité pour cette destination dans la liste déroulante.
* **[!UICONTROL Format]** : (obligatoire) sélectionnez le format souhaité pour cette destination dans la liste déroulante : [!DNL HTTP] ou type de fichier, selon le protocole choisi ci-dessus.
* **[!UICONTROL Sync Type]** : (obligatoire) sélectionnez le type de synchronisation souhaité pour cette destination. Cela indique le niveau d’activités utilisateur que les clients souhaitent inclure dans les commandes sortantes. Sélectionnez **[!UICONTROL Customer]** si les clients souhaitent uniquement analyser les qualifications de segment à partir de leurs propriétés. Sélectionnez **[!UICONTROL Platform]** s’ils souhaitent inclure des qualifications de segment provenant d’activités hors site pour tous les clients [!DNL Audience Manager].
* **[!UICONTROL Customer]** : le fichier contient des utilisateurs actifs qui ont au moins 1 caractéristique réalisée uniquement sur les propriétés du client (associées à la [!UICONTROL PID] du client) pour la période sélectionnée. Vos clients doivent utiliser cette option pour envoyer leurs qualifications de segment *en temps réel* vers les destinations.
* **[!UICONTROL Platform]** : le fichier contient des utilisateurs actifs qui ont au moins 1 interaction en temps réel, qu’il s’agisse de la synchronisation des identifiants ou de la réalisation des caractéristiques, n’importe où sur toutes les propriétés de [!DNL Audience Manager] clients (associées à tous les PID clients) pour la période sélectionnée. Vos clients doivent utiliser cette option pour envoyer leurs qualifications de segment *total* vers les destinations.
* **[!UICONTROL Lifetime]** : le fichier contient des utilisateurs actifs consultés n’importe où sur les propriétés de tous [!DNL Audience Manager] clients depuis la création de la destination.
* **[!UICONTROL Sync Type Lookback Period]** : si vous sélectionnez [!UICONTROL Customer] ou [!UICONTROL Platform], sélectionnez une période. Les fichiers contiennent des utilisateurs actifs pour la période sélectionnée.
Sélectionnez ensuite le type de commande. Cela indique la fréquence et la portée de chaque intégration sortante avec les partenaires. Sélectionnez entre commandes incrémentielles et complètes.
* **[!UICONTROL Incremental Scheduled Run]** : à chaque exécution, [!DNL Audience Manager] ne sortira que les nouveaux utilisateurs nets qualifiés depuis la commande sortante précédente. Sélectionnez la période souhaitée [!DNL Audience Manager] effectuer des processus de synchronisation incrémentielle. Par exemple, vous pouvez sélectionner toutes les 24 heures, tous les sept jours, tous les 30 jours ou jamais.

<!--
I removed {importance="high"} from note for Exp League rendering. -Bob
-->

>[!NOTE]
>
>La toute première commande incrémentielle équivaut à une commande complète, car aucun utilisateur précédent n’a jamais été envoyé à la destination.

* **[!UICONTROL Full Sync Scheduled Run]** : avec chaque exécution, [!DNL Audience Manager] sortira tous les utilisateurs actifs depuis que la destination a été configurée pour la première fois. Sélectionnez la planification que vous [!DNL Audience Manager] utiliser pour exécuter des processus de synchronisation complète. Par exemple, vous pouvez sélectionner toutes les 24 heures, tous les sept jours, tous les 30 jours ou jamais.

<!--
I removed {importance="high"} from note for Exp League rendering. -Bob
-->

>[!NOTE]
>
>Nous vous recommandons d’utiliser des synchronisations incrémentielles plus fréquemment que des synchronisations complètes. Les synchronisations incrémentielles envoient uniquement des fichiers contenant de nouvelles réalisations de caractéristiques ou des synchronisations d’ID. Les synchronisations complètes envoient tous les fichiers, qu’ils contiennent de nouvelles réalisations ou des synchronisations d’ID. N’utilisez la configuration [!UICONTROL Full Sync Scheduled Run] que lorsque les clients ont besoin d’une copie complète de tous leurs utilisateurs afin de réduire le volume de données sortantes.

## Configurer les sources de données {#configure-data-sources}

Pour les destinations [!UICONTROL Bulk ID], [!UICONTROL Bulk Trait] ou [!UICONTROL Bulk Segment], renseignez les champs ci-dessous. Ces paramètres vous permettent d’envoyer toutes les données (caractéristiques, segments ou identifiants, en fonction du type sélectionné) associées aux sources de données.

* **[!UICONTROL All Unrestricted First Party Data]** : sélectionnez cette option pour utiliser toutes les sources de données propriétaires. Si vous sélectionnez cette option, les options [!UICONTROL Available Data Sources] sont désactivées.
* **[!UICONTROL Available Data Sources]** : utilisez les flèches pour déplacer les sources de données entre les zones de **[!UICONTROL Available Data Sources]** et de **[!UICONTROL In File Data Sources]**.

## Enregistrer et finaliser {#save-and-finalize}

Le bouton **[!UICONTROL Save]** est activé après avoir rempli tous les champs obligatoires. Cliquez sur **[!UICONTROL Save]** pour finaliser le processus de création de destination.

## Supprimer les destinations d’entreprise {#delete-company-destinations}

<!-- delete-company-destinations.xml -->

Pour supprimer une destination, procédez comme suit :

1. Cliquez sur **[!UICONTROL Companies]**, recherchez et cliquez sur l’entreprise souhaitée, puis cliquez sur l’onglet **[!UICONTROL Destinations]** .
1. Cliquez sur ![](assets/icon_delete.png) dans la colonne **[!UICONTROL Actions]** de la destination souhaitée.
1. Cliquez sur **[!UICONTROL OK]** pour confirmer la suppression.

>[!NOTE]
>
>Vous ne pouvez pas supprimer une destination si des segments lui sont mappés.
