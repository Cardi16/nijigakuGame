import variables
import random
import math
import tkinter as tk
from colored import fg, bg, attr
from tkinter import simpledialog

def spacing():
    print(" ")
    print("===========================")
    print(" ")
def listLoading(list):
    for all in range(len(list)):
        if list is variables.nijigasaki and variables.favorite in list[all]:
            print(f"{all+1}. {list[all]} ☆")
        else:
            print(f"{all + 1}. {list[all]}")
    spacing() # for general list loading
def introScript():
    print("Here are the idols in the Nijigasaki High School Idol Club.")
    print("")
def printFav(aidoru):
    print(f"Your favorite idol is {variables.nijigasaki[aidoru]}, whose associated color is {variables.colors[aidoru]}.")
    spacing()
    listLoading(variables.nijigasaki)
    initialMenu()
def pickFave():
    global favorite
    variables.favorite = (simpledialog.askstring(title="Favorite Idol",
                                      prompt="Out of Nijigasaki's idols, which is your favorite?")).title()
    for all in range(len(variables.nijigasaki)):
        if variables.favorite in variables.nijigasaki[all]:
            printFav(all)
    print(" ")
def loadMenu(menu):
    for those in range(len(menu)):
        print(f"[{those+1}] {menu[those]}") #only use within a menu
    print("")
def loadIdols():
    choice = int(input("Which idol would you like to view the stats of? "))
    spacing()
    choice -= 1
    print(f"Name: {variables.nijigasaki[choice]}\n\nAge: {variables.ages[choice]}\n\nYear: {variables.year[choice]}\n\nSubunit: {variables.subunits[choice]} \n\nDescription: {variables.descriptions[choice]} \n\nQuote: '{variables.quote[choice]}'")
    spacing()
    listLoading(variables.nijigasaki)
    initialMenu()
def initialMenu():
    loadMenu(variables.initial)
    userChoice = int(input("Which do you choose? "))
    if userChoice == 1:
        loadIdols()
    elif userChoice == 2:
        pickFave()
    else:
        print("That was invalid! Try again!")
        initialMenu()