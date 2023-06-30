# A little project to practice using classes - we have three classes: Menu, Franchise, Business
# Business > Franchise > Menu


# using datetime for the start & end times for each menu 
import datetime

# Menu class
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def calculate_bill(self, purchased_items):
    total = 0
    #self.purchased_items = purchased_items
    for item in purchased_items:
      if item in self.items:
        total += self.items.get(item)
    print("Your Total Bill is £" + str(total))

  def __repr__(self):
    return("{} menu is available from {} until {}".format(self.name, self.start_time, self.end_time))

#Menu details - Brunch, early_bird, dinner, kids, arepas 
brunch = Menu('brunch', {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, datetime.time(11), datetime.time(16))

early_bird = Menu('early_bird', {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}, datetime.time(15), datetime.time(18))

dinner = Menu('dinner', {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}, datetime.time(17), datetime.time(23))

kids = Menu("kids",{'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, datetime.time(11), datetime.time(21))

arepas_menu = Menu("Take a’ Arepa", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, datetime.time(10), datetime.time(20))

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return(self.address)
  
  def available_menus(self, time):
    now = datetime.time(time)
    av_menus = []
    for item in self.menus:
      if item.start_time <= now <= item.end_time:
        av_menus.append(item)
    return(av_menus)

# Our 3 stores:
flagship = Franchise('123 West End Road', [brunch, early_bird, dinner, kids])

new_installment = Franchise('12 East Mulberry Street', [brunch, early_bird, dinner, kids])

arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])



class Business:
  def __init__(self, name, franchise):
    self.name = name
    self.franchise = franchise

# Our 2 businesses
Basta = Business("Basta Fazoolin' with my Heart", [flagship, new_installment])
Arepas = Business("Take a' Arepa", [arepas_place])
