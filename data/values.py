_OPERATIONS = {
    'gnr': {
        'name': 'General',
        'note': "Display is either 'emoji' or 'plain'",
        'key_display_change': 'c+o',
        'display': 'plain',
        '.positive_emoji': "U+2705",
        '.negative_emoji': "U+274C"
    },
    'ks': {
        'name': 'Kill Switch',
        'note': 'Do not abuse Kill Switch! May lower performance!',
        'key_trigger': 'c+0',
        'stat': 0,
    },
    'snt': {
        'name': 'Snatcher',
        'note': 'Remember to set Kill Switch on before use!',
        'key_trigger': 'c+4',
        'key_self_replace': 'c+p',
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
