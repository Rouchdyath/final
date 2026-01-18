# Script PowerShell pour ajouter sidebar.js et supprimer les anciens menus

$frontendPath = "c:\Users\LENOVO\Documents\genie logiciel\projet_SIL3\frontend"
$htmlFiles = Get-ChildItem -Path $frontendPath -Filter "*.html" -Exclude "index.html"

foreach ($file in $htmlFiles) {
    Write-Host "Traitement: $($file.Name)"
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    
    # Ajouter sidebar.js
    if ($content -notmatch 'sidebar.js') {
        $newLine = '<script src="sidebar.js"></script>' + [Environment]::NewLine + '</head>'
        $content = $content -replace '</head>', $newLine
    }
    
    # Supprimer les anciens menus nav
    $content = [System.Text.RegularExpressions.Regex]::Replace($content, '<nav>.*?</nav>', '', [System.Text.RegularExpressions.RegexOptions]::Singleline)
    
    Set-Content $file.FullName -Value $content -Encoding UTF8
    Write-Host "  OK"
}

Write-Host "Done!"

