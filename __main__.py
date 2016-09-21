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
    client = MongoClient("mongodb://localhost:27017")
    db = client.jrnl

    # prompt for the day's rating
    day_validation = lambda x:  x.isdigit() and int(x) <= 7 and int(x) >= 1
    day_prompt = "Enter the day's rating out of 7: "
    day_error_msg = "Oops, enter an integer between 1 and 7: "

    day_rating = int(collect_validated_input(day_prompt, day_error_msg, day_validation))
    
    db.entries.insert_one({
        "rating": day_rating,
        "timestamp": datetime.datetime.now()
    })
