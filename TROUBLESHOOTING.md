# 🔧 GUIDE DE DÉPANNAGE - Résoudre les Problèmes

---

## ⚠️ Problèmes Courants

### Problème 1: "Je ne vois pas le lien S'inscrire"

**Symptôme:** La page login.html ne montre pas le bouton "S'inscrire ici →"

**Causes possibles:**
- Navigateur non à jour
- Cache du navigateur
- JavaScript désactivé

**Solutions:**
```
1. Videz le cache (Ctrl+Shift+Suppr)
2. Rafraîchissez la page (Ctrl+Shift+R)
3. Vérifiez JavaScript activé (F12 → Console)
4. Essayez un autre navigateur
```

---

### Problème 2: "Je n'ai pas reçu le code email"

**Symptôme:** L'étape de vérification apparaît mais pas de code

**Causes possibles:**
- Mode démo (affichage console)
- Spam/dossier junk
- Pas d'API email configurée

**Solutions:**
```
1. Ouvrez la console (F12)
2. Cherchez: "📧 Code de vérification envoyé"
3. Copiez le code 6 chiffres
4. Collez-le dans le formulaire
5. En production: Configurez l'API email
```

---

### Problème 3: "Le code email est incorrect"

**Symptôme:** Message "Code de vérification incorrect"

**Causes possibles:**
- Mauvais code copié
- Code expiré
- Erreur de saisie

**Solutions:**
```
1. Cliquez "Renvoyer"
2. Consultez la console (F12) à nouveau
3. Copiez le NOUVEAU code
4. Entrez-le exactement
```

---

### Problème 4: "Je ne peux pas me connecter"

**Symptôme:** Message "Erreur de connexion"

**Causes possibles:**
- Rôle non sélectionné
- Identifiant/mot de passe incorrect
- Compte pas vérifié

**Solutions:**
```
1. Sélectionnez un RÔLE (obligatoire)
2. Entrez l'identifiant exactement (case-sensitive)
3. Entrez le mot de passe exactement
4. Vérifiez que vous avez complété l'inscription
5. Ouvrez la console (F12) pour voir l'erreur
```

---

### Problème 5: "Le menu n'est pas correct"

**Symptôme:** Menu n'affiche pas les bonnes options

**Causes possibles:**
- Rôle mal sélectionné
- Cache du navigateur
- localStorage corrompu

**Solutions:**
```
1. Déconnectez-vous
2. Videz le cache (Ctrl+Shift+Suppr)
3. Reconnectez-vous
4. Sélectionnez le BON rôle
5. Vérifiez localStorage (F12 → Application)
```

---

### Problème 6: "Je suis redirigé vers login.html"

**Symptôme:** Impossible d'accéder à une page

**Causes possibles:**
- Session expirée
- Rôle n'a pas accès
- localStorage vidé

**Solutions:**
```
1. Reconnectez-vous
2. Vérifiez que vous avez le bon rôle
3. Consultez TEST_GUIDE.md section "Contrôle d'accès"
4. Ouvrez la console pour les erreurs
```

---

### Problème 7: "La page n'est pas responsive"

**Symptôme:** Page mal affichée sur mobile

**Causes possibles:**
- Zoom navigateur
- Navigateur mobile pas à jour
- Cache du navigateur

**Solutions:**
```
1. Zoomez à 100% (Ctrl+0)
2. Rafraîchissez (Ctrl+R)
3. Videz le cache
4. Testez sur un autre appareil
5. Consultez F12 → Device toolbar
```

---

## 🔍 Vérifications à Faire

### Checklist Diagnostic

```
☐ Navigateur à jour? (Chrome, Firefox, Safari)
☐ JavaScript activé? (F12 → Console pas d'erreur)
☐ Cookies acceptés? (Paramètres navigateur)
☐ localStorage activé? (F12 → Application)
☐ Mode incognito? (Essayez)
☐ Cache vidé? (Ctrl+Shift+Suppl)
☐ Page rafraîchie? (Ctrl+Shift+R)
```

---

## 🐛 Debugging avec la Console

### Ouvrir la Console
```
Windows: F12 ou Ctrl+Shift+I
Mac: Cmd+Option+I
```

### Voir les Erreurs
```
Allez sur l'onglet "Console"
Cherchez les messages en rouge
Copiez l'erreur et consultez le guide
```

### Vérifier localStorage
```
1. F12 → Application
2. Expandez "Local Storage"
3. Vérifiez "currentUser" existe
4. Vérifiez contient: id, identifier, role
```

### Vérifier les Requêtes
```
1. F12 → Network
2. Rafraîchissez la page
3. Cherchez les requêtes en rouge
4. Consultez la réponse pour l'erreur
```

---

## 💾 Réinitialiser les Données

### Si localStorage est Corrompu

```javascript
// Dans la console (F12):
localStorage.clear();
console.log('localStorage vidé');

// Rafraîchissez la page
location.reload();
```

### Si Vous Voulez Réinitialiser la Session

```javascript
// Dans la console:
localStorage.removeItem('currentUser');
localStorage.removeItem('pendingUser');
console.log('Session supprimée');

// Rafraîchissez
location.reload();
```

---

## 🔐 Problèmes de Sécurité

### Message: "Vous n'avez pas accès à cette page"

**C'est normal!** Votre rôle n'y a pas accès.

**Solutions:**
- Créez un nouveau compte avec le bon rôle
- Ou demandez à un administrateur

---

### Mot de Passe Rejeté

**Raisons possibles:**
- Moins de 8 caractères
- Pas de majuscule
- Pas de minuscule
- Pas de chiffre

**Solution:** Vérifiez les 4 critères en temps réel

---

## 📱 Problèmes Mobile

### Page pas responsive

```
1. Ouvrez F12
2. Cliquez sur "Toggle device toolbar"
3. Testez sur iPhone/Android
4. Vérifiez all boutons cliquables
```

### Sidebar disparue

```
En développement pour mobile.
Workaround: Utilisez le menu du navigateur
ou consultez le guide utilisateur
```

---

## 📧 Problèmes Email

### Code visible en Console (Mode Démo)

**C'est normal!** En production:
```python
# Utilisez SendGrid ou AWS SES
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
```

### Code email non reçu (Production)

```
1. Vérifiez l'API est configurée
2. Vérifiez les credentials
3. Vérifiez le compte email existe
4. Vérifiez le dossier spam
```

---

## 🔄 Réinstaller/Réinitialiser

### Réinstaller le Système

```bash
# Supprimer ancien
rm -rf frontend/

# Copier nouveau depuis le repo
git checkout -- frontend/

# Rafraîchir navigateur
Ctrl+Shift+R
```

### Réinitialiser la Base de Données

```bash
# Supprimer old database
rm db.sqlite3

# Créer nouveau
python manage.py migrate

# Créer superuser
python manage.py createsuperuser
```

---

## 📞 Demander de l'Aide

### Avant de Contacter Support

1. ☐ Lisez ce guide
2. ☐ Vérifiez les problèmes courants
3. ☐ Ouvrez la console (F12)
4. ☐ Notez l'erreur exacte
5. ☐ Décrivez ce que vous avez tenté

### Informations à Fournir

```
- URL exacte de la page
- Navigateur et version
- Système (Windows/Mac/Linux)
- Erreur exacte dans la console
- Étapes pour reproduire
- Capture d'écran
```

---

## 🆘 Emergency Recovery

### Accès Bloqué

```
1. Videz localStorage:
   localStorage.clear()
   
2. Rafraîchissez:
   Ctrl+Shift+R
   
3. Fermez le navigateur
4. Rouvrez
5. Allez sur login.html
```

### Session Corrompue

```
1. Mode incognito (Ctrl+Shift+N)
2. Allez sur login.html
3. Connectez-vous normalement
4. Testez
```

### Données Perdues

```
Si c'est important:
1. Contactez l'administrateur
2. Backup files si disponible
3. Notez les infos à restaurer
```

---

## 📚 Documents Utiles

Pour différents problèmes:
- **Installation:** README.md
- **Utilisation:** USER_GUIDE_FR.md
- **Architecture:** DEVELOPER_GUIDE.md
- **Tests:** TEST_GUIDE.md
- **Navigation:** NAVIGATION_MAP.md

---

## ✅ Checklist Avant de Contacter Support

- [ ] Navigateur à jour
- [ ] Cache vidé
- [ ] Page rafraîchie
- [ ] localStorage OK
- [ ] Console consultée
- [ ] Guide lu
- [ ] Toutes les étapes tenté

---

## 💡 Tips & Tricks

### Astuce 1: Mode Incognito
```
Chaque problème étrange → Mode incognito
Ctrl+Shift+N pour ouvrir
```

### Astuce 2: Videz Cache
```
Problème persiste → Vider cache
Ctrl+Shift+Suppr
```

### Astuce 3: Console
```
Doute sur erreur → Console (F12)
Cherchez messages rouges
```

### Astuce 4: Autre Navigateur
```
Problème bizarre → Essayez Chrome/Firefox
Élimine problèmes navigateur
```

---

**Besoin d'aide? Consultez les documents d'accompagnement!**
