---
description: Les options de graphique de périphérique sont disponibles pour les entreprises qui participent à Adobe Experience Cloud Device Co-op. Si un client entretient également une relation contractuelle avec un fournisseur tiers de graphiques de périphériques intégré à Audience Manager, cette section affiche les options pour ce graphique de périphériques. Ces options se trouvent sous Entreprises > nom de l’entreprise > Profil > Options graphiques du périphérique.
seo-description: Les options de graphique de périphérique sont disponibles pour les entreprises qui participent à Adobe Experience Cloud Device Co-op. Si un client entretient également une relation contractuelle avec un fournisseur tiers de graphiques de périphériques intégré à Audience Manager, cette section affiche les options pour ce graphique de périphériques. Ces options se trouvent sous Entreprises > nom de l’entreprise > Profil > Options graphiques du périphérique.
seo-title: Options graphiques des périphériques pour les entreprises
title: Options graphiques des périphériques pour les entreprises
uuid: a8ced843-710c-4a8f-a0d7-ea89d010a7a5
translation-type: tm+mt
source-git-commit: 2998dc049971b2fac8c45ca6e3118ea607ae3f92

---


# Options graphiques des périphériques pour les entreprises {#device-graph-options-for-companies}

Elles [!UICONTROL Device Graph Options] sont accessibles aux entreprises qui participent au [!DNL Adobe Experience Cloud Device Co-op]. Si un client entretient également une relation contractuelle avec un fournisseur tiers de graphiques de périphériques intégré à Audience Manager, cette section affiche les options pour ce graphique de périphériques. Ces options se trouvent sous [!UICONTROL Companies] &gt; nom de l’entreprise &gt; [!UICONTROL Profile] &gt; [!UICONTROL Device Graph Options].

![](assets/adminUIdataSource.png)

Cette illustration utilise des noms génériques pour les options de graphique de périphériques tiers. En production, ces noms proviennent du fournisseur de graphiques de périphériques et peuvent varier de ce qui est illustré ici. Par exemple, les [!DNL LiveRamp] options sont généralement (mais pas toujours) :

* Commencez avec les sections "[!DNL LiveRamp]"
* Contient un nom du milieu qui varie
* Terminer par "[!UICONTROL - Household]" ou "[!UICONTROL -Person]"

## Options graphiques du périphérique définies {#device-graph-options-defined}

Les options de graphique de périphérique que vous sélectionnez ici exposent ou masquent les [!UICONTROL Device Options] choix disponibles pour un [!DNL Audience Manager] client lorsqu’il crée un [!UICONTROL Profile Merge Rule].

### Graphique du périphérique de co-op {#co-op-graph}

Les clients qui participent à [Adobe Experience Cloud Device Co-op](https://marketing.adobe.com/resources/help/en_US/mcdc/) utilisent ces options pour créer une [!UICONTROL Profile Merge Rule] instance avec des données [](https://marketing.adobe.com/resources/help/en_US/mcdc/mcdc-links.html)déterministes et probabilistes. L’ [!DNL Corporate Provisioning Team] utilisateur active et désactive cette option par le biais d’un [!DNL API] appel principal. Vous ne pouvez pas cocher ou décocher ces cases dans la [!DNL Admin UI]. En outre, les options **[!UICONTROL Co-op Device Graph]** et **[!UICONTROL Company Device Graph]** sont mutuellement exclusives. Les clients peuvent nous demander d'activer l'un ou l'autre, mais pas les deux. Lorsqu’elle est cochée, cette option expose le **[!UICONTROL Co-op Device Graph]** contrôle dans les [!UICONTROL Device Options] paramètres d’un [!UICONTROL Profile Merge Rule].

![](assets/adminUI1.png)

### Graphique des périphériques de l'entreprise {#company-graph}

Cette option est destinée aux [!DNL Analytics] clients qui utilisent la [!UICONTROL People] mesure dans leur [!DNL Analytics] suite de rapports. L’ [!DNL Corporate Provisioning Team] utilisateur active et désactive cette option par le biais d’un [!DNL API] appel principal. Vous ne pouvez pas cocher ou décocher ces cases dans la [!DNL Admin UI]. En outre, les options **[!UICONTROL Company Device Graph]** et **[!UICONTROL Co-op Device Graph]** sont mutuellement exclusives. Les clients peuvent nous demander d'activer l'un ou l'autre, mais pas les deux. Si cochée :

* Ce graphique de périphérique utilise des données déterministes appartenant à l’entreprise que vous configurez (aucune donnée probabiliste).
* [!DNL Audience Manager] crée automatiquement le nom [!UICONTROL Data Source] du `*``*-Company Device Graph-Person`partenaire. Dans la page [!UICONTROL Data Source] Détails, [!DNL Audience Manager] les clients peuvent modifier le nom, la description et appliquer des contrôles d’exportation de [données](https://marketing.adobe.com/resources/help/en_US/aam/c_dec.html) à cette source de données.
* [!DNL Audience Manager] les clients ne *voient pas* de nouveau paramètre dans la [!UICONTROL Device Options] section pour un [!UICONTROL Profile Merge Rule].

### Graphique des périphériques LiveRamp (personne ou foyer) {#liveramp-device-graph}

Ces cases à cocher sont activées dans le [!DNL Admin UI] cas où un partenaire crée un [!UICONTROL Data Source] et sélectionne **[!UICONTROL Use as an Authenticated Profile]** et/ou **[!UICONTROL Use as a Device Graph]**. Les noms de ces paramètres sont déterminés par le fournisseur de graphiques de périphériques tiers (par exemple, [!DNL LiveRamp], [!DNL TapAd], etc.). Lorsqu'elle est cochée, cela signifie que l'entreprise que vous configurez va utiliser les données fournies par ces graphiques de périphériques.

![](assets/adminUI2.png)

>[!MORELIKETHIS]
>
>* [Définition des options de règle de fusion de profil](https://marketing.adobe.com/resources/help/en_US/aam/merge-rule-definitions.html)
>* [Paramètres de source de données et options de menu](https://marketing.adobe.com/resources/help/en_US/aam/datasource-settings-definitions.html)

