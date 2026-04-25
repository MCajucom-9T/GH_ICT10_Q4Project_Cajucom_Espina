# Object Oriented Programming
from pyscript import display, document

class Student: 
    def __init__(self, name, section, sub):
        self.name = name
        self.section = section
        self.sub = sub
    
classmates = [Student('Martina', 'Topaz', 'TLE'), 
            Student('Miguel', 'Topaz', 'VE'), 
            Student('Khloe', 'Topaz', 'SS'),
            Student('AJ', 'Topaz', 'ICT'),
            Student('Sim', 'Topaz', 'PE')]

def class_info(e):
    document.getElementById('display1').innerHTML = ''

    name = document.getElementById("input1").value
    section = document.getElementById("input2").value
    sub = document.getElementById("input3").value

    classmate = Student(name, section, sub)
    classmates.append(classmate)

    for classmate in classmates:
        display(f'Hi, I am {classmate.name} from {classmate.section}. My favorite subjects is {classmate.sub}', target='display1')

def introduce(e):
    name = document.getElementById("input1").value

    display(f'We have added {name} to the list.', target='display1')