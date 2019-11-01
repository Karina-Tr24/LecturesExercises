#!/usr/bin/python3
import os, sys, subprocess, shutil

def interrogation(name,age,colour,py,world):
  import string
  print("You have provided the following details:\n\tName: ",name,"\n\tAge: ",age,"\n\tFave colour: ",colour,"\n\tPython preference: ",py,"\n\tFlat world: ",world)
  World = {'True' : 'Go to school again please :(', 'False' : 'Yes, that is right'}
  wfa=World[world]
  print(wfa)

details={}
details["Name"]   = input("Hi, what is your name? ")
details["Age"]    = int(input("How old are you? "))
details["Colour"] = input("What's your favourite colour? ")
details["Python"] = input("Do you like Python? ")
details["World"]  = input("The world is flat: True or False? ")

interrogation(*list(details.values()))

print("\n\nThis was the dictionary you set up...\n\n",details,"\n\nBye!\n\n")
exit()