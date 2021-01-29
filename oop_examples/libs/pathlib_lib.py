import pathlib

cwd = pathlib.Path.cwd()
print(cwd)
print('With repr:', repr(cwd))

invalid_dir = pathlib.Path("/var")
print(invalid_dir, 'exists?', invalid_dir.exists())

home_dir = pathlib.Path.home()
print(home_dir)

exist_dir = home_dir / 'Links'
print(exist_dir, 'exists?', exist_dir.exists())


print(home_dir.joinpath('scripts', 'python', 'main.py'))  # пример создания пути
file_name = 'file.txt'
file_path = cwd.parent / file_name
print(file_path)
print(file_path.read_text())  # чтение проще, чем у os

print(cwd.parent)
print(cwd.parent.parent)

print(file_path.name)
print(file_path.parent.name)
print('File name:', file_path.stem, 'File extension:', file_path.suffix)

print('Path root:', file_path.anchor)

print(file_path.with_name('file_2.py'))
print(file_path.with_suffix('.py'))
