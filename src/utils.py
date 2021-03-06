from os import path
import json
from platform import system


# Load or create local config file
def configLoad():
    if path.exists('.\smi_config.json'):
        print('   [+] Found .\\smi_config.json, now loading settings')
        with open('.\smi_config.json', 'r') as config_file:
            return json.load(config_file)
    else:
        print('   [-] Did not find .\\smi_config.json, running first time initialization \n')
        return firstTimeInit()


# First Time Init
def firstTimeInit():
    print("[*] Finding \\.minecraft\\mods folder, auto-checking user directory")
    modFolder = findModFolder()

    options = {"modFolder": modFolder}
    print("[*] Creating and writing config file")
    with open(".\smi_config.json", "w") as config_file:
        json.dump(options, config_file)

    return options


# Mod Folder Handle
def findModFolder():
    if system() == "Windows":
        defaultModPath = path.expanduser("~") + '\\AppData\\Roaming\\.minecraft\\mods'
    elif system() == "Linux":
        defaultModPath = path.expanduser("~") + '/.minecraft/mods'
    elif system() == "Darwin":
        defaultModPath = path.expanduser("~") + '/Library/Application Support/minecraft/mods'
    else:
        defaultModPath = None

    modFolder = None
    if path.exists(defaultModPath):
        print('   [+] Found \\mods folder at ' + defaultModPath)
        modFolder = defaultModPath
    else:
        print('   [-] Did not find \\mods folder in ' + defaultModPath)
        validFolder = False
        while not validFolder:
            modFolder = input('   [-] Manually find and input new mods folder: ')
            if path.exists(modFolder):
                validFolder = True
                print('   [+] Valid Folder Inputted')
            else:
                print('   [-] Folder Not Found or Not Valid')

    return modFolder
