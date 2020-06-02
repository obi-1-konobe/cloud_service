import json

import numpy as np


def count_stat(json_list):
    heartbeats = list()
    temperature = list()
    nrm = list()
    pressure = list()
    for json_ in json_list:
        heartbeats.append(json_['heartbeat'])
        temperature.append(json_['temperature'])
        pressure.append(json_['pressure'])
        nrm.append(json_['nrm'])

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
        },
        'pressure': {
            'mean': float(np.mean(pressure)),
            'std': float(np.std(pressure)),
            'max': float(np.max(pressure)),
            'min': float(np.min(pressure))
        },
        'nrm': {
            'mean': float(np.mean(nrm)),
            'std': float(np.std(nrm)),
            'max': float(np.max(nrm)),
            'min': float(np.min(nrm))
        }
    }

    data_json = json.dumps(data)
    return data_json
