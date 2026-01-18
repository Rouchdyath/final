#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from pathlib import Path

# Répertoire frontend
frontend_dir = r"c:\Users\LENOVO\Documents\genie logiciel\projet_SIL3\frontend"

files = {
    'ajouter-etudiant-promotion.html': '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assigner Étudiants aux Promotions - EduSphère</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html, body { width: 100%; height: 100%; background: #f5f7fa; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
        .page-wrapper { display: grid; grid-template-columns: 300px 1fr; width: 100%; min-height: 100vh; }
        .sidebar-wrapper { background: white; box-shadow: 2px 0 10px rgba(0,0,0,0.08); position: fixed; left: 0; top: 0; width: 300px; height: 100vh; overflow-y: auto; z-index: 100; }
        .content-wrapper { grid-column: 2; padding: 30px 40px; overflow-y: auto; background: #f5f7fa; }
        .content-header { background: white; padding: 30px; border-radius: 8px; margin-bottom: 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        .content-header h1 { color: #2c3e50; font-size: 28px; margin: 0; font-weight: 700; }
        .content-main { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; color: #333; font-weight: 600; margin-bottom: 8px; }
        .form-group select, .form-group input { width: 100%; padding: 12px; border: 2px solid #ddd; border-radius: 4px; font-size: 14px; }
        .form-group select:focus, .form-group input:focus { outline: none; border-color: #3498db; background: #f0f7ff; }
        .form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        .btn { padding: 10px 20px; background: #27ae60; color: white; border: none; border-radius: 4px; cursor: pointer; font-weight: 600; transition: all 0.3s; margin-right: 10px; }
        .btn:hover { background: #229954; }
        .btn-danger { background: #e74c3c; }
        .btn-danger:hover { background: #c0392b; }
        .alert { padding: 15px; border-radius: 4px; margin-bottom: 20px; }
        .alert-success { background: #d4edda; color: #155724; }
        .alert-danger { background: #f8d7da; color: #721c24; }
        .assignment-list { margin-top: 30px; border-top: 2px solid #eee; padding-top: 20px; }
        .assignment-item { background: #f9f9f9; padding: 15px; margin: 10px 0; border-radius: 4px; border-left: 4px solid #3498db; display: flex; justify-content: space-between; align-items: center; }
        .assignment-info { flex: 1; }
        .empty-state { text-align: center; padding: 60px 30px; color: #999; }
        @media (max-width: 768px) { .page-wrapper { grid-template-columns: 1fr; } .sidebar-wrapper { width: 100%; height: auto; position: relative; } .content-wrapper { grid-column: 1; padding: 15px; } .form-row { grid-template-columns: 1fr; } }
    </style>
</head>
<body>
    <div class="page-wrapper">
        <div id="sidebar-wrapper"></div>
        <div class="content-wrapper">
            <div class="content-header">
                <h1>👥 Assigner Étudiants aux Promotions</h1>
                <p>Associez les étudiants aux promotions</p>
            </div>
            <div class="content-main">
                <div id="alertBox"></div>
                <div class="form-row">
                    <div class="form-group">
                        <label for="promotionSelect">Sélectionner une Promotion *</label>
                        <select id="promotionSelect" onchange="loadStudents()">
                            <option value="">--Sélectionner--</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="etudiantSelect">Sélectionner un Étudiant *</label>
                        <select id="etudiantSelect">
                            <option value="">--Sélectionner--</option>
                        </select>
                    </div>
                </div>
                <button class="btn" onclick="assignStudent()">✅ Assigner l'Étudiant</button>
                <div class="assignment-list" id="assignmentList"></div>
            </div>
        </div>
    </div>
    <script src="auth.js"></script>
    <script src="sidebar.js"></script>
    <script>
        window.addEventListener('load', function() {
            if (!isLoggedIn() || getCurrentUser().role !== 'directeur') {
                window.location.href = 'login.html';
            }
            loadPromotions();
            loadAllStudents();
        });

        function loadPromotions() {
            const promotions = JSON.parse(localStorage.getItem('promotions') || '[]');
            const select = document.getElementById('promotionSelect');
            select.innerHTML = '<option value="">--Sélectionner--</option>' +
                promotions.map(p => `<option value="${p.id}">${p.nom} (${p.code})</option>`).join('');
        }

        function loadAllStudents() {
            const users = JSON.parse(localStorage.getItem('app_users') || '[]');
            const select = document.getElementById('etudiantSelect');
            const students = users.filter(u => u.role === 'etudiant');
            select.innerHTML = '<option value="">--Sélectionner--</option>' +
                students.map(s => `<option value="${s.id}">${s.identifier}</option>`).join('');
        }

        function loadStudents() {
            const promotionId = document.getElementById('promotionSelect').value;
            if (!promotionId) {
                document.getElementById('assignmentList').innerHTML = '';
                return;
            }
            const promotions = JSON.parse(localStorage.getItem('promotions') || '[]');
            const promotion = promotions.find(p => p.id === promotionId);
            const users = JSON.parse(localStorage.getItem('app_users') || '[]');

            let html = '<h2 style="color: #2c3e50; margin-bottom: 20px;">📋 Étudiants assignés à ' + promotion.nom + '</h2>';
            if (!promotion.etudiants || promotion.etudiants.length === 0) {
                html += '<div class="empty-state">Aucun étudiant assigné à cette promotion</div>';
            } else {
                promotion.etudiants.forEach(etudId => {
                    const etud = users.find(u => u.id === etudId || u.identifier === etudId);
                    html += `<div class="assignment-item">
                        <div class="assignment-info">👨‍🎓 ${etud ? etud.identifier : 'Étudiant'}</div>
                        <button class="btn btn-danger" onclick="removeStudent('${promotionId}', '${etudId}')">✕ Retirer</button>
                    </div>`;
                });
            }
            document.getElementById('assignmentList').innerHTML = html;
        }

        function assignStudent() {
            const promotionId = document.getElementById('promotionSelect').value;
            const studentId = document.getElementById('etudiantSelect').value;

            if (!promotionId || !studentId) {
                showAlert('❌ Veuillez sélectionner une promotion et un étudiant', 'danger');
                return;
            }

            const promotions = JSON.parse(localStorage.getItem('promotions') || '[]');
            const promotion = promotions.find(p => p.id === promotionId);

            if (promotion.etudiants.includes(studentId)) {
                showAlert('❌ Cet étudiant est déjà assigné à cette promotion', 'danger');
                return;
            }

            promotion.etudiants.push(studentId);
            localStorage.setItem('promotions', JSON.stringify(promotions));
            showAlert('✅ Étudiant assigné avec succès', 'success');
            loadStudents();
        }

        function removeStudent(promotionId, studentId) {
            const promotions = JSON.parse(localStorage.getItem('promotions') || '[]');
            const promotion = promotions.find(p => p.id === promotionId);
            promotion.etudiants = promotion.etudiants.filter(id => id !== studentId);
            localStorage.setItem('promotions', JSON.stringify(promotions));
            showAlert('✅ Étudiant retiré avec succès', 'success');
            loadStudents();
        }

        function showAlert(msg, type) {
            document.getElementById('alertBox').innerHTML = `<div class="alert alert-${type}">${msg}</div>`;
            setTimeout(() => document.getElementById('alertBox').innerHTML = '', 3000);
        }
    </script>
</body>
</html>''',

    'creer-etudiant.html': '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Créer Étudiant - EduSphère</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html, body { width: 100%; height: 100%; background: #f5f7fa; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
        .page-wrapper { display: grid; grid-template-columns: 300px 1fr; width: 100%; min-height: 100vh; }
        .sidebar-wrapper { background: white; box-shadow: 2px 0 10px rgba(0,0,0,0.08); position: fixed; left: 0; top: 0; width: 300px; height: 100vh; overflow-y: auto; z-index: 100; }
        .content-wrapper { grid-column: 2; padding: 30px 40px; overflow-y: auto; background: #f5f7fa; }
        .content-header { background: white; padding: 30px; border-radius: 8px; margin-bottom: 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        .content-header h1 { color: #2c3e50; font-size: 28px; margin: 0; font-weight: 700; }
        .content-main { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); max-width: 800px; }
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; color: #333; font-weight: 600; margin-bottom: 8px; }
        .form-group input { width: 100%; padding: 12px; border: 2px solid #ddd; border-radius: 4px; font-size: 14px; font-family: inherit; }
        .form-group input:focus { outline: none; border-color: #3498db; background: #f0f7ff; }
        .form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        .btn-group { display: flex; gap: 10px; margin-top: 30px; }
        .btn { padding: 12px 24px; background: #27ae60; color: white; border: none; border-radius: 4px; cursor: pointer; font-weight: 600; transition: all 0.3s; }
        .btn:hover { background: #229954; }
        .btn-secondary { background: #95a5a6; margin-left: auto; }
        .btn-secondary:hover { background: #7f8c8d; }
        .alert { padding: 15px; border-radius: 4px; margin-bottom: 20px; }
        .alert-success { background: #d4edda; color: #155724; }
        .alert-danger { background: #f8d7da; color: #721c24; }
        .form-help { color: #999; font-size: 13px; margin-top: 5px; }
        @media (max-width: 768px) { .page-wrapper { grid-template-columns: 1fr; } .sidebar-wrapper { width: 100%; height: auto; position: relative; } .content-wrapper { grid-column: 1; padding: 15px; } .form-row { grid-template-columns: 1fr; } .btn-group { flex-direction: column; } .btn-secondary { margin-left: 0; } }
    </style>
</head>
<body>
    <div class="page-wrapper">
        <div id="sidebar-wrapper"></div>
        <div class="content-wrapper">
            <div class="content-header">
                <h1>👨‍🎓 Créer un Étudiant</h1>
                <p>Ajoutez un nouvel étudiant au système</p>
            </div>
            <div class="content-main">
                <div id="alertBox"></div>
                <form onsubmit="createStudent(event)">
                    <div class="form-group">
                        <label for="email">Email *</label>
                        <input type="email" id="email" placeholder="ex: etudiant@university.com" required>
                    </div>
                    <div class="form-row">
                        <div class="form-group">
                            <label for="identifier">Identifiant *</label>
                            <input type="text" id="identifier" placeholder="ex: etud001" required>
                        </div>
                        <div class="form-group">
                            <label for="password">Mot de passe *</label>
                            <input type="password" id="password" placeholder="Sécurisé" required>
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="nom">Nom Complet</label>
                        <input type="text" id="nom" placeholder="ex: Dupont Jean">
                    </div>
                    <div class="btn-group">
                        <button type="submit" class="btn">✅ Créer l'Étudiant</button>
                        <button type="button" class="btn btn-secondary" onclick="window.location.href='liste-etudiants.html'">Annuler</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <script src="auth.js"></script>
    <script src="sidebar.js"></script>
    <script>
        window.addEventListener('load', function() {
            if (!isLoggedIn() || getCurrentUser().role !== 'directeur') {
                window.location.href = 'login.html';
            }
        });
        function createStudent(event) {
            event.preventDefault();
            const email = document.getElementById('email').value.trim();
            const identifier = document.getElementById('identifier').value.trim();
            const password = document.getElementById('password').value;
            const nom = document.getElementById('nom').value.trim();
            if (!email || !identifier || !password) {
                showAlert('❌ Tous les champs obligatoires doivent être remplis', 'danger');
                return;
            }
            const users = JSON.parse(localStorage.getItem('app_users') || '[]');
            if (users.some(u => u.email === email || u.identifier === identifier)) {
                showAlert('❌ Cet email ou identifiant existe déjà', 'danger');
                return;
            }
            const newStudent = {
                id: Date.now().toString(),
                email,
                identifier,
                password: btoa(password),
                role: 'etudiant',
                nom,
                verified: true,
                dateCreation: new Date().toISOString()
            };
            users.push(newStudent);
            localStorage.setItem('app_users', JSON.stringify(users));
            showAlert('✅ Étudiant créé avec succès !', 'success');
            setTimeout(() => window.location.href = 'liste-etudiants.html', 1500);
        }
        function showAlert(msg, type) {
            document.getElementById('alertBox').innerHTML = `<div class="alert alert-${type}">${msg}</div>`;
            if (type !== 'danger') setTimeout(() => document.getElementById('alertBox').innerHTML = '', 3000);
        }
    </script>
</body>
</html>''',

    'creer-formateur.html': '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Créer Formateur - EduSphère</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html, body { width: 100%; height: 100%; background: #f5f7fa; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
        .page-wrapper { display: grid; grid-template-columns: 300px 1fr; width: 100%; min-height: 100vh; }
        .sidebar-wrapper { background: white; box-shadow: 2px 0 10px rgba(0,0,0,0.08); position: fixed; left: 0; top: 0; width: 300px; height: 100vh; overflow-y: auto; z-index: 100; }
        .content-wrapper { grid-column: 2; padding: 30px 40px; overflow-y: auto; background: #f5f7fa; }
        .content-header { background: white; padding: 30px; border-radius: 8px; margin-bottom: 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        .content-header h1 { color: #2c3e50; font-size: 28px; margin: 0; font-weight: 700; }
        .content-main { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); max-width: 800px; }
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; color: #333; font-weight: 600; margin-bottom: 8px; }
        .form-group input { width: 100%; padding: 12px; border: 2px solid #ddd; border-radius: 4px; font-size: 14px; font-family: inherit; }
        .form-group input:focus { outline: none; border-color: #3498db; background: #f0f7ff; }
        .form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        .btn-group { display: flex; gap: 10px; margin-top: 30px; }
        .btn { padding: 12px 24px; background: #27ae60; color: white; border: none; border-radius: 4px; cursor: pointer; font-weight: 600; transition: all 0.3s; }
        .btn:hover { background: #229954; }
        .btn-secondary { background: #95a5a6; margin-left: auto; }
        .btn-secondary:hover { background: #7f8c8d; }
        .alert { padding: 15px; border-radius: 4px; margin-bottom: 20px; }
        .alert-success { background: #d4edda; color: #155724; }
        .alert-danger { background: #f8d7da; color: #721c24; }
        @media (max-width: 768px) { .page-wrapper { grid-template-columns: 1fr; } .sidebar-wrapper { width: 100%; height: auto; position: relative; } .content-wrapper { grid-column: 1; padding: 15px; } .form-row { grid-template-columns: 1fr; } .btn-group { flex-direction: column; } .btn-secondary { margin-left: 0; } }
    </style>
</head>
<body>
    <div class="page-wrapper">
        <div id="sidebar-wrapper"></div>
        <div class="content-wrapper">
            <div class="content-header">
                <h1>👨‍🏫 Créer un Formateur</h1>
                <p>Ajoutez un nouveau formateur au système</p>
            </div>
            <div class="content-main">
                <div id="alertBox"></div>
                <form onsubmit="createFormateur(event)">
                    <div class="form-group">
                        <label for="email">Email *</label>
                        <input type="email" id="email" placeholder="ex: formateur@university.com" required>
                    </div>
                    <div class="form-row">
                        <div class="form-group">
                            <label for="identifier">Identifiant *</label>
                            <input type="text" id="identifier" placeholder="ex: prof001" required>
                        </div>
                        <div class="form-group">
                            <label for="password">Mot de passe *</label>
                            <input type="password" id="password" placeholder="Sécurisé" required>
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="nom">Nom Complet</label>
                        <input type="text" id="nom" placeholder="ex: Martin Dupont">
                    </div>
                    <div class="btn-group">
                        <button type="submit" class="btn">✅ Créer le Formateur</button>
                        <button type="button" class="btn btn-secondary" onclick="window.history.back()">Annuler</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <script src="auth.js"></script>
    <script src="sidebar.js"></script>
    <script>
        window.addEventListener('load', function() {
            if (!isLoggedIn() || getCurrentUser().role !== 'directeur') {
                window.location.href = 'login.html';
            }
        });
        function createFormateur(event) {
            event.preventDefault();
            const email = document.getElementById('email').value.trim();
            const identifier = document.getElementById('identifier').value.trim();
            const password = document.getElementById('password').value;
            const nom = document.getElementById('nom').value.trim();
            if (!email || !identifier || !password) {
                showAlert('❌ Tous les champs obligatoires doivent être remplis', 'danger');
                return;
            }
            const users = JSON.parse(localStorage.getItem('app_users') || '[]');
            if (users.some(u => u.email === email || u.identifier === identifier)) {
                showAlert('❌ Cet email ou identifiant existe déjà', 'danger');
                return;
            }
            const newFormateur = {
                id: Date.now().toString(),
                email,
                identifier,
                password: btoa(password),
                role: 'formateur',
                nom,
                verified: true,
                dateCreation: new Date().toISOString()
            };
            users.push(newFormateur);
            localStorage.setItem('app_users', JSON.stringify(users));
            showAlert('✅ Formateur créé avec succès !', 'success');
            setTimeout(() => window.history.back(), 1500);
        }
        function showAlert(msg, type) {
            document.getElementById('alertBox').innerHTML = `<div class="alert alert-${type}">${msg}</div>`;
            if (type !== 'danger') setTimeout(() => document.getElementById('alertBox').innerHTML = '', 3000);
        }
    </script>
</body>
</html>''',

    'ajouter-formateur.html': '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assigner Formateurs aux Espaces - EduSphère</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html, body { width: 100%; height: 100%; background: #f5f7fa; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
        .page-wrapper { display: grid; grid-template-columns: 300px 1fr; width: 100%; min-height: 100vh; }
        .sidebar-wrapper { background: white; box-shadow: 2px 0 10px rgba(0,0,0,0.08); position: fixed; left: 0; top: 0; width: 300px; height: 100vh; overflow-y: auto; z-index: 100; }
        .content-wrapper { grid-column: 2; padding: 30px 40px; overflow-y: auto; background: #f5f7fa; }
        .content-header { background: white; padding: 30px; border-radius: 8px; margin-bottom: 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        .content-header h1 { color: #2c3e50; font-size: 28px; margin: 0; font-weight: 700; }
        .content-main { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        .form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; color: #333; font-weight: 600; margin-bottom: 8px; }
        .form-group select { width: 100%; padding: 12px; border: 2px solid #ddd; border-radius: 4px; font-size: 14px; }
        .form-group select:focus { outline: none; border-color: #3498db; background: #f0f7ff; }
        .btn { padding: 10px 20px; background: #27ae60; color: white; border: none; border-radius: 4px; cursor: pointer; font-weight: 600; margin-right: 10px; }
        .btn:hover { background: #229954; }
        .btn-danger { background: #e74c3c; }
        .btn-danger:hover { background: #c0392b; }
        .alert { padding: 15px; border-radius: 4px; margin-bottom: 20px; }
        .alert-success { background: #d4edda; color: #155724; }
        .alert-danger { background: #f8d7da; color: #721c24; }
        .assignment-list { margin-top: 30px; border-top: 2px solid #eee; padding-top: 20px; }
        .assignment-item { background: #f9f9f9; padding: 15px; margin: 10px 0; border-radius: 4px; border-left: 4px solid #3498db; display: flex; justify-content: space-between; align-items: center; }
        @media (max-width: 768px) { .page-wrapper { grid-template-columns: 1fr; } .sidebar-wrapper { width: 100%; height: auto; position: relative; } .content-wrapper { grid-column: 1; padding: 15px; } .form-row { grid-template-columns: 1fr; } }
    </style>
</head>
<body>
    <div class="page-wrapper">
        <div id="sidebar-wrapper"></div>
        <div class="content-wrapper">
            <div class="content-header">
                <h1>👨‍🏫 Assigner Formateurs aux Espaces</h1>
                <p>Associez les formateurs aux espaces pédagogiques</p>
            </div>
            <div class="content-main">
                <div id="alertBox"></div>
                <div class="form-row">
                    <div class="form-group">
                        <label for="espaceSelect">Sélectionner un Espace *</label>
                        <select id="espaceSelect" onchange="loadFormateurs()">
                            <option value="">--Sélectionner--</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="formateurSelect">Sélectionner un Formateur *</label>
                        <select id="formateurSelect">
                            <option value="">--Sélectionner--</option>
                        </select>
                    </div>
                </div>
                <button class="btn" onclick="assignFormateur()">✅ Assigner le Formateur</button>
                <div class="assignment-list" id="assignmentList"></div>
            </div>
        </div>
    </div>
    <script src="auth.js"></script>
    <script src="sidebar.js"></script>
    <script>
        window.addEventListener('load', function() {
            if (!isLoggedIn() || getCurrentUser().role !== 'directeur') {
                window.location.href = 'login.html';
            }
            loadEspaces();
            loadAllFormateurs();
        });
        function loadEspaces() {
            const espaces = JSON.parse(localStorage.getItem('espaces') || '[]');
            const select = document.getElementById('espaceSelect');
            select.innerHTML = '<option value="">--Sélectionner--</option>' +
                espaces.map(e => `<option value="${e.id}">${e.matiere} (${e.code})</option>`).join('');
        }
        function loadAllFormateurs() {
            const users = JSON.parse(localStorage.getItem('app_users') || '[]');
            const select = document.getElementById('formateurSelect');
            const formateurs = users.filter(u => u.role === 'formateur');
            select.innerHTML = '<option value="">--Sélectionner--</option>' +
                formateurs.map(f => `<option value="${f.id}">${f.identifier}</option>`).join('');
        }
        function loadFormateurs() {
            const espaceId = document.getElementById('espaceSelect').value;
            if (!espaceId) {
                document.getElementById('assignmentList').innerHTML = '';
                return;
            }
            const espaces = JSON.parse(localStorage.getItem('espaces') || '[]');
            const espace = espaces.find(e => e.id === espaceId);
            const users = JSON.parse(localStorage.getItem('app_users') || '[]');
            let html = '<h2 style="color: #2c3e50; margin-bottom: 20px;">👨‍🏫 Formateurs assignés à ' + espace.matiere + '</h2>';
            if (!espace.formateurs || espace.formateurs.length === 0) {
                html += '<div style="text-align: center; padding: 40px; color: #999;">Aucun formateur assigné</div>';
            } else {
                espace.formateurs.forEach(formId => {
                    const form = users.find(u => u.id === formId || u.identifier === formId);
                    html += `<div class="assignment-item">
                        <div>👨‍🏫 ${form ? form.identifier : 'Formateur'}</div>
                        <button class="btn btn-danger" onclick="removeFormateur('${espaceId}', '${formId}')">✕ Retirer</button>
                    </div>`;
                });
            }
            document.getElementById('assignmentList').innerHTML = html;
        }
        function assignFormateur() {
            const espaceId = document.getElementById('espaceSelect').value;
            const formateurId = document.getElementById('formateurSelect').value;
            if (!espaceId || !formateurId) {
                showAlert('❌ Veuillez sélectionner un espace et un formateur', 'danger');
                return;
            }
            const espaces = JSON.parse(localStorage.getItem('espaces') || '[]');
            const espace = espaces.find(e => e.id === espaceId);
            if (espace.formateurs.includes(formateurId)) {
                showAlert('❌ Ce formateur est déjà assigné à cet espace', 'danger');
                return;
            }
            espace.formateurs.push(formateurId);
            localStorage.setItem('espaces', JSON.stringify(espaces));
            showAlert('✅ Formateur assigné avec succès', 'success');
            loadFormateurs();
        }
        function removeFormateur(espaceId, formateurId) {
            const espaces = JSON.parse(localStorage.getItem('espaces') || '[]');
            const espace = espaces.find(e => e.id === espaceId);
            espace.formateurs = espace.formateurs.filter(id => id !== formateurId);
            localStorage.setItem('espaces', JSON.stringify(espaces));
            showAlert('✅ Formateur retiré avec succès', 'success');
            loadFormateurs();
        }
        function showAlert(msg, type) {
            document.getElementById('alertBox').innerHTML = `<div class="alert alert-${type}">${msg}</div>`;
            setTimeout(() => document.getElementById('alertBox').innerHTML = '', 3000);
        }
    </script>
</body>
</html>'''
}

# Écrire tous les fichiers
for filename, content in files.items():
    filepath = os.path.join(frontend_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ {filename} créé")

print("\n✅ Tous les fichiers ont été créés avec succès !")
