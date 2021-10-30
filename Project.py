import pandas as pd
import statistics
import math

data=[60,61,65,63,98,99,90,95,91,96]


average = statistics.mean(data)
print(average)

deviations = []
for d in data:
    marks = d - average
    deviations.append(marks)


squared_deviations = []
for s in deviations:
    square = s * s
    squared_deviations.append(square)
    

sum_deviations = 0
for add in squared_deviations:
    sum_deviations = add + sum_deviations
    
variants = sum_deviations/(len(data))
std = math.sqrt(variants)

print(std)
