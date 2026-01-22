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

// Normaliser / migrer les données stockées en localStorage (compat avec anciennes versions)
function normalizeLocalData() {
    const users = JSON.parse(localStorage.getItem('app_users') || '[]');
    if (!users.length) return;

    const byId = new Map(users.map(u => [u.id, u]));
    const byIdentifier = new Map(users.filter(u => u.identifier).map(u => [String(u.identifier).toLowerCase(), u]));
    const byEmail = new Map(users.filter(u => u.email).map(u => [String(u.email).toLowerCase(), u]));

    const toUserId = (value) => {
        if (!value) return value;
        const v = String(value);
        if (byId.has(v)) return v;
        const lower = v.toLowerCase();
        const u = byIdentifier.get(lower) || byEmail.get(lower);
        return u ? u.id : value;
    };

    // Espaces: convertir formateurs/etudiants -> ids
    const espaces = JSON.parse(localStorage.getItem('espaces') || '[]');
    if (Array.isArray(espaces) && espaces.length) {
        espaces.forEach(e => {
            if (Array.isArray(e.formateurs)) e.formateurs = e.formateurs.map(toUserId);
            if (Array.isArray(e.etudiants)) e.etudiants = e.etudiants.map(toUserId);
        });
        localStorage.setItem('espaces', JSON.stringify(espaces));
    }

    // Promotions: convertir etudiants/formateurs -> ids (si présents)
    const promotions = JSON.parse(localStorage.getItem('promotions') || '[]');
    if (Array.isArray(promotions) && promotions.length) {
        promotions.forEach(p => {
            if (Array.isArray(p.etudiants)) p.etudiants = p.etudiants.map(toUserId);
            if (Array.isArray(p.formateurs)) p.formateurs = p.formateurs.map(toUserId);
        });
        localStorage.setItem('promotions', JSON.stringify(promotions));
    }

    // Travaux: assurer createdBy (si ancienne donnée contient "formateur" email/identifier)
    const travaux = JSON.parse(localStorage.getItem('travaux') || '[]');
    if (Array.isArray(travaux) && travaux.length) {
        travaux.forEach(t => {
            if (!t.createdBy && t.formateur) {
                const v = String(t.formateur).toLowerCase();
                const u = byEmail.get(v) || byIdentifier.get(v);
                if (u) t.createdBy = u.id;
            }
            if (Array.isArray(t.assignations)) t.assignations = t.assignations.map(toUserId);
        });
        localStorage.setItem('travaux', JSON.stringify(travaux));
    }

    // Livraisons: convertir etudiantId -> id (ancienne démo utilisait parfois "etudiant1"...)
    const livraisons = JSON.parse(localStorage.getItem('livraisons') || '[]');
    if (Array.isArray(livraisons) && livraisons.length) {
        livraisons.forEach(l => {
            if (l.etudiantId) l.etudiantId = toUserId(l.etudiantId);
        });
        localStorage.setItem('livraisons', JSON.stringify(livraisons));
    }
}

normalizeLocalData();

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
        ,'classement.html'
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

// Connexion (rôle auto-détecté)
// Compat: si un 3e paramètre `role` est fourni, on filtre aussi par rôle.
function login(identifier, password, role) {
    const users = JSON.parse(localStorage.getItem('app_users') || '[]');
    const identifierLower = (identifier || '').toLowerCase().trim();

    const foundUser = users.find(u => {
        const idMatch =
            (u.identifier && u.identifier.toLowerCase() === identifierLower) ||
            (u.email && u.email.toLowerCase() === identifierLower);

        if (!idMatch) return false;
        if (role) return u.role === role;
        return true;
    });

    if (!foundUser) {
        throw new Error("Compte introuvable.");
    }

    const storedPassword = atob(foundUser.password || '');
    if (storedPassword !== password) {
        throw new Error("Mot de passe incorrect.");
    }

    const user = {
        id: foundUser.id,
        identifier: foundUser.identifier,
        email: foundUser.email,
        role: foundUser.role,
        loginTime: new Date().getTime()
    };

    localStorage.setItem('currentUser', JSON.stringify(user));
    return user;
}

// Déconnexion
function logout() {
    localStorage.removeItem('currentUser');
    window.location.href = 'login.html';
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

// (formatRoleName est défini une seule fois plus haut)
