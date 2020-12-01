---
description: Par défaut, toutes les sociétés synchronisent les données avec Adobe Media Optimizer (AMO). Dans l’interface utilisateur d’administration, chaque conteneur de société dispose d’une source de données qui gère ce processus. Cette source de données est l’AMO Adobe (ID 411). Cliquez sur une ligne de conteneur (sous l’onglet Conteneurs) pour une société sélectionnée pour désactiver cette synchronisation par défaut ou pour ajouter et supprimer d’autres sources de données au processus de synchronisation AMO.
seo-description: Par défaut, toutes les sociétés synchronisent les données avec Adobe Media Optimizer (AMO). Dans l’interface utilisateur d’administration, chaque conteneur de société dispose d’une source de données qui gère ce processus. Cette source de données est l’AMO Adobe (ID 411). Cliquez sur une ligne de conteneur (sous l’onglet Conteneurs) pour une société sélectionnée pour désactiver cette synchronisation par défaut ou pour ajouter et supprimer d’autres sources de données au processus de synchronisation AMO.
seo-title: Synchronisation des identifiants avec Media Optimizer
title: Synchronisation des identifiants avec Media Optimizer
uuid: b741dfa7-2947-4288-b214-79eccf18d53a
translation-type: tm+mt
source-git-commit: 2998dc049971b2fac8c45ca6e3118ea607ae3f92
workflow-type: tm+mt
source-wordcount: '287'
ht-degree: 6%

---


# Synchronisation des identifiants avec Media Optimizer {#id-syncing-with-media-optimizer}

Par défaut, toutes les sociétés synchronisent les données avec [!DNL Adobe Media Optimizer] ([!DNL AMO]). Dans [!UICONTROL Admin UI], chaque conteneur de société dispose d’une source de données qui gère ce processus. Cette source de données est [!UICONTROL Adobe AMO] ([!UICONTROL ID] 411). Cliquez sur une ligne de conteneur (sous l&#39;onglet [!UICONTROL Containers]) pour une société sélectionnée pour désactiver cette synchronisation par défaut ou pour ajouter et supprimer d&#39;autres sources de données au processus de synchronisation [!DNL AMO].

![](assets/id-sync.png)

## État de la synchronisation des identifiants {#id-sync-status}

Le tableau suivant décrit l’état de synchronisation d’une source de données.

| État | Description |
|------ | -------- |
| Off | Supprimez toutes les sources de données de [!UICONTROL Selected Data Sources] pour ce conteneur afin de désactiver les synchronisations d’ID avec [!DNL AMO]. |
| Activé (quelle que soit la version du service d’ID) | Une source de données se synchronise avec [!DNL AMO] quelle que soit la version du service d’ID lorsque : <ul><li>La source de données apparaît dans la liste [!UICONTROL Selected Data Sources].</li><li>La case à cocher [!DNL AMO] *n&#39;est pas* sélectionnée.</li></ul> |
| Activé (quelle que soit la version du service d’ID) | Une source de données est synchronisée avec [!DNL AMO] avec le service d’ID version 2.0 (ou supérieure) lorsque : <ul><li>La source de données apparaît dans la liste [!UICONTROL Selected Data Sources].</li><li>La case à cocher [!DNL AMO] *est* sélectionnée.</li></ul> |

>[!MORELIKETHIS]
>
>* [Gestion des conteneurs](../companies/admin-manage-containers.md#task_61DB5CEECC5049DD8D059C642AC3F967)

