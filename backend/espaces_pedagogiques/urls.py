from django.urls import path
from . import views

app_name = 'espaces_pedagogiques'

urlpatterns = [
    # Epic 1: Création d'un espace pédagogique vide
    path('espaces/', views.lister_espaces_pedagogiques, name='lister_espaces'),
    path('espaces/creer/', views.creer_espace_pedagogique, name='creer_espace'),
    path('espaces/<int:espace_id>/', views.detail_espace_pedagogique, name='detail_espace'),
    
    # Epic 2: Insertion d'un formateur dans un espace pédagogique
    path('espaces/<int:espace_id>/ajouter-formateur/', views.ajouter_formateur_espace, name='ajouter_formateur'),
    
    # Gestion des formateurs
    path('formateurs/', views.lister_formateurs, name='lister_formateurs'),
    path('formateurs/creer/', views.creer_formateur, name='creer_formateur'),
    
    # Gestion des promotions
    path('promotions/', views.lister_promotions, name='lister_promotions'),
    path('promotions/creer/', views.creer_promotion, name='creer_promotion'),
    path('promotions/<int:promotion_id>/', views.detail_promotion, name='detail_promotion'),
    path('promotions/<int:promotion_id>/ajouter-espace/', views.ajouter_espace_promotion, name='ajouter_espace_promotion'),
    path('promotions/<int:promotion_id>/ajouter-etudiant/', views.ajouter_etudiant_promotion, name='ajouter_etudiant_promotion'),
    
    # Gestion des étudiants
    path('etudiants/', views.lister_etudiants, name='lister_etudiants'),
    path('etudiants/creer/', views.creer_etudiant, name='creer_etudiant'),
    path('espaces/ajouter-etudiant/', views.ajouter_etudiant_espace, name='ajouter_etudiant'),
    
    # Gestion des travaux individuels
    path('travaux/', views.lister_travaux_individuels, name='lister_travaux'),
    path('travaux/creer/', views.creer_travail_individuel, name='creer_travail'),
    path('espaces/<int:espace_id>/travaux/', views.travaux_par_espace, name='travaux_par_espace'),
    
    # Gestion des livraisons
    path('livraisons/', views.lister_livraisons, name='lister_livraisons'),
    path('livraisons/soumettre/', views.soumettre_livraison, name='soumettre_livraison'),
    path('etudiants/<int:etudiant_id>/livraisons/', views.livraisons_par_etudiant, name='livraisons_par_etudiant'),
    path('travaux/<int:travail_id>/livraisons/', views.livraisons_par_travail, name='livraisons_par_travail'),
    
    # Gestion des assignations de travail
    path('travaux/assigner/', views.assigner_travail_etudiant, name='assigner_travail'),
    path('etudiants/<int:etudiant_id>/travaux-assignes/', views.travaux_assignes_etudiant, name='travaux_assignes_etudiant'),
    path('espaces/<int:espace_id>/travaux-assignes/', views.travaux_assignes_formateur, name='travaux_assignes_formateur'),
    path('etudiants/<int:etudiant_id>/travaux-par-formateur/', views.travaux_par_etudiant_formateur, name='travaux_par_etudiant_formateur'),
    path('assignations/<int:assignation_id>/mettre-a-jour/', views.mettre_a_jour_assignation, name='mettre_a_jour_assignation'),
    
    # Gestion des évaluations de livraisons
    path('livraisons/<int:livraison_id>/evaluer/', views.evaluer_livraison, name='evaluer_livraison'),
    path('travaux/<int:travail_id>/livraisons-a-evaluer/', views.livraisons_a_evaluer_par_travail, name='livraisons_a_evaluer'),
    path('etudiants/<int:etudiant_id>/notes/', views.notes_etudiant, name='notes_etudiant'),
    path('etudiants/<int:etudiant_id>/travaux/<int:travail_id>/notes/', views.notes_par_travail_etudiant, name='notes_par_travail_etudiant'),
]
