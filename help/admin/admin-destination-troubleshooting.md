---
description: Informations destinées à vous aider à configurer des destinations en Audience Manager et à éviter les problèmes courants.
seo-description: Informations destinées à vous aider à configurer des destinations en Audience Manager et à éviter les problèmes courants.
seo-title: Dépannage des configurations de destination
title: Dépannage des configurations de destination
uuid: 04080fb9-6c7b-4de7-960e-54482be2de83
translation-type: tm+mt
source-git-commit: 118e8fa3f35bc77846c6518268448d57d779a2ee
workflow-type: tm+mt
source-wordcount: '1331'
ht-degree: 4%

---


# Dépannage des configurations de destination {#destination-setup-troubleshooting}

Informations destinées à vous aider à configurer des destinations en Audience Manager et à éviter les problèmes courants.

## J&#39;ai installé une destination, mais je ne vois aucun fichier. Où se trouvent-ils ?{#destination-no-files}

<!-- c_dest_tshooting.xml -->

Les problèmes courants de configuration de destination sont les suivants :

### Destination mal configurée

* **Clé[!UICONTROL UserID]incorrecte :** La [!UICONTROL UserID] clé est la [!UICONTROL MasterDPID] clé de cette destination et est la base des valeurs d’ID qui seront délimitées. Même si une [!UICONTROL UserID] clé peut être sélectionnée par le biais de la liste déroulante, cela ne signifie pas nécessairement qu’il existe des identifiants/caractéristiques/segments associés à cette valeur. Si le [!UICONTROL Outbound] processus (qui s’exécute après la création des destinations) ne trouve aucun utilisateur associé à cette [!UICONTROL UserID] clé, aucune donnée n’est délimitée.
* **Aucune source de données dans le fichier sélectionnée :** Lors du choix d’un type de destination autre que [!UICONTROL S2S]le type de destination, une section s’affiche au bas de l’écran, intitulée [!UICONTROL Configure Data Sources]. Lorsque cette section apparaît pour la première fois, aucune valeur n’est sélectionnée. Si vous oubliez de cocher la [!UICONTROL All First Party] case ou de sélectionner individuellement des sources de données dans la [!UICONTROL Available Data Sources] fenêtre, aucune donnée ne sera délimitée.

### Format mal configuré

Lors de la sélection d’un format pour vos données délimitées, il est préférable, si possible, de réutiliser un format existant. L’utilisation d’un format déjà éprouvé permet de garantir que vos données sortantes seront générées avec succès. Pour savoir exactement comment un format existant est formaté, cliquez sur l’ [!UICONTROL Formats] option dans la barre de menus et recherchez votre format par nom ou par numéro d’identification. Les formats ou les macros mal formés utilisés dans les formats fourniront une sortie mal formatée ou empêcheront l’affichage complet des informations.

Pour plus d’informations sur la configuration des formats et l’utilisation des macros, voir Macros [au format de](formats/file-formats.md#) fichier et Macros [au format](formats/web-formats.md)HTTP.

### Serveur mal configuré

* **[!DNL FTP]**
   * **[!UICONTROL Domain]**
      * N’entrez aucun préfixe pour les noms d’hôtes. Si vous avez un compte [!DNL ftp://hello.com], entrez simplement [!DNL hello.com] dans ce champ.
   * **[!UICONTROL Port/Type Combination]**
      * Pour un [!DNL FTP] transfert, le type de transfert préféré est [!DNL SFTP].
      * Lors de la sélection du [!DNL SFTP] type, le port est presque toujours 22.
      * Lors de la sélection du [!DNL FTPs/TLS] type, le port est presque toujours 21.
      * Le [!DNL FTPs/TLS] type n&#39;est pas le même qu&#39;un [!DNL FTP] transfert régulier. Nous ne soutenons pas les [!DNL FTP] transferts réguliers (non sécurisés).
   * **[!UICONTROL Remote Path]**
      * Lorsque vous choisissez un sous-chemin distant, il doit être entré sans barre oblique de début.
      * Si votre fichier transféré est censé être placé dans le [!DNL (root)/inbound] sous-dossier, ajoutez simplement [!DNL inbound] pour le chemin d&#39;accès distant, pas [!DNL /inbound].
      * Si vous envoyez vos fichiers à plusieurs répertoires par le chemin d’accès, entrez des barres obliques entre chaque répertoire. Si l&#39;emplacement de [!DNL /inbound/subdirectory1/subdirectory2]la variable est indiqué, vous devez entrer [!DNL inbound/subdirectory1/subdirectory2] dans ce champ.
      * Si votre fichier doit être placé dans le répertoire automatiquement acheminé vers le serveur externe, vous pouvez laisser cet espace vide. N’entrez pas de point ( . ), barre oblique ( / ) ou autre chose.

* **[!DNL S3]**
   * [!DNL S3] est le protocole de transfert préféré (par rapport [!DNL FTP] ou [!DNL HTTP]).
      * **[!UICONTROL Bucket]**
         * Le nom du compartiment doit être répertorié sans barre oblique, préfixe, suffixe, etc. Si l&#39;adresse [!DNL s3://your-bucket] vous est donnée, vous devez simplement ajouter [!DNL your-bucket] à ce champ.
      * **[!UICONTROL Directory]**
         * Ne renseignez pas ce champ, sauf si un sous-répertoire spécifique vous a été attribué, dans lequel les données doivent être placées. Si l&#39;adresse [!DNL s3://your-bucket/your-subdirectory]vous est attribuée, entrez [!DNL your-bucket] dans le [!UICONTROL Bucket] champ et [!DNL your-subdirectory] ajoutez-le au [!UICONTROL Directory] champ. N’ajoutez pas de barres obliques précédentes.
         * Si vous devez parcourir plusieurs répertoires par le chemin d’accès, vous devez alors utiliser des barres obliques comme séparateurs. Ainsi, un emplacement de [!DNL s3://your-bucket/your-subdirectory1/your-subdirectory2] aurait [!DNL your-bucket] dans le [!UICONTROL Bucket] champ et [!DNL your-subdirectory1/your-subdirectory2] entré dans le [!UICONTROL Directory] champ.
      * **[!UICONTROL Access / Secret Keys]**
         * Lorsque [!DNL TechOps] crée un compartiment et fournit des clés d’accès/de secret à un consultant, ces informations d’identification sont généralement `READ-ONLY` destinées à être transmises au client. Ces informations d’identification ne doivent pas être saisies dans les [!UICONTROL Access / Secret Key] champs, car le transfert échouera (car elles sont en lecture seule et ne peuvent pas être écrites). Dans le cas où [!DNL TechOps] crée un compartiment et fournit des informations d’identification, le consultant doit également demander une paire de clés Adobe - À NE PAS DONNER AU CLIENT - qui permettra d’écrire des fichiers dans ce compartiment. Cette clé devrait être ajoutée à ces champs.

* **[!DNL HTTP]**
   * **[!UICONTROL Domain]**
      * Entrez des informations de préfixe pour [!DNL HTTP] les entrées. Si vous avez un compte [!DNL https://superduper.com], entrez [!DNL https://superduper.com] dans ce champ.
      * **[!UICONTROL URL Prefix]**
         * Lorsque vous ajoutez un [!DNL URL] préfixe, laissez la barre oblique précédente désactivée. Une adresse de [!DNL https://hello.com/r/x/y/z] doit être [!DNL https://hello.com] saisie dans le [!UICONTROL Domain] champ et [!DNL r/x/y/z] saisie ici dans le [!UICONTROL URL Prefix] champ.
         * Si aucune valeur n’ [!UICONTROL URL Prefix] est nécessaire, laissez cette valeur vide.
      * **[!UICONTROL Authentication - SSH Key]**
         * Saisissez la valeur de `SSH PRIVATE` clé complète dans cette zone, y compris les en-têtes, les pieds de page et les sauts de ligne, afin de garantir un chiffrement/un enregistrement de clé précis.

### Pas assez de temps pour la génération sortante

Le processus de décodage s’exécute deux fois par jour et plusieurs processus (décodage, publication, publication vers des emplacements externes, etc.) doit s’exécuter avant qu’un fichier ne soit envoyé vers sa destination finale. Une bonne règle de base est qu’une destination doit être entièrement configurée au moins 24 heures avant que vous puissiez vous attendre à ce que les données soient transférées vers un emplacement externe.

### Taille de fractionnement de fichier trop grande

Lorsque vous délimitez des fichiers vers des destinations, vous pouvez scinder des fichiers sortants plus volumineux en blocs de fichiers. Assurez-vous que les blocs de fichiers individuels ne dépassent pas 10 Go. See also, [Outbound Data File Name: Syntax and Examples](https://docs.adobe.com/help/en/audience-manager/user-guide/implemenation-integration-guides/receiving-audience-data/batch-outbound-data-transfers/outbound-file-name-contents.html).


## Comment configurer vos destinations pour exporter des ID d&#39;Experience Cloud, d&#39;ID de client ou d&#39;ID d&#39;Audience Manager dans des fichiers de données sortants {#set-up-destinations-export}

This page shows you how to set up destinations to export data keyed off the ID type you want in [!UICONTROL Outbound Data Files].

<!-- set-up-destinations-mcid-aamid.xml -->

Les destinations permettent à nos clients d&#39;activer leurs données sur n&#39;importe quel nombre de canaux numériques. Par exemple, ils peuvent exporter des données d’audience vers d’autres [!DNL Adobe Experience Cloud] solutions ([!DNL Target], [!DNL Campaign], etc.). Ou bien, ils peuvent envoyer des données à [!UICONTROL DSP]s, [!UICONTROL SSP]s, ou à toute plate-forme intégrée à l&#39;Audience Manager. Nous conservons une liste de partenaires avec lesquels nous travaillons sur notre page [Wiki](https://wiki.corp.adobe.com/display/MCPI)Intégrations.

>[!NOTE]
>
>Pour obtenir une présentation détaillée sur la création de destinations dans l’interface utilisateur d’administration, consultez l’article [Créer ou modifier des destinations](companies/admin-manage-company-destinations.md#create-edit-company-destinations) de Société.

Vos clients souhaitent exporter différents types d’ID en fonction de la destination. Le graphique de configuration ci-dessous présente les options que vous devez sélectionner pour exporter les informations de profil liées à différents types d’ID. Nous vous recommandons également de consulter l’ [index des identifiants en Audience Manager](https://marketing.adobe.com/resources/help/en_US/aam/ids-in-aam.html). Il y a trois paramètres importants à prendre en compte : le [!UICONTROL User ID Key], le [!UICONTROL Data Source Type] et le [!UICONTROL Format]. Nous les détaillons tous ci-dessous.

* [!UICONTROL User ID Key]. Dans la [!UICONTROL Admin UI], allez à **[!UICONTROL Companies]**. Recherchez la société de votre client et cliquez dessus. Recherchez l&#39; **[!UICONTROL Destinations]** onglet et appuyez sur **[!UICONTROL Add Destination]**. Dans le **[!UICONTROL Add Destination]** processus, sélectionnez le [!UICONTROL User ID Key]. Le [!UICONTROL User ID Key] filtre les identifiants entrants à partir de la source de données de la cible et autorise uniquement la transmission des identifiants.

   ![](assets/user_id_key.PNG)

* [!UICONTROL Data Source Type]. Sélectionnez cette option lors de la création d’une destination dans l’interface utilisateur de l’Audience Manager. Tout d&#39;abord, sélectionnez [!UICONTROL Inbound], puis sélectionnez le type d&#39;ID souhaité. Les options sont les suivantes :

   ![](assets/data_source_settings.PNG)

* [!UICONTROL Format]. Cette option détermine le format de fichier que vous allez exporter. Dans le **[!UICONTROL Add Destination]** processus, sous **[!UICONTROL Batch Data]**, sélectionnez le format.

Pour inspecter un format, accédez à **[!UICONTROL Admin UI > Formats]** et recherchez l’ [!UICONTROL Data Row] élément. Cet élément contient une macro du format de fichier, &lt;MCID>, dans l’exemple ci-dessous.

![](assets/data_row.PNG)

<table id="table_DAEE5BC75DCB4FC690C4BAE41F627DEC"> 
 <thead> 
  <tr> 
   <th colname="col01" class="entry"> Numéro de configuration </th> 
   <th colname="col1" class="entry"> <p>Clé utilisateur </p> </th> 
   <th colname="col2" class="entry"> <p>Type de source de données </p> </th> 
   <th colname="col3" class="entry"> <p>Format </p> </th> 
   <th colname="col4" class="entry"> <p>Type d’ID exporté </p> </th> 
  </tr>
 </thead>
 <tbody> 
  <tr> 
   <td colname="col01"> 1 </td> 
   <td colname="col1"> <p>Adobe Audience Manager (0) </p> </td> 
   <td colname="col2"> <p>Experience Cloud ID </p> </td> 
   <td colname="col3"> <p>&lt;DP_UUID&gt; </p> </td> 
   <td colname="col4"> <p>Experience Cloud ID </p> </td> 
  </tr> 
  <tr> 
   <td colname="col01"> 2 </td> 
   <td colname="col1"> <p>Adobe Audience Manager (0) </p> </td> 
   <td colname="col2"> <p>Experience Cloud ID </p> </td> 
   <td colname="col3"> <p>MCID </p> </td> 
   <td colname="col4"> <p>UUID Audience Manager </p> </td> 
  </tr> 
  <tr> 
   <td colname="col01"> 3 </td> 
   <td colname="col1"> <p>Adobe Audience Manager (0) </p> </td> 
   <td colname="col2"> <p>Experience Cloud ID </p> </td> 
   <td colname="col3"> <p>UUID </p> </td> 
   <td colname="col4"> <p>Experience Cloud ID </p> </td> 
  </tr> 
  <tr> 
   <td colname="col01"> 4 </td> 
   <td colname="col1"> <p>Adobe Audience Manager (0) </p> </td> 
   <td colname="col2"> <p>ID Audience Manager </p> </td> 
   <td colname="col3"> <p>&lt;DP_UUID&gt; </p> </td> 
   <td colname="col4"> <p>UUID Audience Manager </p> </td> 
  </tr> 
  <tr> 
   <td colname="col01"> 5 </td> 
   <td colname="col1"> <p>Adobe Audience Manager (0) </p> </td> 
   <td colname="col2"> <p>ID Audience Manager </p> </td> 
   <td colname="col3"> <p>MCID </p> </td> 
   <td colname="col4"> <p>Experience Cloud ID </p> </td> 
  </tr> 
  <tr> 
   <td colname="col01"> 6 </td> 
   <td colname="col1"> <p>Adobe Audience Manager (0) </p> </td> 
   <td colname="col2"> <p>ID Audience Manager </p> </td> 
   <td colname="col3"> <p>UUID </p> </td> 
   <td colname="col4"> <p>UUID Audience Manager </p> </td> 
  </tr> 
  <tr> 
   <td colname="col01"> 7 </td> 
   <td colname="col1"> <p>DPID (toute source de données à laquelle la société a accès) </p> </td> 
   <td colname="col2"> <p>Identifiant client </p> </td> 
   <td colname="col3"> <p>&lt;DP_UUID&gt; </p> </td> 
   <td colname="col4"> <p>ID de client (DPUUID) </p> </td> 
  </tr> 
  <tr> 
   <td colname="col01"> 8 </td> 
   <td colname="col1"> <p>DPID (toute source de données à laquelle la société a accès) </p> </td> 
   <td colname="col2"> <p>Identifiant client </p> </td> 
   <td colname="col3"> <p>MCID </p> </td> 
   <td colname="col4"> <p>Experience Cloud ID </p> </td> 
  </tr> 
  <tr> 
   <td colname="col01"> 9 </td> 
   <td colname="col1"> <p>DPID (toute source de données à laquelle la société a accès) </p> </td> 
   <td colname="col2"> <p>Identifiant client </p> </td> 
   <td colname="col3"> <p>UUID </p> </td> 
   <td colname="col4"> <p>UUID Audience Manager </p> </td> 
  </tr> 
  <tr> 
   <td colname="col01"> 10 </td> 
   <td colname="col1"> <p>DPID (toute source de données à laquelle la société a accès) </p> </td> 
   <td colname="col2"> <p>ID Audience Manager </p> </td> 
   <td colname="col3"> <p>&lt;DP_UUID&gt; </p> </td> 
   <td colname="col4"> <p>UUID Audience Manager </p> </td> 
  </tr> 
  <tr> 
   <td colname="col01"> 11 </td> 
   <td colname="col1"> <p>DPID (toute source de données à laquelle la société a accès) </p> </td> 
   <td colname="col2"> <p>ID Audience Manager </p> </td> 
   <td colname="col3"> <p>MCID </p> </td> 
   <td colname="col4"> <p>Experience Cloud ID </p> </td> 
  </tr> 
  <tr> 
   <td colname="col01"> 12 </td> 
   <td colname="col1"> <p>DPID (toute source de données à laquelle la société a accès) </p> </td> 
   <td colname="col2"> <p>ID Audience Manager </p> </td> 
   <td colname="col3"> <p>UUID </p> </td> 
   <td colname="col4"> <p>UUID Audience Manager </p> </td> 
  </tr> 
 </tbody> 
</table>

## Cas d’utilisation

Disons que vous utilisez l&#39;Audience Manager et [!DNL Campaign]. Pour rendre les données client exploitables dans [!DNL Campaign], vous souhaitez exporter [!UICONTROL Experience Cloud IDs]. Dans ce cas, vous devez utiliser la configuration numéro 3.