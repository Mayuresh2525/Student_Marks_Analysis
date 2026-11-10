import numpy as np

def cal_avg(std_marks):
    average=np.sum(std_marks)/len(std_marks)
    return average

def med(std_marks):
    med_mks=np.median(std_marks)
    return med_mks

def maximum(std_marks):
    max_mks=np.max(std_marks)
    return max_mks

def minimum(std_marks):
    min_mks=np.min(std_marks)
    return min_mks

def passed_std(students):
    count=0
    passed=[]
    for std in students:
        if std["marks"]>=40:
            passed.append(std)
    if passed==None:
        print("No one passed")

    return passed  