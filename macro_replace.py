#!/usr/bin/env python3

from pprintpp import pprint as pp

macro = {
    '$HOSTNAME$':'myhost',
}

options = [
    {'url': 'https://$HOSTNAME$/pathA?host=$HOSTNAME$'},
    {'url': 'https://$HOSTNAME$/pathB'},
]

for index, item in enumerate(options):
    options[index]['url'] = options[index]['url'].replace("$HOSTNAME$", macro['$HOSTNAME$'])

pp(options)


# FIXME import and use the replace_macros() methode instead
