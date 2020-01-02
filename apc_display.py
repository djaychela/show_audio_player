import mido
import time
import pygame
import os
import json

# some variables
config_file = "config.json"
button_size = 70
BLACK = (0, 0, 0)
GREY = (80, 80, 80)
WHITE = (255, 255, 255)
FPS = 30

# initialise the midi input and output
inport = mido.open_input("APC MINI")
outport = mido.open_output("APC MINI")

# initialise pygame display
pygame.init()
pygame.display.set_caption("Audio Player")
screen = pygame.display.set_mode((1024, 800))
clock = pygame.time.Clock()


# initialise pygame for audio
pygame.mixer.init(frequency=44100)
pygame.mixer.set_num_channels(99)

# font creation
tinyArial = pygame.font.SysFont("arial", 15)
smallArial = pygame.font.SysFont("arial", 25)
medArial = pygame.font.SysFont("arial", 40)
largeArial = pygame.font.SysFont("arial", 65)


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
        self.friendly_name = audio_file.split('/')[-1][:-4]

    def set_state(self, state):
        if isinstance(state, bool):
            self.state = state
            self.midi_output()
            self.audio_output()

    def toggle_state(self):
        self.state = not self.state
        self.midi_output()
        self.audio_output()

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
config_path = os.path.join(os.getcwd(), "config", config_file)
with open(config_path, "r") as f:
    config_data = f.read()

# print(config_data)
config_info = json.loads(config_data)
for page in config_info["PageData"]:
    if page["PageNumber"] == 1:
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

while True:
    clock.tick(FPS)

    for msg in inport.iter_pending():
        # perform actions depending on message type
        if msg.type == "note_on":
            buttons[msg.note].toggle_state()

        elif msg.type == "control_change":
            channels[msg.control - 48] = msg.value

    # display update loop
    for idx in range(99):
        current_state[idx] = pygame.mixer.Channel(idx).get_busy()
        if current_state[idx] != prev_state[idx]:
            if current_state[idx] == 0:
                buttons[idx].set_state(False)
            prev_state[idx] = current_state

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    # time.sleep(0.5)

    # screen display
    screen.fill(BLACK)

    # display items
    # current sample set
    # widgets for playback channels
    # widget for mp3 playback
    
    # pad display
    for idx, c in enumerate(buttons[:64]):
        
        x_loc = 20 + ((idx % 8) * (button_size + 10))
        y_loc = 20 + (button_size + 10) * 7 - ((idx // 8) * (button_size + 10))
        pygame.draw.rect(screen, WHITE, (x_loc, y_loc, button_size, button_size))
        if current_state[idx]:
            pygame.draw.rect(screen, GREY, (x_loc + 2, y_loc + 2, button_size - 4, button_size - 4))
        else:
            pygame.draw.rect(screen, BLACK, (x_loc + 2, y_loc + 2, button_size - 4, button_size - 4))
        text = tinyArial.render(buttons[idx].friendly_name, True, WHITE)
        screen.blit(text, (x_loc + 3, y_loc + 3))

    # volume slider code
    for idx, c in enumerate(channels):
        x_loc = 20 + (idx * (button_size + 10))
        y_loc = 680
        pygame.draw.rect(screen, WHITE, (x_loc, y_loc, button_size, 100))
        pygame.draw.rect(screen, BLACK, (x_loc + 2, y_loc + 2, button_size - 4, 96))
        pygame.draw.rect(screen, GREY, (x_loc + 2, y_loc + 78 - int(c/1.67) ,button_size - 4,20))

        
        
    
    

    # smallArial.render_to(screen, (100 + r.width, 580), " HORIZONTAL",
    #                pygame.Color('blue'),None, size=(48, 24))

    time.sleep(0.05)

    pygame.display.update()
