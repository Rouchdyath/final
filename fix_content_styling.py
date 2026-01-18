#!/usr/bin/env python3
"""
Fix content wrapper styling on all restructured pages.
Replaces old margin-based layout with proper grid-based layout.
"""

import os
import re

FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "frontend")

# Pages to fix (excluding public pages)
PAGES_TO_FIX = [
    "ajouter-etudiant-espace.html",
    "ajouter-etudiant-promotion.html",
    "ajouter-formateur.html",
    "ajouter_etudiant.html",
    "assigner-travail.html",
    "consultation-directeur-espaces.html",
    "consultation-directeur-etudiants.html",
    "consultation-directeur-promotions.html",
    "consultation-formateur-travaux.html",
    "cree_espaces.html",
    "creer-espace.html",
    "creer-etudiant.html",
    "creer-formateur.html",
    "creer-promotion.html",
    "creer-travail.html",
    "espace.html",
    "evaluer-livraisons.html",
    "liste-espaces.html",
    "liste-etudiants.html",
    "liste-promotions.html",
    "liste-travaux.html",
    "liste_membre.html",
    "listes_espaces.html",
    "mes-notes.html",
    "soumettre-livraison.html",
]

# New CSS styles
NEW_STYLES = """    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html, body {
            width: 100%;
            height: 100%;
            background: #f5f7fa;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
        }

        .page-wrapper {
            display: grid;
            grid-template-columns: 300px 1fr;
            width: 100%;
            height: 100%;
            min-height: 100vh;
        }

        .sidebar-wrapper {
            background: white;
            box-shadow: 2px 0 10px rgba(0, 0, 0, 0.08);
            position: fixed;
            left: 0;
            top: 0;
            width: 300px;
            height: 100vh;
            overflow-y: auto;
            z-index: 100;
        }

        .content-wrapper {
            grid-column: 2;
            margin-left: 0;
            padding: 30px 40px;
            width: 100%;
            overflow-y: auto;
            background: #f5f7fa;
        }

        .content-header {
            background: white;
            padding: 30px;
            border-radius: 8px;
            margin-bottom: 30px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        }

        .content-header h1 {
            color: #2c3e50;
            font-size: 28px;
            margin: 0;
            font-weight: 700;
        }

        .content-header p {
            color: #666;
            margin: 10px 0 0 0;
            font-size: 14px;
        }

        .content-main {
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        }

        .content-main h2 {
            color: #2c3e50;
            font-size: 24px;
            margin: 0 0 20px 0;
            font-weight: 600;
        }

        .content-main h3 {
            color: #34495e;
            font-size: 18px;
            margin: 30px 0 15px 0;
            font-weight: 600;
        }

        .content-main p {
            color: #666;
            line-height: 1.6;
            margin: 0 0 15px 0;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            color: #333;
            font-weight: 500;
            margin-bottom: 8px;
        }

        .form-group input,
        .form-group select,
        .form-group textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
            font-family: inherit;
        }

        .form-group input:focus,
        .form-group select:focus,
        .form-group textarea:focus {
            outline: none;
            border-color: #3498db;
            box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        table th {
            background: #f0f0f0;
            color: #2c3e50;
            padding: 12px;
            text-align: left;
            font-weight: 600;
            border-bottom: 2px solid #ddd;
        }

        table td {
            padding: 12px;
            border-bottom: 1px solid #eee;
        }

        table tr:hover {
            background: #f9f9f9;
        }

        .btn {
            display: inline-block;
            padding: 10px 20px;
            background: #3498db;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 500;
            font-size: 14px;
            transition: all 0.3s ease;
        }

        .btn:hover {
            background: #2980b9;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
        }

        .btn-danger {
            background: #e74c3c;
        }

        .btn-danger:hover {
            background: #c0392b;
        }

        .btn-success {
            background: #27ae60;
        }

        .btn-success:hover {
            background: #229954;
        }

        @media (max-width: 768px) {
            .page-wrapper {
                grid-template-columns: 1fr;
            }

            .sidebar-wrapper {
                width: 100%;
                height: auto;
                position: relative;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
            }

            .content-wrapper {
                grid-column: 1;
                margin-left: 0;
                padding: 20px;
            }

            .content-header {
                padding: 20px;
            }

            .content-main {
                padding: 20px;
            }
        }

        .sidebar-wrapper::-webkit-scrollbar {
            width: 8px;
        }

        .sidebar-wrapper::-webkit-scrollbar-track {
            background: #f0f0f0;
        }

        .sidebar-wrapper::-webkit-scrollbar-thumb {
            background: #bbb;
            border-radius: 4px;
        }
    </style>"""

def fix_page_styles(filepath):
    """Fix CSS in a single page."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the old styles section
        # Look for <style> tags and replace content between them
        style_pattern = r'<style>.*?</style>'
        
        if re.search(style_pattern, content, re.DOTALL):
            content = re.sub(style_pattern, NEW_STYLES, content, count=1, flags=re.DOTALL)
        else:
            # If no style tag, we need to add one before </head>
            if '</head>' in content:
                content = content.replace('</head>', f'{NEW_STYLES}\n    </head>')
        
        # Also fix margin-left: 300px to margin-left: 0 if still present
        content = content.replace('margin-left: 300px', 'margin-left: 0')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"❌ Error fixing {filepath}: {e}")
        return False

def main():
    fixed = 0
    failed = 0
    
    for page in PAGES_TO_FIX:
        filepath = os.path.join(FRONTEND_DIR, page)
        if os.path.exists(filepath):
            print(f"Fixing: {page}...", end=" ")
            if fix_page_styles(filepath):
                print("✅")
                fixed += 1
            else:
                print("❌")
                failed += 1
        else:
            print(f"⚠️  Skipped: {page} (not found)")
    
    print(f"\n✅ Done! Fixed {fixed} pages, {failed} failed")

if __name__ == "__main__":
    main()
