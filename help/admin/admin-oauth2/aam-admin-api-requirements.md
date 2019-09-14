---
description: Choses que vous devriez encourager vos clients à connaître lorsqu’ils travaillent avec les API d’Audience Manager.
seo-description: Choses que vous devriez encourager vos clients à connaître lorsqu’ils travaillent avec les API d’Audience Manager.
seo-title: ' Configuration requise et recommandations pour l’API'
title: ' Configuration requise et recommandations pour l’API'
uuid: eba9cf92-f0c8-4394-8532-0de9a2e7b103
translation-type: tm+mt
source-git-commit: be661580da839ce6332a0ad827dec08e854abe54

---


# Configuration requise et recommandations pour l’API {#api-requirements-and-recommendations}

Choses que vous devriez encourager vos clients à connaître lorsqu’ils travaillent avec les gestionnaires d’audience [!DNL API].

## Conditions requises {#requirements}

Tenez compte des points suivants lorsque vous utilisez [!DNL Audience Manager] du code [!DNL API] :

* **** Paramètres de requête : Tous les paramètres de requête sont obligatoires, sauf indication contraire.
* **[!DNL JSON]** type de contenu : Spécifiez `content-type: application/json` et ** `accept: application/json` dans votre code.

* **** Demandes et réponses : Envoyez des requêtes sous la forme d’un [!DNL JSON] objet correctement formaté. [!DNL Audience Manager] répond par des données [!DNL JSON] formatées. Les réponses du serveur peuvent contenir des données demandées, un code d’état ou les deux.

* **** Accès : Votre [!DNL Audience Manager] consultant vous fournira un ID de client et une clé qui vous permettront de faire [!DNL API] des demandes.

* **** Documentation et exemples de code : Le texte en *italique* représente une variable que vous fournissez ou transmettez lors de la création ou de la réception de [!DNL API] données. Remplacez *le texte en italique* par votre propre code, paramètres ou autres informations requises.

## Recommandations : Création d’un utilisateur API générique {#recommendations}

Nous vous recommandons de créer un compte utilisateur technique distinct pour travailler avec les [!DNL API]Audience Manager. Il s’agit d’un compte générique qui n’est pas associé à un utilisateur spécifique de l’entreprise de votre client ou qui n’est pas lui-même associé. Ce type de compte [!DNL API] utilisateur permet d’accomplir deux tâches :

* Identifiez le service qui appelle le [!DNL API] (par exemple, les appels d’une application cliente qui utilise nos [!DNL API]applications ou qui effectuent des modifications en masse).
* Fournir un accès ininterrompu aux [!DNL API]s. Un compte lié à un employé spécifique peut être supprimé lorsqu'il quitte l'entreprise. Cela empêchera vos clients de travailler avec le [!DNL API] code disponible. Un compte générique qui n’est pas lié à un employé particulier permet d’éviter ce problème.

À titre d’exemple ou de cas d’utilisation pour ce type de compte, supposons que vos clients souhaitent modifier un grand nombre de segments à la fois avec les outils [de gestion en](https://docs.adobe.com/content/help/en/audience-manager/user-guide/reference/bult-management-tools/bulk-management-intro.html)masse. Pour ce faire, ils ont besoin d' [!DNL API] accès. Plutôt que d’ajouter des autorisations à un utilisateur spécifique, créez un compte utilisateur non spécifique [!DNL API] doté des informations d’identification, de la clé et du secret appropriés pour effectuer [!DNL API] des appels. Cela est également utile si les clients développent leurs propres applications qui utilisent les [!DNL Audience Manager] s [!DNL API]s.
