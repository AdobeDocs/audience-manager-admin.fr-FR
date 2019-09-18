---
description: Exemples d’utilisation des macros pour créer des modèles de fichiers FTP sortants.
seo-description: Exemples d’utilisation des macros pour créer des modèles de fichiers FTP sortants.
seo-title: Exemples de macro de format de fichier
title: Exemples de macro de format de fichier
uuid: f00d431d-7e43-457a-b633-c79cbc4c8f10
translation-type: tm+mt
source-git-commit: 4c6d1752ff10d2d3d12cab88e823f25f5ef4fcd0

---


# Exemples de macro de format de fichier {#file-format-macro-examples}

Exemples d’utilisation des macros pour créer des modèles de fichiers sortants [!DNL FTP] .

>[!NOTE]
>
>Dans les tableaux, le type **boldface** identifie chaque macro avec sa sortie associée. Pour les exemples de format, les symboles &lt; &gt; ont été ajoutés afin de séparer visuellement chaque macro.

## Macros courantes {#common-macros}

Ces macros peuvent être utilisées dans n’importe quel champ de format. Pour obtenir la liste complète et les définitions, reportez-vous aux macros [au format de](../formats/file-formats.md) fichier.

<table id="table_B5073597219B470298EE614902DACAE8"> 
 <thead> 
  <tr> 
   <th colname="col1" class="entry"> Macro </th> 
   <th colname="col2" class="entry"> Exemples de format et de sortie </th> 
  </tr> 
 </thead>
 <tbody> 
  <tr> 
   <td colname="col1"> <p> <code>DPID </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt;TYPE_SYNC&gt;_&lt;ID_ORDRE&gt;_ &lt;ID_DPID&gt;_&lt;MODE_SYNC&gt;_&lt;FICHIER&gt;.sync </code> </p> <p>Output : <code>ftp_215_ 888_iter_1449756724.sync </code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>MASTER_DPID </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt;TYPE_SYNC&gt;_&lt;ID_ORDRE&gt;_&lt;ID_DPID&gt;_ &lt;ID_MASTER&gt;_&lt;MODE_SYNC&gt;_&lt;MODE_SYNCHRONISTE&gt;_&lt;FICHIER&gt;.sync </code> </p> <p>Output : <code>ftp_215_888_ 20915_iter_1449756724.sync </code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>ORDER_ID </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt;TYPE_SYNC&gt;_ &lt;ID_ORDRE&gt;_&lt;ID_DPID&gt;_&lt;MODE_SYNC&gt;_&lt;FICHIER_TIMESTAMP&gt;.sync </code> </p> <p>Output : <code>ftp_ 215_888_iter_1449756724.sync </code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>SYNC_MODE </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt;TYPE_SYNC&gt;_&lt;ID_ORDRE&gt;_&lt;ID_DPID&gt;_ &lt;MODE_SYNC&gt;_&lt;FICHIER_CALCUL&gt;.sync </code> </p> <p>Output : 
     <ul id="ul_F63D7B78AF1246639D6ED85C1621B17C"> 
      <li id="li_4D0D7B4D047345FE861FCBA2BD0408ED">Complet : <code>ftp_215_888_full_1449756724.sync </code> </li> 
      <li id="li_23F4D1F6B2784E599EDA29AA457327E6">Incrémentiel : <code>ftp_215_888_ iter_1449756724.sync </code> </li> 
     </ul> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>SYNC_TYPE </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt;TYPE_SYNC&gt;_&lt;ID_ORDRE&gt;_&lt;ID_DPID&gt;_&lt;MODE_SYNC&gt;_&lt;FICHIER_TIMESTAMP&gt;.sync </code> </p> <p>Output : 
     <ul id="ul_11B14E740E40474F8302BDB809C428FE"> 
      <li id="li_54A3EAA468B44AC8B2528F855E03D04B">FTP : <code>ftp_215_888_iter_1449756724.sync </code> </li> 
      <li id="li_93468C56B661463CA7F62B1F5D3A53FF">https: <code>http_215_888_iter_1449756724.sync </code> </li> 
      <li id="li_8A204C7BEDBC41C096FE953B5F827DEC">S3 : <code>s3_215_888_iter_1449756724.sync </code> </li> 
     </ul> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>TIMESTAMP </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt;TYPE_SYNC&gt;_&lt;ID_ORDRE&gt;_&lt;ID_DPID&gt;_&lt;MODE_SYNC&gt;_ &lt;FICHIER_CALCUL&gt;_&lt;FICHIER&gt;.sync </code> </p> <p>Output : <code>ftp_215_888_iter_ 1449756724.sync </code> </p> </td> 
  </tr> 
 </tbody> 
</table>

## Macros Champ d’en-tête {#header-field-macros}

Macros utilisées uniquement dans les champs d’en-tête. Pour obtenir la liste complète et les définitions, reportez-vous aux macros [au format de](../formats/file-formats.md) fichier.

<table id="table_ABC31B3D660D47969E111EBC734D5BBC"> 
 <thead> 
  <tr> 
   <th colname="col1" class="entry"> Macro </th> 
   <th colname="col2" class="entry"> Exemples de format et de sortie </th> 
  </tr> 
 </thead>
 <tbody> 
  <tr> 
   <td colname="col1"> <p> <code>TABULATION </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt;ID_ORDER&gt; &lt;TAB&gt;&lt;TYPE_SYNC&gt; </code> </p> <p>Output : <code>888 full.sync </code> </p> <p>Dans la sortie, le caractère de tabulation non imprimable sépare chaque élément. </p> </td>
  </tr>
 </tbody>
</table>

## Macros de ligne de données {#data-row-macros}

Macros utilisées uniquement dans les champs d’en-tête. Pour obtenir la liste complète et les définitions, reportez-vous aux macros [au format de](../formats/file-formats.md) fichier.

<table id="table_408C6DD2B9D54550B003EAC93562E64F"> 
 <thead> 
  <tr> 
   <th colname="col1" class="entry"> Macro </th> 
   <th colname="col2" class="entry"> Exemples de format et de sortie </th> 
  </tr> 
 </thead>
 <tbody> 
  <tr> 
   <td colname="col1"> <p> <code>DP_UUID </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt;DP_UUID&gt;&lt;TAB&gt;&lt;DP_UUID_LIST;separator=TAB&gt; </code> </p> <p>Output : <code>123456 UUID1 UUID2 UUID3 </code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>DP_UUID_LIST </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt;DP_UUID&gt;&lt;TAB&gt; &lt;DP_UUID_LIST;separator=TAB&gt; </code> </p> <p>Output : <code>123456 UUID1 UUID2 UUID3 </code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>SEGMENT_LIST &amp;&amp; REMOVED_SEGMENT_LIST </code> </p> </td> 
   <td colname="col2"> <p>Cet exemple crée un format qui renvoie les segments supprimés dans un flux serveur à serveur. </p> <p> 
     <code>
       {"AdvertiserId":"&lt;PIDALIAS&gt;", "DataCenterId": 2,"TDID":"&lt;DP_UUID&gt;", "Data":[&lt;SEGMENT_LIST:{seg|&lt;OPEN_CURLY_BRACKET&gt;"Name":"&lt;seg.alias&gt;"&lt;CLOSE_CURLY_BRACKET&gt;; 
      separator=","&gt;&lt;if(SEGMENT_LIST &amp;&amp; REMOVED_SEGMENT_LIST)&gt;&lt;COMMA&gt;&lt;endif&gt; &lt;REMOVED_SEGMENT_LIST:{seg|&lt;OPEN_CURLY_BRACKET&gt;"Name":"&lt;seg.alias&gt;", "TtlInMinutes":0&lt;CLOSE_CURator LY_BRACKET&gt;}; separator=","&gt;]} </code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>SEGMENT_LIST </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt;DP_UUID&gt; &lt;SEGMENT_LIST&gt;;separator=" "&gt; </code> </p> <p>Output : <code>123456 105955 101183 101180 101179 </code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>SET_ATTRIBUTES </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt;PID&gt;&lt;TAB&gt;&lt;UUID&gt;&lt;TAB&gt;&lt;DP_UUID&gt;&lt;TAB&gt; &lt;SET_ATTRIBUTES&gt;&lt;TAB&gt;&lt;OPT_OUT&gt;&lt;TAB&gt;&lt;SEGMENT_LIST:{seg|&lt;seg.type&gt;,&lt;seg.alias&gt;,&lt;OUTPUT_ATTRIBUTE_VALUE&gt;&lt;seg.lastVALUE&gt; Heure&gt;&amp;}&gt; </code> </p> <p>Output : <code>1159 0008800857968365374151629750971735000 17t0aj01b11 1 0 5 103 714 1 134 41 146 1000&amp;5 103 713 134 325061 000 </code> </p> </td>
  </tr>
  <tr> 
   <td colname="col1"> <p> <code>TABULATION </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt;DP_UUID&gt;&lt;TAB&gt;&lt;DP_UUID_LIST;separator=TAB&gt; </code> </p> <p>Output : <code>123456 UUID1 UUID2 UUID3 </code> </p> <p>Dans la sortie, le caractère de tabulation non imprimable sépare chaque élément. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>TRAIT_LIST </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt;PID&gt;&lt;TAB&gt;&lt;DP_UUID&gt;&lt;TAB&gt;&lt;SET_ATTRIBUTES&gt;&lt;TAB&gt; &lt;TRAIT_LIST;separator="|"&gt; </code> </p> <p>Output : <code>1131 12345 1 123|456|789 </code> </p> </td> 
  </tr> 
 </tbody> 
</table>
