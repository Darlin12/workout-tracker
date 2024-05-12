import requests
import datetime
import os


header = {
    "Content-Type": "application/json",
    "x-app-id": os.environ["x-app-id"],
    "x-app-key": os.environ["x-app-key"]
}

query = input("Enter your exercises: ")

parameters = {
    "query": query
}

nutrionix_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutrition_request = requests.post(nutrionix_ENDPOINT, headers=header, json=parameters, )
print(nutrition_request.json()["exercises"][0])

#
# # Post request

# # Get the current system date
current_date = datetime.date.today()

# # Get the current system time
current_time = datetime.datetime.now()

# # Get the hour, minutes, and seconds from the current time
current_hour = current_time.hour
current_minute = current_time.minute
current_second = current_time.second

current_time = f"{current_hour}:{current_minute}:{current_second}"

# # Format the current date as a string
formatted_date = current_date.strftime("%d/%m/%Y")

duration = nutrition_request.json()["exercises"][0]["duration_min"]
exercise = nutrition_request.json()["exercises"][0]["name"]
calories = nutrition_request.json()["exercises"][0]["nf_calories"]
id_ex = nutrition_request.json()["exercises"][0]["tag_id"]


sheety_token = os.environ["sheety_token"]

sheety_header = {
  "Authorization": "Bearer " + sheety_token,
}

body = {
    "workout":
        {
            "date": formatted_date,
            "time": current_time,
            "exercise": exercise.title(),
            "duration": duration,
            "calories": calories,
            "id": id_ex
        }
}
#
sheety_endpoint_post = "https://api.sheety.co/deb7ff997231251be4aef243d25dc75c/myWorkouts/workouts"
sheety_endpoint_get = "https://api.sheety.co/deb7ff997231251be4aef243d25dc75c/myWorkouts/workouts"

# # get data from the G sheet
# get_request = requests.get(sheety_endpoint_get, headers=sheety_header)
# print(get_request.json())

# # post data to the G sheet
post_sheety_request = requests.post(sheety_endpoint_post, json=body, headers=sheety_header)
print(post_sheety_request.json)





