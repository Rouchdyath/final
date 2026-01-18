// Sidebar minimaliste et belle - Navigation par rôle
function initSidebar() {
    // Vérifier l'authentification
    const currentPage = window.location.pathname.split('/').pop();
    if (currentPage !== 'login.html' && currentPage !== 'signup.html' && currentPage !== '') {
        checkAccessAndRedirect();
    }

    const currentUser = getCurrentUser();
    const userRole = currentUser ? currentUser.role : null;

    // Menu items par rôle
    const menuItems = {
        'etudiant': [
            { icon: '📚', text: 'Mes Travaux', href: 'liste-travaux.html' },
            { icon: '📤', text: 'Soumettre une Livraison', href: 'soumettre-livraison.html' },
            { icon: '⭐', text: 'Mes Notes', href: 'mes-notes.html' }
        ],
        'formateur': [
            { icon: '🏫', text: 'Créer un Espace', href: 'creer-espace.html' },
            { icon: '📋', text: 'Mes Espaces', href: 'liste-espaces.html' },
            { icon: '👨‍🏫', text: 'Gérer Formateurs', href: 'ajouter-formateur.html' },
            { icon: '👨‍🎓', text: 'Ajouter Étudiants', href: 'ajouter-etudiant-espace.html' },
            { icon: '📝', text: 'Créer un Travail', href: 'creer-travail.html' },
            { icon: '📌', text: 'Assigner des Travaux', href: 'assigner-travail.html' },
            { icon: '✅', text: 'Évaluer Livraisons', href: 'evaluer-livraisons.html' },
            { icon: '📊', text: 'Consulter Travaux', href: 'consultation-formateur-travaux.html' },
            { icon: '📂', text: 'Retour Accueil', href: 'index.html' }
        ],
        'directeur': [
            { icon: '🏫', text: 'Créer un Espace', href: 'creer-espace.html' },
            { icon: '📋', text: 'Tous les Espaces', href: 'liste-espaces.html' },
            { icon: '👨‍🏫', text: 'Gérer Formateurs', href: 'ajouter-formateur.html' },
            { icon: '👨‍🎓', text: 'Gérer Étudiants', href: 'creer-etudiant.html' },
            { icon: '📋', text: 'Consulter Étudiants', href: 'consultation-directeur-etudiants.html' },
            { icon: '📝', text: 'Créer Promotion', href: 'creer-promotion.html' },
            { icon: '📊', text: 'Consulter Promotions', href: 'consultation-directeur-promotions.html' },
            { icon: '🎯', text: 'Consulter Espaces', href: 'consultation-directeur-espaces.html' },
            { icon: '📝', text: 'Créer un Travail', href: 'creer-travail.html' },
            { icon: '📌', text: 'Assigner des Travaux', href: 'assigner-travail.html' },
            { icon: '✅', text: 'Évaluer Livraisons', href: 'evaluer-livraisons.html' },
            { icon: '📚', text: 'Tous les Travaux', href: 'liste-travaux.html' },
            { icon: '📂', text: 'Retour Accueil', href: 'index.html' }
        ]
    };

    const items = menuItems[userRole] || [];

    // Créer le HTML du menu
    let menuHTML = items.map((item, index) => `
        <a href="${item.href}" class="menu-item" style="animation-delay: ${index * 50}ms;">
            <span class="menu-icon">${item.icon}</span>
            <span class="menu-text">${item.text}</span>
            <span class="menu-arrow">→</span>
        </a>
    `).join('');

    // Créer la sidebar HTML
    const sidebarHTML = `
        <aside class="sidebar-nav" id="mainSidebar">
            <div class="sidebar-header">
                <div class="user-avatar">${currentUser ? currentUser.identifier.charAt(0).toUpperCase() : '?'}</div>
                <div class="user-details">
                    <div class="user-name">${currentUser ? currentUser.identifier : 'Anonyme'}</div>
                    <div class="user-role">${currentUser ? formatRoleName(currentUser.role) : 'Non authentifié'}</div>
                </div>
            </div>

            <nav class="sidebar-menu">
                ${menuHTML}
            </nav>

            <div class="sidebar-footer">
                <button onclick="logout()" class="btn-logout">
                    <span>🚪</span> Déconnexion
                </button>
            </div>
        </aside>
    `;

    // CSS pour la sidebar
    const sidebarCSS = `
        * {
            box-sizing: border-box;
        }

        body {
            background: #f8f9fa;
        }

        .main-layout {
            display: grid;
            grid-template-columns: 280px 1fr;
            gap: 0;
            min-height: 100vh;
        }

        @media (max-width: 768px) {
            .main-layout {
                grid-template-columns: 1fr;
            }
            
            .sidebar-nav {
                position: fixed;
                left: -280px;
                top: 0;
                height: 100vh;
                z-index: 1000;
                transition: left 0.3s ease;
            }

            .sidebar-nav.open {
                left: 0;
            }
        }

        .sidebar-nav {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px 20px;
            display: flex;
            flex-direction: column;
            position: sticky;
            top: 0;
            height: 100vh;
            overflow-y: auto;
        }

        .sidebar-header {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 1px solid rgba(255,255,255,0.2);
        }

        .user-avatar {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: rgba(255,255,255,0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            font-weight: bold;
            flex-shrink: 0;
        }

        .user-details {
            flex: 1;
            min-width: 0;
        }

        .user-name {
            font-weight: 700;
            font-size: 14px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .user-role {
            font-size: 12px;
            opacity: 0.9;
            margin-top: 4px;
        }

        .sidebar-menu {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin-bottom: 20px;
        }

        .menu-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px 15px;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            transition: all 0.3s ease;
            font-size: 13px;
            font-weight: 500;
            animation: slideIn 0.3s ease forwards;
            opacity: 0;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateX(-20px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        .menu-icon {
            font-size: 18px;
            flex-shrink: 0;
        }

        .menu-text {
            flex: 1;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .menu-arrow {
            font-size: 14px;
            opacity: 0;
            transition: all 0.3s;
            transform: translateX(-10px);
        }

        .menu-item:hover {
            background: rgba(255,255,255,0.2);
            padding-left: 20px;
        }

        .menu-item:hover .menu-arrow {
            opacity: 1;
            transform: translateX(0);
        }

        .sidebar-footer {
            padding-top: 20px;
            border-top: 1px solid rgba(255,255,255,0.2);
        }

        .btn-logout {
            width: 100%;
            padding: 12px 15px;
            background: rgba(255,255,255,0.2);
            color: white;
            border: 1px solid rgba(255,255,255,0.3);
            border-radius: 6px;
            cursor: pointer;
            font-size: 13px;
            font-weight: 600;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        .btn-logout:hover {
            background: rgba(255,255,255,0.3);
            border-color: rgba(255,255,255,0.5);
            transform: scale(1.05);
        }

        .content-main {
            padding: 40px;
            overflow-y: auto;
        }

        .content-main h1 {
            color: #333;
            margin-top: 0;
            margin-bottom: 30px;
            font-size: 32px;
            font-weight: 700;
        }

        @media (max-width: 768px) {
            .main-layout {
                grid-template-columns: 1fr;
            }

            .content-main {
                padding: 20px;
            }

            .content-main h1 {
                font-size: 24px;
            }
        }

        /* Scrollbar personnalisée */
        .sidebar-nav::-webkit-scrollbar {
            width: 6px;
        }

        .sidebar-nav::-webkit-scrollbar-track {
            background: rgba(255,255,255,0.1);
        }

        .sidebar-nav::-webkit-scrollbar-thumb {
            background: rgba(255,255,255,0.3);
            border-radius: 3px;
        }

        .sidebar-nav::-webkit-scrollbar-thumb:hover {
            background: rgba(255,255,255,0.5);
        }
    `;

    // Injecter le CSS
    if (!document.getElementById('sidebarStyles')) {
        const styleTag = document.createElement('style');
        styleTag.id = 'sidebarStyles';
        styleTag.textContent = sidebarCSS;
        document.head.appendChild(styleTag);
    }

    // Chercher le container
    const container = document.querySelector('.container');
    
    if (container && !document.getElementById('mainSidebar')) {
        // Chercher le main
        let mainContent = container.querySelector('main');
        
        if (mainContent) {
            // Créer le wrapper du layout
            const layoutWrapper = document.createElement('div');
            layoutWrapper.className = 'main-layout';
            
            // Insérer la sidebar
            layoutWrapper.innerHTML = sidebarHTML;
            
            // Créer le div pour le contenu
            const contentDiv = document.createElement('div');
            contentDiv.className = 'content-main';
            
            // Cloner le main dans contentDiv
            contentDiv.appendChild(mainContent.cloneNode(true));
            
            // Ajouter le contenu au layout
            layoutWrapper.appendChild(contentDiv);
            
            // Remplacer le main par le layout
            mainContent.replaceWith(layoutWrapper);
        }
    }
}

// Initialiser quand le DOM est chargé
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSidebar);
} else {
    initSidebar();
}
