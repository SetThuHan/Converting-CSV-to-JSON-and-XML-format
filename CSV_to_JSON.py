import csv, json, glob, os

Path = input("Type Specific Path: ")

for filename in glob.glob(Path+'/*.csv'):
	print ('Scanned CSV: ', filename)
	csvfile = os.path.splitext(filename)[0]
	jsonfile = csvfile + '.json'
	data = {}
	with open(csvfile+'.csv') as f:
		reader= csv.DictReader(f,fieldnames=['x','y','width','height','tag'])
		for csvRow in reader:
			tag = csvRow["tag"]
			data[tag] = csvRow
			
	with open(jsonfile, 'w') as f:
		json.dump(data, f, indent=4)
		print ('Converted to JSON')

