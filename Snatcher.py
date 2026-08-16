import os

from data.helpers import config_parse, read_file, getDir, write_file
from data.values import op
from data.snatcher import snt_prot, snt_switch
from data.visuals import render
from data.killswitch import ks_switch

from pynput.keyboard import Controller as K, Listener as kL, HotKey

k = K()


# ===================================< CONTROL PANNEL
def control_panel():
    while True:
        if op['kill switch']['stat']:
            snt_prot()


# ===================================< MAIN
def main():
    config_parse(read_file('config.json'))

    snt = op['snatcher']

    if not isinstance(snt['path_to'], str) or not os.path.exists(snt['path_to']):
        snt['path_to'] = os.path.join(getDir(), 'stash')

        write_file(getDir(), 'config.json', op)

    # \/===================================< HOTKEYS SETTINGS
    hotkeys = [
        HotKey(HotKey.parse(op['kill switch']['key_trigger']), ks_switch),
        HotKey(HotKey.parse(snt['key_trigger']), snt_switch),
    ]

    def on_press(key):
        for thing in hotkeys:
            thing.press(key)

    def on_release(key):
        for thing in hotkeys:
            thing.release(key)

    # /\===================================< HOTKEYS SETTINGS

    render()

    with kL(on_press=on_press, on_release=on_release):
        control_panel()


# ===================================< MAIN START
if __name__ == '__main__':
    main()
