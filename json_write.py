import os
import json

# some variables
config_file = "config.json"

json_data = {
    "PageData" : [{
        "PageNumber": 1 ,
        "PageName": "Samples 1",
        "Samples": {
            "0": ["Q12 - German - Radio.wav", "silence.wav", "Q16 - German - Radio.wav", "Q12 - German - Radio.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "1": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "2": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "3": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "4": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "5": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "6": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "7": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
        }
    },
    {
        "PageNumber": 2 ,
        "PageName": "Samples 2",
        "Samples": {
            "0": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "1": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "2": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "3": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "4": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "5": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "6": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "7": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
        }
    },
    {
        "PageNumber": 3 ,
        "PageName": "Samples 3",
        "Samples": {
            "0": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "1": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "2": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "3": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "4": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "5": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "6": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "7": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
        }
    },
    {
        "PageNumber": 4 ,
        "PageName": "Samples 4",
        "Samples": {
            "0": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "1": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "2": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "3": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "4": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "5": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "6": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "7": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
        }
    },
    {
        "PageNumber": 5 ,
        "PageName": "Samples 5",
        "Samples": {
            "0": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "1": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "2": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "3": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "4": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "5": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "6": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "7": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
        }
    },
    {
        "PageNumber": 6 ,
        "PageName": "Samples 6",
        "Samples": {
            "0": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "1": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "2": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "3": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "4": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "5": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "6": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "7": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
        }
    },
    {
        "PageNumber": 7 ,
        "PageName": "Samples 7",
        "Samples": {
            "0": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "1": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "2": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "3": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "4": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "5": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "6": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "7": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
        }
    },
    {
        "PageNumber": 8 ,
        "PageName": "Samples 8",
        "Samples": {
            "0": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "1": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "2": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "3": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "4": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "5": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "6": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "7": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
        }
    },
    {
        "PageNumber": 9 ,
        "PageName": "Samples 9",
        "Samples": {
            "0": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "1": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "2": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "3": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "4": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "5": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "6": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "7": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
        }
    },
    
    ],
    "SoundtrackList": ["Playlist 1.mp3", "Playlist 2.mp3", "Playlist 3.mp3", "Playlist 4.mp3", "Playlist 5.mp3", "underscore.mp3", "underscore.mp3", "underscore.mp3", ]
}

j = json.dumps(json_data)

# import files from json config file #
config_path = os.path.join(os.getcwd(), 'config', config_file)
with open(config_path, 'w') as f:
    f.write(j)
