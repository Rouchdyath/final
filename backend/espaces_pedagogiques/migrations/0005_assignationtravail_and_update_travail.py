# Generated migration for AssignationTravail model and TravailIndividuel updates

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('espaces_pedagogiques', '0004_promotion'),
    ]

    operations = [
        # Add fields to TravailIndividuel
        migrations.AddField(
            model_name='travailindividuel',
            name='type_travail',
            field=models.CharField(
                choices=[('individuel', 'Individuel'), ('collectif', 'Collectif')],
                default='individuel',
                max_length=20,
                verbose_name='Type de travail'
            ),
        ),
        migrations.AddField(
            model_name='travailindividuel',
            name='consignes',
            field=models.TextField(default='', verbose_name='Consignes détaillées'),
            preserve_default=False,
        ),
        # Create AssignationTravail model
        migrations.CreateModel(
            name='AssignationTravail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_assignation', models.DateTimeField(auto_now_add=True, verbose_name="Date d'assignation")),
                ('statut', models.CharField(
                    choices=[
                        ('assigné', 'Assigné'),
                        ('en_cours', 'En cours'),
                        ('complété', 'Complété'),
                        ('évalué', 'Évalué'),
                    ],
                    default='assigné',
                    max_length=20,
                    verbose_name='Statut'
                )),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes du formateur')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travaux_assignes', to='espaces_pedagogiques.etudiant', verbose_name='Étudiant')),
                ('travail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignations', to='espaces_pedagogiques.travailindividuel', verbose_name='Travail')),
            ],
            options={
                'verbose_name': 'Assignation de Travail',
                'verbose_name_plural': 'Assignations de Travail',
                'ordering': ['-date_assignation'],
            },
        ),
        # Add unique constraint for AssignationTravail
        migrations.AddConstraint(
            model_name='assignationtravail',
            constraint=models.UniqueConstraint(fields=['etudiant', 'travail'], name='unique_etudiant_travail'),
        ),
    ]
