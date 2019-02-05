# Generated by Django 2.0.3 on 2018-09-17 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_peo', '0048_auto_20180914_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moduloinserimentocampi',
            name='tipo',
            field=models.CharField(choices=[('CharField', 'caratteri'), ('TextField', 'descrizione lunga'), ('IntegerField', 'numero intero'), ('FloatField', 'numero con virgola'), ('PunteggioFloatField', '* punteggio (numero con virgola)'), ('_TitoloStudioField', '* selezione titolo di studio (con calcolo punteggio)'), ('FileField', 'allegato pdf'), ('CheckBoxField', 'checkbox'), ('CustomSelectBoxField', 'menu a tendina'), ('CustomRadioBoxField', 'serie di opzioni'), ('ProtocolloField', 'protocollo (numero + data)'), ('DateField', 'data'), ('StartEndDateField', '* intervallo date IN RANGE OF CARRIERA (con "fino ad oggi")'), ('StartEndDateField_2', '* intervallo date IN RANGE OF CARRIERA (senza "fino ad oggi")'), ('OutStartEndDateField', '* intervallo date OUT OF CARRIERA'), ('DataLowerThanBandoField', '* data SINGOLA IN RANGE OF CARRIERA'), ('DurataComeInteroField', '* durata in anni/mesi/ore')], help_text='I campi contrassegnati da asterisco (*) vengono validati tenendo conto delle specifiche del Bando, pertanto possono influire sul calcolo del punteggio', max_length=33),
        ),
    ]
