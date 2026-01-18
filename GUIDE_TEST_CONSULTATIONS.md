# 🧪 Guide de Test - Corrections Consultations

## 🚀 Démarrer le serveur

```bash
cd backend
python manage.py runserver
# ou
python manage.py runserver 0.0.0.0:8000
```

Accès: http://localhost:8000

---

## 📝 Comptes de Test

### Directeur
- **Identifiant:** directeur1
- **Mot de passe:** 1234
- **URL d'accès:** http://localhost:8000/frontend/index.html

### Formateur
- **Identifiant:** formateur1
- **Mot de passe:** 1234

### Étudiant
- **Identifiant:** etudiant1
- **Mot de passe:** 1234

---

## ✅ Checklist de Test

### Test 1: Directeur - Voir tous les travaux
```
1. Se connecter avec directeur1
2. Cliquer sur Sidebar → "Travaux" → "Tous les Travaux"
3. Vérifier que la page "consultation-directeur-travaux.html" s'ouvre
4. Vérifier l'affichage:
   ✅ Titre du travail
   ✅ Espace pédagogique (matière + code)
   ✅ Nom du formateur qui l'a créé
   ✅ Liste des étudiants assignés (badges)
   ✅ Date d'échéance
   ✅ Description
```

### Test 2: Directeur - Voir tous les utilisateurs
```
1. Se connecter avec directeur1
2. Cliquer sur Sidebar → "Consultations" → "Consulter Étudiants"
3. Vérifier que la page "consultation-directeur-etudiants.html" s'ouvre
4. Vérifier les filtres:
   ✅ Dropdown "Étudiants" ne montre que les étudiants
   ✅ Dropdown "Formateurs" ne montre que les formateurs
   ✅ Dropdown "Directeurs" ne montre que les directeurs
   ✅ Dropdown "Tous" montre tout le monde
5. Vérifier le tableau:
   ✅ Colonnes: Identifiant, Nom, Email, Rôle, Créé le
   ✅ Badges de rôle sont colorés
```

### Test 3: Formateur - Créer travail
```
1. Se connecter avec formateur1
2. Cliquer sur Sidebar → "Travaux & Étudiants" → "Créer un Travail"
3. Créer un travail avec:
   - Espace: (choisir un espace du formateur)
   - Titre: "Test Travail 1"
   - Description: "Description test"
   - Date d'échéance: (date future)
4. Cliquer "Créer"
5. Vérifier que le travail apparaît dans localStorage.travaux
```

### Test 4: Formateur - Assigner travail
```
1. Se connecter avec formateur1
2. Cliquer sur Sidebar → "Travaux & Étudiants" → "Assigner des Travaux"
3. Vérifier que la page "assigner-travail-formateur.html" s'ouvre
4. Dropdown 1 - Sélectionner un travail (celui créé en Test 3)
5. Vérifier que le Dropdown 2 se remplit avec les étudiants de cet espace
6. Cliquer sur un étudiant → "Assigner"
7. Vérifier l'apparition dans la liste d'assignations
8. Cliquer "Retirer" pour tester la suppression
```

### Test 5: Formateur - Consulter travaux créés
```
1. Se connecter avec formateur1
2. Cliquer sur Sidebar → "Travaux & Étudiants" → "Consulter Travaux"
3. Vérifier que la page "consultation-formateur-travaux.html" s'ouvre
4. Vérifier le tableau:
   ✅ Ne montre QUE les travaux créés par formateur1
   ✅ Colonnes: Titre, Espace, Échéance, Nb assignations
   ✅ Bouton "Supprimer" fonctionne (retire du localStorage)
5. Vérifier qu'un travail créé par un autre formateur N'APPARAÎT PAS
```

### Test 6: Étudiant - Voir ses travaux assignés
```
1. Se connecter avec etudiant1
2. Cliquer sur Sidebar → "Mes Études" → "Mes Travaux"
3. Vérifier que seuls les travaux assignés à etudiant1 s'affichent
4. Ne doit PAS voir les travaux assignés aux autres étudiants
```

### Test 7: Sécurité - Accès non autorisé
```
1. Se connecter avec etudiant1
2. Essayer d'accéder à: http://localhost:8000/frontend/consultation-directeur-travaux.html
3. Vérifier la redirection vers login.html (accès refusé)
```

---

## 🔍 Points Clés à Vérifier

### Directeur
- ✅ Voit TOUS les travaux (pas de filtrage)
- ✅ Voit le NOM du formateur créateur
- ✅ Voit la liste complète des étudiants assignés
- ✅ Peut filtrer les utilisateurs par rôle
- ✅ Accès refusé si connecté avec autre rôle

### Formateur
- ✅ Ne voit que SES travaux créés
- ✅ Peut assigner SES travaux aux étudiants
- ✅ Liste des assignations s'affiche correctement
- ✅ Peut retirer une assignation
- ✅ Accès refusé si connecté avec autre rôle

### Étudiant
- ✅ Ne voit que SES travaux assignés
- ✅ Accès refusé à "Consulter Travaux" (formateur only)
- ✅ Accès refusé à "Consultation Directeur" (directeur only)

---

## 🐛 Troubleshooting

### Page ne s'affiche pas
**Symptôme:** Redirection vers login au lieu de la page
**Solution:**
1. Vérifier le rôle dans getCurrentUser() (F12 → Console → `JSON.stringify(getCurrentUser())`)
2. Vérifier que auth.js est bien chargé
3. Vérifier localStorage.app_users contient l'utilisateur

### Données ne s'affichent pas
**Symptôme:** Page charge mais aucun contenu
**Solution:**
1. F12 → Console → vérifier les erreurs
2. Vérifier localStorage.travaux, localStorage.app_users existent
3. Vérifier les données avec: `JSON.parse(localStorage.getItem('travaux'))`

### Dropdown ne se remplit pas
**Symptôme:** Dropdown vide après sélection du travail
**Solution:**
1. Vérifier que le travail a bien un espaceId
2. Vérifier que cet espace contient des étudiants
3. Vérifier que l'événement 'change' du dropdown est déclenché

---

## 📊 Données Test dans localStorage

Pour tester avec des données, utiliser la console (F12):

```javascript
// Créer un travail test
const newTravail = {
    id: 'travail-' + Date.now(),
    titre: 'Travail Test',
    espaceId: 'espace1',
    createdBy: 'formateur1',
    dateEchéance: '2026-02-28',
    description: 'Travail de test',
    assignations: ['etudiant1', 'etudiant2']
};
const travaux = JSON.parse(localStorage.getItem('travaux') || '[]');
travaux.push(newTravail);
localStorage.setItem('travaux', JSON.stringify(travaux));
```

---

## ✅ Validation Finale

Une fois tous les tests passés:
- [ ] Directeur voit tous les travaux avec créateur
- [ ] Directeur peut filtrer utilisateurs par rôle
- [ ] Formateur assigne travaux correctement
- [ ] Formateur ne voit que ses travaux
- [ ] Étudiant ne voit que ses travaux
- [ ] Sécurité: accès refusé pour rôles non autorisés
- [ ] Sidebar navigation fonctionne pour tous les rôles
- [ ] Pas d'erreurs dans la console (F12)

**Status:** Prêt pour les tests complets! 🚀
