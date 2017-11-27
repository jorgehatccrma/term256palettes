from x256 import from_hex

if __name__ == "__main__":
    with open('latexcolors.txt', 'r') as fh:
        for l in fh.readlines():
            if len(l.strip()) == 0:
                continue
            name, rgb = [x.strip() for x in l.strip().split('\t')]
            c = from_hex(rgb.lstrip('#'))
            short, shortrgb = c['index'], c['termrgb']
            print('"{}": ["{}", {}],'.format(name, rgb, short))

