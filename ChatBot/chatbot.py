print("Hello my name is kak tebe ugodno")
print("I was created in 2021")
print('Please, remind me your name')
name = str(input())
print('What a great name you have, ' + name +  "!")
print("Let me guess your age")
print("Enter remainders of divining your age by 3, 5 and 7")
a = int(input())
b = int(input())
c = int(input())
age = (a*70+b*21+c*15)%105
print("Your age is " + str(age) +  " that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
num = int(input())
for i in range(num):
    print(i, end="! \n" )
print("Completed, have a nice day!")

print("""

What is phyton?

1.Snake
2.programming language
3.reception in the fight
""")
def answers(my_answer):
    answer = int(input())
    if answer == 2:
        print("Congratulations, have a nice day!")
    else:
        print("Please, try again.")
        answers("1")
answers("2")

