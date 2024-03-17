
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() 
letter = position[0].lower()
abc = ("a","b","c")
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"
print(f"{line1}\n{line2}\n{line3}")

# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

numberofstudents = 0
for students in student_heights:
  numberofstudents += 1
print(f"number of students = {numberofstudents}")


avg = round(total_height/numberofstudents)
print(f"average height = {avg}")
  


fruits = ["Apple","Peach","Cherry"]
for fruit in fruits:
  print(fruit)
  print(fruit + "pie")


# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
highest_mark = 0
for score in student_scores:
  if score > highest_mark:
    highest_mark = score
print(f"The highest score in the class is: {highest_mark}") 


# Write your code here 👇
target = 100
for number in range(1, target +1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 ==0:
    print("Buzz")
  else:
    print(number)

    
  
  