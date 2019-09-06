---
description: Ce que vous devez encourager vos clients à savoir quand ils travaillent avec les API Audience Manager.
seo-description: Ce que vous devez encourager vos clients à savoir quand ils travaillent avec les API Audience Manager.
seo-title: Exigences et recommandations relatives à l'API
title: Exigences et recommandations relatives à l'API
uuid: eba 9 cf 92-f 0 c 8-4394-8532-0 de 9 a 2 e 7 b 103
translation-type: tm+mt
source-git-commit: be661580da839ce6332a0ad827dec08e854abe54

---


# Exigences et recommandations relatives à l'API {#api-requirements-and-recommendations}

Ce que vous devez encourager vos clients à savoir quand ils travaillent avec Audience Manager [!DNL API]s.

## Conditions requises {#requirements}

Tenez compte des points suivants lorsque vous travaillez avec [!DNL Audience Manager][!DNL API] le code :

* **Paramètres de requête :** Tous les paramètres de requête sont obligatoires sauf indication contraire.
* **[!DNL JSON]type de contenu :** Spécifiez `content-type: application/json`*et* `accept: application/json` dans votre code.

* **Demandes et réponses :** Envoyer des requêtes en tant [!DNL JSON] qu'objet correctement formaté. [!DNL Audience Manager] répond aux [!DNL JSON] données formatées. Les réponses au serveur peuvent contenir les données demandées, un code d'état ou les deux.

* **Accès :** Votre [!DNL Audience Manager] consultant vous fournira un identifiant client et une clé qui vous permettront de [!DNL API] créer des requêtes.

* **Documentation et exemples de code :** Le texte *en italique* représente une variable que vous fournissez ou que vous transmettez lors de la création ou de la réception [!DNL API] de données. Remplacez *le texte en italique* par votre propre code, paramètres ou d'autres informations requises.

## Recommandations : Création d'un utilisateur API générique {#recommendations}

Nous vous recommandons de créer un compte d'utilisateur technique distinct pour travailler avec Audience Manager [!DNL API]. Il s'agit d'un compte générique qui n'est associé ou associé à aucun utilisateur spécifique de l'organisation de votre client. Ce type de compte [!DNL API] d'utilisateur permet d'accomplir 2 tâches :

* Identifiez le service qui appelle les [!DNL API] (appels par exemple d'une application cliente qui utilise notre [!DNL API]s ou effectuez des modifications en masse).
* Fournissez un accès sans interruption aux [!DNL API]s. Un compte lié à un employé spécifique peut être supprimé lorsqu'il quitte la société. Cela empêchera vos clients de travailler avec [!DNL API] le code disponible. Un compte générique qui n'est lié à aucun employé particulier permet d'éviter ce problème.

À titre d'exemple ou de cas d'utilisation pour ce type de compte, imaginons que vos clients souhaitent modifier simultanément beaucoup de segments avec les [outils de gestion en masse](https://docs.adobe.com/content/help/en/audience-manager/user-guide/reference/bult-management-tools/bulk-management-intro.html). Pour ce faire, ils doivent [!DNL API] accéder. Plutôt que d'ajouter des autorisations à un utilisateur spécifique, créez un compte [!DNL API] utilisateur non spécifique possédant les informations d'identification, la clé et le secret appropriés pour [!DNL API] effectuer des appels. Cela s'avère également utile si le client développe ses propres applications qui utilisent [!DNL Audience Manager][!DNL API]s.
