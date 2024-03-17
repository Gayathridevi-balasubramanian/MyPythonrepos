import csv
import json
import xml

def merge_csv(csv_list, output_path):
    fieldnames = []
    for file in csv_list:
        with open(file,'r',encoding='utf-8') as input_csv:
            field = csv.DictReader(input_csv).fieldnames
            fieldnames.extend(f for f in field if f not in fieldnames)

    # to write data to output file based on fieldnames
    with open(output_path,'w',encoding='utf-8',newline='') as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()
        # Iterate over each CSV file and write rows to the output csv
        for file in csv_list:
            with open(file,'r',encoding='utf-8') as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)

merge_csv(['class1.csv','class2.csv'],'class3.csv')
