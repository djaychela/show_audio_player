import os

from html_colors import return_css_color_names
from json_tools import load_config_data, parse_config_data

config_file = "config.json"


# generate tr styles
def create_tr_styles(n_divs):
    div_html = """<style>
    """
    color_list = return_css_color_names()
    for i in range(n_divs):
        div_html_dummy = f"""tr.color_{i+1} td{{
            background-color: {color_list[i]};
            padding-top: 10px;
            text-align:center;
            }}
            tr.color_player_{i+1} td{{
            background-color: {color_list[i]};
            padding-bottom: 10px;
            text-align:center;
            }}
    """
        div_html += div_html_dummy
    div_html += """
</style>
</head>"""
    return div_html


def generate_audio_players(audio_file_list, mode, current_class):
    player_html = ""

    player_html += f"<tr class=color_player_{current_class}>"
    for idx, soundtrack in enumerate(audio_file_list):
        file_path = os.path.join(os.getcwd(), mode, soundtrack)
        player_audio = f"""<td>
        <audio controls>
    <source src="{file_path}" type="audio/mpeg">
</audio>
</td>
"""
        player_html += player_audio
    player_html += "</tr>"
    return player_html


def create_title_row(audio_file_list, current_class):
    html_output = f"<tr class=color_{current_class}>"
    for audio_file in audio_file_list:
        html_output += f"<td>{audio_file.split('.')[0]}</td>"
    html_output += "</tr>"
    return html_output


def create_div(input_html, id):
    return f'<div class="div-{id}">' + input_html + "</div>"


def generate_html_start():
    return """<!doctype html>
        <html lang="en">
        <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link href="bootstrap/css/bootstrap.css" rel="stylesheet">

        """


def generate_html_title(pages_dict, current_sample_set):
    header_text = (f"<h1 class='text-center'>{pages_dict[current_sample_set]}</h1><div class='container'>"
        "<header class='d-flex justify-content-center py-3'>"
        "<ul class='nav nav-pills'>")

    for k, v in pages_dict.items():
        if k == current_sample_set:
            header_text += f"<li class='nav-item'><a href='{v}.html' class='nav-link active' aria-current='page'>{k} - {v}</a></li>"
        else:
            header_text += f"<li class='nav-item'><a href='{v}.html' class='nav-link'>{k} - {v}</a></li>"
    header_text += "</div>"
    return header_text


def generate_html_end():
    return """</table></div></body>
    </html>"""


def create_output_file(file_name, content):
    with open(f"html_output/{file_name}", "w") as file:
        file.write(content)


def generate_soundtrack_players():
    chunks = [soundtrack_list[x : x + 4] for x in range(0, len(soundtrack_list), 4)]
    soundtrack_html = ""
    for chunk in chunks:
        soundtrack_html += create_title_row(chunk, 1)
        soundtrack_html += generate_audio_players(chunk, "playlists", 1)
    return soundtrack_html


def generate_samples_html():
    samples_html = ""
    for idx in range(int(len(samples_list) / 8)):
        samples_group = []
        current_div = 2
        for jdx in range(8):
            samples_group.append(samples_list[idx * 8 + jdx])

        if not all(
            [True if sample == "dummy.wav" else False for sample in samples_group]
        ):
            # generate html for group of samples, in groups of 4
            chunks = [samples_group[x : x + 4] for x in range(0, len(samples_group), 4)]
            for chunk in chunks:
                samples_html += create_title_row(chunk, current_div)
                samples_html += generate_audio_players(chunk, "audio", current_div)
                current_div += 1
    return samples_html


current_sample_set = 1
config_data = load_config_data(config_file)
samples_list, soundtrack_list, pages_dict, page_name = parse_config_data(
    config_data, current_sample_set
)

for page_num, page_name in pages_dict.items():
    samples_list, soundtrack_list, pages_dict, page_name = parse_config_data(
    config_data, page_num
)


    html_output = (
        generate_html_start()
        + create_tr_styles(5)
        + "<body> <div class='container'>"
        + generate_html_title(pages_dict, page_num)
        + "<table>"
        + generate_soundtrack_players()
        + generate_samples_html()
        + generate_html_end()
    )

    create_output_file(f"{page_name}.html", html_output)
