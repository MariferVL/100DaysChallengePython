#Bill Splitter

print("Welcome to the Bill Splitting calculator.")
totalBill = float(input("What was the total bill?: $"))
consumers = int(input("How many people to split the bill?:  "))
tip = int(input("What percentage tip would you like to give?: %"))
split = (round(float(((tip / 100 +1) * totalBill) / consumers), 2))
print(f"Each person should pay: ${split}")
print(f"The detail per person: \n Bill: ${round(totalBill/consumers)} \n"
      f" Tip: ${round(tip/consumers)}\n__________________________ \n Total each: ${split}")




