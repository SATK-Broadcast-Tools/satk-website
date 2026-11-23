## 1 Introduction

voyzSESSION PRO est un logiciel d'enregistrement et de mixage (DAW) pour les productions vocales : voix off et commentaire sur image, doublage, sujets radio, podcasts et livres audio.

Pour les productions sur image, vous chargez une vidéo, enregistrez le texte en synchronisation et exportez le mix final sous forme de fichier audio ou directement dans la vidéo ou dans le MXF. Les productions purement audio comme un podcast, un livre audio ou un sujet radio se passent de vidéo. Elles disposent de la page **AUDIO** avec le Script Editor, de profils de loudness pour la radio, le podcast et le livre audio, ainsi que de formats d'export comme MP2, MP3, FLAC et Opus.

### 1.1 Mode Assist et mode Manual

|                   | Mode Assist                                                                     | Mode Manual                                                |
|-------------------|---------------------------------------------------------------------------------|------------------------------------------------------------|
| Destiné à         | Comédiens voix off, journalistes et monteurs sans connaissances en technique du son | Ingénieurs du son et mixeurs                           |
| Qui mixe          | L'automatisme (AUTO MIX)                                                        | Vous-même, comme dans Pro Tools ou Logic                   |
| Usage typique     | Enregistrement et livraison rapide                                              | Montage et mixage fin                                      |
| Résultat          | Mix conforme à la norme de loudness choisie, d'un simple clic                   | Contrôle total des réglages, des plug-ins et de l'automation |

Ce que l'AUTO MIX calcule en mode Assist, le mode Manual le reprend comme point de départ. Vous pouvez enregistrer dans les deux modes.

### 1.2 Configuration requise

|                        | Recommandé                                              | Minimum                                             |
|------------------------|---------------------------------------------------------|-----------------------------------------------------|
| Mac                    | Puce Apple (M1 ou plus récente)                         | Mac Intel (fonctionne, mais déconseillé)            |
| Système d'exploitation | macOS 14 Sonoma ou ultérieur                            | macOS 14 Sonoma                                     |
| Mémoire vive           | 32 Go pour des projets de plus de 30 minutes avec vidéo 4K | 16 Go                                            |
| Stockage               | SSD                                                     | 5 Go libres, plus l'espace pour le matériel du projet |
| Audio                  | Interface audio avec micro et casque                    | Micro intégré ou micro USB                          |

Sur les Mac Intel et avec moins de 16 Go de mémoire vive, l'app affiche une seule fois, au premier lancement, une remarque sur le matériel. Le pilote audio pour l'enregistrement à distance nécessite macOS 13, la caméra virtuelle macOS 12.3. Ces deux conditions sont remplies avec macOS 14.

### 1.3 Installation

1.  Téléchargez `voyzsession-2.0.dmg` sur pegelwerk.com.
2.  Ouvrez le DMG et faites glisser voyzSESSION PRO dans le dossier Applications. La caméra virtuelle ne fonctionne que si l'app s'y trouve.
3.  Lancez l'app. macOS demande l'accès au micro. Autorisez-le, sinon aucun enregistrement n'est possible.
4.  À la première ouverture du prompteur, macOS demande l'accès à la reconnaissance vocale. Autorisez-le aussi, pour que le texte puisse suivre votre voix.

L'app signale les nouvelles versions par le badge UPDATE dans la barre d'en-tête.

### 1.4 Licence et période d'essai

Au premier lancement s'ouvre la fenêtre « voyzSESSION PRO - Licence ». Vous pouvez tester l'app pendant 7 jours. Un badge dans la barre d'en-tête indique les jours restants.

Pour activer la licence :

1.  Collez la clé de licence reçue par e-mail dans le champ ou faites glisser le fichier `license.lic` sur la fenêtre. Vous pouvez aussi cliquer sur le lien d'activation dans l'e-mail.
2.  Cliquez sur **Activer**.

**Acheter une licence** mène à la boutique. Pour un abonnement, le bouton s'appelle **Gérer l'abonnement**. Le badge de licence de la barre d'en-tête rouvre la fenêtre à tout moment.

À la fin de la période d'essai, l'app continue de fonctionner de manière limitée et émet chaque minute un bref signal de rappel. Lorsqu'un abonnement a expiré, l'export est bloqué.

## 2 L'interface

La fenêtre principale se compose de trois zones fixes : en haut la barre d'en-tête, au milieu la page de travail (**VIDÉO**, **AUDIO** ou **EDIT**) et en bas la barre de transport avec les boutons de lecture et d'enregistrement. Entre la page de travail et la barre de transport, la barre de navigation peut être affichée.

### 2.1 Barre d'en-tête

Les éléments de gauche à droite :

| Élément                   | Fonction                                                                                                                               |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| FICHIER                   | Nouveau projet, Ouvrir, Récents, Enregistrer, Enregistrer sous, Modèles ([chapitre 15](#k15))                                          |
| PROJET...                 | Réglages du projet : fréquence d'échantillonnage, fréquence d'images, timecode de départ, profil, style de mixage                      |
| VIDÉO, AUDIO, EDIT, MIXER | Changement de page de travail ([section 2.2](#k2-2))                                                                                   |
| MEDIA                     | Afficher ou masquer le chutier                                                                                                         |
| OUVRIR VIDÉO              | Ouvrir une vidéo. Lorsqu'une vidéo est chargée, un x apparaît à côté pour la retirer. Le retrait peut être annulé.                    |
| IMAGE                     | Fenêtre vidéo activée ou désactivée (Cmd+9). Par clic droit, vous placez l'image sur un écran externe ou affichez le timecode.        |
| LEVEL                     | Contrôle de niveau du micro                                                                                                            |
| A/V...                    | Réglages audio et vidéo (interface, entrée et sortie)                                                                                  |

Vous ouvrez le manuel via le menu de l'app : voyzSESSION PRO \> Manuel (Cmd+Shift+/). Il est intégré à l'app et fonctionne sans connexion Internet.

Pendant la période d'essai, un badge portant la mention ESSAI indique les jours restants. Lorsqu'une nouvelle version existe, un badge UPDATE apparaît et mène à la page de téléchargement.

### 2.2 Pages de travail

| Page  | Usage                                            | Contenu                                                                                               |
|-------|--------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| VIDÉO | Enregistrement sur image                         | Vidéo et prompteur avec le texte à dire                                                               |
| AUDIO | Projets purement audio, par exemple des podcasts | Script Editor avec la transcription des enregistrements                                               |
| EDIT  | Montage et arrangement                           | Timeline multipiste                                                                                   |
| MIXER | Mixage                                           | La console de mixage se superpose à la page en cours. Un clic sur une autre page la ferme.            |

### 2.3 Barre de transport

- **À gauche :** Annuler et Rétablir, un interrupteur à bascule pour le zoom de l'axe temporel et un autre pour la hauteur des pistes.
- **Au centre :** \|\<\< (au début), retour rapide, **PLAY/STOP**, **REC**, **LOOP**, avance rapide, \>\>\| (à la fin). Une brève pression sur une touche de défilement saute d'1 seconde, un appui maintenu fait défiler à vitesse croissante jusqu'à 32 fois la vitesse normale.
- **Compteur de position :** affiche la position actuelle, en rouge pendant l'enregistrement, en vert pendant la lecture. Après un clic, vous pouvez saisir une position. Par clic droit, vous choisissez l'affichage en timecode, en minutes:secondes ou en samples.
- **Groupe d'enregistrement :** **V-PUNCH** (punch par reconnaissance vocale), **PRE** (pre-roll avant l'enregistrement, 0 à 10 secondes) et **POST** (post-roll après le punch-out).
- **À droite :** le sélecteur **ASSIST \| MANUAL**, la touche du style de mixage (elle affiche le style actif, par exemple **REPORTAGE** ou **TRAILER**, [section 7.1](#k7-1)), le bouton **AUTO MIX** (uniquement en mode Assist) et **EXPORT**.

Sous les boutons se trouve une ligne d'information dans laquelle l'app indique l'opération en cours, par exemple « Rendu du mix... ». Les messages de réussite s'affichent en vert. Si **AUTO MIX** s'allume en bleu, le mix enregistré ne correspond plus au projet et doit être recalculé.

### 2.4 Barre de navigation

Vous affichez et masquez la barre de navigation via Fenêtre \> Barre de navigation. Elle représente tout le projet par sa forme d'onde. Un clic saute à l'endroit choisi. Sur la page **EDIT**, un cadre marque la partie visible, que vous pouvez déplacer avec la souris.

À gauche, vous saisissez **START**, **FIN** et **DURÉE** de la zone. À droite se trouvent les boutons des marqueurs : **MK +** pose un marqueur, les boutons **MK** avec flèche sautent au marqueur précédent ou suivant, **MARKER** affiche la liste de tous les marqueurs. Un projet peut contenir jusqu'à 999 marqueurs.

### 2.5 Barre des menus

| Menu            | Commande                                                                                                             | Raccourci   |
|-----------------|----------------------------------------------------------------------------------------------------------------------|-------------|
| voyzSESSION PRO | À propos de voyzSESSION PRO..., Stream Deck : installer le plug-in..., Stream Deck : charger une disposition, Quitter | Cmd+Q       |
| voyzSESSION PRO | Manuel | Cmd+Shift+/ |
| Fichier | Importer un AAF... ([section 3.5](#k3-5)) | |
| Réglages        | Général...                                                                                                           | Cmd+,       |
| Réglages        | Audio/vidéo...                                                                                                       |             |
| Réglages        | Fondu enchaîné au chevauchement (activé/désactivé)                                                                   |             |
| Fenêtre         | Fenêtre cabine                                                                                                       | Cmd+Shift+B |
| Fenêtre         | Chapitres                                                                                                            | Cmd+Shift+K |
| Fenêtre         | Fenêtre vidéo                                                                                                        | Cmd+9       |
| Fenêtre         | Barre de navigation (activée/désactivée)                                                                             |             |

Nouveau projet, Ouvrir, Enregistrer et Modèles se trouvent dans le bouton **FICHIER** de la barre d'en-tête, pas dans le menu Fichier.

## 3 Premiers pas

Ce chapitre vous mène du projet vide au premier enregistrement.

### 3.1 Créer et enregistrer un projet

1.  Choisissez **FICHIER** \> **Nouveau projet vide**. Un nouveau projet contient déjà une piste voix.
2.  Enregistrez aussitôt le projet avec **FICHIER** \> **Enregistrer...** (Cmd+S), de préférence sur un SSD disposant d'assez d'espace.

L'app écrit les enregistrements directement dans le dossier du projet. Pour un projet pas encore enregistré, la première pression sur **REC** affiche le message « Recording needs a project folder ».

Si vous travaillez souvent avec la même répartition des pistes, créez les nouveaux projets via **FICHIER** \> **Nouveau depuis un modèle** ([chapitre 15](#k15)).

### 3.2 Configurer le périphérique audio

1.  Dans la barre d'en-tête, cliquez sur **A/V...**.
2.  Sous **OUTPUT**, choisissez votre sortie casque ou votre interface, et sous **INPUT** votre micro.
3.  Si vous vous écoutez directement via l'interface (Direct Monitor sur l'appareil), laissez **Direct hardware monitoring** activé. Sans cette possibilité, désactivez l'option. Vous vous entendez alors via le logiciel.

Enregistrez toujours au casque. Lors d'une lecture sur haut-parleurs, le son de la vidéo entre dans le micro.

### 3.3 Régler le niveau du micro (Contrôle de niveau)

Vous ouvrez le contrôle de niveau via **LEVEL** dans la barre d'en-tête. Par défaut, il n'apparaît pas de lui-même au lancement.

1.  Choisissez le micro en haut.
2.  Dites quelques phrases au volume auquel vous enregistrerez ensuite.
3.  Réglez le préampli (gain) de l'interface de sorte que l'affichage indique « Niveau optimal ».

| Affichage      | Niveau crête         | Action                                                              |
|----------------|----------------------|---------------------------------------------------------------------|
| Aucun signal   | sous -50 dBFS        | Vérifier le câble, le choix du micro et l'alimentation fantôme      |
| Trop faible    | sous -18 dBFS        | Augmenter le gain de l'interface                                    |
| Niveau optimal | -18 à -3 dBFS        | Conserver le réglage                                                |
| Trop fort      | au-dessus de -3 dBFS | Réduire le gain, sinon l'enregistrement sature                      |

Dans la même fenêtre, vous choisissez le profil de format, c'est-à-dire la norme pour laquelle vous livrez, par exemple EBU/ARD-ZDF ou Podcast. La case « Ne plus afficher au prochain lancement » est cochée par défaut. Si le contrôle de niveau doit apparaître à chaque lancement, décochez la case ou activez-le sous Réglages \> Général.

### 3.4 Charger une vidéo

1.  Cliquez sur **OUVRIR VIDÉO** ou faites glisser le fichier dans la fenêtre.
2.  Les formats MP4, MOV, M4V et MXF sont pris en charge. WebM ne l'est pas.
3.  Pour un MXF, l'app crée d'abord une copie de lecture (proxy). Une barre de progression indique l'opération. À l'ouverture suivante, la copie est réutilisée.

Si la vidéo comporte plus de deux pistes audio, ce qui est fréquent avec le MXF, la fenêtre « Quelles pistes audio voulez-vous ? » apparaît :

- Cochez chaque piste nécessaire. Par défaut, aucune piste n'est sélectionnée.
- Avec l'accolade à côté d'une paire (1+2, 3+4, etc.), vous créez deux pistes mono sous la forme d'une seule piste stéréo.
- **Choisissez le rôle de chaque ligne :** Auto, Prémix IT, Voix, Dialogue, Musique, Atmo, Stade ou Effets. Le rôle pilote ensuite l'AUTO MIX ([chapitre 7](#k7)).
- **Importer** applique la sélection. Si vous fermez la fenêtre à la place, l'import entier est annulé.

Les vidéos comportant une ou deux pistes audio sont reprises sans question avec le rôle Auto.

**Avec un modèle de session :** si le projet contient des pistes de playout vides issues d'un modèle ([section 15.4](#k15-4)), le son de la vidéo arrive sur ces pistes. La fenêtre est alors préremplie, les cases et les rôles sont réglés comme dans le modèle. Une remarque indique combien de pistes vont sur les pistes existantes du modèle. Vous confirmez avec **Importer**, pour voir un nombre de pistes différent dans le nouveau matériel avant qu'il ne s'applique. Pour les vidéos comportant une ou deux pistes audio, l'app attribue les pistes sans question. Le préremplissage n'a lieu que si le numéro de piste et le format (mono ou stéréo) correspondent au modèle. Sinon, de nouvelles pistes sont créées comme auparavant.

Vous reprenez une séquence du montage vidéo via un fichier AAF ([section 3.5](#k3-5)).

### 3.5 Importer une séquence du montage (AAF)

Avec Fichier \> **Importer un AAF...**, vous ajoutez au projet ouvert les pistes audio d'une séquence du montage vidéo, par exemple depuis Avid Media Composer, Adobe Premiere Pro ou DaVinci Resolve. Les pistes sont ajoutées, et chaque clip se place à sa position de timecode.

1.  Choisir Fichier \> **Importer un AAF...** et ouvrir le fichier AAF.
2.  Dans la fenêtre « Importer un AAF », décider si **Reprendre les niveaux de clip du montage** s'applique. Par défaut, l'interrupteur est désactivé : le volume des clips et les keyframes de niveau du montage sont ignorés, et l'AUTO MIX travaille avec le matériel brut. Activés, ils agissent en plus du réglage de niveau de l'AUTO MIX, sous forme de ligne de clip gain sur le take.
3.  Cliquer sur **Importer**. L'app lit la séquence et décode les médias. Une barre de progression indique l'opération.
4.  Si des fichiers média ne se trouvent pas au chemin indiqué dans l'AAF, le message « Fichiers média introuvables » apparaît. Avec **Choisir un dossier...**, l'app les cherche dans un dossier et ses sous-dossiers. Avec **Importer sans eux**, les clips concernés manquent.
5.  Vérifier les rôles (voir ci-dessous) et confirmer.

Les médias peuvent être intégrés à l'AAF ou liés sous forme de fichiers séparés, y compris en MXF OP-Atom issu d'Avid. Sont repris : les clips, les noms de clips, les fondus, le pan des pistes et l'automation de pan. Les paires mono qui forment une piste stéréo dans le montage sont combinées en pistes stéréo. Dans un projet vide, l'app reprend le timecode de départ de la séquence. Si le projet contient déjà du matériel, les clips sont placés d'après le timecode du projet.

**Rôles :** pour que l'AUTO MIX traite correctement les pistes, chaque piste reçoit un rôle ([section 7.1](#k7-1)).

- **D'après les noms de piste :** si une piste mono s'appelle par exemple « Voice », « Voiceover », « Narrator », « Sprecher » ou « Kommentar », elle devient une piste voix. Des noms comme « Music », « Musik », « Atmo » ou « FX » donnent le rôle correspondant.
- **D'après le contenu :** pour les pistes dont le nom n'indique pas de rôle, l'app écoute le son et propose un rôle dans la fenêtre « Rôles d'après le contenu » : son direct, musique, effets ou ambiance. La parole est toujours proposée comme son direct, car la piste voix du commentaire n'est en général créée qu'ensuite, lors de l'enregistrement. Vérifiez les propositions et modifiez-les si nécessaire. **Sans rôles du contenu** importe ces pistes sans rôle.
- **Clips sans parole sur des pistes de parole :** si un clip sans parole, par exemple un bruit ou un son d'ambiance, se trouve sur une piste son direct ou voix, l'AUTO MIX en réglerait le niveau comme de la parole. L'app liste ces clips. Les clips cochés vont sur une piste propre avec le rôle adapté. **Laisser les clips sur leurs pistes** reprend tout sans modification.

Après l'import, un rapport résume ce qui a été repris et ce qui ne l'a pas été. Ne sont notamment pas repris : les effets de clip et de piste, les déformations temporelles (les clips sont lus à leur vitesse d'origine), le pan sur des clips individuels et les formes de fondu particulières, remplacées par la forme standard. Pour les clips de plus de deux canaux, les canaux 1 et 2 sont repris. L'import n'est pas possible pendant un enregistrement ou une sauvegarde.

### 3.6 Premier enregistrement

1.  Dans l'en-tête de la piste voix, cliquez sur **R** pour armer la piste. La touche s'allume en rouge.
2.  Appuyez sur **REC** ou sur la touche R. Après le pre-roll (**PRE**, 4 secondes par défaut), l'enregistrement commence.
3.  Terminez l'enregistrement avec **STOP REC** ou à nouveau avec la touche R.
4.  La barre d'espace lit l'enregistrement.

Le [chapitre 4](#k4) décrit l'enregistrement en détail, le [chapitre 7](#k7) le mixage automatique et le [chapitre 12](#k12) l'export.

## 4 Enregistrer

L'enregistrement se fait sur chaque piste armée. Plusieurs pistes peuvent être armées en même temps, et chacune d'elles est audible, comme dans les autres DAW.

### 4.1 En-tête de piste

| Touche  | Nom                           | Fonction                                                                                                                                         |
|---------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| R       | Armer                         | REC enregistre sur cette piste. Alt+clic agit sur toutes les pistes.                                                                             |
| I       | Écouter l'entrée (INPUT ONLY) | Activé : l'entrée est toujours audible, aussi pendant la lecture et sans R. Désactivé (Auto Input) : sur une piste armée, l'entrée n'est audible qu'à l'arrêt et pendant l'enregistrement. L'enregistrement n'a lieu qu'avec R. |
| M       | Muet                          | Rendre la piste muette                                                                                                                           |
| S       | Solo                          | N'écouter que cette piste                                                                                                                        |
| AC      | AutoCut                       | Coupe automatiquement le prochain enregistrement aux pauses                                                                                      |
| IMPORT  | Import                        | Charger un fichier audio sur cette piste                                                                                                         |
| Entrée  | Choix de l'entrée             | Entrée de l'interface envoyée sur la piste                                                                                                       |

La touche I n'apparaît que sur les pistes voix, et seulement lorsque le monitoring matériel est désactivé.

Avec **+ Voice**, vous créez une nouvelle piste voix (mono), avec **+ Audio** une piste de playout (stéréo) pour la musique, l'ambiance, etc.

Par clic droit sur l'en-tête de piste ou via la roue dentée, vous accédez à d'autres commandes : Renommer, Monter/Descendre, Voix de référence, combiner en stéréo ou séparer, Affichage et Supprimer la piste. Vous pouvez aussi déplacer les pistes en faisant glisser leur en-tête. Avec Cmd-clic ou Shift-clic, vous sélectionnez plusieurs pistes. La dernière piste voix ne peut pas être supprimée. Vous changez la couleur d'une piste dans la console de mixage par double-clic sur le nom de la piste.

### 4.2 Pre-roll et post-roll

- **PRE** (pre-roll) détermine combien de temps la vidéo démarre avant le point d'enregistrement. Les valeurs vont de 0 à 10 secondes, le réglage par défaut est de 4 secondes. Un double-clic sur le nombre permet de saisir une valeur.
- **POST** (post-roll) détermine combien de temps la lecture continue après la fin d'un enregistrement dans la zone.
- Pendant le pre-roll, le bouton décompte (par exemple « **PRE** 3.2s »), puis il affiche **STOP REC**. Une nouvelle pression interrompt l'enregistrement.
- **REC pendant la lecture** enregistre immédiatement à la position de lecture, sans saut ni pre-roll (punch-in en cours de lecture). Le pre-roll ne s'applique qu'au démarrage depuis l'arrêt.
- Si vous enregistrez par-dessus un take existant, le nouvel enregistrement remplace la partie chevauchée. Ce qui se trouve avant et après est conservé.

### 4.3 Zone, boucle et punch

En haut de la règle se trouve une bande destinée à une zone. Cette zone vaut à la fois pour la boucle et pour l'enregistrement dans la zone.

- **Créer une zone :** faites glisser dans la bande vide. Faire glisser un bord modifie la longueur, faire glisser au milieu déplace la zone, un double-clic la supprime. Le début, la fin et la durée peuvent aussi être saisis dans la barre de navigation.
- **LOOP** ou la touche L répète la zone. Si aucune zone n'est définie, l'app utilise la partie visible.
- **Enregistrer seulement dans la zone (punch) :** un clic droit sur **REC** bascule entre « enregistrement jusqu'à STOP » et « Enregistrer dans la zone ». Dans le second cas, la zone s'affiche en orange, et l'enregistrement commence et se termine exactement à ses bords. Si vous appuyez sur REC pendant la lecture avant la zone, l'enregistrement attend son début. Jusque-là, le bouton affiche le temps d'attente (par exemple « **PUNCH** 2.5s »). À l'intérieur de la zone, l'enregistrement commence immédiatement. Si la position de lecture se trouve après la zone ou juste avant sa fin, la lecture s'arrête, et l'enregistrement démarre comme depuis l'arrêt, avec pre-roll.

### 4.4 Voice Punch

Avec **V-PUNCH**, vous définissez par la voix le point d'entrée après une erreur de lecture :

1.  Appuyez sur **V-PUNCH**.
2.  Dites les derniers mots corrects avant l'erreur.
3.  L'app recherche cet endroit, place le point d'entrée dans la pause qui suit, lit le pre-roll et lance l'enregistrement. À partir de là, vous reprenez votre texte.

Avec Shift+clic sur **V-PUNCH**, vous dites en plus les premiers mots après l'erreur. Seule la partie erronée est alors remplacée, et l'original continue ensuite.

Conditions : le projet est enregistré, la page **VIDÉO** est ouverte, le transport est à l'arrêt, une piste voix est armée, la reconnaissance vocale de macOS est autorisée et le take est déjà transcrit.

### 4.5 Marqueurs

| Commande                     | Fonction                                       |
|------------------------------|------------------------------------------------|
| Alt+M ou MK +                | Poser un marqueur à la position de lecture     |
| 1 à 9                        | Poser un marqueur à l'emplacement 1 à 9        |
| Shift+1 à 9                  | Aller au marqueur 1 à 9                        |
| Alt+virgule, Alt+point       | Au marqueur précédent ou suivant               |
| Faire glisser le fanion      | Déplacer le marqueur                           |
| Clic sur le libellé          | Nommer le marqueur                             |
| Double-clic sur le fanion    | Supprimer le marqueur (peut être annulé)       |

## 5 Prompteur, Script Editor et fenêtre cabine

Le prompteur affiche le texte à dire pendant l'enregistrement et suit la voix. Le Script Editor affiche sous forme de texte ce qui a été dit. Vous pouvez y couper l'audio en sélectionnant des mots et en les supprimant.

### 5.1 Prompteur (page VIDÉO)

Avec **CHARGER SCRIPT**, vous ouvrez un fichier texte au format .txt, .rtf ou .pdf (PDF uniquement avec couche texte). Vous pouvez aussi faire glisser le fichier dans la fenêtre ou coller le texte avec Cmd+V.

Pendant que vous parlez, la reconnaissance vocale de macOS écoute et fait suivre la ligne en cours. Si vous faites défiler avec la molette de la souris, le suivi s'interrompt pendant 8 secondes. Si le prompteur ne peut pas suivre la voix, par exemple parce que la fonction de dictée manque, il affiche une remarque.

| Commande                              | Fonction                                                                                                  |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------|
| LANG                                  | Langue de la reconnaissance vocale, indépendante de la langue de l'app                                   |
| EDIT / DONE                           | Modifier le texte directement. La reconnaissance vocale est suspendue pendant ce temps.                  |
| A- / A+, Cmd+Moins / Cmd+Plus / Cmd+0 | Taille du texte                                                                                           |
| Touches fléchées                      | Un mot en avant ou en arrière                                                                             |
| Page haut, Page bas                   | 20 mots en avant ou en arrière                                                                            |
| Début                                 | Au début du texte                                                                                         |
| Clic sur un mot                       | Le mot devient la ligne en cours. Si le texte est lié à un enregistrement, la timeline saute aussi.      |
| FROM TAKE                             | Crée un texte de prompteur à partir de la transcription d'un enregistrement                               |

### 5.2 Script Editor (page AUDIO)

Le Script Editor affiche la transcription de toutes les pistes voix, chaque piste dans sa couleur. La transcription s'effectue sur le Mac lui-même et démarre automatiquement après un enregistrement, un import ou le chargement d'un projet. Les pistes de playout ne sont pas transcrites.

- **Transcrire** apparaît tant qu'aucun texte n'existe. Si le texte ne manque que pour certains takes, le bouton s'appelle **Transcrire les manquants**.
- Un clic sur un mot place la tête de lecture dans la pause qui le précède.
- **Couper l'audio :** sélectionnez des mots en faisant glisser et appuyez sur Suppr. L'app retire l'audio, place les coupes dans les pauses les plus proches et referme le trou. L'opération peut être annulée en une seule étape.
- **Corriger un mot :** double-cliquez sur le mot, modifiez le texte, appuyez sur Retour. Seul le texte change, pas l'audio.
- **Retirer les hésitations** recherche les mots de remplissage comme « euh », **Recherche de texte** trouve des passages dans la transcription.
- **TEXT EXPORT** enregistre la transcription ou des sous-titres (SRT, VTT, TXT, JSON).

Les temps des mots servent de repère. Pour des coupes très précises, écoutez le résultat.

### 5.3 Fenêtre cabine

La fenêtre cabine (Fenêtre \> Fenêtre cabine, Cmd+Shift+B) est destinée à un moniteur placé dans la cabine et raccordé en HDMI. Elle affiche à gauche le prompteur et à droite l'image avec le timecode. Pendant l'enregistrement, un cadre rouge apparaît. Pendant le pre-roll, le timecode passe au rouge. Le prompteur de la fenêtre cabine défile en synchronisation avec celui de la fenêtre principale. Si un second écran est raccordé, la fenêtre s'y ouvre en plein écran.

## 6 Montage dans la timeline

La page **EDIT** affiche toutes les pistes dans une timeline. C'est ici que vous coupez et déplacez les takes et que vous leur appliquez des fondus.

### 6.1 Modifier les takes

La moitié supérieure et la moitié inférieure d'un take réagissent différemment :

| Zone                          | Le glisser provoque                               |
|-------------------------------|---------------------------------------------------|
| Moitié inférieure             | Déplacer le take                                  |
| Moitié supérieure             | Marquer une zone de sélection jaune dans le take  |
| Bord gauche ou droit          | Raccourcir ou allonger le take (trim)             |
| Poignée de fondu dans le coin | Régler un fondu d'entrée ou de sortie             |

- Cmd+clic ajoute des takes à la sélection, Cmd+A sélectionne tous les takes.
- Avec la touche Control ou Shift enfoncée, un take que vous faites glisser change seulement de piste, sa position temporelle reste inchangée. La règle affiche alors « TEMPS VERROUILLÉ ».
- Avec la touche Alt enfoncée, le glissement ne s'aimante pas.
- Cmd+flèche haut ou bas déplace le take sur la piste voisine, avec Shift une copie est créée.
- Flèche gauche ou droite déplace la sélection d'une image, avec Shift d'une seconde.

### 6.2 Couper, supprimer, copier

| Commande                                                     | Raccourci                |
|--------------------------------------------------------------|--------------------------|
| Scinder à la tête de lecture ou retirer la zone sélectionnée | Cmd+E                    |
| Supprimer                                                    | Suppr ou retour arrière  |
| Copier, coller à la tête de lecture                          | Cmd+C, Cmd+V             |
| Dupliquer                                                    | Cmd+D                    |
| Rendre le take muet                                          | M                        |
| AutoCut (retirer les silences)                               | S                        |
| Annuler, rétablir                                            | Cmd+Z, Cmd+Shift+Z       |

Les morceaux scindés reçoivent des noms numérotés, par exemple « Take 3-01 » et « Take 3-02 ». Le clic droit sur un take propose entre autres : Renommer, Replace audio..., Retirer la sélection, Ne garder que la sélection, Armer l'étirement (tirez ensuite sur le bord pour étirer le take dans le temps), Fade / Crossfade et Réinitialiser la correction de clip gain. Un clic droit sur un emplacement vide propose « Insérer de l'audio ici... ».

### 6.3 Fondus et fondus enchaînés

- **Touche F :** marquez une zone au début ou à la fin d'un take et appuyez sur F. Un fondu est créé. Si la sélection recouvre la limite entre deux takes, un fondu enchaîné est créé.
- **Chevauchement :** si vous faites glisser un take sur un autre, un fondu enchaîné se crée automatiquement sur le chevauchement. Si le take se trouve entièrement à l'intérieur d'un autre take, les deux bords reçoivent un fondu enchaîné de 50 ms. Vous désactivez cette fonction sous Réglages \> Fondu enchaîné au chevauchement. Le take déplacé écrase alors celui qui se trouve dessous.
- Vous modifiez la longueur d'un fondu enchaîné en faisant glisser les bords de la case du fondu enchaîné.

### 6.4 Clip gain

En bas à gauche de chaque take se trouve un petit réglage. Le faire glisser vers le haut ou vers le bas rend tout le take plus fort ou plus faible, avec Shift par petits pas. Un double-clic réinitialise la correction.

Sur la ligne de clip gain du take, vous posez des points par clic, les faites glisser au niveau voulu et les supprimez par double-clic. Vous pouvez ainsi rendre certains mots plus forts ou plus faibles. La ligne de l'AUTO MIX et votre propre correction se superposent en deux couches.

### 6.5 Zoom et affichage

| Fonction                  | Commande                                                                                 |
|---------------------------|------------------------------------------------------------------------------------------|
| Zoomer l'axe temporel     | Interrupteur à bascule à gauche de la barre de transport, Cmd+= et Cmd+Moins, Cmd+molette |
| Afficher tout le projet   | Touche 0                                                                                 |
| Zoomer sur la sélection   | Touche Z                                                                                 |
| Hauteur des pistes        | Second interrupteur à bascule, Control+Alt+flèche haut/bas, Alt+molette                  |
| Agrandir la forme d'onde  | Cmd+Alt+flèche haut/bas, Shift+Alt+molette                                               |
| Au début, à la fin        | Retour, Fin                                                                              |
| Défiler                   | Virgule, point (1 seconde chacun)                                                        |

### 6.6 Chutier

**MEDIA** dans la barre d'en-tête ouvre le chutier (liste des clips). Il contient tout le matériel du projet dans les groupes IMPORTÉ, SON VIDÉO, ENREGISTREMENTS et INUTILISÉ.

- **IMPORT** charge des fichiers dans le chutier, mais pas encore sur une piste. Les formats possibles sont WAV, BWF, AIFF, FLAC, OGG, MP3, M4A, AAC et CAF. Les fichiers importés conservent leur nom d'origine.
- **Pré-écoute :** laissez brièvement le pointeur sur une ligne ou utilisez les touches fléchées. La barre d'espace lance et arrête la lecture, Esc la termine.
- **Placer :** un double-clic place le fichier à la position de lecture sur la piste sélectionnée. Vous pouvez aussi faire glisser le fichier dans la timeline.
- Les régions figurent en retrait sous leur fichier. Un clic montre la région dans la timeline, et en la faisant glisser, seule cette région est déposée.
- **Par clic droit :** Importer sur la piste sélectionnée, Afficher dans le Finder, Retirer de la liste des clips, Retirer l'inutilisé...

Sans le chutier, vous pouvez aussi procéder ainsi : sélectionnez une piste et appuyez sur la touche I. Le fichier choisi est inséré à la position de lecture.

## 7 Mode Assist et AUTO MIX

En mode Assist, l'app se charge du mixage. **AUTO MIX** (ou Cmd+M) traite la voix, abaisse la musique et l'ambiance sous la parole et amène le mix à la loudness du profil choisi. Après le lancement, le mode Assist est actif.

### 7.1 Préparation : profil, style de mixage et rôles

Sous **PROJET...** \> Profil de format, vous définissez la norme pour laquelle vous livrez. Le profil détermine uniquement la livraison : la loudness cible, la crête maximale admise (True Peak) et la normalisation. La sonorité du mix est déterminée par le style de mixage (voir ci-dessous).

| Groupe    | Profil                  | Loudness                 | True Peak          |
|-----------|-------------------------|--------------------------|--------------------|
| TV/Radio  | EBU/ARD-ZDF             | -23 LUFS                 | -1 dBTP            |
| TV/Radio  | ATSC A/85 (États-Unis)  | -24 LUFS                 | -2 dBTP            |
| TV/Radio  | ARIB TR-B32 (Japon)     | -24 LUFS                 | -1 dBTP            |
| TV/Radio  | OP-59 (Australie)       | -24 LUFS                 | -2 dBTP            |
| TV/Radio  | CST-RT-040 (France)     | -23 LUFS                 | -3 dBTP            |
| Streaming | Podcast                 | -16 LUFS                 | -1 dBTP            |
| Streaming | YouTube                 | -14 LUFS                 | -1 dBTP            |
| Autres    | Livre audio             | -18 LUFS                 | -3 dBTP            |
| Autres    | Studio 0 dB             | pas de cible de loudness | crête à 0 dBTP     |

**Style de mixage :** il définit la façon dont l'AUTO MIX pondère les pistes, indépendamment du profil de format. Vous le choisissez avec la touche à côté de **AUTO MIX** dans la barre de transport ou sous **PROJET...** à la ligne **Style de mixage**. Un changement peut être annulé.

| Style de mixage             | Touche de la barre |
|-----------------------------|--------------------|
| Reportage / magazine        | REPORTAGE          |
| Bande-annonce / promo       | TRAILER            |
| Documentaire                | DOCU               |
| Sport / commentaire         | SPORT              |
| Podcast / talk              | PODCAST            |
| Livre audio / fiction radio | LIVRE AUDIO        |

Le réglage par défaut est **Reportage / magazine**. Le style de mixage fixe les valeurs de départ, par exemple la distance entre le tapis et la voix. Avec **Bande-annonce / promo**, la musique et les effets mènent, la voix se place plus près au-dessus, et sous la voix, la musique ne cède que dans la plage de fréquences de la voix. Les basses et le bas-médium restent en place.

Les projets enregistrés avec les anciens profils Trailer, Documentaire, Sport, Podcast ou Livre audio s'ouvrent avec le profil de format et le style de mixage correspondants.

Chaque piste a en outre besoin d'un rôle. Il indique à l'automatisme ce qui se trouve sur la piste. Vous choisissez le rôle avec la touche de rôle dans l'en-tête de piste ou dans la console de mixage.

| Rôle               | Abréviation | Niveau par rapport à la voix | Traitement par l'automatisme                                                          |
|--------------------|-------------|------------------------------|---------------------------------------------------------------------------------------|
| Voix               | SPKR        | Niveau de référence          | La voix est traitée et son niveau est égalisé                                         |
| Son direct         | OT          | aussi fort (0 LU)            | Équilibré par rapport à la voix, chaîne vocale propre                                 |
| Musique            | MUS         | 4 LU plus bas                | Abaissée sous la voix et le son direct                                                |
| Effets             | FX          | 4 LU plus bas                | Abaissés                                                                              |
| Ambiance           | ATMO        | 16 LU plus bas               | Abaissée                                                                              |
| Stade              | STAD        | 5 LU plus bas                | Les sauts de niveau sont compensés, mais la piste n'est jamais abaissée               |
| Prémix IT          | PRE         | inchangé                     | Pour un prémix final issu du montage, se comporte comme « Non classé »               |
| Non classé (Auto)  | AUTO        | inchangé                     | Aucun traitement                                                                      |

Les nouvelles pistes ont le rôle Voix. Une piste de playout mono devient une piste voix avec la commande « Voix - en faire une piste voix ».

### 7.2 Lancer l'AUTO MIX

1.  Il faut au moins un enregistrement, et aucun solo ne doit être actif.
2.  Appuyez sur **AUTO MIX** à droite dans la barre de transport ou sur Cmd+M.
3.  Une fenêtre de progression affiche les différentes étapes : préparation, traitement de la voix, compression et niveau, son, tapis et ducking, loudness. Avec **Annuler**, vous interrompez l'opération à tout moment.
4.  Lisez ensuite le mix final avec **PLAY**.

Avant le calcul, l'app règle en mode Assist tous les faders de la console de mixage sur 0 dB. Cette opération peut être annulée. Si des points d'automation propres ont déjà été posés sur des pistes de playout, l'app demande : **Recalculer**, **Conserver le mien** ou **Annuler**.

**AUTO MIX** ne démarre pas pendant un enregistrement (« Pas pendant l'enregistrement. »), avec un solo actif (« Désactivez **SOLO** avant l'AUTO MIX. ») ni en mode Manual. En mode Manual, c'est l'export qui normalise à la place.

### 7.3 Résultat de l'AUTO MIX

Toutes les décisions de l'automatisme peuvent être consultées et modifiées :

- **Ligne de clip gain de la voix :** le volume de la parole est égalisé par une ligne sur le take, dans une plage allant jusqu'à 9 dB vers le haut ou vers le bas. Votre propre correction se superpose en seconde couche.
- **Ducking sous forme d'automation de volume :** l'abaissement de la musique et de l'ambiance sous la parole figure sous forme de courbe dans l'automation de volume de la piste concernée.
- **Valeurs dans la tranche :** l'EQ, le compresseur, le de-esser et les autres modules reçoivent les valeurs calculées. Clic droit sur une touche \> **Afficher...** montre le module verrouillé avec ces valeurs.

La musique, les effets, l'ambiance et le dialogue disposent chacun de leur propre protection des crêtes. Elle n'intervient que si le fichier final dépasserait sinon la limite True Peak du profil. Un impact fort dans la musique n'écrase donc plus tout le tapis.

Si **AUTO MIX** s'allume en bleu, le mix enregistré ne correspond plus au projet, par exemple après un nouvel enregistrement ou une coupe. Appuyez alors de nouveau sur le bouton.

Les projets de la version 1.6 nécessitent un nouvel **AUTO MIX**, car la chaîne de signal a changé dans la version 2.0.

### 7.4 Réglages possibles en mode Assist

- Les faders des pistes peuvent être déplacés. Les faders du groupe voix et du master sont fixes en mode Assist (affichage **FIXED**).
- Les touches de la tranche ne font qu'activer et désactiver les modules. Le réglage des modules est confié à l'automatisme.
- Les slots d'insert pour plug-ins sont visibles, mais ne sont actifs qu'en mode Manual.

Pour mixer vous-même, passez en mode Manual avec **MANUAL**. Le mix de l'AUTO MIX est alors repris intégralement comme point de départ ([chapitre 8](#k8)).

## 8 Mode Manual : console de mixage, tranche, groupes, master

En mode Manual, vous mixez vous-même, comme dans Pro Tools, Logic ou Nuendo. L'app ne modifie aucun fader, l'écoute se fait sans traitement supplémentaire, et l'export écrit dans le fichier exactement ce que vous entendez.

### 8.1 Passer en mode Manual

Cliquez sur **MANUAL** dans la barre de transport. Le changement fonctionne aussi pendant la lecture et se fait en fondu, sans clic.

Déroulement habituel : enregistrer en mode Assist et lancer **AUTO MIX**, puis passer en mode Manual. La tranche, les modules, les lignes de niveau et le ducking sont repris tels qu'ils sonnaient en dernier. Vous corrigez ensuite les passages que vous souhaitez autrement.

| Fonction                      | Assist                                   | Manual                                                        |
|-------------------------------|------------------------------------------|---------------------------------------------------------------|
| Bouton AUTO MIX               | visible                                  | masqué                                                        |
| Touches de la tranche         | activation/désactivation seulement       | activation/désactivation, ouvre le module pour modification   |
| Slots d'insert (plug-ins)     | visibles, inactifs                       | actifs                                                        |
| Automation                    | désactivée (affichage AUTO en gris)      | Read, Touch, Latch, Write, Trim                               |
| Faders groupe voix et master  | fixes (affichage FIXED)                  | libres                                                        |
| Saturate et réverbération     | inaudibles                               | audibles                                                      |
| Normalisation                 | toujours, par l'AUTO MIX                 | uniquement avec la case « Normaliser » de la fenêtre d'export |

Si le mix sature en mode Manual, un limiteur en sortie protège l'ouïe. L'app signale alors que l'export écrêterait. Dans ce cas, baissez le fader master ou cochez la case « Normaliser » lors de l'export.

### 8.2 Console de mixage

Vous ouvrez la console de mixage avec **MIXER** dans la barre d'en-tête. Chaque piste a une tranche comportant les zones suivantes, de haut en bas :

1.  **Touches DSP :** les neuf modules de traitement intégrés ([chapitre 9](#k9))
2.  Entrée
3.  **Inserts :** cinq emplacements pour plug-ins ([chapitre 10](#k10))
4.  **Sends :** cinq emplacements, encore sans fonction dans la version 2.0
5.  **Sortie :** affichage seulement
6.  Mode d'automation ([chapitre 11](#k11))
7.  **Pan :** position dans l'image stéréo
8.  Fader avec indicateur de niveau, plage de moins l'infini à +12 dB. Le fader utilise toute la hauteur libre de la fenêtre.
9.  **S, M et touche d'enregistrement :** solo, mute, armement
10. Rôle et nom

Le menu contextuel de la tranche permet d'afficher ou de masquer certaines zones, par exemple les inserts ou les sends. C'est là aussi que vous combinez deux pistes mono en une piste stéréo ou que vous les séparez de nouveau.

À côté du fader, une barre cyan indique la réduction de gain (gain reduction) du compresseur, avec des repères à 6 et 12 dB.

### 8.3 Touches DSP

Chaque tranche comporte une grille de neuf touches. Dans le sens de la lecture, elle correspond à l'ordre dans le trajet du signal :

|                  |                  |                  |
|------------------|------------------|------------------|
| REPR Réparation  | NR Débruitage    | EQ Égaliseur     |
| TAME Résonance   | DES De-esser     | CMP Compresseur  |
| BRTH De-Breath   | SAT Saturate     | REV Réverbération |

- L'activation ouvre le module, la désactivation le ferme. Si un module est déjà activé, le premier clic ouvre seulement la fenêtre.
- **Changer l'ordre :** EQ, TAME, DES, CMP, BRTH et SAT peuvent être déplacés à un autre emplacement, comme des inserts. Un astérisque bleu indique que l'ordre a été modifié. Clic droit \> Ordre standard le rétablit. REPR et NR sont fixes au début, REV est fixe à la fin. Ces touches portent un petit point.
- Une touche grise portant la mention « Mode Manual uniquement » n'agit qu'en mode Manual.

Les pistes de playout (musique, ambiance, son direct, etc.) ont la même grille, avec deux restrictions. Avec le rôle « Non classé », la plupart des touches sont verrouillées jusqu'au choix d'un rôle. NR et BRTH ne sont pas encore disponibles sur les pistes de playout, et le de-esser n'agit que sur le son direct et la voix.

### 8.4 Groupes : voix et IT

À côté des pistes se trouvent deux tranches de groupe. Le groupe voix réunit toutes les pistes voix, le groupe IT toutes les pistes de playout (la version internationale sans la voix). Les deux groupes disposent d'un fader, de l'automation, d'inserts et d'une grille avec EQ, TAME, CMP et REV, active uniquement en mode Manual. Pendant la lecture, le fader du groupe IT montre comment le ducking travaille.

### 8.5 Master

Le master est la somme qui est exportée.

- Fader master avec automation.
- **PRE-GAIN** (jusqu'à 24 dB vers le haut ou vers le bas) avant le fader. C'est ici que l'AUTO MIX dépose sa correction de niveau, afin que le fader soit sur 0 dB après le passage en mode Manual. Faire glisser modifie la valeur, Shift permet des pas fins, un double-clic la remet à 0.
- **EQ** et **CMP** (compresseur de bus), uniquement en mode Manual.
- **Indicateurs de niveau :** niveau crête gauche et droite ainsi que la loudness en LUFS, en valeurs momentanée, court terme et intégrée. La grande valeur LUFS I s'affiche en vert si elle s'écarte d'au plus 1 LU de la cible, en orange jusqu'à 3 LU et en rouge au-delà.
- **LRA** : la plage de loudness, c'est-à-dire l'ampleur des variations de loudness sur l'ensemble du programme.
- Indicateur **CLIP** : s'allume après une saturation. Un clic sur la tranche le réinitialise.

La tranche dédiée **CUE** alimente le circuit casque (**CASQUE**) et comporte un emplacement d'insert.

## 9 Les modules de traitement

Chacun des neuf modules de traitement a sa propre fenêtre avec des réglages. L'affichage du module repose sur les mêmes valeurs que celles qu'utilisent l'écoute et l'export.

Pour tous les modules :

- La ligne d'état affiche « Valeurs de l'AUTO MIX », « Modifié (diffère de l'**AUTO MIX**) » ou « Pas encore d'AUTO MIX - affiche l'écoute ».
- **Revenir à l'AUTO MIX** rétablit les valeurs de l'automatisme.
- En mode Assist, clic droit \> **Afficher...** ouvre le module verrouillé avec la mention « Réglé par l'**AUTO MIX** ». Le bouton **Modifier en Manual** passe en mode Manual et déverrouille le module.
- **Presets :** presets d'usine classés par catégories, ainsi que « Utilisateur », « Enregistrer le preset... » et « Afficher le dossier des presets ». Les presets personnels se trouvent sous `~/Library/SATK/Presets/`. Les presets ne peuvent être chargés qu'en mode Manual.
- Cmd+Z, Cmd+S et la barre d'espace fonctionnent aussi lorsqu'une fenêtre de module est au premier plan.

### 9.1 REPR : Réparation (De-Click et De-Plosive)

Le De-Click retire les clics et les bruits de bouche, le De-Plosive atténue les plosives sur P et B en dessous de 240 Hz.

[[IMG:repr.png|Le module REPAIR avec De-Click et De-Plosive]]

| Réglage              | Plage       | Réglage par défaut | Fonction                                                    |
|----------------------|-------------|--------------------|-------------------------------------------------------------|
| SENSIBILITÉ          | 0 à 10      | 4                  | Sensibilité de la détection des clics                       |
| DÉCALAGE FRÉQUENCE   | -10 à +10   | 0                  | Décale la détection vers les clics graves ou aigus          |
| ÉLARGISSEMENT CLIC   | 0 à 10 ms   | 4 ms               | Largeur de la zone réparée autour d'un clic                 |

**CLICS SEULS** ne lit que ce qui est retiré. Vous pouvez ainsi vérifier si le module retire trop. Le De-Click travaille sans latence. Les clics situés dans les pauses de parole sont retirés sur toute la bande de fréquences. Le De-Plosive travaille avec des réglages fixes. En mode Assist, REPR est désactivé ; en mode Manual, il peut être activé.

### 9.2 NR : Débruitage

NR retire les bruits de fond réguliers comme les ventilateurs, le ronflement ou le bruit de la pièce. Un réseau neuronal sépare pour cela la voix et le bruit.

[[IMG:nr.png|Le module NR avec le réglage Intensité]]

Le module comporte un seul réglage, **INTENSITÉ** (0 à 100). Un segment de l'anneau active et désactive NR, un double-clic règle la valeur sur 100. Le cercle affiche le spectre mesuré. NR est désactivé par défaut, et l'AUTO MIX ne l'active pas non plus. Dans la version 2.0, NR est disponible sur les pistes voix.

Des valeurs plus élevées retirent davantage de bruit, mais peuvent modifier les sifflantes. Lors du réglage, soyez attentif aux sifflantes.

### 9.3 EQ : Égaliseur

L'EQ modifie le son d'une piste, par exemple pour rendre une voix plus claire ou plus chaude, ou pour atténuer des fréquences qui résonnent.

[[IMG:eq.png|Le module EQ avec analyseur, bandes et réglages dynamiques]]

L'EQ comporte neuf bandes : coupe-bas (passe-haut, 20 Hz à 1 kHz), cloches 1 à 5, plateau aigu, coupe-haut (1 à 20 kHz, désactivé par défaut) et air (8 kHz).

| Réglage               | Plage                                                                   |
|-----------------------|-------------------------------------------------------------------------|
| FREQ                  | Fréquence en Hz                                                         |
| GAIN                  | -18 à +18 dB                                                            |
| Q (largeur de bande)  | Cloches 0,15 à 14, plateaux 0,1 à 10, coupe-bas et coupe-haut 0,3 à 4   |

Les cloches et les plateaux peuvent être rendus dynamiques (**DYN**). La bande réagit alors au niveau et n'abaisse par exemple une fréquence que lorsqu'elle devient trop forte. Réglages : **RANGE** (-24 à +24 dB), **THRESHOLD** (-80 à 0 dB), **ATTACK** (0,1 à 500 ms), **RELEASE** (5 ms à 5 s ou AUTO).

**SOLO** sur la bande (ou Alt+clic sur un point de bande) ne lit que la plage de fréquences de cette bande. Cela fonctionne aussi en mode Assist et n'agit jamais sur l'export. L'analyseur affiche le spectre avant et après l'EQ. Dans le menu **ANALYZER**, vous choisissez **POST**, **PRE**+**POST** ou OFF, ainsi que la résolution, la vitesse, la plage, la pente et le gel de l'affichage.

### 9.4 TAME : Résonance

TAME détecte les sons isolés gênants, tranchants ou résonnants et ne les abaisse qu'au moment où ils apparaissent.

[[IMG:tame.png|Le module TAME (résonance)]]

| Réglage         | Plage           | Fonction                                    |
|-----------------|-----------------|---------------------------------------------|
| SOFT / HARD     |                 | Fonctionnement doux ou énergique            |
| DEPTH           | 0 à 10          | Intensité de l'abaissement                  |
| DETAIL          | 0 à 10          | Finesse de séparation des sons isolés       |
| ATTACK, RELEASE | 0 à 10          | Temps d'attaque et de retour                |
| MIX             | 0 à 100 %       | Part du signal traité                       |
| MAX CUT         | OFF à 24 dB     | Abaissement maximal                         |
| OUT, WET TRIM   | -18 à +18 dB    | Niveau de sortie                            |

Avec jusqu'à huit bandes de sensibilité (cloche, plateau, coupe, tilt et autres), vous déterminez dans quelles plages de fréquences TAME travaille plus précisément. **DELTA** ne lit que ce qui est retiré. Il existe 16 presets d'usine dans les groupes Général, Parole, Mix et Musique.

### 9.5 DES : De-esser

Le de-esser adoucit les sons S, CH et Z trop aigus, sans rendre la voix terne.

[[IMG:deesser.png|Le module DE-ESS]]

| Réglage                 | Plage                        | Fonction                                                              |
|-------------------------|------------------------------|-----------------------------------------------------------------------|
| SINGLE VOCAL / ALLROUND |                              | Voix seule ou matériel mixé                                           |
| WIDE / SPLIT            |                              | Abaisser tout le signal ou seulement la plage de fréquences agressive |
| THRESHOLD               | moins l'infini à 0 dB        | Seuil de déclenchement                                                |
| RANGE                   | 0 à 24 dB                    | Abaissement maximal                                                   |
| LOOKAHEAD               | 0 à 15 ms, activé/désactivé  | Agit déjà juste avant le son S                                        |
| HIGH-PASS, LOW-PASS     | 2 à 20 kHz                   | Plage de fréquences à laquelle le de-esser réagit                     |

**TRIGGER** lit le signal auquel le de-esser réagit, **RETIRÉ** ce qui est retiré. L'AUTO MIX mesure l'acuité de chaque voix et règle le de-esser en conséquence. Il existe huit presets d'usine, par exemple pour les voix d'hommes et de femmes.

### 9.6 CMP : Compresseur

Le compresseur rapproche les passages forts et faibles, pour que la voix sonne régulière et présente. Le module affiche la courbe caractéristique, l'évolution du niveau et la réduction de gain (en cyan).

[[IMG:comp.png|Le module compresseur avec courbe caractéristique et évolution du niveau]]

Il existe trois modes de fonctionnement : **CLEAN** (orienté crête, pour la parole), **SMOOTH** (doux, orienté valeur moyenne) et **BUS** (pour les groupes et le master).

| Réglage          | Plage                                       | Fonction                                                                                                          |
|------------------|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| THRESHOLD        | -60 à 0 dB                                  | Niveau à partir duquel la compression agit                                                                        |
| RATIO            | 1:1 à 100:1                                 | Intensité de la compression                                                                                       |
| KNEE             | 0 à 24 dB                                   | Entrée en action douce ou dure                                                                                    |
| ATTACK           | 0,1 à 250 ms                                | Temps d'attaque                                                                                                   |
| RELEASE          | 5 ms à 2,5 s ou AUTO                        | Temps de retour. En AUTO, il s'adapte aux pauses de parole, et la valeur réglée est alors sans effet.             |
| MAKEUP           | -12 à +24 dB (AUTO seulement en CLEAN)      | Compense la réduction de gain                                                                                     |
| MIX              | 0 à 100 %                                   | Compression parallèle                                                                                             |
| HOLD, RANGE, DRY | 0 à 500 ms, 0 à 60 dB, OFF à +36 dB         | Réglage fin, sans effet en SMOOTH                                                                                 |

Presets d'usine : Parole - broadcast, Parole - douce, Musique - glue de bus, Musique - tapis dense, Ambiance - nappe, Effets - contenir les crêtes. Les groupes et le master ont leurs propres presets. Un preset règle le mode de fonctionnement, Ratio, Knee, les temps et Mix, mais pas Threshold ni Makeup.

### 9.7 BRTH : De-Breath

Le De-Breath abaisse les bruits de respiration entre les phrases, sans modifier la parole. Les respirations sont reconnues à leur son, et pas seulement à leur volume.

[[IMG:debreath.png|Le module DE-BREATH avec vue d'ensemble et loupe]]

| Réglage             | Plage                       | Réglage par défaut |
|---------------------|-----------------------------|--------------------|
| RANGE (abaissement) | 0 à 24 dB                   | 12 dB              |
| Sensibilité         | PRUDENT, NORMAL, COMPLET    | NORMAL             |

En haut, le module affiche toute la piste, en dessous une loupe autour de la tête de lecture avec la forme d'onde avant et après le traitement. Un clic sur une respiration l'exclut du traitement ou l'y réintègre. Avec Alt+glisser, vous marquez une respiration à la main. **BREATHS ONLY** ne lit que les respirations. La ligne d'état indique le nombre de respirations trouvées, posées à la main et incertaines. En mode Assist, le De-Breath est activé par défaut. Il agit à la lecture et à l'export, mais pas pendant l'enregistrement.

### 9.8 SAT : Saturate

Saturate ajoute une saturation au son analogique, semblable à celle d'un tube ou d'une bande magnétique. Le module n'agit qu'en mode Manual et il est désactivé par défaut.

[[IMG:sat.png|Le module SATURATE avec courbe caractéristique et spectre]]

Comme type, vous choisissez **TUBE** ou **TAPE**, chacun combinable avec **WARM**. On obtient ainsi Tube, Tape, Warm Tube et Warm Tape. Réglages : **DRIVE** (0 à 100), **MIX** (0 à 100), **OUTPUT** (-24 à +24 dB). Il existe des presets d'usine comme Clean ainsi que plusieurs variantes Tube et Tape.

### 9.9 REV : Réverbération

La réverbération place une voix dans un espace, de la petite cabine à la grande salle. Elle n'agit qu'en mode Manual et constitue le dernier maillon de la chaîne. À partir de la réverbération, une piste voix devient stéréo, et la queue de réverbération est incluse dans l'export.

[[IMG:rev.png|Le module de réverbération (REVERB)]]

| Réglage      | Plage        | Réglage par défaut | Fonction                                 |
|--------------|--------------|--------------------|------------------------------------------|
| SPACE        | 0,2 à 10 s   | 2,5 s              | Temps de réverbération, taille de l'espace |
| DECAY RATE   | 0,5 à 2      | 1                  | Vitesse de décroissance                  |
| DISTANCE     | 0 à 1        | 0,5                | Distance perçue de la voix               |
| BRIGHTNESS   | 0 à 1        | 0,5                | Clair ou sombre                          |
| CHARACTER    | 0 à 1        | 0,3                | Couleur sonore de l'espace               |
| STEREO WIDTH | 0 à 1,2      | 0,7                | Largeur stéréo                           |
| MIX          | 0 à 1        | 0,3                | Part de la réverbération                 |
| PREDELAY     | 0 à 500 ms   | 0                  | Écart entre la voix et la réverbération  |

S'y ajoutent les niveaux d'entrée et de sortie, le pan et deux onglets d'EQ (DECAY EQ et **POST** EQ). Il existe environ 30 presets d'usine dans les groupes Ambience, Small, Medium, Large, Very Large et Voice, par exemple Vocal Booth, Narrator Polish et Radio Studio.

## 10 Plug-ins et slots d'insert

Dans les slots d'insert, vous chargez des plug-ins d'autres fabricants aux formats Audio Unit (AU, y compris AUv3) et VST3. Les instruments ne sont pas proposés. Les plug-ins ne sont actifs qu'en mode Manual. En mode Assist, les slots sont visibles, mais sans effet.

Chaque piste, le groupe voix, le groupe IT et le master disposent chacun de cinq slots, la tranche CUE d'un seul. Les plug-ins travaillent dans l'ordre de haut en bas et viennent après les modules intégrés.

### 10.1 Insérer un plug-in

1.  Cliquez sur un slot vide. La liste de choix s'ouvre, triée par fabricant.
2.  Choisissez le plug-in. La fenêtre du plug-in s'ouvre immédiatement.

### 10.2 Commandes du slot

| Commande                          | Fonction                                                              |
|-----------------------------------|-----------------------------------------------------------------------|
| Clic sur le nom                   | Ouvrir la fenêtre du plug-in                                          |
| Symbole marche/arrêt ou Cmd+clic  | Bypass (contourner le plug-in)                                        |
| x au survol de la souris          | Retirer le plug-in (Cmd+Z le rétablit)                                |
| Clic droit                        | Menu avec Open editor, Bypass, Remove et Rescan plugins...            |

Lorsqu'une fenêtre de plug-in est au premier plan, l'app continue de transmettre au transport la barre d'espace (Play/Stop), la touche R (enregistrement) et la touche Début.

### 10.3 Liste des plug-ins et nouvelle analyse

Au lancement, l'app vérifie les plug-ins installés. Chaque plug-in est testé dans un processus auxiliaire distinct. Si un plug-in plante, il est placé sur une liste de blocage et ne met pas l'app en danger. Après l'installation de nouveaux plug-ins ou la mise à jour d'un plug-in, choisissez **Rescan plugins...** dans le menu du slot. La liste de blocage est alors vidée, et les plug-ins qui n'existent plus disparaissent de la liste.

La latence des plug-ins est compensée automatiquement, y compris sur les groupes et le master.

## 11 Automation

L'automation enregistre les mouvements des réglages et les rejoue à chaque lecture. Un passage peut ainsi devenir automatiquement plus faible et un autre plus fort. L'automation est disponible en mode Manual. En mode Assist, la touche AUTO s'affiche en gris.

### 11.1 Paramètres automatisables

- Volume (fader) sur les pistes, le groupe voix, le groupe IT et le master
- Pan
- Mute
- **Paramètres de plug-in :** chaque réglage d'un plug-in que vous bougez pendant l'écriture de l'automation

La tranche CUE n'a pas d'automation.

### 11.2 Modes d'automation

Vous choisissez le mode avec la touche d'automation de la tranche. Les désignations et le comportement correspondent à ceux des DAW courantes :

| Mode          | Couleur     | Comportement                                                                                                                                 |
|---------------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| READ          | gris        | Lit la courbe. Le fader reste déplaçable, un repère affiche la valeur de l'automation.                                                       |
| TOUCH         | bleu clair  | N'écrit que tant que le réglage est touché. Après le relâchement, il revient en 0,25 seconde à la courbe existante.                          |
| LATCH         | bleu foncé  | Écrit dès le premier contact et maintient la dernière valeur jusqu'à STOP.                                                                   |
| WRITE         | rouge       | Écrit en continu dès PLAY, même sans contact. Après un passage, la piste passe automatiquement en TOUCH.                                     |
| TRIM (option) | jaune       | N'écrit pas de valeurs absolues, mais une correction de la courbe existante, par exemple tout un ducking 2 dB plus bas.                      |

Automation du mute : en **TOUCH**, la touche Mute agit comme un bouton poussoir et coupe le son tant qu'elle est enfoncée. En **WRITE**, l'écriture se fait dès le démarrage, en **LATCH** jusqu'à STOP.

### 11.3 L'automation dans la timeline

Dans l'en-tête de piste, vous basculez l'affichage entre Forme d'onde et Volume. Alt+clic bascule toutes les pistes. Dans l'affichage Volume, vous voyez la courbe et pouvez poser, déplacer et supprimer des points (sélectionner et appuyer sur Suppr). Le ducking de l'AUTO MIX y apparaît aussi sous forme de courbe.

Les modes d'automation sont enregistrés avec le projet.

## 12 Export

Avec **EXPORT** dans la barre de transport, vous créez les fichiers de livraison : le mix final, sur demande la voix sous forme de fichier séparé, la vidéo avec le nouveau son ou un MXF pour la diffusion. Tous les fichiers sont placés dans un dossier de livraison propre, et les fichiers existants ne sont pas écrasés.

### 12.1 Déroulement

1.  En mode Assist, lancer **AUTO MIX** ([chapitre 7](#k7)), en mode Manual, finaliser le mix.
2.  Appuyer sur **EXPORT**. La fenêtre d'export s'ouvre.
3.  Dans le champ **Nom**, saisir un nom pour la livraison. S'il reste vide, le nom du projet est utilisé.
4.  Choisir les fichiers à créer ([sections 12.2](#k12-2) à 12.4).
5.  Cliquer sur **EXPORT** ou appuyer sur Retour. Si **Destination** est réglé sur « Demander à chaque export », choisissez maintenant le dossier de destination. Sinon, l'app écrit directement dans la destination choisie.

**Destination :** dans la ligne **Destination** de la fenêtre d'export, vous choisissez « Demander à chaque export », l'une des dernières destinations utilisées ou **Choisir un dossier...**, par exemple un dossier sur un serveur. La destination est enregistrée dans le projet, et donc aussi dans les modèles de session. Si elle n'est pas accessible lors de l'export, par exemple parce que le lecteur réseau n'est pas connecté, ou si les droits d'écriture manquent, l'export s'interrompt avec un message au lieu d'enregistrer les fichiers à un autre endroit. La fenêtre affiche alors « Destination inaccessible - le serveur est-il connecté ? ».

Dans le dossier de destination, un sous-dossier portant le nom de la livraison est créé. Les fichiers s'appellent par exemple `Beitrag_2026-11-19_v1_mix.wav` et `Beitrag_2026-11-19_v1_voice.wav`. À chaque export suivant, le numéro de version augmente (v2, v3, etc.).

### 12.2 Audio

| Ligne                                            | Contenu                                                                                                       | Réglage par défaut |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------|--------------------|
| Mix audio                                        | Mix final (stéréo)                                                                                            | activé, WAV 24 bits |
| Stem voix                                        | Uniquement la ou les voix, par exemple pour un remixage ultérieur                                             | désactivé          |
| Pistes voix séparées                             | Un fichier par piste voix, sans effets, disponible à partir de deux pistes voix                               | désactivé          |
| Liste de montage pour d'autres DAW (AES31, .adl) | Pour ouvrir le projet dans Pro Tools, Nuendo et d'autres DAW. Le projet doit pour cela être enregistré.      | désactivé          |

Formats disponibles : WAV, AIFF, AAC (.m4a), MP3, MP2 (.mp2), MP2 (.wav), FLAC et Opus.

| Réglage                       | Choix                                            | Restriction                                          |
|-------------------------------|--------------------------------------------------|------------------------------------------------------|
| Fréquence d'échantillonnage   | Projet, 44,1, 48, 88,2 ou 96 kHz                 | MP2 et MP3 48 kHz au maximum, Opus toujours 48 kHz   |
| Résolution (WAV, AIFF, FLAC)  | 16 bits avec dither, 24 bits, 32 bits flottant   | FLAC 24 bits au maximum                              |
| Débit (MP3, AAC, MP2, Opus)   | 128, 192, 256 ou 320 kbit/s                      | 384 kbit/s uniquement en MP2                         |

Les fichiers WAV reçoivent un horodatage selon la norme BWF, calculé à partir du timecode de départ du projet.

### 12.3 Normaliser

La case « Normaliser à -23 LUFS (...) » amène le fichier à la loudness cible du profil et limite les crêtes avec un limiteur True Peak. La valeur indiquée dans le libellé dépend du profil. Avec le profil Studio 0 dB, la normalisation se fait à la place sur un niveau crête de 0 dBTP.

- En mode Assist, l'AUTO MIX normalise déjà. L'export sort le mix final.
- En mode Manual, la normalisation n'a lieu que si la case est cochée. Une ligne de la fenêtre indique alors de combien le fichier s'écarte de votre écoute.
- La case ne vaut que pour l'export en cours.
- Vous pouvez en outre choisir « Limiter la plage de loudness (LRA à 6 LU, multibande) ». Cette option réduit les fortes variations de volume.

### 12.4 Vidéo et MXF

Sous **SORTIES**, choisissez **Vidéo (MOV/MP4)** ou **MXF (diffusion)**. L'option active est celle qui correspond à la vidéo chargée. L'image est reprise telle quelle et le nouveau son y est inséré.

Pour le MXF, il existe des réglages supplémentaires :

- **Profil de livraison :** EBU R128, US ATSC - IT 8, Stereo, DE ARD/ZDF - HDF01a, JP ARIB - RDD9, FR CST - AS-10. Si le profil de format du projet ne correspond pas au profil de livraison, un avertissement rouge apparaît.
- **Nombre de pistes :** 8 ou 16 pistes audio. Les profils de livraison JP ARIB - RDD9 et FR CST - AS-10 n'autorisent que 8 pistes audio. Pour eux, l'app passe à 8 et le signale.
- Préréglage des pistes audio, par exemple « Mix 1+2, voix 7+8 ». Sous « Mes préréglages » figurent vos affectations enregistrées.
- **Affectation des pistes :** pour chaque piste (T1 à T8 ou T16), vous définissez ce qu'elle contient (mix G ou D, voix, muet ou un canal de la source). La désignation d'une piste n'est qu'un nom et ne modifie pas son contenu.

Avec **Enregistrer l'affectation comme préréglage...** dans la liste des préréglages, vous enregistrez l'affectation actuelle sous un nom. Sont enregistrés le nombre de pistes ainsi que le contenu et la désignation de chaque piste.

À côté du MXF, une fiche d'affectation (`<Nom>_tracks.txt`) est créée automatiquement. Elle décrit l'affectation réelle des pistes.

### 12.5 Podcast : chapitres et informations d'épisode

Pour les podcasts, ouvrez la fenêtre Chapitres (Fenêtre \> Chapitres, Cmd+Shift+K) :

1.  Placer la tête de lecture au début du chapitre et cliquer sur **À la tête de lecture**.
2.  Saisir le titre, et en option une image et un lien. Les chapitres sans titre ne sont pas exportés.
3.  Sous **PROJET...** \> ÉPISODE, saisir le titre, l'auteur, l'émission, le commentaire et l'image de couverture. L'image de couverture doit être carrée et mesurer de 1400 à 3000 pixels, les images de chapitre au moins 600 pixels.

Lors de l'export, le mix reçoit des informations ID3 et des chapitres. Un fichier de chapitres `<Nom>-chapters.json` selon la norme Podcasting 2.0 est en outre créé, avec les images de chapitre.

### 12.6 Sous-titres et transcription

Vous exportez les sous-titres dans le Script Editor de la page **AUDIO** avec **TEXT EXPORT**. Les formats proposés sont SubRip (.srt), WebVTT (.vtt), texte brut (.txt) et JSON (Podcast 2.0).

## 13 Enregistrement à distance, caméra virtuelle et cue

Lors d'un enregistrement à distance, le comédien se trouve à un autre endroit et il est connecté via un service de navigateur ou de visioconférence. voyzSESSION PRO apporte pour cela son propre périphérique audio virtuel et une caméra virtuelle. Le comédien voit votre image, entend la vidéo et la régie, et parle directement dans votre piste d'enregistrement.

### 13.1 Configuration unique

1.  **Installer le pilote audio :** Réglages \> Audio/vidéo..., puis sous « Virtual audio device », cliquer sur **Install**. Redémarrer ensuite l'app. Deux périphériques sont créés : voyzSESSION Send (sortie de l'app) et voyzSESSION Return (entrée dans l'app).
2.  **Installer la caméra :** dans le menu de l'app, choisir **Installer la caméra virtuelle...**. L'app doit pour cela se trouver dans le dossier Applications. macOS demande une autorisation sous Réglages Système \> Général \> Ouverture et extensions \> Extensions de caméra. Un redémarrage peut être nécessaire. **État de la caméra virtuelle...** indique si la caméra est active.
3.  Dans les réglages A/V, activer **Virtual camera (video to browsers)**.

Dans la version 2.0, la fenêtre des réglages A/V est encore libellée en anglais, même si l'app est réglée en français.

### 13.2 Mener une session

1.  Dans le service de visioconférence ou de navigateur (par exemple SessionLink PRO, Zoom ou Teams), régler : micro = voyzSESSION Send, haut-parleur = voyzSESSION Return, caméra = voyzSESSION.
2.  Dans voyzSESSION PRO, affecter la piste voix à l'entrée voyzSESSION Return L (ou R).
3.  Dans la console de mixage, sur la tranche **CUE**, mesurer la latence avec **MESSEN**. L'app envoie un signal de test discret au comédien et le recherche dans le retour. Le résultat s'affiche en millisecondes.
4.  Enregistrer comme d'habitude ([chapitre 4](#k4)).
5.  **Après l'enregistrement :** clic droit sur le take \> **Aligner selon la latence de liaison**. Le take est avancé de la latence mesurée et se retrouve ensuite en synchronisation avec l'image.

### 13.3 Cue : ce qu'entend le comédien

Le circuit de cue vers le comédien contient le son de la vidéo et des pistes de playout, les takes déjà enregistrés et les ordres de la régie (talkback). Sa propre voix en direct ne lui est pas renvoyée, pour qu'il ne s'entende pas avec un décalage.

- **TALK** dans la tranche **CUE** active le micro de talkback, uniquement à l'arrêt. Le talkback n'est jamais audible sur vos propres haut-parleurs.
- Le fader de cue règle le volume envoyé au comédien (-48 à +6 dB). L'envoi se fait à -23 LUFS.
- En lecture normale, le retour n'est audible que si la touche I (écouter l'entrée) est active sur la piste. Pendant l'enregistrement, il est toujours audible.

### 13.4 Fenêtre cabine et fenêtre vidéo

Pour un comédien dans votre propre cabine, il existe la fenêtre cabine (Fenêtre \> Fenêtre cabine, Cmd+Shift+B). Elle s'affiche sur un moniteur raccordé en HDMI et est donc sans latence. À gauche se trouve le prompteur, à droite l'image avec le timecode, et pendant l'enregistrement un cadre rouge apparaît. La fenêtre vidéo (Cmd+9 ou **IMAGE**) n'affiche que l'image, sans cadre, sur demande sur un écran externe.

## 14 Commande externe : Stream Deck, surfaces de contrôle, OSC

voyzSESSION PRO peut être piloté avec un Elgato Stream Deck, une surface Mackie Control ou par OSC. C'est utile par exemple lorsqu'un comédien travaille seul dans la cabine.

### 14.1 Stream Deck

1.  Dans le menu de l'app, choisir **Stream Deck : installer le plug-in...**. Le logiciel Elgato reprend le plug-in.
2.  Sous **Stream Deck : charger une disposition**, choisir le modèle adapté : Stream Deck (15 touches), Stream Deck MK.2 (15 touches), Stream Deck Mini (6 touches), Stream Deck XL (32 touches) ou Stream Deck + (boutons rotatifs).
3.  Dans les réglages A/V, activer **OSC remote control**. Le plug-in communique avec l'app via OSC.

Les touches affichent l'état de l'app, par exemple activé/désactivé ou les valeurs actuelles. Les touches de tranche suivent le même ordre que dans la console de mixage et commutent aussi les pistes de playout.

### 14.2 Surface Mackie Control (MCU)

Dans les réglages A/V, sous **MCU FADER CONTROLLER (MIDI)**, choisissez le port MIDI de votre surface. La mention **RECEIVING** indique que des données arrivent de la surface.

| Élément de la surface             | Fonction                                                   |
|-----------------------------------|------------------------------------------------------------|
| 8 faders (sensibles au toucher)   | Volume des pistes, comme le fader à l'écran                |
| V-Pot, V-Pot enfoncé              | Pan, pan au centre                                         |
| REC, SOLO, MUTE, SELECT           | Par canal (REC uniquement sur les pistes voix)             |
| PLAY, STOP, RECORD                | Transport (STOP à l'arrêt revient au début)                |
| CYCLE                             | Boucle                                                     |
| Retour rapide, avance rapide      | Défilement                                                 |
| BANK, CHANNEL                     | Décaler la banque de faders de 8 pistes ou d'une piste     |

Le fader master de la surface pilote le master, et l'affichage du timecode de la surface suit la position.

### 14.3 OSC et affichages dans le navigateur

- **OSC :** l'app reçoit sur le port 8000 et renvoie les états, par défaut à 127.0.0.1:9000 (modifiable sous **OSC REPLY TO**). Par OSC, vous accédez au transport, aux fonctions de piste (Arm, Solo, Mute, mode d'automation), au montage, aux marqueurs, aux affichages, à l'**AUTO MIX**, à la sauvegarde, à l'export et au talkback.
- **Affichages de console dans le navigateur :** activer **Console displays (web)**, copier les adresses avec **COPY URLS** et les ouvrir sur une tablette ou un second ordinateur du même réseau (port 8422, avec une clé d'accès dans l'adresse).

## 15 Réglages, projets, sauvegarde et restauration

### 15.1 Réglages > Général (Cmd+,)

| Ligne                | Fonction                                                                                                                                         |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Langue               | Automatique (langue du système), Deutsch, English, Français, Español, Italiano, Português. La modification prend effet au prochain lancement.   |
| Langue du prompteur  | Langue dans laquelle la reconnaissance vocale suit le texte                                                                                      |
| Contrôle de niveau   | « Contrôle de niveau au lancement » activé ou désactivé. Désactivé par défaut.                                                                    |
| Astuces              | « Réafficher les astuces » affiche de nouveau les remarques qui n'apparaissent qu'une fois                                                       |

Directement dans le menu Réglages se trouve l'interrupteur **Fondu enchaîné au chevauchement** (activé par défaut, voir [chapitre 6](#k6)).

### 15.2 Réglages > Audio/vidéo (bouton A/V...)

- **OUTPUT et INPUT :** périphériques de sortie et d'entrée, sélectionnables indépendamment l'un de l'autre, par exemple un micro USB avec une interface.
- **SAMPLE RATE et BUFFER SIZE :** taille de la mémoire tampon de 32 à 1024 samples. Une petite mémoire tampon réduit la latence au casque, mais augmente la charge de calcul. En dessous figure la latence totale mesurée (Round trip).
- **Direct hardware monitoring :** laisser activé si vous vous écoutez via l'interface (réglage par défaut). L'écoute logicielle est alors muette, pour que vous ne vous entendiez pas deux fois.
- **RECORDING DELAY :** décale les nouveaux takes de quelques samples si l'interface les enregistre avec un décalage.
- **Low latency monitoring :** contourne, sur les pistes écoutées, les plug-ins dont la latence est trop élevée. Ces plug-ins sont signalés en orange. L'export n'est pas concerné.
- **En outre :** surface MCU, périphérique audio virtuel, affichages dans le navigateur, OSC et caméra virtuelle ([chapitre 13](#k13) et 14).

### 15.3 Réglages du projet (bouton PROJET...)

Les modifications prennent effet immédiatement.

- **AUDIO, fréquence d'échantillonnage :** la fréquence d'échantillonnage est déterminée par le projet, pas par l'interface. Pour un projet vide, vous la réglez directement. Si le projet contient déjà du matériel, choisissez **Enregistrer une copie à une autre fréquence d'échantillonnage**. L'app convertit alors une copie, et l'original reste inchangé.
- **TEMPS ET IMAGE :** fréquence d'images (23,976 à 60 fps, y compris drop frame), timecode de départ (choix rapide 00:00:00:00 ou 10:00:00:00) et **Depuis la vidéo**. Si la fréquence d'images de la vidéo diffère, elle s'affiche en rouge.
- **LOUDNESS :** profil de format et style de mixage ([section 7.1](#k7-1)).
- **ÉPISODE :** informations pour les podcasts ([section 12.5](#k12-5)).

### 15.4 Sauvegarde, modèles, restauration

- Enregistrer avec Cmd+S, Enregistrer sous avec Cmd+Shift+S ou via le bouton **FICHIER**. Un projet est un dossier portant l'extension `.satkproj`. Les enregistrements audio sont placés directement dans le sous-dossier `audio` du projet enregistré. Il est donc conseillé d'enregistrer un nouveau projet avant le premier enregistrement audio.
- Un Cmd+S pendant un **AUTO MIX** est mis en attente et exécuté ensuite.
- **Modèles :** **FICHIER** \> **Enregistrer l'actuel comme modèle...** enregistre les pistes, les réglages, les inserts, le profil et le texte du prompteur, mais aucun enregistrement audio, aucune vidéo, aucun chapitre et aucun marqueur. Vous créez ensuite de nouveaux projets avec **FICHIER** \> **Nouveau depuis un modèle**. Dans le modèle, les pistes de playout conservent leur rôle et leur attribution aux pistes audio de la vidéo. Lors du prochain import vidéo, l'app remplit ces pistes ([section 3.4](#k3-4)). La destination d'export est aussi enregistrée dans le modèle.
- **Sauvegarde automatique :** en cas de modifications, l'app enregistre toutes les 30 secondes un état de restauration. Après un plantage, elle demande au lancement suivant si cet état doit être restauré ou rejeté.
- **Enregistrement interrompu :** si un enregistrement en cours a été interrompu par un plantage, l'app affiche à l'ouverture suivante « Enregistrement interrompu trouvé ». **Restaurer** le crée sous forme de take, **Abandonner** place les fichiers dans la corbeille. **Plus tard**, Esc ou la fermeture de la fenêtre les laissent en l'état, et l'app pose de nouveau la question à l'ouverture suivante.
- **Quitter :** en cas de modifications non enregistrées, l'app demande s'il faut enregistrer, rejeter ou annuler. La même question apparaît pour Nouveau et Ouvrir.

## Annexe

### A Raccourcis clavier

Les touches sans Cmd, Alt ou Control n'agissent pas tant qu'un champ de texte est actif.

| Domaine    | Touche                             | Fonction                                                     |
|------------|------------------------------------|--------------------------------------------------------------|
| Transport  | Barre d'espace                     | Lecture, arrêt                                               |
| Transport  | R                                  | Lancer ou terminer l'enregistrement                          |
| Transport  | L                                  | Boucle activée ou désactivée                                 |
| Transport  | Retour, Fin, Début                 | Au début, à la fin, à la position 0                          |
| Transport  | Virgule, point                     | 1 seconde en arrière ou en avant                             |
| Marqueurs  | Alt+M                              | Poser un marqueur                                            |
| Marqueurs  | 1 à 9, Shift+1 à 9                 | Poser un marqueur, aller à un marqueur                       |
| Marqueurs  | Alt+virgule, Alt+point             | Marqueur précédent ou suivant                                |
| Édition    | Cmd+Z, Cmd+Shift+Z                 | Annuler, rétablir                                            |
| Édition    | Cmd+E                              | Scinder                                                      |
| Édition    | Cmd+C, Cmd+V, Cmd+D                | Copier, coller, dupliquer                                    |
| Édition    | Cmd+A                              | Sélectionner tous les takes                                  |
| Édition    | Suppr                              | Supprimer la sélection                                       |
| Édition    | M                                  | Rendre le take muet                                          |
| Édition    | S                                  | AutoCut                                                      |
| Édition    | F                                  | Fondu ou fondu enchaîné                                      |
| Édition    | I                                  | Importer de l'audio à la position de lecture                 |
| Édition    | Cmd+flèche haut/bas                | Déplacer le take sur la piste voisine, le copier avec Shift  |
| Édition    | Flèche gauche/droite               | Déplacer la sélection d'1 image, d'1 seconde avec Shift      |
| Affichage  | Cmd+=, Cmd+Moins                   | Zoom                                                         |
| Affichage  | 0, Z                               | Tout le projet, sélection                                    |
| Affichage  | Control+Alt+flèche haut/bas        | Hauteur des pistes                                           |
| Affichage  | Cmd+Alt+flèche haut/bas            | Hauteur de la forme d'onde                                   |
| Mixage     | Cmd+M                              | AUTO MIX                                                     |
| Projet     | Cmd+S, Cmd+Shift+S                 | Enregistrer, enregistrer sous                                |
| Fenêtre    | Cmd+,                              | Réglages \> Général                                          |
| Fenêtre    | Cmd+9                              | Fenêtre vidéo                                                |
| Fenêtre    | Cmd+Shift+B                        | Fenêtre cabine                                               |
| Fenêtre    | Cmd+Shift+K                        | Chapitres                                                    |
| Prompteur  | Cmd+Plus, Cmd+Moins, Cmd+0         | Taille du texte                                              |
| Aide       | Cmd+Shift+/                        | Manuel                                                       |

### B Glossaire

| Terme                           | Signification                                                                                   |
|---------------------------------|-------------------------------------------------------------------------------------------------|
| AUTO MIX                        | Mixage automatique en mode Assist                                                               |
| Bounce                          | Écrire le mix dans un fichier tel qu'on l'entend                                                |
| Clip gain                       | Volume appliqué directement au take, avant la tranche                                           |
| Fondu enchaîné                  | Transition progressive entre deux takes                                                         |
| Ducking                         | Abaissement automatique de la musique ou de l'ambiance pendant que quelqu'un parle              |
| Fader                           | Curseur de réglage du volume                                                                    |
| Insert                          | Emplacement pour un plug-in dans la tranche                                                     |
| IT (version internationale)     | Tous les éléments sauf la voix : son direct, musique, ambiance, effets                          |
| LUFS, LU                        | Unités de mesure de la loudness perçue. -23 LUFS est la norme de la télévision en Europe.       |
| LRA                             | Plage de loudness, c'est-à-dire l'ampleur des variations de loudness sur l'ensemble du programme |
| Son direct                      | Son d'origine de la vidéo, par exemple une interview                                            |
| Pre-roll, post-roll             | Temps de défilement avant et après un enregistrement                                            |
| Punch                           | Enregistrement limité à une zone définie, pour remplacer un passage                             |
| Rôle                            | Type de contenu d'une piste (voix, musique, etc.), pilote l'automatisme                         |
| Armer                           | Préparer une piste pour l'enregistrement                                                        |
| Stem                            | Élément isolé du mix sous forme de fichier séparé, par exemple la voix seule                    |
| Take, région                    | Morceau d'audio enregistré ou importé sur une piste                                             |
| True Peak (dBTP)                | Valeur crête maximale réelle du signal                                                          |

### C Dépannage

| Problème                                                    | Solution                                                                                                                                                                                       |
|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Le contrôle de niveau affiche « Aucun signal »              | Vérifier le micro dans le contrôle de niveau et sous A/V... \> INPUT. Vérifier aussi que macOS autorise l'accès au micro (Réglages Système \> Confidentialité et sécurité \> Micro).          |
| REC ne lance pas d'enregistrement                           | Une piste doit être armée (R). Sans piste armée, l'app affiche « Aucune piste armée ». Un nouveau projet doit d'abord être enregistré.                                                        |
| Votre propre voix s'entend en double ou avec de l'écho      | La voix arrive en même temps par l'interface et par le logiciel. Sous A/V..., activer Direct hardware monitoring ou désactiver le Direct Monitor de l'interface.                              |
| AUTO MIX ne démarre pas                                     | Désactiver le solo, terminer l'enregistrement en cours, passer en mode Assist. Au moins un take doit exister.                                                                                 |
| AUTO MIX s'allume en bleu                                   | Le mix enregistré ne correspond plus au projet. Relancer AUTO MIX.                                                                                                                             |
| Message indiquant que l'export écrêterait (mode Manual)     | Baisser le fader master ou activer « Normaliser » lors de l'export.                                                                                                                            |
| Un plug-in manque dans la liste                             | Dans le menu du slot, choisir Rescan plugins... Les instruments ne sont jamais proposés.                                                                                                      |
| Un plug-in fait planter l'app                               | Le plug-in est placé sur la liste de blocage au lancement suivant. Après une mise à jour du plug-in, relancer l'analyse.                                                                     |
| Le prompteur ne suit pas la voix                            | Autoriser la reconnaissance vocale dans macOS et activer la dictée. Régler la langue du texte avec LANG.                                                                                      |
| Le Script Editor reste vide                                 | Appuyer sur Transcrire. Les pistes de playout ne sont pas transcrites.                                                                                                                        |
| La caméra virtuelle n'apparaît pas                          | L'app doit se trouver dans le dossier Applications. Autoriser l'extension dans les Réglages Système, redémarrer le Mac si nécessaire et, sous A/V..., activer la caméra.                      |
| voyzSESSION Send ou Return manque                           | Installer le pilote sous A/V... et redémarrer l'app.                                                                                                                                           |
| La fréquence d'images s'affiche en rouge                    | La vidéo et le projet ont des fréquences d'images différentes. Sous PROJET..., choisir « Depuis la vidéo ».                                                                                   |
| L'export s'interrompt : destination inaccessible            | Connecter le lecteur réseau ou choisir un autre dossier sous Destination dans la fenêtre d'export. |
| Import AAF : fichiers média introuvables                    | Cliquer sur **Choisir un dossier...** et indiquer le dossier contenant les médias du montage. L'app cherche aussi dans les sous-dossiers. |
| L'app a planté                                              | Au lancement suivant, choisir la restauration. En cas de modifications, l'app sauvegarde toutes les 30 secondes.                                                                              |
| Mauvaise langue d'interface                                 | Choisir Réglages \> Général \> Langue et redémarrer l'app.                                                                                                                                     |
| La fenêtre des réglages A/V est en anglais                  | Cette fenêtre n'est pas encore traduite dans la version 2.0. Le reste de l'app suit la langue choisie.                                                                                        |
