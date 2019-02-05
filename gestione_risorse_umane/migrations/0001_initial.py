# Generated by Django 2.0.3 on 2018-05-30 07:37

from django.db import migrations, models
import django.db.models.deletion
import gestione_risorse_umane.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dipendente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricola', models.CharField(max_length=6)),
                ('data_presa_servizio', models.DateField()),
                ('data_cessazione_contratto', models.DateField(blank=True, null=True)),
                ('motivo_cessazione_contratto', models.CharField(blank=True, default='', max_length=255)),
                ('carta_identita_front', models.FileField(blank=True, null=True, upload_to=gestione_risorse_umane.models._ci_upload)),
                ('carta_identita_retro', models.FileField(blank=True, null=True, upload_to=gestione_risorse_umane.models._ci_upload)),
                ('descrizione', models.TextField(blank=True, default='')),
            ],
            options={
                'verbose_name': 'Dipendente',
                'verbose_name_plural': 'Dipendenti',
            },
        ),
        migrations.CreateModel(
            name='LivelloPosizioneEconomica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Tradizionalmente: 1,2,3,4,5,6 ma diamo spazio ad opportune generalizzazioni', max_length=255)),
            ],
            options={
                'ordering': ('posizione_economica', 'nome'),
                'verbose_name': 'Livello Categoria',
                'verbose_name_plural': 'Livelli Categoria',
            },
        ),
        migrations.CreateModel(
            name='PosizioneEconomica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Tradizionalmente: B, C, D o EP', max_length=255)),
                ('punti_organico', models.FloatField(default=0.0)),
                ('descrizione', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorie',
            },
        ),
        migrations.CreateModel(
            name='TipoContratto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descrizione', models.TextField(blank=True, default='')),
            ],
            options={
                'verbose_name': 'Tipo di Contratto',
                'verbose_name_plural': 'Tipi di Contratti',
            },
        ),
        migrations.CreateModel(
            name='TipoInvalidita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('identificativo', models.CharField(max_length=1)),
                ('descrizione', models.TextField(blank=True, default='')),
            ],
            options={
                'verbose_name': 'Tipo di Invalidità',
                'verbose_name_plural': 'Tipi di Invalidità',
            },
        ),
        migrations.CreateModel(
            name='TipoProfiloProfessionale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descrizione', models.TextField(blank=True, default='')),
            ],
            options={
                'verbose_name': 'Tipo di Profilo Professionale',
                'verbose_name_plural': 'Tipi di Profili Professionali',
            },
        ),
        migrations.CreateModel(
            name='TitoloStudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Come da classificazione ISTAT 2003-2011: https://www.istat.it/it/files/2011/01/Classificazione-titoli-studio-28_ott_2005-classificazione_sintetica.xls', max_length=255)),
                ('istituto', models.CharField(default='', max_length=255)),
                ('codice_livello', models.IntegerField(blank=True, default=0)),
                ('codice_titolo_di_studio', models.IntegerField(blank=True, default=0)),
                ('isced_97_level', models.CharField(blank=True, default='', max_length=12, verbose_name='Isced97 Level and Program destination')),
                ('descrizione', models.TextField()),
            ],
            options={
                'verbose_name': 'Titolo di Studio',
                'verbose_name_plural': 'Titoli di Studio',
            },
        ),
        migrations.AddField(
            model_name='livelloposizioneeconomica',
            name='posizione_economica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestione_risorse_umane.PosizioneEconomica'),
        ),
        migrations.AddField(
            model_name='dipendente',
            name='contratto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestione_risorse_umane.TipoContratto'),
        ),
        migrations.AddField(
            model_name='dipendente',
            name='invalidita',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestione_risorse_umane.TipoInvalidita'),
        ),
        migrations.AddField(
            model_name='dipendente',
            name='livello',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestione_risorse_umane.LivelloPosizioneEconomica'),
        ),
    ]