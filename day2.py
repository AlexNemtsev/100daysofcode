print('Welcome to the tip calculator!')
bill = float(input("What was the total bill? $"))
tips = int(input('How much tip would you like to give? 10, 12, or 15? ')) / 100
people = int(input('How many people to split the bill? '))

total = bill / people * (1 + tips)

print(f'Each person should pay: ${total :1.2f}')