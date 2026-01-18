from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import EspacePedagogique, Formateur, Etudiant, Promotion, TravailIndividuel, Livraison, AssignationTravail
from .serializers import (
    EspacePedagogiqueSerializer, 
    FormateurSerializer,
    AjouterFormateurSerializer,
    EtudiantSerializer,
    PromotionSerializer,
    AjouterEspacePromotionSerializer,
    AjouterEtudiantPromotionSerializer,
    TravailIndividuelSerializer,
    LivraisonSerializer,
    AjouterEtudiantSerializer,
    AssignationTravailSerializer
)


@api_view(['POST'])
def creer_espace_pedagogique(request):
    """
    Créer un nouvel espace pédagogique vide pour une matière
    Epic: Création d'un espace pédagogique vide pour une matière
    """
    serializer = EspacePedagogiqueSerializer(data=request.data)
    
    if serializer.is_valid():
        espace = serializer.save()
        return Response(
            {
                'success': True,
                'message': 'Espace pédagogique créé avec succès',
                'data': EspacePedagogiqueSerializer(espace).data
            },
            status=status.HTTP_201_CREATED
        )
    
    return Response(
        {
            'success': False,
            'message': 'Erreur lors de la création de l\'espace pédagogique',
            'errors': serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['GET'])
def lister_espaces_pedagogiques(request):
    """Lister tous les espaces pédagogiques"""
    espaces = EspacePedagogique.objects.all()
    serializer = EspacePedagogiqueSerializer(espaces, many=True)
    return Response(
        {
            'success': True,
            'data': serializer.data
        },
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def detail_espace_pedagogique(request, espace_id):
    """Obtenir les détails d'un espace pédagogique"""
    espace = get_object_or_404(EspacePedagogique, id=espace_id)
    serializer = EspacePedagogiqueSerializer(espace)
    return Response(
        {
            'success': True,
            'data': serializer.data
        },
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
def ajouter_formateur_espace(request, espace_id):
    """
    Ajouter un formateur à un espace pédagogique
    Epic: Insertion d'un formateur dans un espace pédagogique
    """
    espace = get_object_or_404(EspacePedagogique, id=espace_id)
    serializer = AjouterFormateurSerializer(data=request.data)
    
    if serializer.is_valid():
        formateur_id = serializer.validated_data['formateur_id']
        formateur = get_object_or_404(Formateur, id=formateur_id)
        
        # Vérifier si le formateur n'est pas déjà dans l'espace
        if espace.formateurs.filter(id=formateur_id).exists():
            return Response(
                {
                    'success': False,
                    'message': 'Ce formateur est déjà assigné à cet espace pédagogique'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Ajouter le formateur
        espace.formateurs.add(formateur)
        
        return Response(
            {
                'success': True,
                'message': 'Formateur ajouté avec succès à l\'espace pédagogique',
                'data': EspacePedagogiqueSerializer(espace).data
            },
            status=status.HTTP_200_OK
        )
    
    return Response(
        {
            'success': False,
            'message': 'Erreur lors de l\'ajout du formateur',
            'errors': serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['GET'])
def lister_formateurs(request):
    """Lister tous les formateurs disponibles"""
    formateurs = Formateur.objects.all()
    serializer = FormateurSerializer(formateurs, many=True)
    return Response(
        {
            'success': True,
            'data': serializer.data
        },
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
def creer_formateur(request):
    """Créer un nouveau formateur"""
    serializer = FormateurSerializer(data=request.data)
    
    if serializer.is_valid():
        formateur = serializer.save()
        return Response(
            {
                'success': True,
                'message': 'Formateur créé avec succès',
                'data': FormateurSerializer(formateur).data
            },
            status=status.HTTP_201_CREATED
        )
    
    return Response(
        {
            'success': False,
            'message': 'Erreur lors de la création du formateur',
            'errors': serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )


# Vues pour les promotions

@api_view(['GET'])
def lister_promotions(request):
    """Lister toutes les promotions"""
    promotions = Promotion.objects.all()
    serializer = PromotionSerializer(promotions, many=True)
    return Response(
        {
            'success': True,
            'data': serializer.data
        },
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
def creer_promotion(request):
    """
    Créer une nouvelle promotion pour une année donnée
    User Story: Création d'une promotion pour une année donnée
    """
    serializer = PromotionSerializer(data=request.data)
    
    if serializer.is_valid():
        promotion = serializer.save()
        return Response(
            {
                'success': True,
                'message': 'Promotion créée avec succès',
                'data': PromotionSerializer(promotion).data
            },
            status=status.HTTP_201_CREATED
        )
    
    return Response(
        {
            'success': False,
            'message': 'Erreur lors de la création de la promotion',
            'errors': serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['GET'])
def detail_promotion(request, promotion_id):
    """Obtenir les détails d'une promotion"""
    promotion = get_object_or_404(Promotion, id=promotion_id)
    serializer = PromotionSerializer(promotion)
    return Response(
        {
            'success': True,
            'data': serializer.data
        },
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
def ajouter_espace_promotion(request, promotion_id):
    """
    Ajouter un espace pédagogique à une promotion
    """
    promotion = get_object_or_404(Promotion, id=promotion_id)
    serializer = AjouterEspacePromotionSerializer(data=request.data)
    
    if serializer.is_valid():
        espace_id = serializer.validated_data['espace_id']
        espace = get_object_or_404(EspacePedagogique, id=espace_id)
        
        # Vérifier si l'espace n'est pas déjà lié à la promotion
        if promotion.espaces.filter(id=espace_id).exists():
            return Response(
                {
                    'success': False,
                    'message': 'Cet espace pédagogique est déjà assigné à cette promotion'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Ajouter l'espace
        promotion.espaces.add(espace)
        
        return Response(
            {
                'success': True,
                'message': f'Espace {espace.nom} - {espace.matiere} ajouté avec succès à la promotion {promotion.nom} ({promotion.annee})',
                'data': PromotionSerializer(promotion).data
            },
            status=status.HTTP_200_OK
        )
    
    return Response(
        {
            'success': False,
            'message': 'Erreur lors de l\'ajout de l\'espace',
            'errors': serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['POST'])
def ajouter_etudiant_promotion(request, promotion_id):
    """
    Ajouter un étudiant à une promotion
    User Story: Ajouter un étudiant dans une promotion donnée
    """
    promotion = get_object_or_404(Promotion, id=promotion_id)
    serializer = AjouterEtudiantPromotionSerializer(data=request.data)
    
    if serializer.is_valid():
        etudiant_id = serializer.validated_data['etudiant_id']
        etudiant = get_object_or_404(Etudiant, id=etudiant_id)
        
        # Vérifier si l'étudiant n'est pas déjà dans la promotion
        if etudiant.promotion_id == promotion_id:
            return Response(
                {
                    'success': False,
                    'message': 'Cet étudiant est déjà assigné à cette promotion'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Assigner l'étudiant à la promotion
        etudiant.promotion = promotion
        etudiant.save()
        
        return Response(
            {
                'success': True,
                'message': f'Étudiant {etudiant.prenom} {etudiant.nom} ajouté avec succès à la promotion {promotion.nom} ({promotion.annee})',
                'data': EtudiantSerializer(etudiant).data
            },
            status=status.HTTP_200_OK
        )
    
    return Response(
        {
            'success': False,
            'message': 'Erreur lors de l\'ajout de l\'étudiant à la promotion',
            'errors': serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )


# Vues pour les étudiants

@api_view(['GET'])
def lister_etudiants(request):
    """Lister tous les étudiants"""
    etudiants = Etudiant.objects.all()
    serializer = EtudiantSerializer(etudiants, many=True)
    return Response(
        {
            'success': True,
            'data': serializer.data
        },
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
def creer_etudiant(request):
    """Créer un nouvel étudiant"""
    serializer = EtudiantSerializer(data=request.data)
    
    if serializer.is_valid():
        etudiant = serializer.save()
        return Response(
            {
                'success': True,
                'message': 'Étudiant créé avec succès',
                'data': EtudiantSerializer(etudiant).data
            },
            status=status.HTTP_201_CREATED
        )
    
    return Response(
        {
            'success': False,
            'message': 'Erreur lors de la création de l\'étudiant',
            'errors': serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['POST'])
def ajouter_etudiant_espace(request):
    """Ajouter un étudiant à un espace pédagogique en utilisant nom et matière"""
    serializer = AjouterEtudiantSerializer(data=request.data)
    
    if serializer.is_valid():
        espace = serializer.validated_data['espace']
        etudiant_id = serializer.validated_data['etudiant_id']
        etudiant = get_object_or_404(Etudiant, id=etudiant_id)
        
        # Vérifier si l'étudiant n'est pas déjà dans l'espace
        if espace.etudiants.filter(id=etudiant_id).exists():
            return Response(
                {
                    'success': False,
                    'message': 'Cet étudiant est déjà inscrit à cet espace pédagogique'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Ajouter l'étudiant
        espace.etudiants.add(etudiant)
        
        return Response(
            {
                'success': True,
                'message': f'Étudiant {etudiant.prenom} {etudiant.nom} ajouté avec succès à l\'espace {espace.nom} - {espace.matiere}',
                'data': EspacePedagogiqueSerializer(espace).data
            },
            status=status.HTTP_200_OK
        )
    
    return Response(
        {
            'success': False,
            'message': 'Erreur lors de l\'ajout de l\'étudiant',
            'errors': serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )


# Vues pour les travaux individuels

@api_view(['GET'])
def lister_travaux_individuels(request):
    """Lister tous les travaux individuels"""
    travaux = TravailIndividuel.objects.all()
    serializer = TravailIndividuelSerializer(travaux, many=True)
    return Response(
        {
            'success': True,
            'data': serializer.data
        },
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
def creer_travail_individuel(request):
    """Créer un nouveau travail individuel"""
    serializer = TravailIndividuelSerializer(data=request.data)
    
    if serializer.is_valid():
        travail = serializer.save()
        return Response(
            {
                'success': True,
                'message': 'Travail individuel créé avec succès',
                'data': TravailIndividuelSerializer(travail).data
            },
            status=status.HTTP_201_CREATED
        )
    
    return Response(
        {
            'success': False,
            'message': 'Erreur lors de la création du travail individuel',
            'errors': serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['GET'])
def travaux_par_espace(request, espace_id):
    """Lister les travaux individuels d'un espace pédagogique"""
    espace = get_object_or_404(EspacePedagogique, id=espace_id)
    travaux = espace.travaux_individuels.all()
    serializer = TravailIndividuelSerializer(travaux, many=True)
    return Response(
        {
            'success': True,
            'data': serializer.data
        },
        status=status.HTTP_200_OK
    )


# Vues pour les livraisons

@api_view(['GET'])
def lister_livraisons(request):
    """Lister toutes les livraisons"""
    livraisons = Livraison.objects.all()
    serializer = LivraisonSerializer(livraisons, many=True)
    return Response(
        {
            'success': True,
            'data': serializer.data
        },
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
def soumettre_livraison(request):
    """Soumettre une livraison pour un travail individuel"""
    serializer = LivraisonSerializer(data=request.data)
    
    if serializer.is_valid():
        livraison = serializer.save()
        return Response(
            {
                'success': True,
                'message': 'Livraison soumise avec succès',
                'data': LivraisonSerializer(livraison).data
            },
            status=status.HTTP_201_CREATED
        )
    
    return Response(
        {
            'success': False,
            'message': 'Erreur lors de la soumission de la livraison',
            'errors': serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['GET'])
def livraisons_par_etudiant(request, etudiant_id):
    """Lister les livraisons d'un étudiant"""
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)
    livraisons = etudiant.livraisons.all()
    serializer = LivraisonSerializer(livraisons, many=True)
    return Response(
        {
            'success': True,
            'data': serializer.data
        },
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def livraisons_par_travail(request, travail_id):
    """Lister les livraisons pour un travail individuel"""
    travail = get_object_or_404(TravailIndividuel, id=travail_id)
    livraisons = travail.livraisons.all()
    serializer = LivraisonSerializer(livraisons, many=True)
    return Response(
        {
            'success': True,
            'data': serializer.data
        },
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
def assigner_travail_etudiant(request):
    """
    Assigner un travail à un étudiant
    Body: {'travail_id': int, 'etudiant_id': int}
    """
    serializer = AssignationTravailSerializer(data=request.data)
    
    if serializer.is_valid():
        assignation = serializer.save()
        return Response(
            {
                'success': True,
                'message': 'Travail assigné avec succès',
                'data': AssignationTravailSerializer(assignation).data
            },
            status=status.HTTP_201_CREATED
        )
    
    return Response(
        {
            'success': False,
            'message': 'Erreur lors de l\'assignation du travail',
            'errors': serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['GET'])
def travaux_assignes_etudiant(request, etudiant_id):
    """Lister les travaux assignés à un étudiant"""
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)
    assignations = etudiant.travaux_assignes.all()
    serializer = AssignationTravailSerializer(assignations, many=True)
    return Response(
        {
            'success': True,
            'data': serializer.data
        },
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def travaux_assignes_formateur(request, espace_id, formateur_id=None):
    """
    Lister les travaux assignés dans un espace pédagogique
    Le formateur peut consulter les travaux assignés aux étudiants de ses espaces
    """
    espace = get_object_or_404(EspacePedagogique, id=espace_id)
    
    # Récupérer tous les travaux de l'espace
    travaux = espace.travailindividuel_set.all()
    
    result_data = []
    for travail in travaux:
        assignations = travail.assignations.all()
        travail_data = TravailIndividuelSerializer(travail).data
        travail_data['assignations'] = AssignationTravailSerializer(assignations, many=True).data
        result_data.append(travail_data)
    
    return Response(
        {
            'success': True,
            'espace': EspacePedagogiqueSerializer(espace).data,
            'travaux': result_data
        },
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def travaux_par_etudiant_formateur(request, etudiant_id):
    """
    Lister les travaux assignés à un étudiant
    Endpoint utilisé par les formateurs pour consulter les travaux assignés
    """
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)
    assignations = etudiant.travaux_assignes.all()
    
    result_data = []
    for assignation in assignations:
        assignation_data = AssignationTravailSerializer(assignation).data
        assignation_data['etudiant'] = EtudiantSerializer(etudiant).data
        result_data.append(assignation_data)
    
    return Response(
        {
            'success': True,
            'etudiant': EtudiantSerializer(etudiant).data,
            'travaux_assignes': result_data
        },
        status=status.HTTP_200_OK
    )


@api_view(['PATCH'])
def mettre_a_jour_assignation(request, assignation_id):
    """
    Mettre à jour le statut ou les notes d'une assignation
    Body: {'statut': 'en_cours|complété|évalué', 'notes': 'texte'}
    """
    assignation = get_object_or_404(AssignationTravail, id=assignation_id)
    serializer = AssignationTravailSerializer(assignation, data=request.data, partial=True)
    
    if serializer.is_valid():
        assignation = serializer.save()
        return Response(
            {
                'success': True,
                'message': 'Assignation mise à jour avec succès',
                'data': AssignationTravailSerializer(assignation).data
            },
            status=status.HTTP_200_OK
        )
    
    return Response(
        {
            'success': False,
            'message': 'Erreur lors de la mise à jour de l\'assignation',
            'errors': serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['POST'])
def evaluer_livraison(request, livraison_id):
    """
    Évaluer une livraison (ajouter notes, points, commentaires)
    Body: {'notes': 18.5, 'points': 90, 'commentaire_evaluation': 'Excellent travail!'}
    """
    livraison = get_object_or_404(Livraison, id=livraison_id)
    
    # Récupérer les données d'évaluation
    notes = request.data.get('notes')
    points = request.data.get('points')
    commentaire = request.data.get('commentaire_evaluation')
    
    # Validation
    if notes is None and points is None:
        return Response(
            {
                'success': False,
                'message': 'Vous devez fournir au moins des notes ou des points'
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Validation des notes (0-20)
    if notes is not None:
        try:
            notes_float = float(notes)
            if notes_float < 0 or notes_float > 20:
                return Response(
                    {
                        'success': False,
                        'message': 'Les notes doivent être entre 0 et 20'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        except (ValueError, TypeError):
            return Response(
                {
                    'success': False,
                    'message': 'Les notes doivent être un nombre'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    
    # Validation des points
    if points is not None:
        try:
            points_int = int(points)
            if points_int < 0:
                return Response(
                    {
                        'success': False,
                        'message': 'Les points doivent être positifs'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        except (ValueError, TypeError):
            return Response(
                {
                    'success': False,
                    'message': 'Les points doivent être un nombre entier'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    
    # Mettre à jour la livraison
    from django.utils import timezone
    if notes is not None:
        livraison.notes = float(notes)
    if points is not None:
        livraison.points = int(points)
    if commentaire:
        livraison.commentaire_evaluation = commentaire
    livraison.date_evaluation = timezone.now()
    
    # Essayer d'ajouter le formateur si on a un user_id
    try:
        formateur_id = request.data.get('formateur_id')
        if formateur_id:
            formateur = Formateur.objects.get(id=formateur_id)
            livraison.evaluateur = formateur
    except:
        pass
    
    livraison.save()
    
    return Response(
        {
            'success': True,
            'message': 'Livraison évaluée avec succès',
            'data': LivraisonSerializer(livraison).data
        },
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def livraisons_a_evaluer_par_travail(request, travail_id):
    """
    Lister toutes les livraisons pour un travail (non évaluées)
    Utile pour le formateur qui doit corriger
    """
    travail = get_object_or_404(TravailIndividuel, id=travail_id)
    
    # Récupérer toutes les livraisons pour ce travail
    livraisons = travail.livraisons.all()
    
    # Optionnellement filtrer les non évaluées
    filter_non_evaluees = request.query_params.get('non_evaluees', 'false').lower() == 'true'
    if filter_non_evaluees:
        livraisons = livraisons.filter(notes__isnull=True, points__isnull=True)
    
    serializer = LivraisonSerializer(livraisons, many=True)
    
    return Response(
        {
            'success': True,
            'travail': TravailIndividuelSerializer(travail).data,
            'total_livraisons': livraisons.count(),
            'evaluees': travail.livraisons.exclude(notes__isnull=True, points__isnull=True).count() if not filter_non_evaluees else 0,
            'data': serializer.data
        },
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def notes_etudiant(request, etudiant_id):
    """
    Consulter les notes d'un étudiant pour tous ses travaux
    """
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)
    
    # Récupérer toutes les livraisons de l'étudiant
    livraisons = etudiant.livraisons.all()
    
    # Organiser par travail
    livraisons_evaluees = []
    livraisons_non_evaluees = []
    
    for livraison in livraisons:
        data = {
            'id': livraison.id,
            'travail': TravailIndividuelSerializer(livraison.travail).data,
            'date_soumission': livraison.date_soumission,
            'notes': livraison.notes,
            'points': livraison.points,
            'commentaire': livraison.commentaire_evaluation,
            'date_evaluation': livraison.date_evaluation,
        }
        
        if livraison.est_evaluee:
            livraisons_evaluees.append(data)
        else:
            livraisons_non_evaluees.append(data)
    
    # Calculer les statistiques
    notes_list = [l['notes'] for l in livraisons_evaluees if l['notes'] is not None]
    points_list = [l['points'] for l in livraisons_evaluees if l['points'] is not None]
    
    stats = {}
    if notes_list:
        stats['moyenne_notes'] = round(sum(notes_list) / len(notes_list), 2)
        stats['meilleure_note'] = max(notes_list)
        stats['pire_note'] = min(notes_list)
    
    if points_list:
        stats['total_points'] = sum(points_list)
        stats['moyenne_points'] = round(sum(points_list) / len(points_list), 2)
    
    return Response(
        {
            'success': True,
            'etudiant': EtudiantSerializer(etudiant).data,
            'livraisons_evaluees': livraisons_evaluees,
            'livraisons_non_evaluees': livraisons_non_evaluees,
            'statistiques': stats
        },
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def notes_par_travail_etudiant(request, etudiant_id, travail_id):
    """
    Consulter les notes d'un étudiant pour un travail spécifique
    """
    livraison = get_object_or_404(Livraison, etudiant_id=etudiant_id, travail_id=travail_id)
    
    return Response(
        {
            'success': True,
            'data': LivraisonSerializer(livraison).data
        },
        status=status.HTTP_200_OK
    )

