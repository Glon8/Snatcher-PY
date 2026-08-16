_OPERATIONS = {
    'general': {
        'name': 'General',
        'note': "display is either 'emoji' or 'plain'",
        'display': 'plain'
    },
    'kill switch': {
        'name': 'Kill Switch',
        'key_trigger': 'c+0',
        'key_action': 'None',
        'stat': 0,
    },
    'snatcher': {
        'name': 'Snatcher',
        'key_trigger': 'c+4',
        'key_action': 'None',
        'path_from': '',
        'path_to': '',
        'backup_time': -1,
        'dir_files': 0,
        'self_replace': 0,
        'stat': 0,
    },
}

_SEPERATOR = f"===========================<"

op = _OPERATIONS
