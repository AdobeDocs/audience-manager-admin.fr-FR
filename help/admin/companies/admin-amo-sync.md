---
description: Par défaut, toutes les entreprises synchronisent les données avec Adobe Media Optimizer (AMO). Dans l’interface utilisateur d’administration, chaque conteneur d’entreprise comporte une source de données qui gère ce processus. Cette source de données est Adobe AMO (ID 411). Cliquez sur une ligne de conteneur (sous l’onglet Conteneurs) d’une société sélectionnée pour désactiver cette synchronisation par défaut ou pour ajouter et supprimer d’autres sources de données au processus de synchronisation AMO.
seo-description: By default, all companies sync data with Adobe Media Optimizer (AMO). In the Admin UI, each company container has a data source that manages this process. This data source is Adobe AMO (ID 411). Click a container row (under the Containers tab) for a selected company to disable this default sync or to add and remove other data sources to the AMO sync process.
seo-title: ID Syncing with Media Optimizer
title: Synchronisation des identifiants avec Adobe Media Optimizer
uuid: b741dfa7-2947-4288-b214-79eccf18d53a
exl-id: ebd978ef-3825-4a96-94bd-5cdae269cf7c
TQID: https://experienceleague.adobe.com/R6xtPWC964J1atGK-R0g6J5AG83PYJosHNE3-5LvMVE
product_v2:
  - id: df80eeb1-8d72-467e-b0df-9d51c7d3a0a1
source-git-commit: d2bed13a6ac7d38ae79b65d492b6de0ca6b6d488
workflow-type: tm+mt
source-wordcount: 222
ht-degree: 2%

---

# Synchronisation des identifiants avec Adobe Media Optimizer {#id-syncing-with-media-optimizer}

Par défaut, toutes les entreprises synchronisent les données avec [!DNL Adobe Media Optimizer] ([!DNL AMO]). Dans le [!UICONTROL Admin UI], chaque conteneur d’entreprise dispose d’une source de données qui gère ce processus. Cette source de données est [!UICONTROL Adobe AMO] ([!UICONTROL ID] 411). Cliquez sur une ligne de conteneur (sous l’onglet [!UICONTROL Containers] ) d’une société sélectionnée pour désactiver cette synchronisation par défaut ou pour ajouter et supprimer d’autres sources de données au processus de synchronisation [!DNL AMO].

![](assets/id-sync.png)

## Statut de synchronisation des identifiants {#id-sync-status}

Le tableau suivant décrit le statut de synchronisation d’une source de données.

| État | Description |
|------ | -------- |
| Off | Supprimez toutes les sources de données de [!UICONTROL Selected Data Sources] pour ce conteneur afin de désactiver les synchronisations des identifiants avec [!DNL AMO] |
| Activé (quelle que soit la version du service d’ID) | Une source de données se synchronise avec [!DNL AMO], quelle que soit la version du service d’ID lorsque : <ul><li>La source de données apparaît dans la liste [!UICONTROL Selected Data Sources].</li><li>La case à cocher [!DNL AMO] *n’est pas* sélectionnée.</li></ul> |
| Activé (quelle que soit la version du service d’ID) | Une source de données se synchronise avec [!DNL AMO] avec la version 2.0 (ou ultérieure) du service d’ID lorsque : <ul><li>La source de données apparaît dans la liste [!UICONTROL Selected Data Sources].</li><li>La case à cocher [!DNL AMO] *est* est sélectionnée.</li></ul> |

>[!MORELIKETHIS]
>
>* [Gestion des conteneurs](../companies/admin-manage-containers.md#task_61DB5CEECC5049DD8D059C642AC3F967)
