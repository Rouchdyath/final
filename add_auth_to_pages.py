#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
from pathlib import Path

frontend_path = r"c:\Users\LENOVO\Documents\genie logiciel\projet_SIL3\frontend"

# Liste des fichiers à mettre à jour avec auth.js
files_to_update = [
    "ajouter-etudiant-espace.html",
    "ajouter-etudiant-promotion.html",
    "ajouter-formateur.html",
    "creer-etudiant.html",
    "creer-formateur.html",
    "creer-promotion.html",
    "liste-espaces.html",
    "liste-etudiants.html",
    "liste-promotions.html",
    "liste-travaux.html",
    "soumettre-livraison.html",
    "consultation-directeur-espaces.html",
    "consultation-directeur-etudiants.html",
    "consultation-directeur-promotions.html",
    "assigner-travail.html",
    "creer-travail.html",
    "evaluer-livraisons.html",
    "mes-notes.html",
    "consultation-formateur-travaux.html",
]

for filename in files_to_update:
    file_path = os.path.join(frontend_path, filename)
    
    if not os.path.exists(file_path):
        print(f"❌ {filename} - Not found")
        continue
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Ajouter auth.js avant sidebar.js
        if 'auth.js' not in content and 'sidebar.js' in content:
            content = content.replace('<script src="sidebar.js"></script>', 
                                     '<script src="auth.js"></script>\n    <script src="sidebar.js"></script>')
            print(f"✓ {filename} - Added auth.js")
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ {filename} - Updated")
        else:
            print(f"  {filename} - No changes needed")
            
    except Exception as e:
        print(f"❌ {filename} - Error: {e}")

print("\n✅ Mise à jour complète!")
