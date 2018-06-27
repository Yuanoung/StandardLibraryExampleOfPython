import pathlib

p = pathlib.Path('pathlib_example_dir')

try:
    p.mkdir()
    print('Creating {}'.format(p))
except FileExistsError as err:
    print(err)
