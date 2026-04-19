from ast import While
import string
import random
import json
import os

def AuthCheck(handler):
    pass
#// RETURNS
#“APPROVED” / “DENIED”

def BackendAliveCheck(handler):
    pass

def ListReminders(handler):
    pass
#// RETURNS
#Appointment .json(s)
#// see Appointment_xxxxxxx.json for exact return

def CreateID():
    # Getting the file path~
    FilePath = os.path.join(os.getcwd(), "IDlist.txt")

    # I don't remember what \/ does
    if not os.path.exists(FilePath):
        with open(FilePath, "w") as File:
            pass
    
    while True:
        # 3x random uppercase letters \/
        Letters = "".join(random.choices(string.ascii_uppercase, k = 3))
        # 4x random digits/numerals \/
        Numerals = "".join(random.choices(string.digits, k = 4))
        # Combining them \/
        IDval = Letters + Numerals

        with open(FilePath, "r") as File:
            IDlist = {line.strip() for line in File if line.strip()}
            # Thanks to my friend for writing /\, strings are hard >~<
        if IDval not in IDlist:
            with open(FilePath, "a") as File:
                File.write(IDval + "\n")
        return IDval
 # Call function as follows;
 # import Functions
 # Var = Functions.CreateID()