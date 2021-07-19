---
description: Certains clients peuvent ne pas vouloir fournir leur accès Amazon Simple Storage Service (Amazon S3) ou leur clé secrète pour Adobe afin d’autoriser le téléchargement des données de destination vers leurs compartiments.
seo-description: Certains clients peuvent ne pas vouloir fournir leur accès Amazon Simple Storage Service (Amazon S3) ou leur clé secrète pour Adobe afin d’autoriser le téléchargement des données de destination vers leurs compartiments.
seo-title: Comment autoriser le partage des accès entre comptes dans les compartiments Amazon S3 pour les destinations par lots
title: Comment autoriser le partage des accès entre comptes dans les compartiments Amazon S3 pour les destinations par lots
uuid: da2bcbda-a765-437a-bfe9-4355383a4730
exl-id: f3b97c31-714f-4841-884b-bc507267a932
source-git-commit: f5d74995f0664cf63e68b46f1f3c608f34df0e80
workflow-type: tm+mt
source-wordcount: '200'
ht-degree: 0%

---

# Comment autoriser le partage des accès entre comptes dans les compartiments Amazon S3 pour les destinations par lots{#authorize-cross-account-bucket-batch}

Certains clients peuvent ne pas vouloir fournir leur [!DNL Amazon S3] accès ou clé secrète à Adobe pour autoriser le téléchargement des données de destination vers leurs compartiments.

Une alternative que nous pouvons offrir à nos clients est [!UICONTROL Cross-Account Bucket Permissions] dans [!DNL Amazon S3]. Ce processus est décrit dans la [documentation AWS](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-walkthroughs-managing-access-example2.html). Pour activer cette alternative en Audience Manager, procédez comme suit :

1. Accédez à **[!UICONTROL Servers]** et sélectionnez **[!UICONTROL Create Server]**.
1. Sélectionnez **[!UICONTROL S3]** dans le masque déroulant **[!UICONTROL Protocol/Credentials]**.
1. Cochez l’option **[!UICONTROL Use Internal Adobe Key]** .
1. Utilisez le compte et le nom du compartiment de votre client dans [!DNL Amazon S3].
1. Assurez-vous que votre client liste autorisée le compte [!DNL Amazon S3] `975822914085` dans son compartiment [!DNL S3].

>[!NOTE]
>
>Notre éditeur sortant s’assure que le niveau d’autorisation `bucket-owner-full-control` est défini sur les données chargées, de sorte que votre client puisse posséder ces données.
