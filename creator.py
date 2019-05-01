# How much files to create
number_of_files = int(input())
# Files names
NAME='test'
def createFile(name, id):
    file = open(name+id, 'w+')

for number in range(number_of_files):
    createFile(NAME, str(number))