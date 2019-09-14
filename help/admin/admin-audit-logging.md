---
description: 'Utilisez la journalisation de l’audit comme premier emplacement lors du débogage des problèmes des clients. '
seo-description: 'Utilisez la journalisation de l’audit comme premier emplacement lors du débogage des problèmes des clients. '
seo-title: Journalisation de l'audit
title: Journalisation de l'audit
uuid: null
translation-type: tm+mt
source-git-commit: 190ba5c1215782e46c8e544c10679d451fbed134

---


# Journalisation de l'audit {#audit-logging}

Utilisez-le [!UICONTROL  Audit Logging] comme premier emplacement lors du débogage des problèmes des clients.

> [!NOTE]
>
>[!UICONTROL Audit Logging] est actuellement en cours d'élaboration et peut être modifiée. Veuillez consigner les problèmes rencontrés dans [!DNL JIRA] ([!DNL UI] l'équipe).

![Vue Journalisation de l'audit](assets/audit-logging-img.png)

Dans le sélecteur déroulant Type **** d’audit, choisissez entre :

* [!UICONTROL Partner]
* [!UICONTROL User]
* [!UICONTROL Group]
* [!UICONTROL Datasource Summary]
* [!UICONTROL General Datasource]
* [!UICONTROL Merge Rule Datasource]
* [!UICONTROL Data Feed]
* [!UICONTROL Data Feed Subscription]
* [!UICONTROL Trait Summary]
* [!UICONTROL Trait Rule]
* [!UICONTROL Segment Summary]
* [!UICONTROL Destination Summary]
* [!UICONTROL Server to Server Destination]
* [!UICONTROL Derived Signal]
* [!UICONTROL Model]
* [!UICONTROL Segment Test Group]

L’ID **d’objet** est l’ID de l’élément que vous recherchez. Consultez le tableau ci-dessous pour lequel l’ID correspond à l’ID d’objet dans chaque cas :

| Type d'audit | Identifiant d’objet |
---------|----------|
| [!UICONTROL Partner] | ID de partenaire - PID |
| [!UICONTROL User] | Identifiant utilisateur |
| [!UICONTROL Group] | B3 |
| [!UICONTROL Datasource Summary] | ID de source de données |
| [!UICONTROL General Datasource] | ID de source de données |
| [!UICONTROL Merge Rule Datasource] | ID de source de données |
| [!UICONTROL Data Feed] | ID du flux de données |
| [!UICONTROL Data Feed Subscription] | ID du flux de données |
| [!UICONTROL Trait Summary] | SID (caractéristique) |
| [!UICONTROL Trait Rule] | SID (caractéristique) |
| [!UICONTROL Segment Summary] |  |
| [!UICONTROL Destination Summary] |  |
| [!UICONTROL Server-to-Server Destination] | N/D |
| [!UICONTROL Derived Signal] | N/D |
| [!UICONTROL Model] | N/D |
| [!UICONTROL Segment Test Group] | N/D |

Utilisez [!UICONTROL Start Date] ([!DNL UTC]) et [!UICONTROL End Date] ([!DNL UTC]) pour limiter l’intervalle de temps des journaux.