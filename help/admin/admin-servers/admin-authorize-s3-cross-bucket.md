---
description: Certains clients peuvent ne pas vouloir fournir à leur Adobe un accès à Amazon Simple Enregistrement Service (Amazon S3) ou des clés secrètes pour autoriser le transfert des données de destination vers leur compartiment.
seo-description: Certains clients peuvent ne pas vouloir fournir à leur Adobe un accès à Amazon Simple Enregistrement Service (Amazon S3) ou des clés secrètes pour autoriser le transfert des données de destination vers leur compartiment.
seo-title: Autorisation de l’accès au compartiment intercomptes Amazon S3 pour les destinations par lot
title: Autorisation de l’accès au compartiment intercomptes Amazon S3 pour les destinations par lot
uuid: da2bcbda-a765-437a-bfe9-4355383a4730
translation-type: tm+mt
source-git-commit: be661580da839ce6332a0ad827dec08e854abe54
workflow-type: tm+mt
source-wordcount: '200'
ht-degree: 0%

---


# Autorisation de l’accès au compartiment entre comptes Amazon S3 pour les destinations par lots{#authorize-cross-account-bucket-batch}

Certains clients peuvent ne pas vouloir fournir à l&#39;Adobe [!DNL Amazon S3] leur accès ou leur clé secrète pour autoriser le transfert des données de destination dans leur compartiment.

Une alternative que nous pouvons offre à nos clients est [!UICONTROL Cross-Account Bucket Permissions] dans [!DNL Amazon S3]. Ce processus est décrit dans la [documentation AWS](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-walkthroughs-managing-access-example2.html). Pour activer cette alternative en Audience Manager, procédez comme suit :

1. Accédez à **[!UICONTROL Servers]** et sélectionnez **[!UICONTROL Create Server]**.
1. Sélectionnez **[!UICONTROL S3]** dans le masque déroulant **[!UICONTROL Protocol/Credentials]**.
1. Cochez l&#39;option **[!UICONTROL Use Internal Adobe Key]**.
1. Utilisez le compte et le nom du compartiment de votre client dans [!DNL Amazon S3].
1. Assurez-vous que votre client liste autorisée le compte [!DNL Amazon S3] `975822914085` dans sa corbeille [!DNL S3].

>[!NOTE]
>
>Notre éditeur sortant s’assure que le niveau d’autorisation `bucket-owner-full-control` est défini sur les données téléchargées, de sorte que votre client puisse posséder ces données.
