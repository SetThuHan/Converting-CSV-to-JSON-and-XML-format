import csv, glob, os

Path = input("Type Specific Path: ")

for filename in glob.glob(Path+'/*.csv'):
	print ('Scanned CSV: ', filename)
	csvfile = os.path.splitext(filename)[0]
	xmlfile = csvfile + '.xml'
	reader = csv.reader(open(filename, 'r'), delimiter = ',')
	f = open (xmlfile, 'w')
	f.write('<annotation>'+'\n')

	for row in reader:
		f.write('   '+'<object>'+'\n')
		f.write('     '+'<tag>'+ row[-1] + '</tag>'+ '\n')
		f.write('     '+'<bndbox>'+ '\n')
		f.write('         '+ '<x>'+ row[0]+ '</x>' + '\n')
		f.write('         '+'<y>'+ row[1]+ '</y'+ '\n')
		f.write('         '+'<width>'+ row[2]+ '</width>'+ '\n')
		f.write('         '+'<height>'+ row[3]+ '</height>'+ '\n')
		f.write('     '+'</bndbox>'+ '\n')
		f.write('   '+'</object>'+ '\n')
	f.write('</annotation>'+ '\n')	
	f.close()
	print("Converted to XML")
