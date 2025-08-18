---
description: Afin d’éviter l’intégration accidentelle de fichiers et de données dans des sources de données cibles détenues par d’autres partenaires ou clients, Audience Manager a ajouté une exigence de mappage entre l’ID de partenaire (PID) et les sources de données détenues par d’autres partenaires.
title: Gérer l’accès à l’intégration pour les données tierces
exl-id: 03bec978-dd31-41cc-a3aa-d67fbb98963c
source-git-commit: cc04863272005964cfbf1bb2319cc0dd86863680
workflow-type: tm+mt
source-wordcount: '274'
ht-degree: 0%

---

# Gestion de l’accès à l’intégration pour les données tierces {#manage-onboarding-access-for-second-party-data}

>[!IMPORTANT]
>
> L’audience de cette page est constituée des employés internes à Adobe. Si vous êtes un client d’Audience Manager et que vous demandez un mappage de source de données tierce comme décrit sur cette page, contactez l’assistance clientèle ou votre gestionnaire de compte technique.
> &#x200B;> Notez qu’il n’est pas nécessaire de demander un mappage pour les relations de partage de données existantes. Le mappage n’est pas non plus requis lors de l’intégration de données dans des sources de données cibles qui appartiennent à votre PID.

Afin d’éviter l’intégration accidentelle de fichiers et de données dans des sources de données cibles détenues par d’autres partenaires, Audience Manager a ajouté une exigence de mappage entre l’ID de partenaire (PID) et les sources de données (DPID) détenues par d’autres partenaires. Pour en savoir plus sur les PID et DPID, consultez l’[index des Audience Manager IDs](https://experienceleague.adobe.com/docs/audience-manager/user-guide/reference/ids-in-aam.html?lang=fr).

À des fins de partage de données tierces, si un partenaire Audience Manager ou un client souhaite ingérer des fichiers dans une source de données cible qui ne lui appartient pas, il doit demander un mappage entre son identifiant de partenaire (PID) et cette source de données spécifique (DPID). Si le mappage est manquant, les fichiers ne seront pas traités par la tâche de données entrante et les données ne seront pas intégrées à Audience Manager.

Pour créer ce mappage, envoyez un ticket Jira à l’équipe d’ingénieurs d’Audience Manager. Voir un exemple de ticket Jira [ici](https://jira.corp.adobe.com/browse/AAM-60353). Vous n’avez pas besoin de demander la création de mappages pour les relations de partage de données existantes.
