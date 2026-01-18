#!/usr/bin/env python3
"""
Initialise la base de données localStorage avec des données de démonstration
pour que toutes les pages de consultation s'affichent correctement.
"""

import os

FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "frontend")

# Script d'initialisation des données de démonstration
INIT_SCRIPT = """
// Initialiser les données de démonstration si elles n'existent pas
function initializeDemoData() {
    // Vérifier si les données existent déjà
    if (localStorage.getItem('demo_initialized') === 'true') {
        return;
    }

    // Créer les espaces pédagogiques
    const espacesData = [
        {
            id: 'espace-1',
            matiere: 'Mathématiques Avancées',
            code: 'MATH-101',
            description: 'Cours de mathématiques niveau licence',
            formateurs: ['formateur@institution.fr'],
            etudiants: ['etudiant1@institution.fr', 'etudiant2@institution.fr', 'etudiant3@institution.fr'],
            dateCreation: new Date().toISOString()
        },
        {
            id: 'espace-2',
            matiere: 'Programmation Python',
            code: 'INFO-201',
            description: 'Introduction à la programmation avec Python',
            formateurs: ['formateur@institution.fr'],
            etudiants: ['etudiant1@institution.fr', 'etudiant4@institution.fr', 'etudiant5@institution.fr'],
            dateCreation: new Date().toISOString()
        },
        {
            id: 'espace-3',
            matiere: 'Physique Générale',
            code: 'PHYS-101',
            description: 'Mécanique et thermodynamique',
            formateurs: ['formateur2@institution.fr'],
            etudiants: ['etudiant2@institution.fr', 'etudiant3@institution.fr', 'etudiant6@institution.fr'],
            dateCreation: new Date().toISOString()
        }
    ];

    // Créer les travaux
    const travauxData = [
        {
            id: 'travail-1',
            titre: 'Équations Différentielles',
            description: 'Résoudre 10 équations différentielles du premier ordre',
            espaceId: 'espace-1',
            formateur: 'formateur@institution.fr',
            dateEchéance: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
            dateCreation: new Date().toISOString(),
            statut: 'actif',
            fichier: 'exam_math.pdf'
        },
        {
            id: 'travail-2',
            titre: 'Projet Python: Gestion d\\'Inventaire',
            description: 'Créer une application de gestion d\'inventaire en Python',
            espaceId: 'espace-2',
            formateur: 'formateur@institution.fr',
            dateEchéance: new Date(Date.now() + 14 * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
            dateCreation: new Date().toISOString(),
            statut: 'actif',
            fichier: 'project_description.pdf'
        },
        {
            id: 'travail-3',
            titre: 'TP Mécanique: Pendule Simple',
            description: 'Étude expérimentale du pendule simple et analyse des résultats',
            espaceId: 'espace-3',
            formateur: 'formateur2@institution.fr',
            dateEchéance: new Date(Date.now() + 3 * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
            dateCreation: new Date().toISOString(),
            statut: 'actif',
            fichier: 'tp_protocol.pdf'
        },
        {
            id: 'travail-4',
            titre: 'Dérivées et Intégrales',
            description: 'Exercices sur les dérivées et intégrales',
            espaceId: 'espace-1',
            formateur: 'formateur@institution.fr',
            dateEchéance: new Date(Date.now() + 10 * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
            dateCreation: new Date().toISOString(),
            statut: 'actif',
            fichier: 'exercises.pdf'
        },
        {
            id: 'travail-5',
            titre: 'Quiz Python',
            description: 'Quiz sur les bases de la programmation Python',
            espaceId: 'espace-2',
            formateur: 'formateur@institution.fr',
            dateEchéance: new Date(Date.now() + 5 * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
            dateCreation: new Date().toISOString(),
            statut: 'actif',
            fichier: 'quiz.pdf'
        }
    ];

    // Créer les livraisons
    const livraisonsData = [
        {
            id: 'livraison-1',
            travailId: 'travail-1',
            etudiantId: 'etudiant1',
            statut: 'soumise',
            fichier: 'solution_1.pdf',
            dateRemise: new Date().toISOString(),
            remarques: 'Travail complet',
            note: 18
        },
        {
            id: 'livraison-2',
            travailId: 'travail-1',
            etudiantId: 'etudiant2',
            statut: 'soumise',
            fichier: 'solution_2.pdf',
            dateRemise: new Date().toISOString(),
            remarques: 'Bon travail, quelques erreurs',
            note: 15
        },
        {
            id: 'livraison-3',
            travailId: 'travail-2',
            etudiantId: 'etudiant1',
            statut: 'en_cours',
            fichier: 'project_progress.py',
            dateRemise: null,
            remarques: '',
            note: null
        },
        {
            id: 'livraison-4',
            travailId: 'travail-3',
            etudiantId: 'etudiant2',
            statut: 'soumise',
            fichier: 'report.pdf',
            dateRemise: new Date().toISOString(),
            remarques: 'Excellent rapport',
            note: 19
        }
    ];

    // Créer les promotions
    const promotionsData = [
        {
            id: 'promotion-1',
            nom: 'Licence 1 - 2024-2025',
            code: 'L1-2024',
            dateDebut: '2024-09-01',
            dateFin: '2025-06-30',
            etudiants: ['etudiant1', 'etudiant2', 'etudiant3', 'etudiant4', 'etudiant5'],
            formateurs: ['formateur', 'formateur2']
        },
        {
            id: 'promotion-2',
            nom: 'Master 1 - 2024-2025',
            code: 'M1-2024',
            dateDebut: '2024-09-01',
            dateFin: '2025-06-30',
            etudiants: ['etudiant6', 'etudiant7'],
            formateurs: ['formateur']
        }
    ];

    // Sauvegarder dans localStorage
    localStorage.setItem('espaces', JSON.stringify(espacesData));
    localStorage.setItem('travaux', JSON.stringify(travauxData));
    localStorage.setItem('livraisons', JSON.stringify(livraisonsData));
    localStorage.setItem('promotions', JSON.stringify(promotionsData));
    localStorage.setItem('demo_initialized', 'true');

    console.log('✅ Données de démonstration initialisées');
}

// Initialiser au chargement
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeDemoData);
} else {
    initializeDemoData();
}
"""

def inject_init_script(filepath):
    """Injecter le script d'initialisation dans une page."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Vérifier si le script est déjà présent
        if 'initializeDemoData' in content:
            return False
        
        # Ajouter le script avant </body>
        if '</body>' in content:
            content = content.replace('</body>', f'    <script>\n{INIT_SCRIPT}\n    </script>\n</body>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    # Injecter dans les pages de consultation principales
    pages = [
        'index.html',
        'liste-travaux.html',
        'liste-espaces.html',
        'liste-promotions.html',
        'liste-etudiants.html',
        'consultation-formateur-travaux.html',
        'consultation-directeur-espaces.html',
        'consultation-directeur-etudiants.html',
        'consultation-directeur-promotions.html',
    ]

    injected = 0
    for page in pages:
        filepath = os.path.join(FRONTEND_DIR, page)
        if os.path.exists(filepath):
            print(f"Injecting in: {page}...", end=" ")
            if inject_init_script(filepath):
                print("✅")
                injected += 1
            else:
                print("⚠️ (Already injected)")
        else:
            print(f"⚠️ {page} not found")

    print(f"\n✅ Done! Injected in {injected} pages")

if __name__ == "__main__":
    main()
