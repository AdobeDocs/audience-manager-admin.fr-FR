---
description: L’environnement bêta sert à tester les implémentations d’Audience Manager. Les modifications apportées en version bêta n’affectent pas les données de production. L’environnement bêta d’Audience Manager est une version autonome à plus petite échelle de l’environnement de production. Toutes les données que vous souhaitez tester doivent être saisies et collectées dans cet environnement.
seo-description: The beta environment is for testing Audience Manager implementations. Changes made in beta do not affect production data. The Audience Manager beta environment is a smaller-scale, standalone version of the production environment. All the data that you want to test must be entered and collected in this environment.
seo-title: Beta Environment
solution: Audience Manager
title: Environnement Beta
uuid: 6a253f4e-96e7-4395-a783-a8eb213b7daf
exl-id: 78d5a1ff-c016-4366-ba34-9814a0d92067
TQID: https://experienceleague.adobe.com/Y6hON41v53cSXtuTYMW8UMgimwyewWHvfcBvMYDnBa4
product_v2:
  - id: df80eeb1-8d72-467e-b0df-9d51c7d3a0a1
feature_v2:
  - id: a8b0238e-1d43-4679-a3b4-5ba1bad83baa
topic_v2:
  - id: b5ce8718-c3af-4fdb-a1a9-fca32f83a87c
  - id: c1579802-ddd4-4214-8a91-97b2066abe11
source-git-commit: d2bed13a6ac7d38ae79b65d492b6de0ca6b6d488
workflow-type: tm+mt
source-wordcount: 366
ht-degree: 2%

---

# Environnement Beta {#beta-environment}

L’environnement bêta sert à tester les implémentations d’Audience Manager. Les modifications apportées en version bêta n’affectent pas les données de production. L’environnement bêta d’Audience Manager est une version autonome à plus petite échelle de l’environnement de production. Toutes les données que vous souhaitez tester doivent être saisies et collectées dans cet environnement.

## Présentation {#overview}

<!-- beta_environment_admin.xml -->

| Service | URL/nom d&#39;hôte | Étapes de configuration |
|--- |--- |--- |
| S3 | | Voir [Configurer des compartiments Amazon S3](admin-beta-environment.md#provision-s3-buckets). |
| DCS | https&colon;//dcs-beta.demdex.net/... | Pas besoin d&#39;étapes supplémentaires de notre côté. Voir [Accès au serveur de collecte de données dans l’environnement Beta](admin-beta-environment.md#access-dcs-beta-environment). |
| IU | https&colon;//bank-beta.demdex.com | Les données sont copiées de l’environnement de production vers l’environnement bêta tous les mois. Les informations d’identification de production sont valides pour la version Beta. |
| API | https&colon;//api-beta.demdex.com/... | Les données sont copiées de l’environnement de production vers l’environnement bêta tous les mois. Les informations d’identification de production sont valides pour la version Beta. |

## Configurer les compartiments Amazon S3 {#provision-s3-buckets}

>[!NOTE]
>
>Nous nous éloignons de l&#39;utilisation de [!DNL FTP/SFTP]. Notez également que les transferts de données sortantes ne fonctionnent pas pour l’environnement bêta.

Pour configurer des intervalles de [!DNL S3] pour les données entrantes :

1. Utilisez la fonctionnalité [**Aide sur les opérations techniques des requêtes SKMS**](https://skms.adobe.com/).
1. Accédez à **[!UICONTROL Request TechOps Help]** dans le rail de navigation de gauche.
1. Dans **[!UICONTROL Request Search]**, saisissez Audience Manager dans le champ de recherche.
1. Faites défiler les résultats de la recherche vers le bas et cliquez sur **Audience Manager - Approvisionnement de compte entrant/sortant S3**.
1. Renseignez les champs de la fenêtre d’approvisionnement et spécifiez **Environnement de sandbox** dans le champ **[!UICONTROL Environment]** .

>[!NOTE]
>
>Nous décourageons l&#39;utilisation du [!DNL FTP/SFTP] et encourageons l&#39;utilisation du [!UICONTROL Amazon S3]. Les raisons pour lesquelles nous encourageons l’utilisation de [!UICONTROL Amazon S3] sont répertoriées dans [Amazon S3:About](https://experienceleague.adobe.com/docs/audience-manager/user-guide/reference/amazon-s3.html?lang=fr).

## Accès au serveur de collecte de données dans l’environnement Beta {#access-dcs-beta-environment}

Pour accéder au [!UICONTROL DCS] dans l’environnement Beta :

1. Effectuez un appel [!UICONTROL DCS] à l’aide de la [!DNL curl] [commande](https://curl.haxx.se/docs/manpage.html). [!DNL Curl] est un outil permettant de transférer des données depuis ou vers un serveur, à l’aide de l’un des nombreux protocoles pris en charge.

   Par exemple : `curl -v https://dcs-beta.demdex.net/event`

1. Vérifiez que votre requête a été diffusée par le [!UICONTROL DCS] bêta en recherchant « [!DNL sandbox] » dans l’en-tête de réponse [!UICONTROL DCS].

   Par exemple :

   ```
   curl -v http://dcs-beta.demdex.net/?event
   [...]
   < DCS: va6-sandbox-dcs-3.sandbox.demdex.com <release_number>
   [...]
   ```

<!--
1. Determine the load balancer's endpoint IP addresses.

   Run the `dig` [command](https://en.wikipedia.org/wiki/Dig_(command)) to determine the IP address of the nearest load balancer. The `dig` command queries the Domain Name System and returns the name and IP addresses of the Audience Manager [!UICONTROL Data Collection Servers (DCS)].

   ```
   dig dcs-beta.demdex.net
   ...
   dcs-sandbox-1754093861.us-east-1.elb.amazonaws.com. 60 IN A 52.87.15.51
   dcs-sandbox-1754093861.us-east-1.elb.amazonaws.com. 60 IN A 50.16.150.8
   dcs-sandbox-1754093861.us-east-1.elb.amazonaws.com. 60 IN A 52.2.228.100
   ```

1. Using one of the addresses in the above table, add a static DNS entry in the [!DNL `/etc/hosts`] file.

   On Windows, modify [!DNL `c:\WINDOWS\system32\drivers\etc\hosts`].

   For example:

[!DNL `52.87.15.51 samplepartner.demdex.net`]

   >[!NOTE]
   >
   >The addresses change occasionally, so you must keep your [!DNL /etc/hosts] file up to date.

   Additionally, if you need to set up ID synchronization, you must add a similar entry for [!DNL dpm.demdex.net.]

[!DNL `52.87.15.51 dpm.demdex.net`] [!DNL]. 

1. Make a [!UICONTROL DCS] call, using the `curl` [command](https://curl.haxx.se/docs/manpage.html). Curl is a tool to transfer data from or to a server, using one of many supported protocols.

   For example:

[!DNL `https://<domain>/event?product=camera`] 

1. Verify that your request was served by the beta [!UICONTROL DCS] by looking for "sandbox" in the [!UICONTROL DCS] response header.

   For example:

   ```
   curl -v https://dcs-beta.demdex.net/?event
   [...]
   < DCS: va6-sandbox-dcs-3.sandbox.demdex.com <release_number>
   [...]
   ```
-->
