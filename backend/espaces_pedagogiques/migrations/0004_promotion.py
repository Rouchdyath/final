# Generated migration for Promotion model

from django.db import migrations, models
import django.db.models.deletion
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('espaces_pedagogiques', '0003_alter_espacepedagogique_options_and_more'),
    ]

    operations = [
        # Create Promotion model
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Nom de la promotion')),
                ('annee', models.IntegerField(help_text='Ex: 2024 pour la promotion 2024-2025', verbose_name='Année de la promotion')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('espaces', models.ManyToManyField(blank=True, related_name='promotions', to='espaces_pedagogiques.espacepedagogique', verbose_name='Espaces pédagogiques')),
            ],
            options={
                'verbose_name': 'Promotion',
                'verbose_name_plural': 'Promotions',
                'ordering': ['-annee', 'nom'],
            },
        ),
        
        # Add unique_together constraint for Promotion
        migrations.AddConstraint(
            model_name='promotion',
            constraint=models.UniqueConstraint(fields=['nom', 'annee'], name='unique_promotion_nom_annee'),
        ),
        
        # Add promotion field to Etudiant
        migrations.AddField(
            model_name='etudiant',
            name='promotion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='etudiants', to='espaces_pedagogiques.promotion', verbose_name='Promotion'),
        ),
    ]
