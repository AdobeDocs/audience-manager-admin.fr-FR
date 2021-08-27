---
description: Informations que vous devriez encourager vos clients à connaître lorsqu’ils utilisent les API d’Audience Manager.
seo-description: Things you should encourage your clients to be aware of when they're working with the Audience Manager APIs.
seo-title: API Requirements and Recommendations
title: Configuration requise et recommandations pour l’API
uuid: eba9cf92-f0c8-4394-8532-0de9a2e7b103
exl-id: 24f90732-31a6-436d-862b-e6871d279c7a
source-git-commit: 79415eba732c2a6d50f04124774664f788ccc78c
workflow-type: tm+mt
source-wordcount: '340'
ht-degree: 2%

---

# Configuration requise et recommandations pour l’API {#api-requirements-and-recommendations}

Informations que vous devriez encourager vos clients à connaître lorsqu’ils travaillent avec les [!DNL API]Audiences Manager.

## Exigences {#requirements}

Notez ce qui suit lorsque vous utilisez le code [!DNL Audience Manager] [!DNL API] :

* **Paramètres de requête :** tous les paramètres de requête sont requis, sauf indication contraire.
* **[!DNL JSON]type de contenu :** indiquez  `content-type: application/json` ** `accept: application/json` et dans votre code.

* **Requêtes et réponses :** envoyez des requêtes sous la forme d’un  [!DNL JSON] objet correctement formaté. [!DNL Audience Manager] répond avec des données  [!DNL JSON] formatées. Les réponses du serveur peuvent contenir les données demandées, un code d’état ou les deux.

* **Accès :** votre  [!DNL Audience Manager] consultant vous fournira un identifiant client et une clé qui vous permettront d’effectuer  [!DNL API] des requêtes.

* **Documentation et exemples de code :** le texte en  ** italique représente une variable que vous fournissez ou transmettez lors de la création ou de la réception de  [!DNL API] données. Remplacez *italicized* par votre propre code, paramètres ou d’autres informations requises.

## Recommendations : Création d’un utilisateur API générique {#recommendations}

Nous vous recommandons de créer un compte utilisateur technique distinct pour travailler avec les [!DNL API]Audiences Manager. Il s’agit d’un compte générique qui n’est pas lié ou associé à un utilisateur spécifique de l’organisation de votre client. Ce type de compte utilisateur [!DNL API] permet d’accomplir 2 tâches :

* Identifiez le service qui appelle [!DNL API] (par exemple, les appels d’une application cliente qui utilisent nos [!DNL API]s ou qui effectuent des modifications en masse).
* Accordez un accès ininterrompu aux [!DNL API]s. Un compte lié à un employé spécifique peut être supprimé lorsqu’il quitte la société. Cela empêchera vos clients de travailler avec le code [!DNL API] disponible. Un compte générique qui n’est pas lié à un employé particulier permet d’éviter ce problème.

À titre d’exemple ou de cas d’utilisation pour ce type de compte, supposons que vos clients souhaitent modifier de nombreux segments à la fois avec les [outils de gestion en bloc](https://experienceleague.adobe.com/docs/audience-manager/user-guide/reference/bult-management-tools/bulk-management-intro.html). Pour cela, ils ont besoin d’un accès [!DNL API]. Au lieu d’ajouter des autorisations à un utilisateur spécifique, créez un compte utilisateur [!DNL API] non spécifique qui dispose des informations d’identification, de la clé et du secret appropriés pour effectuer des appels [!DNL API]. Cela s’avère également utile si les clients développent leurs propres applications qui utilisent les [!DNL Audience Manager] [!DNL API]s.
