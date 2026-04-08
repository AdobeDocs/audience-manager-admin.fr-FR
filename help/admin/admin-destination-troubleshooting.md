---
description: Informations pour vous aider à configurer des destinations dans Audience Manager et à éviter les problèmes courants.
seo-description: Information to help you set up destinations in Audience Manager and avoid common problems.
seo-title: Destination Setup Troubleshooting
title: Dépannage de la configuration de la destination
uuid: 04080fb9-6c7b-4de7-960e-54482be2de83
exl-id: 53c72b1a-f1a1-4266-a595-e4821c2640b2
TQID: https://experienceleague.adobe.com/R21EJzuvrPlTAa3n92xgT74wdAKKKZxlJL8nWNn3mgA
product_v2: id: df80eeb1-8d72-467e-b0df-9d51c7d3a0a1
feature_v2: id: a8b0238e-1d43-4679-a3b4-5ba1bad83baaid: b82b475d-1e7d-46c6-9172-1f9c73004b11id: c814092e-2730-45e8-a12d-e084529f52cb
topic_v2: id: b5ce8718-c3af-4fdb-a1a9-fca32f83a87cid: c1579802-ddd4-4214-8a91-97b2066abe11
source-git-commit: d2bed13a6ac7d38ae79b65d492b6de0ca6b6d488
workflow-type: tm+mt
source-wordcount: 1343
ht-degree: 3%

---

# Dépannage de la configuration de la destination {#destination-setup-troubleshooting}

Informations pour vous aider à configurer des destinations dans Audience Manager et à éviter les problèmes courants.

## J’ai configuré une destination, mais je ne vois aucun fichier. Où sont-ils ? {#destination-no-files}

<!-- c_dest_tshooting.xml -->

Les problèmes courants de configuration des destinations incluent les problèmes suivants :

### Destination mal configurée

* **Clé de [!UICONTROL UserID] incorrecte :** la clé de [!UICONTROL UserID] est la [!UICONTROL MasterDPID] de cette destination et sert de base aux valeurs d’identifiant qui seront émises. Même si une clé [!UICONTROL UserID] peut être sélectionnée dans la liste déroulante, cela ne signifie pas nécessairement qu’il existe des identifiants/caractéristiques/segments mappés à cette valeur. Si le processus [!UICONTROL Outbound] (qui s’exécute après la création des destinations) ne trouve aucun utilisateur mappé à cette clé [!UICONTROL UserID], aucune donnée ne sera générée.
* **Non dans le fichier Sources de données sélectionnées :** lorsque vous choisissez un type de destination autre que [!UICONTROL S2S], une section s’affiche au bas de l’écran sous le libellé [!UICONTROL Configure Data Sources]. Lorsque cette section apparaît pour la première fois, aucune valeur n’est sélectionnée. Si vous oubliez de cocher la case [!UICONTROL All First Party] ou de sélectionner individuellement les sources de données dans la fenêtre [!UICONTROL Available Data Sources], aucune donnée ne sera générée.

### Format mal configuré

Lors de la sélection d’un format pour vos données sortantes, il est préférable, si possible, de réutiliser un format existant. L’utilisation d’un format déjà éprouvé garantit que vos données sortantes seront générées avec succès. Pour voir exactement comment un format existant est formaté, cliquez sur l’option [!UICONTROL Formats] dans la barre de menus et recherchez votre format par nom ou par numéro d’ID. Les formats ou macros incorrects utilisés dans les formats fournissent une sortie incorrectement formatée ou empêchent la sortie complète des informations.

Pour plus d’informations sur la configuration des formats et l’utilisation des macros, voir [Macros au format de fichier](formats/file-formats.md#) et [Macros au format HTTP](formats/web-formats.md).

### Serveur mal configuré

* **[!DNL FTP]**
   * **[!UICONTROL Domain]**
      * Ne saisissez aucun préfixe pour les noms d’hôtes. Si vous recevez un [!DNL ftp://hello.com] de compte, il vous suffit de saisir [!DNL hello.com] dans ce champ.
   * **[!UICONTROL Port/Type Combination]**
      * Pour un transfert [!DNL FTP], le type de transfert préféré est [!DNL SFTP].
      * Lors de la sélection du type de [!DNL SFTP], le port est presque toujours 22.
      * Lors de la sélection du type de [!DNL FTPs/TLS], le port est presque toujours 21.
      * Le type de [!DNL FTPs/TLS] n’est pas identique à un transfert de [!DNL FTP] normal. Nous ne prenons pas en charge les transferts [!DNL FTP] réguliers (non sécurisés).
   * **[!UICONTROL Remote Path]**
      * Lors du choix d’un sous-chemin distant, il doit être saisi sans barre oblique.
      * Si le fichier transféré est censé être placé dans le sous-dossier [!DNL (root)/inbound], ajoutez simplement des [!DNL inbound] pour le chemin d’accès distant, et non des [!DNL /inbound].
      * Si vous envoyez vos fichiers dans plusieurs répertoires du chemin d’accès, saisissez des barres obliques entre chaque répertoire. Si l’emplacement de [!DNL /inbound/subdirectory1/subdirectory2] vous est indiqué, vous devez saisir [!DNL inbound/subdirectory1/subdirectory2] dans ce champ.
      * Si votre fichier doit être placé dans le répertoire automatiquement acheminé vers par le serveur externe, vous pouvez laisser cet espace vide. Ne saisissez pas de point ( . ), barre oblique ( / ) ou autre chose.

* **[!DNL S3]**
   * [!DNL S3] est le protocole de transfert préféré (sur [!DNL FTP] ou [!DNL HTTP]).
      * **[!UICONTROL Bucket]**
         * Le nom du compartiment doit être répertorié sans barres obliques, préfixes, suffixes, etc. Si l’adresse [!DNL s3://your-bucket] vous est fournie, il vous suffit d’ajouter [!DNL your-bucket] dans ce champ.
      * **[!UICONTROL Directory]**
         * Ne renseignez pas ce champ, sauf si vous disposez d&#39;un sous-répertoire spécifique dans lequel les données doivent être placées. Si le [!DNL s3://your-bucket/your-subdirectory] d’adresse vous est attribué, saisissez [!DNL your-bucket] dans le champ [!UICONTROL Bucket] et [!DNL your-subdirectory] doit être ajouté dans le champ [!UICONTROL Directory] . N’ajoutez pas les barres obliques précédentes.
         * Si vous devez parcourir plusieurs répertoires le long du chemin, vous devez utiliser des barres obliques comme séparateurs. Ainsi, un emplacement de [!DNL s3://your-bucket/your-subdirectory1/your-subdirectory2] aurait [!DNL your-bucket] dans le champ [!UICONTROL Bucket] et [!DNL your-subdirectory1/your-subdirectory2] saisi dans le champ [!UICONTROL Directory].
      * **[!UICONTROL Access / Secret Keys]**
         * Lorsque [!DNL TechOps] crée un compartiment et fournit des clés d’accès/secrètes à un consultant, ces informations d’identification sont généralement `READ-ONLY` informations d’identification destinées à être transmises au client. Ces informations d’identification ne doivent pas être saisies dans les champs [!UICONTROL Access / Secret Key], car cela entraînerait l’échec du transfert (car ces informations d’identification sont en lecture seule, et non inscriptibles). Dans le cas où [!DNL TechOps] crée un compartiment et fournit des informations d’identification, le consultant doit également demander une paire de clés Adobe (À NE PAS FOURNIR AU CLIENT) qui permettra d’écrire des fichiers dans ce compartiment. Cette clé doit être ajoutée à ces champs.

* **[!DNL HTTP]**
   * **[!UICONTROL Domain]**
      * Ne saisissez pas d’informations de préfixe pour les entrées de [!DNL HTTP]. Si vous recevez un [!DNL https://superduper.com] de compte, saisissez [!DNL https://superduper.com] dans ce champ.
      * **[!UICONTROL URL Prefix]**
         * Lors de l’ajout d’un préfixe [!DNL URL], laissez la barre oblique précédente désactivée. Une adresse de [!DNL https://hello.com/r/x/y/z] doit avoir [!DNL https://hello.com] saisie dans le champ [!UICONTROL Domain] et [!DNL r/x/y/z] saisie ici dans le champ [!UICONTROL URL Prefix].
         * Si aucune [!UICONTROL URL Prefix] n’est nécessaire, laissez cette valeur vide.
      * **[!UICONTROL Authentication - SSH Key]**
         * Saisissez la valeur de clé de `SSH PRIVATE` complète dans cette zone, y compris les en-têtes, pieds de page et sauts de ligne pour garantir un chiffrement/stockage de clé précis.

### Pas assez de temps pour la génération sortante

Le processus sortant s’exécute deux fois par jour et plusieurs processus (sortant, publication, envoi vers des emplacements externes, etc.) doit s’exécuter avant qu’un fichier ne soit envoyé à sa destination finale. Une bonne règle de base est qu’une destination doit être entièrement configurée au moins 24 heures avant que vous puissiez vous attendre à ce que les données soient transmises à un emplacement externe.

### Tailles de partage de fichier trop grandes

Lorsque vous envoyez des fichiers sortants vers des destinations, vous pouvez fractionner les fichiers sortants plus volumineux en blocs de fichiers. Assurez-vous que les blocs de fichiers individuels ne dépassent pas 10 Go. Voir aussi [Nom du fichier de données sortant : syntaxe et exemples](https://experienceleague.adobe.com/docs/audience-manager/user-guide/implementation-integration-guides/receiving-audience-data/batch-outbound-data-transfers/outbound-file-name-contents.html?lang=en).


## Comment configurer vos destinations pour exporter des Experience Cloud ID, des Customer ID ou des Audience Manager ID dans des fichiers de données sortants {#set-up-destinations-export}

Cette page vous explique comment configurer des destinations pour exporter des données indexées selon le type d’identifiant souhaité dans [!UICONTROL Outbound Data Files].

<!-- set-up-destinations-mcid-aamid.xml -->

Les destinations permettent à nos clients d’activer leurs données sur un nombre indéfini de canaux numériques. Par exemple, ils peuvent exporter des données d’audience vers d’autres solutions [!DNL Adobe Experience Cloud] ([!DNL Target], [!DNL Campaign], etc.). Elles peuvent également envoyer des données à [!UICONTROL DSP], [!UICONTROL SSP] ou toute autre plateforme intégrée à Audience Manager. Nous conservons une liste des partenaires avec lesquels nous travaillons sur notre [page Wiki Intégrations](https://wiki.corp.adobe.com/display/MCPI).

>[!NOTE]
>
>Pour une présentation détaillée de la création de destinations dans l’interface utilisateur d’administration, reportez-vous à l’article [Création ou modification de destinations d’entreprise](companies/admin-manage-company-destinations.md#create-edit-company-destinations).

Vos clients souhaitent exporter différents types d’ID en fonction de la destination. Le graphique de configuration ci-dessous montre les options que vous devez sélectionner pour exporter les informations de profil liées aux différents types d’ID. Nous vous recommandons de vous reporter également à l’[Index des identifiants dans Audience Manager](https://experienceleague.adobe.com/docs/audience-manager/user-guide/reference/ids-in-aam.html?lang=en). Il y a trois paramètres importants à considérer, le [!UICONTROL User ID Key], le [!UICONTROL Data Source Type] et le [!UICONTROL Format]. Nous les détaillons tous ci-dessous.

* [!UICONTROL User ID Key]. Dans la [!UICONTROL Admin UI], allez à **[!UICONTROL Companies]**. Recherchez l’entreprise de votre client et cliquez dessus. Recherchez l’onglet **[!UICONTROL Destinations]** et appuyez sur **[!UICONTROL Add Destination]**. Dans le workflow **[!UICONTROL Add Destination]**, sélectionnez le [!UICONTROL User ID Key]. L’[!UICONTROL User ID Key] filtre les identifiants entrants de la source de données cible et n’autorise la transmission que des identifiants.

  ![](assets/user_id_key.PNG)

* [!UICONTROL Data Source Type]. Sélectionnez cette option lors de la création d’une destination dans l’interface utilisateur d’Audience Manager. Tout d’abord, sélectionnez [!UICONTROL Inbound], puis sélectionnez le type d’identifiant de votre choix. Les options sont les suivantes :

  ![](assets/data_source_settings.PNG)

* [!UICONTROL Format]. Cette option détermine le format de fichier que vous allez exporter. Dans le workflow **[!UICONTROL Add Destination]**, sous **[!UICONTROL Batch Data]**, sélectionnez le format.

Pour inspecter un format, accédez à **[!UICONTROL Admin UI > Formats]** et recherchez l’élément [!UICONTROL Data Row] . Cet élément contient une macro du format de fichier, &lt;MCID> dans l&#39;exemple ci-dessous.

![](assets/data_row.PNG)

<table id="table_DAEE5BC75DCB4FC690C4BAE41F627DEC"> 
 <thead> 
  <tr> 
   <th colname="col01" class="entry"> N° de configuration </th> 
   <th colname="col1" class="entry"> <p>Clé de l'utilisateur </p> </th> 
   <th colname="col2" class="entry"> <p>Type de Source de données </p> </th> 
   <th colname="col3" class="entry"> <p>Format </p> </th> 
   <th colname="col4" class="entry"> <p>Type d’identifiant exporté </p> </th> 
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
   <td colname="col4"> <p>UUID AUDIENCE MANAGER </p> </td> 
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
   <td colname="col2"> <p>AUDIENCE MANAGER ID </p> </td> 
   <td colname="col3"> <p>&lt;DP_UUID&gt; </p> </td> 
   <td colname="col4"> <p>UUID AUDIENCE MANAGER </p> </td> 
  </tr> 
  <tr> 
   <td colname="col01"> 5 </td> 
   <td colname="col1"> <p>Adobe Audience Manager (0) </p> </td> 
   <td colname="col2"> <p>AUDIENCE MANAGER ID </p> </td> 
   <td colname="col3"> <p>MCID </p> </td> 
   <td colname="col4"> <p>Experience Cloud ID </p> </td> 
  </tr> 
  <tr> 
   <td colname="col01"> 6 </td> 
   <td colname="col1"> <p>Adobe Audience Manager (0) </p> </td> 
   <td colname="col2"> <p>AUDIENCE MANAGER ID </p> </td> 
   <td colname="col3"> <p>UUID </p> </td> 
   <td colname="col4"> <p>UUID AUDIENCE MANAGER </p> </td> 
  </tr> 
  <tr> 
   <td colname="col01"> 7 </td> 
   <td colname="col1"> <p>DPID (toute source de données à laquelle l’entreprise a accès) </p> </td> 
   <td colname="col2"> <p>Identifiant client </p> </td> 
   <td colname="col3"> <p>&lt;DP_UUID&gt; </p> </td> 
   <td colname="col4"> <p>ID de client (DPUUID) </p> </td> 
  </tr> 
  <tr> 
   <td colname="col01"> 8 </td> 
   <td colname="col1"> <p>DPID (toute source de données à laquelle l’entreprise a accès) </p> </td> 
   <td colname="col2"> <p>Identifiant client </p> </td> 
   <td colname="col3"> <p>MCID </p> </td> 
   <td colname="col4"> <p>Experience Cloud ID </p> </td> 
  </tr> 
  <tr> 
   <td colname="col01"> 9 </td> 
   <td colname="col1"> <p>DPID (toute source de données à laquelle l’entreprise a accès) </p> </td> 
   <td colname="col2"> <p>Identifiant client </p> </td> 
   <td colname="col3"> <p>UUID </p> </td> 
   <td colname="col4"> <p>UUID AUDIENCE MANAGER </p> </td> 
  </tr> 
  <tr> 
   <td colname="col01"> 10 </td> 
   <td colname="col1"> <p>DPID (toute source de données à laquelle l’entreprise a accès) </p> </td> 
   <td colname="col2"> <p>AUDIENCE MANAGER ID </p> </td> 
   <td colname="col3"> <p>&lt;DP_UUID&gt; </p> </td> 
   <td colname="col4"> <p>UUID AUDIENCE MANAGER </p> </td> 
  </tr> 
  <tr> 
   <td colname="col01"> 11 </td> 
   <td colname="col1"> <p>DPID (toute source de données à laquelle l’entreprise a accès) </p> </td> 
   <td colname="col2"> <p>AUDIENCE MANAGER ID </p> </td> 
   <td colname="col3"> <p>MCID </p> </td> 
   <td colname="col4"> <p>Experience Cloud ID </p> </td> 
  </tr> 
  <tr> 
   <td colname="col01"> 12 </td> 
   <td colname="col1"> <p>DPID (toute source de données à laquelle l’entreprise a accès) </p> </td> 
   <td colname="col2"> <p>AUDIENCE MANAGER ID </p> </td> 
   <td colname="col3"> <p>UUID </p> </td> 
   <td colname="col4"> <p>UUID AUDIENCE MANAGER </p> </td> 
  </tr> 
 </tbody> 
</table>

## Cas d’utilisation

Supposons que vous utilisiez Audience Manager et [!DNL Campaign]. Pour que les données client soient exploitables dans [!DNL Campaign], vous devez exporter des [!UICONTROL Experience Cloud IDs]. Dans ce cas, vous devez utiliser le numéro de configuration 3.
