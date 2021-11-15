months_list = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profits_list = (1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300)

max_profit = max(profits_list)
max_profit_index = profits_list.index(max_profit)

print(max_profit_index)

max_profit_month = months_list[max_profit_index]
print("The Maximum profit of " + str(max_profit) + "was recorded in the month of " + str(max_profit_month))

min_profit= min(profits_list)
min_profit_index = profits_list.index(min_profit)

print(min_profit_index)
min_profit_month = months_list[min_profit_index]
print("The Minimum profit of " + str(min_profit) + "was recorded in the month of " + str(min_profit_month))