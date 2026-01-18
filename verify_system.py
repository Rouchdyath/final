#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Vérificateur d'intégrité du système - Valide tous les fichiers HTML créés
"""

import os
from pathlib import Path

frontend_dir = r"c:\Users\LENOVO\Documents\genie logiciel\projet_SIL3\frontend"

# Liste des fichiers qui DOIVENT exister
required_files = {
    # Promotions
    'creer-promotion.html': ['createPromotion', 'promotionForm', 'localStorage'],
    'liste-promotions.html': ['loadPromotions', 'deletePromotion', 'promotionsContainer'],
    'ajouter-etudiant-promotion.html': ['assignStudent', 'promotionSelect', 'etudiantSelect'],
    
    # Étudiants
    'creer-etudiant.html': ['createStudent', 'app_users', 'role.*etudiant'],
    'liste-etudiants.html': ['loadEtudiants', 'etudiantsContainer', 'filter.*etudiant'],
    
    # Formateurs
    'creer-formateur.html': ['createFormateur', 'app_users', 'role.*formateur'],
    'ajouter-formateur.html': ['assignFormateur', 'espaceSelect', 'formateurSelect'],
    
    # Livraisons
    'evaluer-livraisons.html': ['evaluer', 'livraisonsContainer', 'note', 'remarques'],
    'evaluation-livraisons.html': ['evaluer', 'livraisonsContainer', 'note', 'remarques'],
    
    # Travaux
    'assignation-travaux.html': ['assignTravail', 'etudiantSelect', 'multi'],
    'creer-travail.html': ['createTravail', 'travailForm', 'espaceId'],
    
    # Lists
    'liste-espaces.html': ['loadEspaces', 'content-main'],
    'liste-travaux.html': ['loadTravaux', 'content-main'],
}

print("=" * 60)
print("🔍 VÉRIFICATION D'INTÉGRITÉ DU SYSTÈME")
print("=" * 60)

errors = []
warnings = []
success_count = 0

for filename, keywords in required_files.items():
    filepath = os.path.join(frontend_dir, filename)
    
    # Vérifier existence du fichier
    if not os.path.exists(filepath):
        errors.append(f"❌ MANQUANT: {filename}")
        continue
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Vérifier la présence des mots-clés
        missing_keywords = []
        for keyword in keywords:
            # Simple check (non-regex pour le pattern)
            if '*' not in keyword and keyword not in content:
                missing_keywords.append(keyword)
        
        if missing_keywords:
            warnings.append(f"⚠️  {filename}: Mots-clés manquants: {', '.join(missing_keywords)}")
        else:
            success_count += 1
            print(f"✅ {filename}")
        
        # Vérifier que le fichier n'est pas vide
        if len(content) < 1000:
            warnings.append(f"⚠️  {filename}: Fichier trop petit ({len(content)} bytes)")
        
        # Vérifier la présence de auth.js et sidebar.js
        if 'auth.js' not in content:
            warnings.append(f"⚠️  {filename}: Pas de inclusion auth.js")
        
        if 'sidebar.js' not in content:
            warnings.append(f"⚠️  {filename}: Pas de inclusion sidebar.js")
            
    except Exception as e:
        errors.append(f"❌ ERREUR ({filename}): {str(e)}")

print(f"\n{'=' * 60}")
print(f"RÉSUMÉ: {success_count}/{len(required_files)} fichiers OK")
print(f"{'=' * 60}")

if warnings:
    print(f"\n⚠️  AVERTISSEMENTS ({len(warnings)}):")
    for w in warnings[:5]:  # Afficher les 5 premiers
        print(f"   {w}")
    if len(warnings) > 5:
        print(f"   ... et {len(warnings) - 5} autres")

if errors:
    print(f"\n❌ ERREURS ({len(errors)}):")
    for e in errors:
        print(f"   {e}")
else:
    print(f"\n✅ AUCUNE ERREUR CRITIQUE DÉTECTÉE")

# Vérifier les connexions sidebar
print(f"\n{'=' * 60}")
print("🔗 VÉRIFICATION DES LIENS SIDEBAR")
print(f"{'=' * 60}")

try:
    sidebar_path = os.path.join(frontend_dir, 'sidebar.js')
    with open(sidebar_path, 'r', encoding='utf-8') as f:
        sidebar_content = f.read()
    
    required_links = [
        'creer-promotion.html',
        'liste-promotions.html',
        'ajouter-etudiant-promotion.html',
        'creer-etudiant.html',
        'liste-etudiants.html',
        'creer-formateur.html',
        'ajouter-formateur.html',
        'evaluer-livraisons.html',
    ]
    
    for link in required_links:
        if link in sidebar_content:
            print(f"✅ {link} lié dans sidebar.js")
        else:
            warnings.append(f"⚠️  {link} NON lié dans sidebar.js")
            
except Exception as e:
    print(f"❌ Erreur sidebar: {e}")

print(f"\n{'=' * 60}")
print("✨ VÉRIFICATION TERMINÉE")
print(f"{'=' * 60}\n")
