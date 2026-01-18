from rest_framework import serializers
from .models import EspacePedagogique, Formateur, Etudiant, Promotion, TravailIndividuel, Livraison, AssignationTravail


class FormateurSerializer(serializers.ModelSerializer):
    """Serializer pour le modèle Formateur"""
    class Meta:
        model = Formateur
        fields = ['id', 'nom', 'prenom', 'email', 'telephone', 'date_creation']


class PromotionSerializer(serializers.ModelSerializer):
    """Serializer pour le modèle Promotion"""
    nombre_etudiants = serializers.SerializerMethodField()
    nombre_espaces = serializers.SerializerMethodField()
    
    class Meta:
        model = Promotion
        fields = ['id', 'nom', 'annee', 'description', 'date_creation', 'nombre_etudiants', 'nombre_espaces']
        read_only_fields = ['id', 'date_creation']
    
    def get_nombre_etudiants(self, obj):
        return obj.etudiants.count()
    
    def get_nombre_espaces(self, obj):
        return obj.espaces.count()
    
    def validate(self, data):
        """Valider que la combinaison nom/année est unique"""
        nom = data.get('nom')
        annee = data.get('annee')
        
        # Si c'est une mise à jour
        if self.instance:
            if self.instance.nom == nom and self.instance.annee == annee:
                return data
        
        if Promotion.objects.filter(nom=nom, annee=annee).exists():
            raise serializers.ValidationError("Une promotion avec ce nom et cette année existe déjà.")
        
        return data


class AjouterEspacePromotionSerializer(serializers.Serializer):
    """Serializer pour ajouter un espace pédagogique à une promotion"""
    espace_id = serializers.IntegerField(required=True)
    
    def validate_espace_id(self, value):
        if not EspacePedagogique.objects.filter(id=value).exists():
            raise serializers.ValidationError("Cet espace pédagogique n'existe pas.")
        return value


class AjouterEtudiantPromotionSerializer(serializers.Serializer):
    """Serializer pour ajouter un étudiant à une promotion"""
    etudiant_id = serializers.IntegerField(required=True)
    
    def validate_etudiant_id(self, value):
        if not Etudiant.objects.filter(id=value).exists():
            raise serializers.ValidationError("Cet étudiant n'existe pas.")
        return value


class EspacePedagogiqueSerializer(serializers.ModelSerializer):
    """Serializer pour le modèle EspacePedagogique"""
    formateurs = FormateurSerializer(many=True, read_only=True)
    nombre_formateurs = serializers.SerializerMethodField()
    
    class Meta:
        model = EspacePedagogique
        fields = ['id', 'nom', 'matiere', 'code', 'description', 'date_creation', 'formateurs', 'nombre_formateurs']
        read_only_fields = ['id', 'date_creation']
    
    def get_nombre_formateurs(self, obj):
        return obj.formateurs.count()
    
    def validate_code(self, value):
        """Valider que le code est unique"""
        if self.instance and self.instance.code == value:
            return value
        if EspacePedagogique.objects.filter(code=value).exists():
            raise serializers.ValidationError("Un espace pédagogique avec ce code existe déjà.")
        return value


class AjouterFormateurSerializer(serializers.Serializer):
    """Serializer pour ajouter un formateur à un espace pédagogique"""
    formateur_id = serializers.IntegerField(required=True)
    
    def validate_formateur_id(self, value):
        if not Formateur.objects.filter(id=value).exists():
            raise serializers.ValidationError("Ce formateur n'existe pas.")
        return value


class AjouterEtudiantSerializer(serializers.Serializer):
    """Serializer pour ajouter un étudiant à un espace pédagogique en utilisant nom et matière"""
    nom_espace = serializers.CharField(required=True)
    matiere = serializers.CharField(required=True)
    etudiant_id = serializers.IntegerField(required=True)
    
    def validate_etudiant_id(self, value):
        if not Etudiant.objects.filter(id=value).exists():
            raise serializers.ValidationError("Cet étudiant n'existe pas.")
        return value
    
    def validate(self, data):
        nom_espace = data.get('nom_espace')
        matiere = data.get('matiere')
        
        try:
            espace = EspacePedagogique.objects.get(nom=nom_espace, matiere=matiere)
            data['espace'] = espace
        except EspacePedagogique.DoesNotExist:
            raise serializers.ValidationError("Aucun espace pédagogique trouvé avec ce nom et cette matière.")
        
        return data


class EtudiantSerializer(serializers.ModelSerializer):
    """Serializer pour le modèle Etudiant"""
    espaces = EspacePedagogiqueSerializer(many=True, read_only=True)
    promotion = PromotionSerializer(read_only=True)
    promotion_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)
    
    class Meta:
        model = Etudiant
        fields = ['id', 'nom', 'prenom', 'email', 'telephone', 'promotion', 'promotion_id', 'date_creation', 'espaces']
        read_only_fields = ['id', 'date_creation']
    
    def validate_promotion_id(self, value):
        if value is not None and not Promotion.objects.filter(id=value).exists():
            raise serializers.ValidationError("Cette promotion n'existe pas.")
        return value
    
    def create(self, validated_data):
        promotion_id = validated_data.pop('promotion_id', None)
        etudiant = Etudiant.objects.create(**validated_data)
        if promotion_id:
            etudiant.promotion_id = promotion_id
            etudiant.save()
        return etudiant


class TravailIndividuelSerializer(serializers.ModelSerializer):
    """Serializer pour le modèle TravailIndividuel"""
    espace = EspacePedagogiqueSerializer(read_only=True)
    espace_id = serializers.IntegerField(write_only=True)
    nombre_livraisons = serializers.SerializerMethodField()
    nombre_assignations = serializers.SerializerMethodField()
    
    class Meta:
        model = TravailIndividuel
        fields = ['id', 'titre', 'description', 'type_travail', 'consignes', 'date_echeance', 'espace', 'espace_id', 'date_creation', 'nombre_livraisons', 'nombre_assignations']
        read_only_fields = ['id', 'date_creation']
    
    def get_nombre_livraisons(self, obj):
        return obj.livraisons.count()
    
    def get_nombre_assignations(self, obj):
        return obj.assignations.count()
    
    def validate_espace_id(self, value):
        if not EspacePedagogique.objects.filter(id=value).exists():
            raise serializers.ValidationError("Cet espace pédagogique n'existe pas.")
        return value
    
    def create(self, validated_data):
        espace_id = validated_data.pop('espace_id')
        espace = EspacePedagogique.objects.get(id=espace_id)
        return TravailIndividuel.objects.create(espace=espace, **validated_data)


class LivraisonSerializer(serializers.ModelSerializer):
    """Serializer pour le modèle Livraison"""
    etudiant = EtudiantSerializer(read_only=True)
    etudiant_id = serializers.IntegerField(write_only=True)
    travail = TravailIndividuelSerializer(read_only=True)
    travail_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Livraison
        fields = [
            'id', 'etudiant', 'etudiant_id', 'travail', 'travail_id', 'contenu', 'fichier', 
            'date_soumission', 'notes', 'points', 'commentaire_evaluation', 'date_evaluation', 
            'evaluateur', 'est_evaluee'
        ]
        read_only_fields = ['id', 'date_soumission', 'date_evaluation', 'evaluateur', 'est_evaluee']
    
    def validate(self, data):
        etudiant_id = data.get('etudiant_id')
        travail_id = data.get('travail_id')
        
        if Livraison.objects.filter(etudiant_id=etudiant_id, travail_id=travail_id).exists():
            raise serializers.ValidationError("Une livraison existe déjà pour cet étudiant et ce travail.")
        
        if not Etudiant.objects.filter(id=etudiant_id).exists():
            raise serializers.ValidationError("Cet étudiant n'existe pas.")
        
        if not TravailIndividuel.objects.filter(id=travail_id).exists():
            raise serializers.ValidationError("Ce travail individuel n'existe pas.")
        
        return data
    
    def create(self, validated_data):
        etudiant_id = validated_data.pop('etudiant_id')
        travail_id = validated_data.pop('travail_id')
        etudiant = Etudiant.objects.get(id=etudiant_id)
        travail = TravailIndividuel.objects.get(id=travail_id)
        return Livraison.objects.create(etudiant=etudiant, travail=travail, **validated_data)


class AssignationTravailSerializer(serializers.ModelSerializer):
    """Serializer pour le modèle AssignationTravail"""
    etudiant = EtudiantSerializer(read_only=True)
    etudiant_id = serializers.IntegerField(write_only=True)
    travail = TravailIndividuelSerializer(read_only=True)
    travail_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = AssignationTravail
        fields = ['id', 'etudiant', 'etudiant_id', 'travail', 'travail_id', 'date_assignation', 'statut', 'notes']
        read_only_fields = ['id', 'date_assignation']
    
    def validate(self, data):
        etudiant_id = data.get('etudiant_id')
        travail_id = data.get('travail_id')
        
        if AssignationTravail.objects.filter(etudiant_id=etudiant_id, travail_id=travail_id).exists():
            raise serializers.ValidationError("Ce travail est déjà assigné à cet étudiant.")
        
        if not Etudiant.objects.filter(id=etudiant_id).exists():
            raise serializers.ValidationError("Cet étudiant n'existe pas.")
        
        if not TravailIndividuel.objects.filter(id=travail_id).exists():
            raise serializers.ValidationError("Ce travail individuel n'existe pas.")
        
        return data
    
    def create(self, validated_data):
        etudiant_id = validated_data.pop('etudiant_id')
        travail_id = validated_data.pop('travail_id')
        etudiant = Etudiant.objects.get(id=etudiant_id)
        travail = TravailIndividuel.objects.get(id=travail_id)
        return AssignationTravail.objects.create(etudiant=etudiant, travail=travail, **validated_data)
