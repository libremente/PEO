# Generated by Django 2.0.3 on 2018-11-14 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_peo', '0059_auto_20181114_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bando',
            name='bando_url',
            field=models.URLField(blank=True, help_text='URL della risorsa web con le specifiche del Bando', max_length=255, null=True),
        ),
    ]
