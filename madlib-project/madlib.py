
# Madlib Game 
    
import json
# with open("madlibs_template.json") as template:
#     Madlibs_Template = json.load(template)

#Load the Mad Libs Template from a JSON file
Template = open("madlibs_template.json")
Madlibs_Template = json.load(Template)

#Title of the Madlib Game
Title = "Title :  The Monkey King"
print(Title)

#Prompt The User For Input
Verb = input("Enter a verb: ")
Noun = input("Enter a noun: ")
Adjective = input("Enter an adjective: ")
Adverb = input("Enter an adverb: ")

#Fill in the Mad Libs template with user input 
Madlibs = Madlibs_Template["Madlibs_Worksheet"].format(verb=Verb,noun=Noun,adjective=Adjective,adverb=Adverb)

#print the completed Mad Lib
print(Madlibs)
Template.close()