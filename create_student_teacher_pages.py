#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

frontend_dir = r"c:\Users\LENOVO\Documents\genie logiciel\projet_SIL3\frontend"

# Pages pour ÉTUDIANT
etudiant_pages = {
    'mes-travaux.html': '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mes Travaux - EduSphère</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html, body { width: 100%; height: 100%; background: #f5f7fa; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
        .page-wrapper { display: grid; grid-template-columns: 300px 1fr; width: 100%; min-height: 100vh; }
        .sidebar-wrapper { background: white; box-shadow: 2px 0 10px rgba(0,0,0,0.08); position: fixed; left: 0; top: 0; width: 300px; height: 100vh; overflow-y: auto; z-index: 100; }
        .content-wrapper { grid-column: 2; padding: 30px 40px; overflow-y: auto; background: #f5f7fa; }
        .content-header { background: white; padding: 30px; border-radius: 8px; margin-bottom: 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        .content-header h1 { color: #2c3e50; font-size: 28px; margin: 0; font-weight: 700; }
        .content-main { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        .travail-card { background: #f9f9f9; padding: 20px; border-radius: 8px; margin-bottom: 20px; border-left: 4px solid #3498db; }
        .travail-card h3 { color: #2c3e50; margin: 0 0 10px 0; }
        .travail-info { color: #666; font-size: 14px; margin: 10px 0; }
        .btn { padding: 10px 20px; background: #3498db; color: white; border: none; border-radius: 4px; cursor: pointer; font-weight: 600; }
        .btn:hover { background: #2980b9; }
        .btn-primary { background: #27ae60; }
        .btn-primary:hover { background: #229954; }
        .empty-state { text-align: center; padding: 60px 30px; color: #999; }
        .badge { display: inline-block; padding: 5px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; }
        .badge-todo { background: #fff3cd; color: #856404; }
        .badge-done { background: #d4edda; color: #155724; }
        @media (max-width: 768px) { .page-wrapper { grid-template-columns: 1fr; } .sidebar-wrapper { width: 100%; height: auto; position: relative; } .content-wrapper { grid-column: 1; padding: 15px; } }
    </style>
</head>
<body>
    <div class="page-wrapper">
        <div id="sidebar-wrapper"></div>
        <div class="content-wrapper">
            <div class="content-header">
                <h1>📖 Mes Travaux</h1>
                <p>Les travaux qui vous ont été assignés</p>
            </div>
            <div class="content-main">
                <div id="travauxContainer"></div>
            </div>
        </div>
    </div>
    <script src="auth.js"></script>
    <script src="sidebar.js"></script>
    <script>
        window.addEventListener('load', function() {
            const user = getCurrentUser();
            if (!isLoggedIn() || user.role !== 'etudiant') {
                window.location.href = 'login.html';
            }
            loadMesTravaux();
        });

        function loadMesTravaux() {
            const user = getCurrentUser();
            const travaux = JSON.parse(localStorage.getItem('travaux') || '[]');
            const espaces = JSON.parse(localStorage.getItem('espaces') || '[]');
            
            // Récupérer les promotions de l'étudiant
            const promotions = JSON.parse(localStorage.getItem('promotions') || '[]');
            const mesTravaux = [];
            
            travaux.forEach(t => {
                if (t.assignations && t.assignations.includes(user.id)) {
                    mesTravaux.push(t);
                }
            });

            let html = '';
            if (mesTravaux.length === 0) {
                html = '<div class="empty-state"><div style="font-size: 80px;">📋</div><h2>Aucun travail assigné</h2><p>Vous verrez vos travaux ici quand on vous les assignera</p></div>';
            } else {
                mesTravaux.forEach(t => {
                    const espace = espaces.find(e => e.id === t.espaceId);
                    const dateEchéance = new Date(t.dateEchéance);
                    const maintenant = new Date();
                    const estEnRetard = maintenant > dateEchéance;
                    const badge = estEnRetard ? '<span class="badge badge-todo">EN RETARD</span>' : '<span class="badge badge-done">À REMETTRE</span>';
                    
                    html += `<div class="travail-card">
                        <h3>${t.titre}</h3>
                        <div class="travail-info">
                            <strong>Espace:</strong> ${espace ? espace.matiere : 'N/A'}
                        </div>
                        <div class="travail-info">
                            <strong>Description:</strong> ${t.description || 'N/A'}
                        </div>
                        <div class="travail-info">
                            <strong>Date d'échéance:</strong> ${dateEchéance.toLocaleDateString('fr-FR')} ${badge}
                        </div>
                        <button class="btn btn-primary" onclick="alert('Soumettre une livraison - À implémenter')">📤 Soumettre ma Livraison</button>
                    </div>`;
                });
            }
            document.getElementById('travauxContainer').innerHTML = html;
        }
    </script>
</body>
</html>''',

    'mes-notes.html': '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mes Notes - EduSphère</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html, body { width: 100%; height: 100%; background: #f5f7fa; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
        .page-wrapper { display: grid; grid-template-columns: 300px 1fr; width: 100%; min-height: 100vh; }
        .sidebar-wrapper { background: white; box-shadow: 2px 0 10px rgba(0,0,0,0.08); position: fixed; left: 0; top: 0; width: 300px; height: 100vh; overflow-y: auto; z-index: 100; }
        .content-wrapper { grid-column: 2; padding: 30px 40px; overflow-y: auto; background: #f5f7fa; }
        .content-header { background: white; padding: 30px; border-radius: 8px; margin-bottom: 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        .content-header h1 { color: #2c3e50; font-size: 28px; margin: 0; font-weight: 700; }
        .content-main { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        table th { background: #f0f0f0; color: #2c3e50; padding: 12px; text-align: left; font-weight: 600; border-bottom: 2px solid #ddd; }
        table td { padding: 12px; border-bottom: 1px solid #eee; }
        table tr:hover { background: #f9f9f9; }
        .note { font-weight: 700; color: #27ae60; font-size: 18px; }
        .empty-state { text-align: center; padding: 60px 30px; color: #999; }
        .stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 30px; }
        .stat-card { background: #f9f9f9; padding: 20px; border-radius: 8px; text-align: center; border-left: 4px solid #3498db; }
        .stat-card h3 { color: #999; font-size: 12px; margin: 0 0 10px 0; }
        .stat-card .value { color: #2c3e50; font-size: 32px; font-weight: 700; }
        @media (max-width: 768px) { .page-wrapper { grid-template-columns: 1fr; } .sidebar-wrapper { width: 100%; height: auto; position: relative; } .content-wrapper { grid-column: 1; padding: 15px; } .stats { grid-template-columns: 1fr; } }
    </style>
</head>
<body>
    <div class="page-wrapper">
        <div id="sidebar-wrapper"></div>
        <div class="content-wrapper">
            <div class="content-header">
                <h1>⭐ Mes Notes</h1>
                <p>Les notes et évaluations de vos travaux</p>
            </div>
            <div class="content-main">
                <div id="statsContainer"></div>
                <div id="notesContainer"></div>
            </div>
        </div>
    </div>
    <script src="auth.js"></script>
    <script src="sidebar.js"></script>
    <script>
        window.addEventListener('load', function() {
            const user = getCurrentUser();
            if (!isLoggedIn() || user.role !== 'etudiant') {
                window.location.href = 'login.html';
            }
            loadMesNotes();
        });

        function loadMesNotes() {
            const user = getCurrentUser();
            const livraisons = JSON.parse(localStorage.getItem('livraisons') || '[]');
            const travaux = JSON.parse(localStorage.getItem('travaux') || '[]');
            
            // Filtrer les livraisons de l'étudiant qui sont évaluées
            const mesNotes = livraisons.filter(l => 
                l.etudiantId === user.id && l.note !== null && l.note !== undefined
            );

            // Statistiques
            let html = '';
            if (mesNotes.length > 0) {
                const moyenne = (mesNotes.reduce((sum, l) => sum + parseFloat(l.note), 0) / mesNotes.length).toFixed(2);
                const meilleureNote = Math.max(...mesNotes.map(l => parseFloat(l.note))).toFixed(2);
                html += `<div class="stats">
                    <div class="stat-card">
                        <h3>Moyenne</h3>
                        <div class="value">${moyenne}/20</div>
                    </div>
                    <div class="stat-card">
                        <h3>Travaux Évalués</h3>
                        <div class="value">${mesNotes.length}</div>
                    </div>
                    <div class="stat-card">
                        <h3>Meilleure Note</h3>
                        <div class="value">${meilleureNote}/20</div>
                    </div>
                </div>`;
            }

            // Tableau des notes
            if (mesNotes.length === 0) {
                html += '<div class="empty-state"><div style="font-size: 80px;">📊</div><h2>Aucune évaluation</h2><p>Vos notes apparaîtront ici une fois évaluées</p></div>';
            } else {
                html += '<table><thead><tr><th>Travail</th><th>Note</th><th>Remarques</th><th>Date</th></tr></thead><tbody>';
                mesNotes.forEach(l => {
                    const travail = travaux.find(t => t.id === l.travailId);
                    html += `<tr>
                        <td><strong>${travail ? travail.titre : 'N/A'}</strong></td>
                        <td><span class="note">${l.note}/20</span></td>
                        <td>${l.remarques || 'Aucune remarque'}</td>
                        <td>${new Date(l.dateEvaluation).toLocaleDateString('fr-FR')}</td>
                    </tr>`;
                });
                html += '</tbody></table>';
            }
            document.getElementById('notesContainer').innerHTML = html;
            document.getElementById('statsContainer').innerHTML = mesNotes.length > 0 ? html.substring(0, html.indexOf('<table>')) : '';
        }
    </script>
</body>
</html>'''
}

# Pages pour FORMATEUR
formateur_pages = {
    'mes-espaces-formateur.html': '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mes Espaces - EduSphère</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html, body { width: 100%; height: 100%; background: #f5f7fa; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
        .page-wrapper { display: grid; grid-template-columns: 300px 1fr; width: 100%; min-height: 100vh; }
        .sidebar-wrapper { background: white; box-shadow: 2px 0 10px rgba(0,0,0,0.08); position: fixed; left: 0; top: 0; width: 300px; height: 100vh; overflow-y: auto; z-index: 100; }
        .content-wrapper { grid-column: 2; padding: 30px 40px; overflow-y: auto; background: #f5f7fa; }
        .content-header { background: white; padding: 30px; border-radius: 8px; margin-bottom: 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        .content-header h1 { color: #2c3e50; font-size: 28px; margin: 0; font-weight: 700; }
        .content-main { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        .space-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }
        .space-card { background: #f9f9f9; padding: 20px; border-radius: 8px; border-left: 4px solid #3498db; }
        .space-card h3 { color: #2c3e50; margin: 0 0 10px 0; }
        .space-info { color: #666; font-size: 14px; margin: 8px 0; }
        .empty-state { text-align: center; padding: 60px 30px; color: #999; }
        .btn { padding: 8px 16px; background: #3498db; color: white; border: none; border-radius: 4px; cursor: pointer; font-weight: 600; font-size: 14px; }
        .btn:hover { background: #2980b9; }
        @media (max-width: 768px) { .page-wrapper { grid-template-columns: 1fr; } .sidebar-wrapper { width: 100%; height: auto; position: relative; } .content-wrapper { grid-column: 1; padding: 15px; } .space-grid { grid-template-columns: 1fr; } }
    </style>
</head>
<body>
    <div class="page-wrapper">
        <div id="sidebar-wrapper"></div>
        <div class="content-wrapper">
            <div class="content-header">
                <h1>🏫 Mes Espaces</h1>
                <p>Les espaces où vous enseignez</p>
            </div>
            <div class="content-main">
                <div id="espacesContainer"></div>
            </div>
        </div>
    </div>
    <script src="auth.js"></script>
    <script src="sidebar.js"></script>
    <script>
        window.addEventListener('load', function() {
            const user = getCurrentUser();
            if (!isLoggedIn() || user.role !== 'formateur') {
                window.location.href = 'login.html';
            }
            loadMesEspaces();
        });

        function loadMesEspaces() {
            const user = getCurrentUser();
            const espaces = JSON.parse(localStorage.getItem('espaces') || '[]');
            const travaux = JSON.parse(localStorage.getItem('travaux') || '[]');
            
            // Filtrer les espaces du formateur
            const mesEspaces = espaces.filter(e => 
                e.formateurs && (e.formateurs.includes(user.id) || e.formateurs.includes(user.identifier))
            );

            let html = '';
            if (mesEspaces.length === 0) {
                html = '<div class="empty-state"><div style="font-size: 80px;">🏫</div><h2>Aucun espace assigné</h2><p>Vous verrez vos espaces ici quand on vous les assignera</p></div>';
            } else {
                html = '<div class="space-grid">';
                mesEspaces.forEach(e => {
                    const mesTravaux = travaux.filter(t => t.espaceId === e.id).length;
                    const mesEtudiants = (e.etudiants || []).length;
                    html += `<div class="space-card">
                        <h3>📚 ${e.matiere}</h3>
                        <div class="space-info"><strong>Code:</strong> ${e.code}</div>
                        <div class="space-info"><strong>Description:</strong> ${e.description || 'Aucune'}</div>
                        <div class="space-info">👨‍🎓 Étudiants: <strong>${mesEtudiants}</strong></div>
                        <div class="space-info">📖 Travaux: <strong>${mesTravaux}</strong></div>
                        <button class="btn" onclick="alert('Voir détails - À implémenter')">Voir Détails</button>
                    </div>`;
                });
                html += '</div>';
            }
            document.getElementById('espacesContainer').innerHTML = html;
        }
    </script>
</body>
</html>''',
}

# Créer les fichiers
all_pages = {**etudiant_pages, **formateur_pages}

for filename, content in all_pages.items():
    filepath = os.path.join(frontend_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ {filename}")

print(f"\n✅ {len(all_pages)} pages créées/mises à jour")
