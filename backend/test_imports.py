import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
import django
django.setup()

from espaces_pedagogiques.models import Promotion, Etudiant, AssignationTravail, TravailIndividuel
from espaces_pedagogiques.serializers import (
    PromotionSerializer, 
    EtudiantSerializer, 
    AjouterEspacePromotionSerializer,
    AssignationTravailSerializer,
    TravailIndividuelSerializer
)

print('✓ Tous les imports sont OK')
print('✓ Modèles chargés: Promotion, Etudiant, AssignationTravail, TravailIndividuel')
print('✓ Sérializers chargés: PromotionSerializer, EtudiantSerializer, AssignationTravailSerializer, TravailIndividuelSerializer')
print('✓ Vérification complète réussie!')
