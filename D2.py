import csv
# Read the data from the CSV file
csv_file1 = "Loki Bowser21147175.csv"
csv_file2 = "Becca Van Lent24262808.csv"
# Open the CSV file and extract the data
with open(csv_file1, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)


with open(csv_file2, newline='', encoding='utf-8') as file:
    reader = csv.read(file)
    data2 = list(reader)


athletes = data[1:]

# Add each athlete's information to the list
for athlete in athletes:

    
output_file = f"{row['name'].replace(' ', '_').lower()}.html"
with open(output_file, 'w') as file:
    file.write(html_content)
