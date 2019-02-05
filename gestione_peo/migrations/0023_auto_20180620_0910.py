# Generated by Django 2.0.3 on 2018-06-20 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_peo', '0022_auto_20180619_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='moduloinserimentocampi',
            name='valore',
            field=models.CharField(blank=True, default='', help_text="compilare esclusivamente se si sceglie 'Menu a tendina'", max_length=255),
        ),
        migrations.AlterField(
            model_name='moduloinserimentocampi',
            name='tipo',
            field=models.CharField(choices=[('CharField', 'caratteri'), ('TextField', 'descrizione lunga'), ('IntegerField', 'numero intero'), ('FloatField', 'numero con virgola'), ('_TitoloStudioField', 'selezione titolo di studio'), ('DateField', 'data'), ('StartDateField', 'data inizio'), ('EndDateField', 'data fine + checkbox "fino ad oggi"'), ('FileField', 'allegato pdf'), ('CheckBoxField', 'checkbox'), ('CustomSelectBoxField', 'menu a tendina')], max_length=33),
        ),
    ]
