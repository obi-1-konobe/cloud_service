import json

import numpy as np


def count_stat(json_list):
    heartbeats = list()
    temperature = list()
    for json_ in json_list:
        heartbeats.append(json_['heartbeats'])
        temperature.append(json_['temperature'])

    data = {
        'heartbeats': {
            'mean': float(np.mean(heartbeats)),
            'std': float(np.std(heartbeats)),
            'max': float(np.max(heartbeats)),
            'min': float(np.min(heartbeats))
        },
        'temperature': {
            'mean': float(np.mean(temperature)),
            'std': float(np.std(temperature)),
            'max': float(np.max(temperature)),
            'min': float(np.min(temperature))
        }
    }

    data_json = json.dumps(data)
    return data_json
