from .values import op
from .helpers import switch
from .visuals import render


# ===================================< KILL SWITCH
def ks_switch():
    op['snt']['stat'] = 0

    switch(op['ks'], 'stat')

    render()
