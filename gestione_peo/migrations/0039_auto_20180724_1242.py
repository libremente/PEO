# Generated by Django 2.0.3 on 2018-07-24 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_peo', '0038_auto_20180718_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='punteggio_descrizioneindicatore_timedelta',
            name='operatore',
            field=models.CharField(choices=[('x', 'moltiplicatore'), ('a', 'assegnazione'), ('+', 'addizione'), ('/', 'divisione'), ('-', 'sottrazione')], default='a', help_text="Operatore che determina l'assegnazione", max_length=1, verbose_name='Operatore da applicare al punteggio'),
        ),
    ]
