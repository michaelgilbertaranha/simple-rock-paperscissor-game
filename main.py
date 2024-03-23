import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game=int(input("whom do you choose for rock enter'1',for paper '2',for scissors enter '3'"))
if game == 1:
  print(rock)
elif game ==2:
  print(paper)
else :
  print(scissors)

print("computer generated")
random_t=random.randint(1,3)
if random_t == 1:
  print(rock)
elif random_t==2:
  print(paper)
else :
  print(scissors)


if game==1 and random_t==3:
  print("user wins")
elif game==3 and random_t==2:
  print("user wins!")
elif random_t > game:
  print("computer wins")
elif game==1 and random_t==3:
  print("user wins!")
elif game==3 and random_t==1:
  print("computer wins")
else:
  print("noneofthem wins")
