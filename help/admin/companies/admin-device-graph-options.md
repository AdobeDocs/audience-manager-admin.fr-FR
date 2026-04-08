---
description: Les options du graphique des appareils sont disponibles pour les sociétés qui participent à Adobe Experience Cloud Device Co-op. Si un client a également une relation contractuelle avec un fournisseur tiers de graphique d’appareil intégré à Audience Manager, cette section affiche les options de ce graphique d’appareil. Ces options se trouvent dans Entreprises > nom de la société > Profil > Options du graphique d’appareil.
seo-description: The Device Graph Options are available to companies that participate in the Adobe Experience Cloud Device Co-op. If a customer also has a contractual relationship with a third-party device graph provider that is integrated with Audience Manager, this section will show options for that device graph. These options are located in Companies > company name > Profile > Device Graph Options.
seo-title: Device Graph Options for Companies
title: Options de graphique d’appareil pour les entreprises
uuid: a8ced843-710c-4a8f-a0d7-ea89d010a7a5
exl-id: 2502f3d2-b43c-410c-acb6-03c2a2ba2c1d
TQID: https://experienceleague.adobe.com/82qZw1UwK-qaJD2WWXENH2EUtiZur4L2YMhrZO09cCg
product_v2:
  - id: df80eeb1-8d72-467e-b0df-9d51c7d3a0a1
source-git-commit: d2bed13a6ac7d38ae79b65d492b6de0ca6b6d488
workflow-type: tm+mt
source-wordcount: 511
ht-degree: 0%

---

# Options de graphique d’appareil pour les entreprises {#device-graph-options-for-companies}

Les [!UICONTROL Device Graph Options] sont disponibles pour les entreprises qui participent au [!DNL Adobe Experience Cloud Device Co-op]. Si un client a également une relation contractuelle avec un fournisseur tiers de graphique d’appareil intégré à Audience Manager, cette section affiche les options de ce graphique d’appareil. Ces options se trouvent dans [!UICONTROL Companies] > nom de la société > [!UICONTROL Profile] > [!UICONTROL Device Graph Options].

![](assets/adminUIdataSource.png)

Cette illustration utilise des noms génériques pour les options graphiques des appareils tiers. En production, ces noms proviennent du fournisseur de graphiques d’appareils et peuvent différer de ce qui est affiché ici. Par exemple, les options [!DNL LiveRamp] sont généralement (mais pas toujours) les suivantes :

* Commencer par « [!DNL LiveRamp] »
* Contiennent un deuxième prénom qui varie
* Se termine par « [!UICONTROL - Household] » ou « [!UICONTROL -Person] »

## Options de graphique d’appareil définies {#device-graph-options-defined}

Les options de graphique d’appareil que vous sélectionnez ici exposent ou masquent les choix [!UICONTROL Device Options] disponibles pour un client [!DNL Audience Manager] lorsqu’il crée un [!UICONTROL Profile Merge Rule].

### Graphique d’appareil Co-op {#co-op-graph}

Les clients qui participent à la [Adobe Experience Cloud Device Co-op](https://experienceleague.adobe.com/docs/device-co-op/using/about/overview.html?lang=en) utilisent ces options pour créer un [!UICONTROL Profile Merge Rule] avec des [données déterministes et probabilistes](https://experienceleague.adobe.com/docs/device-co-op/using/device-graph/links.html?lang=en). Le [!DNL Corporate Provisioning Team] active et désactive cette option via un appel de [!DNL API] back-end. Vous ne pouvez pas cocher ni décocher ces cases dans le [!DNL Admin UI]. En outre, les options **[!UICONTROL Co-op Device Graph]** et **[!UICONTROL Company Device Graph]** s’excluent mutuellement. Les clients peuvent nous demander d&#39;activer l&#39;un ou l&#39;autre, mais pas les deux. Lorsque cette case est cochée, le contrôle **[!UICONTROL Co-op Device Graph]** est exposé dans les paramètres [!UICONTROL Device Options] d’un [!UICONTROL Profile Merge Rule].

![](assets/adminUI1.png)

### Graphique d’appareil d’entreprise {#company-graph}

Cette option est destinée aux clients [!DNL Analytics] qui utilisent la mesure [!UICONTROL People] dans leur suite de rapports [!DNL Analytics]. Le [!DNL Corporate Provisioning Team] active et désactive cette option via un appel de [!DNL API] back-end. Vous ne pouvez pas cocher ni décocher ces cases dans le [!DNL Admin UI]. En outre, les options **[!UICONTROL Company Device Graph]** et **[!UICONTROL Co-op Device Graph]** s’excluent mutuellement. Les clients peuvent nous demander d&#39;activer l&#39;un ou l&#39;autre, mais pas les deux. Lorsque cette case est cochée :

* Ce graphique d’appareil utilise des données déterministes qui appartiennent à la société que vous configurez (pas de données probabilistes).
* [!DNL Audience Manager] crée automatiquement un [!UICONTROL Data Source] appelé `*`nom du partenaire`*-Company Device Graph-Person`. Dans la page des détails de la [!UICONTROL Data Source], [!DNL Audience Manager] clients peuvent modifier le nom, la description et l’application du [Contrôles d’exportation de données](https://experienceleague.adobe.com/docs/device-co-op/using/device-graph/links.html?lang=en) à cette source de données.
* [!DNL Audience Manager] clients *pas* un nouveau paramètre pour une [!UICONTROL Profile Merge Rule] s’affiche dans la section [!UICONTROL Device Options] .

### Graphique d’appareil LiveRamp (personne ou ménage) {#liveramp-device-graph}

Ces cases à cocher sont activées dans le [!DNL Admin UI] lorsqu’un partenaire crée une [!UICONTROL Data Source] et sélectionne des **[!UICONTROL Use as an Authenticated Profile]** et/ou des **[!UICONTROL Use as a Device Graph]**. Les noms de ces paramètres sont déterminés par le fournisseur tiers de graphiques d’appareils (par exemple, [!DNL LiveRamp], [!DNL TapAd], etc.). Lorsque cette case est cochée, cela signifie que la société que vous configurez va utiliser les données fournies par ces graphiques d’appareils.

![](assets/adminUI2.png)

>[!MORELIKETHIS]
>
>* [Définition des options des stratégies de fusion de profils](https://experienceleague.adobe.com/docs/audience-manager/user-guide/features/profile-merge-rules/merge-rule-definitions.html?lang=en)
>* [Paramètres de Source de données et options de menu](https://experienceleague.adobe.com/docs/audience-manager/user-guide/features/data-sources/datasources-list-and-settings.html?lang=en)
