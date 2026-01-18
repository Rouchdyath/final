#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from pathlib import Path

# Répertoire frontend
frontend_dir = r"c:\Users\LENOVO\Documents\genie logiciel\projet_SIL3\frontend"

# Script pour initialiser les données de démo
init_script = """
// Initialiser les données de démo si pas déjà fait
if (!localStorage.getItem('demo_initialized_v2')) {
    // Promotions
    const promotions = [
        {
            id: '1001',
            nom: 'Licence 3 Informatique 2024-2025',
            code: 'L3INFO2024',
            niveau: 'L3',
            dateDebut: '2024-09-01',
            dateFin: '2025-05-31',
            description: 'Licence Informatique 3e année',
            etudiants: [],
            formateurs: [],
            dateCreation: '2024-01-15'
        },
        {
            id: '1002',
            nom: 'Master 1 IA 2024-2025',
            code: 'M1IA2024',
            niveau: 'M1',
            dateDebut: '2024-09-01',
            dateFin: '2025-08-31',
            description: 'Master Intelligence Artificielle',
            etudiants: [],
            formateurs: [],
            dateCreation: '2024-01-20'
        }
    ];
    localStorage.setItem('promotions', JSON.stringify(promotions));
    localStorage.setItem('demo_initialized_v2', 'true');
    console.log('Demo data initialized with promotions');
}
"""

html_files = [
    'index.html',
    'creer-promotion.html',
    'liste-promotions.html',
    'ajouter-etudiant-promotion.html',
    'creer-etudiant.html',
    'liste-etudiants.html'
]

updated_count = 0
for filename in html_files:
    filepath = os.path.join(frontend_dir, filename)
    if not os.path.exists(filepath):
        continue
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'demo_initialized_v2' not in content:
            new_content = content.replace(
                '</body>',
                f'<script>{init_script}</script></body>'
            )
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_count += 1
            print(f"✅ {filename}")
    except Exception as e:
        print(f"❌ {filename}: {e}")

print(f"\n✅ {updated_count} fichiers mis à jour")

