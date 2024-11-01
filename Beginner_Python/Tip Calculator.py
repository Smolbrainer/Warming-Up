total = float(input("What the total before tax? "))
numberOfPeople = int(input("How many people is bill split up between? "))
tax = .13 * total
totalAfterTax = total + tax
billPerPerson = totalAfterTax/numberOfPeople
print(f"Assuming the tax is 13% it would be {tax}$ which would make the total {totalAfterTax}$ and each person would pay {billPerPerson}$")