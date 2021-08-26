---
description: Utilisez la page Sociétés de l’outil d’administration des Audiences Manager pour créer une société.
seo-description: Use the Companies page in the Audience Manager Admin tool to create a new company.
seo-title: Create a Company Profile
title: Création d’un profil d’entreprise
uuid: 55de18f8-883d-43fe-b37f-e8805bb92f7a
exl-id: 80bb8a89-0207-4645-ac42-e73cd10561de
source-git-commit: 1f4dbf8f7b36e64c3015b98ef90b6726d0e7495a
workflow-type: tm+mt
source-wordcount: '933'
ht-degree: 5%

---

# Création d’un profil d’entreprise {#create-a-company-profile}

Utilisez la page [!UICONTROL Companies] de l’outil d’administration des Audiences Manager pour créer une société.

<!-- t_create_company.xml -->

>[!NOTE]
>
>Vous devez avoir le rôle **[!UICONTROL DEXADMIN]** pour créer de nouvelles entreprises.

1. Cliquez sur **[!UICONTROL Companies]** > **[!UICONTROL Add Company]**.
1. Renseignez les champs suivants :

   * **[!UICONTROL Name]**: (Obligatoire) Indiquez le nom de la société.
   * **[!UICONTROL Description]**: (Obligatoire) Fournissez des informations descriptives sur l’entreprise, telles que son secteur d’activité ou son nom complet.
   * **[!UICONTROL Subdomain]**: (Obligatoire) Indiquez le sous-domaine de la société. Le texte que vous saisissez correspond au sous-domaine de l’appel d’événement. Cela ne peut pas être changé. Il doit s’agir d’une chaîne de caractères [!DNL URL] valides.

      Par exemple, si votre société est nommée [!DNL AcmeCorp], le sous-domaine sera [!DNL acmecorp].

      Audience Manager utilise le sous-domaine pour le [!UICONTROL Data Collection Server] (DCS). Dans l’exemple précédent, si la valeur [!DNL URL] complète de votre société dans [!UICONTROL DCS] est [!DNL acmecorp.demdex.net].

   * **[!UICONTROL Lifecyle]**: Spécifiez l’étape souhaitée pour l’entreprise :
      * **[!UICONTROL Active]**: Indiquez que la société sera un client d’Audience Manager principal. Un compte [!UICONTROL Active] signifie un client payant, non seulement pour le conseil, mais pour le SKU de l’Audience Manager.
      * **[!UICONTROL Demo]**: Indiquez que la société sera réservée à des fins de démonstration. Les données de création de rapports seront automatiquement biffées.
      * **[!UICONTROL Prospect]**: Indiquez que l’entreprise est un client d’Audience Manager potentiel, par exemple une société à qui est attribuée une configuration gratuite  [!DNL POC] ou un compte pour une démonstration de vente.
      * **[!UICONTROL Test]**: Indiquez que l’entreprise sera uniquement dédiée aux tests internes.
   * **[!UICONTROL Account Types]**: Indiquez l’ensemble complet des types de compte pour cette société. Aucun type de compte n’est mutuellement exclusif avec un autre type.
      * **[!UICONTROL Full AAM]**: Indiquez que l’entreprise dispose d’un compte Adobe Audience Manager complet et que les utilisateurs disposent d’un accès de connexion.
      * **[!UICONTROL MMP]**: Indiquez que l’entreprise a été autorisée à utiliser les  [!UICONTROL Master Marketing Profile] ([!UICONTROL MMP]) fonctionnalités. La fonction [!UICONTROL MMP] permet aux audiences d’être partagées dans l’Experience Cloud à l’aide d’une fonction [!UICONTROL Experience Cloud ID] ([!DNL MCID]) affectée à chaque visiteur, puis utilisée par l’Audience Manager. Si vous sélectionnez ce type de compte, la commande [!UICONTROL Experience Cloud ID Service] est également automatiquement sélectionnée.

         Pour plus d’informations, voir [Audiences Experience Cloud](https://experienceleague.adobe.com/docs/core-services/interface/services/audiences/audience-library.html?lang=en).
   * **[!UICONTROL Data Source]**: Indiquez que la société est un fournisseur de données tiers dans Audience Manager.
   * **[!UICONTROL Targeting Partner]**: Indiquez que l’entreprise agit comme une plateforme de ciblage pour les clients d’Audience Manager.
   * **[!UICONTROL Visitor ID Service]**: Indiquez que l’entreprise a été autorisée à utiliser le  [!UICONTROL Experience Cloud Visitor ID Service].

      [!UICONTROL Experience Cloud Visitor ID Service] fournit un identifiant visiteur universel pour toutes les solutions Experience Cloud. Pour plus d’informations, consultez le [guide d’utilisation du service d’identification des visiteurs Experience Cloud](https://experienceleague.adobe.com/docs/id-service/using/intro/overview.html?lang=en).

   * **[!UICONTROL Agency]**: Indiquez que la société aura un  [!UICONTROL Agency] compte.



1. Cliquez sur **[!UICONTROL Create]**. Poursuivez avec les instructions de la section [Modifier un profil d’entreprise](../companies/admin-manage-company-profiles.md#edit-company-profile).

   ![Résultat de l’étape](assets/add_company.png)

## Modification d’un profil d’entreprise {#edit-company-profile}

Modifiez le profil d’une entreprise, notamment son nom, sa description, son sous-domaine, son cycle de vie, etc.

<!-- t_edit_company_profile.xml -->

1. Cliquez sur **[!UICONTROL Companies]**, puis localisez et cliquez sur la société de votre choix pour afficher sa page [!UICONTROL Profile].

   Utilisez la zone [!UICONTROL Search] ou les commandes de pagination en bas de la liste pour trouver la société souhaitée. Vous pouvez trier chaque colonne par ordre croissant ou décroissant en cliquant sur l’en-tête de la colonne de votre choix.

   ![Résultat de l’étape](assets/profile_company.png)

1. Modifiez les champs selon les besoins : 

   * **[!UICONTROL Name]**: Modifiez le nom de la société. Il s’agit d’un champ obligatoire.
   * **[!UICONTROL Description]**: Modifiez la description de la société. Il s’agit d’un champ obligatoire.
   * **[!UICONTROL Subdomain]**: (Obligatoire) Indiquez le sous-domaine de la société. Le texte que vous saisissez correspond au sous-domaine de l’appel d’événement. Cela ne peut pas être changé. Il doit s’agir d’une chaîne de caractères [!DNL URL] valides.

      Par exemple, si votre société est nommée [!DNL AcmeCorp], le sous-domaine sera [!DNL acmecorp].

      Audience Manager utilise le sous-domaine pour le [!UICONTROL Data Collection Server] (DCS). Dans l’exemple précédent, si la valeur [!DNL URL] complète de votre société dans [!UICONTROL DCS] est [!DNL acmecorp.demdex.net].

   * **[!UICONTROL imsOrgld]**: ([!UICONTROL Identity Management System Organization ID]) Cet identifiant vous permet de connecter votre société à Adobe Experience Cloud.
   * **[!UICONTROL Lifecyle]**: Spécifiez l’étape souhaitée pour l’entreprise :
      * **[!UICONTROL Active]**: Indiquez que la société sera un client d’Audience Manager principal. Un compte Principal signifie un client payant, pas seulement pour le conseil, mais pour le SKU de l’Audience Manager.
      * **[!UICONTROL Demo]**: Indiquez que la société sera réservée à des fins de démonstration. Les données de création de rapports seront automatiquement biffées.
      * **[!UICONTROL Prospect]**: Indiquez que l’entreprise est un client d’Audience Manager potentiel, par exemple une société à qui est attribuée une configuration gratuite  [!DNL POC] ou un compte pour une démonstration de vente.
      * **[!UICONTROL Test]**: Indiquez que l’entreprise sera uniquement dédiée aux tests internes.
   * **[!UICONTROL Account Types]**: Indiquez l’ensemble complet des types de compte pour cette société. Aucun type de compte n’est mutuellement exclusif avec un autre type.
      * **[!UICONTROL Full AAM]**: Indiquez que l’entreprise dispose d’un compte Adobe Audience Manager complet et que les utilisateurs disposent d’un accès de connexion.
      * **[!UICONTROL MMP]**: Indiquez que l’entreprise a été autorisée à utiliser les fonctionnalités du profil marketing par Principal ([!UICONTROL MMP]).

         Si vous sélectionnez ce type de compte, **[!UICONTROL Visitor ID Service]** est également automatiquement sélectionné.
Pour plus d’informations, voir [Audiences Experience Cloud](https://experienceleague.adobe.com/docs/core-services/interface/services/audiences/audience-library.html?lang=en).
   * **[!UICONTROL Data Source]**: Indiquez que la société est un fournisseur de données tiers dans Audience Manager.
   * **[!UICONTROL Targeting Partner]**: Indiquez que l’entreprise agit comme une plateforme de ciblage pour les clients d’Audience Manager.
   * **[!UICONTROL Visitor ID Service]**: Indiquez que l’entreprise a été activée pour utiliser le service d’identification des visiteurs Experience Cloud.

      Le service d’identifiant visiteur Experience Cloud fournit un identifiant visiteur universel pour toutes les solutions Experience Cloud. Pour plus d’informations, consultez le [guide d’utilisation du service d’ID Experience Cloud](https://experienceleague.adobe.com/docs/id-service/using/home.html?lang=en).

   * **[!UICONTROL Agency]**: Indiquez que la société aura un compte de l’Agence.
   * **[!UICONTROL Features]**: Sélectionnez les options souhaitées:
      * **[!UICONTROL Password Expiration]**: Définit tous les mots de passe utilisateur de cette société pour qu’ils expirent après 90 jours afin d’accroître la sécurité de l’Audience Manager.
      * **[!UICONTROL Reporting]**: Permet d’activer la création de rapports d’Audience Manager pour cette entreprise.
      * **[!UICONTROL Role Based Access Controls]**: Activez les contrôles d’accès en fonction du rôle pour cette entreprise. Les contrôles d’accès en fonction du rôle vous permettent de créer des groupes d’utilisateurs avec des autorisations d’accès différentes. Les utilisateurs individuels de ces groupes ne peuvent alors accéder qu’à des fonctionnalités spécifiques de l’Audience Manager.


1. Cliquez sur **[!UICONTROL Submit Updates]**.

## Suppression d’un profil d’entreprise {#delete-company-profile}

Utilisez la page [!UICONTROL Companies] de l’outil Audience Manager [!UICONTROL Admin] pour supprimer une société existante.

<!-- t_delete_company.xml -->

>[!NOTE]
>
>Vous devez avoir le rôle [!UICONTROL DEXADMIN] pour pouvoir supprimer les entreprises existantes.

1. Pour supprimer une société existante, cliquez sur **[!UICONTROL Companies]**.

   ![Résultat de l’étape](assets/companies.png)

1. Cliquez sur ![](assets/icon_delete.png) dans la colonne **[!UICONTROL Actions]** de la société souhaitée.
1. Cliquez sur **[!UICONTROL OK]** pour confirmer la suppression.
