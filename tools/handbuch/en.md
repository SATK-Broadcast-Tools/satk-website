## 1 Introduction

voyzSESSION PRO is recording and mixing software (DAW) for speech productions: voice-over and off-screen commentary to picture, dubbing, radio features, podcasts and audiobooks.

For productions to picture, you load a video, record the text in sync with it and export the finished mix as an audio file or directly in the video or in the MXF. Pure audio productions such as a podcast, audiobook or radio feature work without video. For these there is the **AUDIO** page with the Script Editor, loudness profiles for radio, podcast and audiobook, and export formats such as MP2, MP3, FLAC and Opus.

### 1.1 Assist mode and Manual mode

|                   | Assist mode                                                     | Manual mode                                         |
|-------------------|-----------------------------------------------------------------|-----------------------------------------------------|
| Intended for      | Voice artists, editors and video editors without audio training | Sound engineers and audio engineers                 |
| Who mixes         | The automatic mix (AUTO MIX)                                    | You, by hand as in a DAW                       |
| Typical use       | Recording and fast delivery                                     | Editing and fine mixing                             |
| Result            | Mix to the selected loudness standard at the push of a button   | Full control over faders, plugins and automation    |

Manual mode takes what the AUTO MIX calculated in Assist mode as its starting point. You can record in both modes.

### 1.2 System requirements

|                 | Recommended                                      | Minimum                                       |
|-----------------|--------------------------------------------------|-----------------------------------------------|
| Mac             | Apple silicon (M1 or later)                      | Intel Mac (runs, but not recommended)         |
| Operating system| macOS 14 Sonoma or later                         | macOS 14 Sonoma                               |
| Memory          | 32 GB for projects over 30 minutes with 4K video | 16 GB                                         |
| Storage         | SSD                                              | 5 GB free, plus space for the project material|
| Audio           | Audio interface with microphone and headphones   | Built-in microphone or USB microphone         |

On Intel Macs and with less than 16 GB of memory, the app shows a one-time hardware notice at first launch. The audio driver for remote recording requires macOS 13, the virtual camera macOS 12.3. macOS 14 meets both.

### 1.3 Installation

1.  Download `voyzsession-2.0.dmg` from pegelwerk.com.
2.  Open the DMG and drag voyzSESSION PRO into the Applications folder. The virtual camera only works if the app is located there.
3.  Start the app. macOS asks for access to the microphone. Allow it, otherwise recording is not possible.
4.  The first time you open the prompter, macOS asks for speech recognition. Allow this as well, so that the text can follow your voice.

The app announces new versions with the UPDATE badge in the header bar.

### 1.4 License and trial period

At first launch, the "voyzSESSION PRO - License" window opens. You can test the app for 7 days. A badge in the header bar shows the remaining days.

To activate the license:

1.  Paste the license key from your email into the field or drag the `license.lic` file onto the window. You can also click the activation link in the email.
2.  Click **Activate**.

**Buy License** leads to the shop. With a subscription, the button is called **Manage subscription**. You can reopen the window at any time with the license badge in the header bar.

When the trial period has ended, the app keeps running with restrictions and plays a short reminder tone every minute. If a subscription has expired, export is locked.

## 2 The interface

The main window consists of three fixed areas: the header bar at the top, the working page (**VIDEO**, **AUDIO** or **EDIT**) in the middle and the transport bar with the playback and recording buttons at the bottom. The navigation bar can be shown between the working page and the transport bar.

### 2.1 Header bar

The elements from left to right:

| Element                   | Function                                                                                                                                  |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| FILE                      | New project, Open, Recent, Save, Save as, Templates ([Chapter 15](#k15))                                                                  |
| PROJECT...                | Project settings: sample rate, frame rate, start timecode, profile, mix style                                                            |
| VIDEO, AUDIO, EDIT, MIXER | Switch the working page ([Section 2.2](#k2-2))                                                                                            |
| MEDIA                     | Show and hide the media bin                                                                                                               |
| OPEN VIDEO                | Open a video. When a video is loaded, an x for removing it appears next to it. Removing can be undone.                                   |
| PICTURE                   | Picture window on or off (Cmd+9). With a right-click you put the picture on an external display or show the timecode.                     |
| LEVEL                     | Level Check for the microphone                                                                                                            |
| A/V...                    | Audio and video settings (interface, input and output)                                                                                    |

You open the user guide from the app menu: voyzSESSION PRO \> User Guide (Cmd+Shift+/). It is part of the app and works without an internet connection.

During the trial period, a badge labeled TRIAL shows the remaining days. When a new version is available, an UPDATE badge appears that leads to the download page.

### 2.2 Working pages

| Page  | Purpose                                     | Content                                                                                       |
|-------|---------------------------------------------|-----------------------------------------------------------------------------------------------|
| VIDEO | Recording to picture                        | Video and prompter with the script                                                            |
| AUDIO | Pure audio projects, for example podcasts   | Script Editor with the transcript of the recordings                                           |
| EDIT  | Editing and arrangement                     | Multitrack timeline                                                                           |
| MIXER | Mixing                                      | The mixing console is laid over the current page. Clicking another page closes it.            |

### 2.3 Transport bar

- **Left:** Undo and Redo, a rocker switch for zooming the time axis and one for the track height.
- **Center:** \|\<\< (to the start), Rewind, **PLAY/STOP**, **REC**, **LOOP**, Fast forward, \>\>\| (to the end). A short press on a wind button jumps 1 second; holding it winds with increasing speed up to 32 times normal speed.
- **Position counter:** shows the current position, red while recording, green during playback. After a click you can enter a time. With a right-click you choose the display in timecode, minutes:seconds or samples.
- **Record group:** **V-PUNCH** (punch by speech recognition), **PRE** (pre-roll before recording, 0 to 10 seconds) and **POST** (post-roll after the punch-out).
- **Right:** the **ASSIST \| MANUAL** switch, the button for the mix style (it shows the active one, for example **REPORT** or **TRAILER**, [Section 7.1](#k7-1)), the **AUTO MIX** button (Assist mode only) and **EXPORT**.

Below the buttons is a hint line in which the app reports the current operation, for example "Mix rendering...". Success messages appear in green. If **AUTO MIX** lights up blue, the saved mix no longer matches the project and should be recalculated.

### 2.4 Navigation bar

You show and hide the navigation bar with Window \> Navigation bar. It shows the entire project as a waveform. A click jumps to the chosen position. On the **EDIT** page, a frame marks the visible section, which you can move with the mouse.

On the left you enter **START**, **END** and **LENGTH** of the range. On the right are the marker buttons: **MK +** sets a marker, the **MK** buttons with an arrow jump to the previous or next marker, **MARKER** shows a list of all markers. A project can contain up to 999 markers.

### 2.5 Menu bar

| Menu            | Item                                                                                                       | Shortcut          |
|-----------------|------------------------------------------------------------------------------------------------------------|-------------------|
| voyzSESSION PRO | About voyzSESSION PRO..., Stream Deck: install plugin..., Stream Deck: load layout, Quit                   | Cmd+Q             |
| voyzSESSION PRO | User Guide | Cmd+Shift+/ |
| File | Import AAF... ([Section 3.5](#k3-5)) | |
| Settings        | General...                                                                                                 | Cmd+,             |
| Settings        | Audio/Video...                                                                                             |                   |
| Settings        | Crossfade on overlap (on/off)                                                                              |                   |
| Window          | Booth window                                                                                               | Cmd+Shift+B       |
| Window          | Chapters                                                                                                   | Cmd+Shift+K       |
| Window          | Picture window                                                                                             | Cmd+9             |
| Window          | Navigation bar (on/off)                                                                                    |                   |

New project, Open, Save and Templates are in the **FILE** button in the header bar, not in the File menu.

## 3 Getting started

This chapter takes you from an empty project to your first recording.

### 3.1 Creating and saving a project

1.  Choose **FILE** \> **New empty project**. A new project already contains a voice track.
2.  Save the project right away with **FILE** \> **Save...** (Cmd+S), preferably on an SSD with enough space.

The app writes recordings directly into the project folder. With a project that has not been saved yet, the first press of **REC** shows the message "Recording needs a project folder".

If you often work with the same track layout, create new projects with **FILE** \> **New from template** ([Chapter 15](#k15)).

### 3.2 Setting up the audio device

1.  Click **A/V...** in the header bar.
2.  Under **OUTPUT**, select your headphone output or your interface, and under **INPUT** your microphone.
3.  If you monitor yourself directly through the interface (direct monitor on the device), leave **Direct hardware monitoring** switched on. Without this option on your device, switch the setting off. You then hear yourself through the software.

Always record with headphones. When playing back through speakers, the sound of the video gets into the microphone.

### 3.3 Setting the microphone level (Level Check)

You open the Level Check with **LEVEL** in the header bar. By default it does not appear on its own at startup.

1.  Select the microphone at the top.
2.  Speak a few sentences at the volume at which you will record later.
3.  Set the preamp gain on the interface so that the display reports "Optimal level".

| Display         | Peak level      | Action                                                |
|-----------------|-----------------|-------------------------------------------------------|
| No signal       | below -50 dBFS  | Check cable, microphone selection and phantom power   |
| Too quiet       | below -18 dBFS  | Increase the gain on the interface                    |
| Optimal level   | -18 to -3 dBFS  | Keep the setting                                      |
| Too loud        | above -3 dBFS   | Reduce the gain, otherwise the recording distorts     |

In the same window you select the loudness profile, that is, the standard you deliver to, for example EBU/ARD-ZDF or Podcast. The box "Don't show on next launch" is checked by default. If you want the Level Check to appear at every start, uncheck the box or switch it on under Settings \> General.

### 3.4 Loading a video

1.  Click **OPEN VIDEO** or drag the file into the window.
2.  MP4, MOV, M4V and MXF are supported. WebM is not supported.
3.  For MXF, the app first creates a playback copy (proxy). A progress bar shows the operation. The next time you open the file, the copy is reused.

If the video has more than two audio tracks, which is common with MXF, the "Which audio tracks do you want?" window appears:

- Check each track you need. By default, no track is selected.
- With the bracket next to a pair (1+2, 3+4 and so on) you create two mono tracks as one stereo track.
- **Choose the role for each row:** Auto, IT premix, Voice, Dialogue, Music, Atmo, Stadium or Effects. The role later controls the AUTO MIX ([Chapter 7](#k7)).
- **Import** applies the selection. If you close the window instead, the entire import is canceled.

Videos with one or two audio tracks are taken over without asking, with the role Auto.

**With a session template:** If the project contains empty playout tracks from a template ([Section 15.4](#k15-4)), the sound of the video goes onto these tracks. The window is then preset, with checkboxes and roles as in the template. A note says how many tracks go onto the existing tracks of the template. You confirm with **Import**, so that you see a different track count in the new material before it takes effect. For videos with one or two audio tracks, the app assigns the tracks without asking. The window is only preset if track number and format (mono or stereo) match the template; otherwise new tracks are created as before.

You take over a sequence from the video edit with an AAF file ([Section 3.5](#k3-5)).

### 3.5 Importing a sequence from the edit (AAF)

With File \> **Import AAF...** you bring the audio tracks of a sequence from the video edit into the open project, for example from Avid Media Composer, Adobe Premiere Pro or DaVinci Resolve. The tracks are added, and each clip lies at its timecode position.

1.  Choose File \> **Import AAF...** and open the AAF file.
2.  In the "Import AAF" window, decide whether **Take over clip levels from the edit** applies. By default the switch is off: clip volume and level keyframes from the edit are ignored, and the AUTO MIX works with the raw material. When it is on, they act in addition to the leveling of the AUTO MIX, as a clip gain line on the take.
3.  Click **Import**. The app reads the sequence and decodes the media. A progress bar shows the operation.
4.  If media files are not at the path stated in the AAF, "Media files not found" appears. With **Choose folder...** the app searches for them in a folder and its subfolders; with **Import without them** the affected clips are missing.
5.  Check the roles (see below) and confirm.

The media can be embedded in the AAF or linked as separate files, including MXF OP-Atom from Avid. Clips, clip names, fades, track pan and pan automation are taken over. Mono pairs that form a stereo track in the edit are combined into stereo tracks. In an empty project, the app takes over the start timecode of the sequence. If the project already contains material, the clips are placed according to the timecode of the project.

**Roles:** So that the AUTO MIX treats the tracks correctly, each track gets a role ([Section 7.1](#k7-1)).

- **From the track names:** If a mono track is called, for example, "Voice", "Voiceover", "Narrator", "Sprecher" or "Kommentar", it becomes a voice track. Names such as "Music", "Atmo" or "FX" result in the matching role.
- **From the content:** For tracks without a role in their name, the app listens to the sound and suggests a role in the "Roles from the content" window: production sound, music, effects or atmosphere. Speech is always suggested as production sound, because the voice track for the narration is usually only created afterwards, during recording. Check the suggestions and change them if necessary. **Without content roles** imports these tracks without a role.
- **Clips without speech on speech tracks:** If a production sound or voice track contains a clip without speech, such as a noise or room tone, the AUTO MIX would level it like speech. The app lists such clips. Checked clips go onto a separate track with a matching role. **Leave clips on their tracks** takes over everything unchanged.

After the import, a report summarizes what was taken over and what was not. Not taken over are, among other things, clip and track effects, time warps (the clips play at original speed), pan on individual clips and special fade shapes, which are replaced by the standard shape. For clips with more than two channels, channels 1 and 2 are taken over. The import is not possible during a recording or while saving.

### 3.6 First recording

1.  In the track header of the voice track, click **R** to arm the track. The button lights up red.
2.  Press **REC** or the R key. After the pre-roll (**PRE**, default 4 seconds) the recording starts.
3.  End the recording with **STOP REC** or by pressing the R key again.
4.  Press the space bar to play back the recording.

[Chapter 4](#k4) describes recording in detail, [Chapter 7](#k7) automatic mixing and [Chapter 12](#k12) export.

## 4 Recording

Recording takes place on every track that is armed. Several tracks can be armed at the same time, and each of them is audible, as in other DAWs.

### 4.1 Track header

| Button  | Name                         | Function                                                                                                                                      |
|---------|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| R       | Arm                          | REC records on this track. Alt+click affects all tracks.                                                                                      |
| I       | Input monitoring (INPUT ONLY)| On: the input is always audible, also during playback and without R. Off (Auto Input): on an armed track, the input is only audible while stopped and during recording. Recording only happens with R. |
| M       | Mute                         | Mute the track                                                                                                                                |
| S       | Solo                         | Hear only this track                                                                                                                          |
| AC      | AutoCut                      | Automatically cuts the next recording at the pauses                                                                                           |
| IMPORT  | Import                       | Bring an audio file onto this track                                                                                                           |
| Input   | Input selection              | Input of the interface that feeds the track                                                                                                   |

The I button only appears on voice tracks and only when hardware monitoring is switched off.

With **+ Voice** you create a new voice track (mono), with **+ Audio** a playout track (stereo) for music, atmosphere and the like.

Right-clicking the track header or clicking the gear icon gives you further commands: Rename, Move up/down, Voice match, Combine into stereo or split, View and Delete track. You can also move tracks by dragging the track header. With Cmd-click or Shift-click you select several tracks. The last voice track cannot be deleted. You change the color of a track in the mixer by double-clicking the track name.

### 4.2 Pre-roll and post-roll

- **PRE** (pre-roll) determines how long the video runs before the recording point. You can set 0 to 10 seconds; the default is 4 seconds. Double-click the number to enter a value.
- **POST** (post-roll) determines how long playback continues after the end of a range recording.
- During the pre-roll, the button counts down (for example "**PRE** 3.2s"), after that it shows **STOP REC**. Pressing it again cancels the recording.
- **REC during playback** records immediately at the playback position, without a jump and without pre-roll (punch-in on the fly). The pre-roll only applies when starting from a stop.
- If you record over an existing take, the new recording replaces the overlapped part. Whatever lies before and after it is kept.

### 4.3 Range, loop and punch

At the top of the ruler is a strip for a range. This range applies to both the loop and recording in the range.

- **Creating a range:** Drag in the empty strip. Dragging an edge changes the length, dragging in the middle moves the range, a double-click deletes it. Start, end and length can also be entered in the navigation bar.
- **LOOP** or the L key repeats the range. If no range is set, the app uses the visible section.
- **Recording only in the range (punch):** A right-click on **REC** switches between "Record until STOP" and "Record in range". In the second case the range is shown in orange, and the recording starts and ends exactly at its edges. If you press REC during playback before the range, the recording waits for its start. Until then the button shows the waiting time (for example "**PUNCH** 2.5s"). Inside the range the recording starts immediately. If the playback position is behind the range or just before its end, playback stops, and the recording starts as from a stop, with pre-roll.

### 4.4 Voice Punch

With **V-PUNCH** you set the entry point after a slip of the tongue by speech:

1.  Press **V-PUNCH**.
2.  Speak the last error-free words before the slip.
3.  The app searches for this spot, sets the entry point in the pause after it, plays the pre-roll and starts recording. From there you speak again.

With Shift+click on **V-PUNCH** you additionally speak the first words after the mistake. Then only the faulty part is replaced, and the original continues after it.

Requirements: the project is saved, the **VIDEO** page is open, the transport is stopped, a voice track is armed, macOS speech recognition is allowed and the take has already been transcribed.

### 4.5 Markers

| Operation                    | Function                                     |
|------------------------------|----------------------------------------------|
| Alt+M or MK +                | Set a marker at the playback position        |
| 1 to 9                       | Set a marker in slot 1 to 9                  |
| Shift+1 to 9                 | Jump to marker 1 to 9                        |
| Alt+comma, Alt+period        | To the previous or next marker               |
| Drag the flag                | Move the marker                              |
| Click the label              | Name the marker                              |
| Double-click the flag        | Delete the marker (can be undone)            |

## 5 Prompter, Script Editor and booth window

The prompter shows the script during recording and follows the voice. The Script Editor shows what was spoken as text. There you can edit audio by selecting and deleting words.

### 5.1 Prompter (VIDEO page)

With **LOAD SCRIPT** you open a text file in .txt, .rtf or .pdf format (PDF only with a text layer). You can also drag the file into the window or paste the text with Cmd+V.

While you speak, macOS speech recognition listens and keeps the current line in step. If you scroll with the mouse wheel, following pauses for 8 seconds. If the prompter cannot follow the voice, for example because dictation is missing, it shows a notice.

| Operation                             | Function                                                                                                |
|---------------------------------------|---------------------------------------------------------------------------------------------------------|
| LANG                                  | Language of speech recognition, independent of the language of the app                                  |
| EDIT / DONE                           | Edit the text directly. Speech recognition pauses meanwhile.                                            |
| A- / A+, Cmd+Minus / Cmd+Plus / Cmd+0 | Font size                                                                                               |
| Arrow keys                            | One word forward or back                                                                                |
| Page Up, Page Down                    | 20 words forward or back                                                                                |
| Home                                  | To the start of the text                                                                                |
| Click a word                          | The word becomes the current line. If the text is linked to a recording, the timeline jumps as well.   |
| FROM TAKE                             | Creates a prompter text from the transcript of a recording                                              |

### 5.2 Script Editor (AUDIO page)

The Script Editor shows the transcript of all voice tracks, each track in its color. Transcription runs on the Mac itself and starts automatically after a recording, an import or loading a project. Playout tracks are not transcribed.

- **Transcribe** appears as long as there is no text yet. If text is missing only for individual takes, the button is called **Transcribe missing**.
- A click on a word puts the playhead in the pause before it.
- **Editing audio:** Select words by dragging and press Delete. The app cuts out the audio, places the cuts in the nearest pauses and closes the gap. The operation can be undone in one step.
- **Correcting a word:** Double-click the word, change the text, press Return. This changes only the text, not the audio.
- **Remove fillers** searches for filler words such as "uh", **Text search** finds passages in the transcript.
- **TEXT EXPORT** saves the transcript or subtitles (SRT, VTT, TXT, JSON).

The word timings are suitable for orientation. For very precise edits, you should listen to the result.

### 5.3 Booth window

The booth window (Window \> Booth window, Cmd+Shift+B) is intended for a monitor in the voice booth connected via HDMI. It shows the prompter on the left and the picture with timecode on the right. During recording a red frame appears; during the pre-roll the timecode turns red. The prompter in the booth window runs in sync with the prompter in the main window. If a second display is connected, the window opens there in full screen.

## 6 Editing in the timeline

The **EDIT** page shows all tracks in a timeline. Here you cut, move and fade the takes.

### 6.1 Editing takes

The upper and lower halves of a take respond differently:

| Area                     | Dragging                                |
|--------------------------|-----------------------------------------|
| Lower half               | Moves the take                          |
| Upper half               | Marks a yellow selection in the take    |
| Left or right edge       | Shortens or lengthens the take (trims)  |
| Fade handle at the corner| Sets a fade-in or fade-out              |

- Cmd+click adds takes to the selection, Cmd+A selects all takes.
- With the Control or Shift key held, a dragged take changes only its track; the time position stays unchanged. The ruler then shows "TIME LOCKED".
- With the Alt key held, dragging does not snap.
- Cmd+Up Arrow or Down Arrow moves the take to the neighboring track; with Shift a copy is made.
- Left Arrow or Right Arrow moves the selection by one frame, with Shift by one second.

### 6.2 Cutting, deleting, copying

| Command                                                   | Shortcut            |
|-----------------------------------------------------------|---------------------|
| Split at the playhead or cut out the selection            | Cmd+E               |
| Delete                                                    | Delete or Backspace |
| Copy, paste at the playhead                               | Cmd+C, Cmd+V        |
| Duplicate                                                 | Cmd+D               |
| Mute take                                                 | M                   |
| AutoCut (cut out silence)                                 | S                   |
| Undo, Redo                                                | Cmd+Z, Cmd+Shift+Z  |

Split pieces get consecutive names, for example "Take 3-01" and "Take 3-02". Right-clicking a take offers, among other things: Rename, Replace audio, Remove selection, Keep only selection, Arm stretching (then drag the edge to stretch the take in time), Fade / Crossfade and Reset clip gain correction. Right-clicking an empty spot offers "Insert audio here...".

### 6.3 Fades and crossfades

- **F key:** Mark a range at the start or end of a take and press F. A fade is created. If the selection spans the boundary between two takes, a crossfade is created.
- **Overlapping:** If you drag a take over another, a crossfade is created automatically over the overlap. If it lies completely inside another take, both edges get a 50 ms crossfade. You switch this function off under Settings \> Crossfade on overlap. The dragged take then overwrites the one below.
- You change the length of a crossfade by dragging the edges of the crossfade box.

### 6.4 Clip gain

At the bottom left of each take is a small control. Dragging up or down makes the whole take louder or quieter, with Shift in fine steps. A double-click resets the correction.

On the clip gain line in the take you set points with a click, drag them to the desired level and delete them with a double-click. This lets you make individual words louder or quieter. The line from the AUTO MIX and your own correction lie on top of each other as two layers.

### 6.5 Zoom and view

| Function                | Operation                                                                   |
|-------------------------|-----------------------------------------------------------------------------|
| Zoom the time axis      | Rocker switch on the left of the transport bar, Cmd+= and Cmd+Minus, Cmd+mouse wheel |
| Show the whole project  | 0 key                                                                       |
| Zoom to the selection   | Z key                                                                       |
| Track height            | Second rocker switch, Control+Alt+Up/Down Arrow, Alt+mouse wheel            |
| Enlarge the waveform    | Cmd+Alt+Up/Down Arrow, Shift+Alt+mouse wheel                                |
| To the start, to the end| Return, End                                                                 |
| Wind                    | Comma, period (1 second each)                                               |

### 6.6 Media bin

**MEDIA** in the header bar opens the media bin (clip list). It contains all the material of the project in the groups IMPORTED, VIDEO SOUND, RECORDINGS and UNUSED.

- **IMPORT** brings files into the bin, but not yet onto a track. Possible formats are WAV, BWF, AIFF, FLAC, OGG, MP3, M4A, AAC and CAF. Imported files keep their original name.
- **Previewing:** Rest the mouse pointer on a row for a moment or use the arrow keys. The space bar starts and stops, Esc ends.
- **Placing:** A double-click puts the file on the selected track at the playback position. Alternatively, drag the file into the timeline.
- Regions are listed indented under their file. A click shows the region in the timeline; when dragging, only this region is placed.
- **Right-click:** Import to the selected track, Show in Finder, Remove from clip list, Remove unused.

It also works without the bin: select a track and press the I key. The chosen file is inserted at the playback position.

## 7 Assist mode and AUTO MIX

In Assist mode, the app takes care of the mix. **AUTO MIX** (or Cmd+M) processes the voice, lowers music and atmosphere under the speech and brings the mix to the loudness of the selected profile. After launch, Assist mode is active.

### 7.1 Preparation: profile, mix style and roles

Under **PROJECT...** \> Loudness profile you specify which standard you deliver to. The profile only determines the delivery: the target loudness, the highest permitted peak (true peak) and the normalization. How the mix sounds is determined by the mix style (see below).

| Group     | Profile                 | Loudness           | True peak         |
|-----------|-------------------------|--------------------|-------------------|
| TV/Radio  | EBU/ARD-ZDF             | -23 LUFS           | -1 dBTP           |
| TV/Radio  | ATSC A/85 (USA)         | -24 LUFS           | -2 dBTP           |
| TV/Radio  | ARIB TR-B32 (Japan)     | -24 LUFS           | -1 dBTP           |
| TV/Radio  | OP-59 (Australia)       | -24 LUFS           | -2 dBTP           |
| TV/Radio  | CST-RT-040 (France)     | -23 LUFS           | -3 dBTP           |
| Streaming | Podcast                 | -16 LUFS           | -1 dBTP           |
| Streaming | YouTube                 | -14 LUFS           | -1 dBTP           |
| Other     | Audiobook               | -18 LUFS           | -3 dBTP           |
| Other     | Studio 0 dB             | no loudness target | peak at 0 dBTP    |

**Mix style:** It specifies how AUTO MIX weights the tracks, independently of the loudness profile. You choose it with the button next to **AUTO MIX** in the transport bar or under **PROJECT...** in the **Mix style** row. A change can be undone.

| Mix style               | Bar button |
|-------------------------|------------|
| Report / magazine       | REPORT     |
| Trailer / promo         | TRAILER    |
| Documentary             | DOCU       |
| Sports / commentary     | SPORTS     |
| Podcast / talk          | PODCAST    |
| Audiobook / radio drama | AUDIOBOOK  |

The default is **Report / magazine**. The mix style sets the starting values, for example how far the bed sits below the voice. With **Trailer / promo**, music and effects lead, the voice sits closer on top, and under the voice the music only gives way in the voice's frequency range. Bass and low mids stay in place.

Projects saved with the earlier profiles Trailer, Documentary, Sports, Podcast or Audiobook open with the matching loudness profile and the matching mix style.

Each track also needs a role. It tells the automatic mix what is on the track. You choose the role with the role button in the track header or in the mixer.

| Role                     | Abbreviation | Level relative to the voice      | Processing by the automatic mix                                                    |
|--------------------------|--------------|----------------------------------|------------------------------------------------------------------------------------|
| Voice                    | SPKR         | Reference level                  | The voice is processed and leveled                                                 |
| Production sound         | OT           | equally loud (0 LU)              | Leveled against the voice, own voice chain                                         |
| Music                    | MUS          | 4 LU quieter                     | Lowered under voice and production sound                                           |
| Effects                  | FX           | 4 LU quieter                     | Lowered                                                                            |
| Atmosphere               | ATMO         | 16 LU quieter                    | Lowered                                                                            |
| Stadium                  | STAD         | 5 LU quieter                     | Level jumps are evened out, but the track is never lowered                         |
| IT premix                | PRE          | unchanged                        | For a finished premix from the edit, behaves like "Unclassified"                   |
| Unclassified (Auto)      | AUTO         | unchanged                        | No processing                                                                      |

New tracks have the role Voice. A mono playout track becomes a voice track with the menu item "Voice - make this a voice track".

### 7.2 Starting the AUTO MIX

1.  At least one recording must exist, and Solo must not be active.
2.  Press **AUTO MIX** on the right of the transport bar or Cmd+M.
3.  A progress window shows the individual steps: preparing, voice prep, compression & level, voice tone, bed & ducking, loudness. With **Cancel** you end the operation at any time.
4.  Then play the finished mix with **PLAY**.

Before the calculation, the app sets all faders of the mixing console to 0 dB in Assist mode. This can be undone. If your own automation points have already been set on playout tracks, the app asks: **Recalculate**, **Keep mine** or **Cancel**.

**AUTO MIX** does not start during a recording ("Not while recording."), with Solo active ("Turn **SOLO** off before AUTO MIX.") or in Manual mode. In Manual mode, the export normalizes instead.

### 7.3 Result of the AUTO MIX

All decisions of the automatic mix can be viewed and changed:

- **Clip gain line of the voice:** The volume of the speech is evened out with a line on the take, within a range of up to 9 dB up or down. Your own correction lies above it as a second layer.
- **Ducking as volume automation:** The lowering of music and atmosphere under the speech is a curve in the volume automation of the respective track.
- **Values in the channel strip:** EQ, compressor, de-esser and the other modules are set to the calculated values. Right-click a button \> **View...** shows the module locked with these values.

Music, effects, atmosphere and production sound each have their own peak protection. It only engages if the finished file would otherwise exceed the true peak limit of the profile. A loud hit in the music therefore no longer pushes down the whole bed.

If **AUTO MIX** lights up blue, the saved mix no longer matches the project, for example after a new recording or an edit. Then press the button again.

Projects from version 1.6 need a new **AUTO MIX** because the signal chain changed in version 2.0.

### 7.4 Settings in Assist mode

- The track faders can be moved. The faders of the Voice group and the master are fixed in Assist mode (display **FIXED**).
- The buttons in the channel strip only switch modules on and off. The automatic mix takes care of the module settings.
- Insert slots for plugins are visible, but only active in Manual mode.

If you want to mix yourself, switch to Manual mode with **MANUAL**. The AUTO MIX mix is taken over completely as the starting point ([Chapter 8](#k8)).

## 8 Manual mode: mixer, channel strip, groups, master

In Manual mode you mix yourself, by hand as in a DAW. The app does not change any faders, monitoring plays without additional processing, and the export writes exactly what you hear into the file.

### 8.1 Switching to Manual mode

Click **MANUAL** in the transport bar. The switch also works during playback and is crossfaded without clicks.

The usual workflow: record in Assist mode and run **AUTO MIX**, then switch to Manual mode. Channel strip, modules, level lines and ducking are taken over exactly as they last sounded. Afterwards you correct the passages you want to be different.

| Function                      | Assist                       | Manual                                                 |
|-------------------------------|------------------------------|--------------------------------------------------------|
| AUTO MIX button               | visible                      | hidden                                                 |
| Buttons in the channel strip  | on/off only                  | on/off, opens the module for editing                   |
| Insert slots (plugins)        | visible, inactive            | active                                                 |
| Automation                    | off (AUTO display in gray)   | Read, Touch, Latch, Write, Trim                        |
| Voice group and master faders | fixed (FIXED display)        | free                                                   |
| Saturate and reverb           | not audible                  | audible                                                |
| Normalization                 | always, by the AUTO MIX      | only with the "Normalise" checkbox in the export window|

If the mix clips in Manual mode, a limiter on the output protects your hearing. The app then reports that the export would clip. In that case, pull down the master fader or check "Normalise" when exporting.

### 8.2 Mixer

You open the mixer with **MIXER** in the header bar. Each track has a channel strip with the following sections, from top to bottom:

1.  **DSP buttons:** the nine built-in sound modules ([Chapter 9](#k9))
2.  Input
3.  **Inserts:** five slots for plugins ([Chapter 10](#k10))
4.  **Sends:** five slots, not yet functional in version 2.0
5.  **Output:** display only
6.  Automation mode ([Chapter 11](#k11))
7.  **Pan:** position in the stereo image
8.  Fader with level meter, range minus infinity to +12 dB. The fader uses the full free height of the window.
9.  **S, M and record button:** solo, mute, record enable
10. Role and name

With the context menu of the channel strip you show or hide individual sections, for example Inserts or Sends. There you also combine two mono tracks into one stereo track or split them again.

Next to the fader, a cyan bar shows the gain reduction of the compressor, with marks at 6 and 12 dB.

### 8.3 DSP buttons

Each channel strip has a grid of nine buttons. In reading order, it corresponds to the order in the signal path:

|                    |                       |                |
|--------------------|-----------------------|----------------|
| REPR Repair        | NR Noise reduction    | EQ Equalizer   |
| TAME Resonance     | DES De-esser          | CMP Compressor |
| BRTH De-breath     | SAT Saturate          | REV Reverb     |

- Switching on opens the module, switching off closes it. If a module is already switched on, the first click only opens the window.
- **Changing the order:** EQ, TAME, DES, CMP, BRTH and SAT can be dragged to another position like inserts. A blue asterisk indicates that the order has been changed. Right-click \> Standard order restores it. REPR and NR are fixed at the start, REV fixed at the end. These buttons carry a small dot.
- A gray button with the hint "Manual mode only" only takes effect in Manual mode.

Playout tracks (music, atmosphere, production sound and so on) have the same grid, with two restrictions. With the role "Unclassified", most buttons are locked until a role is chosen. NR and BRTH are not yet available on playout tracks, and the de-esser only works with production sound and voice.

### 8.4 Groups: Voice and IT

Next to the tracks are two group channel strips. The Voice group combines all voice tracks, the IT group all playout tracks (the international sound mix without the voice). Both groups have faders, automation, inserts and a grid with EQ, TAME, CMP and REV that is only active in Manual mode. During playback, the fader of the IT group shows how the ducking is working.

### 8.5 Master

The master is the sum that is exported.

- Master fader with automation.
- **PRE-GAIN** (up to 24 dB up or down) before the fader. This is where the AUTO MIX puts its level correction, so that the fader sits at 0 dB after switching to Manual mode. Dragging changes the value, Shift allows fine steps, a double-click sets it to 0.
- **EQ** and **CMP** (bus compressor), only in Manual mode.
- **Meters:** peak level left and right, and loudness in LUFS as momentary, short-term and integrated value. The large LUFS I value appears green if it deviates from the target by no more than 1 LU, orange up to 3 LU and red above that.
- **LRA**: the loudness range, that is, how much the loudness varies over the program.
- **CLIP** indicator: lights up after clipping. A click on the channel strip resets it.

The separate **CUE** channel strip feeds the headphone path (**HEADPHONES**) and has one insert slot.

## 9 The sound modules

Each of the nine sound modules has its own window with controls. The display in the module is based on the same values that monitoring and export use for their calculations.

The following applies to all modules:

- The status line shows "Values from AUTO MIX", "Edited (differs from **AUTO MIX**)" or "No AUTO MIX yet - showing playback".
- **Reset to AUTO MIX** restores the values of the automatic mix.
- In Assist mode, right-click \> **View...** opens the module locked with the notice "Set by **AUTO MIX**". The **Edit in Manual** button switches to Manual mode and unlocks the module.
- **Presets:** factory presets by category, plus "User", "Save preset..." and "Show preset folder". User presets are stored in `~/Library/SATK/Presets/`. Presets can only be loaded in Manual mode.
- Cmd+Z, Cmd+S and the space bar also work when a module window is in front.

### 9.1 REPR: Repair (De-Click and De-Plosive)

De-Click removes clicks and lip smacks, De-Plosive softens popping sounds on P and B below 240 Hz.

[[IMG:repr.png|The REPAIR module with De-Click and De-Plosive]]

| Control              | Range       | Default          | Function                                             |
|----------------------|-------------|------------------|------------------------------------------------------|
| SENSITIVITY          | 0 to 10     | 4                | Sensitivity of click detection                       |
| FREQUENCY SKEW       | -10 to +10  | 0                | Shifts detection toward low or high clicks           |
| CLICK WIDENING       | 0 to 10 ms  | 4 ms             | Width of the repaired area around a click            |

**CLICKS ONLY** plays only what is removed. This lets you check whether too much is being removed. De-Click works without delay. Clicks in speech pauses are removed across the full frequency band. De-Plosive works with fixed settings. In Assist mode REPR is switched off; in Manual mode it can be switched on.

### 9.2 NR: Noise reduction

NR removes steady background noise such as fans, hum or room noise. A neural network separates voice and noise.

[[IMG:nr.png|The NR module with the AMOUNT knob]]

The module has a single control, **AMOUNT** (0 to 100). A segment on the ring switches NR on and off; a double-click sets the value to 100. The measured spectrum is shown in the circle. NR is switched off by default, and the AUTO MIX does not switch it on either. In version 2.0, NR is available on voice tracks.

Higher values remove more noise, but can change S sounds. Listen to the S sounds while adjusting.

### 9.3 EQ: Equalizer

The EQ changes the sound of a track, for example to make a voice brighter or warmer or to lower booming frequencies.

[[IMG:eq.png|The EQ module with analyzer, bands and dynamics controls]]

The EQ has nine bands: low cut (high-pass, 20 Hz to 1 kHz), bells 1 to 5, high shelf, high cut (1 to 20 kHz, off by default) and air (8 kHz).

| Control        | Range                                                     |
|----------------|-----------------------------------------------------------|
| FREQ           | Frequency in Hz                                           |
| GAIN           | -18 to +18 dB                                             |
| Q (bandwidth)  | Bells 0.15 to 14, shelves 0.1 to 10, cuts 0.3 to 4        |

Bells and shelves can be made dynamic (**DYN**). The band then reacts to the level and, for example, lowers a frequency only when it becomes too loud. Controls: **RANGE** (-24 to +24 dB), **THRESHOLD** (-80 to 0 dB), **ATTACK** (0.1 to 500 ms), **RELEASE** (5 ms to 5 s or AUTO).

**SOLO** on the band (or Alt+click on a band point) plays only the frequency range of this band. This also works in Assist mode and never affects the export. The analyzer shows the spectrum before and after the EQ. In the **ANALYZER** menu you choose **POST**, **PRE**+**POST** or OFF, as well as Resolution, Speed, Range, Tilt and Freeze.

### 9.4 TAME: Resonance

TAME detects disturbing, harsh or booming individual tones and lowers them only at the moment they occur.

[[IMG:tame.png|The TAME module (resonance)]]

| Control         | Range          | Function                                   |
|-----------------|----------------|--------------------------------------------|
| SOFT / HARD     |                | Gentle or strong operation                 |
| DEPTH           | 0 to 10        | Amount of reduction                        |
| DETAIL          | 0 to 10        | How finely individual tones are separated  |
| ATTACK, RELEASE | 0 to 10        | Attack and release time                    |
| MIX             | 0 to 100 %     | Share of the processed signal              |
| MAX CUT         | off to 24 dB   | Maximum reduction                          |
| OUT, WET TRIM   | -18 to +18 dB  | Output level                               |

With up to eight sensitivity bands (bell, shelf, cut, tilt and others) you determine in which frequency ranges TAME works more precisely. **DELTA** plays only what is removed. There are 16 factory presets in the groups General, Speech, Mix and Music.

### 9.5 DES: De-esser

The de-esser softens harsh S, SH and Z sounds without making the voice sound dull.

[[IMG:deesser.png|The DE-ESS module]]

| Control                 | Range                    | Function                                                       |
|-------------------------|--------------------------|----------------------------------------------------------------|
| SINGLE VOCAL / ALLROUND |                          | Single voice or mixed material                                 |
| WIDE / SPLIT            |                          | Lower the entire signal or only the harsh frequency range      |
| THRESHOLD               | minus infinity to 0 dB   | Threshold                                                      |
| RANGE                   | 0 to 24 dB               | Maximum reduction                                              |
| LOOKAHEAD               | 0 to 15 ms, on/off       | Acts slightly before the S sound                               |
| HIGH-PASS, LOW-PASS     | 2 to 20 kHz              | Frequency range the de-esser reacts to                         |

**TRIGGER** plays the signal the de-esser reacts to, **REMOVED** plays what is removed. The AUTO MIX measures the sharpness of each voice and sets the de-esser accordingly. There are eight factory presets, for example for male and female voices.

### 9.6 CMP: Compressor

The compressor evens out loud and quiet passages so that the voice sounds even and present. The module shows the characteristic curve, the level history and the gain reduction (in cyan).

[[IMG:comp.png|The compressor module with characteristic curve and level history]]

There are three modes: **CLEAN** (peak-oriented, for speech), **SMOOTH** (soft, based on the average level) and **BUS** (for groups and master).

| Control          | Range                                     | Function                                                                                                    |
|------------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| THRESHOLD        | -60 to 0 dB                               | Level above which compression takes place                                                                   |
| RATIO            | 1:1 to 100:1                              | Strength of compression                                                                                     |
| KNEE             | 0 to 24 dB                                | Soft or hard onset                                                                                          |
| ATTACK           | 0.1 to 250 ms                             | Attack time                                                                                                 |
| RELEASE          | 5 ms to 2.5 s or AUTO                     | Release time. With AUTO it adapts to the speech pauses; the set value then has no effect.                  |
| MAKEUP           | -12 to +24 dB (AUTO with CLEAN only)      | Compensates for the gain reduction                                                                          |
| MIX              | 0 to 100 %                                | Parallel compression                                                                                        |
| HOLD, RANGE, DRY | 0 to 500 ms, 0 to 60 dB, off to +36 dB    | Fine adjustment, no effect with SMOOTH                                                                      |

Factory presets: Speech - broadcast, Speech - gentle, Music - bus glue, Music - dense bed, Atmosphere - pad, Effects - catch peaks. There are separate presets for groups and master. A preset sets mode, ratio, knee, times and mix, but not threshold and makeup.

### 9.7 BRTH: De-breath

De-breath lowers breathing noises between sentences without changing the speech. Breaths are detected by their sound, not by volume alone.

[[IMG:debreath.png|The DE-BREATH module with overview and magnifier]]

| Control           | Range                         | Default          |
|-------------------|-------------------------------|------------------|
| RANGE (reduction) | 0 to 24 dB                    | 12 dB            |
| Sensitivity       | CAREFUL, NORMAL, THOROUGH     | NORMAL           |

At the top, the module shows the entire track; below it is a magnifier around the playhead with the waveform before and after processing. A click on a breath removes it from processing or adds it back. With Alt+drag you mark a breath by hand. **BREATHS ONLY** plays only the breaths. The status line gives the number of breaths found, set by hand and uncertain. In Assist mode, de-breath is switched on by default. It acts during playback and export, but not during recording.

### 9.8 SAT: Saturate

Saturate adds analog-sounding saturation, similar to a tube or tape. The module only acts in Manual mode and is switched off by default.

[[IMG:sat.png|The SATURATE module with characteristic curve and spectrum]]

As the type, choose **TUBE** or **TAPE**, each combinable with **WARM**. This results in Tube, Tape, Warm Tube and Warm Tape. Controls: **DRIVE** (0 to 100), **MIX** (0 to 100), **OUTPUT** (-24 to +24 dB). There are factory presets such as Clean and several tube and tape variants.

### 9.9 REV: Reverb

The reverb places a voice in a room, from a small voice booth to a large hall. It only acts in Manual mode and is the last link in the chain. A voice track becomes stereo from the reverb onward, and the reverb tail is included in the export.

[[IMG:rev.png|The reverb module (REVERB)]]

| Control      | Range        | Default          | Function                            |
|--------------|--------------|------------------|-------------------------------------|
| SPACE        | 0.2 to 10 s  | 2.5 s            | Reverb time, size of the room       |
| DECAY RATE   | 0.5 to 2     | 1                | Speed of the decay                  |
| DISTANCE     | 0 to 1       | 0.5              | Perceived distance of the voice     |
| BRIGHTNESS   | 0 to 1       | 0.5              | Bright or dark                      |
| CHARACTER    | 0 to 1       | 0.3              | Tonal color of the room             |
| STEREO WIDTH | 0 to 1.2     | 0.7              | Stereo width                        |
| MIX          | 0 to 1       | 0.3              | Share of the reverb                 |
| PREDELAY     | 0 to 500 ms  | 0                | Gap between voice and reverb        |

In addition there are input and output levels, pan and two EQ tabs (DECAY EQ and **POST** EQ). There are about 30 factory presets in the groups Ambience, Small, Medium, Large, Very Large and Voice, for example Vocal Booth, Narrator Polish and Radio Studio.

## 10 Plugins and insert slots

In the insert slots you load plugins from other manufacturers in the Audio Unit (AU, including AUv3) and VST3 formats. Instruments are not offered. Plugins are only active in Manual mode. In Assist mode the slots are visible, but have no effect.

Each track, the Voice group, the IT group and the master have five slots each; the CUE channel strip has one. The plugins work in order from top to bottom and come after the built-in modules.

### 10.1 Inserting a plugin

1.  Click an empty slot. The selection opens, sorted by manufacturer.
2.  Choose the plugin. The plugin window opens immediately.

### 10.2 Operation at the slot

| Operation                       | Function                                                          |
|---------------------------------|-------------------------------------------------------------------|
| Click the name                  | Open the plugin window                                            |
| On/off icon or Cmd+click        | Bypass (skip the plugin)                                          |
| x when hovering with the mouse  | Remove the plugin (Cmd+Z restores it)                             |
| Right-click                     | Menu with Open editor, Bypass, Remove and Rescan plugins          |

When a plugin window is in front, the app still passes the space bar (Play/Stop), the R key (record) and Home to the transport.

### 10.3 Plugin list and rescan

At launch, the app checks the installed plugins. Each plugin is tested in its own helper process. If a plugin crashes, it goes on a block list and does not endanger the app. After installing new plugins or a plugin update, choose **Rescan plugins...** in the slot menu. This also clears the block list, and plugins that no longer exist disappear from the list.

The delay (latency) of plugins is compensated automatically, also on groups and master.

## 11 Automation

Automation records control movements and plays them back on every playback. This way, for example, one passage automatically becomes quieter and another louder. Automation is available in Manual mode. In Assist mode, the AUTO button is shown in gray.

### 11.1 Automatable parameters

- Volume (fader) on tracks, Voice group, IT group and master
- Pan
- Mute
- **Plugin parameters:** every control of a plugin that you move during writing

The CUE channel strip has no automation.

### 11.2 Automation modes

You choose the mode with the automation button in the channel strip. Names and behavior match the common DAWs:

| Mode          | Color      | Behavior                                                                                                                                  |
|---------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| READ          | gray       | Plays the curve. The fader can still be moved; a mark shows the value of the automation.                                                  |
| TOUCH         | light blue | Writes only while the control is touched. After releasing, it returns to the existing curve within 0.25 seconds.                          |
| LATCH         | dark blue  | Writes from the first touch and holds the last value until STOP.                                                                          |
| WRITE         | red        | Writes continuously from PLAY, even without touching. After one pass, the track switches to TOUCH automatically.                         |
| TRIM (add-on) | yellow     | Writes no absolute values but a correction of the existing curve, for example an entire ducking 2 dB lower.                              |

Mute automation: in **TOUCH** the mute button acts like a momentary button and mutes as long as it is pressed. In **WRITE** it writes from the start, in **LATCH** until STOP.

### 11.3 Automation in the timeline

In the track header you switch the view between Waveform and Volume. Alt+click switches all tracks. In the Volume view you see the curve and can set, move and delete points (select and press Delete). The AUTO MIX ducking is also visible here as a curve.

The automation modes are saved with the project.

## 12 Export

With **EXPORT** in the transport bar you create the delivery files: the finished mix, optionally the voice as a separate file, the video with new sound or an MXF for broadcast operations. All files go into their own delivery folder; existing files are not overwritten.

### 12.1 Workflow

1.  In Assist mode, run **AUTO MIX** ([Chapter 7](#k7)); in Manual mode, finish the mix.
2.  Press **EXPORT**. The export window opens.
3.  Enter a name for the delivery in the **Name** field. If it stays empty, the project name is used.
4.  Select which files are to be created ([Sections 12.2](#k12-2) to 12.4).
5.  Click **EXPORT** or press Return. If **Destination** is set to "Ask at every export", you now choose the destination folder; otherwise the app writes directly to the chosen destination.

**Destination:** In the **Destination** row of the export window you choose "Ask at every export", one of the recently used destinations or **Choose folder...**, for example a folder on a server. The destination is saved in the project and therefore also in session templates. If it cannot be reached at export time, for example because the server drive is not connected, or if write permissions are missing, the export stops with a message instead of putting the files somewhere else. The window then shows "Destination not reachable - is the server connected?".

A subfolder with the delivery name is created in the destination folder. The files are named, for example, `Beitrag_2026-11-19_v1_mix.wav` and `Beitrag_2026-11-19_v1_voice.wav`. With each further export the version number increases (v2, v3 and so on).

### 12.2 Audio

| Row                                        | Content                                                                                                | Default          |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------|------------------|
| Audio mix                                  | Finished mix (stereo)                                                                                  | on, WAV 24-bit   |
| Voice stem                                 | Only the voice or voices, for example for a later remix                                                | off              |
| Voice tracks individually                  | One file per voice track without effects, only available with two or more voice tracks                 | off              |
| Edit list for other DAWs (AES31, .adl)     | For opening the project in Pro Tools, Nuendo and other DAWs. The project must be saved for this.        | off              |

Available formats: WAV, AIFF, AAC (.m4a), MP3, MP2 (.mp2), MP2 (.wav), FLAC and Opus.

| Setting                       | Options                                 | Restriction                                     |
|-------------------------------|-----------------------------------------|-------------------------------------------------|
| Sample rate                   | Project, 44.1, 48, 88.2 or 96 kHz       | MP2 and MP3 at most 48 kHz, Opus always 48 kHz  |
| Bit depth (WAV, AIFF, FLAC)   | 16-bit with dither, 24-bit, 32-bit float| FLAC at most 24-bit                             |
| Bitrate (MP3, AAC, MP2, Opus) | 128, 192, 256 or 320 kbit/s             | 384 kbit/s with MP2 only                        |

WAV files get a timestamp according to the BWF standard, based on the start timecode of the project.

### 12.3 Normalizing

The "Normalise to -23 LUFS (...)" checkbox brings the file to the target loudness of the profile and limits the peaks with a true peak limiter. The value in the label depends on the profile. With the Studio 0 dB profile, the file is instead normalized to a peak level of 0 dBTP.

- In Assist mode, the AUTO MIX already normalizes. The export outputs the finished mix.
- In Manual mode, normalization only takes place if the checkbox is checked. A line in the window states how far the file will then deviate from your monitoring.
- The checkbox only applies to the current export.
- You can also choose "Limit loudness range (LRA to 6 LU, multiband)". This option reduces large fluctuations in volume.

### 12.4 Video and MXF

Under **OUTPUTS** you choose **Video (MOV/MP4)** or **MXF (broadcast)**. The option that matches the loaded video is active. The picture is taken over unchanged and the new sound is inserted.

For MXF there are additional settings:

- **Delivery profile:** EBU R128, US ATSC - IT 8, Stereo, DE ARD/ZDF - HDF01a, JP ARIB - RDD9, FR CST - AS-10. If the loudness profile of the project does not match the delivery profile, a red warning appears.
- **Track count:** 8 or 16 audio tracks. The delivery profiles JP ARIB - RDD9 and FR CST - AS-10 only allow 8 audio tracks. For them, the app switches to 8 and reports this.
- Preset for the audio tracks, for example "Mix 1+2, voice 7+8". Under "My presets" are your saved allocations.
- **TRACK ALLOCATION:** For each track (T1 to T8 or T16) you specify what is on it (mix L or R, voice, silent or a channel of the source). The label of a track is only a name and does not change its content.

With **Save allocation as preset...** in the list of presets you save the current allocation under a name. The track count and the content and label of each track are saved.

Next to the MXF, an allocation sheet (`<Name>_tracks.txt`) is created automatically that describes the actual track allocation.

### 12.5 Podcast: chapters and episode details

For podcasts, open the Chapters window (Window \> Chapters, Cmd+Shift+K):

1.  Put the playhead at the start of the chapter and click **Add at playhead**.
2.  Enter a title, optionally an image and a link. Chapters without a title are not exported.
3.  Under **PROJECT...** \> EPISODE, enter title, author, show, comment and cover. The cover must be square and 1400 to 3000 pixels in size, chapter images at least 600 pixels.

On export, the mix gets ID3 tags and chapters. In addition, a chapter file `<Name>-chapters.json` according to the Podcasting 2.0 standard is created, including chapter images.

### 12.6 Subtitles and transcript

You export subtitles in the Script Editor on the **AUDIO** page with **TEXT EXPORT**. You can choose SubRip (.srt), WebVTT (.vtt), plain text (.txt) and JSON (Podcast 2.0).

## 13 Remote recording, virtual camera and cue

In remote recording, the voice artist is at another location and connected via a browser or conferencing service. For this, voyzSESSION PRO comes with its own virtual audio device and a virtual camera. The voice artist sees your picture, hears video and director, and speaks directly into your recording track.

### 13.1 One-time setup

1.  **Installing the audio driver:** Settings \> Audio/Video..., there click **Install** under "Virtual audio device". Then restart the app. Two devices are created: voyzSESSION Send (output from the app) and voyzSESSION Return (input into the app).
2.  **Installing the camera:** In the app menu, choose **Install virtual camera...**. The app must be in the Applications folder for this. macOS requires approval under System Settings \> General \> Login Items & Extensions \> Camera Extensions. A restart may be necessary. **Virtual camera status...** shows whether the camera is active.
3.  In the A/V settings, switch on **Virtual camera (video to browsers)**.

In version 2.0, the A/V settings window is still labeled in English, even when the app is set to German.

### 13.2 Running a session

1.  In the conferencing or browser service (for example SessionLink PRO, Zoom or Teams), set: microphone = voyzSESSION Send, speakers = voyzSESSION Return, camera = voyzSESSION.
2.  In voyzSESSION PRO, assign the voice track to the input voyzSESSION Return L (or R).
3.  In the mixer, on the **CUE** channel strip, measure the latency with **MESSEN**. The app sends a quiet test tone to the voice artist and looks for it in the return path. The result is shown in milliseconds.
4.  Record as usual ([Chapter 4](#k4)).
5.  **After recording:** Right-click the take \> **Align by link latency**. The take is moved forward by the measured delay and is then in sync with the picture again.

### 13.3 Cue: what the voice artist hears

The cue path to the voice artist contains the sound of the video and playout tracks, the previous takes and the talkback. The artist's own live voice is not sent back, so that they do not hear themselves delayed.

- **TALK** in the **CUE** channel strip switches on the talkback microphone, only while stopped. Talkback is never heard on your own speakers.
- The cue fader controls the volume to the voice artist (-48 to +6 dB). Sending takes place at -23 LUFS.
- During normal playback, the return path is only audible if the I button (input monitoring) is active on the track. During recording it is always audible.

### 13.4 Booth window and picture window

For a voice artist in your own booth there is the booth window (Window \> Booth window, Cmd+Shift+B). It is shown on a monitor connected via HDMI and is therefore free of delay. The prompter is on the left, the picture with timecode on the right; during recording a red frame appears. The picture window (Cmd+9 or **PICTURE**) shows only the picture without a frame, optionally on an external display.

## 14 External control: Stream Deck, control surfaces, OSC

voyzSESSION PRO can be controlled with an Elgato Stream Deck, a Mackie Control surface or via OSC. This is useful, for example, when a voice artist works alone in the booth.

### 14.1 Stream Deck

1.  In the app menu, choose **Stream Deck: install plugin...**. The Elgato software takes over the plugin.
2.  Under **Stream Deck: load layout**, choose the matching template: Stream Deck (15 keys), Stream Deck MK.2 (15 keys), Stream Deck Mini (6 keys), Stream Deck XL (32 keys) or Stream Deck + (dials).
3.  In the A/V settings, switch on **OSC remote control**. The plugin communicates with the app via OSC.

The keys show the state of the app, for example on/off or current values. The channel strip keys are in the same order as in the mixing console and also switch playout tracks.

### 14.2 Mackie Control surface (MCU)

In the A/V settings, under **MCU FADER CONTROLLER (MIDI)**, select the MIDI port of your surface. The addition **RECEIVING** indicates that data is arriving from the surface.

| Control on the surface          | Function                                                |
|---------------------------------|---------------------------------------------------------|
| 8 faders (touch-sensitive)      | Volume of the tracks, like the fader on screen          |
| V-Pot, press V-Pot              | Pan, pan to center                                      |
| REC, SOLO, MUTE, SELECT         | Per channel (REC on voice tracks only)                  |
| PLAY, STOP, RECORD              | Transport (STOP while stopped jumps to the start)       |
| CYCLE                           | Loop                                                    |
| Rewind, Fast forward            | Winding                                                 |
| BANK, CHANNEL                   | Shift the fader bank by 8 or 1 track                    |

The master fader of the surface controls the master; the timecode display of the surface runs along.

### 14.3 OSC and displays in the browser

- **OSC:** The app receives on port 8000 and reports states back, by default to 127.0.0.1:9000 (changeable under **OSC REPLY TO**). Via OSC you can reach transport, track functions (arm, solo, mute, automation mode), editing, markers, views, **AUTO MIX**, save, export and talkback.
- **Console displays in the browser:** Switch on **Console displays (web)**, copy the addresses with **COPY URLS** and open them on a tablet or second computer in the same network (port 8422, with an access key in the address).

## 15 Settings, projects, saving and recovery

### 15.1 Settings > General (Cmd+,)

| Row                       | Function                                                                                                                        |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Language                  | Automatic (system language), Deutsch, English, Français, Español, Italiano, Português. The change takes effect at the next start.|
| Prompter reading language | Language in which speech recognition follows the text                                                                          |
| Level Check               | "Show level check at startup" on or off. Off by default.                                                                        |
| Hints                     | "Show hints again" shows one-time hints again                                                                                   |

Directly in the Settings menu is the **Crossfade on overlap** switch (switched on by default, see [Chapter 6](#k6)).

### 15.2 Settings > Audio/Video (A/V... button)

- **OUTPUT and INPUT:** output and input device, selectable independently of each other, for example a USB microphone together with an interface.
- **SAMPLE RATE and BUFFER SIZE:** buffer size from 32 to 1024 samples. A small buffer shortens the delay in the headphones, but increases the processing load. Below it is the measured total delay (round trip).
- **Direct hardware monitoring:** leave it switched on if you monitor yourself through the interface (default). Software monitoring is then silent, so that you do not hear yourself twice.
- **RECORDING DELAY:** shifts new takes by a few samples if the interface records them offset.
- **Low latency monitoring:** bypasses plugins with too much delay on monitored tracks. These plugins are marked orange. The export is not affected.
- **Also:** MCU surface, virtual audio device, displays in the browser, OSC and virtual camera ([Chapter 13](#k13) and 14).

### 15.3 Project settings (PROJECT... button)

Changes take effect immediately.

- **AUDIO, sample rate:** The sample rate is determined by the project, not by the interface. For an empty project you set it directly. If the project already contains material, choose **Save copy at different sample rate**. The app then converts a copy; the original stays unchanged.
- **TIME AND PICTURE:** frame rate (23.976 to 60 fps, including drop frame), start timecode (quick selection 00:00:00:00 or 10:00:00:00) and **Take from video**. If the frame rate of the video differs, it is shown in red.
- **LOUDNESS:** loudness profile and mix style ([Section 7.1](#k7-1)).
- **EPISODE:** details for podcasts ([Section 12.5](#k12-5)).

### 15.4 Saving, templates, recovery

- Save with Cmd+S, Save as with Cmd+Shift+S or with the **FILE** button. A project is a folder with the extension `.satkproj`. Recordings are stored directly in the `audio` subfolder of the saved project. A new project should therefore be saved before the first recording.
- Cmd+S during an **AUTO MIX** is queued and carried out afterwards.
- **Templates:** **FILE** \> **Save current as template...** saves tracks, settings, inserts, profile and prompter text, but no recordings, no video, no chapters and no markers. You then create new projects with **FILE** \> **New from template**. In the template, playout tracks keep their role and their assignment to the audio tracks of the video. At the next video import, the app fills these tracks ([Section 3.4](#k3-4)). The export destination is also saved in the template.
- **Automatic backup:** When there are changes, the app saves a recovery state every 30 seconds. After a crash, it asks at the next start whether this state should be restored or discarded.
- **Interrupted recording:** If a running recording was interrupted by a crash, the app reports "Interrupted recording found" the next time it opens. **Restore** creates a take from it, **Discard** moves the files to the Trash. **Later**, Esc or closing the window leave it unchanged, and the app asks again the next time it opens.
- **Quitting:** If there are unsaved changes, the app asks whether to save, discard or cancel. The same question appears with New and Open.

## Appendix

### A Keyboard shortcuts

Keys without Cmd, Alt or Control have no effect while a text field is active.

| Area       | Key                               | Function                                              |
|------------|-----------------------------------|-------------------------------------------------------|
| Transport  | Space bar                         | Play, stop                                            |
| Transport  | R                                 | Start or stop recording                               |
| Transport  | L                                 | Loop on or off                                        |
| Transport  | Return, End, Home                 | To the start, to the end, to position 0               |
| Transport  | Comma, period                     | 1 second back or forward                              |
| Markers    | Alt+M                             | Set a marker                                          |
| Markers    | 1 to 9, Shift+1 to 9              | Set a marker, jump to a marker                        |
| Markers    | Alt+comma, Alt+period             | Previous or next marker                               |
| Edit       | Cmd+Z, Cmd+Shift+Z                | Undo, Redo                                            |
| Edit       | Cmd+E                             | Split                                                 |
| Edit       | Cmd+C, Cmd+V, Cmd+D               | Copy, Paste, Duplicate                                |
| Edit       | Cmd+A                             | Select all takes                                      |
| Edit       | Delete                            | Delete the selection                                  |
| Edit       | M                                 | Mute take                                             |
| Edit       | S                                 | AutoCut                                               |
| Edit       | F                                 | Fade or crossfade                                     |
| Edit       | I                                 | Import audio at the playback position                 |
| Edit       | Cmd+Up/Down Arrow                 | Move the take to the neighboring track, with Shift copy it |
| Edit       | Left/Right Arrow                  | Move the selection by 1 frame, with Shift by 1 second |
| View       | Cmd+=, Cmd+Minus                  | Zoom                                                  |
| View       | 0, Z                              | Whole project, selection                              |
| View       | Control+Alt+Up/Down Arrow         | Track height                                          |
| View       | Cmd+Alt+Up/Down Arrow             | Height of the waveform                                |
| Mix        | Cmd+M                             | AUTO MIX                                              |
| Project    | Cmd+S, Cmd+Shift+S                | Save, Save as                                         |
| Window     | Cmd+,                             | Settings \> General                                   |
| Window     | Cmd+9                             | Picture window                                        |
| Window     | Cmd+Shift+B                       | Booth window                                          |
| Window     | Cmd+Shift+K                       | Chapters                                              |
| Prompter   | Cmd+Plus, Cmd+Minus, Cmd+0        | Font size                                             |
| Help       | Cmd+Shift+/                       | User Guide                                            |

### B Glossary

| Term                            | Meaning                                                                              |
|---------------------------------|--------------------------------------------------------------------------------------|
| AUTO MIX                        | Automatic mix in Assist mode                                                         |
| Bounce                          | Writing the mix to a file exactly as it sounds                                       |
| Clip gain                       | Volume directly on the take, before the channel strip                                |
| Crossfade                       | Transition between two takes                                                         |
| Ducking                         | Automatic lowering of music or atmosphere while someone is speaking                  |
| Fader                           | Slider for the volume                                                                |
| Insert                          | Slot for a plugin in the channel strip                                               |
| IT (international sound mix)    | All components except the voice: production sound, music, atmosphere, effects        |
| LUFS, LU                        | Units for perceived loudness. -23 LUFS is the television standard in Europe.         |
| LRA                             | Loudness range, that is, how much the loudness varies over the program               |
| Production sound (O-Ton)        | Original sound from the video, for example an interview                              |
| Pre-roll, post-roll             | Lead-in and run-out of a recording                                                   |
| Punch                           | Recording only in a defined range to replace a passage                               |
| Role                            | Type of content of a track (voice, music and so on), controls the automatic mix      |
| Arm                             | Prepare a track for recording                                                        |
| Stem                            | Single component of the mix as a separate file, for example only the voice           |
| Take, region                    | Recorded or imported piece of audio on a track                                       |
| True peak (dBTP)                | Actual highest peak value of the signal                                              |

### C Troubleshooting

| Problem                                                 | Solution                                                                                                                                                                       |
|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Level Check shows "No signal"                           | Check the microphone in the Level Check and under A/V... \> INPUT. Also check whether macOS allows microphone access (System Settings \> Privacy & Security \> Microphone).    |
| REC does not start a recording                          | A track must be armed (R). Without an armed track, the app reports "No track armed". A new project must be saved first.                                                       |
| You hear your own voice doubled or reverberant          | The voice comes through the interface and the software at the same time. Switch on Direct hardware monitoring under A/V... or switch off the direct monitor on the interface. |
| AUTO MIX does not start                                 | Switch off Solo, end any running recording, switch to Assist mode. At least one take must exist.                                                                              |
| AUTO MIX lights up blue                                 | The saved mix no longer matches the project. Run AUTO MIX again.                                                                                                               |
| Message that the export would clip (Manual mode)        | Pull down the master fader or enable "Normalise" when exporting.                                                                                                               |
| A plugin is missing from the list                       | Rescan plugins in the slot menu. Instruments are never offered.                                                                                                                |
| A plugin makes the app crash                            | The plugin goes on the block list at the next start. After an update of the plugin, rescan.                                                                                    |
| The prompter does not follow the voice                  | Allow speech recognition in macOS and switch on dictation. Set the language of the text with LANG.                                                                             |
| The Script Editor stays empty                           | Press Transcribe. Playout tracks are not transcribed.                                                                                                                          |
| The virtual camera does not appear                      | The app must be in the Applications folder. Approve the extension in System Settings, restart the Mac if necessary and switch on the camera under A/V...                     |
| voyzSESSION Send or Return is missing                   | Install the driver under A/V... and restart the app.                                                                                                                           |
| The frame rate is shown in red                          | Video and project have different frame rates. Under PROJECT..., choose "Take from video".                                                                                      |
| Export stops: destination not reachable                 | Connect the server drive or choose another folder under Destination in the export window. |
| AAF import: media files not found                       | Click **Choose folder...** and select the folder with the media of the edit. The app also searches subfolders. |
| The app has crashed                                     | At the next start, choose recovery. The app backs up every 30 seconds when there are changes.                                                                                  |
| Wrong interface language                                | Choose Settings \> General \> Language and restart the app.                                                                                                                    |
| The A/V settings window is in English                   | This window is not yet translated in version 2.0. The rest of the app follows the selected language.                                                                          |

### D Trademarks

All product and company names mentioned in this manual are trademarks or registered trademarks of their respective owners. They are mentioned only to indicate what voyzSESSION PRO works with. Their mention does not imply any affiliation with or endorsement by these companies.
