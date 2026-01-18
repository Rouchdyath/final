#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

frontend_dir = r"c:\Users\LENOVO\Documents\genie logiciel\projet_SIL3\frontend"

# Corriger creer-travail.html pour filtrer par espace du formateur
creer_travail = '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Créer un Travail - EduSphère</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html, body { width: 100%; height: 100%; background: #f5f7fa; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
        .page-wrapper { display: grid; grid-template-columns: 300px 1fr; width: 100%; min-height: 100vh; }
        .sidebar-wrapper { background: white; box-shadow: 2px 0 10px rgba(0,0,0,0.08); position: fixed; left: 0; top: 0; width: 300px; height: 100vh; overflow-y: auto; z-index: 100; }
        .content-wrapper { grid-column: 2; padding: 30px 40px; overflow-y: auto; background: #f5f7fa; }
        .content-header { background: white; padding: 30px; border-radius: 8px; margin-bottom: 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        .content-header h1 { color: #2c3e50; font-size: 28px; margin: 0; font-weight: 700; }
        .form-container { background: white; padding: 40px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); max-width: 600px; }
        .form-group { margin-bottom: 25px; }
        label { display: block; margin-bottom: 8px; color: #2c3e50; font-weight: 600; }
        input, select, textarea { width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 4px; font-family: inherit; font-size: 14px; }
        textarea { resize: vertical; min-height: 100px; }
        input:focus, select:focus, textarea:focus { outline: none; border-color: #3498db; box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1); }
        .btn { padding: 12px 24px; background: #3498db; color: white; border: none; border-radius: 4px; cursor: pointer; font-weight: 600; font-size: 16px; }
        .btn:hover { background: #2980b9; }
        .alert { padding: 15px; border-radius: 4px; margin-bottom: 20px; }
        .alert-danger { background: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
        .alert-success { background: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
        @media (max-width: 768px) { .page-wrapper { grid-template-columns: 1fr; } .sidebar-wrapper { width: 100%; height: auto; position: relative; } .content-wrapper { grid-column: 1; padding: 15px; } }
    </style>
</head>
<body>
    <div class="page-wrapper">
        <div id="sidebar-wrapper"></div>
        <div class="content-wrapper">
            <div class="content-header">
                <h1>📝 Créer un Travail</h1>
                <p>Créez un nouveau travail pour l'un de vos espaces</p>
            </div>
            <div class="form-container">
                <div id="alertContainer"></div>
                <form id="travailForm" onsubmit="createTravail(event)">
                    <div class="form-group">
                        <label for="espaceId">Sélectionner l'Espace *</label>
                        <select id="espaceId" required>
                            <option value="">-- Choisir un espace --</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="titre">Titre du Travail *</label>
                        <input type="text" id="titre" placeholder="Ex: Devoir 1" required>
                    </div>
                    <div class="form-group">
                        <label for="description">Description</label>
                        <textarea id="description" placeholder="Description du travail..."></textarea>
                    </div>
                    <div class="form-group">
                        <label for="dateEchéance">Date d'Échéance *</label>
                        <input type="date" id="dateEchéance" required>
                    </div>
                    <button type="submit" class="btn">✅ Créer le Travail</button>
                </form>
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
            
            // Filtrer les espaces du formateur
            const mesEspaces = espaces.filter(e => 
                e.formateurs && (e.formateurs.includes(user.id) || e.formateurs.includes(user.identifier))
            );

            let html = '<option value="">-- Choisir un espace --</option>';
            mesEspaces.forEach(e => {
                html += `<option value="${e.id}">${e.matiere} (${e.code})</option>`;
            });
            document.getElementById('espaceId').innerHTML = html;
        }

        function createTravail(event) {
            event.preventDefault();
            const espaceId = document.getElementById('espaceId').value;
            const titre = document.getElementById('titre').value.trim();
            const description = document.getElementById('description').value.trim();
            const dateEchéance = document.getElementById('dateEchéance').value;

            if (!espaceId || !titre || !dateEchéance) {
                showAlert('❌ Tous les champs obligatoires doivent être remplis', 'danger');
                return;
            }

            const travaux = JSON.parse(localStorage.getItem('travaux') || '[]');
            const newTravail = {
                id: Date.now().toString(),
                espaceId,
                titre,
                description,
                dateEchéance,
                assignations: [],
                dateCreation: new Date().toISOString(),
                createdBy: getCurrentUser().id
            };

            travaux.push(newTravail);
            localStorage.setItem('travaux', JSON.stringify(travaux));
            showAlert('✅ Travail créé avec succès!', 'success');
            setTimeout(() => window.location.href = 'liste-travaux.html', 1500);
        }

        function showAlert(message, type) {
            const alertHTML = `<div class="alert alert-${type}">${message}</div>`;
            document.getElementById('alertContainer').innerHTML = alertHTML;
            setTimeout(() => document.getElementById('alertContainer').innerHTML = '', 5000);
        }
    </script>
</body>
</html>'''

# Corriger consultation-formateur-travaux.html
consultation_travaux = '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consultation Travaux - EduSphère</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html, body { width: 100%; height: 100%; background: #f5f7fa; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
        .page-wrapper { display: grid; grid-template-columns: 300px 1fr; width: 100%; min-height: 100vh; }
        .sidebar-wrapper { background: white; box-shadow: 2px 0 10px rgba(0,0,0,0.08); position: fixed; left: 0; top: 0; width: 300px; height: 100vh; overflow-y: auto; z-index: 100; }
        .content-wrapper { grid-column: 2; padding: 30px 40px; overflow-y: auto; background: #f5f7fa; }
        .content-header { background: white; padding: 30px; border-radius: 8px; margin-bottom: 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        .content-header h1 { color: #2c3e50; font-size: 28px; margin: 0; font-weight: 700; }
        .content-main { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        table { width: 100%; border-collapse: collapse; }
        table th { background: #f0f0f0; color: #2c3e50; padding: 12px; text-align: left; font-weight: 600; border-bottom: 2px solid #ddd; }
        table td { padding: 12px; border-bottom: 1px solid #eee; }
        table tr:hover { background: #f9f9f9; }
        .empty-state { text-align: center; padding: 60px 30px; color: #999; }
        .btn { padding: 8px 16px; background: #3498db; color: white; border: none; border-radius: 4px; cursor: pointer; font-weight: 600; font-size: 12px; }
        .btn:hover { background: #2980b9; }
        .btn-danger { background: #e74c3c; }
        .btn-danger:hover { background: #c0392b; }
        @media (max-width: 768px) { .page-wrapper { grid-template-columns: 1fr; } .sidebar-wrapper { width: 100%; height: auto; position: relative; } .content-wrapper { grid-column: 1; padding: 15px; } }
    </style>
</head>
<body>
    <div class="page-wrapper">
        <div id="sidebar-wrapper"></div>
        <div class="content-wrapper">
            <div class="content-header">
                <h1>📖 Mes Travaux</h1>
                <p>Les travaux que vous avez créés</p>
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
            if (!isLoggedIn() || user.role !== 'formateur') {
                window.location.href = 'login.html';
            }
            loadMesTravaux();
        });

        function loadMesTravaux() {
            const user = getCurrentUser();
            const travaux = JSON.parse(localStorage.getItem('travaux') || '[]');
            const espaces = JSON.parse(localStorage.getItem('espaces') || '[]');
            
            // Filtrer les travaux créés par le formateur
            const mesTravaux = travaux.filter(t => t.createdBy === user.id);

            let html = '';
            if (mesTravaux.length === 0) {
                html = '<div class="empty-state"><div style="font-size: 80px;">📚</div><h2>Aucun travail créé</h2><p>Vous créerez des travaux pour vos espaces ici</p></div>';
            } else {
                html = '<table><thead><tr><th>Titre</th><th>Espace</th><th>Date d\'Échéance</th><th>Assignations</th><th>Actions</th></tr></thead><tbody>';
                mesTravaux.forEach(t => {
                    const espace = espaces.find(e => e.id === t.espaceId);
                    const dateEchéance = new Date(t.dateEchéance).toLocaleDateString('fr-FR');
                    html += `<tr>
                        <td><strong>${t.titre}</strong></td>
                        <td>${espace ? espace.matiere : 'N/A'}</td>
                        <td>${dateEchéance}</td>
                        <td>${t.assignations ? t.assignations.length : 0} étudiants</td>
                        <td>
                            <button class="btn" onclick="viewTravail('${t.id}')">Voir</button>
                            <button class="btn btn-danger" onclick="deleteTravail('${t.id}')">Supprimer</button>
                        </td>
                    </tr>`;
                });
                html += '</tbody></table>';
            }
            document.getElementById('travauxContainer').innerHTML = html;
        }

        function deleteTravail(id) {
            if (confirm('Êtes-vous sûr de vouloir supprimer ce travail?')) {
                const travaux = JSON.parse(localStorage.getItem('travaux') || '[]');
                const index = travaux.findIndex(t => t.id === id);
                if (index > -1) {
                    travaux.splice(index, 1);
                    localStorage.setItem('travaux', JSON.stringify(travaux));
                    loadMesTravaux();
                }
            }
        }

        function viewTravail(id) {
            alert('Détails du travail - À implémenter');
        }
    </script>
</body>
</html>'''

# Pages pour formateur
pages = {
    'creer-travail.html': creer_travail,
    'consultation-formateur-travaux.html': consultation_travaux,
}

for filename, content in pages.items():
    filepath = os.path.join(frontend_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ {filename}")

print(f"\n✅ {len(pages)} pages formateur corrigées")
