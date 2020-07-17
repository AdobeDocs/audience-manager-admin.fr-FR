---
description: Les options de graphique de périphérique sont disponibles pour les sociétés qui participent à Adobe Experience Cloud Device Co-op. Si un client entretient également une relation contractuelle avec un fournisseur tiers de graphiques de périphériques, qui est intégré à l'Audience Manager, cette section affiche les options pour ce graphique de périphériques. Ces options se trouvent sous Sociétés > nom de la société > Profil > Options graphiques du périphérique.
seo-description: Les options de graphique de périphérique sont disponibles pour les sociétés qui participent à Adobe Experience Cloud Device Co-op. Si un client entretient également une relation contractuelle avec un fournisseur tiers de graphiques de périphériques, qui est intégré à l'Audience Manager, cette section affiche les options pour ce graphique de périphériques. Ces options se trouvent sous Sociétés > nom de la société > Profil > Options graphiques du périphérique.
seo-title: Options de Device Graph pour les entreprises
title: Options de Device Graph pour les entreprises
uuid: a8ced843-710c-4a8f-a0d7-ea89d010a7a5
translation-type: tm+mt
source-git-commit: 2998dc049971b2fac8c45ca6e3118ea607ae3f92
workflow-type: tm+mt
source-wordcount: '538'
ht-degree: 4%

---


# Options de Device Graph pour les entreprises {#device-graph-options-for-companies}

Elles [!UICONTROL Device Graph Options] sont à la disposition des sociétés qui participent au [!DNL Adobe Experience Cloud Device Co-op]programme. Si un client entretient également une relation contractuelle avec un fournisseur tiers de graphiques de périphériques, qui est intégré à l&#39;Audience Manager, cette section affiche les options pour ce graphique de périphériques. Ces options se trouvent sous [!UICONTROL Companies] > nom de la société > [!UICONTROL Profile] > [!UICONTROL Device Graph Options].

![](assets/adminUIdataSource.png)

Cette illustration utilise des noms génériques pour les options de graphique de périphériques tiers. En production, ces noms proviennent du fournisseur de graphiques de périphériques et peuvent varier de ce qui est présenté ici. Par exemple, les [!DNL LiveRamp] options habituellement (mais pas toujours) :

* Commencez avec les sections &quot;[!DNL LiveRamp]&quot;
* Contient un deuxième nom qui varie
* Terminer par &quot;[!UICONTROL - Household]&quot; ou &quot;[!UICONTROL -Person]&quot;

## Options graphiques du périphérique définies {#device-graph-options-defined}

Les options de graphique de périphérique que vous sélectionnez ici exposent ou masquent les [!UICONTROL Device Options] choix disponibles pour un [!DNL Audience Manager] client lorsqu’il crée un [!UICONTROL Profile Merge Rule]client.

### Graphique des périphériques coopératifs {#co-op-graph}

Les clients qui participent à [Adobe Experience Cloud Device Co-op](https://marketing.adobe.com/resources/help/en_US/mcdc/) utilisent ces options pour créer un [!UICONTROL Profile Merge Rule] avec des données [](https://marketing.adobe.com/resources/help/en_US/mcdc/mcdc-links.html)déterministes et probabilistes. L’ [!DNL Corporate Provisioning Team] utilisateur active et désactive cette option par le biais d’un appel [!DNL API] principal. Vous ne pouvez pas cocher ou décocher ces cases dans la [!DNL Admin UI]. En outre, les options **[!UICONTROL Co-op Device Graph]** et **[!UICONTROL Company Device Graph]** sont mutuellement exclusives. Les clients peuvent nous demander d&#39;activer l&#39;un ou l&#39;autre, mais pas les deux. Lorsqu’elle est cochée, cette option expose le **[!UICONTROL Co-op Device Graph]** contrôle dans les [!UICONTROL Device Options] paramètres d’un [!UICONTROL Profile Merge Rule].

![](assets/adminUI1.png)

### Graphique du périphérique de Société {#company-graph}

Cette option est destinée aux [!DNL Analytics] clients qui utilisent la [!UICONTROL People] mesure dans leur suite de [!DNL Analytics] rapports. L’ [!DNL Corporate Provisioning Team] utilisateur active et désactive cette option par le biais d’un appel [!DNL API] principal. Vous ne pouvez pas cocher ou décocher ces cases dans la [!DNL Admin UI]. En outre, les options **[!UICONTROL Company Device Graph]** et **[!UICONTROL Co-op Device Graph]** sont mutuellement exclusives. Les clients peuvent nous demander d&#39;activer l&#39;un ou l&#39;autre, mais pas les deux. Si cochée :

* Ce graphique de périphérique utilise des données déterministes qui appartiennent à la société que vous configurez (aucune donnée probabiliste).
* [!DNL Audience Manager] crée automatiquement un [!UICONTROL Data Source] nom `*`de`*-Company Device Graph-Person`partenaire. Dans la page [!UICONTROL Data Source] Détails, [!DNL Audience Manager] les clients peuvent modifier le nom et la description du partenaire et appliquer des contrôles [d’exportation de](https://marketing.adobe.com/resources/help/en_US/aam/c_dec.html) données à cette source de données.
* [!DNL Audience Manager] les clients ne *voient pas* de nouveau paramètre dans la [!UICONTROL Device Options] section pour un [!UICONTROL Profile Merge Rule]segment.

### Graphique des périphériques LiveRamp (personne ou foyer) {#liveramp-device-graph}

Ces cases à cocher sont activées dans le [!DNL Admin UI] cas où un partenaire crée un [!UICONTROL Data Source] et sélectionne **[!UICONTROL Use as an Authenticated Profile]** et/ou **[!UICONTROL Use as a Device Graph]**. Les noms de ces paramètres sont déterminés par le fournisseur de graphiques de périphériques tiers (par exemple, [!DNL LiveRamp], [!DNL TapAd], etc.). Lorsqu&#39;elle est cochée, cela signifie que la société que vous configurez va utiliser les données fournies par ces graphiques de périphériques.

![](assets/adminUI2.png)

>[!MORELIKETHIS]
>
>* [Définition des options des stratégies de fusion de profils](https://marketing.adobe.com/resources/help/en_US/aam/merge-rule-definitions.html)
>* [Paramètres de source de données et options de menu](https://marketing.adobe.com/resources/help/en_US/aam/datasource-settings-definitions.html)

