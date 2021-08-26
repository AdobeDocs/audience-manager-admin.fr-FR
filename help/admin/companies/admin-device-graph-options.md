---
description: Les options Device Graph sont disponibles pour les entreprises qui participent à Adobe Experience Cloud Device Co-op. Si un client entretient également une relation contractuelle avec un fournisseur de représentation graphique des appareils tiers intégré à Audience Manager, cette section affiche les options de cette représentation graphique des appareils. Ces options sont situées dans Entreprises > nom de la société > Profil > Options de représentation graphique des appareils.
seo-description: The Device Graph Options are available to companies that participate in the Adobe Experience Cloud Device Co-op. If a customer also has a contractual relationship with a third-party device graph provider that is integrated with Audience Manager, this section will show options for that device graph. These options are located in Companies > company name > Profile > Device Graph Options.
seo-title: Device Graph Options for Companies
title: Options de Device Graph pour les entreprises
uuid: a8ced843-710c-4a8f-a0d7-ea89d010a7a5
exl-id: 2502f3d2-b43c-410c-acb6-03c2a2ba2c1d
source-git-commit: 1f4dbf8f7b36e64c3015b98ef90b6726d0e7495a
workflow-type: tm+mt
source-wordcount: '482'
ht-degree: 3%

---

# Options de Device Graph pour les entreprises {#device-graph-options-for-companies}

Les [!UICONTROL Device Graph Options] sont disponibles pour les entreprises qui participent à la [!DNL Adobe Experience Cloud Device Co-op]. Si un client entretient également une relation contractuelle avec un fournisseur de représentation graphique des appareils tiers intégré à Audience Manager, cette section affiche les options de cette représentation graphique des appareils. Ces options sont situées dans [!UICONTROL Companies] > nom de la société > [!UICONTROL Profile] > [!UICONTROL Device Graph Options].

![](assets/adminUIdataSource.png)

Cette illustration utilise des noms génériques pour les options de représentation graphique des appareils tiers. En production, ces noms proviennent du fournisseur de représentations graphiques des appareils et peuvent varier de ce qui est présenté ici. Par exemple, les options [!DNL LiveRamp] sont généralement (mais pas toujours) :

* Commencez avec les sections &quot;[!DNL LiveRamp]&quot;
* Contient un deuxième prénom qui varie
* Terminer par &quot;[!UICONTROL - Household]&quot; ou &quot;[!UICONTROL -Person]&quot;

## Options de Device Graph définies {#device-graph-options-defined}

Les options de Device Graph que vous sélectionnez ici exposent ou masquent les choix [!UICONTROL Device Options] disponibles pour un client [!DNL Audience Manager] lorsqu’il crée une balise [!UICONTROL Profile Merge Rule].

### Graphique d’appareil Co-op {#co-op-graph}

Les clients qui participent à [Adobe Experience Cloud Device Co-op](https://experienceleague.adobe.com/docs/device-co-op/using/about/overview.html?lang=en) utilisent ces options pour créer une [!UICONTROL Profile Merge Rule] avec des [données déterministes et probabilistes](https://experienceleague.adobe.com/docs/device-co-op/using/device-graph/links.html?lang=en). [!DNL Corporate Provisioning Team] active et désactive cette option via un appel [!DNL API] principal. Vous ne pouvez pas cocher ou décocher ces cases dans la balise [!DNL Admin UI]. En outre, les options **[!UICONTROL Co-op Device Graph]** et **[!UICONTROL Company Device Graph]** s’excluent mutuellement. Les clients peuvent nous demander d’activer l’un ou l’autre, mais pas les deux. Si cette case est cochée, le contrôle **[!UICONTROL Co-op Device Graph]** est exposé dans les paramètres [!UICONTROL Device Options] pour un [!UICONTROL Profile Merge Rule].

![](assets/adminUI1.png)

### Graphique du périphérique de l’entreprise {#company-graph}

Cette option est destinée aux clients [!DNL Analytics] qui utilisent la mesure [!UICONTROL People] dans leur suite de rapports [!DNL Analytics]. [!DNL Corporate Provisioning Team] active et désactive cette option via un appel [!DNL API] principal. Vous ne pouvez pas cocher ou décocher ces cases dans la balise [!DNL Admin UI]. En outre, les options **[!UICONTROL Company Device Graph]** et **[!UICONTROL Co-op Device Graph]** s’excluent mutuellement. Les clients peuvent nous demander d’activer l’un ou l’autre, mais pas les deux. Lorsque cette case est cochée :

* Ce graphique d’appareil utilise des données déterministes appartenant à la société que vous configurez (aucune donnée probabiliste).
* [!DNL Audience Manager] crée automatiquement un nom  [!UICONTROL Data Source] de  `*`partenaire`*-Company Device Graph-Person`. Sur la page [!UICONTROL Data Source] détails, les clients [!DNL Audience Manager] peuvent modifier le nom et la description du partenaire et appliquer les [contrôles des exportations de données](https://experienceleague.adobe.com/docs/device-co-op/using/device-graph/links.html?lang=en) à cette source de données.
* [!DNL Audience Manager] Les clients  *ne voient* pas de nouveau paramètre dans la  [!UICONTROL Device Options] section pour un  [!UICONTROL Profile Merge Rule].

### Graphique d’appareil LiveRamp (personne ou foyer) {#liveramp-device-graph}

Ces cases à cocher sont activées dans la balise [!DNL Admin UI] lorsqu’un partenaire crée une balise [!UICONTROL Data Source] et sélectionne **[!UICONTROL Use as an Authenticated Profile]** et/ou **[!UICONTROL Use as a Device Graph]**. Les noms de ces paramètres sont déterminés par le fournisseur de graphique d’appareil tiers (par exemple, [!DNL LiveRamp], [!DNL TapAd], etc.). Lorsque cette case est cochée, cela signifie que l’entreprise que vous configurez va utiliser les données fournies par ces représentations graphiques des appareils.

![](assets/adminUI2.png)

>[!MORELIKETHIS]
>
>* [Définition des options des stratégies de fusion de profils](https://experienceleague.adobe.com/docs/audience-manager/user-guide/features/profile-merge-rules/merge-rule-definitions.html?lang=en)
>* [Paramètres de source de données et options de menu](https://experienceleague.adobe.com/docs/audience-manager/user-guide/features/data-sources/datasources-list-and-settings.html?lang=en)

