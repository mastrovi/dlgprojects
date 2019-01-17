#!/usr/bin/env python
import re
from lxml import etree

# --- Ask for file, take file name with or without extension. If no extension, add it ---
xmlFile = input('What xml file would you like to convert? (Enter full file path)')
if ".xml" not in xmlFile:
    xmlFile = xmlFile  + '.xml'

# --- Read in the file ---
with open(xmlFile, 'r', encoding="utf-8") as file:
    filedata = file.read()



'''Start file processing here: includes removing repox prefix, namespace management, common tag changes,
and splitting multivalued fields'''
# --- check to see if it has a repox prefix ---
if filedata.find('repox:') is not None:
    # Replace repox prefixes ---
    filedata = filedata.replace('repox:', '')
    print ('Removing Repox prefix')
else:
    print ('Not a repox file.')

# --- Put in necessary namespaces ---
filedata = filedata.replace('<oai_dc:dc', '<oai_dc:dc xmlns:dlg=\"http://dlg.org/local/elements/1.1/\" xmlns:dcterms=\"http://purl.org/dc/terms/\"')
filedata = filedata.replace('<oai_qdc:qualifieddc', '<oai_qdc:qualifieddc xmlns:dlg=\"http://dlg.org/local/elements/1.1/\" ')
print ('Situating Namespaces')

# --- Get rid of deleted items ---
filedata = re.sub(r'<.*deleted.*>\n.*<metadata/>\n.*</record>', "", filedata)
print ('Getting rid of deleted records')

# --- Change any dc:identifier tags containing http to dcterms:isShownAt ---
if re.search(r'<dc:identifier>(http.*?)</dc:identifier>', filedata) is not None:
	filedata = re.sub(r'<dc:identifier>(http.*?)</dc:identifier>', r"<dcterms:isShownAt>\1</dcterms:isShownAt>", filedata)
	print ('Changing dc:identifier to dcterms:isShownAt')

# --- Remove any dc:identifier tags ending with .jpg (thumbnail links) ---
if re.search(r'<dcterms:isShownAt>http.*\.jpg</dcterms:isShownAt>', filedata) is not None:
    filedata = re.sub(r'<dcterms:isShownAt>http.*\.jpg</dcterms:isShownAt>', "", filedata)
    print ('Removing dcterms:isShownAt ending with .jpg')
	
# --- Change any record tags with additional data to <record> ---
if re.search(r'<record id=(.*?)>', filedata) is not None:
    filedata = re.sub(r'<record id=(.*?)>', r"<record>", filedata)
    print ('Changing <record> tags with extra data to <record>')	
	
# --- DATE FIXES IN THIS SECTION ---

    # --- Change any dc:date.created tags with additional data in timestamp to dc:date and converting to YYYY-MM-DD ---
if re.search(r'<dc:date.created>(\d{4})-(\d{2})-(\d{2})(.*?)</dc:date.created>', filedata) is not None:
    filedata = re.sub(r'<dc:date.created>(\d{4})-(\d{2})-(\d{2})(.*?)</dc:date.created>', r"<dc:date>\1-\2-\3</dc:date>", filedata)
    print ('Changing dc:date.created to dc:date and removing extra data in timestamp')
	
	# --- Change any dc:date tags with additional data in timestamp to YYYY-MM-DD ---
if re.search(r'<dc:date>(\d{4})-(\d{2})-(\d{2})(.*?)</dc:date>', filedata) is not None:
    filedata = re.sub(r'<dc:date>(\d{4})-(\d{2})-(\d{2})(.*?)</dc:date>', r"<dc:date>\1-\2-\3</dc:date>", filedata)
    print ('Removing extra data in timestamp to <dc:date> so that it reads YYYY-MM-DD')
	
# --- Change any dc:date tags with dates written out YYYY Month D to YYYY-MM-DD ---

if re.search(r'<dc:date>(\d{4}) December (\d{1})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) December (\d{1})</dc:date>', r"<dc:date>\1-12-0\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) D to YYYY-MM-DD')

if re.search(r'<dc:date>(\d{4}) November (\d{1})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) November (\d{1})</dc:date>', r"<dc:date>\1-11-0\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) D to YYYY-MM-DD')

if re.search(r'<dc:date>(\d{4}) October (\d{1})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) October (\d{1})</dc:date>', r"<dc:date>\1-10-0\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) D to YYYY-MM-DD')

if re.search(r'<dc:date>(\d{4}) September (\d{1})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) September (\d{1})</dc:date>', r"<dc:date>\1-09-0\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) D to YYYY-MM-DD')

if re.search(r'<dc:date>(\d{4}) August (\d{1})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) August (\d{1})</dc:date>', r"<dc:date>\1-08-0\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) D to YYYY-MM-DD')

if re.search(r'<dc:date>(\d{4}) July (\d{1})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) July (\d{1})</dc:date>', r"<dc:date>\1-07-0\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) D to YYYY-MM-DD')

if re.search(r'<dc:date>(\d{4}) June (\d{1})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) June (\d{1})</dc:date>', r"<dc:date>\1-06-0\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) D to YYYY-MM-DD')

if re.search(r'<dc:date>(\d{4}) May (\d{1})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) May (\d{1})</dc:date>', r"<dc:date>\1-05-0\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) D to YYYY-MM-DD')

if re.search(r'<dc:date>(\d{4}) April (\d{1})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) April (\d{1})</dc:date>', r"<dc:date>\1-04-0\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) D to YYYY-MM-DD')

if re.search(r'<dc:date>(\d{4}) March (\d{1})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) March (\d{1})</dc:date>', r"<dc:date>\1-03-0\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) D to YYYY-MM-DD')

if re.search(r'<dc:date>(\d{4}) February (\d{1})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) February (\d{1})</dc:date>', r"<dc:date>\1-02-0\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) D to YYYY-MM-DD')

if re.search(r'<dc:date>(\d{4}) January (\d{1})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) January (\d{1})</dc:date>', r"<dc:date>\1-01-0\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) D to YYYY-MM-DD')	
	
# --- Change any dc:date tags with dates written out YYYY Month DD to YYYY-MM-DD ---

if re.search(r'<dc:date>(\d{4}) December (\d{2})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) December (\d{2})</dc:date>', r"<dc:date>\1-12-\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) DD to YYYY-MM-DD')

if re.search(r'<dc:date>(\d{4}) November (\d{2})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) November (\d{2})</dc:date>', r"<dc:date>\1-11-\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) DD to YYYY-MM-DD')

if re.search(r'<dc:date>(\d{4}) October (\d{2})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) October (\d{2})</dc:date>', r"<dc:date>\1-10-\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) DD to YYYY-MM-DD')

if re.search(r'<dc:date>(\d{4}) September (\d{2})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) September (\d{2})</dc:date>', r"<dc:date>\1-09-\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) DD to YYYY-MM-DD')

if re.search(r'<dc:date>(\d{4}) August (\d{2})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) August (\d{2})</dc:date>', r"<dc:date>\1-08-\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) DD to YYYY-MM-DD')

if re.search(r'<dc:date>(\d{4}) July (\d{2})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) July (\d{2})</dc:date>', r"<dc:date>\1-07-\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) DD to YYYY-MM-DD')

if re.search(r'<dc:date>(\d{4}) June (\d{2})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) June (\d{2})</dc:date>', r"<dc:date>\1-06-\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) DD to YYYY-MM-DD')

if re.search(r'<dc:date>(\d{4}) May (\d{2})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) May (\d{2})</dc:date>', r"<dc:date>\1-05-\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) DD to YYYY-MM-DD')

if re.search(r'<dc:date>(\d{4}) April (\d{2})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) April (\d{2})</dc:date>', r"<dc:date>\1-04-\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) DD to YYYY-MM-DD')

if re.search(r'<dc:date>(\d{4}) March (\d{2})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) March (\d{2})</dc:date>', r"<dc:date>\1-03-\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) DD to YYYY-MM-DD')

if re.search(r'<dc:date>(\d{4}) February (\d{2})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) February (\d{2})</dc:date>', r"<dc:date>\1-02-\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) DD to YYYY-MM-DD')

if re.search(r'<dc:date>(\d{4}) January (\d{2})</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) January (\d{2})</dc:date>', r"<dc:date>\1-01-\2</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) DD to YYYY-MM-DD')

# --- Change any dc:date tags with dates written out YYYY Month to YYYY-MM---

if re.search(r'<dc:date>(\d{4}) December</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) December</dc:date>', r"<dc:date>\1-12</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) to YYYY-MM')

if re.search(r'<dc:date>(\d{4}) November</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) November</dc:date>', r"<dc:date>\1-11</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) to YYYY-MM')

if re.search(r'<dc:date>(\d{4}) October</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) October</dc:date>', r"<dc:date>\1-10</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) to YYYY-MM')

if re.search(r'<dc:date>(\d{4}) September</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) September</dc:date>', r"<dc:date>\1-09</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) to YYYY-MM')

if re.search(r'<dc:date>(\d{4}) August</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) August</dc:date>', r"<dc:date>\1-08</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) to YYYY-MM')

if re.search(r'<dc:date>(\d{4}) July</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) July</dc:date>', r"<dc:date>\1-07</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) to YYYY-MM')

if re.search(r'<dc:date>(\d{4}) June</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) June</dc:date>', r"<dc:date>\1-06</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) to YYYY-MM')

if re.search(r'<dc:date>(\d{4}) May</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) May</dc:date>', r"<dc:date>\1-05</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) to YYYY-MM')

if re.search(r'<dc:date>(\d{4}) April</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) April</dc:date>', r"<dc:date>\1-04</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) to YYYY-MM')

if re.search(r'<dc:date>(\d{4}) March</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) March</dc:date>', r"<dc:date>\1-03</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) to YYYY-MM')

if re.search(r'<dc:date>(\d{4}) February</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) February</dc:date>', r"<dc:date>\1-02</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) to YYYY-MM')

if re.search(r'<dc:date>(\d{4}) January</dc:date>', filedata) is not None:
	filedata = re.sub(r'<dc:date>(\d{4}) January</dc:date>', r"<dc:date>\1-01</dc:date>", filedata)
	print ('Changing dc:date dates labeled YYYY (month) to YYYY-MM')	

# --- Look for semicolons at the end of string (CONTENTdm specfic)
#if filedata.find(';<') is not None:
#    filedata = filedata.replace(';<', '<')
#    print('Removing trailing semicolons')

# --- Replace &amp; with &amp to make splitting tags easier ---
if filedata.find('&amp;') is not None:
    filedata = filedata.replace('&amp;', '&amp')

# --- Split multivalued fields into individual fields ---
# --- Look for semicolons at the end of string (CONTENTdm specfic)
# --- Expressions for each field to separate ---
separateFields = [
    'dc:subject',
    'dc:type',
    'dc:format',
    'dc:creator',
    'dc:contributor',
    'dcterms:spatial'
    ]

for field in separateFields:
    print('Separating ' + field)
    if re.search(r'<' + field + '>(.*?);</' + field + '>', filedata) is not None:
        filedata = re.sub(r'<(' + field + ')>(.*?);</' + field + '>', r'<\1>\2</\1>', filedata)
    if re.search(r'<' + field + '>(.*?); (.*?)</' + field + '>', filedata) is not None:
        filedata = re.sub(r'<(' + field + ')>(.*?); (.*?)</' + field + '>', r'<\1>\2</\1>\n<\1>\3</\1>', filedata)
    if re.search(r'<' + field + '>(.*?);(.*?)</' + field + '>', filedata) is not None:
        filedata = re.sub(r'<(' + field + ')>(.*?);(.*?)</' + field + '>', r'<\1>\2</\1>\n<\1>\3</\1>', filedata) 

# --- Add &amp; reference back for valid XML ---
if filedata.find('&amp') is not None:
    filedata = filedata.replace('&amp', '&#38;')

#



'''Output new file with all changes'''
# --- Create new xml file ---
# --- Split filename from extension
filename = xmlFile
(prefix, sep, suffix) = filename.rpartition('.')

# --- Add _prep to filename ---
new_filename = prefix + '_prep.xml'

# --- Write new file --
with open(new_filename, 'w', encoding="utf-8") as prepFile:
  prepFile.write(filedata)

file.close()
prepFile.close()

print('\n', 'Your new file,', new_filename, ', has been created.')

input("Press Enter to close...")
