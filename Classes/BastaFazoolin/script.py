# At Basta Fazoolin’ with my Heart our motto is simple: when you’re here with family, that’s great! We have four different menus: brunch, early-bird, dinner, and kids. 
#Create a Menu class. 
#Give Menu a constructor with the five parameters self, name, items, start_time, and end_time.
# Give our Menu class a string representation method that will tell you the name of the menu. Also, indicate in this representation when the menu is available.
class Menu():
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
#Give Menu a method .calculate_bill() that has two parameters: self, and purchased_items, a list of the names of purchased items.
#Have calculate_bill return the total price of a purchase consisting of all the items in purchased_items.
# Test out Menu.calculate_bill(). We have a breakfast order for one order of pancakes, one order of home fries, and one coffee. Pass that into brunch.calculate_bill() and print out the price.
  def calculate_bill(self, purchased_items):
    total_price = 0
    for item in purchased_items:
      total_price = total_price + self.items.get(item)
    return "Total price = $" + str(total_price)

  def __repr__(self):
    return self.name + " menu" + "\nfrom " + str(self.start_time) + " to " + str(self.end_time)
# Let’s create our first menu: brunch. Brunch is served from 11am to 4pm. The following items are sold during brunch:
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)
#print(brunch_menu)
# Let’s create our second menu item early_bird. Early-bird Dinners are served from 3pm to 6pm. The following items are available during the early-bird menu:
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu('Early-Bird', early_bird_items, 1500, 1800)
#print(early_bird_menu)
# Let’s create our third menu, dinner. Dinner is served from 5pm to 11pm. The following items are available for dinner:
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu('Dinner', dinner_items, 1700, 2300)
#print(dinner_menu)
# And let’s create our last menu, kids. The kids menu is available from 11am until 9pm. The following items are available on the kids menu.
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_menu = Menu('Kids', kids_items, 1100, 2100)
#print(kids_menu)
brunch_order = Menu.calculate_bill(brunch_menu, ['pancakes', 'home fries', 'coffee'])
#print(brunch_order)
print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
# What about an early-bird purchase? Our last guests ordered the salumeria plate and the vegan mushroom ravioli. Calculate the bill with .calculate_bill().
print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# We’ve decided to create more than one restaurant to offer our fantastic menus, services, and ambience around the country.
# First, let’s create a Franchise class.
# Give our Franchises a string representation so that we’ll be able to tell them apart. If we print out a Franchise it should tell us the address of the restaurant.
class Franchise():
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return self.address
# Give Franchise an .available_menus() method that takes in a time parameter and returns a list of the Menu objects that are available at that time.
# Let’s test out our .available_menus() method! Call it with 12 noon as an argument and print out the results.
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if (time >= menu.start_time and time <= menu.end_time):
        available_menus.append(menu)
    return available_menus
# Let’s create our first two franchises! Our flagship store is located at "1232 West End Road" and our new installment is located at "12 East Mulberry Street". Pass in all four menus along with these addresses to define flagship_store and new_installment.
flagship_store = Franchise('1232 West End Road', [brunch_menu, early_bird_menu, dinner_menu, kids_menu])
new_installment = Franchise('12 East Mulberry Street', [brunch_menu, early_bird_menu, dinner_menu, kids_menu])
#print(Franchise.available_menus(flagship_store, 1200))
#print(Franchise.available_menus(new_installment, 1700))

# Since we’ve been so successful building out a branded chain of restaurants, we’ve decided to diversify. We’re going to create a restaurant that sells arepas!
# First let’s define a Business class.
# Give Business a constructor. A Business needs a name and a list of franchises.
class Business():
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
# Let’s create our first Business. The name is "Basta Fazoolin' with my Heart" and the two franchises are flagship_store and new_installment.
basta_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
# Before we create our new business, we’ll need a Franchise and before our Franchise we’ll need a menu. The items for our Take a’ Arepa available from 10am until 8pm are the following:
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Take a' Arepa", arepas_items, 1000, 2000)
# Next let’s create our first Take a’ Arepa franchise! Our new restaurant is located at "189 Fitzgerald Avenue". Save the Franchise object to a variable called arepas_place.
arepas_place = Franchise('189 Fitzgerald Avenue', arepas_menu)
arepas = Business("Take a' Arepa", arepas_place)
print(arepas.franchises.menus)