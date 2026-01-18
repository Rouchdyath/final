// Système d'authentification avec gestion des rôles

const AUTH_ROLES = {
    ETUDIANT: 'etudiant',
    FORMATEUR: 'formateur',
    DIRECTEUR: 'directeur'
};

// 🔧 INITIALISER LES UTILISATEURS DE TEST SI PAS ENCORE FAIT
function initializeTestUsers() {
    const existingUsers = localStorage.getItem('app_users');
    
    // Si les utilisateurs existent déjà, ne pas réinitialiser
    if (existingUsers) {
        return;
    }
    
    // Créer SEULEMENT le compte Directeur pré-enregistré
    const testUsers = [
        {
            id: 'user-admin-001',
            email: 'directeur@institution.fr',
            identifier: 'directeur',
            password: btoa('Directeur123'),  // 'Directeur123'
            role: 'directeur',
            verified: true,
            registrationTime: new Date().getTime()
        }
    ];
    
    localStorage.setItem('app_users', JSON.stringify(testUsers));
    console.log('✅ Compte Directeur créé automatiquement');
}

// Initialiser les utilisateurs de test au chargement
initializeTestUsers();

const ROLE_PERMISSIONS = {
    'etudiant': [
        'liste-travaux.html',
        'soumettre-livraison.html',
        'mes-notes.html'
    ],
    'formateur': [
        'creer-espace.html',
        'liste-espaces.html',
        'ajouter-formateur.html',
        'creer-formateur.html',
        'creer-travail.html',
        'assigner-travail.html',
        'liste-travaux.html',
        'evaluer-livraisons.html',
        'consultation-formateur-travaux.html'
    ],
    'directeur': [
        'creer-espace.html',
        'liste-espaces.html',
        'ajouter-formateur.html',
        'creer-formateur.html',
        'creer-etudiant.html',
        'ajouter-etudiant-espace.html',
        'liste-etudiants.html',
        'ajouter-etudiant-promotion.html',
        'creer-promotion.html',
        'liste-promotions.html',
        'creer-travail.html',
        'assigner-travail.html',
        'liste-travaux.html',
        'soumettre-livraison.html',
        'evaluer-livraisons.html',
        'mes-notes.html',
        'consultation-directeur-espaces.html',
        'consultation-directeur-etudiants.html',
        'consultation-directeur-promotions.html',
        'consultation-formateur-travaux.html'
    ]
};

// Obtenir les informations de l'utilisateur connecté
function getCurrentUser() {
    const user = localStorage.getItem('currentUser');
    return user ? JSON.parse(user) : null;
}

// Obtenir le rôle de l'utilisateur actuel
function getCurrentRole() {
    const user = getCurrentUser();
    return user ? user.role : null;
}

// Obtenir l'ID de l'utilisateur actuel
function getCurrentUserId() {
    const user = getCurrentUser();
    return user ? user.id : null;
}

// Vérifier si l'utilisateur est connecté
function isLoggedIn() {
    return getCurrentUser() !== null;
}

// Connexion
function login(identifier, password, role) {
    // Récupérer les utilisateurs enregistrés depuis localStorage
    const users = JSON.parse(localStorage.getItem('app_users') || '[]');
    
    // Convertir l'identifiant en minuscules pour la comparaison (insensible à la casse)
    const identifierLower = identifier.toLowerCase().trim();
    
    console.log('🔍 DEBUG LOGIN:');
    console.log('Identifiant recherché:', identifierLower);
    console.log('Rôle recherché:', role);
    console.log('Utilisateurs enregistrés:', users);
    
    // Chercher l'utilisateur par identifiant (insensible à la casse) ET rôle
    const foundUser = users.find(u => {
        const match = u.identifier.toLowerCase() === identifierLower && u.role === role;
        console.log(`Vérification: ${u.identifier.toLowerCase()} === ${identifierLower} && ${u.role} === ${role} = ${match}`);
        return match;
    });
    
    if (!foundUser) {
        console.log('❌ Utilisateur non trouvé');
        throw new Error(`Identifiant ou rôle incorrect. Utilisateur '${identifier}' avec le rôle '${role}' n'existe pas.`);
    }
    
    console.log('✅ Utilisateur trouvé:', foundUser);
    
    // Vérifier le mot de passe (décoder depuis base64)
    const storedPassword = atob(foundUser.password);
    console.log('Mot de passe entré:', password);
    console.log('Mot de passe stocké (décodé):', storedPassword);
    console.log('Correspondance:', storedPassword === password);
    
    if (storedPassword !== password) {
        console.log('❌ Mot de passe incorrect');
        throw new Error(`Mot de passe incorrect pour l'utilisateur '${identifier}'`);
    }
    
    // Créer la session utilisateur
    const user = {
        id: foundUser.id,
        identifier: foundUser.identifier,
        email: foundUser.email,
        role: foundUser.role,
        loginTime: new Date().getTime()
    };
    
    console.log('✅ Session créée:', user);
    localStorage.setItem('currentUser', JSON.stringify(user));
    return user;
}

// Déconnexion
function logout() {
    localStorage.removeItem('currentUser');
    window.location.href = 'login.html';
}

// Formater le nom du rôle
function formatRoleName(role) {
    const roleNames = {
        'etudiant': 'Étudiant',
        'formateur': 'Formateur',
        'directeur': 'Directeur'
    };
    return roleNames[role] || role;
}

// Vérifier si l'utilisateur a accès à une page
function hasAccessToPage(pageName) {
    const role = getCurrentRole();
    if (!role) return false;
    
    const permissions = ROLE_PERMISSIONS[role] || [];
    return permissions.includes(pageName);
}

// Vérifier l'accès et rediriger si nécessaire
function checkAccessAndRedirect() {
    if (!isLoggedIn()) {
        window.location.href = 'login.html';
        return false;
    }
    
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    
    // Autoriser index.html et login.html pour tous
    if (currentPage === 'index.html' || currentPage === 'login.html' || currentPage === '') {
        return true;
    }
    
    if (!hasAccessToPage(currentPage)) {
        alert('Vous n\'avez pas accès à cette page.');
        window.location.href = 'index.html';
        return false;
    }
    
    return true;
}

// Obtenir les user stories basées sur le rôle
function getUserStoriesByRole(role) {
    const allStories = [
        {
            id: 'us1',
            title: 'US 1: Créer Espace',
            icon: '📚',
            actions: [
                { text: 'Accueil', href: 'index.html' },
                { text: '➕ Créer un espace vide', href: 'creer-espace.html' },
                { text: '📋 Consulter les espaces', href: 'liste-espaces.html' }
            ],
            roles: ['formateur', 'directeur']
        },
        {
            id: 'us2',
            title: 'US 2: Gérer Formateurs',
            icon: '👤',
            actions: [
                { text: '➕ Créer formateur', href: 'creer-formateur.html' },
                { text: '🔗 Assigner formateur', href: 'ajouter-formateur.html' }
            ],
            roles: ['formateur', 'directeur']
        },
        {
            id: 'us3',
            title: 'US 3: Gérer Étudiants',
            icon: '🎓',
            actions: [
                { text: '➕ Créer étudiant', href: 'creer-etudiant.html' },
                { text: '🔗 Ajouter à espace', href: 'ajouter-etudiant-espace.html' },
                { text: '➕ Ajouter à promotion', href: 'ajouter-etudiant-promotion.html' },
                { text: '📋 Consulter étudiants', href: 'liste-etudiants.html' }
            ],
            roles: ['directeur']
        },
        {
            id: 'us4',
            title: 'US 4: Travaux & Livraisons',
            icon: '📝',
            actions: [
                { text: '➕ Créer travail', href: 'creer-travail.html' },
                { text: '🔗 Assigner travail', href: 'assigner-travail.html' },
                { text: '📋 Liste travaux', href: 'liste-travaux.html' },
                { text: '📤 Soumettre livraison', href: 'soumettre-livraison.html' }
            ],
            roles: ['etudiant', 'formateur', 'directeur']
        },
        {
            id: 'us5',
            title: 'US 5: Évaluation',
            icon: '⭐',
            actions: [
                { text: '📊 Évaluer livraisons', href: 'evaluer-livraisons.html' },
                { text: '📈 Consulter notes', href: 'mes-notes.html' }
            ],
            roles: ['etudiant', 'formateur', 'directeur']
        },
        {
            id: 'us6',
            title: 'US 6: Supervision',
            icon: '👁️',
            actions: [
                { text: '📚 Espaces', href: 'consultation-directeur-espaces.html' },
                { text: '🎓 Étudiants', href: 'consultation-directeur-etudiants.html' },
                { text: '📊 Promotions', href: 'consultation-directeur-promotions.html' }
            ],
            roles: ['directeur']
        }
    ];
    
    return allStories.filter(story => story.roles.includes(role));
}

// Formater le nom d'affichage du rôle
function formatRoleName(role) {
    const names = {
        'etudiant': '👤 Étudiant',
        'formateur': '📚 Formateur',
        'directeur': '👁️ Directeur'
    };
    return names[role] || role;
}
