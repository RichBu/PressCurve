# PressCurve
Reads in csv file from Pico Scope and plots a pressure curve

Program by Rich Budek  02/16/2021

Technologies used:
Python, Pandas, MatPlotLib

Description:
This program takes the ouput from a digital USB scope and plots the results on a chart.  
The scope outputs its values in a CSV file. But, with over 655,000 values, Excel just bogs down.
This program was put together to read in the values, and the number of values is absolutely
no problem for Python to handle.

Challenges:
Main program to open a CSV file and to plot it was not very challenging.  Challenge was
the second axis.  All the examples showed was if you had the same number of data points
then you could just plot one chart on top of another.  In my case, I did not have ANY 
values.  I just wanted to plot what the calculated air pressure was WITHOUT going thru
and plotting all of the values.

Using some of those ideas, the plot was getting close except for the X axis tick marks.
I wanted mine formatted to 3 decimal points and then at 90 degrees.

So, I finally figured out the solution.  That was to use the twinax() function.  This
function "twins" or duplicates everthing from an axis except the  Y or Data values. 
Worked PERRFECT.  I don't even put in any data values.

The result is both axis have the same X values, X tick marks, and number of data points.
Except the second copy has no Y values.  This axis is then told to plot against a 
Secondary Y axis.

Results can be seen in the plot_01.svg file.

