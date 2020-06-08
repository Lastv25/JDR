import sys, os

def CleanCharacterFile():
    open(os.path.join(sys.path[0], "characters.txt"), "w+")


def WriteNewCharacter(name, buff, duration):
    if os.path.exists(os.path.join(sys.path[0], "characters.txt")):
        with open(os.path.join(sys.path[0], "characters.txt"), "a+") as f:
            f.write(name+'\t'+buff+'\t'+duration+'\n')
    else:
        with open(os.path.join(sys.path[0], "characters.txt"), "w+") as f:
            f.write(name+'\t'+buff+'\t'+duration+'\n')
    return 0


def getCharacterInfoWithIndex(index):
    with open(os.path.join(sys.path[0], "characters.txt"), "r") as f:
        for position, line in enumerate(f):
            if index == position:
                return line.split("\n")[0].split("\t")


def nextTurn():
    characters_lines = []
    with open(os.path.join(sys.path[0], "characters.txt"), "r") as f:
        for position, line in enumerate(f):
            name, buff, duration = line.split("\n")[0].split("\t")

            if int(duration) != 0:
                duration = str(int(duration)-1)
                if int(duration) == 0:
                    buff = 'None'
            else:
                if buff != 'None':
                    buff = 'None'
            characters_lines.append(name+"\t"+buff+"\t"+duration+"\n")

    with open(os.path.join(sys.path[0], "characters.txt"), "w") as f:
        for i in characters_lines:
            f.write(i)