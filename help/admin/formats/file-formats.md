---
description: Répertorie les macros que vous pouvez utiliser pour créer des fichiers de données FTP. Certaines macros peuvent être utilisées pour tous les champs et lignes de fichier de données. D'autres macros sont spécifiques à l'en-tête et aux lignes de données.
seo-description: Répertorie les macros que vous pouvez utiliser pour créer des fichiers de données FTP. Certaines macros peuvent être utilisées pour tous les champs et lignes de fichier de données. D'autres macros sont spécifiques à l'en-tête et aux lignes de données.
seo-title: Macros de format de fichier
title: Macros de format de fichier
uuid: f 91 c 91 b 6-6581-4 ed 7-8 d 7 f-f 8532 bd 41 df 9
translation-type: tm+mt
source-git-commit: e1122a7f3d3e8c2d67616eb56cb186a4750ed29b

---


# Macros de format de fichier {#file-format-macros}

Répertorie les macros que vous pouvez utiliser pour créer [!DNL FTP]des fichiers de données basés sur la création. Certaines macros peuvent être utilisées pour tous les champs et lignes de fichier de données. D'autres macros sont spécifiques à l'en-tête et aux lignes de données.

## Macros courantes {#common-macros}

Ces macros peuvent être utilisées dans n'importe quel champ de format. Pour obtenir des exemples, reportez-vous à [la section Format de fichier Exemples de macro](../formats/file-format-examples.md).

<table id="table_A3309E175ABF4651BD11CE3632B3C553"> 
 <thead> 
  <tr> 
   <th colname="col1" class="entry"> Macro </th> 
   <th colname="col2" class="entry"> Description </th> 
  </tr> 
 </thead>
 <tbody> 
  <tr> 
   <td colname="col1"> <p> <code>ASCII_ SOH</code> </p> </td> 
   <td colname="col2"> <p>Caractère ASCII non imprimable. Il indique le début d'une ligne ou d'une section de contenu. Il peut également être utilisé pour séparer les colonnes de données d'un fichier. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>DPID</code> </p> </td> 
   <td colname="col2"> <p>Identifiant de fournisseur de données Target. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>MASTER_ DPID</code> </p> </td> 
   <td colname="col2"> <p>User - ID de fournisseur de données de clé d'ID. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>ORDER_ ID</code> </p> </td> 
   <td colname="col2"> <p>ID de commande/de destination. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>PIDALIAS</code> </p> </td> 
   <td colname="col2"> <p>Un alias pour un ID de commande/de destination. </p> <p>La valeur de cet alias est définie dans <span class="wintitle"> le champ ID </span> du compte étranger pour une destination (dans la section Paramètres <span class="wintitle"></span> de base). </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>SYNC_ MODE</code> </p> </td> 
   <td colname="col2"> <p>Indique le type de synchronisation. Accepte les variables facultatives suivantes : </p> 
    <ul id="ul_87E8E3CE6565447A9810B5119298CC7B"> 
     <li id="li_66F4889FB84E40AC92F69F3FF6B0042C"> <code>full</code>: Synchronisation complète. </li> 
     <li id="li_BFE2C2D9A33A44FB9A840A7232ECCFFF"> <code>iter</code>: Synchronisation incrémentielle. </li> 
    </ul> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>SYNC_ TYPE</code> </p> </td> 
   <td colname="col2"> <p>Indique la méthode de transfert de données. Accepte les variables facultatives suivantes : </p> 
    <ul id="ul_13BE35BBBF7C4C67AEFC514C5D192902"> 
     <li id="li_195FE9B4C5494600BD17D7172A8FB630"> <code>ftp</code> </li> 
     <li id="li_751AD59C4C934D66BC530D9806B500AF"> <code>http</code> </li> 
     <li id="li_4638AF7D1FB54E2C890045048B85309C"> <code>s3</code> </li> 
    </ul> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>TIMESTAMP</code> </p> </td> 
   <td colname="col2"> <p>Un horodatage de 10 chiffres, UTC, Unix. </p> <p>Il peut également être formaté en tant <code>que aaaammddhhmmss</code> après les règles de formatage de date Java/timestamp. </p> </td> 
  </tr> 
 </tbody> 
</table>

## Macros de champs d'en-tête {#header-field-macros}

Macros utilisées uniquement dans les champs d'en-tête. Pour obtenir des exemples, reportez-vous à [la section Format de fichier Exemples de macro](../formats/file-format-examples.md).

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
   <td colname="col2"> <p>Utilisé comme séparateur, cette macro insère un onglet entre les champs. </p> </td> 
  </tr> 
 </tbody> 
</table>

## Macros de ligne de données {#data-row-macros}

Macros utilisées dans les lignes de données uniquement. Pour obtenir des exemples, reportez-vous à [la section Format de fichier Exemples de macro](../formats/file-format-examples.md).

<table id="table_E378F94A3907407AA8110C8EE6C10909"> 
 <thead> 
  <tr> 
   <th colname="col1" class="entry"> Macro </th> 
   <th colname="col2" class="entry"> Description </th> 
  </tr> 
 </thead>
 <tbody> 
  <tr> 
   <td colname="col1"> <p> <code>CLOSE_ CURLY_ BRACKET</code> </p> </td> 
   <td colname="col2"> <p>Insère un caractère de crochet fermé}. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>VIRGULE</code> </p> </td> 
   <td colname="col2"> <p>Insère une virgule. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>DP_ UUID</code> </p> </td> 
   <td colname="col2"> <p> <span class="term"> Identifiant utilisateur unique du partenaire de données </span>. Renvoie l'ID que vous avez attribué à un utilisateur/visiteur du site si cet identifiant a déjà été synchronisé avec un <span class="keyword"> ID </span> de périphérique Audience Manager. </p> <p>Si le DPID est 0, cette macro renvoie l'identifiant <span class="keyword"> Audience Manager </span> au lieu de votre ID pour l'utilisateur. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>DP_ UUID_ LIST</code> </p> </td> 
   <td colname="col2"> <p>Renvoie une liste contenant plusieurs ID pour un partenaire de données. Cela s'avère utile si vous disposez d'une grande organisation comptant plusieurs sous-divisions ou d'autres groupes d'organisations auxquels vous êtes autorisé à partager des données. Cette macro renvoie la liste des identifiants de ces groupes subordonnés. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>DPUUIDS</code> </p> </td> 
   <td colname="col2"> <p>La sortie de cette macro associe l'identifiant du fournisseur de données (DPID) à l'utilisateur unique associé - id (DPUUID). Cette macro doit disposer d'une chaîne de formatage pour contrôler sa sortie. L'exemple de sortie ressemble à ce qui suit : </p> <p> <code>« dpids = dpid 1, dpid 2,… dpid n | maxmappings = n | format = json »</code> </p> <p>Le paramètre <code>maxmappings</code> détermine le nombre de mappages que la macro doit renvoyer. Lorsque <code>maxmappings = 0</code>, cette macro renvoie toutes les correspondances pour chaque DPID spécifié. Les données sont triées par horodatage (le plus récent d'abord) et renvoie d'abord les résultats avec le plus grand horodatage. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>endif</code> </p> </td> 
   <td colname="col2"> <p>Obligatoire lors de l'utilisation de la condition conditionnelle <code>if</code> et <code>les macros SEGMENT_ LIST</code> et <code>REMOVED_ SEGMENT_ LIST</code> . </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>if (SEGMENT_ LIST &amp; &amp; REMOVED_ SEGMENT_ LIST) endif</code> </p> </td> 
   <td colname="col2"> <p>Cette combinaison de macros crée une instruction conditionnelle qui répertorie les segments auxquels les utilisateurs appartiennent <i>et</i> qui ont été supprimés. Elle renvoie une chaîne vide si les deux conditions ne sont pas remplies ou qu'il n'y a aucune donnée. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>MCID</code> </p> </td> 
   <td colname="col2"> <p> <span class="keyword"> Adobe Experience Cloud </span> ID. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>OPEN_ CURLY_ BRACKET</code> </p> </td> 
   <td colname="col2"> <p>Insère une accolade {caractère. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>OPT_ OUT</code> </p> </td> 
   <td colname="col2"> <p>Obsolète. N'utilisez pas. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>OUTPUT_ ATTRIBUTE_ TYPE</code> </p> </td> 
   <td colname="col2"> <p>Obsolète. N'utilisez pas. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>OUTPUT_ ATTRIBUTE_ VALUE</code> </p> </td> 
   <td colname="col2"> <p>Renvoie <code>1</code> comme valeur figée et figée dans le code. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>PID</code> </p> </td> 
   <td colname="col2"> <p>ID de partenaire. Le paramètre PID apparaît sous l'onglet <span class="wintitle"> Profil </span> de l'interface utilisateur d'administration. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>REMOVED_ SEGMENT_ LIST</code> </p> </td> 
   <td colname="col2"> <p>Renvoie une liste de segments, le cas échéant, supprimés. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>SEGMENT_ LIST</code> </p> </td> 
   <td colname="col2"> <p>Renvoie une liste de segments dans une liste. Accepte les variables facultatives suivantes : </p> 
    <ul id="ul_B111AA0D6C18445598A1444B8B7E9325"> 
     <li id="li_8603B40229624856AF1FBC434DB8F16A"> <code>Segmentid</code>: ID hérité. Obsolète. Utilisez <code>sid</code> (minuscule uniquement). </li> 
     <li id="li_1EF40DDCA3C5447586904CF021D8F912"> <code>csegid</code>: ID hérité. Obsolète. Utilisez <code>sid</code> (minuscule uniquement). </li> 
     <li id="li_D85F0A5D16AE4DAFB55C17DBB35EA66E"> <code>sid</code>: Identifiant du segment. </li> 
     <li id="li_9BE103EFD8384464B46FAC00422431DB"> <code>type</code>: Renvoie <code>5</code>, valeur figée et figée dans le code qui identifie les données comme données de segment. </li> 
     <li id="li_FE5049089F2944FA9DB9F9D546DBA167"> <code>alias</code>: Mappage du segment. Obsolète. Utilisez <code>sid</code> (minuscule uniquement). </li> 
     <li id="li_DD778AA2D1DB4D409CF5026B5D9DBD27"> <code>Lastupdatetime</code>: Horodatage Unix qui indique la dernière fois qu'un segment a été réalisé. </li> 
    </ul> <p>Placez ces variables entre accolades après la macro. Par exemple, ce code sépare les résultats par une barre verticale|caractère : <code>&lt; SEGMENT_ LIST : {seg|&lt; seg. type &gt;, &lt; seg. sid &gt;} ; separator = "|" &gt;</code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>SET_ ATTRIBUTES</code> </p> </td> 
   <td colname="col2"> <p>Renvoie <code>1</code> comme valeur figée et figée dans le code. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>TAB</code> </p> </td> 
   <td colname="col2"> <p>Insère un séparateur d'onglet. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>TRAIT_ LIST</code> </p> </td> 
   <td colname="col2"> <p>Renvoie une liste de caractéristiques. Accepte les arguments facultatifs suivants : </p> 
    <ul id="ul_757DEB56E4F849768468F3C166B0D171"> 
     <li id="li_859E1F4F21D645519F150DC512B3EB1A"> <code>type</code>: Types de caractéristiques identifiés par un ID numérique. Cette variable renvoie : 
      <ul id="ul_C9839266783D42CCADAAC3FEA33BE4D7"> 
       <li id="li_6996A218E3F04EC3BC70032559DD87FC"> <code>10</code> qui identifie une caractéristique DPM (hors ligne, intégrée à une tâche inentrante). </li> 
       <li id="li_831FF929BF50434C8804C13E5786DF79"> <code>3</code> qui identifie une caractéristique basée sur des règles (temps réel ; intégrée via le serveur de collecte de <span class="wintitle"> données </span>). </li> 
      </ul> </li> 
     <li id="li_E84D6BC80AEE4F10963C9882C4151ED4"> <code>Traitid</code>: Identifiant de caractéristique. </li> 
     <li id="li_D30A849BA35248E6B9110FA3ADEFC332"> <code>Lastrealized</code>: Dernière fois que la caractéristique a été réalisée. Horodatage Unix. </li> 
    </ul> <p>Placez ces variables entre accolades après la macro. Par exemple, ce code sépare les résultats par une barre verticale|caractère : <code>TRAIT_ LIST {type | traitid} ; separator = "|"</code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>UUID</code> </p> </td> 
   <td colname="col2"> <p> <span class="keyword"> Utilisateur Audience Manager </span> - id. </p> </td> 
  </tr> 
 </tbody> 
</table>