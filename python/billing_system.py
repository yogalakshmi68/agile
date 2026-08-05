#Billing_system.py
print("====== Billing System ======")

customer = input("Enter Customer Name: ")

item1 = input("Enter Item 1 Name: ")
price1 = float(input("Enter Item 1 Price: "))

item2 = input("Enter Item 2 Name: ")
price2 = float(input("Enter Item 2 Price: "))

item3 = input("Enter Item 3 Name: ")
price3 = float(input("Enter Item 3 Price: "))

total = price1 + price2 + price3
gst = total * 0.18
final_amount = total + gst

print("\n------ BILL ------")
print("Customer:", customer)
print(item1, ":", price1)
print(item2, ":", price2)
print(item3, ":", price3)
print("Total:", total)
print("GST (18%):", gst)
print("Final Amount:", final_amount)
print("===================")
