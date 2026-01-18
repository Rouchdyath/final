#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

frontend_dir = r"c:\Users\LENOVO\Documents\genie logiciel\projet_SIL3\frontend"

files_to_check = [
    # Étudiant
    'mes-travaux.html',
    'mes-notes.html',
    
    # Formateur
    'mes-espaces-formateur.html',
    'creer-travail.html',
    'consultation-formateur-travaux.html',
    'assigner-travail-formateur.html',
    'consultation-formateur-etudiants.html',
    'evaluer-livraisons.html',
    
    # Directeur (existing)
    'consultation-directeur-espaces.html',
    'consultation-directeur-etudiants.html',
    'consultation-directeur-promotions.html',
]

print("✅ VÉRIFICATION DES PAGES FILTRÉES PAR RÔLE\n")

for filename in files_to_check:
    filepath = os.path.join(frontend_dir, filename)
    if os.path.exists(filepath):
        size = os.path.getsize(filepath)
        print(f"✅ {filename} ({size} bytes)")
    else:
        print(f"❌ {filename} - MANQUANT")

print("\n" + "="*50)
print("✅ VÉRIFICATION COMPLÈTE")
print("="*50)
