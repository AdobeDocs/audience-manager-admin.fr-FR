---
description: Certains clients peuvent ne pas vouloir fournir à Adobe leur accès Amazon Simple Enregistrement Service (Amazon S3) ou leur clé secrète pour autoriser le transfert des données de destination vers leur compartiment.
seo-description: Certains clients peuvent ne pas vouloir fournir à Adobe leur accès Amazon Simple Enregistrement Service (Amazon S3) ou leur clé secrète pour autoriser le transfert des données de destination vers leur compartiment.
seo-title: Comment autoriser l’accès au compartiment intercomptes Amazon S3 pour les destinations par lot
title: Comment autoriser l’accès au compartiment intercomptes Amazon S3 pour les destinations par lot
uuid: da2bcbda-a765-437a-bfe9-4355383a4730
translation-type: tm+mt
source-git-commit: be661580da839ce6332a0ad827dec08e854abe54
workflow-type: tm+mt
source-wordcount: '200'
ht-degree: 0%

---


# How To Authorize Cross-Account Amazon S3 Bucket Access for Batch Destinations{#authorize-cross-account-bucket-batch}

Certains clients peuvent ne pas vouloir fournir leurs clés [!DNL Amazon S3] d’accès ou secrètes à Adobe pour autoriser le transfert des données de destination dans leur compartiment.

Une alternative à laquelle nous pouvons offre nos clients est [!UICONTROL Cross-Account Bucket Permissions] dans [!DNL Amazon S3]. Ce processus est décrit dans la documentation [d’](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-walkthroughs-managing-access-example2.html)AWS. Pour activer cette alternative en Audience Manager, procédez comme suit :

1. Accédez à **[!UICONTROL Servers]** et sélectionnez **[!UICONTROL Create Server]**.
1. Sélectionnez **[!UICONTROL S3]** dans le masque **[!UICONTROL Protocol/Credentials]** déroulant.
1. Cochez l’ **[!UICONTROL Use Internal Adobe Key]** option.
1. Utilisez le compte et le nom du compartiment de votre client dans [!DNL Amazon S3].
1. Assurez-vous que votre client a liste le [!DNL Amazon S3] compte `975822914085` sur son [!DNL S3] compartiment.

>[!NOTE]
>
>Notre éditeur sortant s’assure que le niveau d’autorisation `bucket-owner-full-control` est défini sur les données téléchargées, de sorte que votre client puisse posséder ces données.
