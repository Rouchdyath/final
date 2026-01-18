# 🚀 Guide Rapide - Tester le Système Complet

Bienvenue! Voici comment tester immédiatement le système amélioré EduSphère v2.0.

---

## 🔑 Comptes de Test

### Directeur (Accès Complet)
- **Identifiant:** Directeur
- **Mot de passe:** Directeur123

### Formateur (Accès Limité)
- **Identifiant:** Formateur1
- **Mot de passe:** Formateur123

### Étudiant (Accès Minimal)
- **Identifiant:** Etudiant1
- **Mot de passe:** Etudiant123

---

## ✅ Étapes de Test Rapides

### 1️⃣ **Test Création Promotion (2 min)**
```
1. Login comme Directeur
2. Menu → Promotions → Créer Promotion
3. Remplir:
   - Nom: "Master IA 2024"
   - Code: "MAIA2024"
   - Niveau: "M1"
   - Début: 2024-09-01
   - Fin: 2025-08-31
4. Cliquer "Créer la Promotion"
5. Vérifier dans → Lister Promotions
   ✅ La promotion doit apparaître dans le tableau
```

### 2️⃣ **Test Création Étudiant (2 min)**
```
1. Menu → Équipe → Créer Étudiant
2. Remplir:
   - Email: test@university.fr
   - Identifiant: etest001
   - Mot de passe: Test123
   - Nom: Test Student
3. Cliquer "Créer l'Étudiant"
4. Vérifier dans → Lister Étudiants
   ✅ L'étudiant doit apparaître dans le tableau
```

### 3️⃣ **Test Assignation Promotion (3 min)**
```
1. Menu → Promotions → Assigner Étudiants
2. Dropdown "Promotion": Sélectionner la promo créée
3. Dropdown "Étudiant": Sélectionner l'étudiant créé
4. Cliquer "Assigner l'Étudiant"
5. Voir la liste s'actualiser
   ✅ L'assignation doit apparaître avec bouton Retirer
6. Cliquer "Retirer" pour le retirer
   ✅ Doit disparaître de la liste
```

### 4️⃣ **Test Création Formateur (2 min)**
```
1. Menu → Équipe → Créer Formateur
2. Remplir les champs (email unique, identifiant unique)
3. Cliquer "Créer le Formateur"
4. Vérifier que le formateur est créé dans app_users
   ✅ Formateur ajouté avec role='formateur'
```

### 5️⃣ **Test Assignation Formateur (3 min)**
```
1. Menu → Équipe → Gérer Formateurs
2. Dropdown "Espace": Sélectionner un espace
3. Dropdown "Formateur": Sélectionner le formateur créé
4. Cliquer "Assigner le Formateur"
5. Voir la liste des formateurs assignés
   ✅ Formateur doit apparaître avec bouton Retirer
```

### 6️⃣ **Test Évaluation Livraisons (3 min)**
```
1. Menu → Travaux → Évaluer Livraisons
2. Vous verrez les livraisons groupées par travail
3. Pour chaque livraison:
   - Entrer une Note (0-20): "15"
   - Ajouter Remarques: "Bon travail!"
   - Cliquer "Valider l'Évaluation"
4. Voir la note s'afficher en haut de la livraison
   ✅ Note sauvegardée dans localStorage
```

### 7️⃣ **Test Assignation Travaux (3 min)**
```
1. Menu → Travaux → Assigner des Travaux
2. Dropdown "Espace": Sélectionner un espace
   → Les travaux de cet espace apparaissent
3. Dropdown "Travail": Sélectionner un travail
4. Multi-select "Étudiants": 
   - CTRL+Click pour sélectionner plusieurs
   - OU SHIFT+Click pour plage
5. Cliquer "Assigner les Étudiants"
6. Voir les assignations dans la liste
   ✅ Les étudiants doivent apparaître avec bouton Retirer
```

---

## 🔍 Points à Vérifier

### Création
- ✅ Validation des champs obligatoires
- ✅ Détection des doublons (email, code, identifiant)
- ✅ Validation des dates (fin > début)
- ✅ Message de succès après création
- ✅ Redirection vers liste après création

### Listing
- ✅ Tous les éléments créés apparaissent
- ✅ Les données affichées sont correctes
- ✅ Les boutons Voir/Supprimer fonctionnent
- ✅ Suppression demande confirmation
- ✅ Rafraîchissement instantané après action

### Assignation
- ✅ Les dropdowns se remplissent correctement
- ✅ Pas de doublon d'assignation
- ✅ Bouton Retirer fonctionne
- ✅ La liste se met à jour en temps réel
- ✅ Les données persistent après F5

---

## 🛠️ Dépannage

### "Les données disparaissent après F5"
- ✅ Vérifiez que localStorage est activé
- ✅ Ouvrez DevTools (F12) → Application → LocalStorage
- ✅ Cherchez "promotions", "app_users", "espaces"

### "Les dropdowns sont vides"
- ✅ Créez d'abord des éléments (promotions, espaces, etc.)
- ✅ Vérifiez localStorage pour voir les données

### "Erreur d'accès refusé"
- ✅ Directeur uniquement pour créer
- ✅ Directeur + Formateur pour évaluer
- ✅ Vérifiez votre rôle dans le profil

### "Les assignations ne s'affichent pas"
- ✅ Ouvrez DevTools → Console
- ✅ Vérifiez qu'il n'y a pas d'erreurs JS
- ✅ Rechargez la page complètement (CTRL+F5)

---

## 📊 Vérifier localStorage

Ouvrez la console du navigateur (F12) et tapez:

```javascript
// Voir toutes les promotions
console.log(JSON.parse(localStorage.getItem('promotions')))

// Voir tous les utilisateurs
console.log(JSON.parse(localStorage.getItem('app_users')))

// Voir tous les espaces
console.log(JSON.parse(localStorage.getItem('espaces')))

// Voir tous les travaux
console.log(JSON.parse(localStorage.getItem('travaux')))

// Voir toutes les livraisons
console.log(JSON.parse(localStorage.getItem('livraisons')))

// Voir l'utilisateur actuel
console.log(JSON.parse(localStorage.getItem('currentUser')))
```

---

## 🚀 Cas d'Usage Complets

### Scénario 1: Créer un Cours Complet
```
1. Créer une Promotion (L3 Informatique)
2. Créer 3 Étudiants
3. Assigner les 3 étudiants à la Promotion
4. Créer un Formateur
5. Assigner le Formateur à un Espace
6. Créer 2 Travaux pour l'Espace
7. Assigner les Travaux aux Étudiants
8. Soumettre des Livraisons (optionnel)
9. Évaluer les Livraisons
✅ Cycle complet fonctionnel!
```

### Scénario 2: Gestion Multi-Promotions
```
1. Créer 2 Promotions (L3, M1)
2. Créer 6 Étudiants
3. Assigner 3 à chaque Promotion
4. Créer 2 Espaces
5. Créer 2 Formateurs
6. Assigner chacun à un Espace
7. Créer plusieurs Travaux
8. Assigner les Travaux à des sous-groupes
✅ Gestion multi-niveaux fonctionnelle!
```

---

## 📱 Tests Mobiles

Le système est responsive! Pour tester:

1. Ouvrez DevTools (F12)
2. Cliquez sur icône mobile (Ctrl+Shift+M)
3. Sélectionnez un appareil (iPhone 12, iPad, etc.)
4. Testez les mêmes actions
   ✅ Sidebar doit se collapsér
   ✅ Layout doit s'adapter
   ✅ Buttons doivent être cliquables

---

## ⚡ Raccourcis Utiles

```
F12                  → Ouvrir DevTools
CTRL+F5              → Rafraîchir complètement
CTRL+SHIFT+Delete    → Vider Cache/Cookies
CTRL+ALT+I           → Ouvrir Console
Cmd+Opt+U (Mac)      → Alt+U (Windows) → Voir source
```

---

## 📞 Support

Si quelque chose ne fonctionne pas:

1. **Vérifiez localStorage:**
   ```javascript
   localStorage.getItem('promotions')
   ```

2. **Vérifiez la console:**
   - F12 → Console
   - Cherchez les erreurs rouges

3. **Videz le cache:**
   - CTRL+SHIFT+Delete
   - Sélectionnez "Tout"

4. **Rechargez:**
   - CTRL+F5 (Hard refresh)

---

## ✅ Checklist de Validation Finale

- [ ] Login fonctionnel (Directeur, Formateur, Étudiant)
- [ ] Création de Promotion fonctionne
- [ ] Listing de Promotion fonctionne
- [ ] Assignation d'Étudiants aux Promotions fonctionne
- [ ] Création de Formateur fonctionne
- [ ] Assignation de Formateur aux Espaces fonctionne
- [ ] Création de Travail fonctionne
- [ ] Assignation de Travaux fonctionne
- [ ] Évaluation de Livraisons fonctionne
- [ ] Sidebar navigation correcte
- [ ] Responsive design fonctionne sur mobile
- [ ] localStorage persiste après F5
- [ ] Contrôle d'accès bloque les rôles non autorisés

---

## 🎯 Résultat Attendu

✅ **Système 100% fonctionnel** avec:
- Création/Listing/Suppression de tous les éléments
- Assignations multi-niveaux (étudiants → promotions, formateurs → espaces, etc.)
- Évaluation de travaux avec notes et remarques
- Persistance des données en localStorage
- Interface responsive et belle
- Contrôle d'accès par rôle
- Sidebar navigation intuitive

---

**Bon test! 🚀**
