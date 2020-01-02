import os
import json

# some variables
config_file = "config.json"

json_data = {
    "PageData" : [{
        "PageNumber": 1 ,
        "PageName": "Samples 1",
        "Samples": {
            "0": ["Q12 - German - Radio.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
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
            "0": ["Q12 - German - Radio.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "1": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "2": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "3": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "4": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "5": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "6": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
            "7": ["dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav", "dummy.wav"],
        }
    }
    
    ]
}

j = json.dumps(json_data)

# import files from json config file #
config_path = os.path.join(os.getcwd(), 'config', config_file)
with open(config_path, 'w') as f:
    f.write(j)