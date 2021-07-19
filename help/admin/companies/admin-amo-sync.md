---
description: Par défaut, toutes les entreprises synchronisent les données avec Adobe Media Optimizer (AMO). Dans l’interface utilisateur d’administration, chaque conteneur d’entreprise dispose d’une source de données qui gère ce processus. Cette source de données est l’Adobe AMO (ID 411). Cliquez sur une ligne de conteneur (sous l’onglet Conteneurs ) pour une entreprise sélectionnée afin de désactiver cette synchronisation par défaut ou d’ajouter et de supprimer d’autres sources de données au processus de synchronisation AMO.
seo-description: Par défaut, toutes les entreprises synchronisent les données avec Adobe Media Optimizer (AMO). Dans l’interface utilisateur d’administration, chaque conteneur d’entreprise dispose d’une source de données qui gère ce processus. Cette source de données est l’Adobe AMO (ID 411). Cliquez sur une ligne de conteneur (sous l’onglet Conteneurs ) pour une entreprise sélectionnée afin de désactiver cette synchronisation par défaut ou d’ajouter et de supprimer d’autres sources de données au processus de synchronisation AMO.
seo-title: Synchronisation des identifiants avec Media Optimizer
title: Synchronisation des identifiants avec Media Optimizer
uuid: b741dfa7-2947-4288-b214-79eccf18d53a
exl-id: ebd978ef-3825-4a96-94bd-5cdae269cf7c
source-git-commit: f5d74995f0664cf63e68b46f1f3c608f34df0e80
workflow-type: tm+mt
source-wordcount: '287'
ht-degree: 6%

---

# Synchronisation des identifiants avec Media Optimizer {#id-syncing-with-media-optimizer}

Par défaut, toutes les entreprises synchronisent les données avec [!DNL Adobe Media Optimizer] ([!DNL AMO]). Dans la balise [!UICONTROL Admin UI], chaque conteneur d’entreprise dispose d’une source de données qui gère ce processus. Cette source de données est [!UICONTROL Adobe AMO] ([!UICONTROL ID] 411). Cliquez sur une ligne de conteneur (sous l’onglet [!UICONTROL Containers]) pour qu’une entreprise sélectionnée désactive cette synchronisation par défaut ou ajoute et supprime d’autres sources de données au processus de synchronisation [!DNL AMO].

![](assets/id-sync.png)

## État de synchronisation des identifiants {#id-sync-status}

Le tableau suivant décrit l’état de synchronisation d’une source de données.

| État | Description |
|------ | -------- |
| Off | Supprimez toutes les sources de données de [!UICONTROL Selected Data Sources] pour ce conteneur afin de désactiver les synchronisations des identifiants avec [!DNL AMO]. |
| Activé (quelle que soit la version du service d’ID) | Une source de données se synchronise avec [!DNL AMO], quelle que soit la version du service d’ID lorsque : <ul><li>La source de données apparaît dans la liste [!UICONTROL Selected Data Sources].</li><li>La case [!DNL AMO] *n’est pas* sélectionnée.</li></ul> |
| Activé (quelle que soit la version du service d’ID) | Une source de données se synchronise avec [!DNL AMO] avec le service d’ID version 2.0 (ou ultérieure) lorsque : <ul><li>La source de données apparaît dans la liste [!UICONTROL Selected Data Sources].</li><li>La case [!DNL AMO] *est* sélectionnée.</li></ul> |

>[!MORELIKETHIS]
>
>* [Gestion des conteneurs](../companies/admin-manage-containers.md#task_61DB5CEECC5049DD8D059C642AC3F967)

