## 1 Introduzione

voyzSESSION PRO è un software di registrazione e mixaggio (DAW) per produzioni vocali: voice-over e commento fuori campo sulle immagini, doppiaggio, servizi radiofonici, podcast e audiolibri.

Nelle produzioni sulle immagini carichi un video, registri il testo in sincrono ed esporti il mix finito come file audio oppure direttamente nel video o nell'MXF. Le produzioni solo audio come podcast, audiolibro o servizio radiofonico non hanno bisogno di un video. Per queste ci sono la pagina **AUDIO** con lo Script Editor, i profili di loudness per radio, podcast e audiolibro e formati di esportazione come MP2, MP3, FLAC e Opus.

### 1.1 Modalità Assist e modalità Manual

|                   | Modalità Assist                                                       | Modalità Manual                                        |
|-------------------|-----------------------------------------------------------------------|--------------------------------------------------------|
| Pensata per       | Speaker, redattori e montatori senza conoscenze di tecnica del suono  | Fonici e tecnici del suono                             |
| Chi fa il mix     | L'automatismo (AUTO MIX)                                              | Tu stesso, a mano come in una DAW                   |
| Uso tipico        | Registrazione e consegna rapida                                       | Montaggio e mix di precisione                          |
| Risultato         | Mix secondo la norma di loudness scelta, con un solo clic             | Pieno controllo su controlli, plug-in e automazione    |

Ciò che AUTO MIX calcola in modalità Assist viene ripreso dalla modalità Manual come punto di partenza. Puoi registrare in entrambe le modalità.

### 1.2 Requisiti di sistema

|                   | Consigliato                                        | Minimo                                                  |
|-------------------|----------------------------------------------------|---------------------------------------------------------|
| Mac               | Processore Apple (M1 o successivo)                 | Mac Intel (funziona, ma non è consigliato)              |
| Sistema operativo | macOS 14 Sonoma o successivo                       | macOS 14 Sonoma                                         |
| Memoria           | 32 GB per progetti oltre 30 minuti con video 4K    | 16 GB                                                   |
| Spazio su disco   | SSD                                                | 5 GB liberi, più lo spazio per il materiale del progetto |
| Audio             | Interfaccia audio con microfono e cuffie           | Microfono integrato o microfono USB                     |

Sui Mac Intel e con meno di 16 GB di memoria l'app mostra una sola volta, al primo avvio, un avviso sull'hardware. Il driver audio per la registrazione remota richiede macOS 13, la videocamera virtuale macOS 12.3. Con macOS 14 entrambi i requisiti sono soddisfatti.

### 1.3 Installazione

1.  Scarica `voyzsession-2.0.dmg` da pegelwerk.com.
2.  Apri il DMG e trascina voyzSESSION PRO nella cartella Applicazioni. La videocamera virtuale funziona solo se l'app si trova lì.
3.  Avvia l'app. macOS chiede l'accesso al microfono. Consentilo, altrimenti non è possibile registrare.
4.  Alla prima apertura del prompter macOS chiede il permesso per il riconoscimento vocale. Consenti anche questo, così il testo può seguire la tua voce.

L'app segnala le nuove versioni con l'etichetta UPDATE nella barra superiore.

### 1.4 Licenza e periodo di prova

Al primo avvio si apre la finestra “voyzSESSION PRO - Licenza”. Puoi provare l'app per 7 giorni. Un'etichetta nella barra superiore mostra i giorni rimanenti.

Per attivare la licenza:

1.  Incolla nel campo la chiave di licenza ricevuta per e-mail oppure trascina il file `license.lic` sulla finestra. Puoi anche fare clic sul link di attivazione nell'e-mail.
2.  Fai clic su **Attiva**.

**Acquista licenza** porta al negozio online. Con un abbonamento il pulsante si chiama **Gestisci abbonamento**. Dall'etichetta della licenza nella barra superiore puoi riaprire la finestra in qualsiasi momento.

Al termine del periodo di prova l'app continua a funzionare con limitazioni ed emette ogni minuto un breve segnale acustico di promemoria. Se un abbonamento è scaduto, l'esportazione è bloccata.

## 2 L'interfaccia

La finestra principale è composta da tre aree fisse: in alto la barra superiore, al centro la pagina di lavoro (**VIDEO**, **AUDIO** o **EDIT**) e in basso la barra di trasporto con i pulsanti per la riproduzione e la registrazione. Tra la pagina di lavoro e la barra di trasporto puoi mostrare la barra di navigazione.

### 2.1 Barra superiore

Gli elementi da sinistra a destra:

| Elemento                  | Funzione                                                                                                                                 |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| FILE                      | Nuovo progetto, Apri, Recenti, Salva, Salva con nome, Modelli ([capitolo 15](#k15))                                                      |
| PROGETTO...               | Impostazioni del progetto: frequenza di campionamento, frame rate, timecode iniziale, profilo, stile di mix                               |
| VIDEO, AUDIO, EDIT, MIXER | Cambio della pagina di lavoro ([sezione 2.2](#k2-2))                                                                                     |
| MEDIA                     | Mostra e nasconde l'archivio media                                                                                                       |
| APRI VIDEO                | Apre un video. Quando un video è caricato, accanto compare una x per rimuoverlo. La rimozione si può annullare.                          |
| IMMAGINE                  | Attiva o disattiva la finestra video (Cmd+9). Con un clic destro sposti l'immagine su uno schermo esterno o mostri il timecode.          |
| LEVEL                     | Controllo livello per il microfono                                                                                                       |
| A/V...                    | Impostazioni audio e video (interfaccia, ingresso e uscita)                                                                              |

Apri il manuale dal menu dell'app: voyzSESSION PRO \> Manuale (Cmd+Shift+/). Il manuale è incluso nell'app e funziona senza connessione a Internet.

Durante il periodo di prova un'etichetta con la scritta TRIAL mostra i giorni rimanenti. Se è disponibile una nuova versione, compare un'etichetta UPDATE che porta alla pagina di download.

### 2.2 Pagine di lavoro

| Pagina | Scopo                                       | Contenuto                                                                                        |
|--------|---------------------------------------------|--------------------------------------------------------------------------------------------------|
| VIDEO  | Registrazione sulle immagini                | Video e prompter con il testo da leggere                                                         |
| AUDIO  | Progetti solo audio, per esempio podcast    | Script Editor con la trascrizione delle registrazioni                                            |
| EDIT   | Montaggio e arrangiamento                   | Timeline multitraccia                                                                            |
| MIXER  | Mix                                         | Il mixer si sovrappone alla pagina corrente. Un clic su un'altra pagina lo chiude.               |

### 2.3 Barra di trasporto

- **A sinistra:** Annulla e Ripeti, un interruttore a bilanciere per lo zoom dell'asse temporale e uno per l'altezza delle tracce.
- **Al centro:** \|\<\< (all'inizio), riavvolgimento, **PLAY/STOP**, **REC**, **LOOP**, avanzamento rapido, \>\>\| (alla fine). Una breve pressione su un tasto di avvolgimento salta di 1 secondo, tenendolo premuto avvolge a velocità crescente fino a 32 volte.
- **Contatore di posizione:** mostra la posizione corrente, in rosso durante la registrazione, in verde durante la riproduzione. Dopo un clic puoi inserire un tempo. Con un clic destro scegli la visualizzazione in timecode, minuti:secondi o campioni.
- **Gruppo di registrazione:** **V-PUNCH** (punch tramite riconoscimento vocale), **PRE** (pre-roll prima della registrazione, da 0 a 10 secondi) e **POST** (post-roll dopo il punch-out).
- **A destra:** il selettore **ASSIST \| MANUAL**, il tasto dello stile di mix (mostra quello attivo, per esempio **SERVIZIO** o **TRAILER**, [sezione 7.1](#k7-1)), il pulsante **AUTO MIX** (solo in modalità Assist) ed **EXPORT**.

Sotto i pulsanti c'è una riga di avviso in cui l'app segnala l'operazione in corso, per esempio “Calcolo del mix...”. I messaggi di conferma compaiono in verde. Se **AUTO MIX** è illuminato in blu, il mix salvato non corrisponde più al progetto e va ricalcolato.

### 2.4 Barra di navigazione

Mostri e nascondi la barra di navigazione da Finestra \> Barra di navigazione. Mostra l'intero progetto come forma d'onda. Un clic salta al punto scelto. Nella pagina **EDIT** una cornice indica la porzione visibile, che puoi spostare con il mouse.

A sinistra inserisci **START**, **FINE** e **LUNGHEZZA** dell'intervallo. A destra ci sono i pulsanti per i marker: **MK +** imposta un marker, i pulsanti **MK** con la freccia saltano al marker precedente o successivo, **MARKER** mostra un elenco di tutti i marker. Un progetto può contenere fino a 999 marker.

### 2.5 Barra dei menu

| Menu            | Voce                                                                                                        | Scorciatoia |
|-----------------|-------------------------------------------------------------------------------------------------------------|-------------|
| voyzSESSION PRO | Informazioni su voyzSESSION PRO..., Stream Deck: installa plug-in..., Stream Deck: carica layout, Esci     | Cmd+Q       |
| voyzSESSION PRO | Manuale                                                                                                     | Cmd+Shift+/ |
| Archivio        | Importa AAF... ([sezione 3.5](#k3-5))                                                                       |             |
| Impostazioni    | Generale...                                                                                                 | Cmd+,       |
| Impostazioni    | Audio/video...                                                                                              |             |
| Impostazioni    | Dissolvenza incrociata in sovrapposizione (on/off)                                                          |             |
| Finestra        | Finestra cabina                                                                                             | Cmd+Shift+B |
| Finestra        | Capitoli                                                                                                    | Cmd+Shift+K |
| Finestra        | Finestra video                                                                                              | Cmd+9       |
| Finestra        | Barra di navigazione (on/off)                                                                               |             |

Nuovo progetto, Apri, Salva e Modelli si trovano nel pulsante **FILE** della barra superiore, non nel menu Archivio.

## 3 Primi passi

Questo capitolo ti accompagna dal progetto vuoto alla prima registrazione.

### 3.1 Creare e salvare un progetto

1.  Scegli **FILE** \> **Nuovo progetto vuoto**. Un nuovo progetto contiene già una traccia voce.
2.  Salva subito il progetto con **FILE** \> **Salva...** (Cmd+S), preferibilmente su un SSD con spazio sufficiente.

L'app scrive le registrazioni direttamente nella cartella del progetto. In un progetto non ancora salvato, alla prima pressione di **REC** compare il messaggio “La registrazione richiede una cartella di progetto”.

Se lavori spesso con la stessa disposizione delle tracce, crea i nuovi progetti con **FILE** \> **Nuovo da modello** ([capitolo 15](#k15)).

### 3.2 Configurare il dispositivo audio

1.  Nella barra superiore fai clic su **A/V...**.
2.  In **OUTPUT** scegli l'uscita cuffie o la tua interfaccia, in **INPUT** il tuo microfono.
3.  Se ti ascolti direttamente tramite l'interfaccia (Direct Monitor sul dispositivo), lascia attivo **Direct hardware monitoring**. Se questa possibilità manca, disattiva l'opzione. In questo caso ti ascolti tramite il software.

Registra sempre con le cuffie. Con la riproduzione dagli altoparlanti l'audio del video finisce nel microfono.

### 3.3 Regolare il livello del microfono (Controllo livello)

Apri il Controllo livello con **LEVEL** nella barra superiore. Nell'impostazione predefinita non compare da solo all'avvio.

1.  In alto scegli il microfono.
2.  Pronuncia alcune frasi al volume con cui registrerai in seguito.
3.  Regola il guadagno (gain) del preamplificatore sull'interfaccia in modo che l'indicatore segnali “Livello ottimale”.

| Indicazione      | Livello di picco  | Cosa fare                                                          |
|------------------|-------------------|--------------------------------------------------------------------|
| Nessun segnale   | sotto -50 dBFS    | Controlla il cavo, la scelta del microfono e l'alimentazione phantom |
| Troppo basso     | sotto -18 dBFS    | Aumenta il gain sull'interfaccia                                   |
| Livello ottimale | da -18 a -3 dBFS  | Mantieni l'impostazione                                            |
| Troppo alto      | sopra -3 dBFS     | Riduci il gain, altrimenti la registrazione distorce               |

Nella stessa finestra scegli il profilo di loudness, cioè la norma per cui consegni, per esempio EBU/ARD-ZDF o Podcast. La spunta “Non mostrare al prossimo avvio” è attiva di fabbrica. Se vuoi che il Controllo livello compaia a ogni avvio, togli la spunta o attivalo in Impostazioni \> Generale.

### 3.4 Caricare un video

1.  Fai clic su **APRI VIDEO** o trascina il file nella finestra.
2.  Sono supportati MP4, MOV, M4V e MXF. WebM non è supportato.
3.  Con un MXF l'app crea prima una copia di riproduzione (proxy). Una barra di avanzamento mostra l'operazione. Alla successiva apertura la copia viene riutilizzata.

Se il video ha più di due tracce audio, cosa frequente con gli MXF, compare la finestra “Quali tracce audio vuoi importare?”:

- Metti una spunta su ogni traccia che ti serve. Nell'impostazione predefinita non è selezionata alcuna traccia.
- Con la parentesi accanto a una coppia (1+2, 3+4 ecc.) crei due tracce mono come un'unica traccia stereo.
- **Scegli per ogni riga il ruolo:** Auto, Premix IT, Voce, Presa diretta, Musica, Ambiente, Stadio o Effetti. Il ruolo guida in seguito AUTO MIX ([capitolo 7](#k7)).
- **Importa** applica la scelta. Se invece chiudi la finestra, l'intera importazione viene annullata.

I video con una o due tracce audio vengono importati senza domande con il ruolo Auto.

**Con un modello:** se il progetto contiene tracce di playout vuote provenienti da un modello ([sezione 15.4](#k15-4)), l'audio del video finisce su queste tracce. La finestra è allora precompilata, spunte e ruoli sono impostati come nel modello. Un avviso indica quante tracce vengono assegnate alle tracce già presenti nel modello. Confermi con **Importa**, così vedi un numero di tracce diverso nel nuovo materiale prima che abbia effetto. Con i video con una o due tracce audio l'app assegna le tracce senza domande. L'assegnazione automatica avviene solo se numero di traccia e formato (mono o stereo) corrispondono al modello, altrimenti vengono create nuove tracce come finora.

Una sequenza dal montaggio video la importi tramite un file AAF ([sezione 3.5](#k3-5)).

### 3.5 Importare una sequenza dal montaggio (AAF)

Con Archivio \> **Importa AAF...** porti le tracce audio di una sequenza dal montaggio video nel progetto aperto, per esempio da Avid Media Composer, Adobe Premiere Pro o DaVinci Resolve. Le tracce vengono aggiunte, ogni clip si trova nella sua posizione di timecode.

1.  Scegli Archivio \> **Importa AAF...** e apri il file AAF.
2.  Nella finestra “Importa AAF” decidi se attivare **Riprendere i livelli delle clip dal montaggio**. Nell'impostazione predefinita l'interruttore è disattivato: il volume delle clip e i keyframe di livello del montaggio vengono ignorati e AUTO MIX lavora con il materiale grezzo. Se è attivato, agiscono in aggiunta al livellamento di AUTO MIX, come linea di clip gain sul take.
3.  Fai clic su **Importa**. L'app legge la sequenza e decodifica i media. Una barra di avanzamento mostra l'operazione.
4.  Se dei file multimediali non si trovano nel percorso indicato nell'AAF, compare “File multimediali non trovati”. Con **Scegli cartella...** l'app li cerca in una cartella e nelle sue sottocartelle, con **Importa senza di essi** le clip interessate mancano.
5.  Controlla i ruoli (vedi sotto) e conferma.

I media possono essere incorporati nell'AAF o collegati come file separati, anche come MXF OP-Atom da Avid. Vengono ripresi clip, nomi delle clip, fade, pan delle tracce e automazione del pan. Le coppie mono che nel montaggio formano una traccia stereo vengono unite in tracce stereo. In un progetto vuoto l'app riprende il timecode iniziale della sequenza. Se il progetto contiene già materiale, le clip vengono collocate secondo il timecode del progetto.

**Ruoli:** perché AUTO MIX tratti correttamente le tracce, ogni traccia riceve un ruolo ([sezione 7.1](#k7-1)).

- **Dai nomi delle tracce:** se una traccia mono si chiama per esempio “Voice”, “Voiceover”, “Narrator”, “Sprecher” o “Kommentar”, diventa una traccia voce. Nomi come “Music”, “Musik”, “Atmo” o “FX” danno il ruolo corrispondente.
- **Dal contenuto:** per le tracce senza ruolo nel nome l'app ascolta l'audio e nella finestra “Ruoli dal contenuto” propone un ruolo: Presa diretta, Musica, Effetti o Ambiente. Il parlato viene sempre proposto come presa diretta, perché la traccia voce per il testo fuori campo nasce di solito solo dopo, con la registrazione. Controlla le proposte e, se serve, cambiale. **Senza ruoli dal contenuto** importa queste tracce senza ruolo.
- **Clip senza parlato su tracce di parlato:** se su una traccia di presa diretta o voce c'è una clip senza parlato, per esempio un rumore o il suono dell'ambiente, AUTO MIX la livellerebbe come parlato. L'app elenca queste clip. Le clip spuntate finiscono su una traccia separata con il ruolo adatto. **Lasciare i clip sulle loro tracce** riprende tutto invariato.

Dopo l'importazione un resoconto riassume che cosa è stato ripreso e che cosa no. Tra l'altro non vengono ripresi gli effetti di clip e di traccia, le variazioni di velocità (le clip scorrono alla velocità originale), il pan su singole clip e le forme di fade particolari, che vengono sostituite dalla forma standard. Per le clip con più di due canali vengono ripresi i canali 1 e 2. L'importazione non è possibile durante una registrazione o un salvataggio.

### 3.6 Prima registrazione

1.  Nell'intestazione della traccia voce fai clic su **R** per armare la traccia. Il tasto si illumina in rosso.
2.  Premi **REC** o il tasto R. Dopo il pre-roll (**PRE**, impostazione predefinita 4 secondi) inizia la registrazione.
3.  Termina la registrazione con **STOP REC** o di nuovo con il tasto R.
4.  Con la barra spaziatrice riproduci la registrazione.

Il [capitolo 4](#k4) descrive la registrazione in dettaglio, il [capitolo 7](#k7) il mix automatico e il [capitolo 12](#k12) l'esportazione.

## 4 Registrare

Si registra su ogni traccia armata. Più tracce possono essere armate contemporaneamente e ognuna è udibile, come nelle altre DAW.

### 4.1 Intestazione della traccia

| Tasto    | Nome                          | Funzione                                                                                                                                        |
|----------|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| R        | Armare                        | REC registra su questa traccia. Alt+clic agisce su tutte le tracce.                                                                             |
| I        | Ascolto ingresso (INPUT ONLY) | On: l'ingresso è sempre udibile, anche durante la riproduzione e senza R. Off (Auto Input): con la traccia armata l'ingresso è udibile solo da fermo e durante la registrazione. Si registra solo con R. |
| M        | Mute                          | Silenzia la traccia                                                                                                                             |
| S        | Solo                          | Ascolta solo questa traccia                                                                                                                     |
| AC       | AutoCut                       | Taglia automaticamente la registrazione successiva in corrispondenza delle pause                                                                |
| IMPORT   | Importa                       | Porta un file audio su questa traccia                                                                                                           |
| Ingresso | Selezione ingresso            | Ingresso dell'interfaccia che va sulla traccia                                                                                                  |

Il tasto I compare solo sulle tracce voce e solo quando il monitoraggio hardware è disattivato.

Con **+ Voice** crei una nuova traccia voce (mono), con **+ Audio** una traccia di playout (stereo) per musica, ambiente e simili.

Con un clic destro sull'intestazione della traccia o con l'icona a ingranaggio raggiungi altri comandi: Rinomina, Sposta su/giù, Voce di riferimento, unione o divisione stereo, Vista ed Elimina traccia. Puoi spostare le tracce anche trascinandone l'intestazione. Con Cmd+clic o Shift+clic selezioni più tracce. L'ultima traccia voce non può essere eliminata. Il colore di una traccia si cambia nel mixer con un doppio clic sul nome della traccia.

### 4.2 Pre-roll e post-roll

- **PRE** (pre-roll) stabilisce per quanto tempo il video scorre prima del punto di registrazione. Puoi impostare da 0 a 10 secondi, l'impostazione predefinita è 4 secondi. Con un doppio clic sul numero inserisci un valore.
- **POST** (post-roll) stabilisce per quanto tempo la riproduzione prosegue dopo la fine di una registrazione nell'intervallo.
- Durante il pre-roll il pulsante esegue un conto alla rovescia (per esempio “**PRE** 3.2s”), poi mostra **STOP REC**. Una nuova pressione interrompe la registrazione.
- **REC durante la riproduzione** registra subito dalla posizione di riproduzione, senza salto e senza pre-roll (punch-in in corsa). Il pre-roll vale solo per l'avvio da fermo.
- Se registri sopra un take esistente, la nuova registrazione sostituisce la parte sovrapposta. Ciò che si trova prima e dopo resta invariato.

### 4.3 Intervallo, loop e punch

In alto nel righello c'è una fascia per un intervallo. Questo intervallo vale sia per il loop sia per la registrazione nell'intervallo.

- **Creare un intervallo:** trascina nella fascia vuota. Trascinando un bordo cambi la lunghezza, trascinando al centro sposti l'intervallo, un doppio clic lo elimina. Inizio, fine e lunghezza si possono inserire anche nella barra di navigazione.
- **LOOP** o il tasto L ripete l'intervallo. Se non è impostato alcun intervallo, l'app usa la porzione visibile.
- **Registrazione solo nell'intervallo (punch):** un clic destro su **REC** commuta tra “registrazione fino a STOP” e “Registra nell'intervallo”. Nel secondo caso l'intervallo appare in arancione e la registrazione inizia e finisce esattamente ai suoi bordi. Se premi REC durante la riproduzione prima dell'intervallo, la registrazione attende il suo inizio. Fino ad allora il pulsante mostra il tempo di attesa (per esempio “**PUNCH** 2.5s”). All'interno dell'intervallo la registrazione inizia subito. Se la posizione di riproduzione è dopo l'intervallo o poco prima della sua fine, la riproduzione si ferma e la registrazione parte come da fermo, con pre-roll.

### 4.4 Voice Punch

Con **V-PUNCH**, dopo un errore di lettura, imposti il punto di ingresso con la voce:

1.  Premi **V-PUNCH**.
2.  Pronuncia le ultime parole corrette prima dell'errore.
3.  L'app cerca questo punto, colloca l'ingresso nella pausa successiva, riproduce il pre-roll e avvia la registrazione. Da lì riprendi a leggere.

Con Shift+clic su **V-PUNCH** pronunci anche le prime parole dopo l'errore. In questo caso viene sostituita solo la parte errata e l'originale prosegue dopo.

Requisiti: il progetto è salvato, la pagina **VIDEO** è aperta, il trasporto è fermo, una traccia voce è armata, il riconoscimento vocale di macOS è consentito e il take è già trascritto.

### 4.5 Marker

| Comando                           | Funzione                                         |
|-----------------------------------|--------------------------------------------------|
| Alt+M o MK +                      | Imposta un marker nella posizione di riproduzione |
| da 1 a 9                          | Imposta un marker nello slot da 1 a 9            |
| da Shift+1 a Shift+9              | Salta al marker da 1 a 9                         |
| Alt+virgola, Alt+punto            | Al marker precedente o successivo                |
| Trascinare la bandierina          | Sposta il marker                                 |
| Clic sull'etichetta               | Assegna un nome al marker                        |
| Doppio clic sulla bandierina      | Elimina il marker (si può annullare)             |

## 5 Prompter, Script Editor e finestra cabina

Durante la registrazione il prompter mostra il testo da leggere e segue la voce. Lo Script Editor mostra il parlato come testo. Lì puoi tagliare l'audio selezionando ed eliminando parole.

### 5.1 Prompter (pagina VIDEO)

Con **CARICA SCRIPT** apri un file di testo in formato .txt, .rtf o .pdf (PDF solo con livello di testo). Puoi anche trascinare il file nella finestra o incollare il testo con Cmd+V.

Mentre parli, il riconoscimento vocale di macOS ascolta e fa avanzare la riga corrente. Se scorri con la rotella del mouse, l'inseguimento si sospende per 8 secondi. Se il prompter non riesce a seguire la voce, per esempio perché manca la funzione di dettatura, mostra un avviso.

| Comando                               | Funzione                                                                                                     |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------|
| LANG                                  | Lingua del riconoscimento vocale, indipendente dalla lingua dell'app                                         |
| EDIT / DONE                           | Modifica direttamente il testo. Nel frattempo il riconoscimento vocale è in pausa.                           |
| A- / A+, Cmd+Meno / Cmd+Più / Cmd+0   | Dimensione del carattere                                                                                     |
| Tasti freccia                         | Una parola avanti o indietro                                                                                 |
| Pagina su, Pagina giù                 | 20 parole avanti o indietro                                                                                  |
| Home                                  | All'inizio del testo                                                                                         |
| Clic su una parola                    | La parola diventa la riga corrente. Se il testo è collegato a una registrazione, salta anche la timeline.    |
| FROM TAKE                             | Crea un testo per il prompter dalla trascrizione di una registrazione                                        |

### 5.2 Script Editor (pagina AUDIO)

Lo Script Editor mostra la trascrizione di tutte le tracce voce, ogni traccia nel suo colore. La trascrizione avviene sul Mac stesso e parte automaticamente dopo una registrazione, un'importazione o il caricamento di un progetto. Le tracce di playout non vengono trascritte.

- **Trascrivi** compare finché non c'è ancora testo. Se il testo manca solo in alcuni take, il pulsante si chiama **Trascrivi mancanti**.
- Un clic su una parola porta la testina nella pausa precedente.
- **Tagliare l'audio:** seleziona le parole trascinando e premi Canc. L'app taglia via l'audio, colloca i tagli nelle pause più vicine e chiude il vuoto. L'operazione si può annullare in un solo passaggio.
- **Correggere una parola:** doppio clic sulla parola, modifica il testo, premi Return. Cambia solo il testo, non l'audio.
- **Rimuovi intercalari** cerca parole riempitive come “ehm”, **Ricerca testo** trova punti nella trascrizione.
- **TEXT EXPORT** salva la trascrizione o i sottotitoli (SRT, VTT, TXT, JSON).

I tempi delle parole servono come orientamento. Per tagli molto precisi conviene ascoltare il risultato.

### 5.3 Finestra cabina

La finestra cabina (Finestra \> Finestra cabina, Cmd+Shift+B) è pensata per un monitor nella cabina dello speaker collegato via HDMI. Mostra a sinistra il prompter e a destra l'immagine con il timecode. Durante la registrazione compare una cornice rossa, durante il pre-roll il timecode diventa rosso. Il prompter nella finestra cabina scorre in sincrono con il prompter della finestra principale. Se è collegato un secondo schermo, la finestra si apre lì a schermo intero.

## 6 Montaggio nella timeline

La pagina **EDIT** mostra tutte le tracce in una timeline. Qui tagli i take, li sposti e applichi i fade.

### 6.1 Modificare i take

La metà superiore e la metà inferiore di un take reagiscono in modo diverso:

| Zona                            | Trascinando                                  |
|---------------------------------|----------------------------------------------|
| Metà inferiore                  | Sposti il take                               |
| Metà superiore                  | Selezioni un'area gialla nel take            |
| Bordo sinistro o destro         | Accorci o allunghi il take (trim)            |
| Maniglia del fade nell'angolo   | Imposti il fade-in o il fade-out             |

- Cmd+clic aggiunge take alla selezione, Cmd+A seleziona tutti i take.
- Con il tasto Control o Shift premuto un take trascinato cambia solo traccia, la posizione temporale resta invariata. Nel righello compare “TEMPO BLOCCATO”.
- Con il tasto Alt premuto il trascinamento non si aggancia.
- Cmd+freccia su o giù sposta il take sulla traccia adiacente, con Shift ne crea una copia.
- Freccia sinistra o destra sposta la selezione di un fotogramma, con Shift di un secondo.

### 6.2 Tagliare, eliminare, copiare

| Comando                                                        | Scorciatoia           |
|----------------------------------------------------------------|-----------------------|
| Dividere alla testina o ritagliare l'area selezionata          | Cmd+E                 |
| Eliminare                                                      | Canc o Backspace      |
| Copiare, incollare alla testina                                | Cmd+C, Cmd+V          |
| Duplicare                                                      | Cmd+D                 |
| Silenziare il take                                             | M                     |
| AutoCut (rimuove il silenzio)                                  | S                     |
| Annullare, ripetere                                            | Cmd+Z, Cmd+Shift+Z    |

I pezzi divisi ricevono nomi progressivi, per esempio “Take 3-01” e “Take 3-02”. Il clic destro su un take offre tra l'altro: Rename..., Replace audio..., Rimuovi selezione, Mantieni solo selezione, Abilita lo stretch (poi trascina il bordo per allungare o accorciare il take nel tempo), Fade / Crossfade e Reimposta correzione clip gain. Un clic destro su un punto vuoto offre “Inserisci audio qui...”.

### 6.3 Fade e crossfade

- **Tasto F:** seleziona un'area all'inizio o alla fine di un take e premi F. Si crea un fade. Se la selezione si trova sul confine tra due take, si crea un crossfade.
- **Sovrapposizione:** se trascini un take sopra un altro, sulla sovrapposizione si crea automaticamente un crossfade. Se si trova interamente all'interno di un altro take, entrambi i bordi ricevono un crossfade di 50 ms. Disattivi questa funzione in Impostazioni \> Dissolvenza incrociata in sovrapposizione. Il take trascinato sovrascrive allora quello sottostante.
- Cambi la lunghezza di un crossfade trascinando i bordi del riquadro del crossfade.

### 6.4 Clip gain

In basso a sinistra in ogni take c'è un piccolo controllo. Trascinandolo verso l'alto o verso il basso alzi o abbassi il volume dell'intero take, con Shift a passi fini. Un doppio clic azzera la correzione.

Sulla linea di clip gain nel take imposti dei punti con un clic, li trascini al livello desiderato e li elimini con un doppio clic. Così puoi alzare o abbassare il volume di singole parole. La linea di AUTO MIX e la tua correzione si sovrappongono come due livelli.

### 6.5 Zoom e vista

| Funzione                    | Comando                                                                              |
|-----------------------------|--------------------------------------------------------------------------------------|
| Zoom dell'asse temporale    | Interruttore a bilanciere a sinistra nella barra di trasporto, Cmd+= e Cmd+Meno, Cmd+rotella del mouse |
| Mostrare l'intero progetto  | Tasto 0                                                                              |
| Zoom sulla selezione        | Tasto Z                                                                              |
| Altezza traccia             | Secondo interruttore a bilanciere, Control+Alt+freccia su/giù, Alt+rotella del mouse |
| Ingrandire la forma d'onda  | Cmd+Alt+freccia su/giù, Shift+Alt+rotella del mouse                                  |
| All'inizio, alla fine       | Return, Fine                                                                         |
| Avvolgere                   | Virgola, punto (1 secondo ciascuno)                                                  |

### 6.6 Archivio media

**MEDIA** nella barra superiore apre l'archivio media (elenco clip). Contiene tutto il materiale del progetto nei gruppi IMPORTATO, AUDIO VIDEO, REGISTRAZIONI e INUTILIZZATI.

- **IMPORT** porta i file nell'archivio, ma non ancora su una traccia. I formati possibili sono WAV, BWF, AIFF, FLAC, OGG, MP3, M4A, AAC e CAF. I file importati mantengono il loro nome originale.
- **Preascolto:** lascia il puntatore del mouse per un attimo su una riga oppure usa i tasti freccia. La barra spaziatrice avvia e ferma, Esc termina.
- **Posizionare:** un doppio clic colloca il file nella posizione di riproduzione sulla traccia selezionata. In alternativa trascina il file nella timeline.
- Le regioni sono elencate con un rientro sotto il loro file. Un clic mostra la regione nella timeline, trascinando viene posizionata solo questa regione.
- **Con il clic destro:** Importa nella traccia selezionata, Mostra nel Finder, Rimuovi dall'elenco clip, Rimuovi inutilizzati.

Anche senza l'archivio puoi procedere così: seleziona la traccia e premi il tasto I. Il file scelto viene inserito nella posizione di riproduzione.

## 7 Modalità Assist e AUTO MIX

In modalità Assist il mix lo fa l'app. **AUTO MIX** (o Cmd+M) elabora la voce, abbassa musica e ambiente sotto il parlato e porta il mix alla loudness del profilo scelto. Dopo l'avvio è attiva la modalità Assist.

### 7.1 Preparazione: profilo, stile di mix e ruoli

In **PROGETTO...** \> Profilo di loudness stabilisci per quale norma consegni. Il profilo determina solo la consegna: la loudness di destinazione, il picco massimo ammesso (true peak) e la normalizzazione. Come suona il mix lo determina lo stile di mix (vedi sotto).

| Gruppo    | Profilo                  | Loudness                      | True Peak        |
|-----------|--------------------------|-------------------------------|------------------|
| TV/Radio  | EBU/ARD-ZDF              | -23 LUFS                      | -1 dBTP          |
| TV/Radio  | ATSC A/85 (USA)          | -24 LUFS                      | -2 dBTP          |
| TV/Radio  | ARIB TR-B32 (Giappone)   | -24 LUFS                      | -1 dBTP          |
| TV/Radio  | OP-59 (Australia)        | -24 LUFS                      | -2 dBTP          |
| TV/Radio  | CST-RT-040 (Francia)     | -23 LUFS                      | -3 dBTP          |
| Streaming | Podcast                  | -16 LUFS                      | -1 dBTP          |
| Streaming | YouTube                  | -14 LUFS                      | -1 dBTP          |
| Altro     | Audiolibro               | -18 LUFS                      | -3 dBTP          |
| Altro     | Studio 0 dB              | nessun obiettivo di loudness  | picco a 0 dBTP   |

**Stile di mix:** stabilisce come AUTO MIX bilancia le tracce, indipendentemente dal profilo di loudness. Lo scegli con il tasto accanto ad **AUTO MIX** nella barra di trasporto o in **PROGETTO...** nella riga **Stile di mix**. Un cambio si può annullare.

| Stile di mix             | Tasto nella barra |
|--------------------------|-------------------|
| Servizio / magazine      | SERVIZIO          |
| Trailer / promo          | TRAILER           |
| Documentario             | DOCU              |
| Sport / telecronaca      | SPORT             |
| Podcast / talk           | PODCAST           |
| Audiolibro / radiodramma | AUDIOLIBRO        |

L'impostazione predefinita è **Servizio / magazine**. Lo stile di mix imposta i valori di partenza, per esempio quanto il tappeto sta sotto la voce. Con **Trailer / promo** musica ed effetti guidano il mix, la voce sta sopra in modo più compatto e sotto la voce la musica cede solo nella gamma di frequenze della voce. Bassi e medio-bassi restano invariati.

I progetti salvati con i precedenti profili Trailer, Documentario, Sport, Podcast o Audiolibro si aprono con il profilo di loudness e lo stile di mix corrispondenti.

Ogni traccia ha inoltre bisogno di un ruolo. Il ruolo comunica all'automatismo che cosa c'è sulla traccia. Scegli il ruolo con il tasto del ruolo nell'intestazione della traccia o nel mixer.

| Ruolo                     | Sigla | Livello rispetto alla voce | Elaborazione da parte dell'automatismo                                                  |
|---------------------------|-------|----------------------------|-----------------------------------------------------------------------------------------|
| Voce                      | SPKR  | Livello di riferimento     | La voce viene elaborata e il suo livello viene livellato                                |
| Presa diretta             | OT    | stesso volume (0 LU)       | Viene bilanciata rispetto alla voce, con una propria catena vocale                      |
| Musica                    | MUS   | 4 LU più bassa             | Viene abbassata sotto la voce e la presa diretta                                        |
| Effetti                   | FX    | 4 LU più bassi             | Vengono abbassati                                                                       |
| Ambiente                  | ATMO  | 16 LU più basso            | Viene abbassato                                                                         |
| Stadio                    | STAD  | 5 LU più basso             | I salti di livello vengono compensati, ma la traccia non viene mai abbassata            |
| Premix IT                 | PRE   | invariato                  | Per un premix già pronto dal montaggio, si comporta come “Non classificato”             |
| Non classificato (Auto)   | AUTO  | invariato                  | Nessuna elaborazione                                                                    |

Le nuove tracce hanno il ruolo Voce. Una traccia di playout mono diventa traccia voce con la voce di menu “Voce - rendi questa una traccia voce”.

### 7.2 Avviare AUTO MIX

1.  Deve esserci almeno una registrazione e il Solo non deve essere attivo.
2.  Premi **AUTO MIX** a destra nella barra di trasporto o Cmd+M.
3.  Una finestra di avanzamento mostra i singoli passaggi: preparazione, preparazione voce, compressione e livello, timbro voce, tappeto e ducking, loudness. Con **Annulla** interrompi l'operazione in qualsiasi momento.
4.  Poi riproduci il mix finito con **PLAY**.

Prima del calcolo, in modalità Assist l'app porta tutti i fader del mixer a 0 dB. Si può annullare. Se sulle tracce di playout hai già impostato punti di automazione propri, l'app chiede: **Ricalcola**, **Mantieni i miei** o **Annulla**.

**AUTO MIX** non parte durante una registrazione (“Non durante la registrazione.”), con il Solo attivo (“Disattiva **SOLO** prima dell'AUTO MIX.”) e in modalità Manual. In modalità Manual normalizza invece l'esportazione.

### 7.3 Risultato di AUTO MIX

Tutte le decisioni dell'automatismo si possono vedere e modificare:

- **Linea di clip gain della voce:** il volume del parlato viene livellato tramite una linea sul take, entro un intervallo fino a 9 dB in su o in giù. La tua correzione si sovrappone come secondo livello.
- **Ducking come automazione del volume:** l'abbassamento di musica e ambiente sotto il parlato si trova come curva nell'automazione del volume della rispettiva traccia.
- **Valori nel channel strip:** EQ, compressore, de-esser e gli altri moduli sono impostati con i valori calcolati. Clic destro su un tasto \> **Visualizza...** mostra il modulo bloccato con questi valori.

Musica, effetti, ambiente e presa diretta hanno ciascuno una propria protezione dei picchi. Interviene solo se altrimenti il file finito supererebbe il limite di true peak del profilo. Un colpo forte nella musica quindi non abbassa più l'intero tappeto.

Se **AUTO MIX** è illuminato in blu, il mix salvato non corrisponde più al progetto, per esempio dopo una nuova registrazione o un taglio. In questo caso premi di nuovo il pulsante.

I progetti della versione 1.6 richiedono un nuovo **AUTO MIX**, perché nella versione 2.0 la catena del segnale è cambiata.

### 7.4 Possibilità di regolazione in modalità Assist

- I fader delle tracce si possono muovere. I fader del gruppo voce e del master sono fissi in modalità Assist (indicazione **FIXED**).
- I tasti nel channel strip si limitano ad attivare e disattivare i moduli. L'impostazione dei moduli la gestisce l'automatismo.
- Gli slot insert per i plug-in sono visibili, ma attivi solo in modalità Manual.

Chi vuole fare il mix da sé passa con **MANUAL** alla modalità Manual. Il mix di AUTO MIX viene ripreso integralmente come punto di partenza ([capitolo 8](#k8)).

## 8 Modalità Manual: mixer, channel strip, gruppi, master

In modalità Manual fai il mix da te, a mano come in una DAW. L'app non modifica alcun fader, l'ascolto avviene senza elaborazioni aggiuntive e l'esportazione scrive nel file esattamente ciò che senti.

### 8.1 Passare alla modalità Manual

Nella barra di trasporto fai clic su **MANUAL**. Il passaggio funziona anche durante la riproduzione e avviene con una dissolvenza, senza clic.

Procedura abituale: registra in modalità Assist ed esegui **AUTO MIX**, poi passa alla modalità Manual. Channel strip, moduli, linee di livello e ducking vengono ripresi così come suonavano l'ultima volta. Poi correggi i punti che vuoi diversi.

| Funzione                       | Assist                             | Manual                                                       |
|--------------------------------|------------------------------------|--------------------------------------------------------------|
| Pulsante AUTO MIX              | visibile                           | nascosto                                                     |
| Tasti nel channel strip        | solo on/off                        | on/off, apre il modulo per la modifica                       |
| Slot insert (plug-in)          | visibili, inattivi                 | attivi                                                       |
| Automazione                    | off (indicazione AUTO in grigio)   | Read, Touch, Latch, Write, Trim                              |
| Fader gruppo voce e master     | fissi (indicazione FIXED)          | liberi                                                       |
| Saturate e riverbero           | non udibili                        | udibili                                                      |
| Normalizzazione                | sempre, tramite AUTO MIX           | solo con la spunta “Normalizza” nella finestra di esportazione |

Se il mix in modalità Manual va in saturazione, un limitatore sull'uscita protegge l'udito. L'app segnala allora che l'esportazione andrebbe in clipping. In questo caso abbassa il fader del master o, all'esportazione, metti la spunta “Normalizza”.

### 8.2 Mixer

Apri il mixer con **MIXER** nella barra superiore. Ogni traccia ha un channel strip con le seguenti zone, dall'alto in basso:

1.  **Tasti DSP:** i nove moduli audio integrati ([capitolo 9](#k9))
2.  Ingresso
3.  **Insert:** cinque slot per plug-in ([capitolo 10](#k10))
4.  **Send:** cinque slot, nella versione 2.0 ancora senza funzione
5.  **Uscita:** solo indicazione
6.  Modalità di automazione ([capitolo 11](#k11))
7.  **Pan:** posizione nell'immagine stereo
8.  Fader con indicatore di livello, intervallo da meno infinito a +12 dB. Il fader usa tutta l'altezza libera della finestra.
9.  **S, M e tasto di registrazione:** solo, mute, armamento per la registrazione
10. Ruolo e nome

Con il menu contestuale del channel strip mostri o nascondi singole zone, per esempio gli insert o i send. Lì unisci anche due tracce mono in una traccia stereo o le dividi di nuovo.

Accanto al fader una barra color ciano mostra la riduzione di livello (gain reduction) del compressore, con tacche a 6 e 12 dB.

### 8.3 Tasti DSP

Ogni channel strip ha una griglia di nove tasti. Nel senso di lettura corrisponde all'ordine nel percorso del segnale:

|                          |                          |                          |
|--------------------------|--------------------------|--------------------------|
| REPR Riparazione         | NR Riduzione del rumore  | EQ Equalizzatore         |
| TAME Risonanza           | DES De-esser             | CMP Compressore          |
| BRTH De-Breath           | SAT Saturate             | REV Riverbero            |

- L'attivazione apre il modulo, la disattivazione lo chiude. Se un modulo è già attivo, il primo clic apre solo la finestra.
- **Cambiare l'ordine:** EQ, TAME, DES, CMP, BRTH e SAT si possono trascinare in un'altra posizione come gli insert. Un asterisco blu indica che l'ordine è stato modificato. Clic destro \> Ordine standard lo ripristina. REPR e NR stanno fissi all'inizio, REV fisso alla fine. Questi tasti portano un piccolo punto.
- Un tasto grigio con l'avviso “Solo in modalità Manual” agisce solo in modalità Manual.

Le tracce di playout (musica, ambiente, presa diretta ecc.) hanno la stessa griglia, con due limitazioni. Con il ruolo “Non classificato” la maggior parte dei tasti è bloccata finché non scegli un ruolo. NR e BRTH non esistono ancora sulle tracce di playout, il de-esser agisce solo con presa diretta e voce.

### 8.4 Gruppi: voce e IT

Accanto alle tracce ci sono due channel strip di gruppo. Il gruppo voce riunisce tutte le tracce voce, il gruppo IT tutte le tracce di playout (la colonna internazionale senza voce). Entrambi i gruppi hanno fader, automazione, insert e una griglia con EQ, TAME, CMP e REV, attiva solo in modalità Manual. Durante la riproduzione il fader del gruppo IT mostra come lavora il ducking.

### 8.5 Master

Il master è la somma che viene esportata.

- Fader del master con automazione.
- **PRE-GAIN** (fino a 24 dB in su o in giù) prima del fader. Qui AUTO MIX deposita la sua compensazione di livello, così dopo il passaggio alla modalità Manual il fader si trova a 0 dB. Trascinando cambi il valore, Shift consente passi fini, il doppio clic lo riporta a 0.
- **EQ** e **CMP** (compressore bus), solo in modalità Manual.
- **Indicatori di livello:** livello di picco sinistro e destro e loudness in LUFS come valore momentaneo, a breve termine e integrato. Il valore grande LUFS I è verde se si scosta al massimo di 1 LU dall'obiettivo, arancione fino a 3 LU e rosso oltre.
- **LRA**: la gamma di loudness, cioè quanto varia la loudness nel corso del programma.
- Indicatore **CLIP**: si accende dopo una saturazione. Un clic sul channel strip lo azzera.

Il channel strip dedicato **CUE** alimenta il percorso delle cuffie (**CUFFIE**) e ha uno slot insert.

## 9 I moduli audio

Ognuno dei nove moduli audio ha una propria finestra con i controlli. La visualizzazione nel modulo si basa sugli stessi valori con cui calcolano anche l'ascolto e l'esportazione.

Per tutti i moduli vale:

- La riga di stato mostra “Valori da AUTO MIX”, “Modificato (diverso da **AUTO MIX**)” o “Nessun AUTO MIX ancora - mostra la riproduzione”.
- **Reimposta ad AUTO MIX** ripristina i valori dell'automatismo.
- In modalità Assist clic destro \> **Visualizza...** apre il modulo bloccato con l'avviso “Impostato da **AUTO MIX**”. Il pulsante **Modifica in Manual** passa alla modalità Manual e sblocca il modulo.
- **Preset:** preset di fabbrica per categorie, inoltre “Utente”, “Salva preset...” e “Mostra cartella preset”. I preset propri si trovano in `~/Library/SATK/Presets/`. I preset si possono caricare solo in modalità Manual.
- Cmd+Z, Cmd+S e la barra spaziatrice funzionano anche quando una finestra di modulo è in primo piano.

### 9.1 REPR: Riparazione (De-Click e De-Plosive)

De-Click rimuove clic e schiocchi della bocca, De-Plosive attenua le esplosive di P e B sotto i 240 Hz.

[[IMG:repr.png|Il modulo REPAIR con De-Click e De-Plosive]]

| Controllo            | Intervallo     | Impostazione predefinita | Funzione                                               |
|----------------------|----------------|--------------------------|--------------------------------------------------------|
| SENSIBILITÀ          | da 0 a 10      | 4                        | Sensibilità del rilevamento dei clic                   |
| BARICENTRO FREQ.     | da -10 a +10   | 0                        | Sposta il rilevamento verso clic gravi o acuti         |
| ESTENSIONE CLIC      | da 0 a 10 ms   | 4 ms                     | Ampiezza dell'area riparata attorno a un clic          |

**SOLO CLIC** riproduce solo ciò che è stato rimosso. Così puoi verificare se viene rimosso troppo. De-Click lavora senza ritardo. I clic nelle pause del parlato vengono rimossi sull'intera banda di frequenze. De-Plosive lavora con impostazioni fisse. In modalità Assist REPR è disattivato, in modalità Manual si può attivare.

### 9.2 NR: Riduzione del rumore

NR rimuove rumori di fondo costanti come ventole, ronzio o rumore ambientale. Una rete neurale separa la voce dal rumore.

[[IMG:nr.png|Il modulo NR con il controllo Quantità]]

Il modulo ha un solo controllo, **QUANTITÀ** (da 0 a 100). Un segmento sull'anello attiva e disattiva NR, un doppio clic porta il valore a 100. Nel cerchio viene mostrato lo spettro misurato. NR è disattivato nell'impostazione predefinita e nemmeno AUTO MIX lo attiva. Nella versione 2.0 NR è disponibile sulle tracce voce.

Valori più alti rimuovono più rumore, ma possono alterare le S. Durante la regolazione fai attenzione alle S.

### 9.3 EQ: Equalizzatore

L'EQ modifica il suono di una traccia, per esempio per rendere una voce più brillante o più calda o per abbassare frequenze rimbombanti.

[[IMG:eq.png|Il modulo EQ con analizzatore, bande e controlli della dinamica]]

L'EQ ha nove bande: taglio bassi (passa-alto, da 20 Hz a 1 kHz), campane da 1 a 5, high shelf, taglio alti (da 1 a 20 kHz, disattivato nell'impostazione predefinita) e aria (8 kHz).

| Controllo              | Intervallo                                                          |
|------------------------|---------------------------------------------------------------------|
| FREQ                   | Frequenza in Hz                                                     |
| GAIN                   | da -18 a +18 dB                                                     |
| Q (larghezza di banda) | Campane da 0,15 a 14, shelf da 0,1 a 10, tagli da 0,3 a 4           |

Campane e shelf si possono rendere dinamici (**DYN**). La banda reagisce allora al livello e abbassa una frequenza, per esempio, solo quando diventa troppo forte. Controlli: **RANGE** (da -24 a +24 dB), **THRESHOLD** (da -80 a 0 dB), **ATTACK** (da 0,1 a 500 ms), **RELEASE** (da 5 ms a 5 s o AUTO).

**SOLO** sulla banda (o Alt+clic su un punto della banda) riproduce solo la gamma di frequenze di questa banda. Funziona anche in modalità Assist e non influisce mai sull'esportazione. L'analizzatore mostra lo spettro prima e dopo l'EQ. Nel menu **ANALYZER** imposti **POST**, **PRE**+**POST** o OFF, inoltre risoluzione, velocità, intervallo, inclinazione e congelamento.

### 9.4 TAME: Risonanza

TAME riconosce singoli toni fastidiosi, taglienti o rimbombanti e li abbassa solo nel momento in cui compaiono.

[[IMG:tame.png|Il modulo TAME (risonanza)]]

| Controllo        | Intervallo         | Funzione                                         |
|------------------|--------------------|--------------------------------------------------|
| SOFT / HARD      |                    | Funzionamento morbido o deciso                   |
| DEPTH            | da 0 a 10          | Entità dell'abbassamento                         |
| DETAIL           | da 0 a 10          | Quanto finemente vengono separati i singoli toni |
| ATTACK, RELEASE  | da 0 a 10          | Tempo di attacco e di rilascio                   |
| MIX              | da 0 a 100 %       | Quota del segnale elaborato                      |
| MAX CUT          | da off a 24 dB     | Abbassamento massimo                             |
| OUT, WET TRIM    | da -18 a +18 dB    | Livello di uscita                                |

Con fino a otto bande di sensibilità (campana, shelf, taglio, tilt e altre) stabilisci in quali gamme di frequenza TAME lavora con maggiore precisione. **DELTA** riproduce solo ciò che è stato rimosso. Ci sono 16 preset di fabbrica nei gruppi Generale, Parlato, Mix e Musica.

### 9.5 DES: De-esser

Il de-esser ammorbidisce i suoni taglienti di S, SC e Z senza rendere la voce opaca.

[[IMG:deesser.png|Il modulo DE-ESS]]

| Controllo                 | Intervallo                  | Funzione                                                           |
|---------------------------|-----------------------------|--------------------------------------------------------------------|
| SINGLE VOCAL / ALLROUND   |                             | Voce singola o materiale misto                                     |
| WIDE / SPLIT              |                             | Abbassa l'intero segnale o solo la gamma di frequenze tagliente    |
| THRESHOLD                 | da meno infinito a 0 dB     | Soglia di intervento                                               |
| RANGE                     | da 0 a 24 dB                | Abbassamento massimo                                               |
| LOOKAHEAD                 | da 0 a 15 ms, on/off        | Interviene già poco prima della S                                  |
| HIGH-PASS, LOW-PASS       | da 2 a 20 kHz               | Gamma di frequenze a cui reagisce il de-esser                      |

**TRIGGER** riproduce il segnale a cui reagisce il de-esser, **RIMOSSO** ciò che è stato rimosso. AUTO MIX misura la sibilanza di ogni voce e imposta il de-esser di conseguenza. Ci sono otto preset di fabbrica, per esempio per voci maschili e femminili.

### 9.6 CMP: Compressore

Il compressore bilancia i passaggi forti e quelli deboli, così la voce suona uniforme e presente. Il modulo mostra la curva caratteristica, l'andamento del livello e la riduzione di livello (in ciano).

[[IMG:comp.png|Il modulo compressore con curva caratteristica e andamento del livello]]

Ci sono tre modi di funzionamento: **CLEAN** (orientato ai picchi, per il parlato), **SMOOTH** (morbido, orientato al valore medio) e **BUS** (per gruppi e master).

| Controllo          | Intervallo                                       | Funzione                                                                                                     |
|--------------------|--------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| THRESHOLD          | da -60 a 0 dB                                    | Livello a partire dal quale si comprime                                                                      |
| RATIO              | da 1:1 a 100:1                                   | Entità della compressione                                                                                    |
| KNEE               | da 0 a 24 dB                                     | Intervento morbido o netto                                                                                   |
| ATTACK             | da 0,1 a 250 ms                                  | Tempo di attacco                                                                                             |
| RELEASE            | da 5 ms a 2,5 s o AUTO                           | Tempo di rilascio. Con AUTO si adatta alle pause del parlato e il valore impostato non ha effetto.           |
| MAKEUP             | da -12 a +24 dB (AUTO solo con CLEAN)            | Compensa la riduzione di livello                                                                             |
| MIX                | da 0 a 100 %                                     | Compressione parallela                                                                                       |
| HOLD, RANGE, DRY   | da 0 a 500 ms, da 0 a 60 dB, da off a +36 dB     | Regolazione fine, senza effetto con SMOOTH                                                                   |

Preset di fabbrica: Parlato - broadcast, Parlato - delicato, Musica - bus glue, Musica - tappeto denso, Ambiente - pad, Effetti - contieni i picchi. Per gruppi e master ci sono preset dedicati. Un preset imposta modo di funzionamento, ratio, knee, tempi e mix, ma non threshold e makeup.

### 9.7 BRTH: De-Breath

De-Breath abbassa i rumori del respiro tra le frasi senza alterare il parlato. I respiri vengono riconosciuti dal suono, non solo dal volume.

[[IMG:debreath.png|Il modulo DE-BREATH con panoramica e lente]]

| Controllo             | Intervallo                     | Impostazione predefinita |
|-----------------------|--------------------------------|--------------------------|
| RANGE (abbassamento)  | da 0 a 24 dB                   | 12 dB                    |
| Sensibilità           | PRUDENTE, NORMALE, ACCURATO    | NORMALE                  |

In alto il modulo mostra l'intera traccia, sotto una lente attorno alla testina con la forma d'onda prima e dopo l'elaborazione. Un clic su un respiro lo esclude dall'elaborazione o lo include di nuovo. Con Alt+trascinamento segni un respiro a mano. **BREATHS ONLY** riproduce solo i respiri. La riga di stato indica il numero di respiri trovati, impostati a mano e incerti. In modalità Assist De-Breath è attivo nell'impostazione predefinita. Agisce in riproduzione ed esportazione, ma non durante la registrazione.

### 9.8 SAT: Saturate

Saturate aggiunge una saturazione dal suono analogico, simile a una valvola o a un nastro. Il modulo agisce solo in modalità Manual ed è disattivato nell'impostazione predefinita.

[[IMG:sat.png|Il modulo SATURATE con curva caratteristica e spettro]]

Come tipo scegli **TUBE** o **TAPE**, ciascuno combinabile con **WARM**. Ne risultano Tube, Tape, Warm Tube e Warm Tape. Controlli: **DRIVE** (da 0 a 100), **MIX** (da 0 a 100), **OUTPUT** (da -24 a +24 dB). Ci sono preset di fabbrica come Clean e diverse varianti Tube e Tape.

### 9.9 REV: Riverbero

Il riverbero colloca una voce in un ambiente, dalla piccola cabina dello speaker alla grande sala. Agisce solo in modalità Manual ed è l'ultimo anello della catena. Una traccia voce diventa stereo a partire dal riverbero e la coda di riverbero è inclusa nell'esportazione.

[[IMG:rev.png|Il modulo riverbero (REVERB)]]

| Controllo     | Intervallo      | Impostazione predefinita | Funzione                               |
|---------------|-----------------|--------------------------|----------------------------------------|
| SPACE         | da 0,2 a 10 s   | 2,5 s                    | Tempo di riverbero, dimensione dell'ambiente |
| DECAY RATE    | da 0,5 a 2      | 1                        | Velocità di decadimento                |
| DISTANCE      | da 0 a 1        | 0,5                      | Distanza percepita della voce          |
| BRIGHTNESS    | da 0 a 1        | 0,5                      | Brillante o scuro                      |
| CHARACTER     | da 0 a 1        | 0,3                      | Colore timbrico dell'ambiente          |
| STEREO WIDTH  | da 0 a 1,2      | 0,7                      | Ampiezza stereo                        |
| MIX           | da 0 a 1        | 0,3                      | Quota del riverbero                    |
| PREDELAY      | da 0 a 500 ms   | 0                        | Distanza tra voce e riverbero          |

A questi si aggiungono livello di ingresso e di uscita, pan e due schede EQ (DECAY EQ e **POST** EQ). Ci sono circa 30 preset di fabbrica nei gruppi Ambience, Small, Medium, Large, Very Large e Voice, per esempio Vocal Booth, Narrator Polish e Radio Studio.

## 10 Plug-in e slot insert

Negli slot insert carichi plug-in di altri produttori nei formati Audio Unit (AU, anche AUv3) e VST3. Gli strumenti virtuali non vengono proposti. I plug-in sono attivi solo in modalità Manual. In modalità Assist gli slot sono visibili, ma senza effetto.

Ogni traccia, il gruppo voce, il gruppo IT e il master hanno cinque slot ciascuno, il channel strip CUE ne ha uno. I plug-in lavorano nell'ordine dall'alto in basso e seguono i moduli integrati.

### 10.1 Inserire un plug-in

1.  Fai clic su uno slot vuoto. Si apre la selezione, ordinata per produttore.
2.  Scegli il plug-in. La finestra del plug-in si apre subito.

### 10.2 Comandi sullo slot

| Comando                           | Funzione                                                                       |
|-----------------------------------|--------------------------------------------------------------------------------|
| Clic sul nome                     | Apre la finestra del plug-in                                                   |
| Simbolo on/off o Cmd+clic         | Bypass (esclude il plug-in)                                                    |
| x al passaggio del mouse          | Rimuove il plug-in (Cmd+Z lo ripristina)                                       |
| Clic destro                       | Menu per aprire l'editor, bypass, rimozione e nuova scansione dei plug-in      |

Se una finestra di plug-in è in primo piano, l'app continua a passare al trasporto la barra spaziatrice (Play/Stop), il tasto R (registrazione) e Home.

### 10.3 Elenco dei plug-in e nuova scansione

All'avvio l'app controlla i plug-in installati. Ogni plug-in viene testato in un proprio processo ausiliario. Se un plug-in va in crash, finisce in una lista di blocco e non mette a rischio l'app. Dopo l'installazione di nuovi plug-in o l'aggiornamento di un plug-in, scegli nel menu dello slot **Rescan plugins...**. In questo modo si svuota anche la lista di blocco e i plug-in non più presenti scompaiono dall'elenco.

Il ritardo (latenza) dei plug-in viene compensato automaticamente, anche su gruppi e master.

## 11 Automazione

L'automazione registra i movimenti dei controlli e li ripete a ogni riproduzione. Così, per esempio, un punto diventa automaticamente più basso e un altro più alto. L'automazione è disponibile in modalità Manual. In modalità Assist il tasto AUTO appare in grigio.

### 11.1 Parametri automatizzabili

- Volume (fader) su tracce, gruppo voce, gruppo IT e master
- Pan
- Mute
- **Parametri dei plug-in:** ogni controllo di un plug-in che muovi durante la registrazione dell'automazione

Il channel strip CUE non ha automazione.

### 11.2 Modalità di automazione

Scegli la modalità con il tasto di automazione nel channel strip. Nomi e comportamento corrispondono a quelli delle DAW più diffuse:

| Modalità            | Colore       | Comportamento                                                                                                                            |
|---------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------|
| READ                | grigio       | Riproduce la curva. Il fader si può comunque muovere, un indicatore mostra il valore dell'automazione.                                   |
| TOUCH               | azzurro      | Scrive solo finché il controllo viene toccato. Dopo il rilascio torna entro 0,25 secondi alla curva esistente.                           |
| LATCH               | blu scuro    | Scrive dal primo tocco e mantiene l'ultimo valore fino a STOP.                                                                           |
| WRITE               | rosso        | Scrive ininterrottamente da PLAY, anche senza tocco. Dopo un passaggio la traccia passa automaticamente a TOUCH.                         |
| TRIM (aggiuntiva)   | giallo       | Non scrive valori assoluti, ma una correzione della curva esistente, per esempio un intero ducking 2 dB più in basso.                    |

Automazione del mute: in **TOUCH** il tasto Mute funziona come un pulsante momentaneo e silenzia finché resta premuto. In **WRITE** si scrive dall'avvio, in **LATCH** fino a STOP.

### 11.3 Automazione nella timeline

Nell'intestazione della traccia commuti la vista tra forma d'onda e Volume. Alt+clic commuta tutte le tracce. Nella vista Volume vedi la curva e puoi impostare, spostare ed eliminare punti (selezionali e premi Canc). Anche il ducking di AUTO MIX è visibile qui come curva.

Le modalità di automazione vengono salvate con il progetto.

## 12 Esportazione

Con **EXPORT** nella barra di trasporto crei i file di consegna: il mix finito, se vuoi la voce come file separato, il video con il nuovo audio o un MXF per la messa in onda. Tutti i file finiscono in una cartella di consegna dedicata, i file esistenti non vengono sovrascritti.

### 12.1 Procedura

1.  In modalità Assist esegui **AUTO MIX** ([capitolo 7](#k7)), in modalità Manual completa il mix.
2.  Premi **EXPORT**. Si apre la finestra di esportazione.
3.  Nel campo **Nome** inserisci un nome per la consegna. Se resta vuoto, viene usato il nome del progetto.
4.  Scegli quali file devono essere creati (dalla [sezione 12.2](#k12-2) alla 12.4).
5.  Fai clic su **EXPORT** o premi Return. Se **Destinazione** è impostata su “Chiedi a ogni esportazione”, scegli ora la cartella di destinazione, altrimenti l'app scrive direttamente nella destinazione scelta.

**Destinazione:** nella riga **Destinazione** della finestra di esportazione scegli “Chiedi a ogni esportazione”, una delle ultime destinazioni usate oppure **Scegli cartella...**, per esempio una cartella su un server. La destinazione viene salvata nel progetto e quindi anche nei modelli. Se al momento dell'esportazione non è raggiungibile, per esempio perché l'unità del server non è connessa, o se mancano i permessi di scrittura, l'esportazione si interrompe con un messaggio invece di salvare i file in un altro posto. Nella finestra compare allora “Destinazione non raggiungibile - il server è connesso?”.

Nella cartella di destinazione viene creata una sottocartella con il nome della consegna. I file si chiamano per esempio `Beitrag_2026-11-19_v1_mix.wav` e `Beitrag_2026-11-19_v1_voice.wav`. A ogni esportazione successiva il numero di versione aumenta (v2, v3 ecc.).

### 12.2 Audio

| Riga                                            | Contenuto                                                                                               | Impostazione predefinita |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------|--------------------------|
| Mix audio                                       | Mix finito (stereo)                                                                                     | on, WAV 24 bit           |
| Stem voce                                       | Solo la voce o le voci, per esempio per un nuovo mix in seguito                                         | off                      |
| Tracce voce separate                            | Un file per ogni traccia voce senza effetti, disponibile solo con almeno due tracce voce                | off                      |
| Lista di montaggio per altre DAW (AES31, .adl)  | Per aprire il progetto in Pro Tools, Nuendo e altre DAW. Il progetto deve essere salvato.               | off                      |

Formati disponibili: WAV, AIFF, AAC (.m4a), MP3, MP2 (.mp2), MP2 (.wav), FLAC e Opus.

| Impostazione                          | Scelta                                        | Limitazione                                          |
|---------------------------------------|-----------------------------------------------|------------------------------------------------------|
| Frequenza di campionamento            | Progetto, 44,1, 48, 88,2 o 96 kHz             | MP2 e MP3 al massimo 48 kHz, Opus sempre 48 kHz      |
| Profondità di bit (WAV, AIFF, FLAC)   | 16 bit con dither, 24 bit, 32 bit float       | FLAC al massimo 24 bit                               |
| Bitrate (MP3, AAC, MP2, Opus)         | 128, 192, 256 o 320 kbit/s                    | 384 kbit/s solo con MP2                              |

I file WAV ricevono un timestamp secondo lo standard BWF, a partire dal timecode iniziale del progetto.

### 12.3 Normalizzare

La spunta “Normalizza a -23 LUFS (...)” porta il file alla loudness di destinazione del profilo e limita i picchi con un limiter true peak. Il valore nell'etichetta dipende dal profilo. Con il profilo Studio 0 dB si normalizza invece a un livello di picco di 0 dBTP.

- In modalità Assist normalizza già AUTO MIX. L'esportazione restituisce il mix finito.
- In modalità Manual si normalizza solo se la spunta è attiva. Una riga nella finestra indica di quanto il file si scosterà allora dal tuo ascolto.
- La spunta vale ogni volta solo per l'esportazione corrente.
- Inoltre puoi scegliere “Limita la gamma di loudness (LRA a 6 LU, multibanda)”. Questa opzione riduce le grandi variazioni di volume.

### 12.4 Video e MXF

In **USCITE** scegli **Video (MOV/MP4)** o **MXF (broadcast)**. È attiva l'opzione adatta al video caricato. L'immagine viene ripresa invariata e viene inserito il nuovo audio.

Per l'MXF ci sono impostazioni aggiuntive:

- **Profilo di delivery:** EBU R128, US ATSC - IT 8, Stereo, DE ARD/ZDF - HDF01a, JP ARIB - RDD9, FR CST - AS-10. Se il profilo di loudness del progetto non corrisponde al profilo di delivery, compare un avviso rosso.
- **Numero di tracce:** 8 o 16 tracce audio. I profili di delivery JP ARIB - RDD9 e FR CST - AS-10 consentono solo 8 tracce audio. Con questi profili l'app imposta 8 tracce e lo segnala.
- Preimpostazione per le tracce audio, per esempio “Mix 1+2, voce 7+8”. In “I miei preset” trovi le assegnazioni che hai salvato.
- **Assegnazione tracce:** per ogni traccia (da T1 a T8 o T16) stabilisci che cosa contiene (mix L o R, voce, muto o un canale della sorgente). Il nome di una traccia è solo un nome e non ne cambia il contenuto.

Con **Salva assegnazione come preset...** nell'elenco delle preimpostazioni salvi l'assegnazione corrente con un nome. Vengono salvati il numero di tracce e il contenuto e il nome di ogni traccia.

Accanto all'MXF viene creato automaticamente un foglio di assegnazione (`<Nome>_tracks.txt`) che descrive l'assegnazione effettiva delle tracce.

### 12.5 Podcast: capitoli e dati dell'episodio

Per i podcast apri la finestra Capitoli (Finestra \> Capitoli, Cmd+Shift+K):

1.  Porta la testina all'inizio del capitolo e fai clic su **Aggiungi alla testina**.
2.  Inserisci il titolo, facoltativamente un'immagine e un link. I capitoli senza titolo non vengono esportati.
3.  In **PROGETTO...** \> EPISODIO inserisci titolo, autore, programma, commento e immagine di copertina. L'immagine di copertina deve essere quadrata e misurare da 1400 a 3000 pixel, le immagini dei capitoli almeno 600 pixel.

All'esportazione il mix riceve i tag ID3 e i capitoli. Inoltre viene creato un file dei capitoli `<Nome>-chapters.json` secondo lo standard Podcasting 2.0, insieme alle immagini dei capitoli.

### 12.6 Sottotitoli e trascrizione

Esporti i sottotitoli nello Script Editor della pagina **AUDIO** con **TEXT EXPORT**. Sono disponibili SubRip (.srt), WebVTT (.vtt), testo semplice (.txt) e JSON (Podcast 2.0).

## 13 Registrazione remota, videocamera virtuale e cue

Nella registrazione remota lo speaker si trova in un altro luogo ed è collegato tramite un servizio via browser o di videoconferenza. Per questo voyzSESSION PRO include un proprio dispositivo audio virtuale e una videocamera virtuale. Lo speaker vede la tua immagine, sente il video e la regia e parla direttamente nella tua traccia di registrazione.

### 13.1 Configurazione una tantum

1.  **Installare il driver audio:** Impostazioni \> Audio/video..., lì in “Virtual audio device” fai clic su **Install**. Poi riavvia l'app. Si creano due dispositivi: voyzSESSION Send (uscita dall'app) e voyzSESSION Return (ingresso nell'app).
2.  **Installare la videocamera:** nel menu dell'app scegli **Installa videocamera virtuale...**. L'app deve trovarsi nella cartella Applicazioni. macOS richiede un'autorizzazione in Impostazioni di Sistema \> Generali \> Elementi di login ed estensioni \> Estensioni videocamera. In alcuni casi è necessario un riavvio. **Stato videocamera virtuale...** indica se la videocamera è attiva.
3.  Nelle impostazioni A/V attiva **Virtual camera (video to browsers)**.

Nella versione 2.0 la finestra delle impostazioni A/V è ancora in inglese, anche se l'app è impostata in italiano.

### 13.2 Svolgere una sessione

1.  Nel servizio di videoconferenza o via browser (per esempio SessionLink PRO, Zoom o Teams) imposta: microfono = voyzSESSION Send, altoparlante = voyzSESSION Return, videocamera = voyzSESSION.
2.  In voyzSESSION PRO assegna la traccia voce all'ingresso voyzSESSION Return L (o R).
3.  Nel mixer, sul channel strip **CUE**, misura la latenza con **MESSEN**. L'app invia un tono di prova a basso volume allo speaker e lo cerca nel percorso di ritorno. Il risultato viene mostrato in millisecondi.
4.  Registra come di consueto ([capitolo 4](#k4)).
5.  **Dopo la registrazione:** clic destro sul take \> **Allinea alla latenza del collegamento**. Il take viene spostato in avanti del ritardo misurato e si trova di nuovo in sincrono con l'immagine.

### 13.3 Cue: cosa sente lo speaker

Il percorso cue verso lo speaker contiene l'audio del video e delle tracce di playout, i take precedenti e il talkback. La voce dal vivo dello speaker non viene rimandata indietro, così lo speaker non si sente in ritardo.

- **TALK** nel channel strip **CUE** attiva il microfono del talkback, solo da fermo. Il talkback non si sente mai dai propri altoparlanti.
- Il fader cue regola il volume verso lo speaker (da -48 a +6 dB). L'invio avviene a -23 LUFS.
- Durante la normale riproduzione il percorso di ritorno si sente solo se sulla traccia è attivo il tasto I (ascolto ingresso). Durante la registrazione è sempre udibile.

### 13.4 Finestra cabina e finestra video

Per uno speaker nella tua cabina c'è la finestra cabina (Finestra \> Finestra cabina, Cmd+Shift+B). Viene mostrata su un monitor collegato via HDMI ed è quindi senza ritardo. A sinistra c'è il prompter, a destra l'immagine con il timecode, durante la registrazione compare una cornice rossa. La finestra video (Cmd+9 o **IMMAGINE**) mostra solo l'immagine senza cornice, se vuoi su uno schermo esterno.

## 14 Controllo esterno: Stream Deck, superfici di controllo, OSC

voyzSESSION PRO si può comandare con un Elgato Stream Deck, una superficie di controllo Mackie Control o via OSC. È utile, per esempio, quando uno speaker lavora da solo in cabina.

### 14.1 Stream Deck

1.  Nel menu dell'app scegli **Stream Deck: installa plug-in...**. Il software Elgato acquisisce il plug-in.
2.  In **Stream Deck: carica layout** scegli il modello adatto: Stream Deck (15 tasti), Stream Deck MK.2 (15 tasti), Stream Deck Mini (6 tasti), Stream Deck XL (32 tasti) o Stream Deck + (manopole).
3.  Nelle impostazioni A/V attiva **OSC remote control**. Il plug-in comunica con l'app tramite OSC.

I tasti mostrano lo stato dell'app, per esempio on/off o i valori correnti. I tasti del channel strip sono nello stesso ordine del mixer e commutano anche le tracce di playout.

### 14.2 Superficie Mackie Control (MCU)

Nelle impostazioni A/V, in **MCU FADER CONTROLLER (MIDI)**, scegli la porta MIDI della tua superficie. L'indicazione **RECEIVING** mostra che arrivano dati dalla superficie.

| Elemento della superficie           | Funzione                                                   |
|-------------------------------------|------------------------------------------------------------|
| 8 fader (sensibili al tocco)        | Volume delle tracce, come il fader sullo schermo           |
| V-Pot, pressione del V-Pot          | Pan, pan al centro                                         |
| REC, SOLO, MUTE, SELECT             | Per canale (REC solo sulle tracce voce)                    |
| PLAY, STOP, RECORD                  | Trasporto (STOP da fermo salta all'inizio)                 |
| CYCLE                               | Loop                                                       |
| Riavvolgimento, avanzamento rapido  | Avvolgimento                                               |
| BANK, CHANNEL                       | Sposta il banco di fader di 8 o di 1 traccia               |

Il fader master della superficie controlla il master, il display del timecode della superficie segue la riproduzione.

### 14.3 OSC e display nel browser

- **OSC:** l'app riceve sulla porta 8000 e restituisce gli stati, nell'impostazione predefinita a 127.0.0.1:9000 (modificabile in **OSC REPLY TO**). Via OSC sono accessibili trasporto, funzioni di traccia (arm, solo, mute, modalità di automazione), montaggio, marker, viste, **AUTO MIX**, salvataggio, esportazione e talkback.
- **Display della console nel browser:** attiva **Console displays (web)**, copia gli indirizzi con **COPY URLS** e aprili su un tablet o su un secondo computer nella stessa rete (porta 8422, con chiave di accesso nell'indirizzo).

## 15 Impostazioni, progetti, salvataggio e ripristino

### 15.1 Impostazioni > Generale (Cmd+,)

| Riga                 | Funzione                                                                                                                            |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Lingua               | Automatico (lingua di sistema), Deutsch, English, Français, Español, Italiano, Português. La modifica ha effetto al prossimo avvio. |
| Lingua del prompter  | Lingua in cui il riconoscimento vocale segue il testo                                                                               |
| Controllo livello    | “Mostra il controllo livello all'avvio” on o off. Disattivato nell'impostazione predefinita.                                        |
| Suggerimenti         | “Mostra di nuovo i suggerimenti” mostra di nuovo gli avvisi che compaiono una sola volta                                            |

Direttamente nel menu Impostazioni si trova l'interruttore **Dissolvenza incrociata in sovrapposizione** (attivo nell'impostazione predefinita, vedi [capitolo 6](#k6)).

### 15.2 Impostazioni > Audio/video (pulsante A/V...)

- **OUTPUT e INPUT:** dispositivo di uscita e di ingresso, selezionabili indipendentemente l'uno dall'altro, per esempio un microfono USB insieme a un'interfaccia.
- **SAMPLE RATE e BUFFER SIZE:** dimensione del buffer da 32 a 1024 campioni. Un buffer piccolo riduce il ritardo in cuffia, ma aumenta il carico di calcolo. Sotto è indicato il ritardo complessivo misurato (Round trip).
- **Direct hardware monitoring:** lascialo attivo se ti ascolti tramite l'interfaccia (impostazione predefinita). L'ascolto via software è allora muto, così non ti senti due volte.
- **RECORDING DELAY:** sposta i nuovi take di alcuni campioni, se l'interfaccia li registra sfasati.
- **Low latency monitoring:** sulle tracce in ascolto esclude i plug-in con un ritardo troppo alto. Questi plug-in vengono segnati in arancione. L'esportazione non ne è influenzata.
- **Inoltre:** superficie MCU, dispositivo audio virtuale, display nel browser, OSC e videocamera virtuale ([capitoli 13](#k13) e 14).

### 15.3 Impostazioni del progetto (pulsante PROGETTO...)

Le modifiche hanno effetto subito.

- **AUDIO, Frequenza di campionamento:** la frequenza di campionamento è determinata dal progetto, non dall'interfaccia. In un progetto vuoto la imposti direttamente. Se il progetto contiene già materiale, scegli **Salva copia con altra frequenza di campionamento**. L'app converte allora una copia, l'originale resta invariato.
- **TEMPO E IMMAGINE:** frame rate (da 23,976 a 60 fps, anche drop frame), timecode iniziale (scelta rapida 00:00:00:00 o 10:00:00:00) e **Prendi dal video**. Se il frame rate del video è diverso, viene mostrato in rosso.
- **LOUDNESS:** profilo di loudness e stile di mix ([sezione 7.1](#k7-1)).
- **EPISODIO:** dati per i podcast ([sezione 12.5](#k12-5)).

### 15.4 Salvataggio, modelli, ripristino

- Salva con Cmd+S, Salva con nome con Cmd+Shift+S oppure tramite il pulsante **FILE**. Un progetto è una cartella con l'estensione `.satkproj`. Le registrazioni vengono salvate direttamente nella sottocartella `audio` del progetto salvato. Per questo conviene salvare un nuovo progetto prima della prima registrazione.
- Cmd+S durante un **AUTO MIX** viene messo in coda ed eseguito al termine.
- **Modelli:** **FILE** \> **Salva l'attuale come modello...** salva tracce, impostazioni, insert, profilo e testo del prompter, ma non registrazioni, video, capitoli e marker. Crei poi i nuovi progetti con **FILE** \> **Nuovo da modello**. Nel modello le tracce di playout mantengono il loro ruolo e la loro assegnazione alle tracce audio del video. Alla successiva importazione di un video l'app riempie queste tracce ([sezione 3.4](#k3-4)). Anche la destinazione di esportazione viene salvata nel modello.
- **Salvataggio automatico:** in caso di modifiche l'app salva ogni 30 secondi uno stato di ripristino. Dopo un crash, al successivo avvio chiede se ripristinare o scartare questo stato.
- **Registrazione interrotta:** se una registrazione in corso è stata interrotta da un crash, alla successiva apertura l'app segnala “Trovata registrazione interrotta”. **Ripristina** la crea come take, **Scarta** sposta i file nel Cestino. **Più tardi**, Esc o la chiusura della finestra li lasciano invariati, e l'app chiede di nuovo alla successiva apertura.
- **Uscire:** se ci sono modifiche non salvate, l'app chiede se salvare, scartare o annullare. La stessa domanda compare con Nuovo e Apri.

## Appendice

### A Scorciatoie da tastiera

I tasti senza Cmd, Alt o Control non hanno effetto finché è attivo un campo di testo.

| Area       | Tasto                               | Funzione                                                     |
|------------|-------------------------------------|--------------------------------------------------------------|
| Trasporto  | Barra spaziatrice                   | Riproduzione, stop                                           |
| Trasporto  | R                                   | Avvia o termina la registrazione                             |
| Trasporto  | L                                   | Loop on o off                                                |
| Trasporto  | Return, Fine, Home                  | All'inizio, alla fine, alla posizione 0                      |
| Trasporto  | Virgola, punto                      | 1 secondo indietro o avanti                                  |
| Marker     | Alt+M                               | Imposta un marker                                            |
| Marker     | da 1 a 9, da Shift+1 a Shift+9      | Imposta un marker, salta al marker                           |
| Marker     | Alt+virgola, Alt+punto              | Marker precedente o successivo                               |
| Modifica   | Cmd+Z, Cmd+Shift+Z                  | Annulla, ripeti                                              |
| Modifica   | Cmd+E                               | Dividi                                                       |
| Modifica   | Cmd+C, Cmd+V, Cmd+D                 | Copia, incolla, duplica                                      |
| Modifica   | Cmd+A                               | Seleziona tutti i take                                       |
| Modifica   | Canc                                | Elimina la selezione                                         |
| Modifica   | M                                   | Silenzia il take                                             |
| Modifica   | S                                   | AutoCut                                                      |
| Modifica   | F                                   | Fade o crossfade                                             |
| Modifica   | I                                   | Importa audio nella posizione di riproduzione                |
| Modifica   | Cmd+freccia su/giù                  | Sposta il take sulla traccia adiacente, con Shift copia      |
| Modifica   | Freccia sinistra/destra             | Sposta la selezione di 1 fotogramma, con Shift di 1 secondo  |
| Vista      | Cmd+=, Cmd+Meno                     | Zoom                                                         |
| Vista      | 0, Z                                | Intero progetto, selezione                                   |
| Vista      | Control+Alt+freccia su/giù          | Altezza traccia                                              |
| Vista      | Cmd+Alt+freccia su/giù              | Altezza della forma d'onda                                   |
| Mix        | Cmd+M                               | AUTO MIX                                                     |
| Progetto   | Cmd+S, Cmd+Shift+S                  | Salva, Salva con nome                                        |
| Finestra   | Cmd+,                               | Impostazioni \> Generale                                     |
| Finestra   | Cmd+9                               | Finestra video                                               |
| Finestra   | Cmd+Shift+B                         | Finestra cabina                                              |
| Finestra   | Cmd+Shift+K                         | Capitoli                                                     |
| Prompter   | Cmd+Più, Cmd+Meno, Cmd+0            | Dimensione del carattere                                     |
| Aiuto      | Cmd+Shift+/                         | Manuale                                                      |

### B Glossario

| Termine                           | Significato                                                                               |
|-----------------------------------|-------------------------------------------------------------------------------------------|
| AUTO MIX                          | Mix automatico in modalità Assist                                                         |
| Bounce                            | Scrivere il mix in un file così come si sente                                             |
| Clip gain                         | Volume direttamente sul take, prima del channel strip                                     |
| Crossfade                         | Dissolvenza incrociata tra due take                                                       |
| Ducking                           | Abbassamento automatico di musica o ambiente mentre si parla                              |
| Fader                             | Cursore per il volume                                                                     |
| Insert                            | Slot per un plug-in nel channel strip                                                     |
| IT (colonna internazionale)       | Tutti gli elementi tranne la voce: presa diretta, musica, ambiente, effetti               |
| LUFS, LU                          | Unità di misura della loudness percepita. -23 LUFS è la norma televisiva in Europa.       |
| LRA                               | Gamma di loudness, cioè quanto varia la loudness nel corso del programma                  |
| Presa diretta                     | Audio originale del video, per esempio un'intervista                                      |
| Pre-roll, post-roll               | Tempo di avvio prima di una registrazione e tempo di coda dopo                            |
| Punch                             | Registrazione solo in un intervallo stabilito, per sostituire un punto                    |
| Ruolo                             | Tipo di contenuto di una traccia (voce, musica ecc.), guida l'automatismo                 |
| Armare                            | Preparare una traccia per la registrazione                                                |
| Stem                              | Singolo elemento del mix come file separato, per esempio solo la voce                     |
| Take, regione                     | Pezzo di audio registrato o importato su una traccia                                      |
| True peak (dBTP)                  | Valore di picco massimo effettivo del segnale                                             |

### C Risoluzione dei problemi

| Problema                                                          | Soluzione                                                                                                                                                                                  |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Il Controllo livello mostra “Nessun segnale”                      | Controlla il microfono nel Controllo livello e in A/V... \> INPUT. Verifica inoltre che macOS consenta l'accesso al microfono (Impostazioni di Sistema \> Privacy e sicurezza \> Microfono). |
| REC non avvia la registrazione                                    | Deve essere armata una traccia (R). Senza traccia armata l'app segnala “Nessuna traccia armata”. Un nuovo progetto deve essere prima salvato.                                              |
| La propria voce si sente doppia o con eco                         | La voce arriva contemporaneamente dall'interfaccia e dal software. In A/V... attiva Direct hardware monitoring oppure disattiva il Direct Monitor sull'interfaccia.                        |
| AUTO MIX non parte                                                | Disattiva il Solo, termina la registrazione in corso, passa alla modalità Assist. Deve esserci almeno un take.                                                                             |
| AUTO MIX è illuminato in blu                                      | Il mix salvato non corrisponde più al progetto. Esegui di nuovo AUTO MIX.                                                                                                                  |
| Messaggio che l'esportazione andrebbe in clipping (modalità Manual) | Abbassa il fader del master o attiva “Normalizza” all'esportazione.                                                                                                                      |
| Un plug-in manca nell'elenco                                      | Nel menu dello slot esegui Rescan plugins. Gli strumenti virtuali non vengono mai proposti.                                                                                                |
| Un plug-in fa andare in crash l'app                               | Al successivo avvio il plug-in finisce nella lista di blocco. Dopo un aggiornamento del plug-in esegui una nuova scansione.                                                                |
| Il prompter non segue la voce                                     | Consenti il riconoscimento vocale in macOS e attiva la funzione di dettatura. Con LANG imposta la lingua del testo.                                                                        |
| Lo Script Editor resta vuoto                                      | Premi Trascrivi. Le tracce di playout non vengono trascritte.                                                                                                                              |
| La videocamera virtuale non compare                               | L'app deve trovarsi nella cartella Applicazioni. Autorizza l'estensione nelle Impostazioni di Sistema, se necessario riavvia il Mac e in A/V... attiva la videocamera.                      |
| Manca voyzSESSION Send o Return                                   | Installa il driver in A/V... e riavvia l'app.                                                                                                                                              |
| Il frame rate è mostrato in rosso                                 | Video e progetto hanno frame rate diversi. In PROGETTO... scegli “Prendi dal video”.                                                                                                       |
| L'esportazione si interrompe: destinazione non raggiungibile     | Connetti l'unità del server o nella finestra di esportazione scegli un'altra cartella in Destinazione.                                                                                    |
| Importazione AAF: file multimediali non trovati                  | Fai clic su **Scegli cartella...** e indica la cartella con i media del montaggio. L'app cerca anche nelle sottocartelle.                                                                  |
| L'app è andata in crash                                           | Al successivo avvio scegli il ripristino. In caso di modifiche l'app salva ogni 30 secondi.                                                                                                |
| Lingua dell'interfaccia errata                                    | Scegli Impostazioni \> Generale \> Lingua e riavvia l'app.                                                                                                                                 |
| La finestra delle impostazioni A/V è in inglese                   | Questa finestra non è ancora tradotta nella versione 2.0. Il resto dell'app segue la lingua scelta.                                                                                        |

### D Marchi

Tutti i nomi di prodotti e aziende citati in questo manuale sono marchi o marchi registrati dei rispettivi proprietari. Sono citati solo per indicare con che cosa funziona voyzSESSION PRO. La loro menzione non implica alcun legame con queste aziende né alcuna loro approvazione.
