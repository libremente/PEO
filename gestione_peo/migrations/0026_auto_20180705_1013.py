# Generated by Django 2.0.3 on 2018-07-05 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_peo', '0025_auto_20180705_0942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bando',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='bando',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='categoriedisabilitate_punteggio_titolostudio',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='categoriedisabilitate_punteggio_titolostudio',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='clausolebando',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='clausolebando',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='descrizioneindicatore',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='descrizioneindicatore',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='indicatoreponderato',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='indicatoreponderato',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='punteggio_anzianita_servizio',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='punteggio_anzianita_servizio',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='punteggio_descrizioneindicatore',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='punteggio_descrizioneindicatore',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='punteggio_descrizioneindicatore_timedelta',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='punteggio_descrizioneindicatore_timedelta',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='punteggio_titolostudio',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='punteggio_titolostudio',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='punteggiomax_descrizioneindicatore_poseconomica',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='punteggiomax_descrizioneindicatore_poseconomica',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='punteggiomax_indicatoreponderato_poseconomica',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='punteggiomax_indicatoreponderato_poseconomica',
            name='modified_by',
        ),
    ]
