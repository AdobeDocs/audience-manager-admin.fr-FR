---
description: Utilisez la page Sociétés de l’outil d’administration des Audiences Manager pour créer une société.
seo-description: Use the Companies page in the Audience Manager Admin tool to create a new company.
seo-title: Create a Company Profile
title: Création d’un profil d’entreprise
uuid: 55de18f8-883d-43fe-b37f-e8805bb92f7a
exl-id: 80bb8a89-0207-4645-ac42-e73cd10561de
source-git-commit: 1f4dbf8f7b36e64c3015b98ef90b6726d0e7495a
workflow-type: tm+mt
source-wordcount: '901'
ht-degree: 2%

---

# Création d’un profil d’entreprise {#create-a-company-profile}

Utilisez la page [!UICONTROL Companies] de l’outil d’administration des Audiences Manager pour créer une société.

<!-- t_create_company.xml -->

>[!NOTE]
>
>Vous devez avoir le rôle **[!UICONTROL DEXADMIN]** pour créer de nouvelles entreprises.

1. Cliquez sur **[!UICONTROL Companies]** > **[!UICONTROL Add Company]**.
1. Renseignez les champs suivants :

   * **[!UICONTROL Name]** : (obligatoire) indiquez le nom de la société.
   * **[!UICONTROL Description]** : (obligatoire) fournissez des informations descriptives sur l’entreprise, telles que son secteur d’activité ou son nom complet.
   * **[!UICONTROL Subdomain]** : (obligatoire) spécifiez le sous-domaine de l’entreprise. Le texte que vous saisissez correspond au sous-domaine de l’appel d’événement. Cela ne peut pas être changé. Il doit s’agir d’une chaîne de caractères [!DNL URL] valides.

     Par exemple, si votre société est nommée [!DNL AcmeCorp], le sous-domaine sera [!DNL acmecorp].

     Audience Manager utilise le sous-domaine pour le serveur de collecte de données [!UICONTROL Data Collection Server] (DCS). Dans l’exemple précédent, si le [!DNL URL] complet de votre entreprise dans [!UICONTROL DCS] est [!DNL acmecorp.demdex.net].

   * **[!UICONTROL Lifecyle]** : spécifiez l’étape souhaitée pour l’entreprise :
      * **[!UICONTROL Active]** : indiquez que la société sera un client d’Audience Manager actif. Un compte [!UICONTROL Active] signifie un client payant, non seulement pour le conseil, mais pour le SKU de l’Audience Manager.
      * **[!UICONTROL Demo]** : indiquez que la société sera réservée à des fins de démonstration. Les données de création de rapports seront automatiquement biffées.
      * **[!UICONTROL Prospect]** : spécifiez que l’entreprise est un client d’Audience Manager potentiel, par exemple une société à qui est fourni un [!DNL POC] gratuit ou une configuration de compte pour une démonstration de vente.
      * **[!UICONTROL Test]** : indiquez que l’entreprise sera uniquement dédiée aux tests internes.

   * **[!UICONTROL Account Types]** : spécifiez l’ensemble complet des types de compte pour cette entreprise. Aucun type de compte n’est mutuellement exclusif avec un autre type.
      * **[!UICONTROL Full AAM]** : indiquez que l’entreprise disposera d’un compte Adobe Audience Manager complet et que les utilisateurs auront un accès de connexion.
      * **[!UICONTROL MMP]** : indiquez que l’entreprise a été autorisée à utiliser les fonctionnalités [!UICONTROL Master Marketing Profile] ([!UICONTROL MMP]). Le [!UICONTROL MMP] permet de partager des audiences à l’échelle de l’Experience Cloud à l’aide d’un [!UICONTROL Experience Cloud ID] ([!DNL MCID]) affecté à chaque visiteur, puis utilisé par l’Audience Manager. Si vous sélectionnez ce type de compte, le [!UICONTROL Experience Cloud ID Service] est également automatiquement sélectionné.

        Pour plus d’informations, voir [Audiences Experience Cloud](https://experienceleague.adobe.com/docs/core-services/interface/services/audiences/audience-library.html?lang=fr).

   * **[!UICONTROL Data Source]** : indiquez que l’entreprise est un fournisseur de données tiers dans Audience Manager.
   * **[!UICONTROL Targeting Partner]** : indiquez que l’entreprise agit comme une plateforme de ciblage pour les clients d’Audience Manager.
   * **[!UICONTROL Visitor ID Service]** : indiquez que l’entreprise a été autorisée à utiliser le [!UICONTROL Experience Cloud Visitor ID Service].

     [!UICONTROL Experience Cloud Visitor ID Service] fournit un identifiant visiteur universel pour toutes les solutions Experience Cloud. Pour plus d’informations, consultez le [guide d’utilisation du service d’identification des visiteurs Experience Cloud](https://experienceleague.adobe.com/docs/id-service/using/intro/overview.html?lang=fr).

   * **[!UICONTROL Agency]** : indiquez que la société aura un compte [!UICONTROL Agency].

1. Cliquez sur **[!UICONTROL Create]**. Poursuivez avec les instructions de la section [Modifier un profil d’entreprise](../companies/admin-manage-company-profiles.md#edit-company-profile).

   ![Résultat de l’étape](assets/add_company.png)

## Modification d’un profil d’entreprise {#edit-company-profile}

Modifiez le profil d’une entreprise, notamment son nom, sa description, son sous-domaine, son cycle de vie, etc.

<!-- t_edit_company_profile.xml -->

1. Cliquez sur **[!UICONTROL Companies]**, puis localisez et cliquez sur la société souhaitée pour afficher sa page [!UICONTROL Profile].

   Utilisez la zone [!UICONTROL Search] ou les commandes de pagination au bas de la liste pour trouver la société souhaitée. Vous pouvez trier chaque colonne par ordre croissant ou décroissant en cliquant sur l’en-tête de la colonne de votre choix.

   ![Résultat de l’étape](assets/profile_company.png)

1. Modifiez les champs selon vos besoins :

   * **[!UICONTROL Name]** : modifiez le nom de la société. Il s’agit d’un champ obligatoire.
   * **[!UICONTROL Description]** : modifiez la description de la société. Il s’agit d’un champ obligatoire.
   * **[!UICONTROL Subdomain]** : (obligatoire) spécifiez le sous-domaine de l’entreprise. Le texte que vous saisissez correspond au sous-domaine de l’appel d’événement. Cela ne peut pas être changé. Il doit s’agir d’une chaîne de caractères [!DNL URL] valides.

     Par exemple, si votre société est nommée [!DNL AcmeCorp], le sous-domaine sera [!DNL acmecorp].

     Audience Manager utilise le sous-domaine pour le serveur de collecte de données [!UICONTROL Data Collection Server] (DCS). Dans l’exemple précédent, si le [!DNL URL] complet de votre entreprise dans [!UICONTROL DCS] est [!DNL acmecorp.demdex.net].

   * **[!UICONTROL imsOrgld]** : ([!UICONTROL Identity Management System Organization ID]) Cet identifiant vous permet de connecter votre entreprise à Adobe Experience Cloud.
   * **[!UICONTROL Lifecyle]** : spécifiez l’étape souhaitée pour l’entreprise :
      * **[!UICONTROL Active]** : indiquez que la société sera un client d’Audience Manager actif. Un compte actif signifie un client payant, non seulement pour consulter, mais aussi pour le SKU de l’Audience Manager.
      * **[!UICONTROL Demo]** : indiquez que la société sera réservée à des fins de démonstration. Les données de création de rapports seront automatiquement biffées.
      * **[!UICONTROL Prospect]** : spécifiez que l’entreprise est un client d’Audience Manager potentiel, par exemple une société à qui est fourni un [!DNL POC] gratuit ou une configuration de compte pour une démonstration de vente.
      * **[!UICONTROL Test]** : indiquez que l’entreprise sera uniquement dédiée aux tests internes.
   * **[!UICONTROL Account Types]** : spécifiez l’ensemble complet des types de compte pour cette entreprise. Aucun type de compte n’est mutuellement exclusif avec un autre type.
      * **[!UICONTROL Full AAM]** : indiquez que l’entreprise disposera d’un compte Adobe Audience Manager complet et que les utilisateurs auront un accès de connexion.
      * **[!UICONTROL MMP]** : indiquez que l’entreprise a été autorisée à utiliser les fonctionnalités Profil marketing de Principal ([!UICONTROL MMP]).

        Si vous sélectionnez ce type de compte, **[!UICONTROL Visitor ID Service]** est également automatiquement sélectionné.
Pour plus d’informations, voir [Audiences Experience Cloud](https://experienceleague.adobe.com/docs/core-services/interface/services/audiences/audience-library.html?lang=fr).

   * **[!UICONTROL Data Source]** : indiquez que l’entreprise est un fournisseur de données tiers dans Audience Manager.
   * **[!UICONTROL Targeting Partner]** : indiquez que l’entreprise agit comme une plateforme de ciblage pour les clients d’Audience Manager.
   * **[!UICONTROL Visitor ID Service]** : indiquez que l’entreprise a été activée pour utiliser le service d’identification des visiteurs Experience Cloud.

     Le service d’identifiant visiteur Experience Cloud fournit un identifiant visiteur universel pour toutes les solutions Experience Cloud. Pour plus d’informations, consultez le [guide d’utilisation du service d’ID Experience Cloud](https://experienceleague.adobe.com/docs/id-service/using/home.html?lang=fr).

   * **[!UICONTROL Agency]** : indiquez que la société aura un compte Agence.
   * **[!UICONTROL Features]** : sélectionnez les options de votre choix :
      * **[!UICONTROL Password Expiration]** : définit tous les mots de passe utilisateur de cette société pour qu’ils expirent après 90 jours afin d’accroître la sécurité de l’Audience Manager.
      * **[!UICONTROL Reporting]** : active la création de rapports d’Audience Manager pour cette entreprise.
      * **[!UICONTROL Role Based Access Controls]** : activez les contrôles d’accès en fonction du rôle pour cette entreprise. Les contrôles d’accès en fonction du rôle vous permettent de créer des groupes d’utilisateurs avec des autorisations d’accès différentes. Les utilisateurs individuels de ces groupes ne peuvent alors accéder qu’à des fonctionnalités spécifiques de l’Audience Manager.

1. Cliquez sur **[!UICONTROL Submit Updates]**.

## Suppression d’un profil d’entreprise {#delete-company-profile}

Utilisez la page [!UICONTROL Companies] de l&#39;outil Audience Manager [!UICONTROL Admin] pour supprimer une société existante.

<!-- t_delete_company.xml -->

>[!NOTE]
>
>Pour supprimer des entreprises existantes, vous devez disposer du rôle [!UICONTROL DEXADMIN] .

1. Pour supprimer une société existante, cliquez sur **[!UICONTROL Companies]**.

   ![Résultat de l’étape](assets/companies.png)

1. Cliquez sur ![](assets/icon_delete.png) dans la colonne **[!UICONTROL Actions]** de la société souhaitée.
1. Cliquez sur **[!UICONTROL OK]** pour confirmer la suppression.
