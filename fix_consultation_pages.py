#!/usr/bin/env python3
"""
Fix all consultation pages to properly load and display data from localStorage.
"""

import os

FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "frontend")

# Script to load promotions
PROMOTIONS_SCRIPT = """
        window.addEventListener('load', function() {
            if (!isLoggedIn()) {
                window.location.href = 'login.html';
            }
            loadPromotions();
        });

        function loadPromotions() {
            const promotions = JSON.parse(localStorage.getItem('promotions') || '[]');
            const container = document.getElementById('promotions-container') || document.querySelector('.content-main');

            if (!promotions || promotions.length === 0) {
                container.innerHTML = '<p style="text-align: center; color: #999; margin-top: 50px;">Aucune promotion trouvée</p>';
                return;
            }

            const html = `
                <h2>📊 Liste des Promotions</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Nom</th>
                            <th>Code</th>
                            <th>Début</th>
                            <th>Fin</th>
                            <th>Étudiants</th>
                            <th>Formateurs</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${promotions.map(promo => `
                            <tr>
                                <td><strong>${promo.nom}</strong></td>
                                <td>${promo.code}</td>
                                <td>${promo.dateDebut}</td>
                                <td>${promo.dateFin}</td>
                                <td>${promo.etudiants ? promo.etudiants.length : 0}</td>
                                <td>${promo.formateurs ? promo.formateurs.length : 0}</td>
                            </tr>
                        `).join('')}
                    </tbody>
                </table>
            `;

            container.innerHTML = html;
        }
    """

ETUDIANTS_SCRIPT = """
        window.addEventListener('load', function() {
            if (!isLoggedIn()) {
                window.location.href = 'login.html';
            }
            loadEtudiants();
        });

        function loadEtudiants() {
            const users = JSON.parse(localStorage.getItem('app_users') || '[]');
            const etudiants = users.filter(u => u.role === 'etudiant');
            const container = document.getElementById('etudiants-container') || document.querySelector('.content-main');

            if (!etudiants || etudiants.length === 0) {
                container.innerHTML = '<p style="text-align: center; color: #999; margin-top: 50px;">Aucun étudiant trouvé</p>';
                return;
            }

            const html = `
                <h2>👥 Liste des Étudiants</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Identifiant</th>
                            <th>Email</th>
                            <th>Rôle</th>
                            <th>Vérifié</th>
                            <th>Date d'inscription</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${etudiants.map(etudiant => `
                            <tr>
                                <td><strong>${etudiant.identifier}</strong></td>
                                <td>${etudiant.email}</td>
                                <td>👨‍🎓 Étudiant</td>
                                <td>${etudiant.verified ? '✅' : '❌'}</td>
                                <td>${new Date(etudiant.registrationTime).toLocaleDateString('fr-FR')}</td>
                            </tr>
                        `).join('')}
                    </tbody>
                </table>
            `;

            container.innerHTML = html;
        }
    """

def fix_page(filepath, script_content):
    """Fix a consultation page."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already fixed
        if 'loadPromotions()' in content or 'loadEtudiants()' in content:
            return False
        
        # Replace the old script
        old_pattern = """    <script>
        // Rediriger vers login si pas connecté
        window.addEventListener('load', function() {
            if (!isLoggedIn()) {
                window.location.href = 'login.html';
            }
        });
    </script>"""

        if old_pattern in content:
            content = content.replace(old_pattern, f"    <script>\n{script_content}\n    </script>")
        else:
            # Try to find and replace any script section
            import re
            content = re.sub(
                r'<script>\s*//.*?isLoggedIn.*?</script>',
                f'<script>\n{script_content}\n    </script>',
                content,
                flags=re.DOTALL
            )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    pages_config = [
        ('liste-promotions.html', PROMOTIONS_SCRIPT),
        ('liste-etudiants.html', ETUDIANTS_SCRIPT),
    ]

    fixed = 0
    for page, script in pages_config:
        filepath = os.path.join(FRONTEND_DIR, page)
        if os.path.exists(filepath):
            print(f"Fixing: {page}...", end=" ")
            if fix_page(filepath, script):
                print("✅")
                fixed += 1
            else:
                print("⚠️")
        else:
            print(f"⚠️ {page} not found")

    print(f"\n✅ Done! Fixed {fixed} pages")

if __name__ == "__main__":
    main()
