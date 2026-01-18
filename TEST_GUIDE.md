# 🧪 GUIDE DE TEST - Vérifier que tout fonctionne

## 📋 Checklist de Test Complète

---

## PARTIE 1: Pages Publiques

### Test 1.1: Page de Connexion Accessible
```
✓ URL: http://localhost:8000/frontend/login.html
✓ Page s'affiche (fond violet, formulaire blanc)
✓ 3 boutons rôle visibles: Étudiant, Formateur, Directeur
✓ Champs: Identifiant, Mot de passe
✓ Bouton "Se Connecter"
✓ Info "Mode Démo" visible
```

**Résultat:** ☐ Passé ☐ Échoué

### Test 1.2: Lien vers Inscription
```
✓ Depuis login.html
✓ Bouton vert "S'inscrire ici →" visible
✓ Clic → Redirection vers signup.html
```

**Résultat:** ☐ Passé ☐ Échoué

---

## PARTIE 2: Inscription (signup.html)

### Test 2.1: Affichage du Formulaire
```
✓ Page signup.html accessible
✓ Titre "S'inscrire"
✓ Formulaire visible avec champs:
  ☐ Email
  ☐ Identifiant
  ☐ Mot de passe
  ☐ Confirmer mot de passe
  ☐ Sélection rôle (Étudiant/Formateur)
✓ Bouton "S'inscrire →"
✓ Bouton "← Retour"
✓ Lien "Se connecter" en bas
```

**Résultat:** ☐ Passé ☐ Échoué

### Test 2.2: Validation Mot de Passe
```
✓ Entrez mot de passe faible: "abc"
✓ Les 4 critères s'affichent en rouge (incomplète)
✓ Entrez mot de passe fort: "Test1234!"
✓ Les critères deviennent verts
✓ Vérifiez que:
  ☐ 8+ caractères ✓
  ☐ Une majuscule ✓
  ☐ Une minuscule ✓
  ☐ Un chiffre ✓
```

**Résultat:** ☐ Passé ☐ Échoué

### Test 2.3: Validation Email
```
✓ Entrez email invalide: "notanemail"
✓ Message d'erreur s'affiche
✓ Entrez email valide: "test@example.com"
✓ Pas d'erreur
```

**Résultat:** ☐ Passé ☐ Échoué

### Test 2.4: Mismatch Mot de Passe
```
✓ Mot de passe: Test1234!
✓ Confirmer: Different1!
✓ Cliquez "S'inscrire →"
✓ Message d'erreur: "Les mots de passe ne correspondent pas"
```

**Résultat:** ☐ Passé ☐ Échoué

### Test 2.5: Inscription Réussie
```
✓ Email: testuser@example.com
✓ Identifiant: testuser123
✓ Mot de passe: TestPass123!
✓ Rôle: Étudiant
✓ Cliquez "S'inscrire →"
✓ Vérifiez: "Un code de vérification a été envoyé"
✓ Étape 2 s'affiche (Vérification Email)
```

**Résultat:** ☐ Passé ☐ Échoué

### Test 2.6: Vérification Email
```
✓ Étape 2: "Vérifiez votre Email"
✓ Email affiché: testuser@example.com
✓ Champ "Code de vérification"
✓ Ouvrez Console (F12)
✓ Cherchez message: "📧 Code de vérification envoyé"
✓ Copiez le code 6 chiffres
```

**Résultat:** ☐ Passé ☐ Échoué

### Test 2.7: Code Incorrect
```
✓ Entrez code incorrect: 999999
✓ Cliquez "Vérifier →"
✓ Message d'erreur: "Code de vérification incorrect"
```

**Résultat:** ☐ Passé ☐ Échoué

### Test 2.8: Code Correct
```
✓ Entrez le vrai code (de la console)
✓ Cliquez "Vérifier →"
✓ Étape 3: "Inscription Réussie! ✅"
✓ Message: "Vous serez redirigé..."
✓ Après 3 secondes → Redirection login.html
```

**Résultat:** ☐ Passé ☐ Échoué

### Test 2.9: Renvoi du Code
```
✓ Depuis étape 2, cliquez "Renvoyer"
✓ Message: "Le code a été renvoyé à votre email"
✓ Console: Nouveau code affiché
```

**Résultat:** ☐ Passé ☐ Échoué

### Test 2.10: Retour à l'Inscription
```
✓ Depuis étape 2, cliquez "← Retour"
✓ Retour à étape 1 (formulaire)
✓ Champs vides
```

**Résultat:** ☐ Passé ☐ Échoué

---

## PARTIE 3: Connexion

### Test 3.1: Connexion Réussie
```
✓ Aller sur login.html
✓ Sélectionner rôle: Étudiant
✓ Identifiant: testuser123
✓ Mot de passe: TestPass123!
✓ Cliquez "Se Connecter"
✓ Message de succès s'affiche
✓ Après 1.5 secondes → Redirection index.html
```

**Résultat:** ☐ Passé ☐ Échoué

### Test 3.2: Sans Rôle Sélectionné
```
✓ login.html
✓ NE PAS sélectionner de rôle
✓ Entrez identifiant et mot de passe
✓ Cliquez "Se Connecter"
✓ Message d'erreur: "Veuillez sélectionner un rôle"
```

**Résultat:** ☐ Passé ☐ Échoué

### Test 3.3: Changement de Rôle
```
✓ login.html
✓ Sélectionnez "Étudiant"
✓ Cliquez sur "Formateur"
✓ Vérifiez: Formateur est actif (bleu), Étudiant non
✓ Cliquez sur "Directeur"
✓ Vérifiez: Directeur est actif, Formateur non
```

**Résultat:** ☐ Passé ☐ Échoué

---

## PARTIE 4: Dashboard (index.html)

### Test 4.1: Dashboard Chargé
```
✓ Après connexion comme Étudiant
✓ index.html s'affiche
✓ Sidebar visible à gauche (violet)
✓ Avatar utilisateur avec "T" (première lettre)
✓ Nom: "testuser123"
✓ Rôle: "Étudiant"
✓ Bouton "🚪 Déconnexion"
```

**Résultat:** ☐ Passé ☐ Échoué

---

## PARTIE 5: Sidebar par Rôle

### Test 5.1: Menu Étudiant
```
✓ Connecté comme Étudiant
✓ Sidebar affiche 4 liens:
  ☐ 📚 Mes Travaux
  ☐ 📤 Soumettre une Livraison
  ☐ ⭐ Mes Notes
  ☐ 📂 Retour Accueil
✓ Pas d'autres liens visibles
```

**Résultat:** ☐ Passé ☐ Échoué

### Test 5.2: Menu Formateur
```
✓ Connecté comme Formateur (nouvelle inscription)
✓ Sidebar affiche 9 liens:
  ☐ 🏫 Créer un Espace
  ☐ 📋 Mes Espaces
  ☐ 👨‍🏫 Gérer Formateurs
  ☐ 👨‍🎓 Ajouter Étudiants
  ☐ 📝 Créer un Travail
  ☐ 📌 Assigner des Travaux
  ☐ ✅ Évaluer Livraisons
  ☐ 📊 Consulter Travaux
  ☐ 📂 Retour Accueil
```

**Résultat:** ☐ Passé ☐ Échoué

### Test 5.3: Menu Directeur
```
✓ Connecté comme Directeur (nouvelle inscription)
✓ Sidebar affiche 13 liens (TOUS les menus)
✓ Inclut liens Étudiant + Formateur + Directeur spécifiques
```

**Résultat:** ☐ Passé ☐ Échoué

### Test 5.4: Animations du Menu
```
✓ Les liens s'affichent avec animation fluide
✓ Au survol du lien:
  ☐ Arrière-plan s'éclaircit
  ☐ Flèche → apparaît
  ☐ Lien se décale légèrement
```

**Résultat:** ☐ Passé ☐ Échoué

---

## PARTIE 6: Navigation

### Test 6.1: Cliquer sur les Liens
```
✓ Connecté comme Étudiant
✓ Cliquez "📚 Mes Travaux"
✓ La page liste-travaux.html s'affiche
✓ Sidebar reste visible à gauche
✓ Contenu change à droite
```

**Résultat:** ☐ Passé ☐ Échoué

### Test 6.2: Retour à l'Accueil
```
✓ Depuis n'importe quelle page
✓ Cliquez "📂 Retour Accueil"
✓ Redirection vers index.html
✓ Dashboard s'affiche
```

**Résultat:** ☐ Passé ☐ Échoué

---

## PARTIE 7: Déconnexion

### Test 7.1: Déconnexion
```
✓ Depuis n'importe quelle page
✓ Cliquez "🚪 Déconnexion"
✓ Redirection vers login.html
✓ localStorage.currentUser supprimé
✓ Champs login vides
```

**Résultat:** ☐ Passé ☐ Échoué

### Test 7.2: Accès Page Protégée sans Authentification
```
✓ Après déconnexion
✓ Entrez l'URL directe: liste-travaux.html
✓ Redirection automatique vers login.html
✓ Message: "Vous devez vous connecter"
```

**Résultat:** ☐ Passé ☐ Échoué

---

## PARTIE 8: Contrôle d'Accès

### Test 8.1: Étudiant Accès Refusé
```
✓ Connecté comme Étudiant
✓ Tentez accès: creer-espace.html (page Formateur)
✓ Redirection vers login.html
✓ Message: "Accès non autorisé"
```

**Résultat:** ☐ Passé ☐ Échoué

### Test 8.2: Formateur Accès Refusé
```
✓ Connecté comme Formateur
✓ Tentez accès: creer-etudiant.html (page Directeur)
✓ Redirection vers login.html
```

**Résultat:** ☐ Passé ☐ Échoué

### Test 8.3: Directeur Accès Autorisé
```
✓ Connecté comme Directeur
✓ Accédez à: liste-travaux.html (page Étudiant) → OK
✓ Accédez à: creer-espace.html (page Formateur) → OK
✓ Accédez à: creer-etudiant.html (page Directeur) → OK
```

**Résultat:** ☐ Passé ☐ Échoué

---

## PARTIE 9: Responsive Mobile

### Test 9.1: Vue Desktop
```
✓ Navigateur à 1920x1080
✓ Sidebar à gauche (280px)
✓ Contenu à droite
✓ Bien espacé
```

**Résultat:** ☐ Passé ☐ Échoué

### Test 9.2: Vue Mobile
```
✓ Redimensionnez à 375x667 (iPhone)
✓ Sidebar s'adapte
✓ Contenu prend toute la largeur
✓ Toujours lisible
✓ Tous les boutons cliquables
```

**Résultat:** ☐ Passé ☐ Échoué

---

## PARTIE 10: Validation Données

### Test 10.1: Doublons Email
```
✓ Inscrivez-vous: test@test.com
✓ Vérifiez et confirmez
✓ Tentez nouvelle inscription: test@test.com
✓ Message d'erreur: "Cet email est déjà utilisé"
```

**Résultat:** ☐ Passé ☐ Échoué

### Test 10.2: Doublons Identifiant
```
✓ Inscrivez-vous: "testuser"
✓ Vérifiez et confirmez
✓ Tentez nouvelle inscription: "testuser"
✓ Message d'erreur: "Ce nom d'utilisateur est déjà utilisé"
```

**Résultat:** ☐ Passé ☐ Échoué

---

## 📊 Résumé des Tests

```
SECTION 1 (Pages Publiques):      ☐ 2/2  ☐ Partiel  ☐ Échec
SECTION 2 (Inscription):          ☐ 10/10 ☐ Partiel  ☐ Échec
SECTION 3 (Connexion):            ☐ 3/3  ☐ Partiel  ☐ Échec
SECTION 4 (Dashboard):            ☐ 1/1  ☐ Partiel  ☐ Échec
SECTION 5 (Sidebar):              ☐ 4/4  ☐ Partiel  ☐ Échec
SECTION 6 (Navigation):           ☐ 2/2  ☐ Partiel  ☐ Échec
SECTION 7 (Déconnexion):          ☐ 2/2  ☐ Partiel  ☐ Échec
SECTION 8 (Contrôle d'Accès):    ☐ 3/3  ☐ Partiel  ☐ Échec
SECTION 9 (Responsive):           ☐ 2/2  ☐ Partiel  ☐ Échec
SECTION 10 (Validation):          ☐ 2/2  ☐ Partiel  ☐ Échec
────────────────────────────────────────────────────
TOTAL:                            ☐ 31/31 ☐ Partiel ☐ Échec
```

---

## 🎯 Tests Critiques (À Faire Obligatoirement)

1. ✓ [ ] Inscription complète
2. ✓ [ ] Vérification email
3. ✓ [ ] Connexion
4. ✓ [ ] Menu affiché selon rôle
5. ✓ [ ] Navigation entre pages
6. ✓ [ ] Déconnexion
7. ✓ [ ] Accès refusé si pas connecté
8. ✓ [ ] Contrôle d'accès par rôle

---

## 🐛 Bugs à Chercher

```
❌ Sidebar ne s'affiche pas
❌ Menu n'est pas selon le rôle
❌ Lien "S'inscrire" ne marche pas
❌ Code email non reçu (console)
❌ Impossible de vérifier
❌ Pas de redirection après connexion
❌ Accès autorisé où il ne devrait pas
❌ Déconnexion ne marche pas
```

---

## 💡 Conseils de Test

1. **Toujours tester en mode incognito** (session propre)
2. **Ouvrir la console (F12)** pour voir les messages
3. **Tester chaque rôle séparément** (nouvelle inscription)
4. **Tester la redirection** (directement l'URL)
5. **Tester le responsive** (F12 → Toggle device toolbar)

---

**Mise à jour: 17 janvier 2026**
**Temps estimé: 30-45 minutes pour tous les tests**
