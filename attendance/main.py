from pyscript import display, document #type: ignore (quick fix feature)
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)
import matplotlib.pyplot as plt

def graph(e):
    document.getElementById('output').innerHTML=''
    Month = np.array([document.getElementById('input2').value])
    Absentees = np.array([int(document.getElementById('input1').value)])

    Academic_Attendance_Sheet =plt.plot(Month,Absentees , marker='D')

    plt.show(Academic_Attendance_Sheet )
    plt.title("Academic Attendance sheet")
    plt.xlabel("Month")
    plt.ylabel("Absentees")
