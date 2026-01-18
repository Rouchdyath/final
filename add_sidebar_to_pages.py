#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add auth check and sidebar to all protected pages
"""

import os
import re
from pathlib import Path

FRONTEND_DIR = Path(__file__).parent / 'frontend'

# Pages that should NOT have sidebar (public pages)
PUBLIC_PAGES = {'login.html', 'signup.html', 'test-auth.html', 'debug-users.html', 'indes.html'}

def add_auth_and_sidebar_to_page(filepath):
    """Add auth check and sidebar container to a page"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if sidebar already exists
    if 'id="sidebar-container"' in content:
        print(f"⏭️  {filepath.name} already has sidebar")
        return False
    
    # Find <head> tag - add auth.js if not present
    if '<script src="auth.js"></script>' not in content:
        head_pattern = r'(</head>)'
        head_match = re.search(head_pattern, content, re.IGNORECASE)
        if head_match:
            auth_script = '    <script src="auth.js"></script>\n    <script src="sidebar.js"></script>\n    '
            insert_pos = head_match.start()
            content = content[:insert_pos] + auth_script + content[insert_pos:]
    
    # Find <body> tag and add redirect + sidebar
    body_pattern = r'(<body[^>]*>)'
    body_match = re.search(body_pattern, content, re.IGNORECASE)
    
    if body_match:
        # Create auth check script
        auth_check = '''
    <div id="sidebar-container"></div>
    <script>
        // Rediriger vers login si pas connecté
        window.addEventListener('load', function() {
            if (!isLoggedIn()) {
                window.location.href = 'login.html';
            }
        });
    </script>
'''
        insert_pos = body_match.end()
        content = content[:insert_pos] + auth_check + content[insert_pos:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ {filepath.name} - Auth + Sidebar added")
        return True
    else:
        print(f"❌ {filepath.name} - Could not find <body> tag")
        return False

def main():
    """Process all HTML files"""
    print("🔄 Adding auth and sidebar to protected pages...\n")
    
    html_files = sorted(FRONTEND_DIR.glob('*.html'))
    added = 0
    skipped = 0
    
    for html_file in html_files:
        # Skip public pages
        if html_file.name in PUBLIC_PAGES:
            print(f"⏭️  {html_file.name} (public page)")
            skipped += 1
            continue
        
        # Skip index.html (already has proper structure)
        if html_file.name == 'index.html':
            print(f"⏭️  {html_file.name} (already configured)")
            skipped += 1
            continue
        
        if add_auth_and_sidebar_to_page(html_file):
            added += 1
        else:
            skipped += 1
    
    print(f"\n✅ Done! Updated {added} pages, skipped {skipped}")

if __name__ == '__main__':
    main()
