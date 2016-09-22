from pymongo import MongoClient
import datetime

def collect_validated_input(prompt, error_msg, validator):
    user_input = input(prompt)
    validated = validator(user_input)

    while not validated:
        user_input = input(error_msg)
        validated = validator(user_input)
    
    return user_input

if __name__=="__main__":
    client = MongoClient()
    db = client.day_entries

    # prompt for the day's rating
    day_validation = lambda x:  x.isdigit() and int(x) <= 7 and int(x) >= 1
    day_prompt = "Enter the day's rating out of 7: "
    day_error_msg = "Oops, enter an integer between 1 and 7: "

    day_rating = int(collect_validated_input(day_prompt, day_error_msg, day_validation))

    # good & bad & ugly
    bad = ""
    if day_rating < 4:
        bad = input("I'm sorry it wasn't a good day!  What went wrong? \n")
    
    good = input("What was one good part about the day? \n")
    ugly = input("What was one thing that you learned or threw you off today? \n")

    db.entries.insert_one({
        "rating": day_rating,
        "timestamp": datetime.datetime.now(),
        "good": good,
        "bad": bad,
        "learned": ugly,
    })
