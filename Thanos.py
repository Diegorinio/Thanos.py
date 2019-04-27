import os, random, glob
def getFiles():
    files_rmv =[]
    for f in glob.glob('**/*', recursive=True):
        files_rmv.append(f)
    return files_rmv
def getFilesToVanish():
    files = getFiles()
    files.remove('Thanos.py')
    print(files)
    print('Dlugosc ', len(files))
    population = len(getFiles())
    vanish = []
    sample = random.sample(range(population), population)
    print(sample)
    for file in range(len(sample)//2):
        vanish.append(files[file])
    # for x in range(population//2):
    #     id = sample[x]
    #     print('Act id is ',id)
    #     vanish.append(files[id])
    print('to Delete: ', len(vanish))
    return vanish
    
def Snap():
    for x in getFilesToVanish():
        try:
            os.remove(x)
            print(x, 'was Vanished')
        except IsADirectoryError:
            pass
        except OSError:
            print('File ', x,' not found')
            pass
        except IndexError:
            print('Index Error!, propably not enough files')
    print('Perfectly balanced, as all things should be')
    quit()

while True:
    try:
        print('WARNING!')
        print('Thanos.py will delete half of your files in actual directory: ', os.getcwd())
        will_you_snap = input()
        if will_you_snap == 'y':
            Snap()
        elif will_you_snap == 'n':
            quit()
    except ValueError:
        print('Please decide')