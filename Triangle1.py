#math is important for trig functions and tkinter to draw the triangle
import math 
from tkinter import *

#while loop is True, the code will execute again from top to bottom enabling try_again()
loop = True

while loop == True:
  #These chips are used as placeholder variables for while loops
  cheetos = True
  pringles = True

  #Setting some various variabls to meet certain conditions
  angleTheory = ""
  lengthTheory = ""
  angle_ab = -1
  length_a = -1
  length_b = -1

  #Returns the code to its original state
  def try_again():

    global loop
    global cheetos
    global pringles
    global angleTheory
    global lengthTheory
    global angle_ab
    global length_a
    global length_b

    doritos = True
    
    while doritos == True:
      user_input = input("\nTry again?(y/n)")
      try:
        if user_input.lower() == 'y':
          cheetos = True
          pringles = True
          angleTheory = ""
          lengthTheory = ""
          angle_ab = -1
          length_a = -1
          length_b = -1
          doritos = False
        elif user_input.lower() == 'n':
          print("\nSee ya next time! :)")
          doritos = False
          loop = False
      except:
        pass

  #A brief explanation on angle sum theorem
  print("Angle sum theorem uses two angles and a side length to determine its type of triangle and measurements\n")

  #prompts user if they want to use angle sum theorem or not and sets some variables to trigger next action
  while pringles == True:
    angleTheory = input("Use angle sum theorem?(y/n)")
    try:
      if angleTheory.lower() == 'y':
        pringles = False
        cheetos = False
        angle_a = -1
        angle_b = -1
        length_aa = -1
      elif angleTheory == 'n':
        angle_a = 1
        angle_b = 1
        length_aa = -1
        pringles = False
    except:
      pass

  #A brief explanation on length angle theorem 
  if angleTheory == 'n':
    print("\nLength angle theorem use two sidelengths and the angle between them to calculate the third sidelength and discerns the last side.\
 Also, it will be able to discern the type of triangle and draw it. \n")

  #Checks to see if the user's input was y, n, or neither and either stops the loop when given a suficient answer or keeps on goin
  while cheetos == True:
    if angleTheory == 'n':
      lengthTheory = input("Use length angle theorem? (y/n)")
    try:
      if lengthTheory == 'y':
        cheetos = False
      elif lengthTheory == 'n':
        print("\nSee ya next time! :)")
        cheetos = False
        loop = False
    except:
      pass

  #Prompts user to input two angles
  def angle_input():
    
    #Calls these global variables from outside the function
    global angle_a
    global angle_b
    global length_aa
    
    #Checks to see if the angle is between 0 and 180 and if it can turn into a float
    if angleTheory.lower() == 'y':
      while angle_a <= 0 or angle_a >= 180:
        try:
          angle_a = float(input("Please input an angle between 0 and 180: "))
        #Normally if you try to float() anything that isnt a number, the code will stop and return ValueError,
        #To get around it the except makes an exception if the error were to arise and not stop the code
        except ValueError:
          print ("Not valid angle")
    
      while angle_b <= 0 or angle_b >= 180:
        try:
          angle_b = float(input("Please input a second angle between 0 and 180: "))
        except ValueError:
          print ("Not valid angle")
      
      while length_aa < 5 or length_aa > 40:
        try:
          length_aa = float(input("Please input a length greater than 5 or less than or equal to 40: "))
        except ValueError:
          print("Not valid length")
          

  #Runs the function
  angle_input()

  #If the two user inputted angles add up to 180 or higher, it'll return an error message and prompt them again
  while angle_a + angle_b >= 180:
    print("\nError, angles 1 and 2 add up to or over 180")
    print("Please input two angles again")
    angle_a = -1
    angle_b = -1
    angle_input()
    
  #Angle Sum Theory: The sum of all angles in a triangle add up to 180
  angle_c = 180 - angle_a - angle_b

  #Identifies the type of triangle using a series of if and elif statements
  def angle_triangle(a, b, c, A):
    if a == b == c:
      print("You've got an equilateral triangle!")
    elif a == 90 or b == 90 or c == 90:
      if a != b != c:
        print("You've got a right, scalene triangle!")
      else:
        print("You've got a right, isoscelese triangle!")
    elif a != b != c:
      print("You've got a scalene triangle!")
    elif a == b or a == c or b == c:
      print("You've got an isoscelese triangle!")

    #Sorts the angles in a list from greatest to least
    list_angle = [a,b,c]
    list_angle.sort(reverse=True)

    #Uses sine law to find missing side lengths
    B = math.sin(math.radians(list_angle[1])) * A / math.sin(math.radians(list_angle[0]))
    C = math.sin(math.radians(list_angle[2])) * A / math.sin(math.radians(list_angle[0]))

    #sorts the lengths in a list from greatest to least
    list_length = [A,B,C]
    list_length.sort(reverse=True)

    #Prints the side lengths and angles nicely with appropiate measurements
    print ("Side lengths: " + str(A) + "cm, " + str(round(B, 2)) + "cm, " + str(round(C, 2)) + "cm")
    print ("Angles: " + str(round(a, 4)) + "°, " + str(round(b, 2)) + "°, " + str(round(c, 2)) + "°")


    #Finds the components of the second and third lines using trig ratios
    x = list_length[0]
    l_y = list_length[1] * (math.sin(math.radians(list_angle[2])))
    l_x = list_length[1] * (math.cos(math.radians(list_angle[2])))
    l_x2 = list_length[2] * (math.cos(math.radians(list_angle[1])))
    l_y2 = list_length[2] * (math.sin(math.radians(list_angle[1])))

    #The beginning of tkinter stuff
    master = Tk()

    #Creates a frames inside the master window so the scrollbar can be placed in it so it actually scrolls
    frame = Frame(master, width=800, height=500)
    frame.grid(row=0, column=0)

    #Creates a canvas where the drawing will happen 
    w = Canvas(frame, bg = '#FFFFFF', width=800, height=500, scrollregion=(0,0,1550,800))

    #Creates the horizontal scrollbar and configures it
    hbar = Scrollbar(frame, orient=HORIZONTAL)
    hbar.pack(side=BOTTOM, fill= X)
    hbar.config(command=w.xview)

    #Creates the vertical scrollbar and configures it
    vbar = Scrollbar(frame, orient=VERTICAL)
    vbar.pack(side=RIGHT, fill=Y)
    vbar.config(command=w.yview)

    #Enables the scrollbars to actually scroll
    w.config(width= 800, height= 500)
    w.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    w.pack(side=LEFT, expand =True, fill= BOTH)

    #Creates lines using 3 coordinates and some maths to find where the coordinates are relative to the origin
    w.create_line(4, 30, (x*37.795275591) + 4, 30, fill="#476042", width=3)
    w.create_line((x*37.795275591) + 4, 30, (x*37.795275591) + 4 - (l_x*37.795275591),(l_y*37.795275591) + 30, fill="#476042", width=3)
    w.create_line((x*37.795275591) + 4 - (l_x*37.795275591), (l_y*37.795275591) + 30,4, 30, fill="#476042", width=3)

    #Creates text labelling the angles on the triangle using coordinates
    w.create_text(20,10, text=str(round(list_angle[1], 2)) + "°")
    w.create_text(x*37.795275591 + 4, 10, text=str(round(list_angle[2], 2)) + "°")
    w.create_text((x*37.795275591) + 4 - (l_x*37.795275591),(l_y*37.795275591) + 50, text= str(round(list_angle[0], 2)) + "°")

    #Creates text labelling the lengths on the triangle using coordinates
    w.create_text(x*37.795275591/2 + 4, 10, text=str(round(list_length[0], 2)) + "cm")
    w.create_text((x*37.795275591) - (l_x*37.795275591) / 2, ((l_y*37.795275591) + 30 )/ 2, text= str(round(list_length[1], 2)) + "cm")
    w.create_text((l_x2 * 37.795275591) / 2 + 30, (l_y2*37.795275591) / 2 + 30, text= str(round(list_length[2], 2)) + "cm")

    mainloop()

    try_again()

  #calls the triangle identifying function if the user said they wanted to use it
  if angleTheory.lower() == 'y':      
    angle_triangle(angle_a, angle_b, angle_c, length_aa)

  #Defines a function that asks the user for two sidelengths and an angle
  def length_input():
    
    global length_a
    global length_b
    global angle_ab
    
    if lengthTheory.lower() == 'y':
      while length_a < 3 or length_a > 20:
        try:
          length_a = float(input("Please input a length greater than 3 and less than or equal to 20: "))
        except ValueError:
          print("Please enter a valid input")
      
      while length_b < 3 or length_b > 20:
        try:
          length_b = float(input("Please input a second length greater than 3 and less than or equal to 20: "))
        except ValueError:
          print("Please enter a valid number")
          
      while angle_ab >= 180 or angle_ab <= 0:
        try:
          angle_ab = float(input("Please input an angle between 0 and 180: "))
        except ValueError:
          print("Please enter a valid number")
          
  #Runs said function
  length_input()

  #Defines another function that determines the type of triangle and draws it
  def length_angle_calc(a, b, C):
    #Uses cosine law to find the missing side length and an angle
    c = math.sqrt((a ** 2 + b ** 2) - (2 * a * b * math.cos(math.radians(C))))
    B = math.acos((c**2 + a**2 - b**2) / (2 * c * a))
    #All triangles have 3 angles that add up to 180°
    A = float(180 - math.degrees(B) - C)
    #converts the angle from radians to degrees
    B = round(math.degrees(B), 6)

    #Rounds the sidelengths since they may be 0.00001 off from each other because of math rounding errors
    a = round(a, 4)
    b = round(b, 4)
    c = round(c, 4)

    #Prints the side lengths, angles, and type of triangle
    print ("Side lengths: " + str(a) + "cm, " + str(b) + "cm, " + str(c) + "cm")
    print ("Angles: " + str(round(A, 4)) + "°, " + str(round(B, 4)) + "°, " + str(round(C, 4)) + "°")
    #If and elif statements that compare the lengths and angles to each other to discern the triangle
    if A == 90 or B == 90 or C == 90:
      if A != B  and A != C and B != C:
        print("You've got a right scalene triangle!")
      elif A == B or B == C or A == C:
        print("You've got a right isoscelese triangle!")
      else:
        print("ERROR: 1")
    elif A == B == C:
      print("You've got an equilateral triangle!")
    elif A != B != C:
      print("You've got a scalene triangle!")
    elif A == B or A == C or B == C:
      print("You've got an isoscelese triangle!")
    else:
      print("ERROR: 2")

    #From here on is a repeat from the angle function
    list_length = [a,b,c]
    list_length.sort(reverse=True)
    list_angle = [A,B,C]
    list_angle.sort(reverse=True)



    x = list_length[0]
    l_y = list_length[1] * (math.sin(math.radians(list_angle[2])))
    l_x = list_length[1] * (math.cos(math.radians(list_angle[2])))
    l_x2 = list_length[2] * (math.cos(math.radians(list_angle[1])))
    l_y2 = list_length[2] * (math.sin(math.radians(list_angle[1])))
    

    master = Tk()

    frame = Frame(master, width=800, height=500)
    frame.grid(row=0, column=0)
    
    w = Canvas(frame, bg = '#FFFFFF', width=1200, height=800, scrollregion=(0,0,1550,800))
    
    hbar = Scrollbar(frame, orient=HORIZONTAL)
    hbar.pack(side=BOTTOM, fill= X)
    hbar.config(command=w.xview)

    vbar = Scrollbar(frame, orient=VERTICAL)
    vbar.pack(side=RIGHT, fill=Y)
    vbar.config(command=w.yview)

    w.config(width= 800, height= 500)
    w.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    w.pack(side=LEFT, expand =True, fill= BOTH)



    w.create_line(4, 30, (x*37.795275591) + 4, 30, fill="#B22222", width=3)
    w.create_line((x*37.795275591) + 4, 30, (x*37.795275591) + 4 - (l_x*37.795275591),(l_y*37.795275591) + 30, fill="#B22222", width=3)
    w.create_line((x*37.795275591) + 4 - (l_x*37.795275591), (l_y*37.795275591) + 30,4, 30, fill="#B22222", width=3)

    w.create_text(20,10, text=str(round(list_angle[1], 2)) + "°")
    w.create_text(x*37.795275591 + 4, 10, text=str(round(list_angle[2], 2)) + "°")
    w.create_text((x*37.795275591) + 4 - (l_x*37.795275591),(l_y*37.795275591) + 50, text= str(round(list_angle[0], 2)) + "°")

    w.create_text(x*37.795275591/2 + 4, 10, text=str(round(list_length[0], 2)) + "cm")
    w.create_text((x*37.795275591) - (l_x*37.795275591) / 2, ((l_y*37.795275591) + 30 )/ 2, text= str(round(list_length[1], 2)) + "cm")
    w.create_text((l_x2 * 37.795275591) / 2 + 30, (l_y2*37.795275591) / 2 + 30, text= str(round(list_length[2], 2)) + "cm")


    mainloop()
    #Runs try_again()
    try_again()

  #runs the function prior
  if lengthTheory == 'y':  
    length_angle_calc(length_a, length_b, angle_ab)


