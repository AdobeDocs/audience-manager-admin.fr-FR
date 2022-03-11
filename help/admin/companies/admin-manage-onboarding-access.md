---
description: Afin d’empêcher l’intégration accidentelle de fichiers et de données dans des sources de données cibles détenues par d’autres partenaires ou clients, Audience Manager a ajouté une exigence de mappage entre l’ID de partenaire (PID) et les sources de données détenues par d’autres partenaires.
title: Gestion de l’accès à l’intégration pour les données de deuxième niveau
source-git-commit: 6c88979f876909bc32b5238605cb4a352e327a00
workflow-type: tm+mt
source-wordcount: '217'
ht-degree: 0%

---

# Gestion de l’accès à l’intégration pour les données de deuxième niveau {#manage-onboarding-access-for-second-party-data}

Afin d’empêcher l’intégration accidentelle de fichiers et de données dans des sources de données cibles détenues par d’autres partenaires, Audience Manager a ajouté une exigence de mappage entre l’ID de partenaire (PID) et les sources de données (DPID) détenues par d’autres partenaires. En savoir plus sur PID et DPID dans la section [index des ID d’Audience Manager](https://experienceleague.adobe.com/docs/audience-manager/user-guide/reference/ids-in-aam.html).

À des fins de partage de données de deuxième niveau, si un partenaire ou un client d’Audience Manager souhaite ingérer des fichiers dans une source de données cible qu’il ne possède pas, il doit demander un mappage entre son ID de partenaire (PID) et cette source de données spécifique (DPID). Si le mappage est manquant, les fichiers ne seront pas traités par la tâche de données entrantes et les données ne seront pas intégrées à l’Audience Manager.

Pour créer ce mapping, soumettez un ticket Jira à l’équipe d’ingénierie d’Audience Manager. Afficher un exemple de ticket Jira [here](https://jira.corp.adobe.com/browse/AAM-60353). Vous n’avez pas besoin de demander la création de mappages pour les relations de partage de données existantes.
