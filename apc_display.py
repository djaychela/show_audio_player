import mido
import time
import pygame
import os
import json

from buttons import Button, PlaylistButton

# some variables
config_file = "config.json"
button_size = 70
warning_limit = 0.9
current_sample_set = 1

# colours for display
BLACK = (0, 0, 0)
GREY = (80, 80, 80)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FPS = 30

# initialise the midi input and output
inport = mido.open_input("APC MINI")
outport = mido.open_output("APC MINI")

# initialise pygame display
pygame.init()
pygame.display.set_caption("Audio Player")
screen = pygame.display.set_mode((1024, 840))
clock = pygame.time.Clock()


# initialise pygame for audio
pygame.mixer.init(frequency=44100)
pygame.mixer.set_num_channels(99)

# font creation
print("Initialising fonts...")
tinyArial = pygame.font.SysFont("arial", 15)
smallArial = pygame.font.SysFont("arial", 25)
medArial = pygame.font.SysFont("arial", 40)
largeArial = pygame.font.SysFont("arial", 65)
print("Fonts initialized!")


def draw_button(x_loc, y_loc, button_size, percentage, name, state):

    pygame.draw.rect(screen, WHITE, (x_loc, y_loc, button_size, button_size))
    if state:
        pygame.draw.rect(
            screen, GREY, (x_loc + 2, y_loc + 2, button_size - 4, button_size - 4)
        )
        if percentage < warning_limit:
            color = GREEN
        else:
            color = RED
        pygame.draw.rect(
            screen,
            color,
            (x_loc + 2, y_loc + button_size - 10, ((button_size - 4) * percentage), 8),
        )
    else:
        pygame.draw.rect(
            screen, BLACK, (x_loc + 2, y_loc + 2, button_size - 4, button_size - 4)
        )
    
    # handling of Q numbers to be larger in buttons
    offset = 0
    if len(name) > 0:
        if name.split()[0][0] == "Q":
            text = medArial.render(name.split()[0], True, WHITE)
            screen.blit(text, (x_loc + 3, y_loc + 3))
            name = " ".join(name.split()[1:])
            offset = 25
    # rest of text written as new lines
    if len(name) > 0:
        for t in name.split()[:3]:
            if t != '-':
                text = tinyArial.render(t, True, WHITE)
                screen.blit(text, (x_loc + 3, y_loc + 3 + offset))
                offset += 15


def load_config_data(config_file):
    config_path = os.path.join(os.getcwd(), "config", config_file)
    with open(config_path, "r") as f:
        config_data = f.read()
    return config_data


def parse_config_data(config_data, current_sample_set):
    pages_dict = {}
    config_info = json.loads(config_data)
    for page in config_info["PageData"]:
        pages_dict[page["PageNumber"]] = page["PageName"]
        if page["PageNumber"] == current_sample_set:
            page_name = page["PageName"]
            samples_list = []
            for idx in range(8):
                for sample in page["Samples"][str(idx)]:
                    samples_list.append(sample)

    soundtrack_list = config_info["SoundtrackList"]

    return samples_list, soundtrack_list, pages_dict, page_name


def load_buttons():
    for idx in range(64):
        file_path = os.path.join(os.getcwd(), "audio", samples_list[idx])
        buttons[idx] = Button(idx, file_path, False)


def load_playlist_buttons():
    for idx in range(82, 90):
        file_path = os.path.join(os.getcwd(), "playlists", soundtrack_list[idx - 82])
        buttons[idx] = PlaylistButton(idx, file_path, False)


def turn_off_other_soundtracks(note):
    for idx in range(82, 90):
        if idx != note:
            buttons[idx].set_state(False)


# various lists
channels = [100 for _ in range(9)]
prev_state = [0 for _ in range(90)]
current_state = [0 for _ in range(90)]
buttons = [None for _ in range(90)]
index_1 = [idx for idx in range(64)]
index_2 = [idx for idx in range(82, 90)]
indexes = index_1 + index_2

# initial setup
config_data = load_config_data(config_file)
samples_list, soundtrack_list, pages_dict, page_name = parse_config_data(
    config_data, current_sample_set
)


# initialise buttons

load_buttons()
load_playlist_buttons()


while True:
    clock.tick(FPS)

    for msg in inport.iter_pending():
        # perform actions depending on message type
        if msg.type == "note_on":
            # TODO: correct button number filtering
            if msg.note <= 63:
                buttons[msg.note].toggle_state()
            if 81 < msg.note < 90:
                turn_off_other_soundtracks(msg.note)
                buttons[msg.note].toggle_state()
        elif msg.type == "control_change":
            channels[msg.control - 48] = msg.value

    # display update loop
    for idx in indexes:
        if 81 < idx < 90:
            current_state[idx] = buttons[idx].get_state()
        else:
            current_state[idx] = pygame.mixer.Channel(idx).get_busy()
        if current_state[idx] != prev_state[idx]:
            if idx <= 81:
                if current_state[idx] == 0:
                    buttons[idx].set_state(False)
                prev_state[idx] = current_state

    # set volumes
    for c in range(64):
        volume = channels[c % 8] / 127
        pygame.mixer.Channel(c).set_volume(volume)
    pygame.mixer.music.set_volume(channels[8] / 127)

    # screen display
    screen.fill(BLACK)

    # TODO: display items
    # TODO: current sample set
    # TODO: load different sample set (keys 1-9)
    # TODO: selection of grid buttons from keyboard
    # TODO: display of current sound set on screen
    # TODO: turn off button at the end of soundtrack playback...
    # TODO: error handling for missing files
    # TODO: Large Q labels for Q samples.

    # text display of current sample set
    text = largeArial.render(page_name, True, WHITE)
    screen.blit(text, (200, 10))

    # sample pages name display
    x_loc = 800
    y_loc = 60
    for idx, (k, v) in enumerate(pages_dict.items()):
        text = smallArial.render(f"{idx+1}: {v}", True, WHITE)
        screen.blit(text, (x_loc, y_loc + (30 * idx)))

    # button display
    for idx, c in enumerate(buttons[:64]):

        x_loc = 20 + ((idx % 8) * (button_size + 10))
        y_loc = 60 + (button_size + 10) * 7 - ((idx // 8) * (button_size + 10))

        draw_button(
            x_loc,
            y_loc,
            button_size,
            buttons[idx].percentage_played(),
            buttons[idx].friendly_name,
            current_state[idx],
        )

    # playlist button display
    for idx, c in enumerate(buttons[82:90]):

        x_loc = 20 + (8 * (button_size + 10))
        y_loc = 60 + (idx * (button_size + 10))

        draw_button(
            x_loc,
            y_loc,
            button_size,
            buttons[idx + 82].percentage_played(),
            buttons[idx + 82].friendly_name,
            current_state[idx + 82],
        )

    # volume slider display
    for idx, c in enumerate(channels):
        x_loc = 20 + (idx * (button_size + 10))
        y_loc = 720
        pygame.draw.rect(screen, WHITE, (x_loc, y_loc, button_size, 100))
        pygame.draw.rect(screen, BLACK, (x_loc + 2, y_loc + 2, button_size - 4, 96))
        pygame.draw.rect(
            screen, GREY, (x_loc + 2, y_loc + 78 - int(c / 1.67), button_size - 4, 20)
        )

    time.sleep(0.05)

    # key handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if 49 <= event.key <= 57:
                current_sample_set = event.key - 48
            samples_list, soundtrack_list, pages_dict, page_name = parse_config_data(
                config_data, current_sample_set
            )
            load_buttons()

    pygame.display.update()
