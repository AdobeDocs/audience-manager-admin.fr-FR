---
description: Toutes les mises à jour (ajouts, suppressions et corrections) apportées au guide de l’administrateur d’Audience Manager, classées par date.
seo-description: Toutes les mises à jour (ajouts, suppressions et corrections) apportées au guide de l’administrateur d’Audience Manager, classées par date.
seo-title: Mises à jour de la documentation
title: Mises à jour de la documentation
uuid: 1c02dff5-8e3f-42bf-a50c-03b75e121ac7
exl-id: 8221b4df-99c2-47d3-a2ea-186a701a2b20
source-git-commit: 7767c20bf97ee5c602b60dc6c11a5cd2bf21835d
workflow-type: tm+mt
source-wordcount: '632'
ht-degree: 99%

---

# Mises à jour de la documentation {#documentation-updates}

Toutes les mises à jour (ajouts, suppressions et corrections) apportées au guide de l’administrateur d’Audience Manager, classées par date.

Pour plus d’informations sur les sorties, les améliorations et les corrections de bogues de fonctionnalités, consultez les [notes de mise à jour d’Experience Cloud](https://marketing.adobe.com/resources/help/fr_FR/whatsnew/). Pour lire les anciennes annonces Experience Cloud, voir les [notes de mise à jour précédentes](https://marketing.adobe.com/resources/help/fr_FR/whatsnew/c_legacy_releases.html). Pour les [!DNL Audience Manager] modifications apportées à la documentation, voir [Mises à jour de la documentation](https://docs.adobe.com/content/help/fr-FR/audience-manager/user-guide/documentation-updates/docs-2019.html).

## Mises à jour de la documentation AAM 2019 {#aam-2019-docs-updates}

| Rubrique | Description |
|--- |--- |
| Macros au format HTTP | Nous avons ajouté une nouvelle macro, `REGION_ID_LIST` ainsi que trois nouveaux champs `sda`, `sda` et `sda` à la macro `USER_LIST`. |
| Macros au format HTTP | Nous avons ajouté deux nouvelles macros : `ECID` et `MCID`. |

## Mises à jour de la documentation AAM 2018 {#aam-2018-docs-updates}

<!-- c_doc_updates.xml -->

<table id="table_AECF59E131F84E7791A5A421BFB203FA"> 
 <thead> 
  <tr> 
   <th colname="col1" class="entry"> Rubrique </th> 
   <th colname="col2" class="entry"> Description </th> 
  </tr>
 </thead>
 <tbody> 
  <tr> 
   <td colname="col1"> <p><a href="admin-servers/create-ftp-server.md#task_BF1DD0E5ECA64AEC87EACABFCAEA2C6D"> Création ou modification d’un serveur FTP</a> </p> </td> 
   <td colname="col2"> <p>Nous avons ajouté davantage d’informations concernant l’authentification par clé SSH pour les serveurs SFTP (étape 5). </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p><a href="admin-destination-troubleshooting.md#set-up-destinations-export"> Comment configurer vos destinations à exporter vers Experience Cloud...</a> </p> </td> 
   <td colname="col2"> <p>Cette page vous montre comment configurer les destinations pour exporter les données saisies en dehors du type d’identifiant souhaité dans les fichiers de données sortantes. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p><a href="admin-servers/admin-authorize-s3-cross-bucket.md#task_20B12994C5484A9D8CC40DF6F456CBE7"> Guide pratique : autoriser le partage des accès entre comptes dans les compartiments Amazon S3 pour les destinations par lots</a> </p> </td> 
   <td colname="col2"> <p>S’ils préfèrent ne pas partager les clés d’accès et les clés secrètes Amazon S3, nos clients peuvent utiliser des autorisations de compartiments entre comptes dans Amazon S3 pour la distribution de fichiers de données de sortie. Ce document vous montre comment configurer cette alternative dans l’interface utilisateur d’administration d’Audience Manager. </p> </td> 
  </tr> 
 </tbody> 
</table>

## Mises à jour de la documentation AAM 2017 {#aam-2017-docs-updates}

<table id="table_81D2DA9293A9417085C630D00A7C96E1"> 
 <thead> 
  <tr> 
   <th colname="col1" class="entry"> Rubrique </th> 
   <th colname="col2" class="entry"> Description </th> 
  </tr>
 </thead>
 <tbody> 
  <tr> 
   <td colname="col1"><a href="formats/web-formats.md#reference_C392124A5F3F42E49F8AADDBA601ADFE"> Macros au format HTTP</a> </td> 
   <td colname="col2">Macro <code>segmentId</code> remplacée par <code>legacySegmentId</code> et ajout de la macro <code>newSegmentId</code>. </td> 
  </tr> 
  <tr> 
   <td colname="col1"><a href="companies/admin-company-limits.md#task_3004C10CB9A9430A8D25E25BB830B5D6"> Gestion des limites de l’entreprise</a> </td> 
   <td colname="col2"> Ajout d’un nombre maximal de dossiers de caractéristiques et d’une profondeur de structure de caractéristiques à la documentation des limites. </td> 
  </tr> 
  <tr> 
   <td colname="col1"><a href="formats/enable-outbound-seq.md#concept_526744C9433F40BF8269E18245B2F0BD"> Activer les transferts de fichiers de séquences Hadoop pour les fichiers sortants</a> </td> 
   <td colname="col2"> Découvrez comment vous pouvez permettre aux clients d’envoyer des fichiers SEQ sortants vers leurs propres instances Hadoop. </td> 
  </tr> 
  <tr> 
   <td colname="col1"><a href="companies/admin-manage-containers.md#task_61DB5CEECC5049DD8D059C642AC3F967"> Gestion des conteneurs</a> </td> 
   <td colname="col2"> Ajout d’une instruction brève expliquant comment créer des conteneurs. </td> 
  </tr> 
  <tr> 
   <td colname="col1"><a href="companies/admin-manage-company-destinations.md#create-edit-company-destinations"> Création ou modification des destinations d’entreprise</a> </td> 
   <td colname="col2"> <p> 
     <ul id="ul_527E0E75C03846B0AB39EEE544904BE2"> 
      <li id="li_FC276B34158D44E3A5450C6C8BAF3184">Ajout d’instructions sur l’équilibrage de l’utilisation de synchronisations complètes et incrémentielles. </li> 
      <li id="li_3975DA78DE9E441D8F8CB80F752DD7B7">L’approvisionnement d’<span class="keyword">Adobe Media Optimizer</span> en tant que destination <span class="keyword">Audience Manager</span> est effectué au sein d’<span class="keyword">Adobe Media Optimizer</span>. </li> 
     </ul> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p><a href="companies/admin-manage-company-destinations.md#manage-company-destinations"> Gestion des destinations d’entreprise</a> </p> </td> 
   <td colname="col2"> <p>Révisions mineures. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p><a href="companies/admin-amo-sync.md#concept_2B5537233DAA4860B3503B344F937D83"> Synchronisation des identifiants avec Media Optimizer</a> </p> </td> 
   <td colname="col2"> <p>Nouvelle documentation qui décrit la case à cocher de synchronisation AMO de chaque conteneur d’entreprise. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p><a href="companies/admin-device-graph-options.md#concept_563615F1018340C683E0EE075F8F639D"> Options de Device Graph pour les entreprises</a> </p> </td> 
   <td colname="col2"> <p>Nouvelle documentation qui décrit la manière de configurer les options de Device Graph. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p><a href="admin-oauth2/aam-admin-api-requirements.md#concept_A7FAC9443CF34974A873E6B787616421"> Configuration requise et recommandations pour l’API</a> </p> </td> 
   <td colname="col2"> <p>Nouvelle documentation qui décrit certaines configurations requises et recommandations à connaître et à transmettre aux clients. Celles-ci sont reproduites dans la documentation publique portant le même titre, malgré certaines modifications apportées en vue d’être lues par une audience différente. Reportez-vous à la section <a href="https://docs.adobe.com/content/help/fr-FR/audience-manager/user-guide/api-and-sdk-code/rest-apis/aam-api-getting-started.translate.html#api-requirements-recommendations" format="https" scope="external"> Configuration requise et recommandations pour l’API</a> de la documentation publique. </p> </td> 
  </tr> 
 </tbody> 
</table>

## Mises à jour de la documentation AAM 2016 {#aam-2016-docs-updates}

<table id="table_E9D9810EA8244B58A4F27D56CFE521FD"> 
 <thead> 
  <tr> 
   <th colname="col1" class="entry"> Rubrique </th> 
   <th colname="col2" class="entry"> Description </th> 
  </tr>
 </thead>
 <tbody> 
  <tr> 
   <td colname="col1"><a href="admin-servers/create-ftp-server.md#task_BF1DD0E5ECA64AEC87EACABFCAEA2C6D"> Création ou modification d’un serveur FTP</a> </td> 
   <td colname="col2">Ajout de l’IP de FTP de sortie <b>52.44.29.204</b>. </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p><a href="companies/admin-manage-company-destinations.md#manage-company-destinations"> Gestion des destinations d’entreprise</a> </p> </td> 
   <td colname="col2"> <p>Révisions mineures. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p><a href="admin-servers/create-http-server.md#task_5BF59581868E4144B965D644D36BEACD"> Création ou modification d’un serveur HTTP</a> </p> </td> 
   <td colname="col2"> <p>Ajout d’une <b>signature HTTP</b> à l’assistant de configuration de création du serveur. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p><a href="admin-beta-environment.md#concept_4AA12E66F49A452C8BA4E91AA28060AA"> Environnement bêta</a> </p> </td> 
   <td colname="col2"> <p>Mise à jour des URL et des noms d’hôte dans l’environnement bêta. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p><a href="companies/outbound-active-user-filter.md#task_F5CF8BDDA5DB4D23837B59CADF7A623B"> Filtrage des données sortantes par utilisateurs actifs uniquement</a> </p> </td> 
   <td colname="col2"> <p>Instructions de génération d’un fichier de synchronisation complète qui n’inclut que des utilisateurs actifs. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p><a href="formats/web-formats.md#reference_C392124A5F3F42E49F8AADDBA601ADFE"> Macros au format HTTP</a> </p> </td> 
   <td colname="col2" morerows="1"> <p>Nouvelle documentation qui répertorie les macros HTTP ainsi que des exemples courants. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p><a href="formats/web-format-examples.md#reference_98828E32B0964FF9AAC7C5400E88BA31"> Exemples de macros au format HTTP</a> </p> </td> 
  </tr> 
 </tbody> 
</table>

## Mises à jour de la documentation AAM 2015 {#aam-2015-docs-updates}

<table id="table_90F524BAAED44A45A1F6BF8BBA9F26F9"> 
 <thead> 
  <tr> 
   <th colname="col1" class="entry"> Date et rubrique </th> 
   <th colname="col2" class="entry"> Description </th> 
  </tr>
 </thead>
 <tbody> 
  <tr> 
   <td colname="col1"> <p>Décembre 2015 </p> <p><a href="formats/formats.md#concept_66AA2E78A25C4973B3230D5F75B192A2"> Formats</a> </p> </td> 
   <td colname="col2"> <p>Révision de la section sur les macros et ajout d’exemples. </p> </td> 
  </tr> 
 </tbody> 
</table>

## Mises à jour de la documentation AAM 2014 {#aam-2014-docs-updates}

<table id="table_FA9962E19248418BA73D5A794A378C9D"> 
 <thead> 
  <tr> 
   <th colname="col1" class="entry"> Date et rubrique </th> 
   <th colname="col2" class="entry"> Description </th> 
  </tr>
 </thead>
 <tbody> 
  <tr> 
   <td colname="col1"> <p>12 novembre 2014 </p> <p> <a href="formats/formats.md#concept_66AA2E78A25C4973B3230D5F75B192A2"> Formats</a> </p> </td> 
   <td colname="col2"> <p>Ajout d’informations sur la macro &lt;MCID&gt;. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p>23 octobre 2014 </p> <p><a href="formats/admin-create-format.md#task_1A51FC9189DB439FB218D91F3875FD67"> Création ou modification d’un format</a> </p> </td> 
   <td colname="col2"> <p>Ajout d’informations concernant l’option <span class="wintitle"> .info Receipt</span>. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p>23 octobre 2014 </p> <p><a href="formats/formats.md#concept_66AA2E78A25C4973B3230D5F75B192A2"> Formats</a> </p> </td> 
   <td colname="col2"> <p>Nouvelle page. Notez que cette page n’est pas finalisée et qu’elle sera mise à jour dans les prochains jours. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p>22 octobre 2014 </p> <p><a href="admin-destination-troubleshooting.md#"> Dépannage des configurations de destination</a> </p> </td> 
   <td colname="col2"> <p>Nouvelle rubrique. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p>21 octobre 2014 </p> <p><a href="companies/admin-manage-company-destinations.md#manage-company-destinations"> Gestion des destinations d’entreprise</a> </p> </td> 
   <td colname="col2"> <p>Remaniement complet de la rubrique. Ajout d’informations et de paramètres supplémentaires. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p>25 septembre 2014 </p> <p><a href="companies/admin-manage-company-profiles.md"> Création d’une entreprise</a> </p> </td> 
   <td colname="col2"> <p>Ajout d’informations supplémentaires aux sections<span class="wintitle"> Cycle de vie</span> et<span class="wintitle"> Types de compte</span>. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p>25 septembre 2014 </p> <p><a href="companies/admin-manage-company-profiles.md#edit-company-profile"> Modification d’un profil d’entreprise</a> </p> </td> 
   <td colname="col2"> <p>Ajout d’informations supplémentaires aux sections<span class="wintitle"> Cycle de vie</span> et<span class="wintitle"> Types de compte</span>. </p> </td> 
  </tr> 
 </tbody> 
</table>
