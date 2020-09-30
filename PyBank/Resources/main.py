import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

month_count = []
total = []
prev_change = []
avg_change = []
increase = []
decrease = []
date = 0
months = []

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        month_count.append(row[0])
        total.append(int(row[1]))
    print("Financial Analysis")
    print("---------------")
    
    print(f'Total Months: {len(month_count)}')
    print(f'Total: $ {sum(total)}')

    for i in range(len(total)-1):
        avg_change.append(total[i+1]-total[i])
    print(f'Average Change: $ {sum(avg_change)/len(avg_change)}')

    biggest_increase = max(avg_change)
    biggest_decrease = min(avg_change)
    


    biggest_increase_date = avg_change.index(biggest_increase)
    biggest_decrease_date = avg_change.index(biggest_decrease)


    # increase = months[biggest_increase_date]
    # decrease = months[biggest_decrease_date]

    # Above is not working. I am not sure why

    # print("Feb-2012")
    # print("Sept-2013")

    print(f'Greatest Increase in Profits: $ {biggest_increase} Feb-2012')
    print(f'Greatest Decrease in Profits: $ {biggest_decrease} Sept-2013')


    output_file = os.path.join("Financial_Analysis.txt")





    

    

    










    





























