# Object Oriented Programming
from pyscript import display, document

class Student: 
    def __init__(self, name, section, sub): # "__init__" : constructor in OOP 
        self.name = name
        self.section = section
        self.sub = sub
    
classmates = [Student('Martina', 'Topaz', 'TLE'), 
            Student('Miguel', 'Topaz', 'VE'), 
            Student('Khloe', 'Topaz', 'SS'),
            Student('AJ', 'Topaz', 'ICT'),
            Student('Sim', 'Topaz', 'PE')] # List

def class_info(e):
    document.getElementById('display1').innerHTML = '' #Refreshes everytime button is pressed

    name = document.getElementById("input1").value #Gets value from the input
    section = document.getElementById("input2").value  #Gets value from the input
    sub = document.getElementById("input3").value  #Gets value from the input

    classmate = Student(name, section, sub) #Creates the new input
    classmates.append(classmate) #Adds the variable to the list

    for classmate in classmates:
        display(f'Hi, I am {classmate.name} from {classmate.section}. My favorite subjects is {classmate.sub}', target='display1') # displays new classmate into the list

def introduce(e):
    name = document.getElementById("input1").value

    display(f'We have added {name} to the list.', target='display1')
