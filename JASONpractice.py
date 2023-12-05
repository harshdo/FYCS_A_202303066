# JSON is commonly used with data APIS. here we can parse JSON into a python dictionary.

import json

# sample JSON
      #userJSON = '{"first_name":"harsh":"last_name":"age":17}'

# Parse to dict

     #user = json.loads(userJSON)

     #print(user)


# turning from dict to JSON.

car = {"make":"Ford","model":"Mustang","Year":1970}

carJSON = json.dumps(car)

print(carJSON)
