"""
URL configuration for backend project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from .views import api_root

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/', include('espaces_pedagogiques.urls')),
    
    # ===== PAGES PRINCIPALES =====
    path('frontend/', TemplateView.as_view(template_name='index.html'), name='frontend'),
    path('Index.html', TemplateView.as_view(template_name='index.html'), name='index-html'),
    path('index.html', TemplateView.as_view(template_name='index.html'), name='index'),
    path('index', TemplateView.as_view(template_name='index.html'), name='index-path'),
    
    # ===== AUTHENTIFICATION =====
    path('login.html', TemplateView.as_view(template_name='login.html'), name='login-html'),
    path('login', TemplateView.as_view(template_name='login.html'), name='login'),
    path('signup.html', TemplateView.as_view(template_name='signup.html'), name='signup-html'),
    path('signup', TemplateView.as_view(template_name='signup.html'), name='signup'),
    
    # ===== PAGES ÉTUDIANT =====
    path('liste-travaux.html', TemplateView.as_view(template_name='liste-travaux.html'), name='liste-travaux-html'),
    path('liste-travaux', TemplateView.as_view(template_name='liste-travaux.html'), name='liste-travaux'),
    path('soumettre-livraison.html', TemplateView.as_view(template_name='soumettre-livraison.html'), name='soumettre-livraison-html'),
    path('soumettre-livraison', TemplateView.as_view(template_name='soumettre-livraison.html'), name='soumettre-livraison'),
    path('mes-notes.html', TemplateView.as_view(template_name='mes-notes.html'), name='mes-notes-html'),
    path('mes-notes', TemplateView.as_view(template_name='mes-notes.html'), name='mes-notes'),
    
    # ===== PAGES ESPACE =====
    path('espace.html', TemplateView.as_view(template_name='espace.html'), name='espace-html'),
    path('espace', TemplateView.as_view(template_name='espace.html'), name='espace'),
    path('creer-espace.html', TemplateView.as_view(template_name='creer-espace.html'), name='creer-espace-html'),
    path('creer-espace', TemplateView.as_view(template_name='creer-espace.html'), name='creer-espace'),
    path('liste-espaces.html', TemplateView.as_view(template_name='liste-espaces.html'), name='liste-espaces-html'),
    path('liste-espaces', TemplateView.as_view(template_name='liste-espaces.html'), name='liste-espaces'),
    path('listes_espaces.html', TemplateView.as_view(template_name='listes_espaces.html'), name='listes-espaces-old'),
    path('listes-espaces', TemplateView.as_view(template_name='listes_espaces.html'), name='listes-espaces-old-path'),
    path('cree_espaces.html', TemplateView.as_view(template_name='cree_espaces.html'), name='cree-espaces-old'),
    
    # ===== PAGES ÉTUDIANT (GESTION) =====
    path('creer-etudiant.html', TemplateView.as_view(template_name='creer-etudiant.html'), name='creer-etudiant-html'),
    path('creer-etudiant', TemplateView.as_view(template_name='creer-etudiant.html'), name='creer-etudiant'),
    path('liste-etudiants.html', TemplateView.as_view(template_name='liste-etudiants.html'), name='liste-etudiants-html'),
    path('liste-etudiants', TemplateView.as_view(template_name='liste-etudiants.html'), name='liste-etudiants'),
    path('ajouter-etudiant-espace.html', TemplateView.as_view(template_name='ajouter-etudiant-espace.html'), name='ajouter-etudiant-espace-html'),
    path('ajouter-etudiant-espace', TemplateView.as_view(template_name='ajouter-etudiant-espace.html'), name='ajouter-etudiant-espace'),
    path('ajouter-etudiant-promotion.html', TemplateView.as_view(template_name='ajouter-etudiant-promotion.html'), name='ajouter-etudiant-promotion-html'),
    path('ajouter-etudiant-promotion', TemplateView.as_view(template_name='ajouter-etudiant-promotion.html'), name='ajouter-etudiant-promotion'),
    path('ajouter_etudiant.html', TemplateView.as_view(template_name='ajouter_etudiant.html'), name='ajouter-etudiant-old'),
    path('liste_membre.html', TemplateView.as_view(template_name='liste_membre.html'), name='liste-membre-old'),
    
    # ===== PAGES FORMATEUR =====
    path('creer-formateur.html', TemplateView.as_view(template_name='creer-formateur.html'), name='creer-formateur-html'),
    path('creer-formateur', TemplateView.as_view(template_name='creer-formateur.html'), name='creer-formateur'),
    path('ajouter-formateur.html', TemplateView.as_view(template_name='ajouter-formateur.html'), name='ajouter-formateur-html'),
    path('ajouter-formateur', TemplateView.as_view(template_name='ajouter-formateur.html'), name='ajouter-formateur'),
    
    # ===== PAGES PROMOTION =====
    path('creer-promotion.html', TemplateView.as_view(template_name='creer-promotion.html'), name='creer-promotion-html'),
    path('creer-promotion', TemplateView.as_view(template_name='creer-promotion.html'), name='creer-promotion'),
    path('liste-promotions.html', TemplateView.as_view(template_name='liste-promotions.html'), name='liste-promotions-html'),
    path('liste-promotions', TemplateView.as_view(template_name='liste-promotions.html'), name='liste-promotions'),
    
    # ===== PAGES TRAVAUX =====
    path('creer-travail.html', TemplateView.as_view(template_name='creer-travail.html'), name='creer-travail-html'),
    path('creer-travail', TemplateView.as_view(template_name='creer-travail.html'), name='creer-travail'),
    path('assigner-travail.html', TemplateView.as_view(template_name='assigner-travail.html'), name='assigner-travail-html'),
    path('assigner-travail', TemplateView.as_view(template_name='assigner-travail.html'), name='assigner-travail'),
    path('evaluer-livraisons.html', TemplateView.as_view(template_name='evaluer-livraisons.html'), name='evaluer-livraisons-html'),
    path('evaluer-livraisons', TemplateView.as_view(template_name='evaluer-livraisons.html'), name='evaluer-livraisons'),
    
    # ===== PAGES CONSULTATION DIRECTEUR =====
    path('consultation-directeur-espaces.html', TemplateView.as_view(template_name='consultation-directeur-espaces.html'), name='consultation-directeur-espaces-html'),
    path('consultation-directeur-espaces', TemplateView.as_view(template_name='consultation-directeur-espaces.html'), name='consultation-directeur-espaces'),
    path('consultation-directeur-etudiants.html', TemplateView.as_view(template_name='consultation-directeur-etudiants.html'), name='consultation-directeur-etudiants-html'),
    path('consultation-directeur-etudiants', TemplateView.as_view(template_name='consultation-directeur-etudiants.html'), name='consultation-directeur-etudiants'),
    path('consultation-directeur-promotions.html', TemplateView.as_view(template_name='consultation-directeur-promotions.html'), name='consultation-directeur-promotions-html'),
    path('consultation-directeur-promotions', TemplateView.as_view(template_name='consultation-directeur-promotions.html'), name='consultation-directeur-promotions'),
    
    # ===== PAGES CONSULTATION FORMATEUR =====
    path('consultation-formateur-travaux.html', TemplateView.as_view(template_name='consultation-formateur-travaux.html'), name='consultation-formateur-travaux-html'),
    path('consultation-formateur-travaux', TemplateView.as_view(template_name='consultation-formateur-travaux.html'), name='consultation-formateur-travaux'),
    
    # ===== PAGE TEST =====
    path('test-auth.html', TemplateView.as_view(template_name='test-auth.html'), name='test-auth-html'),
    path('test-auth', TemplateView.as_view(template_name='test-auth.html'), name='test-auth'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT or settings.STATICFILES_DIRS[0])

