# Generated by Django 2.0.3 on 2018-07-12 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_peo', '0029_descrizioneindicatore_is_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='bando',
            name='agevolazione_dipendenti_bloccati_anni',
            field=models.IntegerField(default=0, help_text="Anzianità di servizio nella stessa posizione economica per usufruire della moltiplicazione del punteggio relativo all'anzianità di servizio", verbose_name='Anni permanenza per bonus punteggio anzianità'),
        ),
        migrations.AddField(
            model_name='bando',
            name='agevolazione_dipendenti_bloccati_fattore_moltiplicazione',
            field=models.IntegerField(default=1, help_text="Fattore di moltiplicazione del punteggio relativo all'anzianità di servizio nel caso di permanenza maggiore o uguale alla soglia stabilita", verbose_name='Fattore moltiplicazione per bonus punteggio anzianità'),
        ),
    ]
