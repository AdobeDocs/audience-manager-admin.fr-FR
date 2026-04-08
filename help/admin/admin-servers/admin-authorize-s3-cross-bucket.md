---
description: Certains clients peuvent ne pas vouloir fournir leur accès Amazon Simple Storage Service (Amazon S3) ou leurs clés secrètes à Adobe pour autoriser le chargement des données de destination dans leurs compartiments.
seo-description: Some customers may not want to provide their Amazon Simple Storage Service (Amazon S3) access or secret keys to Adobe to authorize destination data upload to their buckets.
seo-title: How To  Authorize Cross-Account Amazon S3 Bucket Access for Batch Destinations
title: Comment autoriser l’accès au compartiment Amazon S3 entre comptes pour les destinations par lots
uuid: da2bcbda-a765-437a-bfe9-4355383a4730
exl-id: f3b97c31-714f-4841-884b-bc507267a932
TQID: https://experienceleague.adobe.com/KFc06xetyatq5n-F8Uu-6nmepyjbFyQ3nYB-vXkdPdE
product_v2:
  - id: df80eeb1-8d72-467e-b0df-9d51c7d3a0a1
feature_v2:
  - id: c814092e-2730-45e8-a12d-e084529f52cb
source-git-commit: d2bed13a6ac7d38ae79b65d492b6de0ca6b6d488
workflow-type: tm+mt
source-wordcount: 168
ht-degree: 0%

---

# Comment autoriser l’accès au compartiment Amazon S3 entre comptes pour les destinations par lots{#authorize-cross-account-bucket-batch}

Certains clients peuvent ne pas vouloir fournir leur accès [!DNL Amazon S3] ou leurs clés secrètes à Adobe pour autoriser le chargement des données de destination dans leurs compartiments.

Une alternative que nous pouvons offrir à nos clients est [!UICONTROL Cross-Account Bucket Permissions] en [!DNL Amazon S3]. Ce processus est décrit dans la documentation [&#128279;](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-walkthroughs-managing-access-example2.html). Pour activer cette alternative dans Audience Manager, procédez comme suit :

1. Accédez à **[!UICONTROL Servers]** et sélectionnez **[!UICONTROL Create Server]**.
1. Sélectionnez **[!UICONTROL S3]** dans le masque déroulant **[!UICONTROL Protocol/Credentials]** .
1. Cochez l’option **[!UICONTROL Use Internal Adobe Key]** .
1. Utilisez le compte et le nom du compartiment de votre client dans [!DNL Amazon S3].
1. Assurez-vous que votre client ou votre cliente dispose des `975822914085` de compte [!DNL Amazon S3] dans son compartiment de [!DNL S3].

>[!NOTE]
>
>Notre éditeur sortant s’assure que le niveau d’autorisation `bucket-owner-full-control` est défini sur les données téléchargées, de sorte que votre client puisse être propriétaire de ces données.
