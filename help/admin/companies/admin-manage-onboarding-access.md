---
description: Afin d’empêcher l’intégration accidentelle de fichiers et de données dans des sources de données cibles détenues par d’autres partenaires ou clients, Audience Manager a ajouté une exigence de mappage entre l’ID de partenaire (PID) et les sources de données détenues par d’autres partenaires.
title: Gestion de l’accès à l’intégration pour les données de deuxième niveau
exl-id: 03bec978-dd31-41cc-a3aa-d67fbb98963c
source-git-commit: cc04863272005964cfbf1bb2319cc0dd86863680
workflow-type: tm+mt
source-wordcount: '283'
ht-degree: 0%

---

# Gestion de l’accès à l’intégration pour les données de deuxième niveau {#manage-onboarding-access-for-second-party-data}

>[!IMPORTANT]
>
> Le public de cette page est les employés internes à l’Adobe. Si vous êtes un client d’Audience Manager qui demande un mappage de source de données tierce comme décrit sur cette page, contactez l’assistance clientèle ou votre gestionnaire de compte technique.
> Notez qu’il n’est pas nécessaire de demander un mappage pour les relations de partage de données existantes. Le mappage n’est pas non plus requis lors de l’intégration de données dans des sources de données cibles appartenant à votre PID.

Afin d’empêcher l’intégration accidentelle de fichiers et de données dans des sources de données cibles détenues par d’autres partenaires, Audience Manager a ajouté une exigence de mappage entre l’ID de partenaire (PID) et les sources de données (DPID) détenues par d’autres partenaires. En savoir plus sur PID et DPID dans la section [index des ID d’Audience Manager](https://experienceleague.adobe.com/docs/audience-manager/user-guide/reference/ids-in-aam.html).

À des fins de partage de données de deuxième niveau, si un partenaire ou un client d’Audience Manager souhaite ingérer des fichiers dans une source de données cible qu’il ne possède pas, il doit demander un mappage entre son ID de partenaire (PID) et cette source de données spécifique (DPID). Si le mappage est manquant, les fichiers ne seront pas traités par la tâche de données entrantes et les données ne seront pas intégrées à l’Audience Manager.

Pour créer ce mapping, soumettez un ticket Jira à l’équipe d’ingénierie d’Audience Manager. Afficher un exemple de ticket Jira [here](https://jira.corp.adobe.com/browse/AAM-60353). Vous n’avez pas besoin de demander la création de mappages pour les relations de partage de données existantes.
