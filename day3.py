# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names = name1 + name2
true = 0
love = 0

for ch in 'TRUE':
    true += names.lower().count(ch.lower())

for ch in 'LOVE':
    love += names.lower().count(ch.lower())

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif score > 40 and score < 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')