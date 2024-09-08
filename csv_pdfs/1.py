


# pandas
# openpyxl
# google sheets python api 

import csv

# open the file

data = open('csv_pdfs/example.csv',encoding='utf-8')

# call csv reader
csv_data = csv.reader(data)

# list of list reformating

data_lines = list(csv_data)

print(data_lines[0])
print(data_lines[1])
print(len(data_lines))

for line in data_lines[:5]:
    # print(line)

    pass

print(data_lines[10][3])

all_emails = []

for line in data_lines:
    all_emails.append(line[3])

print(all_emails)


full_name = []

for line in data_lines:

    full_name.append( line[1] + " "+line[2]  )

print(full_name)


#### how to write to csv files

file_to_output = open('csv_pdfs/to_save_file.csv',mode='w',newline='')

csv_writer = csv.writer(file_to_output,delimiter=',')

csv_writer.writerow(['a','b','c'])

csv_writer.writerows([['a','ad','adsf'],['234','4','45']])


file_to_output.close()


#### appending to a file 

f = open('csv_pdfs/to_save_file.csv',mode='a',newline='')

csv_writer = csv.writer(f)

csv_writer.writerow(['345345','34534523423423'])

f.close()