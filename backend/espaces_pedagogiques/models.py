from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone


class Promotion(models.Model):
    """Modèle pour représenter une promotion d'étudiants"""
    nom = models.CharField(
        max_length=100,
        verbose_name="Nom de la promotion",
        validators=[MinLengthValidator(2)]
    )
    annee = models.IntegerField(
        verbose_name="Année de la promotion",
        help_text="Ex: 2024 pour la promotion 2024-2025"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    espaces = models.ManyToManyField(
        'EspacePedagogique',
        related_name='promotions',
        blank=True,
        verbose_name="Espaces pédagogiques"
    )
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    
    class Meta:
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"
        ordering = ['-annee', 'nom']
        unique_together = ['nom', 'annee']
    
    def __str__(self):
        return f"{self.nom} ({self.annee})"


class Formateur(models.Model):
    """Modèle pour représenter un formateur"""
    nom = models.CharField(max_length=100, verbose_name="Nom")
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    email = models.EmailField(unique=True, verbose_name="Email")
    telephone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Téléphone")
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    
    class Meta:
        verbose_name = "Formateur"
        verbose_name_plural = "Formateurs"
        ordering = ['nom', 'prenom']
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"


class EspacePedagogique(models.Model):
    """Modèle pour représenter un espace pédagogique"""
    nom = models.CharField(
        max_length=200,
        verbose_name="Nom de l'espace",
        validators=[MinLengthValidator(2)]
    )
    matiere = models.CharField(
        max_length=200, 
        verbose_name="Matière",
        validators=[MinLengthValidator(2)]
    )
    code = models.CharField(
        max_length=50, 
        unique=True, 
        verbose_name="Code",
        validators=[MinLengthValidator(2)]
    )
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    formateurs = models.ManyToManyField(
        Formateur, 
        related_name='espaces_pedagogiques',
        blank=True,
        verbose_name="Formateurs"
    )
    
    class Meta:
        verbose_name = "Espace pédagogique"
        verbose_name_plural = "Espaces pédagogiques"
        ordering = ['nom', 'matiere']
    
    def __str__(self):
        return f"{self.nom} - {self.matiere} ({self.code})"


class Etudiant(models.Model):
    """Modèle pour représenter un étudiant"""
    nom = models.CharField(max_length=100, verbose_name="Nom")
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    email = models.EmailField(unique=True, verbose_name="Email")
    telephone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Téléphone")
    promotion = models.ForeignKey(
        Promotion,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='etudiants',
        verbose_name="Promotion"
    )
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    espaces = models.ManyToManyField(
        EspacePedagogique, 
        related_name='etudiants',
        blank=True,
        verbose_name="Espaces pédagogiques"
    )
    
    class Meta:
        verbose_name = "Étudiant"
        verbose_name_plural = "Étudiants"
        ordering = ['nom', 'prenom']
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"


class TravailIndividuel(models.Model):
    """Modèle pour représenter un travail individuel ou collectif"""
    TYPES_TRAVAIL = [
        ('individuel', 'Individuel'),
        ('collectif', 'Collectif'),
    ]
    
    titre = models.CharField(max_length=200, verbose_name="Titre")
    description = models.TextField(verbose_name="Description")
    type_travail = models.CharField(
        max_length=20,
        choices=TYPES_TRAVAIL,
        default='individuel',
        verbose_name="Type de travail"
    )
    consignes = models.TextField(verbose_name="Consignes détaillées")
    date_echeance = models.DateTimeField(verbose_name="Date d'échéance")
    espace = models.ForeignKey(
        EspacePedagogique, 
        on_delete=models.CASCADE, 
        related_name='travaux_individuels', 
        verbose_name="Espace pédagogique"
    )
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    
    class Meta:
        verbose_name = "Travail Individuel"
        verbose_name_plural = "Travaux Individuels"
        ordering = ['-date_echeance']
    
    def __str__(self):
        return f"{self.titre} ({self.get_type_travail_display()}) - {self.espace.code}"


class AssignationTravail(models.Model):
    """Modèle pour représenter l'assignation d'un travail à un étudiant"""
    etudiant = models.ForeignKey(
        Etudiant,
        on_delete=models.CASCADE,
        related_name='travaux_assignes',
        verbose_name="Étudiant"
    )
    travail = models.ForeignKey(
        TravailIndividuel,
        on_delete=models.CASCADE,
        related_name='assignations',
        verbose_name="Travail"
    )
    date_assignation = models.DateTimeField(auto_now_add=True, verbose_name="Date d'assignation")
    statut = models.CharField(
        max_length=20,
        choices=[
            ('assigné', 'Assigné'),
            ('en_cours', 'En cours'),
            ('complété', 'Complété'),
            ('évalué', 'Évalué'),
        ],
        default='assigné',
        verbose_name="Statut"
    )
    notes = models.TextField(blank=True, null=True, verbose_name="Notes du formateur")
    
    class Meta:
        verbose_name = "Assignation de Travail"
        verbose_name_plural = "Assignations de Travail"
        unique_together = ['etudiant', 'travail']
        ordering = ['-date_assignation']
    
    def __str__(self):
        return f"{self.etudiant.prenom} {self.etudiant.nom} - {self.travail.titre}"


class Livraison(models.Model):
    """Modèle pour représenter une livraison de production"""
    etudiant = models.ForeignKey(
        Etudiant, 
        on_delete=models.CASCADE, 
        related_name='livraisons', 
        verbose_name="Étudiant"
    )
    travail = models.ForeignKey(
        TravailIndividuel, 
        on_delete=models.CASCADE, 
        related_name='livraisons', 
        verbose_name="Travail Individuel"
    )
    contenu = models.TextField(verbose_name="Contenu de la livraison")
    fichier = models.FileField(
        upload_to='livraisons/', 
        blank=True, 
        null=True, 
        verbose_name="Fichier joint"
    )
    date_soumission = models.DateTimeField(auto_now_add=True, verbose_name="Date de soumission")
    
    # Champs d'évaluation ✨ NOUVEAUX
    notes = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        blank=True, 
        null=True, 
        verbose_name="Note obtenue",
        help_text="Note sur 20 ou autre échelle"
    )
    points = models.IntegerField(
        blank=True, 
        null=True, 
        verbose_name="Points obtenues",
        help_text="Points numériques"
    )
    commentaire_evaluation = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Commentaire d'évaluation",
        help_text="Feedback du formateur"
    )
    date_evaluation = models.DateTimeField(
        blank=True, 
        null=True, 
        verbose_name="Date d'évaluation",
        auto_now=False
    )
    evaluateur = models.ForeignKey(
        Formateur,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='evaluations',
        verbose_name="Formateur Évaluateur"
    )
    
    class Meta:
        verbose_name = "Livraison"
        verbose_name_plural = "Livraisons"
        ordering = ['-date_soumission']
        unique_together = ['etudiant', 'travail']  # Une livraison par étudiant par travail
    
    def __str__(self):
        return f"Livraison de {self.etudiant} pour {self.travail.titre}"
    
    @property
    def est_evaluee(self):
        """Vérifier si la livraison a été évaluée"""
        return self.notes is not None or self.points is not None

