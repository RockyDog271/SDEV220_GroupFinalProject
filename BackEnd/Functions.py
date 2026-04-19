import urllib.request
import string
import random
import json
import os

def AuthCheck(handler):
    # Getting the file path~
    FilePath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Data", "Users.json"))

    def CheckCredentials(Username, Password, FilePath):
        AuthStatus = "DENIED"
        # \/ opening the .json file and also the loading of it
        with open(FilePath, "r") as File:
            UserData = json.load(File)
        # \/ Checking ID/HASH logic below
        for User in UserData.get("Users", []):
            if User.get("UserID") == Username:
                if User.get("PasswordHASH") == Password:
                    AuthStatus = "APPROVED"
                    return AuthStatus
                else:
                    AuthStatus = "DENIED"
                    return AuthStatus
        return AuthStatus
       
    try:
        # Reading the .post.
        ContentLength = int(handler.headers.get("Content-Length", 0))
        Body = handler.rfile.read(ContentLength)
        Data = json.loads(Body.decode("utf-8"))

        # Assigning Vars from .post.
        Username = Data.get("UserID")
        Password = Data.get("PasswordHASH")
        AuthStatus = "DENIED" 

        # Call the function to check the .json file :3
        AuthStatus = CheckCredentials(Username, Password, FilePath)

        # Create the data file in prep for response
        data = {
            "Status": AuthStatus
        }

        # Convert data to JSON and encode it
        body = json.dumps(data).encode("utf-8")
        # Send the response
        handler.send_response(200)
        handler.send_header("Content-Type", "application/json")
        handler.send_header("Content-Length", str(len(body)))
        handler.end_headers()
        handler.wfile.write(body)

    # This is a good example of how not to handle errors :3c
    except:
        # Create the data file in prep for response
        data = {
            "Status": "DENIED"
        }

        # Convert data to JSON and encode it
        body = json.dumps(data).encode("utf-8")
        # Send the response
        handler.send_response(500)
        handler.send_header("Content-Type", "application/json")
        handler.send_header("Content-Length", str(len(body)))
        handler.end_headers()
        handler.wfile.write(body)


def BackendAliveCheck(handler):
    pass

def ListReminders(handler):
    pass
 #// RETURNS
 #Appointment .json(s)
 #// see Appointment_xxxxxxx.json for exact return

def CreateID():
    # Getting the file path~
    FilePath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Data", "IDlist.txt"))

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