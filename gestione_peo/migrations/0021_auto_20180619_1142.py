# Generated by Django 2.0.3 on 2018-06-19 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_peo', '0020_auto_20180619_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='bando',
            name='anni_servizio_minimi',
            field=models.IntegerField(default=3, verbose_name='Anni di servizio per poter partecipare'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bando',
            name='data_validita_titoli_fine',
            field=models.DateField(help_text='Data fino alla quale i titoli sono accettati', verbose_name='Data fine validità titoli'),
        ),
        migrations.AlterField(
            model_name='bando',
            name='data_validita_titoli_inizio',
            field=models.DateField(help_text='Data a partire dalla quale i titoli sono accettati', verbose_name='Data inizio validità titoli'),
        ),
    ]