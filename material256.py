from x256 import from_hex

if __name__ == "__main__":
    with open('materialcolors.txt', 'r') as fh:
        for l in fh.readlines():
            if len(l.strip()) == 0:
                continue
            name, rgb = [x.strip() for x in l.strip().split('#')]
            c = from_hex(rgb)
            short, shortrgb = c['index'], c['termrgb']
            print('"{}": ["#{}", {}],'.format(name, rgb, short))

