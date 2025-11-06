# What Can I Cook

import requests

API_KEY = "8a98b5cbb9b74ce187cc4f84bcce2fb1"  #my api key bro

print("What do you have in your fridge?")
ingredients = input("Enter your ingredients (separated by commas): ").lower()

#This connect to spooacular 
url = "https://api.spoonacular.com/recipes/findByIngredients"
params = {
    "apiKey": API_KEY,
    "ingredients": ingredients,
    "number": 5,        #number of recipe that will show maximum is 100 but too much la so 10 maybe 5 ionno let do 5 first actually uhm actually i have an idea
    "ignorePantry": True #This ignore common pantry stuff like salt water oil yknow
}

#Get data from the API
response = requests.get(url, params=params)
data = response.json()

#Show recipe results
for recipe in data:
    #the name bro
    print("\n", recipe["title"])
    
    #this is for the ingredient already have dumbass
    used = []
    for item in recipe["usedIngredients"]:
        used.append(item["name"])
    
    #this the missing one dont get confused 
    missed = []
    for item in recipe["missedIngredients"]:
        missed.append(item["name"])
    
    # Print them nicely mwah
    if used:
        print("Used:", ", ".join(used))
    else:
        print("Used: None")

    if missed:
        print("Missing:", ", ".join(missed))
    else:
        print("Missing: Nothing!")

