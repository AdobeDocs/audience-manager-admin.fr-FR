---
description: Éléments à connaître lorsque vos clients utilisent les API d’Audience Manager.
seo-description: Things you should encourage your clients to be aware of when they're working with the Audience Manager APIs.
seo-title: API Requirements and Recommendations
title: Exigences et recommandations relatives aux API
uuid: eba9cf92-f0c8-4394-8532-0de9a2e7b103
exl-id: 24f90732-31a6-436d-862b-e6871d279c7a
TQID: https://experienceleague.adobe.com/mm5-TOwj8WckXoG4-E4wzuEF-1oBbxbBUvRLOoA--As
product_v2: id: df80eeb1-8d72-467e-b0df-9d51c7d3a0a1
feature_v2: id: baaa0dd2-d27e-4921-aae3-7888623a5fa5
source-git-commit: d2bed13a6ac7d38ae79b65d492b6de0ca6b6d488
workflow-type: tm+mt
source-wordcount: 350
ht-degree: 0%

---

# Exigences et recommandations relatives aux API {#api-requirements-and-recommendations}

Éléments à prendre en compte lorsque vos clients utilisent les [!DNL API] d’Audience Manager.

## Exigences {#requirements}

Notez ce qui suit lorsque vous utilisez [!DNL Audience Manager] code [!DNL API] :

* **Paramètres de requête :** tous les paramètres de requête sont requis, sauf indication contraire.
* **[!DNL JSON]le type de contenu :** spécifiez `content-type: application/json` *et* `accept: application/json` dans votre code.

* **Demandes et réponses :** envoyez les demandes sous la forme d’un objet [!DNL JSON] correctement formaté. [!DNL Audience Manager] répond avec des données formatées [!DNL JSON]. Les réponses du serveur peuvent contenir les données demandées, un code d’état, ou les deux.

* **Accès :** votre consultant [!DNL Audience Manager] vous fournira un identifiant client et une clé qui vous permettront d’effectuer des demandes de [!DNL API].

* **Documentation et exemples de code :** le texte en *italique* représente une variable que vous fournissez ou transmettez lors de l’exécution ou de la réception de données [!DNL API]. Remplacez le texte *en italique* par votre propre code, vos propres paramètres ou d’autres informations requises.

## Recommendations : création d’un utilisateur d’API générique {#recommendations}

Nous vous recommandons de créer un compte utilisateur technique distinct pour travailler avec les [!DNL API] Audience Manager. Il s’agit d’un compte générique qui n’est ni lié ni associé à un utilisateur spécifique de l’organisation de votre client. Ce type de compte utilisateur [!DNL API] permet d’accomplir deux choses :

* Identifiez le service qui appelle le [!DNL API] (par exemple, les appels provenant d’une application cliente qui utilise nos [!DNL API] ou qui effectuent des modifications en bloc).
* Assurer un accès ininterrompu aux [!DNL API]. Un compte lié à un employé spécifique peut être supprimé lorsqu’il quitte l’entreprise. Cela empêchera vos clients d’utiliser le code [!DNL API] disponible. Un compte générique qui n’est pas lié à un employé particulier permet d’éviter ce problème.

À titre d’exemple ou de cas d’utilisation pour ce type de compte, supposons que vos clients souhaitent modifier de nombreux segments à la fois à l’aide des [ outils de gestion en bloc ](https://experienceleague.adobe.com/docs/audience-manager/user-guide/reference/bulk-management-tools/bulk-management-intro.html?lang=en). Pour ce faire, ils ont besoin d’un accès [!DNL API]. Au lieu d’ajouter des autorisations à un utilisateur spécifique, créez un compte utilisateur [!DNL API] non spécifique disposant des informations d’identification, de la clé et du secret appropriés pour effectuer des appels [!DNL API]. Cela s’avère également utile si les clients développent leurs propres applications qui utilisent les [!DNL API] [!DNL Audience Manager].
