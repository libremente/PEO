# Generated by Django 2.0.3 on 2018-07-24 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domande_peo', '0019_remove_rettificadomandabando_data_rettifica'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulodomandabando',
            name='punteggio_calcolato',
            field=models.FloatField(blank=True, help_text='popolato da metodo .calcolo_punteggio_domanda', null=True),
        ),
    ]
