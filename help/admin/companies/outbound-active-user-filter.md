---
description: Suivez ces instructions pour générer un fichier de synchronisation complet incluant uniquement les utilisateurs récemment actifs. Vous pouvez filtrer les utilisateurs actifs afin de transmettre les données pertinentes à un système de ciblage sur site ou de limiter la taille des fichiers envoyés à un DSP. Vous ne pouvez pas utiliser ce filtre avec une synchronisation incrémentielle.
seo-description: Suivez ces instructions pour générer un fichier de synchronisation complet incluant uniquement les utilisateurs récemment actifs. Vous pouvez filtrer les utilisateurs actifs afin de transmettre les données pertinentes à un système de ciblage sur site ou de limiter la taille des fichiers envoyés à un DSP. Vous ne pouvez pas utiliser ce filtre avec une synchronisation incrémentielle.
seo-title: Filtrage des données sortantes par les utilisateurs actifs uniquement
title: Filtrage des données sortantes par les utilisateurs actifs uniquement
uuid: a 2 b 4 a 385-eee 3-458 c-b 978-09509 cacb 397
translation-type: tm+mt
source-git-commit: be661580da839ce6332a0ad827dec08e854abe54

---


# Filtrage des données sortantes par les utilisateurs actifs uniquement {#filter-outbound-data-by-active-users-only}

Suivez ces instructions pour générer un fichier de synchronisation complet incluant uniquement les utilisateurs récemment actifs. Vous pouvez filtrer les utilisateurs actifs afin de transmettre les données pertinentes à un système de ciblage sur site ou de limiter la taille des fichiers envoyés à un DSP. Vous ne pouvez pas utiliser ce filtre avec une synchronisation incrémentielle.

>[!NOTE]
>
>Il n'est pas nécessaire qu'un visiteur soit visible sur un site client sélectionné ou dans son trafic publicitaire pour être qualifié comme « actif ».  » » Ils peuvent être vus par tout [!DNL Audience Manager] client ou partenaire comme étant « actif ».  » »

Pour filtrer uniquement les utilisateurs actifs :

1. Cliquez sur **[!UICONTROL Companies]**.
1. Sélectionnez la société avec laquelle vous souhaitez travailler et cliquez **[!UICONTROL Destinations]** sur.
1. Dans la [!UICONTROL Batch Data] section, définissez les options suivantes :

   * **[!UICONTROL Sync Type]**: Sélectionnez **[!UICONTROL Customer]** ou **[!UICONTROL Platform]**.
   * **[!UICONTROL Sync Type Lookback Period]**: Cet intervalle définit la plage de votre fichier de données. Les choix incluent **[!UICONTROL 24 hours]****[!UICONTROL 7 days]****[!UICONTROL 30 days]**.
   * **[!UICONTROL Incremental Sync Scheduled Run]**: Sélectionnez **[!UICONTROL Never]**. Souvenez-vous que ce filtre s'applique uniquement aux fichiers de synchronisation complets.
   * **[!UICONTROL Full Sync Scheduled Run]**: Détermine la fréquence de réception de ce fichier. Les choix incluent **[!UICONTROL 24 hours]****[!UICONTROL 7 days]**, **[!UICONTROL 30 days]** ou **[!UICONTROL Never]** (désactiver).

1. Cliquez sur **[!UICONTROL Save]**.
