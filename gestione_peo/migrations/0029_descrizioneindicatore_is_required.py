# Generated by Django 2.0.3 on 2018-07-12 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_peo', '0028_auto_20180711_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='descrizioneindicatore',
            name='is_required',
            field=models.BooleanField(default=True, help_text='Se attivo la domanda non potrà essere conclusa senza la presenza di un inserimento inerente a questa DescrizioneIndicatore.'),
        ),
    ]