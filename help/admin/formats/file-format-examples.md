---
description: Exemples d'utilisation de macros pour créer des modèles de fichiers sortants et sortants.
seo-description: Exemples d'utilisation de macros pour créer des modèles de fichiers sortants et sortants.
seo-title: Exemples de macros de format de fichier
title: Exemples de macros de format de fichier
uuid: f 00 d 431 d -7 e 43-457 a-b 633-c 79 cbc 4 c 8 f 10
translation-type: tm+mt
source-git-commit: 4c6d1752ff10d2d3d12cab88e823f25f5ef4fcd0

---


# Exemples de macros de format de fichier {#file-format-macro-examples}

Exemples d'utilisation de macros pour créer des modèles de [!DNL FTP] fichiers sortants et sortants.

>[!NOTE]
>
>Dans les tableaux, **le type gras** identifie chaque macro avec sa sortie associée. Pour les exemples de format, les symboles &lt; &gt; ont été ajoutés pour permettre de séparer visuellement chaque macro.

## Macros courantes {#common-macros}

Ces macros peuvent être utilisées dans n'importe quel champ de format. Voir les macros Format [de fichier](../formats/file-formats.md) pour obtenir une liste complète et des définitions.

<table id="table_B5073597219B470298EE614902DACAE8"> 
 <thead> 
  <tr> 
   <th colname="col1" class="entry"> Macro </th> 
   <th colname="col2" class="entry"> Formats et exemples de sortie </th> 
  </tr> 
 </thead>
 <tbody> 
  <tr> 
   <td colname="col1"> <p> <code>DPID </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt; SYNC_ TYPE &gt;_ &lt; ORDER_ ID &gt;_ &lt; DPID &gt;_ &lt; SYNCHRO_ MODE &gt;_ &lt; TIMESTAMP &gt;. sync </code> </p> <p>Output : <code>ftp_ 215_ 888_ iter_ 1449756724. sync </code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>MASTER_ DPID </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt; SYNC_ TYPE &gt;_ &lt; ORDER_ ID &gt;_ &lt; DPID &gt;_ &lt; MASTER_ DPID &gt;_ &lt; SYNC_ MODE &gt;_ &lt; TIMESTAMP &gt;. sync </code> </p> <p>Output : <code>ftp_ 215_ 888_ 20915_ iter_ 1449756724. sync </code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>ORDER_ ID </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt; SYNC_ TYPE &gt;_ &lt; ORDER_ ID &gt;_ &lt; DPID &gt;_ &lt; SYNCHRO_ MODE &gt;_ &lt; TIMESTAMP &gt;. sync </code> </p> <p>Output : <code>ftp_ 215_ 888_ iter_ 1449756724. sync </code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>SYNC_ MODE </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt; SYNC_ TYPE &gt;_ &lt; ORDER_ ID &gt;_ &lt; DPID &gt;_ &lt; SYNCHRO_ MODE &gt;_ &lt; TIMESTAMP &gt;. sync </code> </p> <p>Output : 
     <ul id="ul_F63D7B78AF1246639D6ED85C1621B17C"> 
      <li id="li_4D0D7B4D047345FE861FCBA2BD0408ED">Complet : <code>ftp_ 215_ 888_ full_ 1449756724. sync </code> </li> 
      <li id="li_23F4D1F6B2784E599EDA29AA457327E6">Incrémentiel : <code>ftp_ 215_ 888_ iter_ 1449756724. sync </code> </li> 
     </ul> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>SYNC_ TYPE </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt; SYNC_ TYPE &gt;_ &lt; ORDER_ ID &gt;_ &lt; DPID &gt;_ &lt; SYNCHRO_ MODE &gt;_ &lt; TIMESTAMP &gt;. sync </code> </p> <p>Output : 
     <ul id="ul_11B14E740E40474F8302BDB809C428FE"> 
      <li id="li_54A3EAA468B44AC8B2528F855E03D04B">FTP : <code>ftp_ 215_ 888_ iter_ 1449756724. sync </code> </li> 
      <li id="li_93468C56B661463CA7F62B1F5D3A53FF">https : <code>http_ 215_ 888_ iter_ 1449756724. sync </code> </li> 
      <li id="li_8A204C7BEDBC41C096FE953B5F827DEC">S 3 : <code>s 3_ 215_ 888_ iter_ 1449756724. sync </code> </li> 
     </ul> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>TIMESTAMP </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt; SYNC_ TYPE &gt;_ &lt; ORDER_ ID &gt;_ &lt; DPID &gt;_ &lt; SYNCHRO_ MODE &gt;_ &lt; TIMESTAMP &gt;. sync </code> </p> <p>Output : <code>ftp_ 215_ 888_ iter_ 1449756724. sync </code> </p> </td> 
  </tr> 
 </tbody> 
</table>

## Macros de champs d'en-tête {#header-field-macros}

Macros utilisées uniquement dans les champs d'en-tête. Voir les macros Format [de fichier](../formats/file-formats.md) pour obtenir une liste complète et des définitions.

<table id="table_ABC31B3D660D47969E111EBC734D5BBC"> 
 <thead> 
  <tr> 
   <th colname="col1" class="entry"> Macro </th> 
   <th colname="col2" class="entry"> Formats et exemples de sortie </th> 
  </tr> 
 </thead>
 <tbody> 
  <tr> 
   <td colname="col1"> <p> <code>TAB </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt; ORDER_ ID &gt; &lt; TAB &gt; &lt; SYNC_ TYPE &gt; </code> </p> <p>Output : <code>888 full. sync </code> </p> <p>Dans la sortie, le caractère de tabulation non imprimable sépare chaque élément. </p> </td>
  </tr>
 </tbody>
</table>

## Macros de ligne de données {#data-row-macros}

Macros utilisées uniquement dans les champs d'en-tête. Voir les macros Format [de fichier](../formats/file-formats.md) pour obtenir une liste complète et des définitions.

<table id="table_408C6DD2B9D54550B003EAC93562E64F"> 
 <thead> 
  <tr> 
   <th colname="col1" class="entry"> Macro </th> 
   <th colname="col2" class="entry"> Formats et exemples de sortie </th> 
  </tr> 
 </thead>
 <tbody> 
  <tr> 
   <td colname="col1"> <p> <code>DP_ UUID </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt; DP_ UUID &gt; &lt; TAB &gt; &lt; DP_ UUID_ LIST ; separator = TAB &gt; </code> </p> <p>Output : <code>123456 UUID 1 UUID 2 UUID 3 </code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>DP_ UUID_ LIST </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt; DP_ UUID &gt; &lt; TAB &gt; &lt; DP_ UUID_ LIST ; separator = TAB &gt; </code> </p> <p>Output : <code>123456 UUID 1 UUID 2 UUID 3 </code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>SEGMENT_ LIST &amp; &amp; REMOVED_ SEGMENT_ LIST </code> </p> </td> 
   <td colname="col2"> <p>Cet exemple crée un format qui renvoie les segments supprimés dans un flux serveur à serveur. </p> <p> 
     <code>{« Advertiserid » : « &lt; PIDALIAS &gt; », « datacenterid » : 2, « TDID » : « &lt; DP_ UUID &gt; », 
 « Données » : [&lt; SEGMENT_ LIST : {seg|&lt; OPEN_ CURLY_ BRACKET &gt; « Name » : " &lt; seg. alias &gt; " &lt; CLOSE_ CURLY_ BRACKET &gt;} ; 
 separator = », " &gt; &lt; if (SEGMENT_ LIST &amp; &amp; REMOVED_ SEGMENT_ LIST) &gt; &lt; COMMA &gt; &lt; endif &gt; 
 &lt; REMOVED_ SEGMENT_ LIST : {seg|&lt; OPEN_ CURLY_ BRACKET &gt; « Name » : « &lt; seg. alias &gt; », 
 « Ttlinminutes » : 0 &lt; CLOSE_ CURLY_ BRACKET &gt;} ; separator = », " &gt;]} </code>
  </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>SEGMENT_ LIST </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt; DP_ UUID &gt; &lt; SEGMENT_ LIST &gt; ; separator = » « &gt; </code> </p> <p>Output : <code>123456 105955 101183 101180 101179 </code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>SET_ ATTRIBUTES </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt; PID &gt; &lt; TAB &gt; &lt; UUID &gt; &lt; TAB &gt; &lt; DP_ UUID &gt; &lt; TAB &gt; &lt; SET_ ATTRIBUTES &gt; &lt; TAB &gt; &lt; OPT_ OUT &gt; &lt; TAB &gt; &lt; SEGMENT_ LIST : {seg|&lt; seg. type &gt;, &lt; seg. alias &gt;, &lt; OUTPUT_ ATTRIBUTE_ VALUE &gt;, &lt; seg. lastupdatetime &gt; &amp;} &gt; </code> </p> <p>Output : <code>1159 00088008579683653741516297509717335000 17 t 0 aj 01 b 120 hp 1 0 5,103714,1,1344114661000 &amp; 5,103713,1,1343250661000 </code> </p> </td>
  </tr>
  <tr> 
   <td colname="col1"> <p> <code>TAB </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt; DP_ UUID &gt; &lt; TAB &gt; &lt; DP_ UUID_ LIST ; separator = TAB &gt; </code> </p> <p>Output : <code>123456 UUID 1 UUID 2 UUID 3 </code> </p> <p>Dans la sortie, le caractère de tabulation non imprimable sépare chaque élément. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>TRAIT_ LIST </code> </p> </td> 
   <td colname="col2"> <p>Format : <code>&lt; PID &gt; &lt; TAB &gt; &lt; DP_ UUID &gt; &lt; TAB &gt; &lt; SET_ ATTRIBUTES &gt; &lt; TAB &gt; &lt; CARACTÉRISTIQUE_ LIST ; separator = « | » &gt; </code> </p> <p>Output : <code>1131 12345 1 123|456|789 </code> </p> </td> 
  </tr> 
 </tbody> 
</table>
