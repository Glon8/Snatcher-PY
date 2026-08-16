from .values import op
from .helpers import switch
from .visuals import render


# ===================================< KILL SWITCH
def ks_switch():
    op['snatcher']['stat'] = 0

    switch(op['kill switch'], 'stat')

    render()
