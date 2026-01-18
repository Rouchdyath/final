"""
Commande Django pour initialiser la base de données avec des données de test
Usage: python manage.py init_data
"""
from django.core.management.base import BaseCommand
from espaces_pedagogiques.models import EspacePedagogique, Formateur, Etudiant, TravailIndividuel, Livraison
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Initialise la base de données avec des données de test'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Initialisation de la base de donnees...'))
        
        # Créer des formateurs de test
        formateurs_data = [
            {
                'nom': 'Martin',
                'prenom': 'Jean',
                'email': 'jean.martin@univ.fr',
                'telephone': '+33 6 12 34 56 78'
            },
            {
                'nom': 'Dubois',
                'prenom': 'Marie',
                'email': 'marie.dubois@univ.fr',
                'telephone': '+33 6 23 45 67 89'
            },
            {
                'nom': 'Bernard',
                'prenom': 'Pierre',
                'email': 'pierre.bernard@univ.fr',
                'telephone': '+33 6 34 56 78 90'
            },
        ]
        
        formateurs_crees = []
        for formateur_data in formateurs_data:
            formateur, created = Formateur.objects.get_or_create(
                email=formateur_data['email'],
                defaults=formateur_data
            )
            if created:
                formateurs_crees.append(formateur)
                self.stdout.write(
                    self.style.SUCCESS(f'  [OK] Formateur cree: {formateur.prenom} {formateur.nom}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'  [INFO] Formateur existe deja: {formateur.prenom} {formateur.nom}')
                )
        
        # Créer des espaces pédagogiques de test
        espaces_data = [
            {
                'nom': 'Groupe 1',
                'matiere': 'Base de Donnees',
                'code': 'BD-SIL3',
                'description': 'Cours de base de donnees avancees'
            },
            {
                'nom': 'Groupe 2',
                'matiere': 'Genie Logiciel',
                'code': 'GL-SIL3',
                'description': 'Cours de genie logiciel pour la troisieme annee'
            },
            {
                'nom': 'Groupe 3',
                'matiere': 'Reseaux et Securite',
                'code': 'RS-SIL3',
                'description': 'Cours sur les reseaux informatiques et la securite'
            },
        ]
        
        espaces_crees = []
        for espace_data in espaces_data:
            espace, created = EspacePedagogique.objects.get_or_create(
                code=espace_data['code'],
                defaults=espace_data
            )
            if created:
                espaces_crees.append(espace)
                self.stdout.write(
                    self.style.SUCCESS(f'  [OK] Espace cree: {espace.matiere} ({espace.code})')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'  [INFO] Espace existe deja: {espace.matiere} ({espace.code})')
                )
        
        # Assigner des formateurs aux espaces
        if espaces_crees and formateurs_crees:
            # Assigner le premier formateur au premier espace
            if len(espaces_crees) > 0 and len(formateurs_crees) > 0:
                espaces_crees[0].formateurs.add(formateurs_crees[0])
                self.stdout.write(
                    self.style.SUCCESS(
                        f'  [OK] Formateur {formateurs_crees[0].prenom} {formateurs_crees[0].nom} '
                        f'assigne a {espaces_crees[0].nom} - {espaces_crees[0].matiere}'
                    )
                )
            
            # Assigner le deuxième formateur au deuxième espace
            if len(espaces_crees) > 1 and len(formateurs_crees) > 1:
                espaces_crees[1].formateurs.add(formateurs_crees[1])
                self.stdout.write(
                    self.style.SUCCESS(
                        f'  [OK] Formateur {formateurs_crees[1].prenom} {formateurs_crees[1].nom} '
                        f'assigne a {espaces_crees[1].nom} - {espaces_crees[1].matiere}'
                    )
                )
        
        # Créer des étudiants de test
        etudiants_data = [
            {
                'nom': 'Dupont',
                'prenom': 'Alice',
                'email': 'alice.dupont@etudiant.univ.fr',
                'telephone': '+33 6 45 67 89 01'
            },
            {
                'nom': 'Leroy',
                'prenom': 'Bob',
                'email': 'bob.leroy@etudiant.univ.fr',
                'telephone': '+33 6 56 78 90 12'
            },
            {
                'nom': 'Moreau',
                'prenom': 'Claire',
                'email': 'claire.moreau@etudiant.univ.fr',
                'telephone': '+33 6 67 89 01 23'
            },
        ]
        
        etudiants_crees = []
        for etudiant_data in etudiants_data:
            etudiant, created = Etudiant.objects.get_or_create(
                email=etudiant_data['email'],
                defaults=etudiant_data
            )
            if created:
                etudiants_crees.append(etudiant)
                self.stdout.write(
                    self.style.SUCCESS(f'  [OK] Etudiant cree: {etudiant.prenom} {etudiant.nom}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'  [INFO] Etudiant existe deja: {etudiant.prenom} {etudiant.nom}')
                )
        
        # Assigner des étudiants aux espaces
        espaces = EspacePedagogique.objects.all()
        if espaces.exists() and etudiants_crees:
            for espace in espaces:
                for etudiant in etudiants_crees:
                    espace.etudiants.add(etudiant)
                self.stdout.write(
                    self.style.SUCCESS(f'  [OK] Etudiants assignes a {espace.matiere}')
                )
        
        # Créer des travaux individuels de test
        travaux_data = [
            {
                'titre': 'TP Genie Logiciel - Architecture MVC',
                'description': 'Developper une application web utilisant l\'architecture MVC',
                'date_echeance': datetime.now() + timedelta(days=7),
                'espace': espaces.filter(matiere='Genie Logiciel').first()
            },
            {
                'titre': 'Exercice Base de Donnees - Modelisation',
                'description': 'Modeliser une base de donnees pour un systeme de gestion',
                'date_echeance': datetime.now() + timedelta(days=10),
                'espace': espaces.filter(matiere='Base de Donnees').first()
            },
            {
                'titre': 'Rapport Reseaux - Analyse de securite',
                'description': 'Analyser la securite d\'un reseau informatique',
                'date_echeance': datetime.now() + timedelta(days=14),
                'espace': espaces.filter(matiere='Reseaux et Securite').first()
            },
        ]
        
        travaux_crees = []
        for travail_data in travaux_data:
            if travail_data['espace']:
                travail, created = TravailIndividuel.objects.get_or_create(
                    titre=travail_data['titre'],
                    espace=travail_data['espace'],
                    defaults=travail_data
                )
                if created:
                    travaux_crees.append(travail)
                    self.stdout.write(
                        self.style.SUCCESS(f'  [OK] Travail cree: {travail.titre}')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'  [INFO] Travail existe deja: {travail.titre}')
                    )
        
        # Créer des livraisons de test
        if etudiants_crees and travaux_crees:
            livraisons_data = [
                {
                    'etudiant': etudiants_crees[0],
                    'travail': travaux_crees[0],
                    'contenu': 'Voici ma livraison pour le TP Genie Logiciel. J\'ai implemente une architecture MVC basique.'
                },
                {
                    'etudiant': etudiants_crees[1],
                    'travail': travaux_crees[1],
                    'contenu': 'Mon schema de modelisation pour la base de donnees est attache.'
                },
            ]
            
            for livraison_data in livraisons_data:
                livraison, created = Livraison.objects.get_or_create(
                    etudiant=livraison_data['etudiant'],
                    travail=livraison_data['travail'],
                    defaults=livraison_data
                )
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f'  [OK] Livraison creee pour {livraison.etudiant.prenom} {livraison.etudiant.nom}')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'  [INFO] Livraison existe deja pour {livraison.etudiant.prenom} {livraison.etudiant.nom}')
                    )
        
        self.stdout.write(self.style.SUCCESS('\nInitialisation terminee avec succes!'))
        self.stdout.write(self.style.SUCCESS(f'Total: {Formateur.objects.count()} formateur(s) dans la base'))
        self.stdout.write(self.style.SUCCESS(f'Total: {EspacePedagogique.objects.count()} espace(s) pedagogique(s) dans la base'))
        self.stdout.write(self.style.SUCCESS(f'Total: {Etudiant.objects.count()} etudiant(s) dans la base'))
        self.stdout.write(self.style.SUCCESS(f'Total: {TravailIndividuel.objects.count()} travail(s) individuel(s) dans la base'))
        self.stdout.write(self.style.SUCCESS(f'Total: {Livraison.objects.count()} livraison(s) dans la base'))

