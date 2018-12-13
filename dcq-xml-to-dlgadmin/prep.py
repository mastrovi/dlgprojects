#!/usr/bin/env python
import re
from lxml import etree

# --- Ask for file, take file name with or without extension. If no extension, add it ---
xmlFile = input('What xml file would you like to convert? (Enter full file path)')
if ".xml" not in xmlFile:
    xmlFile = xmlFile  + '.xml'

# --- Read in the file ---
with open(xmlFile, 'r') as file:
    filedata = file.read()

# --- check to see if it has a repox prefix ---
repox = filedata.find('repox:')

# --- if Repox file ---
if repox > 0:
    # Replace repox prefixes and situate namespaces ---
    filedata = filedata.replace('repox:', '')
    print ('Removing Repox prefix...')
else:
    print ('Not a repox file.')

# --- Put in necessary namespaces ---
filedata = filedata.replace('<oai_dc:dc', '<oai_dc:dc xmlns:dlg=\"http://dlg.org/local/elements/1.1/\" xmlns:dcterms=\"http://purl.org/dc/terms/\"')
filedata = filedata.replace('<oai_qdc:qualifieddc', '<oai_qdc:qualifieddc xmlns:dlg=\"http://dlg.org/local/elements/1.1/\" ')
print ('Situating Namespaces...')

# --- Get rid of deleted items ---
filedata = re.sub(r'<.*deleted.*>\n.*<metadata/>\n.*</record>', "", filedata)
print ('Getting rid of deleted records...')
print ('Changing:')

# --- Change any  dc:identifier tags containing http to dcterms:isShownAt ---
filedata = re.sub(r'<dc:identifier>(http.*)</dc:identifier>', r"<dcterms:isShownAt>\1</dcterms:isShownAt>", filedata)
print ('dc:identifier to dcterms:isShownAt')

# --- Change any dc:identifier tags ending with .jpg (thumbnail links) ---
if re.search(r'<dcterms:isShownAt>http.*\.jpg</dcterms:isShownAt>', filedata) is not None:
    filedata = re.sub(r'<dcterms:isShownAt>http.*\.jpg</dcterms:isShownAt>', "", filedata)
    print ('Removing dcterms:isShownAt ending with .jpg')
    
# --- Create new xml file ---
# --- Split filename from extension
filename = xmlFile
(prefix, sep, suffix) = filename.rpartition('.')

# --- Add _prep to filename ---
new_filename = prefix + '_prep.xml'

# --- Write new file --
with open(new_filename, 'w') as prepFile:
  prepFile.write(filedata)

file.close()
prepFile.close()

print('\n', 'Your new file,', new_filename, ', has been created.')
