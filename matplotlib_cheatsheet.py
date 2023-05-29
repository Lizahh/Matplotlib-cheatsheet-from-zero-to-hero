# -*- coding: utf-8 -*-
"""Matplotlib - Cheatsheet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V3I3zQ7l30pDlLmScXJOjUOWK1JOcOSc

# **Introduction:**

1.**Matplotlib is known as the 'Grand father' of plotting and visualization libraries for Python** *(because many other libraries e.g. seaborn and Pandas are built directly off Matplotlib for visualization)*

2. There are 2 approaches to create plots:

  * **Functional-based methods** (Matplotlib Basics)
  * **OOP (classes) based methods** (Matplotlib figures and subplots)

# **Part A: Matplotlib Basics (using Functional Based Methods)**
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,20)
y = 2 * x

plt.plot(x,y) # Using plot call of matplotlib is most basic way of using matplotlib, but it doesn't allow for very high degree of control.

"""**Nota Bene:** If we don't write plt.show() in jupyter notebook, it will give us this extra line:

> [<matplotlib.lines.Line2D at 0x7f4018fa5c90>]

which shows the location of this plot in the memory. But, we definitely don't need it. So, it has two methods to remove this line:

1. Write **plt.show()** so this line won't show along with plot.
2. Add semicolon ' ; ' at the end of plt.plot() or whatever statement is the last statement of the code which would only show the plot.

"""

# METHOD 1

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,20)
y = 2 * x

plt.plot(x,y)
plt.show()  # write it very end of the code

"""Woah! that extra line is gone."""

# METHOD 2

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,20)
y = 2 * x

plt.plot(x,y); # SEMICOLON ADDED

"""## **Enhancing Plot Visualizations: Adding Titles, Labels, and More:**"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,20)
y = 2 * x

plt.plot(x,y)

plt.title('Simple plotting')

plt.xlim(0,6) # Min limt on x-axis: 0 and maximum limit on x-axis: 6
plt.ylim(0,15)  # Min limt on y-axis: 0 and maximum limit on y-axis: 15

plt.xlabel('X Axis')
plt.ylabel('Y Axis') 

#  --- to save plot in current working directory ---

# bbox_inches='tight' will save the axes also, along with figure. 
# Otherwise only figure will be saved without axes which will look weird.

plt.savefig('Myfirstplot.png', bbox_inches = 'tight');

"""# **Part B: Figure object in Matplotlib (using OOP Based Methods):**

**Purpose:**

  * The purpose of the 'figure object' in Matplotlib is to serve as a container that holds all the elements of a plot, such as axes, labels, legends, and other graphical elements. 

  * It represents the entire plotting area or canvas on which visualizations are created.
"""

plt.figure()

"""The figure object is technically not visible untill we add axes to it. Because it is a blank canvas, waiting for the axes.

Let's add a figure of size (10,10) in this canvas:
"""

fig = plt.figure()
fig.add_axes([0,0,1,1])

"""In ([0,0,1,1]):

  * **0, 0:** First two zeros show the lower left corner of axes. If its 0,0 it means it should start from origin. Lets change it to 4,5. 

  * **1:** This 1 shows the width of x-axis, means use 100% width of canvas. Here, 1 = 100%. 0.9 = 90% etc.

  * **1:** This last 1 shows the height of y-axis, means use 100% height of canvas. Here, 1 = 100%. 0.9 = 90% etc.
"""

fig = plt.figure()

fig.add_axes([0,0,0.5,0.2]) # It means, use 50% width and 20% height of the canvas !

# Lets plot the data

fig = plt.figure()

axes = fig.add_axes([0,0,0.5,0.2])

# plotting the data
axes.plot(x,y);   # --- DON'T FORGET TO ADD SEMICOLON, TO SEE ONLY PLOT ---

"""We can also add multiple axes in the same figure (canvas). Ofcourse we can!"""

import numpy as np

a = np.linspace(0,10,11)
b = a * 4

fig = plt.figure()

# plotting first data
axes1 = fig.add_axes([0,0,1,1])
axes1.plot(x,y)
axes1.set_title("I am the First axes (Zoomed out)") # use set_title (not .title() function) while working in canvas
axes1.set_xlabel('x')   # use set_xlabel (not .xlabel() function) while working in canvas
axes1.set_ylabel('y')   # use set_ylabel (not .ylabel() function) while working in canvas

# plotting second data

axes2 = fig.add_axes([0.2, 0.2, 0.5, 0.5])
axes2.plot(a,b)
axes2.set_title("I am the Second axes (Zoomed in)")
axes2.set_xlabel('a')   
axes2.set_ylabel('b'); # Semicolon added at the end of last line to show only plot

"""*Nota Bene: Note that the second axes (axes2) is starting from 0.2 on x-axis and 0.2 on y-axis of main canvas.*

## **Figure (Canvas) Parameters:**

We can add dots per inch (dpi) in the figure object and can also set the size of canvas using 'figsize' parameter. dpi makes the image more thicker.
"""

fig = plt.figure(figsize = (9,3), dpi = 200)

axes = fig.add_axes([0,0,0.5,0.5])
axes.plot(x,y);

"""Now see above the magic of dpi and setting the canvas size to (9,3) where 9:3 is the ratio of height and width (means width is 3-times bigger than height).

# **Part C: Advanced - Subplot Functionality**

* Adding axes to figure object (canvas) and then arranging them in axis, is very hectic. 

* Matplotlib has a pre-configuration function for it called plt.subplots() that automatically does this for us :)))

* Just tell the number of rows and columns you want in it, and hurrah! Here you go:

  fig, axes = plt.subplots(nrows = , ncols = )

* nrows = 1 and ncols = 1 are default values.

* To add multiple axes like axes1 and axes2, use the row and column number. For example, for 2nd row and 3 column it would be: axes[1][2] as indexing start from 0. 

* You can also add figsize and dpi parameters to subplots also.
"""

fig, axes = plt.subplots(nrows = 2, ncols = 2, figsize = (4,4), dpi = 150)

axes[0][0].plot(x,y)
axes[0][1].plot(x,y)
axes[1][0].plot(x,y)
axes[1][1].plot(x,y)


# to add one big title on top of the subplots called Super title (suptitle)
fig.suptitle('This is 2x2 Subplot Figure', fontsize = 16);  # See we use fig. here as we are giving title to complete canvas.

"""**Nota Bene:** Sometimes, we use too many subplots then their x and y axis can overlap. So use this to avoid it: **plt.tight_layout()** Just add it as last line after adding all axes to the subplots.

(These numbers on axis are called tickers. Just for information!)

BUT !

Sometimes, the subplots don't get adjusted properly even after using tight_layout(). Then, we do it manually using **fig.subplots_adjust()** function.

It uses these parameters to get adjusted:

1. **Left:** Adjusts the left margin of the subplot area.
2. **Right:** Adjusts the right margin of the subplot area.
3. **Bottom:** Adjusts the bottom margin of the subplot area.
4. **Top:** Adjusts the top margin of the subplot area.
5. **Wspace:** Adjusts the horizontal spacing between subplots.
6. **Hspace:** Adjusts the vertical spacing between subplots.

Give these all between 0 and 1 (where 1 shows 100%).

## **Adding Legends:**

Legends in figures in Matplotlib are like a guide that helps you understand what different parts of a plot represent.

To add it:

1. Add the parameter of **'label = '** in each axes.
2. Add **'axes.legend()'** at the end after adding all axes.
"""

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])

axes.plot(x,x, label = 'x vs x')
axes.plot(x,x**2, label = 'x vs x**2')
axes.plot(x,x**3, label = 'x vs x**3');

axes.legend();

"""We can adjust the position of legend on our canvas by using the loc parameter in it. We can adjust it using following ways:

loc = (0.5, 0.5): which means on half width and half length of the canvas.

loc = (1.1, 0.5) which means out of that 100% width of canvas (as 1 means 100 and 1.1 means 110% which is out of canvas) and half of the length of the canvas.

loc = (-0.5, 0.5) which means out of that 100% width of canvas (as 1 means 100 and 1.1 means -0.5 means out of canvas on left side) and half of the length of the canvas.

etc. 

Let's try both.
"""

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])

axes.plot(x,x, label = 'x vs x')
axes.plot(x,x**2, label = 'x vs x**2')
axes.plot(x,x**3, label = 'x vs x**3');

axes.legend(loc = (0.5, 0.5));

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])

axes.plot(x,x, label = 'x vs x')
axes.plot(x,x**2, label = 'x vs x**2')
axes.plot(x,x**3, label = 'x vs x**3');

axes.legend(loc = (1.1, 0.5));

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])

axes.plot(x,x, label = 'x vs x')
axes.plot(x,x**2, label = 'x vs x**2')
axes.plot(x,x**3, label = 'x vs x**3');

axes.legend(loc = (-0.5, 0.5));

"""We can also use english phrases like 'lower left', 'upper right' etc to adjust it."""

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])

axes.plot(x,x, label = 'x vs x')
axes.plot(x,x**2, label = 'x vs x**2')
axes.plot(x,x**3, label = 'x vs x**3');

axes.legend(loc = 'upper right');

"""## **Colors and Style:**

1. To change the color of plotted line, we use the color parameter in the plot command.
"""

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])

axes.plot(x,x, color = 'red');

"""We can also add hex color values instead of english names of colors."""

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])

axes.plot(x,x, color = '#A020F0'); # Hex color value of purple color

"""2. To set the line width, use **lw** parameter or **linewidth**. Both are Okay."""

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])

axes.plot(x,x, color = '#A020F0', lw = 10); # Hex color value of purple color

"""3. To add line style, use **ls** or **linestyle** parameter.

Some common line styles:

1. **'-'**  or **'solid'**
2. **'--'**  or **'dashed'**
3. **'-.'**  or **'dashdot'**
4. ':'
5. 'None'
6. ' '
7. 'dotted'
"""

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])

axes.plot(x,x, color = '#A020F0', ls = 'dotted'); # Hex color value of purple color

"""4. Markers in figures in Matplotlib are like little symbols or shapes that show where each data point is plotted on a graph.

* To add markets, use the parameter of **marker**. Types of markers are:
'^', 'v', '1', '3', 's', 'p', '<', '>', '2', '4', 'P', '.' etc.
* To set its size use **markersize** or **ms**
* To set its color use **markerfacecolor** 
* To set its color of edges use **markeredgecolor**
* To set its size of edge use **markeredgewidth** 

"""

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])

axes.plot(x,x, marker= '<', markersize= 20, markerfacecolor = 'pink', markeredgecolor = 'red', markeredgewidth=2); # Hex color value of purple color