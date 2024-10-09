import datetime as dt
from decimal import Decimal
from random import randint, choice
from custom_module import generate_time_travel_message

# Calculate current date and time
date = dt.date.today().strftime('%m/%d/%y')
year = dt.date.today().strftime('%Y')
time = dt.datetime.now().time().strftime('%I:%M%p')
# Calculate the Time Travel Cost
baseCost = Decimal('10.00')
randomTargetYear = randint(1800, 2023)
desination = ["France", "Spain", "Russia", "Africa", "South America", "Antartica"]
destination = choice(desination)
def costMultiplier(randomTargetYear, baseCost):
  startDate = dt.datetime.now().strftime('%Y')
  travelDate = randomTargetYear
  diff = (int(startDate) - travelDate)* int(baseCost)
  round(diff)
  return diff

print(generate_time_travel_message(randomTargetYear, destination, costMultiplier(randomTargetYear, 1)))

