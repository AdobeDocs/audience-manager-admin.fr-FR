---
description: Certains clients peuvent ne pas souhaiter fournir à Adobe leur accès Amazon Simple Storage Service (Amazon S3) ni leurs clés secrètes pour autoriser le transfert des données de destination vers leur compartiment.
seo-description: Certains clients peuvent ne pas souhaiter fournir à Adobe leur accès Amazon Simple Storage Service (Amazon S3) ni leurs clés secrètes pour autoriser le transfert des données de destination vers leur compartiment.
seo-title: Autorisation de l’accès au compartiment inter-comptes Amazon S3 pour les destinations par lot
title: Autorisation de l’accès au compartiment inter-comptes Amazon S3 pour les destinations par lot
uuid: da2bcbda-a765-437a-bfe9-4355383a4730
translation-type: tm+mt
source-git-commit: be661580da839ce6332a0ad827dec08e854abe54

---


# Autorisation de l’accès au compartiment inter-comptes Amazon S3 pour les destinations par lot{#authorize-cross-account-bucket-batch}

Certains clients peuvent ne pas souhaiter fournir leurs clés [!DNL Amazon S3] d’accès ou secrètes à Adobe pour autoriser le transfert des données de destination vers leur compartiment.

Une alternative que nous pouvons offrir à nos clients est [!UICONTROL Cross-Account Bucket Permissions] dans [!DNL Amazon S3]. Ce processus est décrit dans la documentation [](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-walkthroughs-managing-access-example2.html)AWS. Pour activer cette alternative dans Audience Manager, procédez comme suit :

1. Allez à **[!UICONTROL Servers]** et sélectionnez **[!UICONTROL Create Server]**.
1. Sélectionnez **[!UICONTROL S3]** dans le **[!UICONTROL Protocol/Credentials]** masque déroulant.
1. Cochez l’ **[!UICONTROL Use Internal Adobe Key]** option.
1. Utilisez le compte et le nom du compartiment de votre client dans [!DNL Amazon S3].
1. Assurez-vous que votre client affiche la liste blanche du [!DNL Amazon S3] compte `975822914085` dans son [!DNL S3] compartiment.

>[!NOTE]
>
>Notre éditeur sortant s’assure que le niveau d’autorisation `bucket-owner-full-control` est défini sur les données transférées, de sorte que votre client puisse posséder ces données.
