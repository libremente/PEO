# Generated by Django 2.0.3 on 2018-07-18 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domande_peo', '0017_domandabando_commento_punteggio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domandabando',
            name='punteggio_calcolato',
            field=models.FloatField(blank=True, help_text='popolato da metodo .calcolo_punteggio_domanda', null=True),
        ),
    ]
