## 1 Introdução

O voyzSESSION PRO é um software de gravação e mistura (DAW) para produções de voz: voice-over e comentário off sobre imagem, dobragem, peças de rádio, podcasts e audiolivros.

Nas produções sobre imagem, carrega um vídeo, grava o texto em sincronia com ele e exporta a mistura final como ficheiro de áudio ou diretamente no vídeo ou no MXF. As produções só de áudio, como podcast, audiolivro ou peça de rádio, dispensam o vídeo. Para elas existe a página **ÁUDIO** com o Script Editor, perfis de loudness para rádio, podcast e audiolivro, bem como formatos de exportação como MP2, MP3, FLAC e Opus.

### 1.1 Modo Assist e modo Manual

|                   | Modo Assist                                                  | Modo Manual                                           |
|-------------------|--------------------------------------------------------------|-------------------------------------------------------|
| Pensado para      | Locutores, redatores e editores sem conhecimentos de som     | Técnicos de som e engenheiros de som                  |
| Quem mistura      | A automação (AUTO MIX)                                       | O próprio utilizador, à mão como numa DAW   |
| Utilização típica | Gravação e entrega rápida                                    | Edição e mistura fina                                 |
| Resultado         | Mistura conforme a norma de loudness escolhida, com um clique | Controlo total sobre faders, plug-ins e automação     |

O que o AUTO MIX calcula no modo Assist é assumido pelo modo Manual como ponto de partida. Pode gravar em ambos os modos.

### 1.2 Requisitos do sistema

|                     | Recomendado                                            | Mínimo                                              |
|---------------------|--------------------------------------------------------|-----------------------------------------------------|
| Mac                 | Processador Apple (M1 ou mais recente)                 | Mac com Intel (funciona, mas não é recomendado)     |
| Sistema operativo   | macOS 14 Sonoma ou mais recente                        | macOS 14 Sonoma                                     |
| Memória             | 32 GB em projetos com mais de 30 minutos e vídeo 4K    | 16 GB                                               |
| Espaço em disco     | SSD                                                    | 5 GB livres, mais espaço para o material do projeto |
| Áudio               | Interface de áudio com microfone e auscultadores       | Microfone integrado ou microfone USB                |

Em Macs com Intel e com menos de 16 GB de memória, a app mostra uma única vez, no primeiro arranque, uma indicação sobre o hardware. O controlador de áudio para a gravação remota precisa do macOS 13, a câmara virtual do macOS 12.3. Ambos os requisitos são cumpridos com o macOS 14.

### 1.3 Instalação

1.  Descarregue `voyzsession-2.0.dmg` de pegelwerk.com.
2.  Abra o DMG e arraste o voyzSESSION PRO para a pasta Aplicações. A câmara virtual só funciona se a app estiver nessa pasta.
3.  Inicie a app. O macOS pede acesso ao microfone. Permita-o, caso contrário não é possível gravar.
4.  Ao abrir o prompter pela primeira vez, o macOS pede autorização para o reconhecimento de fala. Permita também este acesso, para que o texto possa seguir a sua voz.

A app anuncia novas versões com a etiqueta ATUALIZAR na barra superior.

### 1.4 Licença e período de teste

No primeiro arranque abre-se a janela «voyzSESSION PRO - Licença». Pode testar a app durante 7 dias. Uma etiqueta na barra superior mostra os dias restantes.

Para ativar a licença:

1.  Cole a chave de licença do seu e-mail no campo ou arraste o ficheiro `license.lic` para a janela. Também pode clicar na ligação de ativação do e-mail.
2.  Clique em **Ativar**.

**Comprar licença** leva à loja. Numa subscrição, o botão chama-se **Gerir subscrição**. Através da etiqueta de licença na barra superior, volta a abrir a janela em qualquer momento.

Depois de terminado o período de teste, a app continua a funcionar com limitações e emite a cada minuto um breve som de lembrete. Se uma subscrição tiver expirado, a exportação fica bloqueada.

## 2 A interface

A janela principal é composta por três áreas fixas: em cima, a barra superior; ao centro, a página de trabalho (**VÍDEO**, **ÁUDIO** ou **EDIT**); em baixo, a barra de transporte com os botões de reprodução e gravação. Entre a página de trabalho e a barra de transporte pode ser apresentada a barra de navegação.

### 2.1 Barra superior

Os elementos da esquerda para a direita:

| Elemento                   | Função                                                                                                                                         |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| FICHEIRO                   | Novo projeto, Abrir, Recentes, Guardar, Guardar como, Modelos ([capítulo 15](#k15))                                                           |
| PROJETO...                 | Definições do projeto: frequência de amostragem, taxa de fotogramas, timecode inicial, perfil, estilo de mistura                              |
| VÍDEO, ÁUDIO, EDIT, MIXER  | Mudança da página de trabalho ([secção 2.2](#k2-2))                                                                                           |
| MEDIA                      | Mostrar e ocultar o painel multimédia                                                                                                          |
| ABRIR VÍDEO                | Abrir um vídeo. Com um vídeo carregado, aparece ao lado um x para o remover. A remoção pode ser anulada.                                      |
| IMAGEM                     | Janela de vídeo ligada ou desligada (Cmd+9). Com o botão direito, coloca a imagem num ecrã externo ou mostra o timecode.                       |
| LEVEL                      | Verificação de nível do microfone                                                                                                              |
| A/V...                     | Definições de áudio e vídeo (interface, entrada e saída)                                                                                       |

Abre o manual do utilizador através do menu da app: voyzSESSION PRO \> Manual (Cmd+Shift+/). Está incluído na app e funciona sem ligação à Internet.

Durante o período de teste, uma etiqueta com a inscrição TESTE mostra os dias restantes. Quando existe uma nova versão, aparece uma etiqueta ATUALIZAR que leva à página de download.

### 2.2 Páginas de trabalho

| Página | Finalidade                                    | Conteúdo                                                                                                       |
|--------|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| VÍDEO  | Gravação sobre imagem                         | Vídeo e prompter com o texto a ler                                                                             |
| ÁUDIO  | Projetos só de áudio, por exemplo podcasts    | Script Editor com a transcrição das gravações                                                                  |
| EDIT   | Edição e arranjo                              | Timeline multipista                                                                                            |
| MIXER  | Mistura                                       | O mixer é colocado sobre a página atual. Um clique noutra página fecha-o.                                      |

### 2.3 Barra de transporte

- **À esquerda:** anular e refazer, um seletor basculante para o zoom do eixo do tempo e outro para a altura das faixas.
- **Ao centro:** \|\<\< (para o início), retroceder, **PLAY/STOP**, **REC**, **LOOP**, avançar, \>\>\| (para o fim). Um toque breve numa tecla de bobinagem salta 1 segundo; mantendo-a premida, bobina com velocidade crescente até 32 vezes a velocidade normal.
- **Contador de posição:** mostra a posição atual, a vermelho durante a gravação, a verde durante a reprodução. Depois de um clique, pode introduzir um tempo. Com o botão direito, escolhe a apresentação em timecode, minutos:segundos ou samples.
- **Grupo de gravação:** **V-PUNCH** (punch por reconhecimento de fala), **PRE** (pre-roll antes da gravação, 0 a 10 segundos) e **POST** (post-roll depois do punch-out).
- **À direita:** o comutador **ASSIST \| MANUAL**, o botão do estilo de mistura (mostra o ativo, por exemplo **REPORTAGEM** ou **TRAILER**, [secção 7.1](#k7-1)), o botão **AUTO MIX** (só no modo Assist) e **EXPORT**.

Por baixo dos botões fica uma linha de mensagens em que a app indica o processo em curso, por exemplo «A gerar o mix...». As mensagens de sucesso aparecem a verde. Se o **AUTO MIX** se acender a azul, a mistura guardada já não corresponde ao projeto e deve ser calculada de novo.

### 2.4 Barra de navegação

A barra de navegação é mostrada e ocultada através de Janela \> Barra de navegação. Mostra o projeto inteiro como forma de onda. Um clique salta para o ponto escolhido. Na página **EDIT**, uma moldura assinala o excerto visível, que pode deslocar com o rato.

À esquerda, introduz o **START**, o **FIM** e a **DURAÇÃO** do intervalo. À direita ficam os botões para marcadores: **MK +** cria um marcador, os botões **MK** com seta saltam para o marcador anterior ou seguinte, **MARKER** mostra uma lista de todos os marcadores. Um projeto pode conter até 999 marcadores.

### 2.5 Barra de menus

| Menu            | Item                                                                                                       | Atalho de teclado |
|-----------------|------------------------------------------------------------------------------------------------------------|-------------------|
| voyzSESSION PRO | Acerca do voyzSESSION PRO..., Stream Deck: instalar plug-in..., Stream Deck: carregar layout, Sair         | Cmd+Q             |
| voyzSESSION PRO | Manual | Cmd+Shift+/ |
| Ficheiro | Importar AAF... ([secção 3.5](#k3-5)) | |
| Definições      | Geral...                                                                                                   | Cmd+,             |
| Definições      | Áudio/vídeo...                                                                                             |                   |
| Definições      | Crossfade na sobreposição (lig./desl.)                                                                     |                   |
| Janela          | Janela da cabine                                                                                           | Cmd+Shift+B       |
| Janela          | Capítulos                                                                                                  | Cmd+Shift+K       |
| Janela          | Janela de vídeo                                                                                            | Cmd+9             |
| Janela          | Barra de navegação (lig./desl.)                                                                            |                   |

Novo projeto, Abrir, Guardar e Modelos estão no botão **FICHEIRO** da barra superior, não no menu Ficheiro.

## 3 Primeiros passos

Este capítulo conduz do projeto vazio até à primeira gravação.

### 3.1 Criar e guardar um projeto

1.  Escolha **FICHEIRO** \> **Novo projeto vazio**. Um projeto novo já contém uma faixa de voz.
2.  Guarde o projeto de imediato com **FICHEIRO** \> **Guardar...** (Cmd+S), de preferência num SSD com espaço suficiente.

A app grava as gravações diretamente na pasta do projeto. Num projeto ainda não guardado, ao premir **REC** pela primeira vez aparece a mensagem «A gravação precisa de uma pasta de projeto».

Se trabalha frequentemente com a mesma distribuição de faixas, crie os projetos novos através de **FICHEIRO** \> **Novo a partir de modelo** ([capítulo 15](#k15)).

### 3.2 Configurar o dispositivo de áudio

1.  Clique em **A/V...** na barra superior.
2.  Em **OUTPUT**, escolha a saída dos auscultadores ou a sua interface e, em **INPUT**, o seu microfone.
3.  Se se ouve diretamente através da interface (Direct Monitor no aparelho), deixe **Direct hardware monitoring** ligado. Sem essa possibilidade, desligue a opção. Nesse caso ouve-se através do software.

Grave sempre com auscultadores. Na reprodução por altifalantes, o som do vídeo entra no microfone.

### 3.3 Ajustar o nível do microfone (Verificação de nível)

Abre a Verificação de nível através de **LEVEL** na barra superior. Na predefinição, não aparece automaticamente no arranque.

1.  Escolha o microfone em cima.
2.  Diga algumas frases ao volume a que vai gravar mais tarde.
3.  Ajuste o pré-amplificador (gain) na interface de modo que a indicação mostre «Nível ideal».

| Indicação         | Nível de pico      | Medida                                                         |
|-------------------|--------------------|----------------------------------------------------------------|
| Sem sinal         | abaixo de -50 dBFS | Verificar o cabo, a seleção do microfone e a alimentação phantom |
| Demasiado baixo   | abaixo de -18 dBFS | Aumentar o gain na interface                                   |
| Nível ideal       | -18 a -3 dBFS      | Manter a definição                                             |
| Demasiado alto    | acima de -3 dBFS   | Reduzir o gain, caso contrário a gravação distorce             |

Na mesma janela escolhe o perfil de loudness, ou seja, a norma para a qual entrega, por exemplo EBU/ARD-ZDF ou Podcast. A opção «Não mostrar na próxima abertura» vem assinalada de fábrica. Se quiser que a Verificação de nível apareça em cada arranque, desmarque a opção ou ative-a em Definições \> Geral.

### 3.4 Carregar um vídeo

1.  Clique em **ABRIR VÍDEO** ou arraste o ficheiro para a janela.
2.  São suportados MP4, MOV, M4V e MXF. WebM não é suportado.
3.  No caso de MXF, a app cria primeiro uma cópia de reprodução (proxy). Uma barra de progresso mostra o processo. Da próxima vez que o abrir, a cópia é reutilizada.

Se o vídeo tiver mais de duas faixas de áudio, o que acontece com frequência em MXF, aparece a janela «Que faixas de áudio pretende?»:

- Assinale cada faixa necessária. Na predefinição não está selecionada nenhuma faixa.
- Com o parêntese ao lado de um par (1+2, 3+4, etc.), cria duas faixas mono como uma faixa estéreo.
- **Escolha a função de cada linha:** Auto, Pré-mix IT, Voz, Diálogo, Música, Atmo, Estádio ou Efeitos. A função controla mais tarde o AUTO MIX ([capítulo 7](#k7)).
- **Importar** aplica a seleção. Se, em vez disso, fechar a janela, toda a importação é cancelada.

Os vídeos com uma ou duas faixas de áudio são importados sem pergunta, com a função Auto.

**Com um modelo de sessão:** se o projeto contiver faixas de playout vazias de um modelo ([secção 15.4](#k15-4)), o som do vídeo vai para essas faixas. A janela aparece então pré-preenchida, com as marcas e as funções como no modelo. Uma indicação diz quantas faixas vão para as faixas já existentes do modelo. Confirma com **Importar**, para ver um número de faixas diferente no material novo antes de ter efeito. Nos vídeos com uma ou duas faixas de áudio, a app faz a atribuição sem pergunta. Só há pré-preenchimento quando o número da faixa e o formato (mono ou estéreo) correspondem ao modelo; caso contrário, são criadas faixas novas, como até aqui.

Uma sequência da edição de vídeo é importada através de um ficheiro AAF ([secção 3.5](#k3-5)).

### 3.5 Importar uma sequência da edição (AAF)

Com Ficheiro \> **Importar AAF...** traz as faixas de áudio de uma sequência da edição de vídeo para o projeto aberto, por exemplo do Avid Media Composer, do Adobe Premiere Pro ou do DaVinci Resolve. As faixas são acrescentadas, e cada clip fica na sua posição de timecode.

1.  Escolher Ficheiro \> **Importar AAF...** e abrir o ficheiro AAF.
2.  Na janela «Importar AAF», decidir se **Adotar os níveis de clip da montagem** se aplica. Na predefinição, a opção está desligada: o volume dos clips e os keyframes de nível da edição são ignorados, e o AUTO MIX trabalha com o material em bruto. Ligada, estes valores atuam além do ajuste de nível do AUTO MIX, como linha de clip gain no take.
3.  Clicar em **Importar**. A app lê a sequência e descodifica os ficheiros multimédia. Uma barra de progresso mostra o processo.
4.  Se os ficheiros multimédia não estiverem no caminho indicado no AAF, aparece «Ficheiros multimédia não encontrados». Com **Escolher pasta...**, a app procura-os numa pasta e nas suas subpastas; com **Importar sem eles**, os clips afetados ficam de fora.
5.  Verificar as funções (ver abaixo) e confirmar.

Os ficheiros multimédia podem estar incorporados no AAF ou ligados como ficheiros próprios, também como MXF OP-Atom do Avid. São importados os clips, os nomes dos clips, os fades, o pan das faixas e a automação de pan. Os pares mono que formam uma faixa estéreo na edição são combinados em faixas estéreo. Num projeto vazio, a app adota o timecode inicial da sequência. Se o projeto já contiver material, os clips são colocados segundo o timecode do projeto.

**Funções:** para que o AUTO MIX trate as faixas corretamente, cada faixa recebe uma função ([secção 7.1](#k7-1)).

- **A partir dos nomes das faixas:** se uma faixa mono se chamar, por exemplo, «Voice», «Voiceover», «Narrator», «Sprecher» ou «Kommentar», passa a ser uma faixa de voz. Nomes como «Music», «Musik», «Atmo» ou «FX» dão a função correspondente.
- **A partir do conteúdo:** para as faixas sem função no nome, a app ouve o som e propõe uma função na janela «Funções a partir do conteúdo»: Som direto, Música, Efeitos ou Ambiente. A fala é sempre proposta como Som direto, porque a faixa de voz para o texto off normalmente só é criada depois, na gravação. Verifique as propostas e altere-as se necessário. **Sem funções do conteúdo** importa estas faixas sem função.
- **Clips sem fala em faixas de fala:** se numa faixa de som direto ou de voz houver um clip sem fala, por exemplo um ruído ou som de sala, o AUTO MIX ajustaria o seu nível como se fosse fala. A app lista esses clips. Os clips assinalados vão para uma faixa própria com a função adequada. **Deixar os clips nas suas faixas** importa tudo sem alterações.

Depois da importação, um relatório resume o que foi importado e o que não foi. Não são importados, entre outros, os efeitos de clip e de faixa, as alterações de velocidade (os clips correm à velocidade original), o pan em clips individuais e as formas especiais de fade, que são substituídas pela forma padrão. Em clips com mais de dois canais, são importados os canais 1 e 2. A importação não é possível durante uma gravação nem enquanto o projeto é guardado.

### 3.6 Primeira gravação

1.  No cabeçalho da faixa de voz, clique em **R** para armar a faixa. O botão acende-se a vermelho.
2.  Prima **REC** ou a tecla R. Depois do pre-roll (**PRE**, predefinição de 4 segundos), a gravação começa.
3.  Termine a gravação com **STOP REC** ou de novo com a tecla R.
4.  Com a barra de espaços reproduz a gravação.

O [capítulo 4](#k4) descreve a gravação em pormenor, o [capítulo 7](#k7) a mistura automática e o [capítulo 12](#k12) a exportação.

## 4 Gravar

Grava-se em todas as faixas que estejam armadas. Podem estar várias faixas armadas ao mesmo tempo, e cada uma delas é audível, tal como noutras DAWs.

### 4.1 Cabeçalho da faixa

| Botão   | Nome                                 | Função                                                                                                                                         |
|---------|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| R       | Armar                                | O REC grava nesta faixa. Alt+clique atua em todas as faixas.                                                                                   |
| I       | Monitorizar a entrada (INPUT ONLY)   | Ligado: a entrada é sempre audível, também durante a reprodução e sem R. Desligado (Auto Input): com a faixa armada, a entrada só é audível com o transporte parado e durante a gravação. Só se grava com R. |
| M       | Mute                                 | Silenciar a faixa                                                                                                                              |
| S       | Solo                                 | Ouvir só esta faixa                                                                                                                            |
| AC      | AutoCut                              | Corta automaticamente a próxima gravação nas pausas                                                                                            |
| IMPORT  | Importar                             | Trazer um ficheiro de áudio para esta faixa                                                                                                    |
| Entrada | Seleção de entrada                   | Entrada da interface que vai para a faixa                                                                                                      |

O botão I só aparece em faixas de voz e só quando a monitorização por hardware está desligada.

Com **+ Voice** cria uma nova faixa de voz (mono); com **+ Audio**, uma faixa de playout (estéreo) para música, ambiente e semelhantes.

Clicando com o botão direito no cabeçalho da faixa ou através da roda dentada, acede a outros comandos: Renomear, Mover para cima/baixo, Voz de referência, combinar ou dividir estéreo, Visualização e Eliminar faixa. As faixas também podem ser deslocadas arrastando o cabeçalho. Com Cmd+clique ou Shift+clique seleciona várias faixas. A última faixa de voz não pode ser eliminada. A cor de uma faixa altera-se no mixer com um duplo clique no nome da faixa.

### 4.2 Pre-roll e post-roll

- **PRE** (pre-roll) determina durante quanto tempo o vídeo corre antes do ponto de gravação. É possível definir de 0 a 10 segundos; a predefinição é de 4 segundos. Com um duplo clique no número, introduz um valor.
- **POST** (post-roll) determina durante quanto tempo a reprodução continua depois do fim de uma gravação num intervalo.
- Durante o pre-roll, o botão faz a contagem decrescente (por exemplo «**PRE** 3.2s») e depois mostra **STOP REC**. Premir de novo cancela a gravação.
- **REC durante a reprodução** grava de imediato na posição de reprodução, sem salto e sem pre-roll (punch-in em andamento). O pre-roll só se aplica ao arrancar com o transporte parado.
- Se gravar sobre um take existente, a nova gravação substitui a parte sobreposta. O que fica antes e depois mantém-se.

### 4.3 Intervalo, loop e punch

Na parte superior da régua há uma faixa para um intervalo. Este intervalo serve tanto para o loop como para a gravação no intervalo.

- **Criar um intervalo:** arrastar na faixa vazia. Arrastar uma extremidade altera a duração, arrastar no meio desloca o intervalo, um duplo clique elimina-o. O início, o fim e a duração também podem ser introduzidos na barra de navegação.
- **LOOP** ou a tecla L repete o intervalo. Se não houver nenhum intervalo definido, a app usa o excerto visível.
- **Gravar só no intervalo (punch):** um clique com o botão direito em **REC** alterna entre «Gravar até STOP» e «Gravar no intervalo». No segundo caso, o intervalo é apresentado a cor de laranja, e a gravação começa e termina exatamente nas suas extremidades. Se premir REC durante a reprodução antes do intervalo, a gravação espera pelo seu início. Até lá, o botão mostra o tempo de espera (por exemplo «**PUNCH** 2.5s»). Dentro do intervalo, a gravação começa de imediato. Se a posição de reprodução estiver depois do intervalo ou pouco antes do seu fim, a reprodução para e a gravação arranca como a partir do transporte parado, com pre-roll.

### 4.4 Voice Punch

Com **V-PUNCH** define por voz o ponto de entrada depois de um erro de leitura:

1.  Prima **V-PUNCH**.
2.  Diga as últimas palavras corretas antes do erro.
3.  A app procura esse ponto, coloca a entrada na pausa a seguir, reproduz o pre-roll e inicia a gravação. A partir daí, volte a ler.

Com Shift+clique em **V-PUNCH**, diz também as primeiras palavras depois do erro. Assim, só a parte errada é substituída e o original continua a seguir.

Requisitos: o projeto está guardado, a página **VÍDEO** está aberta, o transporte está parado, uma faixa de voz está armada, o reconhecimento de fala do macOS está autorizado e o take já está transcrito.

### 4.5 Marcadores

| Operação                         | Função                                         |
|----------------------------------|------------------------------------------------|
| Alt+M ou MK +                    | Criar marcador na posição de reprodução        |
| 1 a 9                            | Criar marcador na posição 1 a 9                |
| Shift+1 a 9                      | Saltar para o marcador 1 a 9                   |
| Alt+vírgula, Alt+ponto           | Para o marcador anterior ou seguinte           |
| Arrastar a bandeirinha           | Deslocar o marcador                            |
| Clique na legenda                | Dar nome ao marcador                           |
| Duplo clique na bandeirinha      | Eliminar o marcador (pode ser anulado)         |

## 5 Prompter, Script Editor e janela da cabine

O prompter mostra o texto a ler durante a gravação e segue a voz. O Script Editor mostra o que foi dito como texto. Aí pode cortar áudio marcando palavras e eliminando-as.

### 5.1 Prompter (página VÍDEO)

Com **CARREGAR GUIÃO** abre um ficheiro de texto no formato .txt, .rtf ou .pdf (PDF só com camada de texto). Também pode arrastar o ficheiro para a janela ou colar o texto com Cmd+V.

Enquanto fala, o reconhecimento de fala do macOS acompanha e faz avançar a linha atual. Se fizer scroll com a roda do rato, o acompanhamento é suspenso durante 8 segundos. Se o prompter não conseguir seguir a voz, por exemplo porque falta a função de ditado, mostra uma indicação.

| Operação                              | Função                                                                                                         |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------|
| LANG                                  | Idioma do reconhecimento de fala, independente do idioma da app                                               |
| EDIT / DONE                           | Editar o texto diretamente. Entretanto, o reconhecimento de fala fica em pausa.                               |
| A- / A+, Cmd+Menos / Cmd+Mais / Cmd+0 | Tamanho da letra                                                                                               |
| Teclas de seta                        | Uma palavra para a frente ou para trás                                                                         |
| Page Up, Page Down                    | 20 palavras para a frente ou para trás                                                                         |
| Home                                  | Para o início do texto                                                                                         |
| Clique numa palavra                   | A palavra passa a ser a linha atual. Se o texto estiver associado a uma gravação, a timeline também salta.     |
| FROM TAKE                             | Cria um texto de prompter a partir da transcrição de uma gravação                                              |

### 5.2 Script Editor (página ÁUDIO)

O Script Editor mostra a transcrição de todas as faixas de voz, cada faixa na sua cor. A transcrição é feita no próprio Mac e começa automaticamente depois de uma gravação, de uma importação ou do carregamento de um projeto. As faixas de playout não são transcritas.

- **Transcrever** aparece enquanto ainda não existe texto. Se o texto faltar apenas em alguns takes, o botão chama-se **Transcrever em falta**.
- Um clique numa palavra coloca o cursor de reprodução na pausa anterior.
- **Cortar áudio:** marcar palavras arrastando e premir Delete. A app corta o áudio, coloca os cortes nas pausas mais próximas e fecha o espaço. O processo pode ser anulado num só passo.
- **Corrigir uma palavra:** duplo clique na palavra, alterar o texto, premir Return. Só o texto muda, não o áudio.
- **Remover hesitações** procura palavras de hesitação como «hã», **Pesquisa de texto** encontra pontos na transcrição.
- **TEXT EXPORT** guarda a transcrição ou legendas (SRT, VTT, TXT, JSON).

Os tempos das palavras servem para orientação. Para cortes muito precisos, convém ouvir o resultado.

### 5.3 Janela da cabine

A janela da cabine (Janela \> Janela da cabine, Cmd+Shift+B) destina-se a um monitor na cabine do locutor, ligado por HDMI. Mostra à esquerda o prompter e à direita a imagem com timecode. Durante a gravação aparece uma moldura vermelha; no pre-roll, o timecode fica vermelho. O prompter da janela da cabine corre em sincronia com o prompter da janela principal. Se estiver ligado um segundo ecrã, a janela abre-se aí em ecrã inteiro.

## 6 Editar na timeline

A página **EDIT** mostra todas as faixas numa timeline. Aqui corta, desloca e aplica fades aos takes.

### 6.1 Editar takes

A metade superior e a metade inferior de um take reagem de forma diferente:

| Zona                             | Arrastar faz                                     |
|----------------------------------|--------------------------------------------------|
| Metade inferior                  | Deslocar o take                                  |
| Metade superior                  | Marcar uma área de seleção amarela no take       |
| Extremidade esquerda ou direita  | Encurtar ou alongar o take (trim)                |
| Pega de fade no canto            | Ajustar o fade in ou o fade out                  |

- Cmd+clique acrescenta takes à seleção, Cmd+A seleciona todos os takes.
- Com a tecla Control ou Shift premida, um take arrastado só muda de faixa; a posição no tempo não se altera. Na régua aparece então «TEMPO BLOQUEADO».
- Com a tecla Alt premida, o arrastamento não se ajusta à grelha.
- Cmd+seta para cima ou para baixo desloca o take para a faixa vizinha; com Shift é criada uma cópia.
- Seta para a esquerda ou para a direita desloca a seleção um fotograma; com Shift, um segundo.

### 6.2 Cortar, eliminar, copiar

| Comando                                                        | Atalho de teclado      |
|----------------------------------------------------------------|------------------------|
| Dividir no cursor de reprodução ou cortar a área de seleção    | Cmd+E                  |
| Eliminar                                                       | Delete ou Retrocesso   |
| Copiar, colar no cursor de reprodução                          | Cmd+C, Cmd+V           |
| Duplicar                                                       | Cmd+D                  |
| Silenciar o take                                               | M                      |
| AutoCut (remover silêncio)                                     | S                      |
| Anular, refazer                                                | Cmd+Z, Cmd+Shift+Z     |

As partes divididas recebem nomes sequenciais, por exemplo «Take 3-01» e «Take 3-02». O clique com o botão direito num take oferece, entre outros: Renomear, Substituir áudio, Remover seleção, Manter só a seleção, Armar o time stretch (depois, arrastar a extremidade para esticar o take no tempo), Fade / Crossfade e Repor correção de clip gain. Um clique com o botão direito num espaço vazio oferece «Inserir áudio aqui...».

### 6.3 Fades e crossfades

- **Tecla F:** marque uma área no início ou no fim de um take e prima F. É criado um fade. Se a marcação abranger o limite entre dois takes, é criado um crossfade.
- **Sobreposição:** se um take for arrastado sobre outro, é criado automaticamente um crossfade na sobreposição. Se ficar totalmente dentro de outro take, ambas as extremidades recebem um crossfade de 50 ms. Esta função desliga-se em Definições \> Crossfade na sobreposição. O take arrastado substitui então o que está por baixo.
- A duração de um crossfade altera-se arrastando as extremidades da caixa do crossfade.

### 6.4 Clip gain

Em baixo, à esquerda, em cada take há um pequeno controlo. Arrastar para cima ou para baixo torna o take inteiro mais alto ou mais baixo; com Shift, em passos finos. Um duplo clique repõe a correção.

Na linha de clip gain do take, cria pontos com um clique, arrasta-os até ao nível pretendido e elimina-os com um duplo clique. Assim é possível tornar palavras individuais mais altas ou mais baixas. A linha do AUTO MIX e a sua própria correção ficam sobrepostas como duas camadas.

### 6.5 Zoom e visualização

| Função                       | Operação                                                                              |
|------------------------------|---------------------------------------------------------------------------------------|
| Zoom do eixo do tempo        | Seletor basculante à esquerda na barra de transporte, Cmd+= e Cmd+Menos, Cmd+roda do rato |
| Mostrar o projeto inteiro    | Tecla 0                                                                               |
| Zoom para a seleção          | Tecla Z                                                                               |
| Altura das faixas            | Segundo seletor basculante, Control+Alt+seta para cima/baixo, Alt+roda do rato        |
| Ampliar a forma de onda      | Cmd+Alt+seta para cima/baixo, Shift+Alt+roda do rato                                  |
| Para o início, para o fim    | Return, End                                                                           |
| Bobinar                      | Vírgula, ponto (1 segundo cada)                                                       |

### 6.6 Painel multimédia

**MEDIA** na barra superior abre o painel multimédia (lista de clips). Contém todo o material do projeto nos grupos IMPORTADO, SOM DO VÍDEO, GRAVAÇÕES e SEM USO.

- **IMPORT** traz ficheiros para o painel, mas ainda não para uma faixa. Os formatos possíveis são WAV, BWF, AIFF, FLAC, OGG, MP3, M4A, AAC e CAF. Os ficheiros importados mantêm o nome original.
- **Pré-escuta:** deixar o ponteiro do rato repousar brevemente sobre uma linha ou usar as teclas de seta. A barra de espaços inicia e para, Esc termina.
- **Colocar:** um duplo clique coloca o ficheiro na posição de reprodução, na faixa selecionada. Em alternativa, arraste o ficheiro para a timeline.
- As regiões aparecem indentadas por baixo do seu ficheiro. Um clique mostra a região na timeline; ao arrastar, só essa região é colocada.
- **Com o botão direito:** Importar para a faixa selecionada, Mostrar no Finder, Remover da lista de clips, Remover não utilizado.

Também se dispensa o painel: selecione a faixa e prima a tecla I. O ficheiro escolhido é inserido na posição de reprodução.

## 7 Modo Assist e AUTO MIX

No modo Assist, a app assume a mistura. O **AUTO MIX** (ou Cmd+M) trata a voz, baixa a música e o ambiente por baixo da fala e leva a mistura até à loudness do perfil escolhido. Depois do arranque, o modo Assist está ativo.

### 7.1 Preparação: perfil, estilo de mistura e funções

Em **PROJETO...** \> Perfil de loudness define para que norma entrega. O perfil determina apenas a entrega: a loudness alvo, o pico máximo permitido (true peak) e a normalização. O som da mistura é determinado pelo estilo de mistura (ver abaixo).

| Grupo     | Perfil                  | Loudness              | True peak          |
|-----------|-------------------------|-----------------------|--------------------|
| TV/Radio  | EBU/ARD-ZDF             | -23 LUFS              | -1 dBTP            |
| TV/Radio  | ATSC A/85 (EUA)         | -24 LUFS              | -2 dBTP            |
| TV/Radio  | ARIB TR-B32 (Japão)     | -24 LUFS              | -1 dBTP            |
| TV/Radio  | OP-59 (Austrália)       | -24 LUFS              | -2 dBTP            |
| TV/Radio  | CST-RT-040 (França)     | -23 LUFS              | -3 dBTP            |
| Streaming | Podcast                 | -16 LUFS              | -1 dBTP            |
| Streaming | YouTube                 | -14 LUFS              | -1 dBTP            |
| Outros    | Audiolivro              | -18 LUFS              | -3 dBTP            |
| Outros    | Studio 0 dB             | sem alvo de loudness  | pico a 0 dBTP      |

**Estilo de mistura:** determina a forma como o AUTO MIX pondera as faixas, independentemente do perfil de loudness. Escolhe-o com o botão ao lado de **AUTO MIX** na barra de transporte ou em **PROJETO...**, na linha **Estilo de mistura**. Uma mudança pode ser anulada.

| Estilo de mistura        | Botão na barra |
|--------------------------|----------------|
| Reportagem / magazine    | REPORTAGEM     |
| Trailer / promo          | TRAILER        |
| Documentário             | DOC            |
| Desporto / comentário    | DESPORTO       |
| Podcast / conversa       | PODCAST        |
| Audiolivro / radioteatro | AUDIOLIVRO     |

A predefinição é **Reportagem / magazine**. O estilo de mistura define os valores iniciais, por exemplo a que distância o fundo fica por baixo da voz. Em **Trailer / promo**, a música e os efeitos estão em primeiro plano, o locutor fica mais próximo por cima, e por baixo do locutor a música só cede na gama de frequências da voz. Os graves e os médios graves mantêm-se.

Os projetos guardados com os antigos perfis Trailer, Documentário, Desporto, Podcast ou Audiolivro abrem com o perfil de loudness e o estilo de mistura correspondentes.

Cada faixa precisa ainda de uma função. Esta indica à automação o que está na faixa. Escolhe a função através do botão de função no cabeçalho da faixa ou no mixer.

| Função                       | Abreviatura | Nível em relação ao locutor | Tratamento pela automação                                                            |
|------------------------------|-------------|-----------------------------|--------------------------------------------------------------------------------------|
| Voz                          | SPKR        | Nível de referência         | A voz é tratada e o nível é equilibrado                                              |
| Som direto                   | OT          | igualmente alto (0 LU)      | É equilibrado em relação ao locutor, cadeia de voz própria                           |
| Música                       | MUS         | 4 LU mais baixo             | É baixada por baixo do locutor e do som direto                                       |
| Efeitos                      | FX          | 4 LU mais baixo             | É baixado                                                                            |
| Ambiente                     | ATMO        | 16 LU mais baixo            | É baixado                                                                            |
| Estádio                      | STAD        | 5 LU mais baixo             | Os saltos de nível são equilibrados, mas a faixa nunca é baixada                     |
| Pré-mix IT                   | PRE         | inalterado                  | Para um pré-mix final vindo da edição, comporta-se como «Sem classificação»          |
| Sem classificação (Auto)     | AUTO        | inalterado                  | Sem tratamento                                                                       |

As faixas novas têm a função Voz. Uma faixa de playout mono passa a faixa de voz através do item de menu «Voz - converter em faixa de voz».

### 7.2 Iniciar o AUTO MIX

1.  Tem de existir pelo menos uma gravação, e o Solo não pode estar ativo.
2.  Prima **AUTO MIX** à direita na barra de transporte ou Cmd+M.
3.  Uma janela de progresso mostra os vários passos: a preparar, preparação da voz, compressão e nível, timbre da voz, fundo e ducking, loudness. Com **Cancelar** termina o processo a qualquer momento.
4.  Depois disso, reproduz com **PLAY** a mistura final.

Antes do cálculo, no modo Assist, a app coloca todos os faders do mixer em 0 dB. Isso pode ser anulado. Se já tiverem sido definidos pontos de automação próprios em faixas de playout, a app pergunta: **Recalcular**, **Manter a minha** ou **Cancelar**.

O **AUTO MIX** não arranca durante uma gravação («Não durante a gravação.»), com o Solo ativo («Desligue o **SOLO** antes do AUTO MIX.») nem no modo Manual. No modo Manual, quem normaliza é a exportação.

### 7.3 Resultado do AUTO MIX

Todas as decisões da automação podem ser vistas e alteradas:

- **Linha de clip gain da voz:** o volume da fala é equilibrado através de uma linha no take, num intervalo de até 9 dB para cima ou para baixo. A sua própria correção fica como segunda camada por cima.
- **Ducking como automação de volume:** a redução da música e do ambiente por baixo da fala está como curva na automação de volume da respetiva faixa.
- **Valores no channel strip:** o EQ, o compressor, o de-esser e os outros módulos estão preenchidos com os valores calculados. Clique com o botão direito num botão \> **Ver...** mostra o módulo bloqueado com esses valores.

A música, os efeitos, o ambiente e o som direto têm cada um a sua própria proteção de picos. Esta só atua quando o ficheiro final, de outro modo, ultrapassaria o limite de true peak do perfil. Por isso, um impacto forte na música já não baixa todo o fundo.

Se o **AUTO MIX** se acender a azul, a mistura guardada já não corresponde ao projeto, por exemplo depois de uma nova gravação ou de um corte. Prima então o botão de novo.

Os projetos da versão 1.6 precisam de um novo **AUTO MIX**, porque a cadeia de sinal mudou na versão 2.0.

### 7.4 Opções de ajuste no modo Assist

- Os faders das faixas podem ser movidos. Os faders do grupo de voz e do master estão fixos no modo Assist (indicação **FIXED**).
- Os botões do channel strip só ligam e desligam os módulos. O ajuste dos módulos fica a cargo da automação.
- Os slots de insert para plug-ins são visíveis, mas só ficam ativos no modo Manual.

Quem quiser misturar por si próprio muda com **MANUAL** para o modo Manual. A mistura do AUTO MIX é assumida na íntegra como ponto de partida ([capítulo 8](#k8)).

## 8 Modo Manual: mixer, channel strip, grupos, master

No modo Manual, mistura por si próprio, à mão como numa DAW. A app não altera nenhum fader, a monitorização reproduz sem tratamento adicional e a exportação grava no ficheiro exatamente aquilo que ouve.

### 8.1 Mudar para o modo Manual

Clique em **MANUAL** na barra de transporte. A mudança também funciona durante a reprodução e é feita com uma transição sem estalidos.

Processo habitual: gravar no modo Assist e executar o **AUTO MIX**, depois mudar para o modo Manual. O channel strip, os módulos, as linhas de nível e o ducking são assumidos tal como soaram da última vez. Em seguida, corrige os pontos que pretende de outra forma.

| Função                            | Assist                         | Manual                                                  |
|-----------------------------------|--------------------------------|---------------------------------------------------------|
| Botão AUTO MIX                    | visível                        | oculto                                                  |
| Botões no channel strip           | só lig./desl.                  | lig./desl., abre o módulo para edição                   |
| Slots de insert (plug-ins)        | visíveis, inativos             | ativos                                                  |
| Automação                         | desligada (indicação AUTO a cinzento) | Read, Touch, Latch, Write, Trim                  |
| Fader do grupo de voz e do master | fixo (indicação FIXED)         | livre                                                   |
| Saturate e reverberação           | não audíveis                   | audíveis                                                |
| Normalização                      | sempre, pelo AUTO MIX          | só com a opção «Normalizar» assinalada na janela de exportação |

Se a mistura saturar no modo Manual, um limitador na saída protege o ouvido. A app avisa então que a exportação teria clipping. Nesse caso, baixe o fader do master ou assinale a opção «Normalizar» na exportação.

### 8.2 Mixer

Abre o mixer com **MIXER** na barra superior. Cada faixa tem um channel strip com as seguintes áreas, de cima para baixo:

1.  **Botões DSP:** os nove módulos de som integrados ([capítulo 9](#k9))
2.  Entrada
3.  **Inserts:** cinco posições para plug-ins ([capítulo 10](#k10))
4.  **Sends:** cinco posições, na versão 2.0 ainda sem função
5.  **Saída:** só indicação
6.  Modo de automação ([capítulo 11](#k11))
7.  **Pan:** posição na imagem estéreo
8.  Fader com indicador de nível, intervalo de menos infinito a +12 dB. O fader usa toda a altura livre da janela.
9.  **S, M e botão de gravação:** solo, mute, prontidão para gravação
10. Função e nome

Através do menu de contexto do channel strip, mostra ou oculta áreas individuais, por exemplo os inserts ou os sends. Aí também combina duas faixas mono numa faixa estéreo ou volta a separá-las.

Ao lado do fader, uma barra ciano mostra a redução de ganho (gain reduction) do compressor, com marcas a 6 e 12 dB.

### 8.3 Botões DSP

Cada channel strip tem uma grelha de nove botões. No sentido de leitura, corresponde à ordem no percurso do sinal:

|                     |                          |                  |
|---------------------|--------------------------|------------------|
| REPR Reparação      | NR Redução de ruído      | EQ Equalizador   |
| TAME Ressonância    | DES De-esser             | CMP Compressor   |
| BRTH De-breath      | SAT Saturate             | REV Reverberação |

- Ligar abre o módulo, desligar fecha-o. Se um módulo já estiver ligado, o primeiro clique apenas abre a janela.
- **Alterar a ordem:** EQ, TAME, DES, CMP, BRTH e SAT podem ser arrastados para outra posição, tal como os inserts. Um asterisco azul indica que a ordem foi alterada. Clique com o botão direito \> Ordem padrão repõe-na. REPR e NR ficam fixos no início, REV fixo no fim. Estes botões têm um pequeno ponto.
- Um botão cinzento com a indicação «Só no Manual» só atua no modo Manual.

As faixas de playout (música, ambiente, som direto, etc.) têm a mesma grelha, com duas restrições. Com a função «Sem classificação», a maioria dos botões fica bloqueada até ser escolhida uma função. NR e BRTH ainda não existem nas faixas de playout, e o de-esser só atua com Som direto e Voz.

### 8.4 Grupos: voz e IT

Ao lado das faixas há dois channel strips de grupo. O grupo de voz reúne todas as faixas de voz, o grupo IT todas as faixas de playout (a mistura de som internacional sem locutor). Ambos os grupos têm fader, automação, inserts e uma grelha com EQ, TAME, CMP e REV, que só está ativa no modo Manual. Durante a reprodução, o fader do grupo IT mostra como o ducking está a trabalhar.

### 8.5 Master

O master é a soma que é exportada.

- Fader do master com automação.
- **PRE-GAIN** (até 24 dB para cima ou para baixo) antes do fader. É aqui que o AUTO MIX coloca o seu equilíbrio de nível, para que o fader fique em 0 dB depois da mudança para o modo Manual. Arrastar altera o valor, Shift permite passos finos, o duplo clique coloca-o em 0.
- **EQ** e **CMP** (compressor de bus), só no modo Manual.
- **Indicadores de nível:** nível de pico esquerdo e direito e loudness em LUFS como valor momentâneo, de curto prazo e integrado. O valor grande LUFS I aparece a verde quando se desvia no máximo 1 LU do alvo, a laranja até 3 LU e a vermelho acima disso.
- **LRA**: a gama de loudness, ou seja, quanto a loudness varia ao longo do programa.
- Indicação **CLIP**: acende-se depois de uma sobrecarga. Um clique no channel strip repõe-na.

O channel strip próprio **CUE** alimenta o percurso dos auscultadores (**AUSCULTADORES**) e tem uma posição de insert.

## 9 Os módulos de som

Cada um dos nove módulos de som tem uma janela própria com controlos. A apresentação no módulo baseia-se nos mesmos valores com que a monitorização e a exportação calculam.

Para todos os módulos aplica-se:

- A linha de estado mostra «Valores do AUTO MIX», «Editado (difere do **AUTO MIX**)» ou «Ainda sem AUTO MIX - a mostrar a reprodução».
- **Voltar ao AUTO MIX** repõe os valores da automação.
- No modo Assist, clique com o botão direito \> **Ver...** abre o módulo bloqueado com a indicação «Definido pelo **AUTO MIX**». O botão **Editar no Manual** muda para o modo Manual e liberta o módulo.
- **Presets:** presets de fábrica por categorias, além de «Do utilizador», «Guardar preset...» e «Mostrar pasta de presets». Os presets próprios ficam em `~/Library/SATK/Presets/`. Os presets só podem ser carregados no modo Manual.
- Cmd+Z, Cmd+S e a barra de espaços também funcionam quando uma janela de módulo está em primeiro plano.

### 9.1 REPR: Reparação (de-click e de-plosive)

O de-click remove cliques e ruídos de estalos da boca; o de-plosive atenua as plosivas em P e B abaixo de 240 Hz.

[[IMG:repr.png|O módulo REPAIR com de-click e de-plosive]]

| Controlo                   | Intervalo    | Predefinição | Função                                                       |
|----------------------------|--------------|--------------|--------------------------------------------------------------|
| SENSIBILIDADE              | 0 a 10       | 4            | Sensibilidade da deteção de cliques                          |
| INCLINAÇÃO DE FREQUÊNCIA   | -10 a +10    | 0            | Desloca a deteção para cliques graves ou agudos              |
| ALARGAMENTO DO CLIQUE      | 0 a 10 ms    | 4 ms         | Largura da zona reparada em torno de um clique               |

**SÓ CLIQUES** reproduz apenas o que foi removido. Assim, é possível verificar se está a ser removido demasiado. O de-click trabalha sem atraso. Os cliques nas pausas da fala são removidos em toda a banda de frequências. O de-plosive trabalha com definições fixas. No modo Assist, o REPR está desligado; no modo Manual, pode ser ligado.

### 9.2 NR: Redução de ruído

O NR remove ruídos de fundo constantes, como ventoinhas, zumbido ou ruído da sala. Uma rede neuronal separa a voz do ruído.

[[IMG:nr.png|O módulo NR com o controlo Intensidade]]

O módulo tem um único controlo, **INTENSIDADE** (0 a 100). Um segmento no anel liga e desliga o NR; um duplo clique coloca o valor em 100. No círculo é apresentado o espetro medido. O NR está desligado na predefinição, e o AUTO MIX também não o liga. Na versão 2.0, o NR está disponível em faixas de voz.

Valores mais altos removem mais ruído, mas podem alterar os sons de S. Ao fazer o ajuste, preste atenção aos sons de S.

### 9.3 EQ: Equalizador

O EQ altera o som de uma faixa, por exemplo para tornar uma voz mais brilhante ou mais quente, ou para baixar frequências ressonantes.

[[IMG:eq.png|O módulo EQ com analisador, bandas e controlos de dinâmica]]

O EQ tem nove bandas: corte de graves (passa-alto, 20 Hz a 1 kHz), bell 1 a 5, high shelf, corte de agudos (1 a 20 kHz, desligado na predefinição) e ar (8 kHz).

| Controlo        | Intervalo                                                  |
|-----------------|------------------------------------------------------------|
| FREQ            | Frequência em Hz                                           |
| GAIN            | -18 a +18 dB                                               |
| Q (largura)     | Bells 0,15 a 14, shelves 0,1 a 10, cortes 0,3 a 4          |

As bandas bell e shelf podem ser tornadas dinâmicas (**DYN**). A banda reage então ao nível e baixa uma frequência, por exemplo, só quando ela fica demasiado alta. Controlos: **RANGE** (-24 a +24 dB), **THRESHOLD** (-80 a 0 dB), **ATTACK** (0,1 a 500 ms), **RELEASE** (5 ms a 5 s ou AUTO).

**SOLO** na banda (ou Alt+clique num ponto de banda) reproduz apenas a gama de frequências dessa banda. Isto também funciona no modo Assist e nunca afeta a exportação. O analisador mostra o espetro antes e depois do EQ. No menu **ANALYZER** define **POST**, **PRE**+**POST** ou DESL., bem como a resolução, a velocidade, o intervalo, a inclinação e o congelamento.

### 9.4 TAME: Ressonância

O TAME deteta tons isolados incómodos, cortantes ou ressonantes e baixa-os apenas no momento em que surgem.

[[IMG:tame.png|O módulo TAME (ressonância)]]

| Controlo         | Intervalo        | Função                                       |
|------------------|------------------|----------------------------------------------|
| SOFT / HARD      |                  | Modo de trabalho suave ou forte              |
| DEPTH            | 0 a 10           | Intensidade da redução                       |
| DETAIL           | 0 a 10           | Quão finamente os tons isolados são separados |
| ATTACK, RELEASE  | 0 a 10           | Tempo de resposta e de recuperação           |
| MIX              | 0 a 100 %        | Proporção do sinal processado                |
| MAX CUT          | desligado a 24 dB | Redução máxima                              |
| OUT, WET TRIM    | -18 a +18 dB     | Nível de saída                               |

Com até oito bandas de sensibilidade (bell, shelf, corte, inclinação e outras), determina em que gamas de frequência o TAME trabalha com mais precisão. **DELTA** reproduz apenas o que foi removido. Há 16 presets de fábrica nos grupos Geral, Fala, Mix e Música.

### 9.5 DES: De-esser

O de-esser suaviza os sons agudos de S, CH e Z sem deixar a voz abafada.

[[IMG:deesser.png|O módulo DE-ESS]]

| Controlo                  | Intervalo                  | Função                                                          |
|---------------------------|----------------------------|-----------------------------------------------------------------|
| SINGLE VOCAL / ALLROUND   |                            | Voz única ou material misturado                                 |
| WIDE / SPLIT              |                            | Baixar o sinal inteiro ou só a gama de frequências agressiva    |
| THRESHOLD                 | menos infinito a 0 dB      | Limiar de atuação                                               |
| RANGE                     | 0 a 24 dB                  | Redução máxima                                                  |
| LOOKAHEAD                 | 0 a 15 ms, lig./desl.      | Atua já pouco antes do som de S                                 |
| HIGH-PASS, LOW-PASS       | 2 a 20 kHz                 | Gama de frequências a que o de-esser reage                      |

**TRIGGER** reproduz o sinal a que o de-esser reage, **REMOVIDO** o que foi removido. O AUTO MIX mede a agressividade de cada voz e ajusta o de-esser em conformidade. Há oito presets de fábrica, por exemplo para vozes masculinas e femininas.

### 9.6 CMP: Compressor

O compressor equilibra as passagens altas e baixas, para que a voz soe uniforme e presente. O módulo mostra a curva característica, o histórico de nível e a redução de ganho (a ciano).

[[IMG:comp.png|O módulo do compressor com curva característica e histórico de nível]]

Há três modos de trabalho: **CLEAN** (orientado para picos, para fala), **SMOOTH** (suave, orientado para a média) e **BUS** (para grupos e master).

| Controlo          | Intervalo                                   | Função                                                                                                          |
|-------------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| THRESHOLD         | -60 a 0 dB                                  | Nível a partir do qual há compressão                                                                            |
| RATIO             | 1:1 a 100:1                                 | Intensidade da compressão                                                                                       |
| KNEE              | 0 a 24 dB                                   | Atuação suave ou dura                                                                                           |
| ATTACK            | 0,1 a 250 ms                                | Tempo de resposta                                                                                               |
| RELEASE           | 5 ms a 2,5 s ou AUTO                        | Tempo de recuperação. Em AUTO adapta-se às pausas da fala, e o valor definido deixa de ter efeito.              |
| MAKEUP            | -12 a +24 dB (AUTO só com CLEAN)            | Compensa a redução de ganho                                                                                     |
| MIX               | 0 a 100 %                                   | Compressão paralela                                                                                             |
| HOLD, RANGE, DRY  | 0 a 500 ms, 0 a 60 dB, desligado a +36 dB   | Ajuste fino, sem efeito em SMOOTH                                                                               |

Presets de fábrica: Fala - broadcast, Fala - suave, Música - glue de bus, Música - fundo denso, Ambiente - pad, Efeitos - conter picos. Para grupos e master há presets próprios. Um preset define o modo de trabalho, o ratio, o knee, os tempos e o mix, mas não o threshold nem o makeup.

### 9.7 BRTH: De-breath

O de-breath baixa os ruídos de respiração entre as frases sem alterar a fala. As respirações são detetadas pelo som, não apenas pelo volume.

[[IMG:debreath.png|O módulo DE-BREATH com vista geral e lupa]]

| Controlo            | Intervalo                         | Predefinição |
|---------------------|-----------------------------------|--------------|
| RANGE (redução)     | 0 a 24 dB                         | 12 dB        |
| Sensibilidade       | PRUDENTE, NORMAL, COMPLETO        | NORMAL       |

Em cima, o módulo mostra a faixa inteira e, por baixo, uma lupa em torno do cursor de reprodução com a forma de onda antes e depois do processamento. Um clique numa respiração retira-a do processamento ou volta a incluí-la. Com Alt+arrastar marca uma respiração à mão. **BREATHS ONLY** reproduz apenas as respirações. A linha de estado indica o número de respirações encontradas, definidas à mão e incertas. No modo Assist, o de-breath está ligado na predefinição. Atua na reprodução e na exportação, mas não durante a gravação.

### 9.8 SAT: Saturate

O Saturate acrescenta uma saturação de som analógico, semelhante a uma válvula ou a uma fita magnética. O módulo só atua no modo Manual e está desligado na predefinição.

[[IMG:sat.png|O módulo SATURATE com curva característica e espetro]]

Como tipo, escolhe **TUBE** ou **TAPE**, cada um combinável com **WARM**. Daí resultam Tube, Tape, Warm Tube e Warm Tape. Controlos: **DRIVE** (0 a 100), **MIX** (0 a 100), **OUTPUT** (-24 a +24 dB). Há presets de fábrica como Clean e várias variantes Tube e Tape.

### 9.9 REV: Reverberação

A reverberação coloca uma voz numa sala, desde a pequena cabine de locução até ao grande salão. Só atua no modo Manual e é o último elo da cadeia. Uma faixa de voz passa a estéreo a partir da reverberação, e a cauda de reverberação está incluída na exportação.

[[IMG:rev.png|O módulo de reverberação (REVERB)]]

| Controlo       | Intervalo      | Predefinição | Função                                    |
|----------------|----------------|--------------|-------------------------------------------|
| SPACE          | 0,2 a 10 s     | 2,5 s        | Tempo de reverberação, tamanho da sala    |
| DECAY RATE     | 0,5 a 2        | 1            | Velocidade do decaimento                  |
| DISTANCE       | 0 a 1          | 0,5          | Distância percebida da voz                |
| BRIGHTNESS     | 0 a 1          | 0,5          | Brilhante ou escuro                       |
| CHARACTER      | 0 a 1          | 0,3          | Timbre da sala                            |
| STEREO WIDTH   | 0 a 1,2        | 0,7          | Largura estéreo                           |
| MIX            | 0 a 1          | 0,3          | Proporção da reverberação                 |
| PREDELAY       | 0 a 500 ms     | 0            | Intervalo entre a voz e a reverberação    |

A isto juntam-se os níveis de entrada e de saída, o pan e dois separadores de EQ (DECAY EQ e **POST** EQ). Há cerca de 30 presets de fábrica nos grupos Ambience, Small, Medium, Large, Very Large e Voice, por exemplo Vocal Booth, Narrator Polish e Radio Studio.

## 10 Plug-ins e slots de insert

Nos slots de insert carrega plug-ins de outros fabricantes nos formatos Audio Unit (AU, também AUv3) e VST3. Os instrumentos não são apresentados. Os plug-ins só estão ativos no modo Manual. No modo Assist, os slots são visíveis, mas não têm efeito.

Cada faixa, o grupo de voz, o grupo IT e o master têm cinco slots cada; o channel strip CUE tem um. Os plug-ins trabalham pela ordem de cima para baixo e vêm a seguir aos módulos integrados.

### 10.1 Inserir um plug-in

1.  Clique num slot vazio. A seleção abre-se, ordenada por fabricante.
2.  Escolha o plug-in. A janela do plug-in abre-se de imediato.

### 10.2 Operação no slot

| Operação                              | Função                                                                    |
|---------------------------------------|---------------------------------------------------------------------------|
| Clique no nome                        | Abrir a janela do plug-in                                                 |
| Símbolo lig./desl. ou Cmd+clique      | Bypass (contornar o plug-in)                                              |
| x ao passar com o rato                | Remover o plug-in (Cmd+Z repõe-no)                                        |
| Clique com o botão direito            | Menu com Open editor, Bypass, Remove e Rescan plugins...                  |

Quando uma janela de plug-in está em primeiro plano, a app continua a passar a barra de espaços (Play/Stop), a tecla R (gravação) e Home ao transporte.

### 10.3 Lista de plug-ins e nova análise

No arranque, a app verifica os plug-ins instalados. Cada plug-in é testado num processo auxiliar próprio. Se um plug-in falhar, vai para uma lista de bloqueio e não põe a app em risco. Depois de instalar novos plug-ins ou de uma atualização de plug-ins, escolha no menu do slot **Rescan plugins...**. Nesse processo, a lista de bloqueio também é esvaziada, e os plug-ins que já não existem desaparecem da lista.

O atraso (latência) dos plug-ins é compensado automaticamente, também nos grupos e no master.

## 11 Automação

A automação grava os movimentos dos controlos e reprodu-los em cada reprodução. Assim, por exemplo, um ponto fica automaticamente mais baixo e outro mais alto. A automação está disponível no modo Manual. No modo Assist, o botão AUTO aparece a cinzento.

### 11.1 Parâmetros automatizáveis

- Volume (fader) em faixas, grupo de voz, grupo IT e master
- Pan
- Mute
- **Parâmetros de plug-ins:** qualquer controlo de um plug-in que mova durante a gravação da automação

O channel strip CUE não tem automação.

### 11.2 Modos de automação

O modo escolhe-se através do botão de automação no channel strip. Os nomes e o comportamento correspondem aos das DAWs habituais:

| Modo             | Cor           | Comportamento                                                                                                                              |
|------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| READ             | cinzento      | Reproduz a curva. O fader pode mesmo assim ser movido; uma marca mostra o valor da automação.                                              |
| TOUCH            | azul-claro    | Só escreve enquanto o controlo é tocado. Depois de o largar, regressa à curva existente em 0,25 segundos.                                 |
| LATCH            | azul-escuro   | Escreve a partir do primeiro toque e mantém o último valor até STOP.                                                                       |
| WRITE            | vermelho      | Escreve continuamente a partir de PLAY, mesmo sem toque. Depois de uma passagem, a faixa muda automaticamente para TOUCH.                   |
| TRIM (adicional) | amarelo       | Não escreve valores absolutos, mas uma correção da curva existente, por exemplo um ducking inteiro 2 dB mais baixo.                         |

Automação de mute: em **TOUCH**, o botão Mute funciona como um botão momentâneo e silencia enquanto estiver premido. Em **WRITE** escreve-se a partir do início, em **LATCH** até STOP.

### 11.3 Automação na timeline

No cabeçalho da faixa alterna a visualização entre Forma de onda e Volume. Alt+clique alterna todas as faixas. Na visualização Volume vê a curva e pode criar, deslocar e eliminar pontos (selecionar e premir Delete). O ducking do AUTO MIX também está visível aqui como curva.

Os modos de automação são guardados com o projeto.

## 12 Exportação

Com **EXPORT** na barra de transporte, cria os ficheiros de entrega: a mistura final, se quiser a voz como ficheiro próprio, o vídeo com o som novo ou um MXF para emissão. Todos os ficheiros vão para uma pasta de entrega própria; os ficheiros existentes não são substituídos.

### 12.1 Processo

1.  No modo Assist, executar o **AUTO MIX** ([capítulo 7](#k7)); no modo Manual, concluir a mistura.
2.  Premir **EXPORT**. A janela de exportação abre-se.
3.  No campo **Nome**, introduzir um nome para a entrega. Se ficar vazio, é usado o nome do projeto.
4.  Escolher que ficheiros devem ser criados ([secções 12.2](#k12-2) a 12.4).
5.  Clicar em **EXPORT** ou premir Return. Se **Destino** estiver em «Perguntar em cada exportação», escolhe agora a pasta de destino; caso contrário, a app grava diretamente no destino escolhido.

**Destino:** na linha **Destino** da janela de exportação, escolhe «Perguntar em cada exportação», um dos destinos usados recentemente ou **Escolher pasta...**, por exemplo uma pasta num servidor. O destino é guardado no projeto e, por isso, também nos modelos de sessão. Se não estiver acessível na exportação, por exemplo porque a unidade do servidor não está ligada, ou se faltarem permissões de escrita, a exportação é cancelada com uma mensagem, em vez de guardar os ficheiros noutro local. A janela mostra então «Destino inacessível - o servidor está ligado?».

Na pasta de destino é criada uma subpasta com o nome da entrega. Os ficheiros chamam-se, por exemplo, `Beitrag_2026-11-19_v1_mix.wav` e `Beitrag_2026-11-19_v1_voice.wav`. A cada nova exportação, o número de versão aumenta (v2, v3, etc.).

### 12.2 Áudio

| Linha                                           | Conteúdo                                                                                                       | Predefinição       |
|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------|--------------------|
| Mix de áudio                                    | Mistura final (estéreo)                                                                                        | ligado, WAV 24 bits |
| Stem de voz                                     | Só a voz ou as vozes, por exemplo para uma nova mistura posterior                                              | desligado          |
| Faixas de voz separadas                         | Um ficheiro por faixa de voz sem efeitos, disponível só a partir de duas faixas de voz                          | desligado          |
| Lista de edição para outras DAWs (AES31, .adl)  | Para abrir o projeto no Pro Tools, no Nuendo e noutras DAWs. Para isso, o projeto tem de estar guardado.        | desligado          |

Formatos disponíveis: WAV, AIFF, AAC (.m4a), MP3, MP2 (.mp2), MP2 (.wav), FLAC e Opus.

| Definição                          | Opções                                          | Restrição                                             |
|------------------------------------|-------------------------------------------------|-------------------------------------------------------|
| Frequência de amostragem           | Projeto, 44,1, 48, 88,2 ou 96 kHz               | MP2 e MP3 no máximo 48 kHz, Opus sempre 48 kHz        |
| Profundidade de bits (WAV, AIFF, FLAC) | 16 bits com dither, 24 bits, 32 bits float  | FLAC no máximo 24 bits                                |
| Taxa de bits (MP3, AAC, MP2, Opus) | 128, 192, 256 ou 320 kbit/s                     | 384 kbit/s só em MP2                                  |

Os ficheiros WAV recebem uma marca temporal conforme a norma BWF, a partir do timecode inicial do projeto.

### 12.3 Normalizar

A opção «Normalizar para -23 LUFS (...)» leva o ficheiro até à loudness alvo do perfil e limita os picos com um limitador de true peak. O valor na legenda depende do perfil. Com o perfil Studio 0 dB, normaliza-se em vez disso para um nível de pico de 0 dBTP.

- No modo Assist, o AUTO MIX já normaliza. A exportação produz a mistura final.
- No modo Manual, só se normaliza quando a opção está assinalada. Uma linha na janela indica quanto o ficheiro se desvia então da sua monitorização.
- A opção vale apenas para a exportação atual.
- Além disso, pode escolher «Limitar a gama de loudness (LRA em 6 LU, multibanda)». Esta opção reduz grandes variações de volume.

### 12.4 Vídeo e MXF

Em **SAÍDAS** escolhe **Vídeo (MOV/MP4)** ou **MXF (broadcast)**. Está ativa a opção que corresponde ao vídeo carregado. A imagem é mantida sem alterações e o som novo é inserido.

No MXF há definições adicionais:

- **Perfil de entrega:** EBU R128, US ATSC - IT 8, Stereo, DE ARD/ZDF - HDF01a, JP ARIB - RDD9, FR CST - AS-10. Se o perfil de loudness do projeto não corresponder ao perfil de entrega, aparece um aviso vermelho.
- **Número de faixas:** 8 ou 16 faixas de áudio. Os perfis de entrega JP ARIB - RDD9 e FR CST - AS-10 só permitem 8 faixas de áudio. Com eles, a app muda para 8 e avisa.
- Predefinição para as faixas de áudio, por exemplo «Mix 1+2, voz 7+8». Em «Os meus presets» ficam as alocações que guardou.
- **Alocação de faixas:** para cada faixa (T1 a T8 ou T16) define o que está nela (mix L ou R, voz, silêncio ou um canal da fonte). A designação de uma faixa é apenas um nome e não altera o seu conteúdo.

Com **Guardar atribuição como preset...** na lista de predefinições, guarda a alocação atual com um nome. São guardados o número de faixas e o conteúdo e a designação de cada faixa.

Ao lado do MXF é criada automaticamente uma folha de alocação (`<Nome>_tracks.txt`) que descreve a alocação real das faixas.

### 12.5 Podcast: capítulos e dados do episódio

Para podcasts, abra a janela Capítulos (Janela \> Capítulos, Cmd+Shift+K):

1.  Colocar o cursor de reprodução no início do capítulo e clicar em **Adicionar no cursor**.
2.  Introduzir o título e, opcionalmente, uma imagem e uma ligação. Os capítulos sem título não são exportados.
3.  Em **PROJETO...** \> EPISÓDIO, introduzir o título, o autor, o programa, um comentário e a imagem de capa. A imagem de capa tem de ser quadrada e ter 1400 a 3000 píxeis; as imagens dos capítulos, pelo menos 600 píxeis.

Na exportação, o mix recebe dados ID3 e capítulos. Além disso, é criado um ficheiro de capítulos `<Nome>-chapters.json` conforme a norma Podcasting 2.0, incluindo as imagens dos capítulos.

### 12.6 Legendas e transcrição

As legendas exportam-se no Script Editor, na página **ÁUDIO**, com **TEXT EXPORT**. Estão disponíveis SubRip (.srt), WebVTT (.vtt), texto simples (.txt) e JSON (Podcast 2.0).

## 13 Gravação remota, câmara virtual e cue

Na gravação remota, o locutor está noutro local e está ligado através de um serviço de browser ou de videoconferência. Para isso, o voyzSESSION PRO traz um dispositivo de áudio virtual e uma câmara virtual próprios. O locutor vê a sua imagem, ouve o vídeo e a realização e fala diretamente para a sua faixa de gravação.

### 13.1 Configuração única

1.  **Instalar o controlador de áudio:** Definições \> Áudio/vídeo..., aí, em «Virtual audio device», clicar em **Install**. Depois, reiniciar a app. São criados dois dispositivos: voyzSESSION Send (saída da app) e voyzSESSION Return (entrada na app).
2.  **Instalar a câmara:** no menu da app, escolher **Instalar câmara virtual...**. Para isso, a app tem de estar na pasta Aplicações. O macOS exige uma autorização em Definições do Sistema \> Geral \> Elementos de início de sessão e extensões \> Extensões de câmara. Em certos casos é necessário reiniciar. **Estado da câmara virtual...** mostra se a câmara está ativa.
3.  Nas definições A/V, ligar **Virtual camera (video to browsers)**.

A janela de definições A/V ainda tem legendas em inglês na versão 2.0, mesmo que a app esteja definida em português.

### 13.2 Realizar uma sessão

1.  No serviço de videoconferência ou de browser (por exemplo SessionLink PRO, Zoom ou Teams), definir: microfone = voyzSESSION Send, altifalante = voyzSESSION Return, câmara = voyzSESSION.
2.  No voyzSESSION PRO, atribuir à faixa de voz a entrada voyzSESSION Return L (ou R).
3.  No mixer, no channel strip **CUE**, medir a latência com **MESSEN**. A app envia um sinal de teste baixo para o locutor e procura-o no percurso de retorno. O resultado é apresentado em milissegundos.
4.  Gravar como habitualmente ([capítulo 4](#k4)).
5.  **Depois da gravação:** clique com o botão direito no take \> **Alinhar pela latência da ligação**. O take é deslocado para a frente pelo atraso medido e fica de novo em sincronia com a imagem.

### 13.3 Cue: o que o locutor ouve

O percurso de cue para o locutor contém o som do vídeo e das faixas de playout, os takes anteriores e o talkback. A própria voz ao vivo não é devolvida, para que o locutor não se ouça com atraso.

- **TALK** no channel strip **CUE** liga o microfone de talkback, só com o transporte parado. O talkback nunca se ouve nos altifalantes próprios.
- O fader de cue regula o volume para o locutor (-48 a +6 dB). O envio é feito a -23 LUFS.
- Na reprodução normal, o retorno só é audível se o botão I (monitorizar a entrada) estiver ativo na faixa. Durante a gravação é sempre audível.

### 13.4 Janela da cabine e janela de vídeo

Para um locutor na própria cabine existe a janela da cabine (Janela \> Janela da cabine, Cmd+Shift+B). É apresentada num monitor ligado por HDMI e, por isso, sem atraso. À esquerda fica o prompter, à direita a imagem com timecode; durante a gravação aparece uma moldura vermelha. A janela de vídeo (Cmd+9 ou **IMAGEM**) mostra apenas a imagem sem moldura, se quiser num ecrã externo.

## 14 Controlo externo: Stream Deck, superfícies de controlo, OSC

O voyzSESSION PRO pode ser controlado com um Elgato Stream Deck, uma superfície Mackie Control ou por OSC. Isso é útil, por exemplo, quando um locutor trabalha sozinho na cabine.

### 14.1 Stream Deck

1.  No menu da app, escolher **Stream Deck: instalar plug-in...**. O software da Elgato assume o plug-in.
2.  Em **Stream Deck: carregar layout**, escolher o modelo adequado: Stream Deck (15 teclas), Stream Deck MK.2 (15 teclas), Stream Deck Mini (6 teclas), Stream Deck XL (32 teclas) ou Stream Deck + (controlos rotativos).
3.  Nas definições A/V, ligar **OSC remote control**. O plug-in comunica com a app por OSC.

As teclas mostram o estado da app, por exemplo ligado/desligado ou valores atuais. As teclas do channel strip estão na mesma ordem que no mixer e também comutam as faixas de playout.

### 14.2 Superfície Mackie Control (MCU)

Nas definições A/V, em **MCU FADER CONTROLLER (MIDI)**, escolha a ligação MIDI da sua superfície. A indicação **RECEIVING** mostra que estão a chegar dados da superfície.

| Elemento na superfície            | Função                                                           |
|-----------------------------------|------------------------------------------------------------------|
| 8 faders (sensíveis ao toque)     | Volume das faixas, como o fader no ecrã                          |
| V-Pot, premir o V-Pot             | Pan, pan ao centro                                               |
| REC, SOLO, MUTE, SELECT           | Por canal (REC só em faixas de voz)                              |
| PLAY, STOP, RECORD                | Transporte (STOP com o transporte parado salta para o início)    |
| CYCLE                             | Loop                                                             |
| Retroceder, avançar               | Bobinar                                                          |
| BANK, CHANNEL                     | Deslocar o banco de faders 8 ou 1 faixa                          |

O fader master da superfície controla o master, e o indicador de timecode da superfície acompanha.

### 14.3 OSC e indicadores no browser

- **OSC:** a app recebe na porta 8000 e devolve estados, na predefinição para 127.0.0.1:9000 (alterável em **OSC REPLY TO**). Por OSC são acessíveis o transporte, as funções de faixa (Arm, Solo, Mute, modo de automação), a edição, os marcadores, as visualizações, o **AUTO MIX**, guardar, a exportação e o talkback.
- **Indicadores da consola no browser:** ligar **Console displays (web)**, copiar os endereços com **COPY URLS** e abri-los num tablet ou num segundo computador na mesma rede (porta 8422, com chave de acesso no endereço).

## 15 Definições, projetos, guardar e recuperar

### 15.1 Definições > Geral (Cmd+,)

| Linha                  | Função                                                                                                                              |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Idioma                 | Automático (idioma do sistema), Deutsch, English, Français, Español, Italiano, Português. A alteração tem efeito no próximo arranque. |
| Idioma do prompter     | Idioma em que o reconhecimento de fala segue o texto                                                                                |
| Verificação de nível   | «Verificação de nível no arranque» ligada ou desligada. Desligada na predefinição.                                                  |
| Dicas                  | «Voltar a mostrar as dicas» volta a mostrar as indicações que só aparecem uma vez                                                    |

Diretamente no menu Definições está o comutador **Crossfade na sobreposição** (ligado na predefinição, ver [capítulo 6](#k6)).

### 15.2 Definições > Áudio/vídeo (botão A/V...)

- **OUTPUT e INPUT:** dispositivo de saída e de entrada, escolhidos independentemente um do outro, por exemplo um microfone USB juntamente com uma interface.
- **SAMPLE RATE e BUFFER SIZE:** tamanho do buffer de 32 a 1024 samples. Um buffer pequeno reduz o atraso nos auscultadores, mas aumenta a carga de processamento. Por baixo surge o atraso total medido (Round trip).
- **Direct hardware monitoring:** deixar ligado se se ouve através da interface (predefinição). A monitorização por software fica então muda, para que não se ouça a dobrar.
- **RECORDING DELAY:** desloca os takes novos alguns samples, caso a interface os grave desfasados.
- **Low latency monitoring:** contorna, nas faixas monitorizadas, os plug-ins com atraso demasiado elevado. Esses plug-ins são assinalados a cor de laranja. A exportação não é afetada.
- **Além disso:** superfície MCU, dispositivo de áudio virtual, indicadores no browser, OSC e câmara virtual ([capítulo 13](#k13) e 14).

### 15.3 Definições do projeto (botão PROJETO...)

As alterações têm efeito imediato.

- **ÁUDIO, frequência de amostragem:** a frequência de amostragem é determinada pelo projeto, não pela interface. Num projeto vazio, defina-a diretamente. Se o projeto já contiver material, escolha **Guardar cópia com outra frequência de amostragem**. A app converte então uma cópia, e o original fica inalterado.
- **TEMPO E IMAGEM:** taxa de fotogramas (23,976 a 60 fps, também drop-frame), timecode inicial (escolha rápida 00:00:00:00 ou 10:00:00:00) e **Copiar do vídeo**. Se a taxa de fotogramas do vídeo for diferente, é apresentada a vermelho.
- **LOUDNESS:** perfil de loudness e estilo de mistura ([secção 7.1](#k7-1)).
- **EPISÓDIO:** dados para podcasts ([secção 12.5](#k12-5)).

### 15.4 Guardar, modelos, recuperar

- Guardar com Cmd+S, Guardar como com Cmd+Shift+S ou através do botão **FICHEIRO**. Um projeto é uma pasta com a extensão `.satkproj`. As gravações são guardadas diretamente na subpasta `audio` do projeto guardado. Por isso, um projeto novo deve ser guardado antes da primeira gravação.
- Cmd+S durante um **AUTO MIX** fica em espera e é executado a seguir.
- **Modelos:** **FICHEIRO** \> **Guardar atual como modelo...** guarda as faixas, as definições, os inserts, o perfil e o texto do prompter, mas nenhuma gravação, nenhum vídeo, nenhum capítulo e nenhum marcador. Os projetos novos criam-se então com **FICHEIRO** \> **Novo a partir de modelo**. As faixas de playout mantêm no modelo a sua função e a sua atribuição às faixas de áudio do vídeo. Na importação de vídeo seguinte, a app preenche estas faixas ([secção 3.4](#k3-4)). O destino da exportação também é guardado no modelo.
- **Cópia de segurança automática:** quando há alterações, a app guarda a cada 30 segundos um estado de recuperação. Depois de uma falha, pergunta no arranque seguinte se esse estado deve ser recuperado ou descartado.
- **Gravação interrompida:** se uma gravação em curso tiver sido interrompida por uma falha, a app indica na abertura seguinte «Gravação interrompida encontrada». **Restaurar** cria-a como take, **Descartar** põe os ficheiros no Lixo. **Mais tarde**, Esc ou fechar a janela deixam-na como está, e a app pergunta de novo na abertura seguinte.
- **Sair:** se houver alterações não guardadas, a app pergunta se devem ser guardadas, descartadas ou se a ação deve ser cancelada. A mesma pergunta aparece em Novo e Abrir.

## Anexo

### A Atalhos de teclado

As teclas sem Cmd, Alt ou Control não têm efeito enquanto um campo de texto estiver ativo.

| Área       | Tecla                                 | Função                                                        |
|------------|---------------------------------------|---------------------------------------------------------------|
| Transporte | Barra de espaços                      | Reprodução, paragem                                           |
| Transporte | R                                     | Iniciar ou terminar a gravação                                |
| Transporte | L                                     | Loop ligado ou desligado                                      |
| Transporte | Return, End, Home                     | Para o início, para o fim, para a posição 0                   |
| Transporte | Vírgula, ponto                        | 1 segundo para trás ou para a frente                          |
| Marcadores | Alt+M                                 | Criar marcador                                                |
| Marcadores | 1 a 9, Shift+1 a 9                    | Criar marcador, saltar para o marcador                        |
| Marcadores | Alt+vírgula, Alt+ponto                | Marcador anterior ou seguinte                                 |
| Edição     | Cmd+Z, Cmd+Shift+Z                    | Anular, refazer                                               |
| Edição     | Cmd+E                                 | Dividir                                                       |
| Edição     | Cmd+C, Cmd+V, Cmd+D                   | Copiar, colar, duplicar                                       |
| Edição     | Cmd+A                                 | Selecionar todos os takes                                     |
| Edição     | Delete                                | Eliminar a seleção                                            |
| Edição     | M                                     | Silenciar o take                                              |
| Edição     | S                                     | AutoCut                                                       |
| Edição     | F                                     | Fade ou crossfade                                             |
| Edição     | I                                     | Importar áudio na posição de reprodução                       |
| Edição     | Cmd+seta para cima/baixo              | Deslocar o take para a faixa vizinha, com Shift copiar        |
| Edição     | Seta para a esquerda/direita          | Deslocar a seleção 1 fotograma, com Shift 1 segundo           |
| Vista      | Cmd+=, Cmd+Menos                      | Zoom                                                          |
| Vista      | 0, Z                                  | Projeto inteiro, seleção                                      |
| Vista      | Control+Alt+seta para cima/baixo      | Altura das faixas                                             |
| Vista      | Cmd+Alt+seta para cima/baixo          | Altura da forma de onda                                       |
| Mistura    | Cmd+M                                 | AUTO MIX                                                      |
| Projeto    | Cmd+S, Cmd+Shift+S                    | Guardar, Guardar como                                         |
| Janela     | Cmd+,                                 | Definições \> Geral                                           |
| Janela     | Cmd+9                                 | Janela de vídeo                                               |
| Janela     | Cmd+Shift+B                           | Janela da cabine                                              |
| Janela     | Cmd+Shift+K                           | Capítulos                                                     |
| Prompter   | Cmd+Mais, Cmd+Menos, Cmd+0            | Tamanho da letra                                              |
| Ajuda      | Cmd+Shift+/                           | Manual                                                        |

### B Glossário

| Termo                                  | Significado                                                                                 |
|----------------------------------------|---------------------------------------------------------------------------------------------|
| AUTO MIX                               | Mistura automática no modo Assist                                                           |
| Bounce                                 | Gravar a mistura num ficheiro tal como se ouve                                              |
| Clip gain                              | Volume diretamente no take, antes do channel strip                                          |
| Crossfade                              | Transição entre dois takes                                                                  |
| Ducking                                | Redução automática da música ou do ambiente enquanto se fala                                |
| Fader                                  | Controlo deslizante para o volume                                                           |
| Insert                                 | Posição para um plug-in no channel strip                                                    |
| IT (mistura de som internacional)      | Todos os componentes exceto o locutor: som direto, música, ambiente, efeitos                |
| LUFS, LU                               | Unidades de medida da loudness percebida. -23 LUFS é a norma de televisão na Europa.        |
| LRA                                    | Gama de loudness, ou seja, quanto a loudness varia ao longo do programa                     |
| Som direto                             | Som original do vídeo, por exemplo uma entrevista                                           |
| Pre-roll, post-roll                    | Avanço antes e continuação depois de uma gravação                                           |
| Punch                                  | Gravação só num intervalo definido, para substituir um trecho                               |
| Função                                 | Tipo de conteúdo de uma faixa (voz, música, etc.), controla a automação                     |
| Armar                                  | Preparar uma faixa para a gravação                                                          |
| Stem                                   | Componente individual da mistura como ficheiro próprio, por exemplo só a voz                |
| Take, região                           | Excerto de áudio gravado ou importado numa faixa                                            |
| True peak (dBTP)                       | Valor de pico máximo real do sinal                                                          |

### C Resolução de problemas

| Problema                                                       | Solução                                                                                                                                                                                         |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A Verificação de nível mostra «Sem sinal»                      | Verificar o microfone na Verificação de nível e em A/V... \> INPUT. Verificar também se o macOS permite o acesso ao microfone (Definições do Sistema \> Privacidade e segurança \> Microfone).  |
| O REC não inicia nenhuma gravação                              | Tem de haver uma faixa armada (R). Sem faixa armada, a app indica «Nenhuma faixa armada». Um projeto novo tem de ser guardado primeiro.                                                          |
| A própria voz ouve-se a dobrar ou com eco                      | A voz chega ao mesmo tempo pela interface e pelo software. Em A/V..., ligar Direct hardware monitoring ou desligar o Direct Monitor na interface.                                               |
| O AUTO MIX não arranca                                         | Desligar o Solo, terminar a gravação em curso, mudar para o modo Assist. Tem de existir pelo menos um take.                                                                                     |
| O AUTO MIX acende-se a azul                                    | A mistura guardada já não corresponde ao projeto. Executar de novo o AUTO MIX.                                                                                                                  |
| Mensagem de que a exportação teria clipping (modo Manual)      | Baixar o fader do master ou ativar «Normalizar» na exportação.                                                                                                                                  |
| Falta um plug-in na lista                                      | No menu do slot, escolher Rescan plugins... Os instrumentos nunca são apresentados.                                                                                                             |
| Um plug-in faz a app falhar                                    | O plug-in vai para a lista de bloqueio no arranque seguinte. Depois de uma atualização do plug-in, voltar a analisar.                                                                           |
| O prompter não segue a voz                                     | Permitir o reconhecimento de fala no macOS e ligar a função de ditado. Com LANG, definir o idioma do texto.                                                                                     |
| O Script Editor fica vazio                                     | Premir Transcrever. As faixas de playout não são transcritas.                                                                                                                                   |
| A câmara virtual não aparece                                   | A app tem de estar na pasta Aplicações. Autorizar a extensão nas Definições do Sistema, se necessário reiniciar o Mac e, em A/V..., ligar a câmara.                                               |
| Falta o voyzSESSION Send ou o voyzSESSION Return               | Instalar o controlador em A/V... e reiniciar a app.                                                                                                                                             |
| A taxa de fotogramas é apresentada a vermelho                  | O vídeo e o projeto têm taxas de fotogramas diferentes. Em PROJETO..., escolher «Copiar do vídeo».                                                                                              |
| A exportação é cancelada: destino inacessível                 | Ligar a unidade do servidor ou, na janela de exportação, escolher outra pasta em Destino. |
| Importação AAF: ficheiros multimédia não encontrados           | Clicar em **Escolher pasta...** e indicar a pasta com os ficheiros multimédia da edição. A app também procura nas subpastas. |
| A app falhou                                                   | No arranque seguinte, escolher a recuperação. A app guarda a cada 30 segundos quando há alterações.                                                                                             |
| Idioma errado na interface                                     | Escolher Definições \> Geral \> Idioma e reiniciar a app.                                                                                                                                       |
| A janela de definições A/V está em inglês                      | Esta janela ainda não está traduzida na versão 2.0. O resto da app segue o idioma escolhido.                                                                                                    |
