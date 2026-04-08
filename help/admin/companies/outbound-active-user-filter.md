---
description: Suivez ces instructions pour générer un fichier de synchronisation complet incluant uniquement les utilisateurs récemment actifs. Vous pouvez filtrer les utilisateurs actifs afin de transmettre les données pertinentes à un système de ciblage sur site ou de limiter la taille des fichiers envoyés à un DSP. Vous ne pouvez pas utiliser ce filtre avec la synchronisation incrémentielle.
seo-description: Follow these instructions to generate a full synchronization file that includes recently active users only. You may want to filter for active users to push relevant data to an on-site targeting system or to limit the size of the files sent to a DSP. You cannot use this filter with incremental synchronization.
seo-title: Filter Outbound Data by Active Users Only
title: Filtrer les données sortantes par les utilisateurs actifs uniquement
uuid: a2b4a385-eee3-458c-b978-09509cacb397
exl-id: d501cfd1-64dd-448e-92c5-180c0081d3e5
TQID: https://experienceleague.adobe.com/rr6ABB4pgrhkWG88VenqIcbyAaPQfbg258M6SVdE28k
product_v2:
  - id: df80eeb1-8d72-467e-b0df-9d51c7d3a0a1
feature_v2:
  - id: c814092e-2730-45e8-a12d-e084529f52cb
source-git-commit: d2bed13a6ac7d38ae79b65d492b6de0ca6b6d488
workflow-type: tm+mt
source-wordcount: 219
ht-degree: 0%

---

# Filtrer les données sortantes par les utilisateurs actifs uniquement {#filter-outbound-data-by-active-users-only}

Suivez ces instructions pour générer un fichier de synchronisation complet incluant uniquement les utilisateurs récemment actifs. Vous pouvez filtrer les utilisateurs actifs afin de transmettre les données pertinentes à un système de ciblage sur site ou de limiter la taille des fichiers envoyés à un DSP. Vous ne pouvez pas utiliser ce filtre avec la synchronisation incrémentielle.

>[!NOTE]
>
>Un visiteur n’a pas besoin d’être affiché sur un site client sélectionné ou dans son trafic publicitaire pour être qualifié d’« actif ». Ils peuvent être considérés comme « actifs » par n’importe quel client ou partenaire [!DNL Audience Manager].

Pour filtrer par utilisateurs actifs uniquement :

1. Cliquez sur **[!UICONTROL Companies]**.
1. Sélectionnez la société avec laquelle vous souhaitez travailler et cliquez sur **[!UICONTROL Destinations]**.
1. Dans la section [!UICONTROL Batch Data] , définissez les options suivantes :

   * **[!UICONTROL Sync Type]** : sélectionnez **[!UICONTROL Customer]** ou **[!UICONTROL Platform]**.
   * **[!UICONTROL Sync Type Lookback Period]** : cet intervalle de temps définit la plage de votre fichier de données. Les choix possibles sont les suivants : **[!UICONTROL 24 hours]**, **[!UICONTROL 7 days]**, **[!UICONTROL 30 days]**.
   * **[!UICONTROL Incremental Sync Scheduled Run]** : sélectionnez **[!UICONTROL Never]**. N’oubliez pas que ce filtre s’applique uniquement aux fichiers de synchronisation complète.
   * **[!UICONTROL Full Sync Scheduled Run]** : détermine la fréquence à laquelle vous souhaitez recevoir ce fichier. Les choix possibles sont **[!UICONTROL 24 hours]**, **[!UICONTROL 7 days]**, **[!UICONTROL 30 days]** ou **[!UICONTROL Never]** (pour désactiver).

1. Cliquez sur **[!UICONTROL Save]**.
