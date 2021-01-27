import os


def demo_os_base():
    print(os.name)
    # print(os.environ)
    print(os.environ['PATH'])
    print('Текущая директория:', os.getcwd())
    print(os.curdir)

    cwd = os.getcwd()
    subdir = os.path.join(cwd, 'subdir')
    print(subdir)
    try:
        os.mkdir(subdir)
        # os.makedirs(subdir) # like as mkdir, but create all intermediate-level directories
    except FileExistsError:
        print('Directory already exists')

    os.chdir(subdir)  # переход в папку
    print('В папке subdir:', os.getcwd())


# open file/create
def demo_file():
    filename = 'file.txt'
    with open(filename, 'w'):
        pass

    print(os.listdir("."))

    # os.remove()
    os.unlink(filename)  # remove created file


def demo_walk():
    for root, dirs, files in os.walk('.'):
        print('root:', root)
        print('dirs:')
        for d in dirs:
            print('-', d)
        print('files:')
        for f in files:
            print('-', f)


# demo_os_base()
# demo_file()
# demo_walk()

def demo_structure_dir():
    cwd = os.getcwd()
    print('cwd:', cwd)
    print('base name cwd:', os.path.basename(cwd))
    print('dir name cwd:', os.path.dirname(cwd))

demo_structure_dir()