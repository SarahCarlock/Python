# Weight of package to ship
weight = 69

# Intro to include in message
intro = "The package weighs " + str(weight) + "lb. "
print(intro)

# Ground Shipping
ground ="Sent by ground, the cost will be $"
if (weight <= 2 ):
  cost_GroundShipping = weight * 1.5 + 20
  print(ground + str(cost_GroundShipping))
elif (weight > 2) and (weight <=6):
  cost_GroundShipping = weight * 3 + 20
  print(ground + str(cost_GroundShipping))
elif (weight > 6) and (weight <= 10):
  cost_GroundShipping = weight * 4 + 20
  print(ground + str(cost_GroundShipping))
elif (weight > 10):
  cost_GroundShipping = weight * 4.75 + 20
  print(ground + str(cost_GroundShipping))
else:
  print("Error")

# Ground Shipping Premium
groundShippingPremium = "To send with Premium Ground Shipping there is a Flat charge of $125"
print(groundShippingPremium)

# Drone Shipping
drone = "Sent by drone, the cost will be $"
if (weight <= 2):
  cost_droneShipping = weight * 4.5
  print(drone + str(cost_droneShipping))
elif (weight > 2) and (weight <= 6):
  cost_droneShipping = weight * 9
  print(drone + str(cost_droneShipping))
elif (weight > 6) and (weight <= 10):
  cost_droneShipping = weight * 12
  print(drone + str(cost_droneShipping))
elif (weight > 10):
  cost_droneShipping = weight * 14.25
  print(drone + str(cost_droneShipping))
else:
  print("Error")
