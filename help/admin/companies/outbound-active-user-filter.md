---
description: Suivez ces instructions pour générer un fichier de synchronisation complet qui inclut uniquement les utilisateurs récemment principaux. Vous pouvez filtrer les utilisateurs principaux afin de transmettre les données pertinentes à un système de ciblage sur site ou de limiter la taille des fichiers envoyés à un DSP. Vous ne pouvez pas utiliser ce filtre avec une synchronisation incrémentielle.
seo-description: Suivez ces instructions pour générer un fichier de synchronisation complet qui inclut uniquement les utilisateurs récemment principaux. Vous pouvez filtrer les utilisateurs principaux afin de transmettre les données pertinentes à un système de ciblage sur site ou de limiter la taille des fichiers envoyés à un DSP. Vous ne pouvez pas utiliser ce filtre avec une synchronisation incrémentielle.
seo-title: Filtrage des données sortantes par utilisateurs actifs uniquement
title: Filtrage des données sortantes par utilisateurs actifs uniquement
uuid: a2b4a385-eee3-458c-b978-09509cacb397
translation-type: tm+mt
source-git-commit: be661580da839ce6332a0ad827dec08e854abe54
workflow-type: tm+mt
source-wordcount: '276'
ht-degree: 8%

---


# Filtrage des données sortantes par utilisateurs actifs uniquement {#filter-outbound-data-by-active-users-only}

Suivez ces instructions pour générer un fichier de synchronisation complet qui inclut uniquement les utilisateurs récemment principaux. Vous pouvez filtrer les utilisateurs principaux afin de transmettre les données pertinentes à un système de ciblage sur site ou de limiter la taille des fichiers envoyés à un DSP. Vous ne pouvez pas utiliser ce filtre avec une synchronisation incrémentielle.

>[!NOTE]
>
>Il n’est pas nécessaire qu’un visiteur soit visible sur un site client sélectionné ou dans son trafic publicitaire pour être considéré comme &quot;principal&quot;. Ils peuvent être vus par n&#39;importe quel client ou partenaire [!DNL Audience Manager] pour être considérés comme &quot;principaux&quot;.

Pour filtrer par utilisateurs principaux uniquement :

1. Cliquez sur **[!UICONTROL Companies]**.
1. Sélectionnez la société à utiliser, puis cliquez sur **[!UICONTROL Destinations]**.
1. Dans la section [!UICONTROL Batch Data], définissez les options suivantes :

   * **[!UICONTROL Sync Type]**: Sélectionnez  **[!UICONTROL Customer]** ou  **[!UICONTROL Platform]**.
   * **[!UICONTROL Sync Type Lookback Period]**: Cet intervalle de temps définit la plage de votre fichier de données. Les choix possibles sont **[!UICONTROL 24 hours]**, **[!UICONTROL 7 days]**, **[!UICONTROL 30 days]**.
   * **[!UICONTROL Incremental Sync Scheduled Run]**: Select **[!UICONTROL Never]**. N’oubliez pas que ce filtre s’applique uniquement aux fichiers de synchronisation complète.
   * **[!UICONTROL Full Sync Scheduled Run]**: Cela détermine la fréquence à laquelle vous souhaitez recevoir ce fichier. Les choix sont les suivants : **[!UICONTROL 24 hours]**, **[!UICONTROL 7 days]**, **[!UICONTROL 30 days]** ou **[!UICONTROL Never]** (à désactiver).

1. Cliquez sur **[!UICONTROL Save]**.
