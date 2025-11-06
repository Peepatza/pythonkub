#        WHAT CAN I COOOOK

import requests

api_key = "8a98b5cbb9b74ce187cc4f84bcce2fb1"  #my api key bro

print("What do you have in your fridge?")
ingredients = input("Enter your ingredients (type it separated by commas): ").lower()

if ingredients == "":
    print("You didn't enter any ingredients,come on now are your really hungry?") #first fix###########

ingredient_list = ingredients.split(",")  #third fix bro y did i skip this
beautiful_ingredient = []
for item in ingredient_list:
    beautiful_ingredient.append(item.strip())
ingredients = ",".join(beautiful_ingredient)

#This connect to spooacular 
url = "https://api.spoonacular.com/recipes/findByIngredients"
params = {
    "apiKey": api_key,
    "ingredients": ingredients,
    "number": 5,        #number of recipe that will show maximum is 100 but too much la so 10 maybe 5 ionno let do 5
    "ignorePantry": True #This ignore common pantry stuff like salt water oil yknow
}

#Get data from the API
response = requests.get(url, params=params)
data = response.json() #recieve the json file from spoonacular id, name, useIn, and missIn

if len(data) == 0:
    print("Enter a real ingredient bro") #second fix bruh

#Show recipe results
for recipe in data: #start the loop gang one loop per recipe maybe hopefully
    #the name bro
    print("\n", recipe["title"])
    
    #this is for the ingredient already have
    used = []
    for item in recipe["usedIngredients"]:  #Capital I because the key is written in it so gotta deal with it
        used.append(item["name"])
    
    #this the missing one
    missed = []
    for item in recipe["missedIngredients"]: #same as the one above
        missed.append(item["name"])
    
    # Print them nicely mwah!!
    if used:
        print("Used:", ", ".join(used))
    else:
        print("Used: None")

    if missed:
        print("Missing:", ", ".join(missed))
    else:
        print("Missing: Nothing!")

