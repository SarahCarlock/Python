# Hairstyle Services provided
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
# Services provided per style
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
# Last weeks earnings
total_price = 0
for price in prices:
  total_price += price
print(total_price)
# Average haircut price
average_price = total_price / len(prices)
print("Average Haircut Price: $", average_price)
# Reduce prices by $5
new_prices = [price - 5 for price in prices]
print(new_prices)
# Total Revenue
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] 
  total_revenue += last_week[i]
  print(i)
print("Total Revenue: $", total_revenue)
# Average Daily Revenue
average_daily_revenue = total_revenue / 7
print("Daily Average Sales: $", average_daily_revenue)
# Haircuts under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)