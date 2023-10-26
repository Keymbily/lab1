import csv
from statistics import mean

with open("DATA475_lab_rectangles_data (1).csv") as f:
    reader = csv.reader(f)
    next(f)
    areas = []
    for row in reader:
        areas.append(float(row[1]) * float(row[2]))

summary = {
    "Max": max(areas),
    "Min": min(areas),
    "Ave": mean(areas),
    "Sum": sum(areas),
    "Count": len(areas),
}
for key,value in summary.items():
    print(f"{key} is {value}")

with open('summary.csv', mode="w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(summary.keys())
    writer.writerow(summary.values()) 


    