---
description: Informations que vous devriez encourager vos clients à connaître lorsqu’ils utilisent les API d’Audience Manager.
seo-description: Things you should encourage your clients to be aware of when they're working with the Audience Manager APIs.
seo-title: API Requirements and Recommendations
title: Configuration requise pour l’API et Recommendations
uuid: eba9cf92-f0c8-4394-8532-0de9a2e7b103
exl-id: 24f90732-31a6-436d-862b-e6871d279c7a
source-git-commit: c7c5da62b32f6a56152e1c09a965facfc601cade
workflow-type: tm+mt
source-wordcount: '334'
ht-degree: 0%

---

# Configuration requise pour l’API et Recommendations {#api-requirements-and-recommendations}

Informations que vous devriez encourager vos clients à connaître lorsqu&#39;ils travaillent avec l&#39;Audience Manager [!DNL API].

## Exigences {#requirements}

Notez ce qui suit lorsque vous utilisez du code [!DNL Audience Manager] [!DNL API] :

* **Paramètres de requête :** Tous les paramètres de requête sont requis, sauf indication contraire.
* **[!DNL JSON]type de contenu :** Spécifiez `content-type: application/json` *et* `accept: application/json` dans votre code.

* **Requêtes et réponses :** envoyez des requêtes sous la forme d’un objet [!DNL JSON] correctement formaté. [!DNL Audience Manager] répond avec [!DNL JSON] données formatées. Les réponses du serveur peuvent contenir les données demandées, un code d’état ou les deux.

* **Accès :** Votre consultant [!DNL Audience Manager] vous fournira un identifiant client et une clé qui vous permettront d’effectuer des requêtes [!DNL API].

* **Documentation et exemples de code :** Le texte en *italics* représente une variable que vous fournissez ou transmettez lors de la création ou de la réception de données [!DNL API]. Remplacez le texte *italicized* par votre propre code, paramètres ou d’autres informations requises.

## Recommendations : création d’un utilisateur API générique {#recommendations}

Nous vous recommandons de créer un compte utilisateur technique distinct pour travailler avec les Audiences Manager [!DNL API]. Il s’agit d’un compte générique qui n’est pas lié ou associé à un utilisateur spécifique de l’organisation de votre client. Ce type de compte utilisateur [!DNL API] permet d’accomplir 2 tâches :

* Identifiez le service qui appelle le [!DNL API] (par exemple, les appels d&#39;une application cliente qui utilisent nos [!DNL API] ou qui effectuent des modifications en masse).
* Accordez un accès ininterrompu aux [!DNL API]. Un compte lié à un employé spécifique peut être supprimé lorsqu’il quitte la société. Cela empêchera vos clients de travailler avec le code [!DNL API] disponible. Un compte générique qui n’est pas lié à un employé particulier permet d’éviter ce problème.

À titre d’exemple ou de cas d’utilisation pour ce type de compte, supposons que vos clients souhaitent modifier de nombreux segments à la fois avec les [outils de gestion en bloc](https://experienceleague.adobe.com/docs/audience-manager/user-guide/reference/bulk-management-tools/bulk-management-intro.html?lang=en). Pour cela, ils ont besoin d’un accès [!DNL API]. Au lieu d’ajouter des autorisations à un utilisateur spécifique, créez un compte utilisateur [!DNL API] non spécifique disposant des informations d’identification, de la clé et du secret appropriés pour effectuer des appels [!DNL API]. Ceci est également utile si les clients développent leurs propres applications qui utilisent les [!DNL Audience Manager] [!DNL API].
