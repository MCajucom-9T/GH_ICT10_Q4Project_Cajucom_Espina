from pyscript import display, document #type: ignore (quick fix feature)
import numpy as np #importing numpy
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR) 
import matplotlib.pyplot as plt #importing matplotlib

def graph(e):
    Month = np.array([document.getElementById('input2').value]) #Gets value of the id
    Absentees = np.array([int(document.getElementById('input1').value)]) #Gets value of the id

    Academic_Attendance_Sheet =plt.plot(Month,Absentees , marker='D')

    plt.show(Academic_Attendance_Sheet ) 
    plt.title("Academic Attendance sheet") #Adds Title
    plt.xlabel("Month") #Adds label for X-Axis
    plt.ylabel("Absentees") #Adds label for Y-Axis
