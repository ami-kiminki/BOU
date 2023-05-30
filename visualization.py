import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

"""
BOU_case1.xlsx
"""

fig = plt.figure(figsize=(14,14))

def split_list(lst):
    start = []
    end = []
    current_start = lst[0]

    for i in range(1, len(lst)):
        if lst[i] - lst[i-1] > 1:  # 다음 값과의 차이가 1보다 크면 end로 저장
            start.append(current_start)
            end.append(lst[i-1])
            current_start = lst[i]
    
    # 마지막 값은 항상 end로 저장되어야 함
    start.append(current_start)
    end.append(lst[-1])
    
    return start, end

def debug_func(info):
    print("***"*50)
    print(info)
    print("***"*50)
    
BOU1_path = './BOU_case1.xlsx'

def each_dataset_pressure_visaulization(datapath):
    abnormal_index = []
    normal_index = []
    abnormal_columns = []
    normal_columns = []
    if(os.path.isfile(datapath) == True):
        BOU_DATA = pd.read_excel(datapath, sheet_name=[0,1,2,3])
        
        for i in range(len(BOU_DATA)):
            if('InsertedPostion' in BOU_DATA[i].columns.to_list()):
                abnormal_index.append(i)
            else:
                normal_index.append(i)
        abnormal_columns = BOU_DATA[abnormal_index[0]].columns.to_list()
        normal_columns = BOU_DATA[normal_index[0]].columns.to_list()
        
        for i in range(len(normal_index)):
            plt.plot(BOU_DATA[normal_index[i]]['No'], BOU_DATA[normal_index[i]]['BCPressure(kg/cm)'], label="BC", color='r')
            plt.plot(BOU_DATA[normal_index[i]]['No'], BOU_DATA[normal_index[i]]['ACPressure(kg/cm)'], label="AC", color='g')
            plt.legend()
            plt.xlabel('Index')
            plt.ylabel('Pressure')
            plt.savefig('normal_index'+str(i)+'.png')            
            plt.clf()
            
        for i in range(len(abnormal_index)):
            plt.plot(BOU_DATA[abnormal_index[i]]['No'], BOU_DATA[abnormal_index[i]]['BCPressure(kg/cm)'], label="BC", color='r')
            plt.plot(BOU_DATA[abnormal_index[i]]['No'], BOU_DATA[abnormal_index[i]]['ACPressure(kg/cm)'], label="AC", color='g')
            plt.legend()
            plt.xlabel('Index')
            plt.ylabel('Pressure')
            
            index = BOU_DATA[abnormal_index[i]].index[(BOU_DATA[abnormal_index[i]][abnormal_columns[-1]] == 1)]
            index = index.to_list()
            
            start, end = split_list(index)
            
            for j in range(len(start)):
                plt.axvspan(start[j], end[j], facecolor = 'gray')
            plt.savefig('abnormal_index'+str(i)+'.png')
            plt.clf()
        
each_dataset_pressure_visaulization(BOU1_path)