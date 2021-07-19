---
description: L’environnement bêta est destiné au test des mises en oeuvre d’Audience Manager. Les modifications effectuées en version bêta n’affectent pas les données de production. L’environnement bêta d’Audience Manager est une version autonome à plus petite échelle de l’environnement de production. Toutes les données que vous souhaitez tester doivent être entrées et collectées dans cet environnement.
seo-description: L’environnement bêta est destiné au test des mises en oeuvre d’Audience Manager. Les modifications effectuées en version bêta n’affectent pas les données de production. L’environnement bêta d’Audience Manager est une version autonome à plus petite échelle de l’environnement de production. Toutes les données que vous souhaitez tester doivent être entrées et collectées dans cet environnement.
seo-title: Environnement bêta
solution: Audience Manager
title: Environnement bêta
uuid: 6a253f4e-96e7-4395-a783-a8eb213b7daf
exl-id: 78d5a1ff-c016-4366-ba34-9814a0d92067
source-git-commit: f5d74995f0664cf63e68b46f1f3c608f34df0e80
workflow-type: tm+mt
source-wordcount: '414'
ht-degree: 3%

---

# Environnement bêta {#beta-environment}

L’environnement bêta est destiné au test des mises en oeuvre d’Audience Manager. Les modifications effectuées en version bêta n’affectent pas les données de production. L’environnement bêta d’Audience Manager est une version autonome à plus petite échelle de l’environnement de production. Toutes les données que vous souhaitez tester doivent être entrées et collectées dans cet environnement.

## Présentation {#overview}

<!-- beta_environment_admin.xml -->

| Service | URL/Nom d’hôte | Procédure de configuration |
|--- |--- |--- |
| S3 |  | Voir [Configuration des compartiments Amazon S3](admin-beta-environment.md#provision-s3-buckets). |
| DCS | https&amp;deux-points;//dcs-beta.demdex.net/... | Pas besoin de pas supplémentaires de notre côté. Voir [Accès au DCS dans l’environnement bêta](admin-beta-environment.md#access-dcs-beta-environment). |
| IU | https&amp;deux-points;//bank-beta.demdex.com | Les données sont copiées de la production vers l’environnement bêta tous les mois. Les informations d’identification de production sont valides pour la version bêta. |
| API | https&amp;deux-points;//api-beta.demdex.com/... | Les données sont copiées de la production vers l’environnement bêta tous les mois. Les informations d’identification de production sont valides pour la version bêta. |

## Configuration des compartiments Amazon S3 {#provision-s3-buckets}

>[!NOTE]
>
>Nous nous éloignons de l’utilisation de [!DNL FTP/SFTP]. Notez également que les transferts de données sortants ne fonctionnent pas pour l’environnement bêta.

Pour configurer des compartiments [!DNL S3] pour les données entrantes :

1. Utilisez la fonction [**Aide des opérations techniques de demande SKMS**](https://skms.adobe.com/).
1. Accédez à **[!UICONTROL Request TechOps Help]** dans le rail de navigation de gauche.
1. Dans **[!UICONTROL Request Search]**, saisissez Audience Manager dans le champ de recherche.
1. Faites défiler les résultats de la recherche vers le bas et cliquez sur **Audience Manager - S3 Inbound / Outbound Account Provisioning**.
1. Renseignez les champs de la fenêtre de configuration et spécifiez **Environnement Sandbox** dans le champ **[!UICONTROL Environment]**.

>[!NOTE]
>
>Nous décourageons l&#39;utilisation de [!DNL FTP/SFTP] et encourageons l&#39;utilisation de [!UICONTROL Amazon S3]. Les raisons pour lesquelles nous encourageons l’utilisation de [!UICONTROL Amazon S3] sont répertoriées dans [Amazon S3:About](https://docs.adobe.com/content/help/en/audience-manager/user-guide/reference/amazon-s3.html).

## Accès au DCS dans l’environnement bêta {#access-dcs-beta-environment}

Pour accéder à [!UICONTROL DCS] dans l’environnement bêta :

1. Effectuez un appel [!UICONTROL DCS] à l’aide de la [!DNL curl] [commande](https://curl.haxx.se/docs/manpage.html). [!DNL Curl] est un outil permettant de transférer des données depuis ou vers un serveur, à l’aide de l’un des nombreux protocoles pris en charge.

   Par exemple: `curl -v https://dcs-beta.demdex.net/event`

1. Vérifiez que votre requête a été traitée par la version bêta de [!UICONTROL DCS] en recherchant &quot;[!DNL sandbox]&quot; dans l’en-tête de réponse [!UICONTROL DCS].

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
