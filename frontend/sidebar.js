// Sidebar simple et fonctionnel
function initSidebar() {
    // Attendre que l'utilisateur soit connecté
    const currentUser = getCurrentUser();
    if (!currentUser) {
        console.log('User not logged in, skipping sidebar init');
        return;
    }

    const userRole = currentUser.role;
    const container = document.getElementById('sidebar-wrapper');
    
    if (!container) {
        console.log('No sidebar container found');
        return;
    }

    // Menu par rôle - Groupé
    const menus = {
        'etudiant': [
            { title: 'Mes Études', icon: '📚', items: [
                { text: 'Mes Travaux', href: 'mes-travaux.html', icon: '📖' },
                { text: 'Soumettre une Livraison', href: 'soumettre-livraison.html', icon: '📤' },
                { text: 'Mes Livraisons', href: 'mes-livraisons.html', icon: '📦' },
                { text: 'Mes Notes', href: 'mes-notes.html', icon: '⭐' },
                { text: 'Accueil', href: 'index.html', icon: '🏠' }
            ]}
        ],
        'formateur': [
            { title: 'Mes Espaces', icon: '🏫', items: [
                { text: 'Voir Mes Espaces', href: 'mes-espaces-formateur.html', icon: '📋' }
            ]},
            { title: 'Travaux & Étudiants', icon: '📝', items: [
                { text: 'Créer un Travail', href: 'creer-travail.html', icon: '➕' },
                { text: 'Assigner des Travaux', href: 'assigner-travail-formateur.html', icon: '📌' },
                { text: 'Consulter Travaux', href: 'consultation-formateur-travaux.html', icon: '📊' },
                { text: 'Consulter Étudiants', href: 'consultation-formateur-etudiants.html', icon: '👁️' },
                { text: 'Évaluer Livraisons', href: 'evaluer-livraisons.html', icon: '✅' }
            ]},
            { title: 'Navigation', icon: '🔗', items: [
                { text: 'Accueil', href: 'index.html', icon: '🏠' }
            ]}
        ],
        'directeur': [
            { title: 'Espaces', icon: '🏫', items: [
                { text: 'Créer un Espace', href: 'creer-espace.html', icon: '➕' },
                { text: 'Tous les Espaces', href: 'liste-espaces.html', icon: '📋' },
                { text: 'Assigner Espaces', href: 'ajouter-espace.html', icon: '📌' },
                { text: 'Consulter Espaces', href: 'consultation-directeur-espaces.html', icon: '👁️' }
            ]},
            { title: 'Équipe', icon: '👥', items: [
                { text: 'Gérer Formateurs', href: 'ajouter-formateur.html', icon: '👨‍🏫' },
                { text: 'Créer Formateur', href: 'creer-formateur.html', icon: '➕' },
                { text: 'Lister Étudiants', href: 'liste-etudiants.html', icon: '👨‍🎓' },
                { text: 'Créer Étudiant', href: 'creer-etudiant.html', icon: '➕' },
                { text: 'Consulter Étudiants', href: 'consultation-directeur-etudiants.html', icon: '👁️' }
            ]},
            { title: 'Promotions', icon: '📊', items: [
                { text: 'Lister Promotions', href: 'liste-promotions.html', icon: '📋' },
                { text: 'Créer Promotion', href: 'creer-promotion.html', icon: '➕' },
                { text: 'Assigner Étudiants', href: 'ajouter-etudiant-promotion.html', icon: '👨‍🎓' },
                { text: 'Consulter Promotions', href: 'consultation-directeur-promotions.html', icon: '👁️' },
                { text: 'Classement', href: 'classement.html', icon: '🏆' }
            ]},
            { title: 'Travaux', icon: '📝', items: [
                { text: 'Créer un Travail', href: 'creer-travail.html', icon: '➕' },
                { text: 'Tous les Travaux', href: 'consultation-directeur-travaux.html', icon: '📋' },
                { text: 'Assigner des Travaux', href: 'assigner-travail.html', icon: '📌' },
                { text: 'Évaluer Livraisons', href: 'evaluer-livraisons.html', icon: '✅' }
            ]},
            { title: 'Système', icon: '⚙️', items: [
                { text: 'Base de Données', href: 'admin-database.html', icon: '📊' },
                { text: 'Accueil', href: 'index.html', icon: '🏠' }
            ]}
        ]
    };

    const userMenus = menus[userRole] || [];

    // Générer le HTML du sidebar
    let html = `
        <div class="sidebar-nav">
            <div class="sidebar-header">
                <div class="user-avatar">${currentUser.identifier.charAt(0).toUpperCase()}</div>
                <div class="user-info">
                    <div class="user-name">${currentUser.identifier}</div>
                    <div class="user-role">${userRole.charAt(0).toUpperCase() + userRole.slice(1)}</div>
                </div>
            </div>

            <nav class="sidebar-menu">`;

    userMenus.forEach((group, idx) => {
        html += `
            <div class="menu-group" style="animation-delay: ${idx * 0.05}s;">
                <button class="menu-group-btn" onclick="toggleMenu(this)" type="button">
                    <span class="menu-icon">${group.icon}</span>
                    <span class="menu-text">${group.title}</span>
                    <span class="toggle-arrow">▼</span>
                </button>
                <div class="submenu">`;
        
        group.items.forEach((item, itemIdx) => {
            html += `
                    <a href="${item.href}" class="menu-item" style="animation-delay: ${(idx + itemIdx * 0.02) * 0.05}s;">
                        <span class="menu-icon">${item.icon}</span>
                        <span class="menu-text">${item.text}</span>
                    </a>`;
        });
        
        html += `
                </div>
            </div>`;
    });

    html += `
            </nav>

            <div class="sidebar-footer">
                <button class="btn-logout" onclick="logout()" type="button">
                    🚪 Déconnexion
                </button>
            </div>
        </div>`;

    container.innerHTML = html;
}

function toggleMenu(btn) {
    const menu = btn.nextElementSibling;
    if (menu && menu.classList.contains('submenu')) {
        menu.classList.toggle('open');
        btn.classList.toggle('active');
    }
}

// Injecter les styles CSS
const styles = `
    .sidebar-nav {
        display: flex;
        flex-direction: column;
        height: 100%;
        background: white;
    }

    .sidebar-header {
        padding: 25px 20px;
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        color: white;
        display: flex;
        align-items: center;
        gap: 15px;
        border-bottom: 2px solid #3498db;
        flex-shrink: 0;
    }

    .user-avatar {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: #3498db;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 24px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
        flex-shrink: 0;
    }

    .user-info {
        flex: 1;
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
        margin-top: 2px;
        text-transform: uppercase;
    }

    .sidebar-menu {
        flex: 1;
        overflow-y: auto;
        padding: 15px 0;
    }

    .menu-group {
        margin-bottom: 10px;
        animation: slideInLeft 0.4s ease forwards;
    }

    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    .menu-group-btn {
        width: 100%;
        padding: 15px 20px;
        background: white;
        border: none;
        display: flex;
        align-items: center;
        gap: 12px;
        font-size: 14px;
        font-weight: 600;
        color: #333;
        cursor: pointer;
        transition: all 0.3s;
        border-left: 3px solid transparent;
    }

    .menu-group-btn:hover {
        background: #f5f5f5;
        border-left-color: #3498db;
        padding-left: 25px;
    }

    .menu-group-btn.active {
        color: #3498db;
    }

    .toggle-arrow {
        margin-left: auto;
        font-size: 12px;
        transition: transform 0.3s;
    }

    .menu-group-btn.active .toggle-arrow {
        transform: rotate(180deg);
    }

    .menu-icon {
        font-size: 18px;
        flex-shrink: 0;
    }

    .menu-text {
        flex: 1;
        text-align: left;
    }

    .submenu {
        max-height: 0;
        overflow: hidden;
        transition: max-height 0.3s ease;
        background: #f9f9f9;
    }

    .submenu.open {
        max-height: 500px;
    }

    .menu-item {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 12px 40px;
        color: #555;
        text-decoration: none;
        font-size: 13px;
        transition: all 0.3s;
        border-left: 3px solid transparent;
        animation: slideInLeft 0.3s ease forwards;
    }

    .menu-item:hover {
        background: white;
        border-left-color: #3498db;
        padding-left: 45px;
        color: #2c3e50;
        font-weight: 500;
    }

    .sidebar-footer {
        padding: 20px;
        border-top: 1px solid #e0e0e0;
        flex-shrink: 0;
    }

    .btn-logout {
        width: 100%;
        padding: 12px 15px;
        background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
        color: white;
        border: none;
        border-radius: 6px;
        font-size: 14px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
    }

    .btn-logout:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(231, 76, 60, 0.3);
    }

    .sidebar-menu::-webkit-scrollbar {
        width: 6px;
    }

    .sidebar-menu::-webkit-scrollbar-track {
        background: #f0f0f0;
    }

    .sidebar-menu::-webkit-scrollbar-thumb {
        background: #bbb;
        border-radius: 3px;
    }

    .sidebar-menu::-webkit-scrollbar-thumb:hover {
        background: #999;
    }
`;

const styleEl = document.createElement('style');
styleEl.textContent = styles;
document.head.appendChild(styleEl);

// Initialiser quand le DOM est prêt
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSidebar);
} else {
    initSidebar();
}
