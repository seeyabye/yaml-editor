import sys, traceback
from ruamel.yaml.comments import CommentedMap as OrderedDict

try:
    # Copy CommentToken
    # ct = hiera['download'].ca.items['attribute'][2]
    ct = ruamel.yaml.tokens.CommentToken('\n\n', ruamel.yaml.error.CommentMark(0), None)

    hiera['download']['selectors'] = [OrderedDict([
        ('selector', hiera['download']['selector']),
        ('attribute', hiera['download']['attribute'])
    ])]

    print(hiera['download']['selectors'][0].ca.items)
    hiera['download']['selectors'][0].ca.items['attribute'] = [None, None, ct, None]

    del hiera['download']['selector']
    del hiera['download']['attribute']

except Exception as e:
    traceback.print_exc(file=sys.stdout)
    pass

