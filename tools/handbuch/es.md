## 1 Introducción

voyzSESSION PRO es un software de grabación y mezcla (DAW) para producciones de voz: locución y comentario en off sobre imagen, doblaje, reportajes de radio, podcasts y audiolibros.

En las producciones sobre imagen cargas un vídeo, grabas el texto sincronizado con él y exportas la mezcla terminada como archivo de audio o directamente en el vídeo o en el MXF. Las producciones solo de audio, como un podcast, un audiolibro o un reportaje de radio, no necesitan vídeo. Para ellas están la página **AUDIO** con el Script Editor, perfiles de sonoridad para radio, podcast y audiolibro, y formatos de exportación como MP2, MP3, FLAC y Opus.

### 1.1 Modo Assist y modo Manual

| | Modo Assist | Modo Manual |
|---|---|---|
| Pensado para | Locutores, redactores y montadores sin conocimientos de técnica de sonido | Técnicos e ingenieros de sonido |
| Quién mezcla | El automatismo (AUTO MIX) | Tú mismo, como en Pro Tools o Logic |
| Uso típico | Grabación y entrega rápida | Edición y mezcla fina |
| Resultado | Mezcla según la norma de sonoridad elegida con solo pulsar un botón | Control total sobre controles, plug-ins y automatización |

Lo que AUTO MIX calcula en el modo Assist, el modo Manual lo adopta como punto de partida. Puedes grabar en ambos modos.

### 1.2 Requisitos del sistema

| | Recomendado | Mínimo |
|---|---|---|
| Mac | Procesador de Apple (M1 o posterior) | Mac con Intel (funciona, pero no se recomienda) |
| Sistema operativo | macOS 14 Sonoma o posterior | macOS 14 Sonoma |
| Memoria | 32 GB en proyectos de más de 30 minutos con vídeo 4K | 16 GB |
| Almacenamiento | SSD | 5 GB libres, más espacio para el material del proyecto |
| Audio | Interfaz de audio con micrófono y auriculares | Micrófono integrado o micrófono USB |

En los Mac con Intel y con menos de 16 GB de memoria, la app muestra una sola vez, en el primer inicio, un aviso sobre el hardware. El controlador de audio para la locución remota necesita macOS 13, y la cámara virtual, macOS 12.3. Con macOS 14 se cumplen ambos requisitos.

### 1.3 Instalación

1.  Descarga `voyzsession-2.0.dmg` de pegelwerk.com.
2.  Abre el DMG y arrastra voyzSESSION PRO a la carpeta Aplicaciones. La cámara virtual solo funciona si la app está allí.
3.  Inicia la app. macOS pide acceso al micrófono. Permítelo; de lo contrario no es posible grabar.
4.  La primera vez que abras el prompter, macOS pide permiso para el reconocimiento de voz. Permítelo también, para que el texto pueda seguir tu voz.

La app avisa de las nuevas versiones con la etiqueta UPDATE en la barra superior.

### 1.4 Licencia y periodo de prueba

En el primer inicio se abre la ventana "voyzSESSION PRO - Licencia". Puedes probar la app durante 7 días. Una etiqueta en la barra superior muestra los días restantes.

Así activas la licencia:

1.  Pega en el campo la clave de licencia de tu correo electrónico o arrastra el archivo `license.lic` a la ventana. También puedes hacer clic en el enlace de activación del correo.
2.  Haz clic en **Activar**.

**Comprar licencia** lleva a la tienda. Con una suscripción, el botón se llama **Gestionar suscripción**. Con la etiqueta de licencia de la barra superior vuelves a abrir la ventana en cualquier momento.

Al terminar el periodo de prueba, la app sigue funcionando con limitaciones y emite cada minuto un breve tono de recordatorio. Si una suscripción ha caducado, la exportación queda bloqueada.

## 2 La interfaz

La ventana principal consta de tres zonas fijas: arriba, la barra superior; en el centro, la página de trabajo (**VÍDEO**, **AUDIO** o **EDIT**); y abajo, la barra de transporte con los botones de reproducción y grabación. Entre la página de trabajo y la barra de transporte puede mostrarse la barra de navegación.

### 2.1 Barra superior

Los elementos, de izquierda a derecha:

| Elemento | Función |
|---|---|
| ARCHIVO | Proyecto nuevo, abrir, usados recientemente, guardar, guardar como, plantillas ([capítulo 15](#k15)) |
| PROYECTO... | Ajustes del proyecto: frecuencia de muestreo, frecuencia de imagen, código de tiempo inicial, perfil, estilo de mezcla |
| VÍDEO, AUDIO, EDIT, MIXER | Cambio de página de trabajo ([sección 2.2](#k2-2)) |
| MEDIA | Mostrar y ocultar la bandeja de medios |
| ABRIR VÍDEO | Abrir un vídeo. Con un vídeo cargado aparece al lado una x para quitarlo. Quitarlo se puede deshacer. |
| IMAGEN | Activar o desactivar la ventana de vídeo (Cmd+9). Con un clic derecho llevas la imagen a una pantalla externa o muestras el código de tiempo. |
| LEVEL | Control de nivel del micrófono |
| A/V... | Ajustes de audio y vídeo (interfaz, entrada y salida) |

El manual de usuario lo abres desde el menú de la app: voyzSESSION PRO \> Manual (Cmd+Shift+/). Viene incluido en la app y funciona sin conexión a internet.

Durante el periodo de prueba, una etiqueta con el rótulo PRUEBA muestra los días restantes. Si hay una versión nueva, aparece una etiqueta UPDATE que lleva a la página de descarga.

### 2.2 Páginas de trabajo

| Página | Finalidad | Contenido |
|---|---|---|
| VÍDEO | Grabación sobre imagen | Vídeo y prompter con el texto que se va a locutar |
| AUDIO | Proyectos solo de audio, por ejemplo podcasts | Script Editor con la transcripción de las grabaciones |
| EDIT | Edición y arreglo | Línea de tiempo multipista |
| MIXER | Mezcla | El mezclador se superpone a la página actual. Un clic en otra página lo cierra. |

### 2.3 Barra de transporte

- **Izquierda:** deshacer y rehacer, un conmutador basculante para el zoom del eje de tiempo y otro para la altura de las pistas.
- **Centro:** \|\<\< (al principio), retroceso, **PLAY/STOP**, **REC**, **LOOP**, avance, \>\>\| (al final). Una pulsación breve de una tecla de bobinado salta 1 segundo; si la mantienes pulsada, bobina a velocidad creciente hasta 32 veces la normal.
- **Contador de posición:** muestra la posición actual, en rojo al grabar y en verde al reproducir. Tras un clic puedes introducir un tiempo. Con un clic derecho eliges la visualización en código de tiempo, minutos:segundos o samples.
- **Grupo de grabación:** **V-PUNCH** (punch mediante reconocimiento de voz), **PRE** (pre-roll antes de la grabación, 0 a 10 segundos) y **POST** (post-roll tras el punch-out).
- **Derecha:** el conmutador **ASSIST \| MANUAL**, el botón del estilo de mezcla (muestra el activo, por ejemplo **REPORTAJE** o **TRÁILER**, [sección 7.1](#k7-1)), el botón **AUTO MIX** (solo en el modo Assist) y **EXPORT**.

Debajo de los botones hay una línea de avisos en la que la app informa del proceso en curso, por ejemplo "Renderizando mezcla...". Los mensajes de éxito aparecen en verde. Si **AUTO MIX** se ilumina en azul, la mezcla guardada ya no corresponde al proyecto y conviene volver a calcularla.

### 2.4 Barra de navegación

La barra de navegación se muestra y se oculta con Ventana \> Barra de navegación. Muestra todo el proyecto como forma de onda. Un clic salta a la posición elegida. En la página **EDIT**, un marco señala la sección visible, que puedes desplazar con el ratón.

A la izquierda introduces **START**, **FIN** y **DURACIÓN** del rango. A la derecha están los botones de marcadores: **MK +** pone un marcador, los botones **MK** con flecha saltan al marcador anterior o siguiente y **MARKER** muestra una lista de todos los marcadores. Un proyecto puede contener hasta 999 marcadores.

### 2.5 Barra de menús

| Menú | Opción | Atajo de teclado |
|---|---|---|
| voyzSESSION PRO | Acerca de voyzSESSION PRO..., Stream Deck: instalar plug-in..., Stream Deck: cargar disposición, Salir | Cmd+Q |
| voyzSESSION PRO | Manual | Cmd+Shift+/ |
| Archivo | Importar AAF... ([sección 3.5](#k3-5)) | |
| Ajustes | General... | Cmd+, |
| Ajustes | Audio/vídeo... | |
| Ajustes | Fundido cruzado al solapar (activar/desactivar) | |
| Ventana | Ventana de cabina | Cmd+Shift+B |
| Ventana | Capítulos | Cmd+Shift+K |
| Ventana | Ventana de imagen | Cmd+9 |
| Ventana | Barra de navegación (activar/desactivar) | |

Proyecto nuevo, abrir, guardar y plantillas están en el botón **ARCHIVO** de la barra superior, no en el menú Archivo.

## 3 Primeros pasos

Este capítulo te lleva del proyecto vacío a la primera grabación.

### 3.1 Crear y guardar un proyecto

1.  Elige **ARCHIVO** \> **Nuevo proyecto vacío**. Un proyecto nuevo ya contiene una pista de voz.
2.  Guarda el proyecto enseguida con **ARCHIVO** \> **Guardar...** (Cmd+S), preferiblemente en un SSD con espacio suficiente.

La app escribe las grabaciones directamente en la carpeta del proyecto. Si el proyecto aún no se ha guardado, la primera vez que pulses **REC** aparece el mensaje "Recording needs a project folder".

Si trabajas a menudo con la misma distribución de pistas, crea los proyectos nuevos con **ARCHIVO** \> **Nuevo desde plantilla** ([capítulo 15](#k15)).

### 3.2 Configurar el dispositivo de audio

1.  Haz clic en **A/V...** en la barra superior.
2.  En **OUTPUT**, elige tu salida de auriculares o tu interfaz y, en **INPUT**, tu micrófono.
3.  Si te escuchas directamente a través de la interfaz (Direct Monitor en el aparato), deja activada la opción **Direct hardware monitoring**. Si no dispones de esa posibilidad, desactívala. Entonces te escuchas a través del software.

Graba siempre con auriculares. Si reproduces por altavoces, el sonido del vídeo entra en el micrófono.

### 3.3 Ajustar el nivel del micrófono (control de nivel)

El control de nivel lo abres con **LEVEL** en la barra superior. Con el ajuste por defecto no aparece por sí solo al iniciar.

1.  Elige el micrófono arriba.
2.  Di algunas frases con el volumen con el que vas a grabar después.
3.  Ajusta la preamplificación (gain) de la interfaz de modo que el indicador muestre "Nivel óptimo".

| Indicación | Nivel de pico | Qué hacer |
|---|---|---|
| Sin señal | por debajo de -50 dBFS | Comprobar el cable, la selección de micrófono y la alimentación phantom |
| Demasiado bajo | por debajo de -18 dBFS | Subir el gain en la interfaz |
| Nivel óptimo | -18 a -3 dBFS | Mantener el ajuste |
| Demasiado alto | por encima de -3 dBFS | Bajar el gain; de lo contrario la grabación se distorsiona |

En la misma ventana eliges el perfil de sonoridad, es decir, la norma para la que entregas, por ejemplo EBU/ARD-ZDF o Podcast. La casilla "No mostrar en el próximo inicio" viene marcada de fábrica. Si quieres que el control de nivel aparezca en cada inicio, desmarca la casilla o actívalo en Ajustes \> General.

### 3.4 Cargar un vídeo

1.  Haz clic en **ABRIR VÍDEO** o arrastra el archivo a la ventana.
2.  Se admiten MP4, MOV, M4V y MXF. WebM no se admite.
3.  Con un MXF, la app crea primero una copia de reproducción (proxy). Una barra de progreso muestra el proceso. La próxima vez que lo abras se reutiliza la copia.

Si el vídeo tiene más de dos pistas de audio, algo frecuente en MXF, aparece la ventana "¿Qué pistas de audio quieres?":

- Marca cada pista que necesites. Por defecto no hay ninguna pista seleccionada.
- Con el corchete junto a una pareja (1+2, 3+4, etc.) creas dos pistas mono como una pista estéreo.
- **Elige el rol de cada fila:** Auto, Premezcla IT, Voz, Diálogo, Música, Atmo, Estadio o Efectos. El rol controla después AUTO MIX ([capítulo 7](#k7)).
- **Importar** adopta la selección. Si en cambio cierras la ventana, se cancela toda la importación.

Los vídeos con una o dos pistas de audio se adoptan sin preguntar, con el rol Auto.

**Con una plantilla de sesión:** si el proyecto contiene pistas de playout vacías procedentes de una plantilla ([sección 15.4](#k15-4)), el sonido del vídeo va a esas pistas. La ventana aparece entonces ya rellenada, con las casillas y los roles como en la plantilla. Un aviso indica cuántas pistas van a las pistas existentes de la plantilla. Confirmas con **Importar**; así ves un número de pistas distinto en el material nuevo antes de que se aplique. Con vídeos de una o dos pistas de audio, la app asigna sin preguntar. Solo se rellena de antemano si el número de pista y el formato (mono o estéreo) coinciden con la plantilla; si no, se crean pistas nuevas como hasta ahora.

Una secuencia del montaje de vídeo la adoptas mediante un archivo AAF ([sección 3.5](#k3-5)).

### 3.5 Importar una secuencia del montaje (AAF)

Con Archivo \> **Importar AAF...** traes al proyecto abierto las pistas de audio de una secuencia del montaje de vídeo, por ejemplo de Avid Media Composer, Adobe Premiere Pro o DaVinci Resolve. Las pistas se añaden y cada clip queda en su posición de código de tiempo.

1.  Elige Archivo \> **Importar AAF...** y abre el archivo AAF.
2.  En la ventana "Importar AAF", decide si se aplica **Adoptar los niveles de clip del montaje**. Por defecto el conmutador está desactivado: el volumen de clip y los keyframes de nivel del montaje se ignoran, y AUTO MIX trabaja con el material en bruto. Si lo activas, actúan además de la nivelación de AUTO MIX, como línea de clip gain en la toma.
3.  Haz clic en **Importar**. La app lee la secuencia y decodifica los medios. Una barra de progreso muestra el proceso.
4.  Si los archivos multimedia no están en la ruta que figura en el AAF, aparece "Archivos multimedia no encontrados". Con **Elegir carpeta...** la app los busca en una carpeta y sus subcarpetas; con **Importar sin ellos** faltan los clips afectados.
5.  Comprueba los roles (ver más abajo) y confirma.

Los medios pueden estar incrustados en el AAF o vinculados como archivos aparte, también como MXF OP-Atom de Avid. Se adoptan los clips, los nombres de los clips, los fundidos, el pan de pista y la automatización de pan. Las parejas mono que forman una pista estéreo en el montaje se combinan en pistas estéreo. En un proyecto vacío, la app adopta el código de tiempo inicial de la secuencia. Si el proyecto ya contiene material, los clips se colocan según el código de tiempo del proyecto.

**Roles:** para que AUTO MIX trate las pistas correctamente, cada pista recibe un rol ([sección 7.1](#k7-1)).

- **Según los nombres de pista:** si una pista mono se llama, por ejemplo, "Voice", "Voiceover", "Narrator", "Sprecher" o "Kommentar", se convierte en pista de voz. Nombres como "Music", "Musik", "Atmo" o "FX" dan el rol correspondiente.
- **Según el contenido:** para las pistas sin rol en el nombre, la app escucha el audio y propone un rol en la ventana "Roles según el contenido": sonido directo, música, efectos o ambiente. El habla se propone siempre como sonido directo, porque la pista de voz para el texto en off suele crearse después, al grabar. Revisa las propuestas y cámbialas si es necesario. **Sin roles del contenido** importa estas pistas sin rol.
- **Clips sin habla en pistas de habla:** si en una pista de sonido directo o de voz hay un clip sin habla, por ejemplo un ruido o un tono de sala, AUTO MIX lo nivelaría como si fuera habla. La app enumera esos clips. Los clips marcados van a una pista propia con el rol adecuado. **Dejar los clips en sus pistas** lo adopta todo sin cambios.

Tras la importación, un informe resume lo que se ha adoptado y lo que no. No se adoptan, entre otras cosas, los efectos de clip y de pista, las alteraciones de tiempo (los clips se reproducen a velocidad original), el pan en clips sueltos ni las formas de fundido especiales, que se sustituyen por la forma estándar. En los clips con más de dos canales se adoptan los canales 1 y 2. La importación no es posible durante una grabación ni mientras se guarda.

### 3.6 Primera grabación

1.  En la cabecera de la pista de voz, haz clic en **R** para armar la pista. La tecla se ilumina en rojo.
2.  Pulsa **REC** o la tecla R. Tras el pre-roll (**PRE**, por defecto 4 segundos) empieza la grabación.
3.  Termina la grabación con **STOP REC** o pulsando de nuevo la tecla R.
4.  Con la barra espaciadora reproduces la grabación.

El [capítulo 4](#k4) describe la grabación en detalle, el [capítulo 7](#k7) la mezcla automática y el [capítulo 12](#k12) la exportación.

## 4 Grabar

Se graba en cada pista que esté armada. Puede haber varias pistas armadas a la vez, y cada una de ellas se oye, como en otras DAW.

### 4.1 Cabecera de pista

| Tecla | Nombre | Función |
|---|---|---|
| R | Armar | REC graba en esta pista. Alt+clic actúa sobre todas las pistas. |
| I | Escuchar la entrada (INPUT ONLY) | Activado: la entrada se oye siempre, también durante la reproducción y sin R. Desactivado (Auto Input): con la pista armada, la entrada solo se oye con el transporte parado y durante la grabación. Solo se graba con R. |
| M | Silencio | Silenciar la pista |
| S | Solo | Oír solo esta pista |
| AC | AutoCut | Corta automáticamente la siguiente grabación en las pausas |
| IMPORT | Importar | Traer un archivo de audio a esta pista |
| Entrada | Selección de entrada | Entrada de la interfaz que va a la pista |

La tecla I solo aparece en las pistas de voz y solo cuando la monitorización por hardware está desactivada.

Con **+ Voice** creas una nueva pista de voz (mono) y con **+ Audio** una pista de playout (estéreo) para música, ambiente y similares.

Con un clic derecho en la cabecera de pista o con la rueda dentada accedes a más comandos: Renombrar, Subir/Bajar, Voz de referencia, combinar o separar en estéreo, Vista y Borrar pista. Las pistas también se pueden mover arrastrando la cabecera de pista. Con Cmd+clic o Shift+clic seleccionas varias pistas. La última pista de voz no se puede borrar. El color de una pista se cambia en el mezclador con un doble clic en el nombre de la pista.

### 4.2 Pre-roll y post-roll

- **PRE** (pre-roll) determina cuánto tiempo arranca el vídeo antes del punto de grabación. Se puede ajustar de 0 a 10 segundos; el valor por defecto es 4 segundos. Con un doble clic en el número introduces un valor.
- **POST** (post-roll) determina cuánto tiempo sigue la reproducción tras el final de una grabación en rango.
- Durante el pre-roll el botón hace una cuenta atrás (por ejemplo "**PRE** 3.2s") y después muestra **STOP REC**. Una nueva pulsación cancela la grabación.
- **REC durante la reproducción** graba de inmediato en la posición de reproducción, sin salto y sin pre-roll (punch-in en marcha). El pre-roll solo se aplica al arrancar desde parado.
- Si se graba sobre una toma existente, la nueva grabación sustituye la parte solapada. Lo que queda antes y después se conserva.

### 4.3 Rango, loop y punch

Arriba, en la regla, hay una franja para un rango. Este rango sirve tanto para el loop como para la grabación en rango.

- **Crear un rango:** arrastra en la franja vacía. Arrastrar un borde cambia la longitud, arrastrar en el centro desplaza el rango y un doble clic lo borra. El inicio, el final y la duración también se pueden introducir en la barra de navegación.
- **LOOP** o la tecla L repite el rango. Si no hay ningún rango, la app usa la sección visible.
- **Grabar solo en el rango (punch):** un clic derecho en **REC** alterna entre "grabar hasta STOP" y "Grabar en rango". En el segundo caso el rango se muestra en naranja, y la grabación empieza y termina exactamente en sus bordes. Si pulsas REC durante la reproducción antes del rango, la grabación espera a su inicio. Hasta entonces el botón muestra el tiempo de espera (por ejemplo "**PUNCH** 2.5s"). Dentro del rango la grabación empieza de inmediato. Si la posición de reproducción está detrás del rango o justo antes de su final, la reproducción se detiene y la grabación arranca como desde parado, con pre-roll.

### 4.4 Voice Punch

Con **V-PUNCH** fijas mediante la voz el punto de entrada tras una equivocación:

1.  Pulsa **V-PUNCH**.
2.  Di las últimas palabras correctas antes de la equivocación.
3.  La app busca ese punto, coloca la entrada en la pausa siguiente, reproduce el pre-roll e inicia la grabación. A partir de ahí vuelves a locutar.

Con Shift+clic en **V-PUNCH** dices además las primeras palabras después del error. Entonces solo se sustituye la parte errónea, y el original continúa a continuación.

Requisitos: el proyecto está guardado, la página **VÍDEO** está abierta, el transporte está parado, hay una pista de voz armada, el reconocimiento de voz de macOS está permitido y la toma ya está transcrita.

### 4.5 Marcadores

| Manejo | Función |
|---|---|
| Alt+M o MK + | Poner un marcador en la posición de reproducción |
| 1 a 9 | Poner un marcador en el puesto 1 a 9 |
| Shift+1 a 9 | Saltar al marcador 1 a 9 |
| Alt+coma, Alt+punto | Al marcador anterior o siguiente |
| Arrastrar la banderita | Mover el marcador |
| Clic en el rótulo | Nombrar el marcador |
| Doble clic en la banderita | Borrar el marcador (se puede deshacer) |

## 5 Prompter, Script Editor y ventana de cabina

El prompter muestra el texto durante la grabación y sigue la voz. El Script Editor muestra lo dicho como texto. Allí puedes editar el audio marcando palabras y borrándolas.

### 5.1 Prompter (página VÍDEO)

Con **CARGAR GUION** abres un archivo de texto en formato .txt, .rtf o .pdf (PDF solo con capa de texto). También puedes arrastrar el archivo a la ventana o pegar el texto con Cmd+V.

Mientras hablas, el reconocimiento de voz de macOS escucha y hace avanzar la línea actual. Si te desplazas con la rueda del ratón, el seguimiento se detiene durante 8 segundos. Si el prompter no puede seguir la voz, por ejemplo porque falta la función de dictado, muestra un aviso.

| Manejo | Función |
|---|---|
| LANG | Idioma del reconocimiento de voz, independiente del idioma de la app |
| EDIT / DONE | Editar el texto directamente. Mientras tanto, el reconocimiento de voz se pausa. |
| A- / A+, Cmd+Menos / Cmd+Más / Cmd+0 | Tamaño de letra |
| Teclas de flecha | Una palabra adelante o atrás |
| Re Pág, Av Pág | 20 palabras adelante o atrás |
| Inicio | Al principio del texto |
| Clic en una palabra | La palabra pasa a ser la línea actual. Si el texto está vinculado a una grabación, la línea de tiempo también salta. |
| FROM TAKE | Crea un texto de prompter a partir de la transcripción de una grabación |

### 5.2 Script Editor (página AUDIO)

El Script Editor muestra la transcripción de todas las pistas de voz, cada pista en su color. La transcripción se realiza en el propio Mac y empieza automáticamente después de una grabación, una importación o la carga de un proyecto. Las pistas de playout no se transcriben.

- **Transcribir** aparece mientras todavía no haya texto. Si solo falta el texto de algunas tomas, el botón se llama **Transcribir faltantes**.
- Un clic en una palabra coloca el cursor en la pausa anterior a ella.
- **Editar el audio:** marca palabras arrastrando y pulsa Supr. La app recorta el audio, coloca los cortes en las pausas más cercanas y cierra el hueco. La operación se puede deshacer en un solo paso.
- **Corregir una palabra:** doble clic en la palabra, cambia el texto y pulsa Return. Solo cambia el texto, no el audio.
- **Quitar muletillas** busca muletillas como "eh"; **Buscar texto** encuentra pasajes en la transcripción.
- **TEXT EXPORT** guarda la transcripción o subtítulos (SRT, VTT, TXT, JSON).

Los tiempos de las palabras sirven como orientación. Para cortes muy precisos conviene escuchar el resultado.

### 5.3 Ventana de cabina

La ventana de cabina (Ventana \> Ventana de cabina, Cmd+Shift+B) está pensada para un monitor en la cabina del locutor, conectado por HDMI. Muestra a la izquierda el prompter y a la derecha la imagen con código de tiempo. Durante la grabación aparece un marco rojo; durante el pre-roll el código de tiempo se pone rojo. El prompter de la ventana de cabina va sincronizado con el prompter de la ventana principal. Si hay una segunda pantalla conectada, la ventana se abre allí a pantalla completa.

## 6 Edición en la línea de tiempo

La página **EDIT** muestra todas las pistas en una línea de tiempo. Aquí cortas, desplazas y aplicas fundidos a las tomas.

### 6.1 Editar tomas

La mitad superior y la mitad inferior de una toma reaccionan de forma distinta:

| Zona | Al arrastrar |
|---|---|
| Mitad inferior | Mover la toma |
| Mitad superior | Marcar un rango de selección amarillo dentro de la toma |
| Borde izquierdo o derecho | Acortar o alargar la toma (recortar) |
| Tirador de fundido en la esquina | Ajustar el fundido de entrada o de salida |

- Cmd+clic añade tomas a la selección; Cmd+A selecciona todas las tomas.
- Con la tecla Control o Shift pulsada, una toma arrastrada solo cambia de pista y su posición temporal no varía. En la regla aparece entonces "TIEMPO BLOQUEADO".
- Con la tecla Alt pulsada, al arrastrar no se ajusta a la cuadrícula.
- Cmd+flecha arriba o abajo mueve la toma a la pista vecina; con Shift se crea una copia.
- Flecha izquierda o derecha desplaza la selección un fotograma; con Shift, un segundo.

### 6.2 Cortar, borrar, copiar

| Comando | Atajo de teclado |
|---|---|
| Dividir en el cursor o recortar el rango de selección | Cmd+E |
| Borrar | Supr o Retroceso |
| Copiar, pegar en el cursor | Cmd+C, Cmd+V |
| Duplicar | Cmd+D |
| Silenciar la toma | M |
| AutoCut (quitar silencios) | S |
| Deshacer, rehacer | Cmd+Z, Cmd+Shift+Z |

Los fragmentos divididos reciben nombres consecutivos, por ejemplo "Take 3-01" y "Take 3-02". El clic derecho en una toma ofrece, entre otras cosas: Renombrar, reemplazar el audio, Quitar selección, Conservar solo la selección, Activar estiramiento (después arrastra el borde para estirar la toma en el tiempo), Fade / Crossfade y Restablecer corrección de clip gain. Un clic derecho en un lugar vacío ofrece "Insertar audio aquí...".

### 6.3 Fundidos y fundidos cruzados

- **Tecla F:** marca un rango al principio o al final de una toma y pulsa F. Se crea un fundido. Si la marca abarca el límite entre dos tomas, se crea un fundido cruzado.
- **Solapar:** si una toma se arrastra sobre otra, se crea automáticamente un fundido cruzado sobre el solapamiento. Si queda completamente dentro de otra toma, ambos bordes reciben un fundido cruzado de 50 ms. Esta función se desactiva en Ajustes \> Fundido cruzado al solapar. La toma arrastrada sobrescribe entonces la que está debajo.
- La duración de un fundido cruzado se cambia arrastrando los bordes de la casilla del fundido cruzado.

### 6.4 Clip gain

Abajo a la izquierda de cada toma hay un pequeño control. Arrastrarlo hacia arriba o hacia abajo sube o baja el volumen de toda la toma; con Shift, en pasos finos. Un doble clic restablece la corrección.

En la línea de clip gain de la toma pones puntos con un clic, los arrastras al nivel deseado y los borras con un doble clic. Así se pueden subir o bajar palabras sueltas. La línea de AUTO MIX y tu propia corrección se superponen como dos capas.

### 6.5 Zoom y vista

| Función | Manejo |
|---|---|
| Zoom del eje de tiempo | Conmutador basculante a la izquierda de la barra de transporte, Cmd+= y Cmd+Menos, Cmd+rueda del ratón |
| Mostrar todo el proyecto | Tecla 0 |
| Zoom a la selección | Tecla Z |
| Altura de pista | Segundo conmutador basculante, Control+Alt+flecha arriba/abajo, Alt+rueda del ratón |
| Ampliar la forma de onda | Cmd+Alt+flecha arriba/abajo, Shift+Alt+rueda del ratón |
| Al principio, al final | Return, Fin |
| Bobinar | Coma, punto (1 segundo cada vez) |

### 6.6 Bandeja de medios

**MEDIA** en la barra superior abre la bandeja de medios (lista de clips). Contiene todo el material del proyecto en los grupos IMPORTADO, SONIDO DEL VÍDEO, GRABACIONES y SIN USAR.

- **IMPORT** trae archivos a la bandeja, pero todavía no a una pista. Los formatos posibles son WAV, BWF, AIFF, FLAC, OGG, MP3, M4A, AAC y CAF. Los archivos importados conservan su nombre original.
- **Preescucha:** deja el puntero del ratón un momento sobre una fila o usa las teclas de flecha. La barra espaciadora inicia y detiene; Esc termina.
- **Colocar:** un doble clic coloca el archivo en la posición de reproducción de la pista seleccionada. También puedes arrastrar el archivo a la línea de tiempo.
- Las regiones aparecen sangradas debajo de su archivo. Un clic muestra la región en la línea de tiempo; al arrastrar se coloca solo esa región.
- **Con clic derecho:** Importar a la pista seleccionada, Mostrar en el Finder, Quitar de la lista de clips, Quitar material sin usar.

Sin la bandeja también es posible: selecciona una pista y pulsa la tecla I. El archivo elegido se inserta en la posición de reproducción.

## 7 Modo Assist y AUTO MIX

En el modo Assist, la app se encarga de la mezcla. **AUTO MIX** (o Cmd+M) procesa la voz, baja la música y el ambiente bajo el habla y lleva la mezcla a la sonoridad del perfil elegido. Tras el inicio, el modo Assist está activo.

### 7.1 Preparación: perfil, estilo de mezcla y roles

En **PROYECTO...** \> Perfil de sonoridad fijas para qué norma entregas. El perfil determina solo la entrega: la sonoridad objetivo, el pico máximo admisible (true peak) y la normalización. Cómo suena la mezcla lo determina el estilo de mezcla (ver más abajo).

| Grupo | Perfil | Sonoridad | True peak |
|---|---|---|---|
| TV/Radio | EBU/ARD-ZDF | -23 LUFS | -1 dBTP |
| TV/Radio | ATSC A/85 (EE. UU.) | -24 LUFS | -2 dBTP |
| TV/Radio | ARIB TR-B32 (Japón) | -24 LUFS | -1 dBTP |
| TV/Radio | OP-59 (Australia) | -24 LUFS | -2 dBTP |
| TV/Radio | CST-RT-040 (Francia) | -23 LUFS | -3 dBTP |
| Streaming | Podcast | -16 LUFS | -1 dBTP |
| Streaming | YouTube | -14 LUFS | -1 dBTP |
| Otros | Audiolibro | -18 LUFS | -3 dBTP |
| Otros | Studio 0 dB | sin objetivo de sonoridad | pico a 0 dBTP |

**Estilo de mezcla:** fija cómo pondera AUTO MIX las pistas, con independencia del perfil de sonoridad. Lo eliges con el botón junto a **AUTO MIX** en la barra de transporte o en **PROYECTO...**, en la fila **Estilo de mezcla**. El cambio se puede deshacer.

| Estilo de mezcla | Botón de la barra |
|---|---|
| Reportaje / magacín | REPORTAJE |
| Tráiler / promo | TRÁILER |
| Documental | DOCU |
| Deporte / comentario | DEPORTE |
| Pódcast / tertulia | PÓDCAST |
| Audiolibro / radioteatro | AUDIOLIBRO |

El ajuste predeterminado es **Reportaje / magacín**. El estilo de mezcla fija los valores iniciales, por ejemplo cuánto queda la cama por debajo de la voz. Con **Tráiler / promo** mandan la música y los efectos, el locutor queda más denso por encima y, bajo el locutor, la música solo cede en su rango de frecuencias. Los graves y los medios bajos se mantienen.

Los proyectos guardados con los antiguos perfiles Trailer, Documental, Deportes, Podcast o Audiolibro se abren con el perfil de sonoridad y el estilo de mezcla correspondientes.

Además, cada pista necesita un rol. El rol indica al automatismo qué hay en la pista. Lo eliges con el botón de rol de la cabecera de pista o en el mezclador.

| Rol | Abreviatura | Nivel respecto al locutor | Procesamiento del automatismo |
|---|---|---|---|
| Voz | SPKR | Nivel de referencia | La voz se procesa y se nivela |
| Sonido directo | OT | igual de alto (0 LU) | Se nivela respecto al locutor, cadena de voz propia |
| Música | MUS | 4 LU más bajo | Se baja bajo el locutor y el sonido original |
| Efectos | FX | 4 LU más bajo | Se baja |
| Ambiente | ATMO | 16 LU más bajo | Se baja |
| Estadio | STAD | 5 LU más bajo | Se compensan los saltos de nivel, pero la pista nunca se baja |
| Premezcla IT | PRE | sin cambios | Para una premezcla terminada procedente del montaje; se comporta como "Sin clasificar" |
| Sin clasificar (Auto) | AUTO | sin cambios | Sin procesamiento |

Las pistas nuevas tienen el rol Voz. Una pista de playout mono se convierte en pista de voz con la opción de menú "Voz - convertir en pista de voz".

### 7.2 Iniciar AUTO MIX

1.  Debe haber al menos una grabación, y el solo no puede estar activo.
2.  Pulsa **AUTO MIX** a la derecha de la barra de transporte o Cmd+M.
3.  Una ventana de progreso muestra los distintos pasos: preparar, preparar la voz, compresión y nivel, timbre, cama y ducking, sonoridad. Con **Cancelar** detienes el proceso en cualquier momento.
4.  Después reproduces la mezcla terminada con **PLAY**.

Antes del cálculo, en el modo Assist la app pone todos los faders del mezclador a 0 dB. Esto se puede deshacer. Si ya se han puesto puntos de automatización propios en pistas de playout, la app pregunta: **Recalcular**, **Mantener la mía** o **Cancelar**.

**AUTO MIX** no se inicia durante una grabación ("No durante la grabación."), con el solo activo ("Desactiva **SOLO** antes de AUTO MIX.") ni en el modo Manual. En el modo Manual, en su lugar, normaliza la exportación.

### 7.3 Resultado de AUTO MIX

Todas las decisiones del automatismo se pueden ver y cambiar:

- **Línea de clip gain de la voz:** el volumen del habla se nivela mediante una línea en la toma, en un margen de hasta 9 dB hacia arriba o hacia abajo. Tu propia corrección queda encima como segunda capa.
- **Ducking como automatización de volumen:** la bajada de la música y el ambiente bajo el habla figura como curva en la automatización de volumen de cada pista.
- **Valores en el channel strip:** el EQ, el compresor, el de-esser y los demás módulos tienen los valores calculados. Clic derecho en un botón \> **Ver...** muestra el módulo bloqueado con esos valores.

La música, los efectos, el ambiente y el sonido original tienen cada uno su propia protección de picos. Solo actúa si el archivo final superaría de otro modo el límite de true peak del perfil. Así, un golpe fuerte en la música ya no hunde toda la cama.

Si **AUTO MIX** se ilumina en azul, la mezcla guardada ya no corresponde al proyecto, por ejemplo tras una grabación nueva o un corte. Pulsa entonces el botón de nuevo.

Los proyectos de la versión 1.6 necesitan un nuevo **AUTO MIX**, porque la cadena de señal ha cambiado en la versión 2.0.

### 7.4 Opciones de ajuste en el modo Assist

- Los faders de las pistas se pueden mover. Los faders del grupo de voz y del master son fijos en el modo Assist (indicación **FIXED**).
- Los botones del channel strip solo activan y desactivan módulos. El ajuste de los módulos lo hace el automatismo.
- Las ranuras de insert para plug-ins son visibles, pero solo se activan en el modo Manual.

Quien quiera mezclar por sí mismo pasa al modo Manual con **MANUAL**. La mezcla de AUTO MIX se adopta por completo como punto de partida ([capítulo 8](#k8)).

## 8 Modo Manual: mezclador, channel strip, grupos, master

En el modo Manual mezclas tú mismo, como en Pro Tools, Logic o Nuendo. La app no modifica ningún fader, la escucha suena sin procesamiento adicional y la exportación escribe en el archivo exactamente lo que oyes.

### 8.1 Cambiar al modo Manual

Haz clic en **MANUAL** en la barra de transporte. El cambio también funciona durante la reproducción y se hace con un fundido, sin chasquidos.

Flujo habitual: grabar en el modo Assist y ejecutar **AUTO MIX**, y después pasar al modo Manual. El channel strip, los módulos, las líneas de nivel y el ducking se adoptan tal como sonaban por última vez. A continuación corriges los pasajes que quieras de otra manera.

| Función | Assist | Manual |
|---|---|---|
| Botón AUTO MIX | visible | oculto |
| Botones del channel strip | solo activar/desactivar | activar/desactivar, abre el módulo para editarlo |
| Ranuras de insert (plug-ins) | visibles, inactivas | activas |
| Automatización | desactivada (indicación AUTO en gris) | Read, Touch, Latch, Write, Trim |
| Faders del grupo de voz y del master | fijos (indicación FIXED) | libres |
| Saturate y reverberación | no se oyen | se oyen |
| Normalización | siempre, mediante AUTO MIX | solo con la casilla "Normalizar" de la ventana de exportación |

Si la mezcla satura en el modo Manual, un limitador en la salida protege el oído. La app avisa entonces de que la exportación recortaría (clipping). En ese caso, baja el fader del master o marca la casilla "Normalizar" al exportar.

### 8.2 Mezclador

El mezclador se abre con **MIXER** en la barra superior. Cada pista tiene un channel strip con las siguientes zonas, de arriba abajo:

1.  **Botones DSP:** los nueve módulos de sonido integrados ([capítulo 9](#k9))
2.  Entrada
3.  **Inserts:** cinco ranuras para plug-ins ([capítulo 10](#k10))
4.  **Sends:** cinco ranuras, todavía sin función en la versión 2.0
5.  **Salida:** solo indicación
6.  Modo de automatización ([capítulo 11](#k11))
7.  **Pan:** posición en la imagen estéreo
8.  Fader con medidor de nivel, rango de menos infinito a +12 dB. El fader aprovecha toda la altura libre de la ventana.
9.  **S, M y tecla de grabación:** solo, silencio, preparación para grabar
10. Rol y nombre

Con el menú contextual del channel strip muestras u ocultas zonas concretas, por ejemplo los inserts o los sends. Allí también combinas dos pistas mono en una pista estéreo o las vuelves a separar.

Junto al fader, una barra cian muestra la reducción de nivel (gain reduction) del compresor, con marcas en 6 y 12 dB.

### 8.3 Botones DSP

Cada channel strip tiene una cuadrícula de nueve botones. Leída en el orden de lectura, corresponde al orden en la ruta de señal:

| | | |
|---|---|---|
| REPR reparación | NR reducción de ruido | EQ ecualizador |
| TAME resonancia | DES de-esser | CMP compresor |
| BRTH De-Breath | SAT Saturate | REV reverberación |

- Activar abre el módulo; desactivar lo cierra. Si un módulo ya está activado, el primer clic solo abre la ventana.
- **Cambiar el orden:** EQ, TAME, DES, CMP, BRTH y SAT se pueden arrastrar a otra posición como los inserts. Un asterisco azul indica que el orden se ha cambiado. Clic derecho \> Orden estándar lo restablece. REPR y NR están fijos al principio, REV fijo al final. Estos botones llevan un pequeño punto.
- Un botón gris con el aviso "Solo en Manual" solo actúa en el modo Manual.

Las pistas de playout (música, ambiente, sonido original, etc.) tienen la misma cuadrícula, con dos limitaciones. Con el rol "Sin clasificar", la mayoría de los botones están bloqueados hasta que se elige un rol. NR y BRTH todavía no existen en las pistas de playout; el de-esser solo actúa con sonido original y locutor.

### 8.4 Grupos: voz e IT

Junto a las pistas hay dos channel strips de grupo. El grupo de voz reúne todas las pistas de voz; el grupo IT, todas las pistas de playout (la mezcla internacional sin locutor). Ambos grupos tienen fader, automatización, inserts y una cuadrícula con EQ, TAME, CMP y REV, que solo está activa en el modo Manual. Durante la reproducción, el fader del grupo IT muestra cómo trabaja el ducking.

### 8.5 Master

El master es la suma que se exporta.

- Fader del master con automatización.
- **PRE-GAIN** (hasta 24 dB hacia arriba o hacia abajo) antes del fader. Aquí deja AUTO MIX su compensación de nivel, para que el fader quede en 0 dB tras pasar al modo Manual. Arrastrar cambia el valor, Shift permite pasos finos y un doble clic lo pone a 0.
- **EQ** y **CMP** (compresor de bus), solo en el modo Manual.
- **Medidores de nivel:** nivel de pico izquierdo y derecho, y sonoridad en LUFS como valor momentáneo, de corto plazo e integrado. El valor grande LUFS I aparece en verde si se desvía como máximo 1 LU del objetivo, en naranja hasta 3 LU y en rojo por encima.
- **LRA**: el rango de sonoridad, es decir, cuánto varía la sonoridad a lo largo del programa.
- Indicador **CLIP**: se ilumina tras una saturación. Un clic en el channel strip lo restablece.

El channel strip propio **CUE** alimenta la ruta de auriculares (**AURICULARES**) y tiene una ranura de insert.

## 9 Los módulos de sonido

Cada uno de los nueve módulos de sonido tiene su propia ventana con controles. Lo que muestra el módulo se basa en los mismos valores con los que calculan la escucha y la exportación.

Para todos los módulos se aplica:

- La línea de estado muestra "Valores de AUTO MIX", "Editado (difiere del **AUTO MIX**)" o "Aún no hay AUTO MIX - se muestra la escucha".
- **Volver a AUTO MIX** restablece los valores del automatismo.
- En el modo Assist, clic derecho \> **Ver...** abre el módulo bloqueado con el aviso "Ajustado por **AUTO MIX**". El botón **Editar en Manual** pasa al modo Manual y desbloquea el módulo.
- **Presets:** presets de fábrica por categorías, además de "Propios", "Guardar preset..." y "Mostrar carpeta de presets". Los presets propios están en `~/Library/SATK/Presets/`. Los presets solo se pueden cargar en el modo Manual.
- Cmd+Z, Cmd+S y la barra espaciadora también funcionan cuando hay una ventana de módulo en primer plano.

### 9.1 REPR: reparación (De-Click y De-Plosive)

De-Click elimina clics y chasquidos de la boca; De-Plosive atenúa las explosivas de P y B por debajo de 240 Hz.

[[IMG:repr.png|El módulo REPAIR con De-Click y De-Plosive]]

| Control | Rango | Valor por defecto | Función |
|---|---|---|---|
| SENSIBILIDAD | 0 a 10 | 4 | Sensibilidad de la detección de clics |
| SESGO DE FRECUENCIA | -10 a +10 | 0 | Desplaza la detección hacia clics graves o agudos |
| ENSANCHE DE CLIC | 0 a 10 ms | 4 ms | Anchura de la zona reparada alrededor de un clic |

**SOLO CLICS** reproduce solo lo eliminado. Así se puede comprobar si se elimina demasiado. De-Click trabaja sin retardo. Los clics en las pausas del habla se eliminan en toda la banda de frecuencias. De-Plosive trabaja con ajustes fijos. En el modo Assist, REPR está desactivado; en el modo Manual se puede activar.

### 9.2 NR: reducción de ruido

NR elimina ruidos de fondo constantes, como ventiladores, zumbidos o el ruido de la sala. Para ello, una red neuronal separa la voz del ruido.

[[IMG:nr.png|El módulo NR con el control Cantidad]]

El módulo tiene un único control, **CANTIDAD** (0 a 100). Un segmento del anillo activa y desactiva NR; un doble clic pone el valor a 100. En el círculo se muestra el espectro medido. NR está desactivado por defecto, y AUTO MIX tampoco lo activa. En la versión 2.0, NR está disponible en las pistas de voz.

Los valores más altos eliminan más ruido, pero pueden alterar las eses. Presta atención a las eses al ajustarlo.

### 9.3 EQ: ecualizador

El EQ cambia el sonido de una pista, por ejemplo para hacer una voz más brillante o más cálida o para bajar frecuencias que retumban.

[[IMG:eq.png|El módulo EQ con analizador, bandas y controles de dinámica]]

El EQ tiene nueve bandas: paso alto (20 Hz a 1 kHz), campana 1 a 5, shelf de agudos, paso bajo (1 a 20 kHz, desactivado por defecto) y aire (8 kHz).

| Control | Rango |
|---|---|
| FREQ | Frecuencia en Hz |
| GAIN | -18 a +18 dB |
| Q (ancho de banda) | Campanas 0,15 a 14, shelves 0,1 a 10, filtros de corte 0,3 a 4 |

Las campanas y los shelves se pueden hacer dinámicos (**DYN**). La banda reacciona entonces al nivel y baja una frecuencia, por ejemplo, solo cuando se vuelve demasiado alta. Controles: **RANGE** (-24 a +24 dB), **THRESHOLD** (-80 a 0 dB), **ATTACK** (0,1 a 500 ms), **RELEASE** (5 ms a 5 s o AUTO).

**SOLO** en la banda (o Alt+clic en un punto de banda) reproduce solo la zona de frecuencias de esa banda. Funciona también en el modo Assist y nunca afecta a la exportación. El analizador muestra el espectro antes y después del EQ. En el menú **ANALYZER** ajustas **POST**, **PRE**+**POST** u OFF, además de resolución, velocidad, rango, inclinación y congelar.

### 9.4 TAME: resonancia

TAME detecta tonos aislados molestos, cortantes o retumbantes y los baja solo en el momento en que aparecen.

[[IMG:tame.png|El módulo TAME (resonancia)]]

| Control | Rango | Función |
|---|---|---|
| SOFT / HARD | | Modo de trabajo suave o enérgico |
| DEPTH | 0 a 10 | Intensidad de la reducción |
| DETAIL | 0 a 10 | Con qué finura se separan los tonos aislados |
| ATTACK, RELEASE | 0 a 10 | Tiempo de ataque y de liberación |
| MIX | 0 a 100 % | Proporción de señal procesada |
| MAX CUT | desactivado a 24 dB | Reducción máxima |
| OUT, WET TRIM | -18 a +18 dB | Nivel de salida |

Con hasta ocho bandas de sensibilidad (campana, shelf, filtro de corte, tilt y otras) determinas en qué zonas de frecuencia TAME trabaja con más precisión. **DELTA** reproduce solo lo eliminado. Hay 16 presets de fábrica en los grupos General, Habla, Mezcla y Música.

### 9.5 DES: de-esser

El de-esser suaviza las eses, ches y zetas agudas sin que la voz suene apagada.

[[IMG:deesser.png|El módulo DE-ESS]]

| Control | Rango | Función |
|---|---|---|
| SINGLE VOCAL / ALLROUND | | Voz individual o material mezclado |
| WIDE / SPLIT | | Bajar toda la señal o solo la zona de frecuencias aguda |
| THRESHOLD | menos infinito a 0 dB | Umbral de actuación |
| RANGE | 0 a 24 dB | Reducción máxima |
| LOOKAHEAD | 0 a 15 ms, activado/desactivado | Actúa ya un instante antes de la ese |
| HIGH-PASS, LOW-PASS | 2 a 20 kHz | Zona de frecuencias a la que reacciona el de-esser |

**TRIGGER** reproduce la señal a la que reacciona el de-esser; **QUITADO**, lo eliminado. AUTO MIX mide la agudeza de cada voz y ajusta el de-esser en consecuencia. Hay ocho presets de fábrica, por ejemplo para voces masculinas y femeninas.

### 9.6 CMP: compresor

El compresor iguala los pasajes fuertes y suaves para que la voz suene uniforme y presente. El módulo muestra la curva característica, la evolución del nivel y la reducción de nivel (en cian).

[[IMG:comp.png|El módulo de compresor con curva característica y evolución del nivel]]

Hay tres modos de trabajo: **CLEAN** (orientado a los picos, para la voz), **SMOOTH** (suave, orientado al valor medio) y **BUS** (para grupos y master).

| Control | Rango | Función |
|---|---|---|
| THRESHOLD | -60 a 0 dB | Nivel a partir del cual se comprime |
| RATIO | 1:1 a 100:1 | Intensidad de la compresión |
| KNEE | 0 a 24 dB | Actuación suave o dura |
| ATTACK | 0,1 a 250 ms | Tiempo de ataque |
| RELEASE | 5 ms a 2,5 s o AUTO | Tiempo de liberación. Con AUTO se adapta a las pausas del habla, y el valor ajustado no tiene efecto. |
| MAKEUP | -12 a +24 dB (AUTO solo con CLEAN) | Compensa la reducción de nivel |
| MIX | 0 a 100 % | Compresión en paralelo |
| HOLD, RANGE, DRY | 0 a 500 ms, 0 a 60 dB, desactivado a +36 dB | Ajuste fino, sin efecto con SMOOTH |

Presets de fábrica: Habla - broadcast, Habla - suave, Música - glue de bus, Música - cama densa, Ambiente - colchón, Efectos - contener picos. Para grupos y master hay presets propios. Un preset fija el modo de trabajo, el ratio, el knee, los tiempos y el mix, pero no el threshold ni el makeup.

### 9.7 BRTH: De-Breath

De-Breath baja las respiraciones entre las frases sin alterar el habla. Las respiraciones se detectan por su sonido, no solo por el volumen.

[[IMG:debreath.png|El módulo DE-BREATH con vista general y lupa]]

| Control | Rango | Valor por defecto |
|---|---|---|
| RANGE (reducción) | 0 a 24 dB | 12 dB |
| Sensibilidad | PRUDENTE, NORMAL, A FONDO | NORMAL |

Arriba, el módulo muestra toda la pista y, debajo, una lupa alrededor del cursor con la forma de onda antes y después del procesamiento. Un clic en una respiración la excluye del procesamiento o la vuelve a incluir. Con Alt+arrastrar marcas una respiración a mano. **BREATHS ONLY** reproduce solo las respiraciones. La línea de estado indica el número de respiraciones encontradas, puestas a mano y dudosas. En el modo Assist, De-Breath está activado por defecto. Actúa en la reproducción y en la exportación, pero no durante la grabación.

### 9.8 SAT: Saturate

Saturate añade una saturación de sonido analógico, parecida a la de una válvula o una cinta magnética. El módulo solo actúa en el modo Manual y está desactivado por defecto.

[[IMG:sat.png|El módulo SATURATE con curva característica y espectro]]

Como tipo eliges **TUBE** o **TAPE**, combinables en cada caso con **WARM**. Así resultan Tube, Tape, Warm Tube y Warm Tape. Controles: **DRIVE** (0 a 100), **MIX** (0 a 100), **OUTPUT** (-24 a +24 dB). Hay presets de fábrica como Clean y varias variantes de Tube y Tape.

### 9.9 REV: reverberación

La reverberación sitúa una voz en un espacio, desde la pequeña cabina de locución hasta una gran sala. Solo actúa en el modo Manual y es el último eslabón de la cadena. A partir de la reverberación, una pista de voz pasa a ser estéreo, y la cola de reverberación se incluye en la exportación.

[[IMG:rev.png|El módulo de reverberación (REVERB)]]

| Control | Rango | Valor por defecto | Función |
|---|---|---|---|
| SPACE | 0,2 a 10 s | 2,5 s | Tiempo de reverberación, tamaño de la sala |
| DECAY RATE | 0,5 a 2 | 1 | Velocidad de la extinción |
| DISTANCE | 0 a 1 | 0,5 | Distancia percibida de la voz |
| BRIGHTNESS | 0 a 1 | 0,5 | Brillante u oscuro |
| CHARACTER | 0 a 1 | 0,3 | Timbre de la sala |
| STEREO WIDTH | 0 a 1,2 | 0,7 | Anchura estéreo |
| MIX | 0 a 1 | 0,3 | Proporción de reverberación |
| PREDELAY | 0 a 500 ms | 0 | Separación entre la voz y la reverberación |

A esto se añaden el nivel de entrada y de salida, el pan y dos pestañas de EQ (DECAY EQ y **POST** EQ). Hay unos 30 presets de fábrica en los grupos Ambience, Small, Medium, Large, Very Large y Voice, por ejemplo Vocal Booth, Narrator Polish y Radio Studio.

## 10 Plug-ins y ranuras de insert

En las ranuras de insert cargas plug-ins de otros fabricantes en los formatos Audio Unit (AU, también AUv3) y VST3. No se ofrecen instrumentos. Los plug-ins solo están activos en el modo Manual. En el modo Assist las ranuras son visibles, pero no tienen efecto.

Cada pista, el grupo de voz, el grupo IT y el master tienen cinco ranuras cada uno; el channel strip CUE tiene una. Los plug-ins trabajan en orden de arriba abajo y van después de los módulos integrados.

### 10.1 Insertar un plug-in

1.  Haz clic en una ranura vacía. Se abre la selección, ordenada por fabricantes.
2.  Elige el plug-in. La ventana del plug-in se abre de inmediato.

### 10.2 Manejo en la ranura

| Manejo | Función |
|---|---|
| Clic en el nombre | Abrir la ventana del plug-in |
| Símbolo de encendido/apagado o Cmd+clic | Bypass (puentear el plug-in) |
| x al pasar el ratón por encima | Quitar el plug-in (Cmd+Z lo restaura) |
| Clic derecho | Menú con abrir editor, bypass, quitar y volver a escanear plug-ins |

Si hay una ventana de plug-in en primer plano, la app sigue pasando al transporte la barra espaciadora (Play/Stop), la tecla R (grabación) e Inicio.

### 10.3 Lista de plug-ins y nuevo escaneo

Al iniciarse, la app comprueba los plug-ins instalados. Cada plug-in se prueba en un proceso auxiliar propio. Si un plug-in falla, pasa a una lista de bloqueo y no pone en peligro la app. Tras instalar plug-ins nuevos o actualizar un plug-in, elige **Rescan plugins...** en el menú de la ranura. Así también se vacía la lista de bloqueo, y los plug-ins que ya no existen desaparecen de la lista.

El retardo (latencia) de los plug-ins se compensa automáticamente, también en los grupos y en el master.

## 11 Automatización

La automatización graba los movimientos de los controles y los reproduce en cada reproducción. Así, por ejemplo, un pasaje se vuelve más bajo automáticamente y otro más alto. La automatización está disponible en el modo Manual. En el modo Assist, el botón AUTO se muestra en gris.

### 11.1 Parámetros automatizables

- Volumen (fader) en pistas, grupo de voz, grupo IT y master
- Pan
- Mute
- **Parámetros de plug-in:** cualquier control de un plug-in que muevas durante la grabación de automatización

El channel strip CUE no tiene automatización.

### 11.2 Modos de automatización

El modo se elige con el botón de automatización del channel strip. Los nombres y el comportamiento corresponden a las DAW habituales:

| Modo | Color | Comportamiento |
|---|---|---|
| READ | gris | Reproduce la curva. El fader se puede mover de todos modos; una marca muestra el valor de la automatización. |
| TOUCH | azul claro | Solo escribe mientras se toca el control. Al soltarlo vuelve en 0,25 segundos a la curva existente. |
| LATCH | azul oscuro | Escribe desde el primer contacto y mantiene el último valor hasta STOP. |
| WRITE | rojo | Escribe de forma continua desde PLAY, también sin tocar. Tras una pasada, la pista cambia automáticamente a TOUCH. |
| TRIM (adicional) | amarillo | No escribe valores absolutos, sino una corrección de la curva existente, por ejemplo todo un ducking 2 dB más bajo. |

Automatización de mute: en **TOUCH**, la tecla de mute funciona como un pulsador y silencia mientras está pulsada. En **WRITE** se escribe desde el inicio; en **LATCH**, hasta STOP.

### 11.3 Automatización en la línea de tiempo

En la cabecera de pista cambias la vista entre forma de onda y volumen. Alt+clic cambia todas las pistas. En la vista de volumen ves la curva y puedes poner, mover y borrar puntos (seleccionarlos y pulsar Supr). También el ducking de AUTO MIX se ve aquí como curva.

Los modos de automatización se guardan con el proyecto.

## 12 Exportar

Con **EXPORT** en la barra de transporte creas los archivos de entrega: la mezcla terminada, si lo deseas la voz como archivo aparte, el vídeo con el sonido nuevo o un MXF para la emisión. Todos los archivos van a una carpeta de entrega propia; los archivos existentes no se sobrescriben.

### 12.1 Procedimiento

1.  En el modo Assist, ejecuta **AUTO MIX** ([capítulo 7](#k7)); en el modo Manual, termina la mezcla.
2.  Pulsa **EXPORT**. Se abre la ventana de exportación.
3.  En el campo **Nombre**, escribe un nombre para la entrega. Si queda vacío, se usa el nombre del proyecto.
4.  Elige qué archivos se van a crear ([secciones 12.2](#k12-2) a 12.4).
5.  Haz clic en **EXPORT** o pulsa Return. Si **Destino** está en "Preguntar en cada exportación", eliges ahora la carpeta de destino; si no, la app escribe directamente en el destino elegido.

**Destino:** en la fila **Destino** de la ventana de exportación eliges "Preguntar en cada exportación", uno de los destinos usados recientemente o **Elegir carpeta...**, por ejemplo una carpeta en un servidor. El destino se guarda en el proyecto y, con ello, también en las plantillas de sesión. Si al exportar no es accesible, por ejemplo porque la unidad del servidor no está conectada, o faltan permisos de escritura, la exportación se cancela con un mensaje en lugar de dejar los archivos en otro lugar. La ventana muestra entonces "Destino no accesible - ¿está conectado el servidor?".

En la carpeta de destino se crea una subcarpeta con el nombre de la entrega. Los archivos se llaman, por ejemplo, `Beitrag_2026-11-19_v1_mix.wav` y `Beitrag_2026-11-19_v1_voice.wav`. Con cada exportación adicional sube el número de versión (v2, v3, etc.).

### 12.2 Audio

| Fila | Contenido | Valor por defecto |
|---|---|---|
| Mezcla de audio | Mezcla terminada (estéreo) | activado, WAV 24 bits |
| Stem de voz | Solo la voz o las voces, por ejemplo para una remezcla posterior | desactivado |
| Pistas de voz por separado | Un archivo por pista de voz sin efectos; solo disponible a partir de dos pistas de voz | desactivado |
| Lista de edición para otros DAW (AES31, .adl) | Para abrir el proyecto en Pro Tools, Nuendo y otras DAW. Para ello el proyecto debe estar guardado. | desactivado |

Formatos disponibles: WAV, AIFF, AAC (.m4a), MP3, MP2 (.mp2), MP2 (.wav), FLAC y Opus.

| Ajuste | Opciones | Limitación |
|---|---|---|
| Frecuencia de muestreo | Proyecto, 44,1, 48, 88,2 o 96 kHz | MP2 y MP3 como máximo 48 kHz, Opus siempre 48 kHz |
| Profundidad de bits (WAV, AIFF, FLAC) | 16 bits con dither, 24 bits, 32 bits float | FLAC como máximo 24 bits |
| Tasa de bits (MP3, AAC, MP2, Opus) | 128, 192, 256 o 320 kbit/s | 384 kbit/s solo con MP2 |

Los archivos WAV reciben una marca de tiempo según el estándar BWF, a partir del código de tiempo inicial del proyecto.

### 12.3 Normalizar

La casilla "Normalizar a -23 LUFS (...)" lleva el archivo a la sonoridad objetivo del perfil y limita los picos con un limitador de true peak. El valor del rótulo depende del perfil. Con el perfil Studio 0 dB, en su lugar se normaliza a un nivel de pico de 0 dBTP.

- En el modo Assist ya normaliza AUTO MIX. La exportación entrega la mezcla terminada.
- En el modo Manual solo se normaliza si la casilla está marcada. Una línea de la ventana indica cuánto se desvía entonces el archivo de tu escucha.
- La casilla se aplica solo a la exportación actual.
- Además puedes elegir "Limitar el rango de sonoridad (LRA a 6 LU, multibanda)". Esta opción reduce las grandes variaciones de volumen.

### 12.4 Vídeo y MXF

En **SALIDAS** eliges **Vídeo (MOV/MP4)** o **MXF (broadcast)**. Está activa la opción que corresponde al vídeo cargado. La imagen se adopta sin cambios y se inserta el sonido nuevo.

Con MXF hay ajustes adicionales:

- **Perfil de entrega:** EBU R128, US ATSC - IT 8, Stereo, DE ARD/ZDF - HDF01a, JP ARIB - RDD9, FR CST - AS-10. Si el perfil de sonoridad del proyecto no corresponde al perfil de entrega, aparece una advertencia roja.
- **Número de pistas:** 8 o 16 pistas de audio. Los perfiles de entrega JP ARIB - RDD9 y FR CST - AS-10 solo admiten 8 pistas de audio. Con ellos, la app cambia a 8 y lo indica.
- Preajuste para las pistas de audio, por ejemplo "Mezcla 1+2, voz 7+8". En "Mis presets" están tus asignaciones guardadas.
- **Asignación de pistas:** para cada pista (T1 a T8 o T16) fijas qué lleva (mezcla L o R, voz, silencio o un canal de la fuente). La denominación de una pista es solo un nombre y no cambia su contenido.

Con **Guardar asignación como preset...** en la lista de preajustes guardas la asignación actual con un nombre. Se guardan el número de pistas y el contenido y la denominación de cada pista.

Junto al MXF se crea automáticamente una hoja de asignación (`<Nombre>_tracks.txt`) que describe la asignación real de las pistas.

### 12.5 Podcast: capítulos y datos del episodio

Para los podcasts abres la ventana Capítulos (Ventana \> Capítulos, Cmd+Shift+K):

1.  Coloca el cursor al principio del capítulo y haz clic en **Añadir en el cursor**.
2.  Escribe el título y, si quieres, una imagen y un enlace. Los capítulos sin título no se exportan.
3.  En **PROYECTO...** \> EPISODIO escribe el título, el autor, el programa, el comentario y la imagen de portada. La imagen de portada debe ser cuadrada y medir de 1400 a 3000 píxeles; las imágenes de capítulo, al menos 600 píxeles.

Al exportar, la mezcla recibe datos ID3 y capítulos. Además se crea un archivo de capítulos `<Nombre>-chapters.json` según el estándar Podcasting 2.0, junto con las imágenes de los capítulos.

### 12.6 Subtítulos y transcripción

Los subtítulos se exportan en el Script Editor de la página **AUDIO** con **TEXT EXPORT**. Puedes elegir SubRip (.srt), WebVTT (.vtt), texto sin formato (.txt) y JSON (Podcast 2.0).

## 13 Locución remota, cámara virtual y cue

En la locución remota, el locutor está en otro lugar y se conecta a través de un servicio de navegador o de videoconferencia. Para ello, voyzSESSION PRO incluye un dispositivo de audio virtual propio y una cámara virtual. El locutor ve tu imagen, oye el vídeo y la dirección y habla directamente en tu pista de grabación.

### 13.1 Configuración inicial

1.  **Instalar el controlador de audio:** en Ajustes \> Audio/vídeo..., en "Virtual audio device", haz clic en **Install**. Después reinicia la app. Se crean dos dispositivos: voyzSESSION Send (salida de la app) y voyzSESSION Return (entrada a la app).
2.  **Instalar la cámara:** en el menú de la app, elige **Instalar cámara virtual...**. Para ello la app debe estar en la carpeta Aplicaciones. macOS pide una autorización en Ajustes del Sistema \> General \> Ítems de inicio y extensiones \> Extensiones de cámara. Puede que sea necesario reiniciar. **Estado de la cámara virtual...** indica si la cámara está activa.
3.  En los ajustes de A/V, activa **Virtual camera (video to browsers)**.

En la versión 2.0, la ventana de ajustes de A/V todavía está rotulada en inglés, aunque la app esté configurada en español.

### 13.2 Realizar una sesión

1.  En el servicio de videoconferencia o de navegador (por ejemplo SessionLink PRO, Zoom o Teams), configura: micrófono = voyzSESSION Send, altavoz = voyzSESSION Return, cámara = voyzSESSION.
2.  En voyzSESSION PRO, asigna a la pista de voz la entrada voyzSESSION Return L (o R).
3.  En el mezclador, en el channel strip **CUE**, mide la latencia con **MESSEN**. La app envía un tono de prueba suave al locutor y lo busca en la ruta de retorno. El resultado se muestra en milisegundos.
4.  Graba como de costumbre ([capítulo 4](#k4)).
5.  **Después de la grabación:** clic derecho en la toma \> **Alinear por latencia del enlace**. La toma se desplaza hacia delante el retardo medido y vuelve a quedar sincronizada con la imagen.

### 13.3 Cue: lo que oye el locutor

La ruta de cue hacia el locutor contiene el sonido del vídeo y de las pistas de playout, las tomas grabadas hasta el momento y el talkback. La propia voz en directo no se devuelve, para que el locutor no se oiga con retardo.

- **TALK** en el channel strip **CUE** activa el micrófono de talkback, solo con el transporte parado. El talkback nunca se oye en tus propios altavoces.
- El fader de cue regula el volumen hacia el locutor (-48 a +6 dB). Se envía a -23 LUFS.
- En la reproducción normal, la ruta de retorno solo se oye si en la pista está activa la tecla I (escuchar la entrada). Durante la grabación se oye siempre.

### 13.4 Ventana de cabina y ventana de imagen

Para un locutor en tu propia cabina está la ventana de cabina (Ventana \> Ventana de cabina, Cmd+Shift+B). Se muestra en un monitor conectado por HDMI y, por tanto, sin retardo. A la izquierda está el prompter, a la derecha la imagen con código de tiempo; durante la grabación aparece un marco rojo. La ventana de imagen (Cmd+9 o **IMAGEN**) muestra solo la imagen, sin marco, y si lo deseas en una pantalla externa.

## 14 Control externo: Stream Deck, superficies de control, OSC

voyzSESSION PRO se puede controlar con un Elgato Stream Deck, una superficie Mackie Control o por OSC. Esto resulta útil, por ejemplo, cuando un locutor trabaja solo en la cabina.

### 14.1 Stream Deck

1.  En el menú de la app, elige **Stream Deck: instalar plug-in...**. El software de Elgato adopta el plug-in.
2.  En **Stream Deck: cargar disposición**, elige la plantilla adecuada: Stream Deck (15 teclas), Stream Deck MK.2 (15 teclas), Stream Deck Mini (6 teclas), Stream Deck XL (32 teclas) o Stream Deck + (controles giratorios).
3.  En los ajustes de A/V, activa **OSC remote control**. El plug-in se comunica con la app por OSC.

Las teclas muestran el estado de la app, por ejemplo activado/desactivado o valores actuales. Las teclas del channel strip están en el mismo orden que en el mezclador y también conmutan pistas de playout.

### 14.2 Superficie Mackie Control (MCU)

En los ajustes de A/V, en **MCU FADER CONTROLLER (MIDI)**, elige el puerto MIDI de tu superficie. La indicación **RECEIVING** muestra que llegan datos de la superficie.

| Elemento de la superficie | Función |
|---|---|
| 8 faders (sensibles al tacto) | Volumen de las pistas, como el fader de la pantalla |
| V-Pot, pulsar V-Pot | Pan, pan al centro |
| REC, SOLO, MUTE, SELECT | Por canal (REC solo en pistas de voz) |
| PLAY, STOP, RECORD | Transporte (STOP con el transporte parado salta al principio) |
| CYCLE | Loop |
| Retroceso, avance | Bobinar |
| BANK, CHANNEL | Desplazar el banco de faders 8 pistas o 1 pista |

El fader master de la superficie controla el master, y el visor de código de tiempo de la superficie avanza a la par.

### 14.3 OSC y visualizaciones en el navegador

- **OSC:** la app recibe en el puerto 8000 y devuelve los estados, por defecto a 127.0.0.1:9000 (modificable en **OSC REPLY TO**). Por OSC se puede acceder al transporte, a las funciones de pista (arm, solo, mute, modo de automatización), a la edición, los marcadores, las vistas, **AUTO MIX**, guardar, exportar y talkback.
- **Visualizaciones de consola en el navegador:** activa **Console displays (web)**, copia las direcciones con **COPY URLS** y ábrelas en una tableta o en un segundo ordenador de la misma red (puerto 8422, con clave de acceso en la dirección).

## 15 Ajustes, proyectos, guardar y recuperar

### 15.1 Ajustes > General (Cmd+,)

| Fila | Función |
|---|---|
| Idioma | Automático (idioma del sistema), Deutsch, English, Français, Español, Italiano, Português. El cambio se aplica en el próximo inicio. |
| Idioma del prompter | Idioma en el que el reconocimiento de voz sigue el texto |
| Control de nivel | "Mostrar el control de nivel al iniciar" activado o desactivado. Desactivado por defecto. |
| Consejos | "Volver a mostrar los consejos" vuelve a mostrar los avisos que solo aparecen una vez |

Directamente en el menú Ajustes está el conmutador **Fundido cruzado al solapar** (activado por defecto, consulta el [capítulo 6](#k6)).

### 15.2 Ajustes > Audio/vídeo (botón A/V...)

- **OUTPUT e INPUT:** dispositivo de salida y de entrada, que se eligen por separado, por ejemplo un micrófono USB junto con una interfaz.
- **SAMPLE RATE y BUFFER SIZE:** tamaño de búfer de 32 a 1024 samples. Un búfer pequeño reduce el retardo en los auriculares, pero aumenta la carga de cálculo. Debajo figura el retardo total medido (Round trip).
- **Direct hardware monitoring:** déjalo activado si te escuchas a través de la interfaz (valor por defecto). La escucha por software queda entonces muda, para que no te oigas por duplicado.
- **RECORDING DELAY:** desplaza las tomas nuevas unos samples, por si la interfaz las graba desplazadas.
- **Low latency monitoring:** en las pistas que se escuchan, puentea los plug-ins con un retardo demasiado alto. Estos plug-ins se marcan en naranja. La exportación no se ve afectada.
- **Además:** superficie MCU, dispositivo de audio virtual, visualizaciones en el navegador, OSC y cámara virtual ([capítulo 13](#k13) y 14).

### 15.3 Ajustes del proyecto (botón PROYECTO...)

Los cambios se aplican de inmediato.

- **AUDIO, frecuencia de muestreo:** la frecuencia de muestreo la determina el proyecto, no la interfaz. En un proyecto vacío la ajustas directamente. Si el proyecto ya contiene material, elige **Guardar copia con otra frecuencia de muestreo**. La app convierte entonces una copia; el original no cambia.
- **TIEMPO E IMAGEN:** frecuencia de imagen (23,976 a 60 fps, también drop frame), código de tiempo inicial (selección rápida 00:00:00:00 o 10:00:00:00) y **Tomar del vídeo**. Si la frecuencia de imagen del vídeo es distinta, se muestra en rojo.
- **SONORIDAD:** perfil de sonoridad y estilo de mezcla ([sección 7.1](#k7-1)).
- **EPISODIO:** datos para podcasts ([sección 12.5](#k12-5)).

### 15.4 Guardar, plantillas, recuperar

- Guardar con Cmd+S, guardar como con Cmd+Shift+S o mediante el botón **ARCHIVO**. Un proyecto es una carpeta con la extensión `.satkproj`. Las grabaciones se guardan directamente en la subcarpeta `audio` del proyecto guardado. Por eso, un proyecto nuevo debería guardarse antes de la primera grabación.
- Cmd+S durante un **AUTO MIX** queda anotado y se ejecuta después.
- **Plantillas:** **ARCHIVO** \> **Guardar el actual como plantilla...** guarda las pistas, los ajustes, los inserts, el perfil y el texto del prompter, pero no las grabaciones, el vídeo, los capítulos ni los marcadores. Los proyectos nuevos los creas después con **ARCHIVO** \> **Nuevo desde plantilla**. En la plantilla, las pistas de playout conservan su rol y su asignación a las pistas de audio del vídeo. En la siguiente importación de vídeo, la app rellena esas pistas ([sección 3.4](#k3-4)). La plantilla guarda también el destino de exportación.
- **Copia de seguridad automática:** cuando hay cambios, la app guarda cada 30 segundos un estado de recuperación. Tras un cierre inesperado, en el siguiente inicio pregunta si se debe restaurar o descartar ese estado.
- **Grabación interrumpida:** si un cierre inesperado interrumpió una grabación en curso, la próxima vez que abras el proyecto la app muestra "Se encontró una grabación interrumpida". **Restaurar** la crea como toma, **Descartar** mueve los archivos a la papelera. **Más tarde**, Esc o cerrar la ventana la dejan como está, y la app vuelve a preguntar la próxima vez que lo abras.
- **Salir:** si hay cambios sin guardar, la app pregunta si se deben guardar, descartar o cancelar. La misma pregunta aparece con Nuevo y Abrir.

## Apéndice

### A Atajos de teclado

Las teclas sin Cmd, Alt o Control no actúan mientras haya un campo de texto activo.

| Ámbito | Tecla | Función |
|---|---|---|
| Transporte | Barra espaciadora | Reproducción, parada |
| Transporte | R | Iniciar o terminar la grabación |
| Transporte | L | Activar o desactivar el loop |
| Transporte | Return, Fin, Inicio | Al principio, al final, a la posición 0 |
| Transporte | Coma, punto | 1 segundo atrás o adelante |
| Marcadores | Alt+M | Poner un marcador |
| Marcadores | 1 a 9, Shift+1 a 9 | Poner un marcador, saltar a un marcador |
| Marcadores | Alt+coma, Alt+punto | Marcador anterior o siguiente |
| Edición | Cmd+Z, Cmd+Shift+Z | Deshacer, rehacer |
| Edición | Cmd+E | Dividir |
| Edición | Cmd+C, Cmd+V, Cmd+D | Copiar, pegar, duplicar |
| Edición | Cmd+A | Seleccionar todas las tomas |
| Edición | Supr | Borrar la selección |
| Edición | M | Silenciar la toma |
| Edición | S | AutoCut |
| Edición | F | Fundido o fundido cruzado |
| Edición | I | Importar audio en la posición de reproducción |
| Edición | Cmd+flecha arriba/abajo | Mover la toma a la pista vecina; con Shift, copiarla |
| Edición | Flecha izquierda/derecha | Desplazar la selección 1 fotograma; con Shift, 1 segundo |
| Vista | Cmd+=, Cmd+Menos | Zoom |
| Vista | 0, Z | Todo el proyecto, selección |
| Vista | Control+Alt+flecha arriba/abajo | Altura de pista |
| Vista | Cmd+Alt+flecha arriba/abajo | Altura de la forma de onda |
| Mezcla | Cmd+M | AUTO MIX |
| Proyecto | Cmd+S, Cmd+Shift+S | Guardar, guardar como |
| Ventana | Cmd+, | Ajustes \> General |
| Ventana | Cmd+9 | Ventana de imagen |
| Ventana | Cmd+Shift+B | Ventana de cabina |
| Ventana | Cmd+Shift+K | Capítulos |
| Prompter | Cmd+Más, Cmd+Menos, Cmd+0 | Tamaño de letra |
| Ayuda | Cmd+Shift+/ | Manual |

### B Glosario

| Término | Significado |
|---|---|
| AUTO MIX | Mezcla automática en el modo Assist |
| Bounce | Escribir la mezcla en un archivo tal como se oye |
| Clip gain | Volumen directamente en la toma, antes del channel strip |
| Fundido cruzado (crossfade) | Transición entre dos tomas |
| Ducking | Bajada automática de la música o el ambiente mientras se habla |
| Fader | Control deslizante del volumen |
| Insert | Ranura para un plug-in en el channel strip |
| IT (mezcla internacional) | Todos los componentes excepto el locutor: sonido original, música, ambiente, efectos |
| LUFS, LU | Unidades de medida de la sonoridad percibida. -23 LUFS es la norma de televisión en Europa. |
| LRA | Rango de sonoridad, es decir, cuánto varía la sonoridad a lo largo del programa |
| Sonido original | Sonido original del vídeo, por ejemplo una entrevista |
| Pre-roll, post-roll | Tiempo previo y posterior de una grabación |
| Punch | Grabación solo en un rango definido, para sustituir un pasaje |
| Rol | Tipo de contenido de una pista (voz, música, etc.); controla el automatismo |
| Armar | Preparar una pista para la grabación |
| Stem | Componente individual de la mezcla como archivo aparte, por ejemplo solo la voz |
| Toma, región | Fragmento de audio grabado o importado en una pista |
| True peak (dBTP) | Valor de pico máximo real de la señal |

### C Solución de problemas

| Problema | Solución |
|---|---|
| El control de nivel muestra "Sin señal" | Comprueba el micrófono en el control de nivel y en A/V... \> INPUT. Comprueba además si macOS permite el acceso al micrófono (Ajustes del Sistema \> Privacidad y seguridad \> Micrófono). |
| REC no inicia ninguna grabación | Debe haber una pista armada (R). Sin pista armada, la app muestra "Ninguna pista armada". Un proyecto nuevo debe guardarse primero. |
| La propia voz se oye por duplicado o con eco | La voz llega a la vez por la interfaz y por el software. En A/V..., activa Direct hardware monitoring o desactiva el Direct Monitor en la interfaz. |
| AUTO MIX no se inicia | Desactiva el solo, termina la grabación en curso y pasa al modo Assist. Debe haber al menos una toma. |
| AUTO MIX se ilumina en azul | La mezcla guardada ya no corresponde al proyecto. Vuelve a ejecutar AUTO MIX. |
| Aviso de que la exportación recortaría (modo Manual) | Baja el fader del master o activa "Normalizar" al exportar. |
| Falta un plug-in en la lista | En el menú de la ranura, vuelve a escanear los plug-ins. Los instrumentos no se ofrecen nunca. |
| Un plug-in hace que la app se cierre inesperadamente | El plug-in pasa a la lista de bloqueo en el siguiente inicio. Tras una actualización del plug-in, vuelve a escanear. |
| El prompter no sigue la voz | Permite el reconocimiento de voz en macOS y activa el dictado. Con LANG ajusta el idioma del texto. |
| El Script Editor se queda vacío | Pulsa Transcribir. Las pistas de playout no se transcriben. |
| La cámara virtual no aparece | La app debe estar en la carpeta Aplicaciones. Autoriza la extensión en Ajustes del Sistema, reinicia el Mac si es necesario y activa la cámara en A/V... |
| Falta voyzSESSION Send o Return | Instala el controlador en A/V... y reinicia la app. |
| La frecuencia de imagen se muestra en rojo | El vídeo y el proyecto tienen frecuencias de imagen distintas. En PROYECTO..., elige "Tomar del vídeo". |
| La exportación se cancela: destino no accesible | Conecta la unidad del servidor o elige otra carpeta en la ventana de exportación, en Destino. |
| Importación AAF: archivos multimedia no encontrados | Haz clic en **Elegir carpeta...** e indica la carpeta con los medios del montaje. La app busca también en las subcarpetas. |
| La app se ha cerrado inesperadamente | En el siguiente inicio, elige la recuperación. Cuando hay cambios, la app guarda una copia cada 30 segundos. |
| Idioma de la interfaz incorrecto | Elige Ajustes \> General \> Idioma y reinicia la app. |
| La ventana de ajustes de A/V está en inglés | Esta ventana todavía no está traducida en la versión 2.0. El resto de la app sigue el idioma elegido. |
