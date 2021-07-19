---
description: Suivez ces instructions pour générer un fichier de synchronisation complète qui inclut uniquement les utilisateurs principaux récemment. Vous pouvez filtrer pour que les utilisateurs principaux puissent transmettre les données pertinentes à un système de ciblage sur site ou limiter la taille des fichiers envoyés à un DSP. Vous ne pouvez pas utiliser ce filtre avec la synchronisation incrémentielle.
seo-description: Suivez ces instructions pour générer un fichier de synchronisation complète qui inclut uniquement les utilisateurs principaux récemment. Vous pouvez filtrer pour que les utilisateurs principaux puissent transmettre les données pertinentes à un système de ciblage sur site ou limiter la taille des fichiers envoyés à un DSP. Vous ne pouvez pas utiliser ce filtre avec la synchronisation incrémentielle.
seo-title: Filtrage des données sortantes par utilisateurs actifs uniquement
title: Filtrage des données sortantes par utilisateurs actifs uniquement
uuid: a2b4a385-eee3-458c-b978-09509cacb397
exl-id: d501cfd1-64dd-448e-92c5-180c0081d3e5
source-git-commit: f5d74995f0664cf63e68b46f1f3c608f34df0e80
workflow-type: tm+mt
source-wordcount: '276'
ht-degree: 8%

---

# Filtrage des données sortantes par utilisateurs actifs uniquement {#filter-outbound-data-by-active-users-only}

Suivez ces instructions pour générer un fichier de synchronisation complète qui inclut uniquement les utilisateurs principaux récemment. Vous pouvez filtrer pour que les utilisateurs principaux puissent transmettre les données pertinentes à un système de ciblage sur site ou limiter la taille des fichiers envoyés à un DSP. Vous ne pouvez pas utiliser ce filtre avec la synchronisation incrémentielle.

>[!NOTE]
>
>Un visiteur n’a pas besoin d’être vu sur un site client sélectionné ou dans son trafic publicitaire pour être considéré comme &quot;principal&quot;. Ils peuvent être vus par n’importe quel client ou partenaire [!DNL Audience Manager] pour être &quot;principal&quot;.

Pour filtrer par utilisateurs principaux uniquement :

1. Cliquez sur **[!UICONTROL Companies]**.
1. Sélectionnez la société avec laquelle vous souhaitez travailler et cliquez sur **[!UICONTROL Destinations]**.
1. Dans la section [!UICONTROL Batch Data] , définissez les options suivantes :

   * **[!UICONTROL Sync Type]**: Sélectionnez  **[!UICONTROL Customer]** ou  **[!UICONTROL Platform]**.
   * **[!UICONTROL Sync Type Lookback Period]**: Cet intervalle définit la plage de votre fichier de données. **[!UICONTROL 24 hours]**, **[!UICONTROL 7 days]**, **[!UICONTROL 30 days]**.
   * **[!UICONTROL Incremental Sync Scheduled Run]**: Select **[!UICONTROL Never]**. Pour rappel, ce filtre s’applique uniquement aux fichiers de synchronisation complète.
   * **[!UICONTROL Full Sync Scheduled Run]**: Cela détermine la fréquence à laquelle vous souhaitez recevoir ce fichier. **[!UICONTROL 24 hours]**, **[!UICONTROL 7 days]**, **[!UICONTROL 30 days]** ou **[!UICONTROL Never]** (à désactiver).

1. Cliquez sur **[!UICONTROL Save]**.
