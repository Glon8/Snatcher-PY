from .values import op
from .helpers import switch
from .visuals import render

# ===================================< REPLACE SWITCH
def replace_switch():
    if not op['ks']['stat']:
        return

    switch(op['snt'], 'self_replace')

    render()