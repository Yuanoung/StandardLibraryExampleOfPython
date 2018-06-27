import pathlib

p = pathlib.Path('.')

for f in p.glob('*.PNG'):
    print(f)
