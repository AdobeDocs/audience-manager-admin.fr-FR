---
description: Créez, modifiez et supprimez des destinations d’Audience Manager.
seo-description: Create, edit, and delete Audience Manager destinations.
seo-title: Manage Company Destinations
title: Gestion des destinations d’entreprise
uuid: d9a6bfb1-7629-44e0-b7d7-ece44f65ea2b
exl-id: a2e73613-07cd-4ab8-8c6e-be451ed50bfc
source-git-commit: 79415eba732c2a6d50f04124774664f788ccc78c
workflow-type: tm+mt
source-wordcount: '1068'
ht-degree: 1%

---

# Gestion des destinations d’entreprise {#manage-company-destinations}

Créez, modifiez et supprimez des destinations d’Audience Manager.

<!-- t_company_destinations.xml -->

Pour plus d’informations, voir [Destinations](https://experienceleague.adobe.com/docs/audience-manager/user-guide/features/destinations/destinations.html) dans le *Guide de l’utilisateur de l’Audience Manager*.

## Création ou modification des destinations d’entreprise {#create-edit-company-destinations}

Faites défiler les sections pour obtenir des instructions détaillées sur la création de destinations [!DNL Audience Manager] ou la modification de destinations existantes.

<!-- create-edit-company-destinations.xml -->

Consultez la [page d’intégration du partenaire Experience Cloud](https://wiki.corp.adobe.com/x/mPIMPw) avant de configurer des destinations. La page contient les informations spécifiques que vous devez renseigner pour chaque intégration de partenaire [!DNL Audience Manager].

Si votre client souhaite utiliser [!DNL Adobe Media Optimizer] comme destination dans [!DNL Audience Manager] , vous devez le configurer dans [!DNL Adobe Media Optimizer].

## Accédez à l’onglet Destinations {#navigate-destinations}

1. Cliquez sur **[!UICONTROL Companies]**, puis localisez et cliquez sur la société de votre choix pour afficher sa page [!UICONTROL Profile]. Vous pouvez utiliser la zone [!UICONTROL Search] ou les commandes de pagination en bas de la liste pour trouver la société souhaitée. Vous pouvez trier chaque colonne par ordre croissant ou décroissant en cliquant sur l’en-tête de la colonne de votre choix.
1. Cliquez sur l’onglet **[!UICONTROL Destinations]** .
1. Pour créer une destination, cliquez sur **[!UICONTROL Add Destination]**. Pour modifier une destination existante, cliquez sur son nom dans la colonne **[!UICONTROL Name]**.

## Paramètres de base {#basic-settings}

Renseignez les champs de la fenêtre **[!UICONTROL Basic Settings]**.

* **[!UICONTROL Name]:**  (obligatoire) indiquez le nom de cette destination.
* **[!UICONTROL Description]:** renseignez des informations descriptives sur cette destination.
* **[!UICONTROL Type]:**  (Obligatoire) Sélectionnez le type de destination souhaité :
   * **[!UICONTROL Bulk ID]**: Synchronisation des identifiants entre différentes plateformes.
   * **[!UICONTROL Bulk Trait]**: Envoyez des informations de caractéristiques en bloc vers différentes plateformes.
   * **[!UICONTROL Bulk Segment]**: Envoyez des informations sur les segments en bloc vers différentes plateformes.
   * **[!UICONTROL S2S]**: Utilisez les destinations serveur à serveur pour envoyer des données en temps réel et par lots à différentes plateformes.
* **[!UICONTROL Auto-Fill Destination Mapping]:**  ( [!UICONTROL S2S] uniquement) Sélectionnez une option :
   * **[!UICONTROL Segment ID]:** Si vous sélectionnez ce paramètre, le mappage des valeurs de destination est renseigné avec l’ID de  [!DNL Audience Manager] segment.
   * **[!UICONTROL Integration Code Value]:** Si vous sélectionnez ce paramètre, le mappage des valeurs de destination est renseigné avec le code d’intégration du  [!DNL Audience Manager] segment.
* **[!UICONTROL User ID Key]:**  (Obligatoire) Sélectionnez la clé d’ID utilisateur de votre choix pour cette destination dans la liste déroulante.

Cet identifiant est utilisé comme identifiant de source de données principal. Cela détermine les ID utilisateur à délimiter dans le fichier.

>[!NOTE]
>
>Pour le type de destination [!UICONTROL Bulk ID] , vous ne pouvez pas utiliser l’ID [!DNL Audience Manager] [!UICONTROL User ID] ou l’ID [!DNL Adobe Experience Cloud].

Si votre ID de source de données ( [!UICONTROL DPID]) ne s’affiche pas dans la liste déroulante, vous devez cocher la case **[!UICONTROL Outbound]** au niveau de la source de données sur la [page Paramètres de source de données](https://experienceleague.adobe.com/docs/audience-manager/user-guide/features/data-sources/manage-datasources.html).

* **[!UICONTROL Target Data Source]:**  (Obligatoire) Sélectionnez la source de données de votre choix pour cette destination dans la liste déroulante. Ce paramètre permet l’étiquetage des données délimitées, ce qui permet l’ingestion dans des systèmes distincts du côté des clients.
* **[!UICONTROL Foreign Account ID]:** indiquez l’identifiant de compte étranger pour cette destination. Il s’agit de la valeur d’identification dans le système du destinataire pour ces données délimitées.
* **[!UICONTROL Outbound Sample Rate Denominator]:** Lorsque la quantité totale de données renvoyées est inconnue, utilisez ce paramètre pour renvoyer uniquement un échantillon de données, plutôt que la quantité totale. Ajustez le nombre ici pour représenter une fraction des données (par exemple, une valeur de &quot;100&quot; renvoie 1/100la quantité normale de données, une valeur de &quot;10&quot; renvoie 1/10 la quantité normale de données). La valeur par défaut est &quot;1&quot;, ce qui renvoie toutes les données.

## Données en temps réel (pour les destinations S2S) {#realtime-s2s}

Si vous créez une destination [!UICONTROL S2S], renseignez les champs ci-dessous :

**[!UICONTROL Servers]**: Sélectionnez le  `HTTP` serveur souhaité pour cette destination.
**[!UICONTROL Format]**: Sélectionnez le format de votre choix pour cette destination dans la liste déroulante :  [!UICONTROL HTTP only].

>[!NOTE]
>
>Pour [!DNL S2S] uniquement, vous pouvez activer ou désactiver les destinations [!UICONTROL Realtime] ou [!UICONTROL Batch] à l’aide des curseur de désactivation/d’activation à l’écran. Vous ne pouvez pas désactiver les deux options.

## Données par lots {#batch-data}

Pour les destinations [!UICONTROL Bulk ID], [!UICONTROL Bulk Trait] ou [!UICONTROL Bulk Segment], renseignez les champs ci-dessous :

* **[!UICONTROL Protocol]**: (Obligatoire) Sélectionnez le protocole souhaité pour cette destination dans la liste déroulante :
   * **[!UICONTROL FTP]**
   * **[!UICONTROL HTTP]**
   * **[!UICONTROL S3]**
* **[!UICONTROL Servers]**: (Obligatoire) Sélectionnez le serveur souhaité pour cette destination dans la liste déroulante.
* **[!UICONTROL Format]**: (Obligatoire) Sélectionnez le format souhaité pour cette destination dans la liste déroulante :  [!DNL HTTP] ou type de fichier, en fonction du protocole choisi ci-dessus.
* **[!UICONTROL Sync Type]**: (Obligatoire) Sélectionnez le type de synchronisation souhaité pour cette destination. Cela indique le niveau d’activités utilisateur que les clients souhaitent inclure dans les commandes sortantes. Sélectionnez **[!UICONTROL Customer]** si les clients souhaitent uniquement analyser les qualifications de segments à partir de leurs propriétés. Sélectionnez **[!UICONTROL Platform]** s’ils souhaitent inclure les qualifications de segments provenant d’activités hors site pour tous les clients [!DNL Audience Manager].
* **[!UICONTROL Customer]**: Le fichier contient des utilisateurs principaux qui ont au moins une réalisation de caractéristiques sur les propriétés du client (associées à  [!UICONTROL PID]) pendant la période sélectionnée. Vos clients doivent utiliser cette option pour sortir leurs *qualifications de segment en temps réel* vers les destinations.
* **[!UICONTROL Platform]**: Le fichier contient des utilisateurs principaux qui ont au moins une interaction en temps réel, que ce soit la synchronisation des identifiants ou la réalisation de caractéristiques, n’importe où sur les propriétés de tous les  [!DNL Audience Manager] clients (associées à tous les PID client) pendant la période sélectionnée. Vos clients doivent utiliser cette option pour sortir leurs *qualifications de segment* totales vers les destinations.
* **[!UICONTROL Lifetime]**: Le fichier contient des utilisateurs principaux, que l’on voit n’importe où sur toutes les propriétés de tous les  [!DNL Audience Manager] clients depuis la création de la destination.
* **[!UICONTROL Sync Type Lookback Period]**: Si vous sélectionnez  [!UICONTROL Customer] ou  [!UICONTROL Platform], sélectionnez une période. Les fichiers contiennent des utilisateurs principaux pour la période sélectionnée.
Sélectionnez ensuite le type de commande. Cela indique la fréquence et la portée de chaque intégration sortante avec les partenaires. Effectuez une sélection entre les commandes incrémentielles et complètes.
* **[!UICONTROL Incremental Scheduled Run]**: Pour chaque exécution,  [!DNL Audience Manager] ne sortira que les nouveaux utilisateurs nets qualifiés depuis l’ordre sortant précédent. Sélectionnez la période souhaitée pendant laquelle [!DNL Audience Manager] doit exécuter des processus de synchronisation incrémentielle. Par exemple, vous pouvez sélectionner toutes les 24 heures, tous les sept jours, tous les 30 jours ou jamais.

<!--
I removed {importance="high"} from note for Exp League rendering. -Bob
-->

>[!NOTE]
>
>La première commande incrémentielle équivaut à une commande complète, car aucun utilisateur précédent n’a jamais été envoyé à la destination.

* **[!UICONTROL Full Sync Scheduled Run]**: À chaque exécution,  [!DNL Audience Manager] sortira tous les utilisateurs principaux depuis la configuration initiale de la destination. Sélectionnez la planification que vous souhaitez que [!DNL Audience Manager] utilise pour effectuer des processus de synchronisation complets. Par exemple, vous pouvez sélectionner toutes les 24 heures, tous les sept jours, tous les 30 jours ou jamais.

<!--
I removed {importance="high"} from note for Exp League rendering. -Bob
-->

>[!NOTE]
>
>Nous vous recommandons d’utiliser plus fréquemment des synchronisations incrémentielles que des synchronisations complètes. Les synchronisations incrémentielles envoient uniquement les fichiers qui contiennent de nouvelles réalisations de caractéristiques ou synchronisations des identifiants. Les synchronisations complètes envoient tous les fichiers, qu’ils incluent de nouvelles réalisations ou synchronisations des identifiants. N’utilisez la configuration [!UICONTROL Full Sync Scheduled Run] que lorsque les clients ont besoin d’une copie complète de tous leurs utilisateurs, afin de réduire le volume des données sortantes.

## Configuration des sources de données {#configure-data-sources}

Pour les destinations [!UICONTROL Bulk ID], [!UICONTROL Bulk Trait] ou [!UICONTROL Bulk Segment], renseignez les champs ci-dessous. Ces paramètres vous permettent d’envoyer toutes les données (caractéristiques, segments ou identifiants, selon le type sélectionné) associées aux sources de données.

* **[!UICONTROL All Unrestricted First Party Data]**: Sélectionnez cette option pour utiliser toutes les sources de données propriétaires. Si vous sélectionnez cette option, les options [!UICONTROL Available Data Sources] sont désactivées.
* **[!UICONTROL Available Data Sources]**: Utilisez les flèches pour déplacer les sources de données entre les  **[!UICONTROL Available Data Sources]** zones  **[!UICONTROL In File Data Sources]** et .

## Enregistrer et finaliser {#save-and-finalize}

Le bouton **[!UICONTROL Save]** est activé après le remplissage de tous les champs obligatoires. Cliquez sur **[!UICONTROL Save]** pour finaliser le processus de création de destination.

## Suppression de destinations d’entreprise {#delete-company-destinations}

<!-- delete-company-destinations.xml -->

Pour supprimer une destination :

1. Cliquez sur **[!UICONTROL Companies]**, recherchez la société de votre choix, puis cliquez sur l’onglet **[!UICONTROL Destinations]** .
1. Cliquez sur ![](assets/icon_delete.png) dans la colonne **[!UICONTROL Actions]** de la destination souhaitée.
1. Cliquez sur **[!UICONTROL OK]** pour confirmer la suppression.

>[!NOTE]
>
>Vous ne pouvez pas supprimer une destination si des segments y sont associés.
