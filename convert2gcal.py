#Converts misformatted csv file to Google Calendar-compatible format
#Nathan Villotti, 2023

#Run from same directory in which opportunities.csv is located
#Outputs new file opportunities_gcal.csv

import csv

with open('opportunities.csv') as in_file, open('opportunities_gcal.csv', 'w') as out_file:
	in_file.readline() #Skip first row
	reader = csv.DictReader(in_file)
	writer = csv.DictWriter(out_file, ['Start Date', 'Start Time', 'Subject', 'Location', 'Description'])

	writer.writeheader()

	for in_row in reader:
		#Start building new row and copy "Subject"
		out_row = {'Subject': in_row['Subject']}

		#Split "Start Date" at white space
		out_row['Start Date'] = in_row['Start Date'].split()[0]
		out_row['Start Time'] = in_row['Start Date'].split()[1]

		#Rename "Delivery Address Name" to "Location"
		out_row['Location'] = in_row['Delivery Address Name']

		#Put everything else in "Description"
		description = ''
		for key in ['Store', 'Prep Start Date', 'Created By']:
			if in_row[key]: #Ignore empty fields
				description += '[' + key + ": "+ in_row[key] + '] '
		out_row['Description'] = description
		
		#Write modified row to output file
		writer.writerow(out_row)