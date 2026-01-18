#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to restructure all protected pages with proper sidebar layout
"""

import os
import re
from pathlib import Path

FRONTEND_DIR = Path(__file__).parent / 'frontend'

# Pages that should NOT be modified
SKIP_PAGES = {
    'login.html', 'signup.html', 'test-auth.html', 
    'debug-users.html', 'indes.html', 'index.html',
    'TEMPLATE_PAGE.html'
}

def restructure_page(filepath):
    """Restructure a page with proper sidebar layout"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already restructured
    if 'class="page-wrapper"' in content:
        print(f"⏭️  {filepath.name} already restructured")
        return False
    
    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    title = title_match.group(1) if title_match else 'Page'
    
    # Extract header (if exists)
    header_match = re.search(r'<header>(.*?)</header>', content, re.DOTALL | re.IGNORECASE)
    header_content = header_match.group(1) if header_match else '<h1>Titre de la page</h1>'
    
    # Extract main content (between <main> and </main> or the body content)
    main_match = re.search(r'<main[^>]*>(.*?)</main>', content, re.DOTALL | re.IGNORECASE)
    if main_match:
        main_content = main_match.group(1)
    else:
        # Get content from after header
        body_match = re.search(r'</header>(.*?)(?=</body>)', content, re.DOTALL | re.IGNORECASE)
        main_content = body_match.group(1) if body_match else '<p>Contenu ici...</p>'
    
    # Create new structure
    new_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="styles.css">
    <script src="auth.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            background: #f5f7fa;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
        }}

        .page-wrapper {{
            display: grid;
            grid-template-columns: 300px 1fr;
            min-height: 100vh;
            gap: 0;
        }}

        .sidebar-wrapper {{
            background: white;
            box-shadow: 2px 0 10px rgba(0, 0, 0, 0.08);
            position: fixed;
            left: 0;
            top: 0;
            width: 300px;
            height: 100vh;
            overflow-y: auto;
            z-index: 100;
        }}

        .content-wrapper {{
            margin-left: 300px;
            padding: 30px;
            min-height: 100vh;
        }}

        .content-wrapper header {{
            background: white;
            padding: 25px;
            border-radius: 8px;
            margin-bottom: 30px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        }}

        .content-wrapper header h1 {{
            color: #2c3e50;
            font-size: 28px;
            margin: 0 0 10px 0;
        }}

        .content-wrapper header p {{
            color: #666;
            margin: 0;
        }}

        .content-wrapper h2 {{
            color: #2c3e50;
            font-size: 20px;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #3498db;
        }}

        .content-wrapper > main {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        }}

        @media (max-width: 768px) {{
            .page-wrapper {{
                grid-template-columns: 1fr;
            }}

            .sidebar-wrapper {{
                width: 100%;
                height: auto;
                position: relative;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
            }}

            .content-wrapper {{
                margin-left: 0;
                padding: 20px;
            }}
        }}

        .sidebar-wrapper::-webkit-scrollbar {{
            width: 8px;
        }}

        .sidebar-wrapper::-webkit-scrollbar-track {{
            background: #f0f0f0;
        }}

        .sidebar-wrapper::-webkit-scrollbar-thumb {{
            background: #bbb;
            border-radius: 4px;
        }}

        .sidebar-wrapper::-webkit-scrollbar-thumb:hover {{
            background: #999;
        }}
    </style>
</head>
<body>
    <div class="page-wrapper">
        <!-- Sidebar -->
        <div class="sidebar-wrapper" id="sidebar-wrapper"></div>

        <!-- Contenu -->
        <div class="content-wrapper">
            <header>
                {header_content}
            </header>

            <main>
                {main_content}
            </main>
        </div>
    </div>

    <script src="sidebar.js"></script>
    <script>
        // Rediriger vers login si pas connecté
        window.addEventListener('load', function() {{
            if (!isLoggedIn()) {{
                window.location.href = 'login.html';
            }}
        }});
    </script>
</body>
</html>
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    print(f"✅ {filepath.name} - Restructured")
    return True

def main():
    """Process all HTML files"""
    print("🔄 Restructuring protected pages with sidebar layout...\n")
    
    html_files = sorted(FRONTEND_DIR.glob('*.html'))
    restructured = 0
    skipped = 0
    
    for html_file in html_files:
        # Skip certain pages
        if html_file.name in SKIP_PAGES:
            print(f"⏭️  {html_file.name} (skipped)")
            skipped += 1
            continue
        
        if restructure_page(html_file):
            restructured += 1
        else:
            skipped += 1
    
    print(f"\n✅ Done! Restructured {restructured} pages, skipped {skipped}")

if __name__ == '__main__':
    main()
