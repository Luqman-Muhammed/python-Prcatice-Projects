Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0


print('======== Sorting Hat =========')

#Question 1

print("\nQ1) Do you like Dawn or Dusk?")
print(' 1) Dawn')
print(' 2) Dusk')

answer = int(input('Enter numbers (1-2): '))

if answer == 1:
    Gryffindor += 1
    Ravenclaw += 1

elif answer == 2:
    Hufflepuff += 1
    Slytherin += 1

else:
    print('Wrong input')

#Question 2

print("\nQ2) When Im dead, I want people to remember me as:")
print(' 1) The Good')
print(' 2) The Great')
print(' 3) The Wise')
print(' 4) The Bold')

answer = int(input('Enter numbers (1-4): '))

if answer == 1:
    Hufflepuff += 2

elif  answer == 2:
     Slytherin += 2

elif answer == 3:
     Ravenclaw += 2

elif answer == 4:
      Gryffindor += 2

else:
    print('Wrong input')
    
#Question 3

print("\nQ3) Which kind of instrument most pleases your ear?")
print(' 1) The violin')
print(' 2) The trumpet')
print(' 3) The piano')
print(' 4) The drum')

answer = int(input('Enter the numbers from(1-4): '))

if answer == 1:
   Slytherin += 4

elif answer == 2:
    Hufflepuff += 4

elif answer == 3:
    Ravenclaw += 4

elif answer == 4:
    Gryffindor += 4

else:
    print('Wrong input')

most_points = max(Gryffindor,Hufflepuff,Slytherin,Ravenclaw)

if Gryffindor == most_points:
    print("\n🦁 Gryffindor has the most points")

elif Ravenclaw == most_points:
    print("\n🦅 Ravenclaw has the most points")

elif Hufflepuff == most_points:
    print("\n🦡 Hufflepuff has the most points")

else:
    print("\n🐍 Slytherin has the most points")