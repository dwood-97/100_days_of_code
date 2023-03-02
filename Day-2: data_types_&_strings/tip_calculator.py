bill = input("What is the total of your bill? $")
tip = input("What percentage of a tip would you like to leave? ")
split = input("How many people will are splitting the bill? ")
tip_percent = float(tip) / 100 + 1
total = float(bill) / float(split) * float(tip_percent)
each = (float(total))

print(f"$" + format(each,".2f"))