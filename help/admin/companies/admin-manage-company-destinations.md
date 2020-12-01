---
description: Créez, modifiez et supprimez des destinations d’Audience Manager.
seo-description: Créez, modifiez et supprimez des destinations d’Audience Manager.
seo-title: Gestion des destinations d’entreprise
title: Gestion des destinations d’entreprise
uuid: d9a6bfb1-7629-44e0-b7d7-ece44f65ea2b
translation-type: tm+mt
source-git-commit: f247457004a624297ddc8847dd256dbb7d8da418
workflow-type: tm+mt
source-wordcount: '1082'
ht-degree: 1%

---


# Gestion des destinations d’entreprise {#manage-company-destinations}

Créez, modifiez et supprimez des destinations d’Audience Manager.

<!-- t_company_destinations.xml -->

Pour plus d&#39;informations, consultez [Destinations](https://docs.adobe.com/content/help/en/audience-manager/user-guide/features/destinations/destinations.html) dans le *Guide de l&#39;utilisateur de l&#39;Audience Manager*.

## Création ou modification des destinations d’entreprise {#create-edit-company-destinations}

Faites défiler les sections pour obtenir des instructions détaillées sur la création de nouvelles destinations [!DNL Audience Manager] ou la modification de destinations existantes.

<!-- create-edit-company-destinations.xml -->

Consultez la [page d’intégration des partenaires Experience Cloud](https://wiki.corp.adobe.com/x/mPIMPw) avant de configurer les destinations. La page contient les informations spécifiques que vous devez renseigner pour chaque intégration de partenaire [!DNL Audience Manager].

Si votre client souhaite utiliser [!DNL Adobe Media Optimizer] en tant que destination dans [!DNL Audience Manager], vous devez le configurer dans [!DNL Adobe Media Optimizer].

## Accédez à l&#39;onglet Destinations {#navigate-destinations}

1. Cliquez sur **[!UICONTROL Companies]**, puis recherchez et cliquez sur la société souhaitée pour afficher sa page [!UICONTROL Profile]. Vous pouvez utiliser la zone [!UICONTROL Search] ou les commandes de pagination au bas de la liste pour trouver la société souhaitée. Vous pouvez trier chaque colonne par ordre croissant ou décroissant en cliquant sur l’en-tête de la colonne de votre choix.
1. Cliquez sur l&#39;onglet **[!UICONTROL Destinations]**.
1. Pour créer une nouvelle destination, cliquez sur **[!UICONTROL Add Destination]**. Pour modifier une destination existante, cliquez sur son nom dans la colonne **[!UICONTROL Name]**.

## Paramètres de base {#basic-settings}

Renseignez les champs de la fenêtre **[!UICONTROL Basic Settings]**.

* **[!UICONTROL Name]:** (Obligatoire) Indiquez le nom de cette destination.
* **[!UICONTROL Description]:** Spécifiez des informations descriptives sur cette destination.
* **[!UICONTROL Type]:** (Obligatoire) Sélectionnez un type de destination :
   * **[!UICONTROL Bulk ID]**: Synchroniser les ID entre différentes plateformes.
   * **[!UICONTROL Bulk Trait]**: Envoyez des informations de caractéristiques en bloc à différentes plateformes.
   * **[!UICONTROL Bulk Segment]**: Envoyez des informations de segment en bloc vers différentes plateformes.
   * **[!UICONTROL S2S]**: Utilisez les destinations serveur à serveur pour envoyer des données en temps réel et par lot à différentes plates-formes.
* **[!UICONTROL Auto-Fill Destination Mapping]:** (  [!UICONTROL S2S] uniquement) Sélectionnez une option :
   * **[!UICONTROL Segment ID]:** Si vous sélectionnez ce paramètre, le mappage des valeurs de destination est renseigné avec l’ID de  [!DNL Audience Manager] segment.
   * **[!UICONTROL Integration Code Value]:** Si vous sélectionnez ce paramètre, le mappage des valeurs de destination est renseigné avec le code d’intégration de  [!DNL Audience Manager] segment.
* **[!UICONTROL User ID Key]:** (Obligatoire) Sélectionnez la clé d’ID utilisateur de votre choix pour cette destination dans la liste déroulante.

Cet ID est utilisé comme ID de source de données maître. Cela détermine les ID utilisateur à délimiter dans le fichier.

>[!NOTE]
>
>Pour le type de destination [!UICONTROL Bulk ID], vous ne pouvez pas utiliser l&#39;ID [!DNL Audience Manager] [!UICONTROL User ID] ou l&#39;ID [!DNL Adobe Experience Cloud].

Si votre ID de source de données ( [!UICONTROL DPID]) ne s’affiche pas dans la liste déroulante, vous devez cocher la case **[!UICONTROL Outbound]** au niveau de la source de données sur la page [Paramètres de source de données](https://docs.adobe.com/content/help/en/audience-manager/user-guide/features/data-sources/manage-datasources.html).

* **[!UICONTROL Target Data Source]:** (Obligatoire) Sélectionnez la source de données de votre choix pour cette destination dans la liste déroulante. Ce paramètre permet l&#39;étiquetage des données délimitées, ce qui permet l&#39;assimilation dans des systèmes distincts côté client.
* **[!UICONTROL Foreign Account ID]:** indiquez l’identifiant de compte étranger pour cette destination. Il s’agit de la valeur d’identification du système des destinataires pour ces données délimitées.
* **[!UICONTROL Outbound Sample Rate Denominator]:** Lorsque le nombre total de données renvoyées est inconnu, utilisez ce paramètre pour renvoyer uniquement un échantillon de données, plutôt que le total. Ajustez le nombre ici pour représenter une fraction des données (par exemple, une valeur de &quot;100&quot; renvoie 1/100 de la quantité normale de données, une valeur de &quot;10&quot; renvoie 1/10 de la quantité normale de données). La valeur par défaut est &quot;1&quot;, ce qui renvoie toutes les données.

## Données en temps réel (pour les destinations S2S) {#realtime-s2s}

Si vous créez une destination [!UICONTROL S2S], renseignez les champs ci-dessous :

**[!UICONTROL Servers]**: Sélectionnez le  `HTTP` serveur de votre choix pour cette destination.
**[!UICONTROL Format]**: Sélectionnez le format de destination dans la liste déroulante :  [!UICONTROL HTTP only].

>[!NOTE]
>
>Pour [!DNL S2S] uniquement, vous pouvez activer ou désactiver les destinations [!UICONTROL Realtime] ou [!UICONTROL Batch] à l’aide des curseurs Désactivé/Activé à l’écran. Vous ne pouvez pas désactiver les deux options.

## Données du lot {#batch-data}

Pour les destinations [!UICONTROL Bulk ID], [!UICONTROL Bulk Trait] ou [!UICONTROL Bulk Segment], renseignez les champs ci-dessous :

* **[!UICONTROL Protocol]**: (Obligatoire) Sélectionnez le protocole souhaité pour cette destination dans la liste déroulante :
   * **[!UICONTROL FTP]**
   * **[!UICONTROL HTTP]**
   * **[!UICONTROL S3]**
* **[!UICONTROL Servers]**: (Obligatoire) Sélectionnez le serveur de votre choix pour cette destination dans la liste déroulante.
* **[!UICONTROL Format]**: (Obligatoire) Sélectionnez le format de destination dans la liste déroulante :  [!DNL HTTP] ou type de fichier, selon le protocole choisi ci-dessus.
* **[!UICONTROL Sync Type]**: (Obligatoire) Sélectionnez le type de synchronisation souhaité pour cette destination. Cela indique le niveau d&#39;activités utilisateur que les clients souhaitent inclure dans les commandes sortantes. Sélectionnez **[!UICONTROL Customer]** si les clients souhaitent uniquement analyser les qualifications des segments à partir de leurs propriétés. Sélectionnez **[!UICONTROL Platform]** si vous souhaitez inclure les qualifications des segments provenant d&#39;activités hors site pour tous les clients [!DNL Audience Manager].
* **[!UICONTROL Customer]**: Le fichier contient des utilisateurs principaux qui ont réalisé au moins 1 caractéristique uniquement sur les propriétés du client (associées à celles du client  [!UICONTROL PID]) pendant la période sélectionnée. Vos clients doivent utiliser cette option pour exporter leurs *qualifications de segment en temps réel* vers les destinations.
* **[!UICONTROL Platform]**: Le fichier contient des utilisateurs principaux qui ont au moins 1 interaction en temps réel, qu’il s’agisse de la synchronisation des identifiants ou de la réalisation des caractéristiques, n’importe où sur les propriétés de tous les  [!DNL Audience Manager] clients (associées à tous les PID client) pendant la période sélectionnée. Vos clients doivent utiliser cette option pour exporter leurs *qualifications de segment* totales vers les destinations.
* **[!UICONTROL Lifetime]**: Le fichier contient des utilisateurs principaux, visibles n’importe où sur les propriétés de tous les  [!DNL Audience Manager] clients depuis la création de la destination.
* **[!UICONTROL Sync Type Lookback Period]**: Si vous sélectionnez  [!UICONTROL Customer] ou  [!UICONTROL Platform], sélectionnez une période. Les fichiers contiennent des utilisateurs principaux pour la période sélectionnée.
Sélectionnez ensuite le type de commande. Cela indique la fréquence et la portée de chaque intégration sortante avec les partenaires. Effectuez une sélection entre les commandes incrémentielles et complètes.
* **[!UICONTROL Incremental Scheduled Run]**: Pour chaque exécution,  [!DNL Audience Manager] les nouveaux utilisateurs nets sortants sont uniquement qualifiés depuis l’ordre sortant précédent. Sélectionnez la période souhaitée pour laquelle [!DNL Audience Manager] doit effectuer des processus de synchronisation incrémentielle. Par exemple, vous pouvez sélectionner toutes les 24 heures, tous les sept jours, tous les 30 jours ou jamais.

<!--
I removed {importance="high"} from note for Exp League rendering. -Bob
-->

>[!NOTE]
>
>La première commande incrémentielle équivaut à une commande complète, car aucun utilisateur précédent n’a jamais été envoyé à la destination.

* **[!UICONTROL Full Sync Scheduled Run]**: A chaque exécution, tous les utilisateurs principaux  [!DNL Audience Manager] sortiront de la liste depuis la première configuration de la destination. Sélectionnez la planification que [!DNL Audience Manager] doit utiliser pour effectuer des processus de synchronisation complets. Par exemple, vous pouvez sélectionner toutes les 24 heures, tous les sept jours, tous les 30 jours ou jamais.

<!--
I removed {importance="high"} from note for Exp League rendering. -Bob
-->

>[!NOTE]
>
>Nous vous recommandons d’utiliser des synchronisations incrémentielles plus fréquemment que des synchronisations complètes. Les synchronisations incrémentielles envoient uniquement des fichiers qui contiennent de nouvelles réalisations de caractéristiques ou synchronisations d’identifiants. Les synchronisations complètes envoient tous les fichiers, qu’ils incluent ou non de nouvelles réalisations ou synchronisations d’identifiants. N&#39;utilisez la configuration [!UICONTROL Full Sync Scheduled Run] que lorsque les clients ont besoin d&#39;une copie complète de tous leurs utilisateurs, afin de réduire le volume de données sortant.

## Configurer les sources de données {#configure-data-sources}

Pour les destinations [!UICONTROL Bulk ID], [!UICONTROL Bulk Trait] ou [!UICONTROL Bulk Segment], renseignez les champs ci-dessous. Ces paramètres vous permettent d’envoyer toutes les données (caractéristiques, segments ou identifiants, selon le type sélectionné) associées aux sources de données.

* **[!UICONTROL All Unrestricted First Party Data]**: Sélectionnez cette option pour utiliser toutes les sources de données propriétaires. Si vous sélectionnez cette option, les options [!UICONTROL Available Data Sources] sont désactivées.
* **[!UICONTROL Available Data Sources]**: Utilisez les flèches pour déplacer les sources de données entre les  **[!UICONTROL Available Data Sources]** zones et les  **[!UICONTROL In File Data Sources]** zones.

## Enregistrer et finaliser {#save-and-finalize}

Le bouton **[!UICONTROL Save]** est activé après avoir rempli tous les champs obligatoires. Cliquez sur **[!UICONTROL Save]** pour finaliser le processus de création de destination.

## Supprimer les destinations de Société {#delete-company-destinations}

<!-- delete-company-destinations.xml -->

Pour supprimer une destination :

1. Cliquez sur **[!UICONTROL Companies]**, recherchez et cliquez sur la société souhaitée, puis cliquez sur l&#39;onglet **[!UICONTROL Destinations]**.
1. Cliquez sur ![](assets/icon_delete.png) dans la colonne **[!UICONTROL Actions]** de la destination souhaitée.
1. Cliquez sur **[!UICONTROL OK]** pour confirmer la suppression.

>[!NOTE]
>
>Vous ne pouvez pas supprimer une destination si des segments y sont associés.