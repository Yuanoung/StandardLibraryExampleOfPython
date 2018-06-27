import pathlib

p = pathlib.Path('pathlib_example_link')

p.symlink_to('pathlib_example.txt')

print(p)
print(p.resolve().name)
