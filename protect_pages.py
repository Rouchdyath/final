#!/usr/bin/env python3
"""
Add access control to pages that should only be accessible by directeurs.
"""

import os

FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "frontend")

# Pages that require directeur role
DIRECTEUR_ONLY_PAGES = [
    "creer-espace.html",
    "creer-etudiant.html",
    "creer-formateur.html",
    "creer-promotion.html",
    "ajouter-etudiant-promotion.html",
    "ajouter-formateur.html",
    "ajouter_etudiant.html",
    "consultation-directeur-espaces.html",
    "consultation-directeur-etudiants.html",
    "consultation-directeur-promotions.html",
]

# Pages that require directeur or formateur role (students can't access)
DIRECTOR_OR_FORMATEUR_PAGES = [
    "creer-travail.html",
    "assigner-travail.html",
    "evaluer-livraisons.html",
    "consultation-formateur-travaux.html",
]

ACCESS_CONTROL_CODE = """    <script>
        // Vérifier l'accès à cette page
        window.addEventListener('load', function() {
            const user = getCurrentUser();
            
            if (!isLoggedIn()) {
                window.location.href = 'login.html';
                return;
            }

            // Contrôle d'accès par page
            const pageAccess = {
                'creer-espace.html': ['directeur'],
                'creer-etudiant.html': ['directeur'],
                'creer-formateur.html': ['directeur'],
                'creer-promotion.html': ['directeur'],
                'creer-travail.html': ['directeur'],
                'ajouter-etudiant-promotion.html': ['directeur'],
                'ajouter-formateur.html': ['directeur'],
                'ajouter_etudiant.html': ['directeur'],
                'consultation-directeur-espaces.html': ['directeur'],
                'consultation-directeur-etudiants.html': ['directeur'],
                'consultation-directeur-promotions.html': ['directeur'],
                'assigner-travail.html': ['directeur', 'formateur'],
                'evaluer-livraisons.html': ['directeur', 'formateur'],
                'consultation-formateur-travaux.html': ['directeur', 'formateur']
            };

            const currentPage = window.location.pathname.split('/').pop();
            const allowedRoles = pageAccess[currentPage];

            if (allowedRoles && !allowedRoles.includes(user.role)) {
                document.querySelector('.content-main').innerHTML = `
                    <div class="alert alert-danger" style="padding: 30px; text-align: center; margin-top: 50px;">
                        <h2 style="color: #721c24; margin-bottom: 10px;">❌ Accès Refusé</h2>
                        <p style="color: #721c24; margin-bottom: 20px;">Vous n'avez pas les permissions nécessaires pour accéder à cette page.</p>
                        <p style="color: #999; font-size: 14px; margin-bottom: 20px;">Rôle requis: <strong>${allowedRoles.join(', ')}</strong></p>
                        <p style="color: #999; font-size: 14px;">Votre rôle: <strong>${user.role}</strong></p>
                        <a href="index.html" style="display: inline-block; margin-top: 20px; padding: 10px 20px; background: #3498db; color: white; text-decoration: none; border-radius: 4px;">Retour à l'accueil</a>
                    </div>
                `;
                return;
            }
        });
    </script>"""

def add_access_control(filepath):
    """Add access control to a page."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if access control already exists
        if 'Vérifier l\'accès à cette page' in content:
            print(f"⚠️  Already protected: {os.path.basename(filepath)}")
            return False
        
        # Find the location to insert (before closing </body>)
        if '</body>' in content:
            # Also remove any existing old access control script if present
            content = content.replace("""    <script>
        // Rediriger vers login si pas connecté
        window.addEventListener('load', function() {
            if (!isLoggedIn()) {
                window.location.href = 'login.html';
            }
        });
    </script>""", "")
            
            content = content.replace('</body>', f'{ACCESS_CONTROL_CODE}\n</body>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        return False
    except Exception as e:
        print(f"❌ Error protecting {filepath}: {e}")
        return False

def main():
    protected = 0
    failed = 0
    
    all_protected_pages = DIRECTEUR_ONLY_PAGES + DIRECTOR_OR_FORMATEUR_PAGES
    
    for page in all_protected_pages:
        filepath = os.path.join(FRONTEND_DIR, page)
        if os.path.exists(filepath):
            print(f"Protecting: {page}...", end=" ")
            if add_access_control(filepath):
                print("✅")
                protected += 1
            else:
                print("⚠️")
        else:
            print(f"⚠️  Skipped: {page} (not found)")
    
    print(f"\n✅ Done! Protected {protected} pages")

if __name__ == "__main__":
    main()
