import json

from django import forms
from django.db import models
from django.utils import timezone

from gestione_peo.models import (Bando,
                                 DescrizioneIndicatore,
                                 Punteggio_TitoloStudio)
from gestione_peo.settings import (ETICHETTA_INSERIMENTI_ID,
                                   ETICHETTA_INSERIMENTI_LABEL,
                                   ETICHETTA_INSERIMENTI_HELP_TEXT)
from gestione_risorse_umane.models import *
from unical_template.models import TimeStampedModel, CreatedModifiedModel

from .punteggio import PunteggioModuloDomandaBando, PunteggioDomandaBando
from .utils import get_path_allegato


class AbilitazioneBandoDipendente(TimeStampedModel):
    """
    modello che viene generato da ARU a seguito del filtro sulla idoneità
    selezionano tutti i dipendenti che possono rendere idonei e questi
    vengono spostati in questo schema.
    Se il dipendente è presente in questo schema sulla dashboard apparirà
    'Sei idoneo a partecipare al Bando'
    """
    bando = models.ForeignKey(Bando, on_delete=models.CASCADE, null=True)
    dipendente = models.ForeignKey(Dipendente, on_delete=models.CASCADE,)
    class Meta:
        verbose_name = 'Abilitazione al Bando per Dipendente'
        verbose_name_plural = 'Abilitazioni di partecipazione ai Bandi per i Dipendenti'

    def __str__(self):
        return '{}, {}'.format(self.bando, self.dipendente.matricola)


class DomandaBando(TimeStampedModel, PunteggioDomandaBando):
    """
    Quando un utente partecipa a PEO
    relazione debole su matricola
    Se il login cambia e viene generato un altro utente questi
    dati verranno pescati sempre dalla matricola (globalmente)
    con riferimento agli utenti nel tempo (AUTH_USER_MODEL)
    """
    # Il nome che la identifica nelle relazioni (più intuitivo della data)
    bando = models.ForeignKey(Bando, on_delete=models.SET_NULL,
                              null=True, blank=True)
    dipendente = models.ForeignKey(Dipendente, on_delete=models.PROTECT)
    modified = models.DateTimeField(blank=True, null=True)
    data_chiusura   = models.DateTimeField(help_text=("quando la domanda è stata conclusa,"
                                                      " se manca significa che è stata riaperta"),
                                           blank=True, null=True)
    numero_protocollo = models.CharField(blank=True, default='',
                                         max_length=32)
    # data_chiusura deve essere impostata prima della protocollazione
    data_protocollazione = models.DateTimeField(help_text="quando la domanda è stata protocolla/consegnata",
                                                blank=True, null=True)
    punteggio_anzianita_manuale = models.FloatField('Punteggio assegnato all\'anzianità interna MANUALE',
                                                    help_text="impostato manualmente",
                                                    blank=True, null=True)
    punteggio_calcolato = models.FloatField(help_text="popolato da metodo .calcolo_punteggio_domanda,"
                                                      " comprensivo di quello derivante dall'anzianità",
                                            blank=True, null=True)
    progressione_accettata = models.BooleanField(default=False,
                                    help_text=("Marca questa domanda come idonea alla progressione."
                                               " Se vero fa fede la data di protocollazione come"
                                               " Data ultima progressione"))
    descrizione = models.TextField(blank=True, default='')
    commento_punteggio = models.TextField(blank=True, default='',
                                          help_text="Il testo inserito in questo"
                                                    " campo sarà reso visibile al"
                                                    " dipendente dopo la chiusura del Bando"
                                                    " e motiverà eventuali revisioni sul"
                                                    " calcolo e l'assegnazione del punteggio")
    is_active = models.BooleanField(default=True,
                                    help_text=("Per eventuale disabilitazione d'ufficio"
                                               " come ad esempio una esclusione coatta dovuta a contenziosi"
                                               " o motivazioni di natura giuridica."
                                               " Se una domanda è presente ma disabilitata il dipendente"
                                               " non potrà crearne una nuova" ))

    class Meta:
        ordering = ['-data_chiusura']
        verbose_name = 'Domanda di partecipazione del Dipendente'
        verbose_name_plural = 'Domande di partecipazione dei Dipendenti'

    def __str__(self):
        return '{}, {} {} ({})'.format(self.bando,
                               self.dipendente.nome,
                               self.dipendente.cognome,
                               self.dipendente.matricola)

    def mark_as_modified(self):
        """
        salva la data di modifica  dell'oggetto
        """
        self.modified=timezone.localtime()
        self.save()

    def moduli_non_validi(self):
        """
        Torna la lista dei moduli compilati male
        Se True la domanda non è valida
        """
        moduli = []
        # controllo che tutti i moduli inseriti siano validi
        for mdb in self.modulodomandabando_set.all():
            if not mdb.is_valid():
                moduli.append(mdb)
        return moduli

    def indicatori_richiesti(self):
        """
        Torna i descrizione_indicatore.is_required mancanti
        Se True la domanda non è valida
        """
        di_mancanti = []
        for ip in self.bando.indicatoreponderato_set.all():
            for di in ip.descrizioneindicatore_set.filter(is_required=True):
                if not di.is_available_for_cateco(self.dipendente.livello.posizione_economica):
                    continue
                if di not in [ i.descrizione_indicatore for i in self.modulodomandabando_set.all()]:
                    di_mancanti.append(di)
        return di_mancanti

    def descr_ind_non_cancellabili(self):
        """
        Torna True se nella domanda sono presenti
        DescrizioniIndicatori non eliminabili
        """
        di_mancanti = []
        for ip in self.bando.indicatoreponderato_set.all():
            for di in ip.descrizioneindicatore_set.filter(non_cancellabile=True):
                if di in [ i.descrizione_indicatore for i in self.modulodomandabando_set.all()]:
                    return True

    def valida(self):
        """
        Torna True se il controllo su tutti i moduli.is_valid() tornano true
        e se tutti le descrizioni indicatori.is_required sono presenti
        """
        if not self.moduli_non_validi() and not self.indicatori_richiesti():
            return True

    def is_aperta(self):
        if not self.data_chiusura and self.is_active:
            return self.created

    def rettificabile(self):
        if not self.bando.presentazione_domande_scaduta():
            return True

    def modificabile(self):
        if not self.is_aperta():
            return False
        if not self.rettificabile():
            return False
        if self.bando.is_scaduto() or self.bando.presentazione_domande_scaduta():
            return False
        return True

    def is_protocollata(self):
        return self.data_protocollazione

    def get_data_progressione(self):
        if self.progressione_accettata:
            return self.data_protocollazione

    def num_mdb_tipo_inseriti(self, descrizione_indicatore):
        """
        Restituisce il numero di ModuliCompilati relativi
        alla stessa DescrizioneIndicatore presenti nella domanda
        """
        mdbs = self.modulodomandabando_set.all()
        n = 0
        for mdb in mdbs:
            if mdb.descrizione_indicatore.pk == descrizione_indicatore.pk:
                n += 1
        return n

class RettificaDomandaBando(TimeStampedModel):
    """
    Timeline di chiusure, protocollazioni e rettifiche delle domande
    """
    # Il nome che la identifica nelle relazioni (più intuitivo della data)
    domanda_bando = models.ForeignKey(DomandaBando, on_delete=models.CASCADE)
    data_chiusura   = models.DateTimeField(help_text="quando la domanda è stata conclusa",
                                           blank=True, null=True)
    numero_protocollo = models.CharField(blank=True, default='',
                                         max_length=32)
    data_protocollazione = models.DateTimeField(help_text="quando la domanda è stata protocolla/consegnata",
                                                blank=True, null=True)
    # data_rettifica   = models.DateTimeField(help_text=("Data di rettifica in caso"
                                                       # " di riapertura della"
                                                       # " domanda per modifiche"),)
    class Meta:
        ordering = ['-created']
        verbose_name = 'Chiusura della Domanda di partecipazione del Dipendente'
        verbose_name_plural = 'Chiusura delle Domande di partecipazione dei Dipendenti'

    def __str__(self):
        return '{} {}'.format(self.domanda_bando, self.numero_protocollo)


class ModuloDomandaBando(TimeStampedModel, PunteggioModuloDomandaBando):
    """
    Quando un utente partecipa a PEO
    relazione debole su matricola
    Se il login cambia e viene generato un altro utente questi
    dati verranno pescati sempre dalla matricola (globalmente)
    con riferimento agli utenti nel tempo (AUTH_USER_MODEL)
    """
    # Il nome che la identifica nelle relazioni (più intuitivo della data)
    domanda_bando = models.ForeignKey(DomandaBando, on_delete=models.CASCADE)
    descrizione_indicatore = models.ForeignKey(DescrizioneIndicatore,
                                               on_delete=models.CASCADE)
    # libreria esterna oppure cambio client per JsonField
    # non serve gestirlo come JsonField perchè non vi facciamo ricerche al suo interno ;)
    modulo_compilato = models.TextField()
    # Escludi il modulo dal calcolo del punteggio
    disabilita = models.BooleanField(help_text="Se selezionato, esclude "
                                               "il modulo dal calcolo del punteggio",
                                     default=False)
    motivazione = models.TextField(help_text="Motivazione disabilitazione",
                                   blank=True, default='')
    punteggio_calcolato = models.FloatField(help_text="popolato da metodo .calcolo_punteggio",
                                            blank=True, null=True)
    # sovrascrive il field di TimeStampedModel per tracciare solo le modifiche
    # dell'utente lato frontend. Es: in fase di calcolo del punteggio questo valore
    # verrebbe sfalsato
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Modulo compilato Bando del Dipendente'
        verbose_name_plural = 'Moduli compilati Bando dei Dipendenti'
        ordering = ['descrizione_indicatore__id_code',]

    def mark_as_modified(self):
        """
        salva la data di modifica  dell'oggetto
        """
        self.modified=timezone.localtime()
        self.save()

    def get_allegati_dict(self):
        allegati_dict = self.get_as_dict().get('allegati')
        if allegati_dict:
            return allegati_dict
        else:
            return {}

    def get_allegati(self):
        """
        torna un lista di file path contenenti gli allegati su filesystem
        """
        allegati = self.get_allegati_dict()
        if allegati:
            return allegati.items()
        else:
            return []

    def allegati_validi(self):
        """
        controlla che gli allegati del modulo siano presenti se required
        """
        allegati = dict(self.get_allegati())
        form = self.descrizione_indicatore.get_form()
        for field in form.fields:
            f = form.fields[field]
            if (f.required and isinstance(f, forms.FileField)):
                if not allegati:
                    return False
                if not field in allegati.keys():
                    return False
        # any fields returns as False
        return True

    def get_as_dict_with_allegati(self):
        """
        torna il dizionario con i field allegati originali
        """
        d = self.get_as_dict()

        # ricostruisco la struttura con gli allegati
        allegati = d.get('allegati')
        if allegati:
            del d['allegati']
            d.update(allegati)
        return d

    def get_as_dict(self, allegati=True):
        """
        torna il dizionario con gli allegati raggruppati in 'allegati'
        """
        d = json.loads(self.modulo_compilato)
        if d.get('allegati'):
            if not allegati:
                del d['allegati']
                return d

        # Corregge i campi inseriti con spazi prima e dopo
        for k,v in d.items():
           if isinstance(d[k],str):
               d[k] = d[k].strip()

        return d

    def set_as_dict(self, modulo_compilato_dict):
        self.modulo_compilato = json.dumps(modulo_compilato_dict)
        self.save()

    def is_valid(self):
        """
        controlla che il modulo sia valido
        """
        if not self.allegati_validi():
            return False
        # NON FARE ripopolamento+clean di ogni form, altrimenti rallenta!
        # form = self.compiled_form()
        # return form.is_valid()
        return True

    def get_allegati_path(self):
        l = []
        allegati = self.get_allegati()
        for allegato in allegati:
            fpath = get_path_allegato(self.domanda_bando.dipendente.matricola,
                                      self.domanda_bando.bando.slug,
                                      self.pk)
            fname = '/'.join((fpath, allegato[1]))
            l.append(fname)
        return l

    def compiled_form(self, files=None, remove_filefields=True):
        """
        Torna il form compilato senza allegati
        """
        form = self.descrizione_indicatore.get_form(data=self.get_as_dict(allegati=False),
                                                    files=files,
                                                    domanda_id=self.domanda_bando.pk,
                                                    remove_filefields=remove_filefields)
        return form

    def compiled_form_readonly(self, show_title=False, attr='disabled'):
        """
        Restituisce una versione "più pulita" di compiled_form
        - I field non compilati non vengono mostrati (remove_not_compiled_fields())
        - Il campo "titolo" di default non viene mostrato
        - I fields sono readonly
        NOTA: i field select non risentono dell'attributo readonly!!!
        Usato nei metodo che producono le anteprime non modificabili
        dei moduli compilati
        """
        form = self.compiled_form()
        form.remove_not_compiled_fields()
        if not show_title:
            del form.fields[ETICHETTA_INSERIMENTI_ID]
        for generic_field in form:
            field = form.fields[generic_field.name]
            widget = field.widget
            widget.attrs[attr] = True
            # Es: TextArea non ha attributo 'input_type'
            # Senza questo controllo il codice genera un'eccezione
            if not hasattr(widget, 'input_type'):
                widget.attrs[attr] = True
                continue
            tipo = widget.input_type
            if tipo in ['select', 'checkbox', 'radiobox']:
                widget.attrs['disabled'] = True
            else:
                widget.attrs[attr] = True
        return form

    def migrate_fieldname(self, old, new, save=True, strict=False):
        """
        change fieldname for migration purpose
        """
        d = self.get_as_dict()
        if not d.get(old):
            if strict: raise Exception('{} does not exist'.format(old))
            return
        d[new] = ''.join(d[old])
        del d[old]
        if save:
            self.set_as_dict(d)
        return d

    def compiled_form_as_table(self):
        return self.compiled_form().as_table()

    def get_identificativo_veloce(self):
        modulo_compilato_dict = json.loads(self.modulo_compilato)
        return modulo_compilato_dict.get(ETICHETTA_INSERIMENTI_ID)

    def __str__(self):
        return '{} ({})'.format(self.domanda_bando, self.descrizione_indicatore.nome)
