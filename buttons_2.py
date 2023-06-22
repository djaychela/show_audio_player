import mido
import time
import pygame
import os
import json

from mutagen.mp3 import MP3
from mutagen import MutagenError

# initialise the midi input and output
try:
    inport = mido.open_input("APC MINI")
except OSError:
    inport = mido.open_input(mido.get_input_names()[0])
    
try:
    outport = mido.open_output("APC MINI")
except OSError:
    outport = mido.open_output(mido.get_output_names()[0])


# button class for midi io and audio playback
class Button:
    """Class for buttons on APC controller, with MIDI note numbers, 
    audio file and states, with methods for state setting and getting
    and playing of audio files"""

    def __init__(self, note_number, audio_file, state=False):
        self.note_number = note_number
        if isinstance(state, bool):
            self.state = state
        else:
            self.state = False
        self.audio_file = audio_file
        self.audio = pygame.mixer.Sound(self.audio_file)
        self.channel = self.note_number % 8
        self.friendly_name = audio_file.split("/")[-1][:-4]
        if self.friendly_name == "dummy":
            self.friendly_name = ""
        self.start_time = 0
        self.length = self.audio.get_length()
        
        self.x_grid = 0
        self.y_grid = 0
        self.idx = 0
        self.button_size = 70

    def set_state(self, state):
        """ Set state of button using bools"""

        if isinstance(state, bool):
            self.state = state
            self.midi_output()
            self.audio_output()

    def toggle_state(self):
        """ Toggle the state to the opposite of current state."""

        self.state = not self.state
        self.midi_output()
        self.audio_output()

    def _calculate_position(self):
        self.x_position = 20 + ((self.idx % 8) * (self.button_size + 10))
        self.y_position = 60 + (self.button_size + 10) * 7 - ((self.idx // 8) * (self.button_size + 10))

    def get_state(self):
        return self.state

    def output_state(self):
        pass

    def midi_output(self):
        """ Performs MIDI output to illuminate APC buttons to reflect state."""

        if self.state:
            velocity = 127
        else:
            velocity = 0
        out_msg = mido.Message("note_on", note=self.note_number, velocity=velocity)
        outport.send(out_msg)

    def audio_output(self):
        """ Plays audio on the relevant channel."""
        if self.state:
            pygame.mixer.Channel(self.note_number).play(self.audio)
            self.start_time = time.time()
        else:
            try:
                self.audio.fadeout(500)
                self.start_time = 0
            except:
                pass

    def percentage_played(self):
        played = time.time() - self.start_time
        if self.get_state():
            return played / self.length
        else:
            return 0


class PlaylistButton(Button):
    """ Subclass of button, with altered audio output to allow
    use of MP3 files for soundtracks """

    def __init__(self, note_number, audio_file, state=False):
        self.note_number = note_number
        if isinstance(state, bool):
            self.state = state
        else:
            self.state = False
        self.audio_file = audio_file
        self.channel = self.note_number % 8
        self.friendly_name = audio_file.split("/")[-1][:-4]
        if self.friendly_name == "dummy":
            self.friendly_name = ""
        self.start_time = 0
        try:
            audio = MP3(audio_file)
            self.length = audio.info.length
        except MutagenError:
            self.length = 0

    def audio_output(self):
        if self.state:
            try:
                pygame.mixer.music.load(self.audio_file)
                pygame.mixer.music.play()
                self.start_time = time.time()
            except pygame.error:
                print(f"Soundtrack file missing: {self.audio_file}")
                self.start_time = 0
                self.state = False
        else:
            try:
                pygame.mixer.music.fadeout(2000)
                self.start_time = 0
            except:
                pass
