---
description: Créez, modifiez et supprimez des destinations Audience Manager.
seo-description: Créez, modifiez et supprimez des destinations Audience Manager.
seo-title: Gérer les destinations de l'entreprise
title: Gérer les destinations de l'entreprise
uuid: d 9 a 6 bfb 1-7629-44 e 0-b 7 d 7-ece 44 f 65 ea 2 b
translation-type: tm+mt
source-git-commit: 57d7a92265e565b6c411e4cfa5c579e40eb837b3

---


# Gérer les destinations de l'entreprise {#manage-company-destinations}

Créez, modifiez et supprimez des destinations Audience Manager.

<!-- t_company_destinations.xml -->

Pour plus d'informations, reportez-vous à [la section Destinations](https://docs.adobe.com/content/help/en/audience-manager/user-guide/features/destinations/destinations.html) du Guide de l'utilisateur *d'Audience Manager*.

## Créer ou modifier des destinations de société {#create-edit-company-destinations}

Faites défiler les sections pour obtenir des instructions détaillées sur la création [!DNL Audience Manager] de nouvelles destinations ou la modification de destinations existantes.

<!-- create-edit-company-destinations.xml -->

Consultez la page d'intégration des partenaires [Experience Cloud](https://wiki.corp.adobe.com/x/mPIMPw) avant de définir les destinations - vers le haut. La page contient les informations spécifiques que vous devez renseigner pour chaque [!DNL Audience Manager] intégration de partenaire.

Si votre client souhaite utiliser [!DNL Adobe Media Optimizer] comme destination dans [!DNL Audience Manager] , vous devez le configurer [!DNL Adobe Media Optimizer]dans.

## Navigate to the Destinations Tab {#navigate-destinations}

1. Cliquez sur **[!UICONTROL Companies]**, puis localisez et cliquez sur la société souhaitée pour afficher sa [!UICONTROL Profile] page. Vous pouvez utiliser [!UICONTROL Search] la zone ou les commandes de pagination au bas de la liste pour trouver la société souhaitée. Vous pouvez trier chaque colonne par ordre croissant ou décroissant en cliquant sur l'en-tête de la colonne concernée.
1. Click the **[!UICONTROL Destinations]** tab.
1. Pour créer une destination, cliquez **[!UICONTROL Add Destination]** sur. To edit an existing destination, click the destination's name in the **[!UICONTROL Name]** column.

## Paramètres de base {#basic-settings}

Fill in the fields in the **[!UICONTROL Basic Settings]** window.

* **[!UICONTROL Name]:** (Obligatoire) Indiquez le nom de cette destination.
* **[!UICONTROL Description]:** Spécifiez des informations descriptives sur cette destination.
* **[!UICONTROL Type]:** (Obligatoire) Sélectionnez le type de destination souhaité :
   * **[!UICONTROL Bulk ID]**: Identifiants de synchronisation entre différentes plateformes.
   * **[!UICONTROL Bulk Trait]**: Envoyez des informations de caractéristique en bloc sur différentes plateformes.
   * **[!UICONTROL Bulk Segment]**: Envoyez les informations de segment en bloc sur différentes plateformes.
   * **[!UICONTROL S2S]**: Utilisez les destinations serveur à serveur pour envoyer des données en temps réel et par lots à différentes plateformes.
* **[!UICONTROL Auto-Fill Destination Mapping]:** ( [!UICONTROL S2S] uniquement) Sélectionnez une option :
   * **[!UICONTROL Segment ID]:** Si vous sélectionnez ce paramètre, le mappage de valeur de destination est rempli avec l'ID [!DNL Audience Manager] de segment.
   * **[!UICONTROL Integration Code Value]:** Si vous sélectionnez ce paramètre, le mappage de valeur de destination est rempli avec le code d'intégration [!DNL Audience Manager] de segment.
* **[!UICONTROL User ID Key]:** (Obligatoire) Sélectionnez la clé utilisateur - id de cette destination dans la liste déroulante.

Cet ID est utilisé comme ID de source de données maître. Ceci détermine l'utilisateur - les identifiants à afficher dans le fichier.

>[!NOTE]
>
>Pour le type [!UICONTROL Bulk ID] de destination, vous ne pouvez pas utiliser l' [!DNL Audience Manager][!UICONTROL User ID] ID ou [!DNL Adobe Experience Cloud] l'ID.

Si votre ID de source de données ( [!UICONTROL DPID]) ne s'affiche pas dans la liste déroulante, vous devez cocher la **[!UICONTROL Outbound]** case au niveau source de données de la [page Paramètres de source de données](https://docs.adobe.com/content/help/en/audience-manager/user-guide/features/data-sources/manage-datasources.html).

* **[!UICONTROL Target Data Source]:** (Obligatoire) Sélectionnez la source de données souhaitée pour cette destination dans la liste déroulante. Ce paramètre permet l'étiquetage des données semi-limitées, ce qui permet d'assimiler des systèmes distincts côté client.
* **[!UICONTROL Foreign Account ID]:** Indiquez l'ID de compte étranger pour cette destination. Il s'agit de la valeur d'identification du système du destinataire pour ces données finalisées.
* **[!UICONTROL Outbound Sample Rate Denominator]:** Lorsque la quantité totale de données renvoyées est inconnue, utilisez ce paramètre pour renvoyer uniquement un échantillon de données, plutôt que le montant complet. Ajustez le nombre ici pour représenter une fraction des données (par exemple, la valeur « 100 » renvoie 1/100 ème la quantité régulière de données, la valeur « 10 » renvoie 1/10 e la quantité régulière de données). La valeur par défaut est 1, qui renvoie toutes les données.

## Données en temps réel (pour les destinations S 2 S) {#realtime-s2s}

Si vous créez [!UICONTROL S2S] une destination, renseignez les champs ci-dessous :

**[!UICONTROL Servers]**: Sélectionnez le serveur de votre `HTTP` choix pour cette destination.
**[!UICONTROL Format]**: Sélectionnez le format souhaité pour cette destination dans la liste déroulante : [!UICONTROL HTTP only].

>[!NOTE]
>
>Pour [!DNL S2S] seulement, vous pouvez activer ou désactiver l'une [!UICONTROL Realtime] ou l'autre [!UICONTROL Batch] des destinations à l'aide des curseurs Désactivé/Activé. Vous ne pouvez pas désactiver les deux options.

## Données par lots {#batch-data}

Pour [!UICONTROL Bulk ID]les [!UICONTROL Bulk Trait] destinations ou [!UICONTROL Bulk Segment] les destinations, renseignez les champs ci-dessous :

* **[!UICONTROL Protocol]**: (Obligatoire) Sélectionnez le protocole souhaité pour cette destination dans la liste déroulante :
   * **[!UICONTROL FTP]**
   * **[!UICONTROL HTTP]**
   * **[!UICONTROL S3]**
* **[!UICONTROL Servers]**: (Obligatoire) Sélectionnez le serveur souhaité pour cette destination dans la liste déroulante.
* **[!UICONTROL Format]**: (Obligatoire) Sélectionnez le format souhaité pour cette destination dans la liste déroulante : [!DNL HTTP] ou le type de fichier, selon le protocole choisi ci-dessus.
* **[!UICONTROL Sync Type]**: (Obligatoire) Sélectionnez le type de synchronisation souhaité pour cette destination. Cela indique le niveau des activités utilisateur que les clients souhaiteraient inclure dans les commandes sortantes. Sélectionnez **[!UICONTROL Customer]** si les clients souhaitent uniquement analyser les qualifications des segments à partir de leurs propriétés. Sélectionnez **[!UICONTROL Platform]** s'ils souhaitent inclure des critères de segmentation des activités hors site sur tous [!DNL Audience Manager] les clients.
* **[!UICONTROL Customer]**: Le fichier contient des utilisateurs actifs ayant au moins 1 rendu de caractéristiques sur les propriétés du client (associé aux clients [!UICONTROL PID]) pour la période sélectionnée. Vos clients doivent utiliser cette option pour dépasser les critères de segmentation en *temps réel* des destinations.
* **[!UICONTROL Platform]**: Le fichier contient des utilisateurs actifs ayant au moins 1 interaction en temps réel, qu'il s'agisse de synchronisation des identifiants ou de concrétisation des caractéristiques, n'importe où sur les propriétés [!DNL Audience Manager] des clients (associé à tous les identifiants d'utilisateur client) pour la période sélectionnée. Vos clients doivent utiliser cette option pour dépasser les *limites de* segmentation totale des destinations.
* **[!UICONTROL Lifetime]**: Le fichier contient des utilisateurs actifs vus n'importe où sur les propriétés [!DNL Audience Manager] des clients depuis la création de la destination.
* **[!UICONTROL Sync Type Lookback Period]**: Si vous sélectionnez [!UICONTROL Customer] ou [!UICONTROL Platform]sélectionnez une période. Les fichiers contiennent des utilisateurs actifs pour la période sélectionnée.
Sélectionnez ensuite le type de commande. Ceci indique la fréquence et la portée de chaque intégration sortante avec des partenaires. Sélectionnez entre les commandes incrémentielles et complètes.
* **[!UICONTROL Incremental Scheduled Run]**: Avec chaque exécution, [!DNL Audience Manager] ne sortira que les nouveaux utilisateurs net qualifiés depuis l'ordre sortant précédent. Sélectionnez la période souhaitée pour effectuer [!DNL Audience Manager] des processus de synchronisation incrémentielle. Par exemple, vous pouvez sélectionner toutes les 24 heures, tous les sept jours, tous les 30 jours ou jamais.

>[!NOTE] {importance = « high »}
>
>La première - la commande incrémentielle est équivalente à un ordre complet, car aucun utilisateur précédent n'a été envoyé vers la destination.

* **[!UICONTROL Full Sync Scheduled Run]**: A chaque exécution, [!DNL Audience Manager] tous les utilisateurs actifs sont sortants depuis la première configuration de la destination. Sélectionnez le planning que vous souhaitez [!DNL Audience Manager] utiliser pour effectuer des processus de synchronisation complets. Par exemple, vous pouvez sélectionner toutes les 24 heures, tous les sept jours, tous les 30 jours ou jamais.

>[!NOTE] {importance = « high »}
>
>Nous vous recommandons d'utiliser des synchronisations incrémentielles plus fréquentes que les synchronisations complètes. La synchronisation incrémentielle n'envoie que les fichiers qui contiennent de nouvelles realizations de caractéristiques ou des synchronisations d'ID. Les synchronisations complètes envoient tous les fichiers, qu'ils incluent ou non de nouvelles relations ou synchronisations d'ID. N'utilisez la [!UICONTROL Full Sync Scheduled Run] configuration que lorsque les clients ont besoin d'une copie complète de tous leurs utilisateurs, afin de réduire le volume de données sortant.

## Configuration des sources de données {#configure-data-sources}

Pour [!UICONTROL Bulk ID]les [!UICONTROL Bulk Trait][!UICONTROL Bulk Segment] destinations, renseignez les champs ci-dessous. Ces paramètres vous permettent d'envoyer toutes les données (caractéristiques, segments ou ID, selon le type sélectionné) associées aux sources de données.

* **[!UICONTROL All Unrestricted First Party Data]**: Choisissez d'utiliser toutes les sources de données propriétaires. Si vous sélectionnez cette option, les [!UICONTROL Available Data Sources] options sont désactivées.
* **[!UICONTROL Available Data Sources]**: Utilisez les flèches pour déplacer les sources de données entre les champs **[!UICONTROL Available Data Sources]** et **[!UICONTROL In File Data Sources]** les zones.

## Enregistrer et finaliser {#save-and-finalize}

**[!UICONTROL Save]** Le bouton est activé après avoir rempli tous les champs obligatoires. Cliquez sur **[!UICONTROL Save]** pour finaliser le processus de destination de création.

## Supprimer les destinations de société {#delete-company-destinations}

<!-- delete-company-destinations.xml -->

Pour supprimer une destination :

1. Cliquez sur **[!UICONTROL Companies]**, localisez et cliquez sur la société souhaitée, puis cliquez sur l **[!UICONTROL Destinations]** 'onglet.
1. Cliquez ![](assets/icon_delete.png) dans la **[!UICONTROL Actions]** colonne de la destination souhaitée.
1. Cliquez sur **[!UICONTROL OK]pour confirmer la suppression.**

>[!NOTE]
>
>Vous ne pouvez pas supprimer une destination si des segments lui sont associés.