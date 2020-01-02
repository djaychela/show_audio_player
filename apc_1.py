import mido
import time
import pygame

# initialise the midi input and output
inport = mido.open_input('APC MINI')
outport = mido.open_output('APC MINI')

# initialise pygame for audio
pygame.mixer.init()
print('Pygame Mixer Init done.')

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

    def toggle_state(self):
        self.state = not self.state
        self.midi_output()

    def get_state(self):
        return self.state

    def output_state(self):
        pass

    def midi_output(self):
        if self.state:
            velocity = 127
        else:
            velocity = 0
        out_msg = mido.Message('note_on', note=self.note_number, velocity=velocity)
        outport.send(out_msg)

buttons = []
for idx in range(98):
    buttons.append(button(idx, 'file.wav', False))

channels = [0 for _ in range(9)]

while True:
    for msg in inport.iter_pending():
        # perform actions depending on message type
        if msg.type == 'note_on':
            buttons[msg.note].toggle_state() 
        elif msg.type == 'control_change':
            channels[msg.control - 48] = msg.value

        
        
