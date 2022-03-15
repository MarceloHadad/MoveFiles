import os


def moveFiles(sourceFolder, destinationFolder, patternToUse):
    os.chdir(sourceFolder)

    putQuotesIfWordHasSpaces(patternToUse)

    curDir = os.getcwd()
    print(f"Searching for {patternToUse} in {curDir}")

    cmdCommand = f'cmd /c "move {patternToUse} {destinationFolder}"'
    os.system(cmdCommand)
    obj = os.scandir(sourceFolder)

    for entry in obj:
        if entry.is_dir():
            path = f"{sourceFolder}\{entry.name}"
            if path != destinationFolder:
                moveFiles(path, destinationFolder, patternToUse)

    obj.close()


def getPatternFromFolders(srcFolder, dstFolder, patternOpt):

    PatternFolders = os.scandir(dstFolder)
    for entry in PatternFolders:
        if entry.is_dir() and srcFolder != entry.name:
            curDestFolder = putQuotesIfWordHasSpaces(
                f"{dstFolder}\{entry.name}")
            patternToUse = formatPattern(patternOpt, entry.name)
            moveFiles(srcFolder, curDestFolder, patternToUse)
    
    PatternFolders.close()


def validatePath(path):
    if path == "":
        print("Folder path cannot be NULL")
        quit()

    else:
        putQuotesIfWordHasSpaces(path)

    return path


def putQuotesIfWordHasSpaces(word):
    if ' ' in word:
        word = '"' + f"{word}" + '"'

    return word


def formatPattern(patternOption, word):
    formatedPattern = word
    match patternOption:
        case 1:
            return formatedPattern
        case 2:
            return f"*{formatedPattern}"
        case 3:
            return f"{formatedPattern}*"
        case 4:
            return f"*{formatedPattern}*"


def main():
    print("Press enter if you want to use a destination folder as a pattern OR type a pattern to search:")
    patternToUse = input()
    print("Type the source folder path:")
    src_folder = validatePath(input())
    print("Type the destination folder path:")
    dst_folder = validatePath(input())

    if (patternToUse == ""):
        print("Choose the pattern to search for:\n"
            + "1- folder name\n"
            + "2- *folder name\n"
            + "3- folder name*\n"
            + "4- *folder name*\n")
        patternOption = int(input())

        getPatternFromFolders(src_folder, dst_folder, patternOption)

    else:
        moveFiles(src_folder, dst_folder, patternToUse)


if __name__ == "__main__":
    main()