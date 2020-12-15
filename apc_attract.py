import mido
import time
import pygame
import os
import json

# some variables
config_file = "config.json"

# initialise the midi input and output
inport = mido.open_input("APC MINI")
outport = mido.open_output("APC MINI")

# initialise pygame for audio
pygame.mixer.init(frequency=44100)
pygame.mixer.set_num_channels(99)

# button class for midi io and audio playback
class button:
    def __init__(self, note_number, audio_file, state=False):
        self.note_number = note_number
        if isinstance(state, bool):
            self.state = state
        else:
            self.state = False
        self.audio_file = audio_file
        self.channel = self.note_number % 8

    def set_state(self, state):
        if isinstance(state, bool):
            self.state = state
            self.midi_output()
            # self.audio_output()

    def toggle_state(self):
        self.state = not self.state
        self.midi_output()
        # self.audio_output()

    def get_state(self):
        return self.state

    def output_state(self):
        pass

    def midi_output(self):
        if self.state:
            velocity = 127
        else:
            velocity = 0
        out_msg = mido.Message("note_on", note=self.note_number, velocity=velocity)
        outport.send(out_msg)

    def audio_output(self):
        if self.state:
            self.audio = pygame.mixer.Sound(self.audio_file)
            pygame.mixer.Channel(self.note_number).play(self.audio)
        else:
            try:
                self.audio.fadeout(500)
            except:
                pass

# import files from json config file #
config_path = os.path.join(os.getcwd(), 'config', config_file)
with open(config_path, 'r') as f:
    config_data = f.read()

# print(config_data)
config_info = json.loads(config_data)
for page in config_info['PageData']:
    if page['PageNumber'] == 1:
        samples_list = []
        for idx in range(8):
            for sample in page["Samples"][str(idx)]:
                samples_list.append(sample)      

# initialise buttons
buttons = []
for idx in range(63):
    file_path = os.path.join(os.getcwd(), "audio", samples_list[idx])
    buttons.append(button(idx, file_path, False))
for idx in range(63, 99):
    file_path = os.path.join(os.getcwd(), "audio", "dummy.wav")
    buttons.append(button(idx, file_path, False))


channels = [0 for _ in range(9)]
prev_state = [0 for _ in range(99)]
current_state = [0 for _ in range(99)]

loop_counter = 1.0
while True:
    display_string = bin(int(loop_counter))[2:]
    display_string = "{:0>64}".format(display_string)
    loop_counter *= 1.1
    # display update loop

    for idx in range(64):
        buttons[idx].set_state(bool(int(display_string[idx])))
        
    time.sleep(0.05)

    if loop_counter > 18446744073709551615:
        loop_counter = 1
