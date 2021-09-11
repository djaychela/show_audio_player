import os

from html_colors import return_css_color_names
from json_tools import load_config_data, parse_config_data

config_file = "config.json"
current_sample_set = 1

#TODO: iterate over all sample sets

config_data = load_config_data(config_file)
samples_list, soundtrack_list, pages_dict, page_name = parse_config_data(
    config_data, current_sample_set
)

# generate div styles
def create_div_styles(n_divs):
    div_html = """<style>
    """
    color_list = return_css_color_names()
    for i in range(n_divs):
        div_html_dummy = f""".div-{i+1} {{
            background-color: {color_list[i]};
            padding-top: 10px;
            padding-bottom: 10px;
            }}
    """
        div_html += div_html_dummy
    div_html += """
</style>"""
    return div_html

def generate_audio_players(soundtrack_list, mode="playlists"):
    player_html = ""
    for idx, soundtrack in enumerate(soundtrack_list):
        file_path = os.path.join(os.getcwd(), mode, soundtrack)
        player_audio = f"""<audio controls>
    <source src="{file_path}" type="audio/mpeg">
</audio>
"""
        player_html += player_audio
    return player_html

def create_div(input_html, id):
    return f'<div class="div-{id}">' + input_html + '</div>'


div_html = create_div_styles(5)
soundtrack_html = create_div(generate_audio_players(soundtrack_list, "playlists"), 1)

samples_html = ""
for idx in range(int(len(samples_list) / 8)):
    samples_group = []
    current_div = 2
    for jdx in range(8):
        samples_group.append(samples_list[idx*8 + jdx])

    if not all([True if sample=="dummy.wav" else False for sample in samples_group ]):
        # generate div of samples
        current_samples_html = create_div(generate_audio_players(samples_group, "media"), current_div)
        print(current_samples_html)
        current_div += 1
        samples_html += current_samples_html
# generate players for soundtracks
# generate players for samples_list
# output files

html_start = """<!DOCTYPE html>
<html>
"""

html_end = """</body>
</html>"""

html_output = html_start + div_html + "<body>" + soundtrack_html + samples_html + html_end

print(html_output)

with open("html_output/test.html", "w") as file:
    file.write(html_output)