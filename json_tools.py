import json
import os

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