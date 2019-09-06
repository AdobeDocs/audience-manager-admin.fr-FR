---
description: L'environnement bêta est destiné à tester les implémentations d'Audience Manager. Les modifications effectuées en version bêta n'affectent pas les données de production. L'environnement bêta d'Audience Manager est une version autonome à plus petite échelle de l'environnement de production. Toutes les données à tester doivent être entrées et collectées dans cet environnement.
seo-description: L'environnement bêta est destiné à tester les implémentations d'Audience Manager. Les modifications effectuées en version bêta n'affectent pas les données de production. L'environnement bêta d'Audience Manager est une version autonome à plus petite échelle de l'environnement de production. Toutes les données à tester doivent être entrées et collectées dans cet environnement.
seo-title: Environnement bêta
solution: Audience Manager
title: Environnement bêta
uuid: 6 a 253 f 4 e -96 e 7-4395-a 783-a 8 eb 213 b 7 daf
translation-type: tm+mt
source-git-commit: 7765dbf79c2fb6ca8c4b52fe8090c1fd11f9db27

---


# Environnement bêta {#beta-environment}

L'environnement bêta est destiné à tester les implémentations d'Audience Manager. Les modifications effectuées en version bêta n'affectent pas les données de production. L'environnement bêta d'Audience Manager est une version autonome à plus petite échelle de l'environnement de production. Toutes les données à tester doivent être entrées et collectées dans cet environnement.

## Aperçu {#overview}

<!-- beta_environment_admin.xml -->

| Service | URL/Nom d'hôte | Procédure de configuration |
|--- |--- |--- |
| S3 |  | Voir [Configuration des intervalles Amazon S 3](admin-beta-environment.md#provision-s3-buckets). |
| DCS | https &amp; amp ; deux-points ; // dcs-beta.demdex.net/.. | Aucune étape supplémentaire nécessaire de notre part. Voir [Accès au serveur de collecte de données dans l'environnement bêta](admin-beta-environment.md#access-dcs-beta-environment). |
| IU | https &amp; amp ; deux-points ; //bank-beta.demdex.com | Les données sont automatiquement copiées de la production vers l'environnement bêta. Les informations d'identification de production sont valides pour la version bêta. |
| API | https &amp; amp ; deux-points ; // api-beta.demdex.com/.. | Les données sont automatiquement copiées de la production vers l'environnement bêta. Les informations d'identification de production sont valides pour la version bêta. |

## Configuration des intervalles Amazon S 3 {#provision-s3-buckets}

>[!NOTE]
>
>Nous abandonnons l'utilisation [!DNL FTP/SFTP]. Notez également que les transferts de données sortants ne fonctionnent pas pour l'environnement bêta.

Pour configurer [!DNL S3] les intervalles pour les données entrantes :

1. Utilisez [**la fonction d'aide**](https://skms.adobe.com/) de la demande de service SKMS.
1. Accédez **[!UICONTROL Request TechOps Help]** au rail de navigation de gauche.
1. Dans **[!UICONTROL Request Search]**, saisissez Audience Manager dans le champ de recherche.
1. Faites défiler la liste vers le bas dans les résultats de la recherche et cliquez dans **Audience Manager - S 3 Inbound/Outbound Account Provisioning.**
1. Renseignez les champs de la fenêtre de mise en service et spécifiez **l'environnement Sandbox** dans **[!UICONTROL Environment]** le champ.

>[!NOTE]
>
>Nous déconseillons l'utilisation [!DNL FTP/SFTP] de cette méthode et nous encourageons l'utilisation [!UICONTROL Amazon S3]de. Les raisons pour lesquelles nous encourageons l'utilisation [!UICONTROL Amazon S3] de sont répertoriées dans [Amazon S 3 : A propos](https://docs.adobe.com/content/help/en/audience-manager/user-guide/reference/amazon-s3.html)de.

## Accès au serveur de collecte de données dans l'environnement bêta {#access-dcs-beta-environment}

Pour accéder à l [!UICONTROL DCS] 'environnement bêta :

1. [!UICONTROL DCS] Effectuez un appel à l'aide de [!DNL curl][la commande](https://curl.haxx.se/docs/manpage.html). [!DNL Curl] est un outil de transfert de données depuis ou vers un serveur, à l'aide de l'un des nombreux protocoles pris en charge.

   Par exemple : `curl -v https://dcs-beta.demdex.net/event`

1. Vérifiez que votre requête a été diffusée par la version bêta [!UICONTROL DCS] en recherchant « [!DNL sandbox]dans l'en-tête [!UICONTROL DCS] de réponse.

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