# Generated by Django 2.0.3 on 2018-05-30 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domande_peo', '0004_auto_20180530_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abilitazionebandodipendente',
            name='bando',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestione_peo.Bando'),
        ),
    ]