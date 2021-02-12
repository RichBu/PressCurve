"""
routine pasted from main program ... keep here for reference
"""






    #test plot #2

    #xticks_num = np.arange(-1.1, 4.1, step=0.1)
    #xticks_label = map(str, xticks_num)

    #ax = df['one'].plot()
    ax=df_readings.plot(kind='line', title='Mini Bone Air Pressure', legend='False', figsize=(11,8))
    ax.set_ylim(-0.5, 3.0)

    ax.set(xlabel='Time (in secs) ', ylabel='Air Pressure (in Volts)')
    xticks_label = ['{:1.3f}'.format(x) for x in xticks_num]
    ax.set_xticks(xticks_num)
    ax.set_xticklabels(xticks_label, rotation=90)


    #ax2 = df['two'].plot(secondary_y=True)
    readings_list = df_readings.values.tolist()
    readings_index = df_readings.index.tolist()
    df_read_2 = DataFrame(readings_list, index=readings_index)

    #df_read_2 = df_readings.copy(deep=True)
    #maybe do not plot the second time around
    #ax = df.plot('Date','A')
    #df.plot('Date','B',secondary_y=True, ax=ax)


    ax2 = df_read_2.plot(kind='line', title='Mini Bone Air Pressure', legend='False', figsize=(11,8), secondary_y=True)
    ax2.set_ylim(0, 145)
    ax2.set_xticks(xticks_num)
    ax2.set_xticklabels(xticks_label, rotation=90)

    ax2.set(xlabel='Time (in secs) ', ylabel='Air Pressure (in Volts)')
    xticks_label = ['{:1.3f}'.format(x) for x in xticks_num]


    ax2.set_xticks(xticks_num)
    ax2.set_xticklabels(xticks_label, rotation=90)
    
    
    fig = ax.get_figure()
    fig.savefig('test.svg')
    fig = ax2.get_figure()
    fig.savefig('test2.svg')


