# Generated by Django 2.0.3 on 2019-02-27 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_peo', '0079_bando_protocollo_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bando',
            name='protocollo_cod_titolario',
            field=models.CharField(blank=True, choices=[('9095', '7.1'), ('9099', '7.5')], max_length=12, null=True, verbose_name='Codice titolario'),
        ),
    ]
