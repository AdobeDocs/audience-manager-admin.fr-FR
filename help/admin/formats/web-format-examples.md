---
description: Exemples de combinaisons de macro HTTP couramment utilisées.
seo-description: Exemples de combinaisons de macro HTTP couramment utilisées.
seo-title: ' Exemples de macro au format HTTP'
title: ' Exemples de macro au format HTTP'
uuid: a81a2e2a-de7e-4b6a-8771-fcfa0dc74570
translation-type: tm+mt
source-git-commit: 4c6d1752ff10d2d3d12cab88e823f25f5ef4fcd0

---


# Exemples de macro au format HTTP {#http-format-macro-examples}

Exemples de combinaisons [!DNL HTTP] de macro couramment utilisées.

Pour obtenir la liste des macros et de leurs définitions, reportez-vous aux macros [au format](../formats/web-formats.md) HTTP.

<table id="table_D5FAC5D056ED49D79FA883197EF8F42E"> 
 <thead> 
  <tr> 
   <th colname="col1" class="entry"> Exemples de macro </th> 
   <th colname="col2" class="entry"> Format de sortie </th> 
  </tr> 
 </thead>
 <tbody> 
  <tr> 
   <td colname="col1"> <p> <code>&lt;PID_ALIAS&gt;|&lt;DP_UUID&gt;|&lt;TRAITALIAS_LIST; separator=","&gt;</code> </p> </td> 
   <td colname="col2"> <p> <code>pid_alias|dp_uid|trait_1,trait_2</code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>&lt;PID_ALIAS&gt;|count:&lt;NUM_USERS&gt;|users:[&lt;USER_LIST:{user|&lt;user.aamUuid&gt;:&lt;user.dpUuid&gt;}; separator=", "&gt;]</code> </p> </td> 
   <td colname="col2"> <p> <code>"pid_alias|count:2|users:[uuid1:dpuuid1, uuuid2:dpuuid2]"</code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>&lt;USER_AGENT&gt;|&lt;IP&gt;|&lt;TIMESTAMP&gt;|&lt;RANDOM&gt;</code> </p> </td> 
   <td colname="col2"> <p> <code>"Firefox|255.255.255.255|1395758143|42341"</code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>&lt;USER_LIST:{u|&lt;u.userAgent&gt;|&lt;u.ip&gt;|&lt;u.timestamp&gt;|&lt;u.random&gt;}; separator=", "&gt;</code> </p> </td> 
   <td colname="col2"> <p> <code>"Firefox|255.255.255.255|1395758143|42341"</code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>&lt;DP_UUIDS.1&gt; ET &lt;DP_UUIDS.2&gt;</code> </p> </td> 
   <td colname="col2"> <p> <code>dpuuid1 ET dpuuid2</code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>utilisateurs :[&lt;USER_LIST:{user|&lt;user.dpUuids.1&gt; AND &lt;user.dpUuids.2&gt;}; separator=", "&gt;]</code> </p> </td> 
   <td colname="col2"> <p> <code>utilisateurs :[dpuuid1 ET dpuuid2]</code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>test_known_string=loremlipsum&amp;segid=&lt;TRAITALIAS_LIST; separator=","&gt;&amp;test_dpuuid_1000=&lt;DP_UIDS.1000&gt;</code> </p> </td> 
   <td colname="col2"> <p> <code>test_known_string=loremlipsum&amp;segid=trait_1,trait_2&amp;test_dpuuid_1000=dpuuid_1000</code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>test_dpuuids=&lt;DP_UUIDS.(DPID)&gt;</code> </p> </td> 
   <td colname="col2"> <p> <code>test_dpuuids=dpuuid2</code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>"&lt;PID_ALIAS&gt;|&lt;DP_UUID&gt;|&lt;TRAITALIAS_LIST; separator=","&gt;|&lt;REMOVED_TRAITALIAS_LIST; separator=","&gt;</code> </p> </td> 
   <td colname="col2"> <p> <code>pid_alias|dp_uuid|trait_1,trait_2|trait_3,trait_4</code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> 
     <code>
       {"Utilisateurs": [&lt;USER_LIST:{user|&lt;OPEN_BRACKET&gt; "AAM_UUID": "&lt;user.aamUuid&gt;", "DataPartner_UUID": "&lt;user.dpUuid&gt;", "Segments": [&lt;user.segments:{seg|&lt;OPEN_BRACKET&gt;"Segment": &lt;seg.traitAlias&gt;"&lt;CLOSE_BRACKET&gt;}; separator=","&gt;] "Supprimé_Segments": [&lt;user.removeSegments:{rseg|&lt;OPEN_BRACKET&gt;"Segment": "&lt;rseg.traitAlias&gt;"&lt;CLOSE_BRACKET&gt;}; separator=","&gt; BRACKET&gt;}; separator=","&gt;]} </code> </p> </td> 
   <td colname="col2"> <p> 
     <code>
       { "Utilisateurs":[ { "AAM_UUID":"uuid1", "DataPartner_UUID":"dpuuid1", "Segments":[ { "Segment":"alias1" }, { "Segment":"alias2" } ], "Segments_supprimés":[ "Segment":"alias3" }, { "Segment": alias4" } ] } ] } </code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> 
     <code>
       {"Utilisateurs": [&lt;USER_LIST:{user|&lt;OPEN_BRACKET&gt; "AAM_UUID": "&lt;user.aamUuid&gt;", "DataPartner_UUID": "&lt;user.dpUuid&gt;", "Segments": [&lt;user.segments:{seg|&lt;OPEN_BRACKET&gt;"Segment":&lt;seg.traitAlias&gt;","Status": "&lt;seg.status&gt;"&lt;CLOSE_BRACKET&gt;}; separator=","&gt;] &lt;CLOSE_BRACKET&gt;}; separator=","&gt;]} </code> </p> </td> 
   <td colname="col2"> <p> 
     <code>
       { "Utilisateurs":[ { "AAM_UUID":"uuid1", "DataPartner_UUID":"dpuuid1", "Segments":[ { "Segment":"alias1" "État":"1" }, { "Segment":"alias2" "État":"0" } ] } ] </code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>&lt;PID_ALIAS&gt;|&lt;DP_UUID&gt;|&lt;SEGMENTS:{seg|&lt;seg.traitAlias&gt;}; separator=\",\"&gt;|&lt;REMOVED_SEGMENTS:{seg|&lt;seg.traitAlias&gt;}; separator=\",\"&gt;</code> </p> </td> 
   <td colname="col2"> <p> <code>pid_alias|dp_uuid|trait_1,trait_2|trait_3,trait_4</code> </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <code>&lt;if(user.segments &amp;&amp; user.removeSegments)&gt;&lt;COMMA&gt;&lt;endif&gt;</code> </p> </td> 
   <td colname="col2"> <p>Imprime une virgule si les <code>segments</code> des champs et les segments <code>supprimés</code> ne sont pas vides. Cette condition peut être utilisée pour les requêtes POST lors de la concaténation de listes pour les segments et les segments supprimés. </p> </td> 
  </tr> 
 </tbody> 
</table>
