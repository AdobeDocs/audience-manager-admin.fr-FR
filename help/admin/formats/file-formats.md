---
description: Liste les macros que vous pouvez utiliser pour créer des fichiers de données FTP. Certaines macros peuvent être utilisées pour tous les champs et lignes de fichier de données. Les autres macros sont spécifiques aux lignes d’en-tête et de données uniquement.
seo-description: Liste les macros que vous pouvez utiliser pour créer des fichiers de données FTP. Certaines macros peuvent être utilisées pour tous les champs et lignes de fichier de données. Les autres macros sont spécifiques aux lignes d’en-tête et de données uniquement.
seo-title: Macros Format du fichier
title: Macros Format du fichier
uuid: f91c91b6-6581-4ed7-8d7f-f8532bd41df9
translation-type: tm+mt
source-git-commit: 0ee7aa9c13f1b9b8fd64dddff4e52d101055e77c
workflow-type: tm+mt
source-wordcount: '717'
ht-degree: 2%

---


# Macros Format du fichier {#file-format-macros}

Liste les macros que vous pouvez utiliser pour créer des fichiers de données [!DNL FTP]. Certaines macros peuvent être utilisées pour tous les champs et lignes de fichier de données. Les autres macros sont spécifiques aux lignes d’en-tête et de données uniquement.

## Macros courantes {#common-macros}

Ces macros peuvent être utilisées dans n’importe quel champ de format. Pour obtenir des exemples, voir [Exemples de macro de format de fichier](../formats/file-format-examples.md).

<table id="table_A3309E175ABF4651BD11CE3632B3C553"> 
 <thead> 
  <tr> 
   <th colname="col1" class="entry"> Macro </th> 
   <th colname="col2" class="entry"> Description </th> 
  </tr> 
 </thead>
 <tbody> 
  <tr> 
   <td colname="col1"> <p> <code>ASCII_SOH</code> </p> </td> 
   <td colname="col2"> <p>Caractère ASCII non imprimable. Il indique le début d’une rangée ou d’une section de contenu. Il peut également être utilisé pour séparer les colonnes de données dans un fichier. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>DPID</code> </p> </td> 
   <td colname="col2"> <p>ID du fournisseur de données de cible. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>MASTER_DPID</code> </p> </td> 
   <td colname="col2"> <p>ID utilisateur ID du fournisseur de données de clé. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>ORDER_ID</code> </p> </td> 
   <td colname="col2"> <p>ID de commande/de destination. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>PIDALIAS</code> </p> </td> 
   <td colname="col2"> <p>Un alias pour un ID de commande/destination. </p> <p>La valeur de cet alias est définie dans le champ <span class="wintitle"> ID de compte étranger </span> pour une destination (dans la section <span class="wintitle"> Paramètres de base </span>). </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>SYNC_MODE</code> </p> </td> 
   <td colname="col2"> <p>Indique le type de synchronisation. Accepte les variables facultatives suivantes : </p> 
    <ul id="ul_87E8E3CE6565447A9810B5119298CC7B"> 
     <li id="li_66F4889FB84E40AC92F69F3FF6B0042C"> <code>full</code>: Synchronisation complète. </li> 
     <li id="li_BFE2C2D9A33A44FB9A840A7232ECCFFF"> <code>iter</code>: Synchronisation incrémentielle. </li> 
    </ul> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>SYNC_TYPE</code> </p> </td> 
   <td colname="col2"> <p>Indique la méthode de transfert de données. Accepte les variables facultatives suivantes : </p> 
    <ul id="ul_13BE35BBBF7C4C67AEFC514C5D192902"> 
     <li id="li_195FE9B4C5494600BD17D7172A8FB630"> <code>ftp</code> </li> 
     <li id="li_751AD59C4C934D66BC530D9806B500AF"> <code>http</code> </li> 
     <li id="li_4638AF7D1FB54E2C890045048B85309C"> <code>s3</code> </li> 
    </ul> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>TIMESTAMP</code> </p> </td> 
   <td colname="col2"> <p>Horodatage à 10 chiffres, UTC, Unix. </p> <p>Il peut également être formaté sous la forme <code>YYYYMMDDhhmmss</code> suivant les règles de formatage de date/horodatage Java. </p> </td> 
  </tr> 
 </tbody> 
</table>

## Macros de champ d’en-tête {#header-field-macros}

Macros utilisées uniquement dans les champs d’en-tête. Pour obtenir des exemples, voir [Exemples de macro de format de fichier](../formats/file-format-examples.md).

<table id="table_1A8BD1750F4940B3A34E3F80371A447A"> 
 <thead> 
  <tr> 
   <th colname="col1" class="entry"> Macro </th> 
   <th colname="col2" class="entry"> Description </th> 
  </tr> 
 </thead>
 <tbody> 
  <tr> 
   <td colname="col1"> <p> <code>TAB</code> </p> </td> 
   <td colname="col2"> <p>Utilisée comme séparateur, cette macro insère un onglet entre les champs. </p> </td> 
  </tr> 
 </tbody> 
</table>

## Macros de ligne de données {#data-row-macros}

Macros utilisées dans les lignes de données uniquement. Pour obtenir des exemples, voir [Exemples de macro de format de fichier](../formats/file-format-examples.md).

<table id="table_E378F94A3907407AA8110C8EE6C10909"> 
 <thead> 
  <tr> 
   <th colname="col1" class="entry"> Macro </th> 
   <th colname="col2" class="entry"> Description </th> 
  </tr> 
 </thead>
 <tbody> 
  <tr> 
   <td colname="col1"> <p> <code>CLOSE_CURLY_BRACKET</code> </p> </td> 
   <td colname="col2"> <p>Insère un caractère de crochet fermé <code>}</code>. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>COMMA</code> </p> </td> 
   <td colname="col2"> <p>Insère une virgule. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>DP_UUID</code> </p> </td> 
   <td colname="col2"> <p> <span class="term"> Identifiant utilisateur unique du partenaire de données  </span>. Renvoie l'identifiant que vous avez attribué à un utilisateur/visiteur de site si cet identifiant a déjà été synchronisé avec un ID de périphérique <span class="keyword"> Audience Manager </span>. </p> <p>Si le DPID est égal à 0, cette macro renvoie l'identifiant <span class="keyword"> Audience Manager </span> à la place de l'identifiant de l'utilisateur. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>DP_UUID_LIST</code> </p> </td> 
   <td colname="col2"> <p>Renvoie une liste qui contient plusieurs ID pour un partenaire de données. Cela s’avère utile si vous disposez d’une grande organisation avec plusieurs sous-divisions ou d’autres groupes d’organisation avec lesquels vous pouvez partager des données. Cette macro renvoie une liste des identifiants pour ces groupes Secondaires. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>DPUUIDS</code> </p> </td> 
   <td colname="col2"> <p>La sortie de cette macro mappe l’ID de fournisseur de données (DPID) aux ID d’utilisateur uniques associés (DPUUID). Cette macro doit avoir une chaîne de formatage pour contrôler sa sortie. L’exemple de sortie se présenterait comme suit : </p> <p> <code>"dpids=dpid1,dpid2,...dpid n|maxMappings= n|format=json"</code> </p> <p>Le paramètre <code>maxMappings</code> détermine le nombre de correspondances que la macro doit renvoyer. Lorsque <code>maxMappings=0</code>, cette macro renvoie tous les mappages pour chaque DPID spécifié. Les données sont triées par horodatage (le plus récent en premier) et renvoient d’abord les résultats avec l’horodatage le plus grand. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>endif</code> </p> </td> 
   <td colname="col2"> <p>Requis lors de l’utilisation des macros conditionnelles <code>if</code> et <code>SEGMENT_LIST</code> et <code>REMOVED_SEGMENT_LIST</code>. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>if(SEGMENT_LIST &amp;&amp; REMOVED_SEGMENT_LIST)endif</code> </p> </td> 
   <td colname="col2"> <p>Cette combinaison de macros crée une instruction conditionnelle indiquant que les listes des segments auxquels appartiennent les utilisateurs <i>et</i> ont été supprimées. Elle renvoie une chaîne vide si les deux conditions ne sont pas remplies ou s’il n’y a aucune donnée. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>MCID</code> </p> </td> 
   <td colname="col2"> <p> <span class="keyword"> Identifiant Adobe Experience Cloud.</span> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>OPEN_CURLY_BRACKET</code> </p> </td> 
   <td colname="col2"> <p>Insère un caractère d’accolade <code>{</code> ouvert. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>OPT_OUT</code> </p> </td> 
   <td colname="col2"> <p>Obsolète. Ne pas utiliser. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>OUTPUT_ATTRIBUTE_TYPE</code> </p> </td> 
   <td colname="col2"> <p>Obsolète. Ne pas utiliser. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>OUTPUT_ATTRIBUTE_VALUE</code> </p> </td> 
   <td colname="col2"> <p>Renvoie <code>1</code> en tant que valeur statique codée en dur. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>PID</code> </p> </td> 
   <td colname="col2"> <p>ID de partenaire (PID). Le PID s’affiche sous l’onglet <span class="wintitle"> Profil </span> dans l’interface utilisateur d’administration. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>REMOVED_SEGMENT_LIST</code> </p> </td> 
   <td colname="col2"> <p>Renvoie une liste de segments, le cas échéant, qui ont été supprimés. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>SEGMENT_LIST</code> </p> </td> 
   <td colname="col2"> <p>Renvoie une liste de segments dans une liste. Accepte les variables facultatives suivantes : </p> 
    <ul id="ul_B111AA0D6C18445598A1444B8B7E9325"> 
     <li id="li_8603B40229624856AF1FBC434DB8F16A"> <code>segmentId</code>: Identifiant hérité. Obsolète. Utilisez <code>sid</code> (minuscule uniquement). </li> 
     <li id="li_1EF40DDCA3C5447586904CF021D8F912"> <code>csegid</code>: Identifiant hérité. Obsolète. Utilisez <code>sid</code> (minuscule uniquement). </li> 
     <li id="li_D85F0A5D16AE4DAFB55C17DBB35EA66E"> <code>sid</code>: ID de segment. </li> 
     <li id="li_9BE103EFD8384464B46FAC00422431DB"> <code>type</code>: Renvoie  <code>5</code>une valeur statique codée en dur qui identifie les données comme des données de segment. </li> 
     <li id="li_FE5049089F2944FA9DB9F9D546DBA167"> <code>alias</code>: Mappage du segment. Obsolète. Utilisez <code>sid</code> (minuscule uniquement). </li> 
     <li id="li_DD778AA2D1DB4D409CF5026B5D9DBD27"> <code>lastUpdateTime</code>: Horodatage Unix qui indique la dernière fois qu’un segment a été réalisé. </li> 
    </ul> <p>Placez ces variables entre accolades après la macro. Par exemple, ce code sépare les résultats par une barre verticale "|" : <code>&lt;SEGMENT_LIST:{seg|&lt;seg.type&gt;,&lt;seg.sid&gt;}; separator="|"&gt;</code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>SET_ATTRIBUTES</code> </p> </td> 
   <td colname="col2"> <p>Renvoie <code>1</code> en tant que valeur statique codée en dur. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>TAB</code> </p> </td> 
   <td colname="col2"> <p>Insère un séparateur de tabulation. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>TRAIT_LIST</code> </p> </td> 
   <td colname="col2"> <p>Renvoie une liste de caractéristiques. Accepte les arguments facultatifs suivants : </p> 
    <ul id="ul_757DEB56E4F849768468F3C166B0D171"> 
     <li id="li_859E1F4F21D645519F150DC512B3EB1A"> <code>type</code>: Types de caractéristiques identifiés par un ID numérique. Cette variable renvoie : 
      <ul id="ul_C9839266783D42CCADAAC3FEA33BE4D7"> 
       <li id="li_6996A218E3F04EC3BC70032559DD87FC"> <code>10</code> qui identifie une caractéristique DPM (hors ligne, intégrée par une tâche entrante). </li> 
       <li id="li_831FF929BF50434C8804C13E5786DF79"> <code>3</code> qui identifie une caractéristique basée sur des règles (en temps réel, intégré par le biais du  <span class="wintitle"> serveur de collecte de données  </span>). </li> 
      </ul> </li> 
     <li id="li_E84D6BC80AEE4F10963C9882C4151ED4"> <code>traitId</code>: ID de caractéristique. </li> 
     <li id="li_D30A849BA35248E6B9110FA3ADEFC332"> <code>lastRealized</code>: La dernière fois que le trait a été réalisé. Horodatage Unix. </li> 
    </ul> <p>Placez ces variables entre accolades après la macro. Par exemple, ce code sépare les résultats par une barre verticale "|" : <code>TRAIT_LIST{type|traitId};separator="|"</code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>UUID</code> </p> </td> 
   <td colname="col2"> <p> <span class="keyword"> ID  </span> utilisateur de l’Audience Manager. </p> </td> 
  </tr> 
 </tbody> 
</table>