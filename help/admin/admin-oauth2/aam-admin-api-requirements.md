---
description: Ce que vous devriez encourager vos clients à savoir quand ils travaillent avec les API d'Audience Manager.
seo-description: Ce que vous devriez encourager vos clients à savoir quand ils travaillent avec les API d'Audience Manager.
seo-title: Configuration requise et recommandations pour l’API
title: Configuration requise et recommandations pour l’API
uuid: eba9cf92-f0c8-4394-8532-0de9a2e7b103
translation-type: tm+mt
source-git-commit: be661580da839ce6332a0ad827dec08e854abe54
workflow-type: tm+mt
source-wordcount: '364'
ht-degree: 3%

---


# Configuration requise et recommandations pour l’API {#api-requirements-and-recommendations}

Les choses que vous devriez encourager vos clients à être conscients quand ils travaillent avec l&#39;Audience Manager [!DNL API]s.

## Exigences {#requirements}

Tenez compte des points suivants lorsque vous travaillez avec [!DNL Audience Manager] du [!DNL API] code :

* **Paramètres de requête :** Tous les paramètres de requête sont requis, sauf indication contraire.
* **[!DNL JSON]type de contenu :**Spécifiez`content-type: application/json`et **`accept: application/json`dans votre code.

* **Demandes et réponses :** Envoie les requêtes sous la forme d’un [!DNL JSON] objet correctement formaté. [!DNL Audience Manager] répond par des données [!DNL JSON] formatées. Les réponses du serveur peuvent contenir des données demandées, un code d’état ou les deux.

* **Accès :** Votre [!DNL Audience Manager] consultant vous fournira un ID de client et une clé qui vous permettront de faire [!DNL API] des demandes.

* **Documentation et exemples de code :** Le texte en *italique* représente une variable que vous fournissez ou transmettez lors de la création ou de la réception de [!DNL API] données. Remplacez le texte *en italique* par votre propre code, paramètres ou autres informations requises.

## Recommandations : Création d’un utilisateur API générique {#recommendations}

Nous vous recommandons de créer un compte utilisateur technique distinct pour travailler avec les Audiences Manager [!DNL API]s. Il s’agit d’un compte générique qui n’est pas lié ou associé à un utilisateur spécifique de l’entreprise de votre client. Ce type de compte [!DNL API] d’utilisateur permet d’accomplir deux tâches :

* Identifiez le service qui appelle le [!DNL API] (par exemple, les appels d’une application cliente qui utilise nos [!DNL API]applications ou qui effectuent des modifications en masse).
* Fournir un accès ininterrompu aux [!DNL API]s. Un compte lié à un employé donné peut être supprimé lorsqu&#39;il quitte la société. Cela empêchera vos clients de travailler avec le [!DNL API] code disponible. Un compte générique qui n’est pas lié à un employé particulier permet d’éviter ce problème.

À titre d&#39;exemple ou de cas d&#39;utilisation pour ce type de compte, supposons que vos clients souhaitent modifier un grand nombre de segments à la fois avec les outils [de gestion](https://docs.adobe.com/content/help/en/audience-manager/user-guide/reference/bult-management-tools/bulk-management-intro.html)en bloc. Pour ce faire, ils ont besoin d&#39; [!DNL API] accès. Plutôt que d’ajouter des autorisations à un utilisateur spécifique, créez un compte d’ [!DNL API] utilisateur non spécifique doté des informations d’identification, de la clé et du secret appropriés pour effectuer [!DNL API] des appels. Cela est également utile si les clients développent leurs propres applications qui utilisent les [!DNL Audience Manager] [!DNL API]s.
