# Numerical Python and MATLAB Plotting Library
from pyscript import display, document
import numpy as np # np is just a common alias
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)
import matplotlib.pyplot as plt


plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()

def smallgraph(e):


    absences = np.array([int(document.getElementById("input").value)])
    month = np.array([(document.getElementById("month").value)])

    Topaz_absence_graph = plt.bar(month, absences)


    plt.show(Topaz_absence_graph)
    plt.title("Topaz's Absenses Over a Month")
    plt.xlabel('Month')
    plt.ylabel('Absences')