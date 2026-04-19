# This is all the required imports,
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json
import os

# This is all of the local imports
import APIgroupAppointments
import APIgroupUsers
import APIgroupPets
import Functions

# Print statement for my sanity
print(f"Backend file has successfully loaded")

def PrintLog(self, Location):
    print(f"{self.client_address[0]} called {Location} at {self.path}")

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):

        # API Endpoint for checking if BackEnd is alive and listening
        if self.path == "/API/BackendAlive":
            Functions.BackendAliveCheck(self)
            PrintLog(self, "BackendAliveCheck")


        # API Endpoints for Appointments
        elif self.path == "/API/CreateAppointment":
            APIgroupAppointments.CreateAppointment(self)
            PrintLog(self, "CreateAppointment")
        elif self.path == "/API/GetAppointment":
            APIgroupAppointments.GetAppointment(self)
            PrintLog(self, "GetAppointment")
        if self.path == "/API/ListAppointments":
            APIgroupAppointments.ListAppointments(self)
            PrintLog(self, "ListAppointments")


        # API Endpoints for Pets
        elif self.path == "/API/CreatePet":
            APIgroupPets.CreatePet(self)
            PrintLog(self, "CreatePet")
        elif self.path == "/API/GetPet":
            APIgroupPets.GetPet(self)
            PrintLog(self, "GetPet")
        elif self.path == "/API/ListPets":
            APIgroupPets.ListPets(self)
            PrintLog(self, "ListPets")


        # API Endpoints for Users
        elif self.path == "/API/CreateUser":
            APIgroupUsers.CreateUser(self)
            PrintLog(self, "CreateUser")


        # API Endpoint for Login / Auth
        elif self.path == "/API/LoginAuth":
            Functions.AuthCheck(self)
            PrintLog(self, "LoginAuth")

        # API Endpoint for Reminders
        elif self.path == "/API/ListReminders":
            Functions.ListReminders(self)
            PrintLog(self, "ListReminders")

        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 10000), Handler).serve_forever()
    print(f"Backend server is now listening on port 10000")