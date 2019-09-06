---
description: Certains clients ne souhaitent peut-être pas fournir leur accès Amazon Simple Storage Service (Amazon S 3) ou des clés secrètes à Adobe pour autoriser le transfert des données de destination vers leurs compartiments.
seo-description: Certains clients ne souhaitent peut-être pas fournir leur accès Amazon Simple Storage Service (Amazon S 3) ou des clés secrètes à Adobe pour autoriser le transfert des données de destination vers leurs compartiments.
seo-title: Autorisation d'accès au compartiment Amazon S 3 à plusieurs comptes pour les destinations par lots
title: Autorisation d'accès au compartiment Amazon S 3 à plusieurs comptes pour les destinations par lots
uuid: da 2 bcbda-a 765-437 a-bfe 9-4355383 a 4730
translation-type: tm+mt
source-git-commit: be661580da839ce6332a0ad827dec08e854abe54

---


# Autorisation d'accès au compartiment Amazon S 3 à plusieurs comptes pour les destinations par lots{#authorize-cross-account-bucket-batch}

Certains clients ne souhaitent peut-être pas fournir leur [!DNL Amazon S3] accès ou clé secrète à Adobe pour autoriser le transfert des données de destination vers leurs intervalles.

Une alternative que nous pouvons offrir à nos clients se trouve [!UICONTROL Cross-Account Bucket Permissions][!DNL Amazon S3]. Ce processus est décrit dans la documentation [AWS](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-walkthroughs-managing-access-example2.html). Pour activer cette alternative dans Audience Manager, procédez comme suit :

1. Sélectionnez **[!UICONTROL Servers]** et sélectionnez **[!UICONTROL Create Server]**.
1. Sélectionnez **[!UICONTROL S3]** dans le masque **[!UICONTROL Protocol/Credentials]** déroulant.
1. Vérifiez l **[!UICONTROL Use Internal Adobe Key]** 'option.
1. Utilisez le nom de votre client et le nom de compartiment dans [!DNL Amazon S3].
1. Assurez-vous que le client blanc répertorie le [!DNL Amazon S3] compte `975822914085` sur son [!DNL S3] compartiment.

>[!NOTE]
>
>Notre éditeur sortant garantit que le niveau d'autorisation `bucket-owner-full-control` est défini sur les données téléchargées, de sorte que votre client puisse posséder ces données.
