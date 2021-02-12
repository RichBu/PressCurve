"""
This program uses Digital Oscilliscope data read in from a PicScope.
The PicoScope outputs the data as a CSV and this Python app reads it in.
Then, we plot on an X-Y chart

By Rich Budek 02/12/2021 in Python 3.8
"""

import pandas as pd
import numpy as np
import jinja2
import math
import re
from pandas import DataFrame

# program to read in CSV file from PicoScope and create a graph
# excel was dragged to a halt because the data set is so large


class Config_Data:
    #set up by user once
    filepath = "Z:\Shared Folders\Data\WCO\Customer\BHPB\BHPB_Pressure\Graph-Python\PressCurve"
    filename_readings = "Test_01_02b_csv.csv"


class Project_Data:
    #data that gets transferred between functions
    full_filename_readings = ""
    file_orders_is_csv = False


def ReadAllReadings(_project_data):
    #read all of the current orders
    orders = pd.read_excel(_project_data.full_filename_readings)
    return orders


#main function or run
def main():
    #this is the "main" program

    #print welcome
    print(" ")
    print("Sample Program")
    print("by Rich Budek")
    print(" ")

    #setup needed variables
    config_data = Config_Data()
    project_data = Project_Data()

    #create all the full file path names here, so only have to do it once
    project_data.full_filename_readings = config_data.filepath + "\\" + config_data.filename_readings
    if project_data.full_filename_readings[-3:].lower() == 'csv':
        project_data.file_readings_is_csv = True
    else:
        project_data.file_readings_is_csv = False



    #these are all the data tables
    readings = []

    #read in the readings
    #this can be a database, but for this example write to xls file so can see the output
    #if write to cloud database, anyone can read it
    if project_data.file_readings_is_csv:
        #FUTURE read in csv file
        readings = pd.read_csv(project_data.full_filename_readings,index_col=0, skiprows=3)
        pass
    else:
        readings = pd.read_excel(project_data.full_filename_readings)
    readings_len = len(readings.index)
    print ("number of readings = {:d}".format( readings_len ) )

    #plot the readings
    
    #plot #01  all the hole diameters
    df_readings = readings
    df_readings_len = len(df_readings.index)
    print ("number of df readings = {:d}".format( df_readings_len ) )


    ax01=df_readings.plot(kind='line',  figsize=(11,8))
    ax01.set_ylim(-0.5, 3.0)
    ax01.set(xlabel='Time (in secs) ', ylabel='Air Pressure (in Volts)')
    xticks_num = np.arange(-1.1, 4.1, step=0.1)
    #xticks_label = map(str, xticks_num)
    xticks_label = ['{:1.3f}'.format(x) for x in xticks_num]


    ax01.set_xticks(xticks_num)
    ax01.set_xticklabels(xticks_label, rotation=90)

    #set up secondary dummy data frame
    df_sec_axis = pd.DataFrame(range(0,readings_len))

    df_sec_axis = pd.DataFrame({'two': range(100, 110)})
    ax02 = df_sec_axis.plot( title='Mini Bone Air Pressure', legend='False', figsize=(11,8), secondary_y=True, ax=ax01)
    ax02.set_ylim(-23.8, 143)
    ax02.set(ylabel='Approx. Air Pressure (in PSI)')

    ax02.set_xticks(xticks_num)
    ax02.set_xticklabels(xticks_label, rotation=90)
    fig01=ax02.get_figure()
    fig01.savefig('plot_01.svg')



    ax02=df_sec_axis.plot(kind='line', title='Mini Bone Air Pressure', legend='False', figsize=(11,8), secondary_y=True)
    #ax02 = df_sec_axis.plot(secondary_y=True)
    ax02.set_ylim(0, 143)

    #fig = ax.get_figure()
    #fig.savefig('test.png')

    df = pd.DataFrame({'one': range(10), 'two': range(100, 110)})
    #ax2 = df['two'].plot(secondary_y=True)
    #ax2.set_ylim(-20, 50)
    ax2 = df_readings.plot(secondary_y=True)
    ax2.set_ylim(-20, 50)

    fig01=ax01.get_figure()
    fig01.savefig('plot_02.svg')




print (" ")
print (".Program start.")

if __name__ == "__main__":
     main()
     print (".Program end.")
