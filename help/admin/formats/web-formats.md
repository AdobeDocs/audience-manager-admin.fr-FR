---
description: Répertorie les macros que vous pouvez utiliser pour créer des fichiers de données HTTP. HTTP envoie les données au format JSON.
seo-description: Répertorie les macros que vous pouvez utiliser pour créer des fichiers de données HTTP. HTTP envoie les données au format JSON.
seo-title: Macros de format HTTP
title: Macros de format HTTP
uuid: 91021 f 60-75 d 0-4 b 1 d -86 ca -86 ca -91 c 9 dadafac 1
translation-type: tm+mt
source-git-commit: 1a547e421346a6bf281e2b3ff3a0bcb5cf1d78df

---


# Macros de format HTTP {#http-format-macros}

Répertorie les macros que vous pouvez utiliser pour créer [!DNL HTTP] des fichiers de données. [!DNL HTTP] envoie des données dans [!DNL JSON] un format.

Voir les exemples de macros de format [HTTP](../formats/web-format-examples.md) pour obtenir une liste et des exemples de combinaisons de macro couramment utilisées.

<table id="table_72A72EA63C3643FB84B47A76CD2CC1CA"> 
 <thead> 
  <tr> 
   <th colname="col1" class="entry"> Macro </th> 
   <th colname="col2" class="entry"> Type de méthode </th> 
   <th colname="col3" class="entry"> Description </th> 
  </tr> 
 </thead>
 <tbody> 
  <tr> 
   <td colname="col1"> <p> <code>AAM_ UUID</code> </p> </td> 
   <td colname="col2"> <p> <code>GET</code> </p> </td> 
   <td colname="col3"> <p> <span class="keyword"> Identifiant Audience Manager </span> . </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>DP_ UUID</code> </p> </td> 
   <td colname="col2"> <p> <code>GET</code> </p> </td> 
   <td colname="col3"> <p>Utilisateur unique du partenaire de données - id. Cette macro renvoie l'ID que vous avez attribué à un utilisateur si son identifiant a déjà été synchronisé avec un <span class="keyword"> ID </span> de périphérique Audience Manager. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>DPID</code> </p> </td> 
   <td colname="col2"> <p> <code>GET</code> </p> </td> 
   <td colname="col3"> <p>Identifiant de fournisseur de données. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>ECID</code> </p> </td> 
   <td colname="col2"> <p> <code>GET</code> </p> </td> 
   <td colname="col3"> <p>Identifiant de fournisseur de données. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>GENERATION_ TIME</code> </p> </td> 
   <td colname="col2"> <p> <code>GET, POST</code> </p> </td> 
   <td colname="col3"> <p>Horodatage UNIX. Un horodatage interne représente le moment où AAM a été notifié de publier la destination <span class="wintitle"> S 2 S </span> auprès de nos partenaires. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>IP</code> </p> </td> 
   <td colname="col2"> <p> <code>GET</code> </p> </td> 
   <td colname="col3"> <p>Adresse IP de l'utilisateur. </p> </td> 
  </tr>
    <tr> 
   <td colname="col1"> <p> <code>MCID</code> </p> </td> 
   <td colname="col2"> <p> <code>GET</code> </p> </td> 
   <td colname="col3"> <p>Experience Cloud ID. (MCID signifie Marketing Cloud, qui est le nom hérité du cloud Experience Cloud) </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>NUM_ REMOVED_ SEGMENTS</code> </p> </td> 
   <td colname="col2"> <p> <code>GET</code> </p> </td> 
   <td colname="col3"> <p>Nombre (entier) de segments auxquels un utilisateur n'appartient plus. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>NUM_ SEGMENTS</code> </p> </td> 
   <td colname="col2"> <p> <code>GET</code> </p> </td> 
   <td colname="col3"> <p>Nombre de segments auxquels un utilisateur appartient. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>ORDER_ ID</code> </p> </td> 
   <td colname="col2"> <p> <code>GET, POST</code> </p> </td> 
   <td colname="col3"> <p>ID de commande ou de destination. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>PID_ ALIAS</code> </p> </td> 
   <td colname="col2"> <p> <code>GET, POST</code> </p> </td> 
   <td colname="col3"> <p>Un alias pour l'ID de partenaire. Egalement appelé ID de compte étranger. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>ALÉATOIRE</code> </p> </td> 
   <td colname="col2"> <p> <code>GET</code> </p> </td> 
   <td colname="col3"> <p>Génère un nombre aléatoire. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>REGION_ ID_ LIST</code> </p> </td> 
   <td colname="col2"> <p> <code>GET</code> </p> </td> 
   <td colname="col3"> <p>Région d <a href="https://docs.adobe.com/help/en/audience-manager/user-guide/api-and-sdk-code/dcs/dcs-api-reference/dcs-regions.html"> 'Audience Manager DCS </a> dans laquelle l'activité a été créée.</p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>REMOVED_ SEGMENT_ LIST</code> </p> </td> 
   <td colname="col2"> <p> <code>GET</code> </p> </td> 
   <td colname="col3"> <p>Renvoie la liste des ID de segment, le cas échéant, auxquels ne correspond plus un utilisateur. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>REMOVED_ SEGMENTS</code> </p> </td> 
   <td colname="col2"> <p> <code>GET</code> </p> </td> 
   <td colname="col3"> <p>Liste des segments auxquels un utilisateur n'est plus admissible. Vous pouvez également renvoyer des champs de segment spécifiques qui incluent : </p> <p> 
     <ul id="ul_29B83093A7624A908F0C06F2A248981A"> 
      <li id="li_57A60A54F5D44E38ACB4E2648095F246"> <code>Traitalias</code> </li> 
      <li id="li_4079F646493F40DBA0CE75D662A69454"> <code>Legacysegmentid (anciennement segmentid)</code> </li> 
      <li id="li_D3509A2D379E4C1FB3BC1B5E7D45A916"> <code>Newsegmentid</code> </li> 
      <li id="li_EA901C20EEEB4CFAA39A5E0E822D2394"> <code>status</code> </li> 
      <li id="li_6310E21F88CC4691980DD3C9D551409F"> <code>Datetime</code> </li> 
     </ul> </p> <p>Spécifiez ces champs dans un tableau comme indiqué dans l'exemple suivant : </p> <p> <code>[&lt; REMOVED_ SEGMENTS : {seg|&lt; OPEN_ BRACKET &gt; « Mappage » : &lt; seg. traitalias &gt;, "Status : " &lt; seg. status &gt;, « Time » : &lt; seg. datetime &gt;, « legacysegmentid » : &lt; seg. legacysegmentid &gt;, « newsegmentid » : &lt; seg. newsegmentid &gt; &lt; CLOSE_ BRACKET &gt;} ; « separator = », " &gt;]</code> </p> <p>Voir aussi <a href="../formats/web-format-examples.md#reference_98828E32B0964FF9AAC7C5400E88BA31"> Exemples de macros de format HTTP </a>. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>REMOVED_ TIME_ LIST</code> </p> </td> 
   <td colname="col2"> <p> <code>GET</code> </p> </td> 
   <td colname="col3"> Liste des dernières exécutions pour les segments dont l'utilisateur n'est plus admissible. </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>REMOVED_ TRAITALIAS_ LIST</code> </p> </td> 
   <td colname="col2"> <p> <code>GET</code> </p> </td> 
   <td colname="col3"> <p>Liste de noms alias des segments auxquels un utilisateur n'est plus admissible. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>SEGMENT_ LIST</code> </p> </td> 
   <td colname="col2"> <p> <code>GET</code> </p> </td> 
   <td colname="col3"> <p>Renvoie une liste des ID de segment. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>SEGMENTS</code> </p> </td> 
   <td colname="col2"> <p> <code>GET</code> </p> </td> 
   <td colname="col3"> <p>Liste des segments auxquels un utilisateur est admissible. Vous pouvez également renvoyer des champs de segment spécifiques qui incluent : </p> <p> 
     <ul id="ul_9209683A8E0A4B8081E5EFA4602F743F"> 
      <li id="li_D796526C1C9E45BEA891D619539888C4"> <code>Traitalias</code> </li> 
      <li id="li_BF12E010E1AD432C84605B9817F209DD"> <code>Legacysegmentid (anciennement segmentid)</code> </li> 
      <li id="li_4A81E3B715254549B9EADB983A2FC32B"> <code>Newsegmentid</code> </li> 
      <li id="li_1F01A60829DF4C87879D94299E1D589C"> <code>status</code> </li> 
      <li id="li_E52F10CD5A04487D81A4B1750B0DC4E3"> <code>Datetime</code> </li> 
     </ul> </p> <p>Spécifiez ces champs dans un tableau comme indiqué dans l'exemple suivant : </p> <p> <code>[&lt; SEGMENTS : {seg|&lt; OPEN_ BRACKET &gt; « Mappage » : &lt; seg. traitalias &gt;, "Status : " &lt; seg. status &gt;, « Time » : &lt; seg. datetime &gt;, « legacysegmentid » : &lt; seg. legacysegmentid &gt;, « newsegmentid » : &lt; seg. newsegmentid &gt; &lt; CLOSE_ BRACKET &gt;} ; « separator = », " &gt;]</code> </p> <p>Voir aussi <a href="../formats/web-format-examples.md#reference_98828E32B0964FF9AAC7C5400E88BA31"> Exemples de macros de format HTTP </a>. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>TIME_ LIST</code> </p> </td> 
   <td colname="col2"> <p> <code>GET</code> </p> </td> 
   <td colname="col3"> <p>Liste des dernières exécutions. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>TIMESTAMP</code> </p> </td> 
   <td colname="col2"> <p> <code>GET</code> </p> </td> 
   <td colname="col3"> <p>Unix, horodatage UTC. Représente la dernière réalisation du segment. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>TRAITALIAS_ LIST</code> </p> </td> 
   <td colname="col2"> <p> <code>GET</code> </p> </td> 
   <td colname="col3"> <p>Liste des noms d'alias pour un segment particulier. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>USER_ AGENT</code> </p> </td> 
   <td colname="col2"> <p> <code>GET</code> </p> </td> 
   <td colname="col3"> <p>Agent utilisateur de la requête initiale. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>USER_ LIST</code> </p> </td> 
   <td colname="col2"> <p> <code>POST</code> </p> </td> 
   <td colname="col3"> <p>Liste de l'utilisateur <span class="keyword"> Audience Manager </span> - ID. Vous pouvez également renvoyer des champs spécifiques qui incluent les éléments suivants : </p> 
    <ul id="ul_B6857D809FDC46749B7E745BD8C45F8E"> 
     <li id="li_F31CD82D16ED41FD82518141D90B5B35"> <code>user. aamuuid</code> </li> 
     <li id="li_623FA758C84D4A2D9B25C7FBE90F62B7"> <code>user. dpuuid</code> </li> 
     <li id="li_976B941908EB494EB476B5FB68B8972D"> <code>user. segments</code> </li> 
     <li id="li_D7E129833D1E4D59A554FFCE353924EE"> <code>user. removedsegments</code> </li> 
     <li id="li_8B3DD69D3FE3493492FC9F162812FCD5"> <code>user. useragent</code> </li> 
     <li id="li_8C7EA05585A64141876DF169C31322FE"> <code>user. ip</code> </li> 
     <li id="li_678076A31A7743C480F718C9E7A07E99"> <code>user. dpuuids</code> </li> 
     <li id="li_B598A5AED28C4304972E51DBD4E480D8"> <code>user. timestamp</code> </li> 
     <li id="li_8424D540282F449CA5AF6B3CC343DDCB"> <code>user. random</code> </li>
     <li><code>user. regionids</code></li> 
    </ul> <p>Spécifiez ces champs comme indiqué dans l'exemple suivant : </p> <p> 
     <codeblock>
       « AAM_ UUID » : « &lt; user. aamuuid &gt; » 
« datapartner_ UUID » : « &lt; user. dpuuid &gt; » 
     </codeblock> </p> <p>Voir aussi <a href="../formats/web-format-examples.md#reference_98828E32B0964FF9AAC7C5400E88BA31"> Exemples de macros de format HTTP </a> pour obtenir un exemple complet. </p> </td> 
  </tr>
 </tbody>
</table>