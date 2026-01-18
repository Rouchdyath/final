#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
from pathlib import Path

frontend_path = r"c:\Users\LENOVO\Documents\genie logiciel\projet_SIL3\frontend"

# Liste des fichiers à modifier
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
        
        # Ajouter le script sidebar.js avant </head>
        if 'sidebar.js' not in content:
            content = content.replace('</head>', '<script src="sidebar.js"></script>\n</head>')
            print(f"✓ {filename} - Added sidebar.js")
        
        # Supprimer les éléments <nav>...</nav> avec regex multiline
        content = re.sub(r'<nav>.*?</nav>', '', content, flags=re.DOTALL)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ {filename} - Updated")
        else:
            print(f"  {filename} - No changes")
            
    except Exception as e:
        print(f"❌ {filename} - Error: {e}")

print("\n✅ Mise à jour complète!")
