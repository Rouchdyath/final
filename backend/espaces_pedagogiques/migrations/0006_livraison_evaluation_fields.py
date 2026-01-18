# Generated migration for Livraison evaluation fields and constraint fixes

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('espaces_pedagogiques', '0005_assignationtravail_and_update_travail'),
    ]

    operations = [
        # Remove constraint unique_etudiant_travail from AssignationTravail and replace with constraint
        migrations.RemoveConstraint(
            model_name='assignationtravail',
            name='unique_etudiant_travail',
        ),
        
        # Remove constraint unique_promotion_nom_annee from Promotion and replace with constraint
        migrations.RemoveConstraint(
            model_name='promotion',
            name='unique_promotion_nom_annee',
        ),
        
        # Alter unique_together for AssignationTravail
        migrations.AlterUniqueTogether(
            name='assignationtravail',
            unique_together={('etudiant', 'travail')},
        ),
        
        # Alter unique_together for Promotion
        migrations.AlterUniqueTogether(
            name='promotion',
            unique_together={('nom', 'annee')},
        ),
        
        # Add evaluation fields to Livraison
        migrations.AddField(
            model_name='livraison',
            name='notes',
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text='Note sur 20 ou autre échelle',
                max_digits=5,
                null=True,
                verbose_name='Note obtenue'
            ),
        ),
        migrations.AddField(
            model_name='livraison',
            name='points',
            field=models.IntegerField(
                blank=True,
                help_text='Points numériques',
                null=True,
                verbose_name='Points obtenues'
            ),
        ),
        migrations.AddField(
            model_name='livraison',
            name='commentaire_evaluation',
            field=models.TextField(
                blank=True,
                help_text='Feedback du formateur',
                null=True,
                verbose_name='Commentaire d\'évaluation'
            ),
        ),
        migrations.AddField(
            model_name='livraison',
            name='date_evaluation',
            field=models.DateTimeField(
                blank=True,
                null=True,
                verbose_name='Date d\'évaluation'
            ),
        ),
        migrations.AddField(
            model_name='livraison',
            name='evaluateur',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='evaluations',
                to='espaces_pedagogiques.formateur',
                verbose_name='Formateur Évaluateur'
            ),
        ),
    ]

