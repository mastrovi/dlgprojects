#!/usr/bin/env python

import re
import sys
from lxml import etree

# --- Ask for file, take file name with or without extension. If no extension, add it ---
xmlFile = input('What xml file would you like to convert? (Enter full file path)')
if ".xml" not in xmlFile:
    xmlFile = xmlFile  + '.xml'

# --- Read in the file ---
with open(xmlFile, 'r', encoding="utf-8") as file:
    filedata = file.read()

# --- Remove \r\n and whitespace

filedata = filedata.replace('\r', '').replace('\n', '')

# --- Remove all tabs

filedata = filedata.replace('\t', '')


# --- Remove leading spaces

filedata = filedata.replace('    ', '')


# --- Remove second group of leading spaces

filedata = filedata.replace('  ', '')

# --- Remove spaces between > and <

filedata = filedata.replace('> <', '><')


# --- Remove <items type="array">

filedata = filedata.replace('<items type="array">', '<items>')


# --- Replace <id type="integer"> with <id>

s = '<id type="integer">'

filedata = filedata.replace('<id type="integer">', '<id>')


# --- Replace <dpla type="boolean"> with <dpla>

s = '<dpla type="boolean">'

filedata = filedata.replace('<dpla type="boolean">', '<dpla>')


# --- Replace <public type="boolean"> with <public>

s = '<public type="boolean">'

filedata = filedata.replace('<public type="boolean">', '<public>')

# --- Replace <local type="boolean"> with <local>

s = '<local type="boolean">'

filedata = filedata.replace('<local type="boolean">', '<local>')

# --- Remove <collection>

s = '<collection>'

filedata = filedata.replace('<collection>', '')


# --- Remove </collection>

s = '</collection>'

filedata = filedata.replace('</collection>', '')


# --- Replace <record_id> with <collection>

filedata = filedata.replace('<record_id>', '<collection>')


# --- Replace </record_id> with </collection>

filedata = filedata.replace('</record_id>', '</collection>')



# --- Remove <portals type="array">

filedata = filedata.replace('<portals type="array">', '')


# --- Remove <portal>

filedata = filedata.replace('<portal>', '')


# --- Remove </portal>

filedata = filedata.replace('</portal>', '')


# --- Replace <code> with <portal>


filedata = filedata.replace('<code>', '<portal>')


# --- Replace </code> with </portal>

filedata = filedata.replace('</code>', '</portal>')







# --- Remove <portals>

filedata = filedata.replace('<portals>', '')


# --- Remove </portals>

filedata = filedata.replace('</portals>', '')

# --- Replace <record_id> with <portals>

s = '<record_id>'

filedata = filedata.replace('<record_id>', '<portals>')


# --- Replace </record_id> with </portals>

filedata = filedata.replace('</record_id>', '</portals>')








# --- Remove <pages_count type="integer" nil="true"/>

s = '<pages_count type="integer" nil="true"/>'

filedata = filedata.replace('<pages_count type="integer" nil="true"/>', '')


# --- Remove <dc_format type="array">


s = '<dc_format type="array">'

filedata = filedata.replace('<dc_format type="array">', '')


# --- Remove <dc_format type="array"/>


s = '<dc_format type="array"/>'

filedata = filedata.replace('<dc_format type="array"/>', '')


# --- Replace </dc_format>\r\n<dc_format> with ; 

if filedata.find('</dc_format><dc_format>') is not None:
    filedata = filedata.replace('</dc_format><dc_format>', '; ')
print ('Separating multiple dc_format entries with semicolon and space')


# --- Replace </dc_format><dc_format> with ;

if filedata.find('</dc_format><dc_format>') is not None:
    filedata = filedata.replace('</dc_format><dc_format>', '; ')
print ('Separating multiple dc_format entries without line break to semicolon and space')


# --- Replace </dc_format>\r\n</dc_format> with </dc_format>

if filedata.find('</dc_format></dc_format>') is not None:
    filedata = filedata.replace('</dc_format></dc_format>', '</dc_format>')
print ('Collapsing dc_format again')


# --- Remove <dc_right type="array">


s = '<dc_right type="array">'

filedata = filedata.replace('<dc_right type="array">', '')


# --- Remove <dc_right type="array"/>


s = '<dc_right type="array"/>'

filedata = filedata.replace('<dc_right type="array"/>', '')

# --- Replace </dc_right>\r\n<dc_right> with ; 

if filedata.find('</dc_right><dc_right>') is not None:
    filedata = filedata.replace('</dc_right><dc_right>', '; ')
print ('Separating multiple dc_right entries with semicolon and space')


# --- Replace </dc_right><dc_right> with ;

if filedata.find('</dc_right><dc_right>') is not None:
    filedata = filedata.replace('</dc_right><dc_right>', '; ')
print ('Separating multiple dc_right entries without line break to semicolon and space')


# --- Replace </dc_right>\r\n</dc_right> with </dc_right>

if filedata.find('</dc_right></dc_right>') is not None:
    filedata = filedata.replace('</dc_right></dc_right>', '</dc_right>')
print ('Collapsing dc_right')


# --- Remove <dc_date type="array">


s = '<dc_date type="array">'

filedata = filedata.replace('<dc_date type="array">', '')


# --- Remove <dc_date type="array"/>


s = '<dc_date type="array"/>'

filedata = filedata.replace('<dc_date type="array"/>', '')


# --- Replace </dc_date>\r\n</dc_date> with </dc_date>

if filedata.find('</dc_date></dc_date>') is not None:
    filedata = filedata.replace('</dc_date></dc_date>', '</dc_date>')
print ('Collapsing dc_date')


# --- Remove <dc_relation type="array">


s = '<dc_relation type="array">'

filedata = filedata.replace('<dc_relation type="array">', '')


# --- Remove <dc_relation type="array"/>


s = '<dc_relation type="array"/>'

filedata = filedata.replace('<dc_relation type="array"/>', '')

# --- Replace </dc_relation>\r\n<dc_relation> with ; 

if filedata.find('</dc_relation><dc_relation>') is not None:
    filedata = filedata.replace('</dc_relation><dc_relation>', '; ')
print ('Separating multiple dc_relation entries with semicolon and space')


# --- Replace </dc_relation><dc_relation> with ;

if filedata.find('</dc_relation><dc_relation>') is not None:
    filedata = filedata.replace('</dc_relation><dc_relation>', '; ')
print ('Separating multiple dc_relation entries without line break to semicolon and space')


# --- Replace </dc_relation>\r\n</dc_relation> with </dc_relation>

if filedata.find('</dc_relation></dc_relation>') is not None:
    filedata = filedata.replace('</dc_relation></dc_relation>', '</dc_relation>')
print ('Collapsing dc_relation again')


# --- Remove <dcterms_is_part_of type="array">


s = '<dcterms_is_part_of type="array">'

filedata = filedata.replace('<dcterms_is_part_of type="array">', '')


# --- Remove <dcterms_is_part_of type="array"/>


s = '<dcterms_is_part_of type="array"/>'

filedata = filedata.replace('<dcterms_is_part_of type="array"/>', '')

# --- Replace </dcterms_is_part_of>\r\n<dcterms_is_part_of> with ; 

if filedata.find('</dcterms_is_part_of><dcterms_is_part_of>') is not None:
    filedata = filedata.replace('</dcterms_is_part_of><dcterms_is_part_of>', '; ')
print ('Separating multiple dcterms_is_part_of entries with semicolon and space')


# --- Replace </dcterms_is_part_of><dcterms_is_part_of> with ;

if filedata.find('</dcterms_is_part_of><dcterms_is_part_of>') is not None:
    filedata = filedata.replace('</dcterms_is_part_of><dcterms_is_part_of>', '; ')
print ('Separating multiple dcterms_is_part_of entries without line break to semicolon and space')


# --- Replace </dcterms_is_part_of>\r\n</dcterms_is_part_of> with </dcterms_is_part_of>

if filedata.find('</dcterms_is_part_of></dcterms_is_part_of>') is not None:
    filedata = filedata.replace('</dcterms_is_part_of></dcterms_is_part_of>', '</dcterms_is_part_of>')
print ('Collapsing dcterms_is_part_of')


# --- Remove <dcterms_contributor type="array">


s = '<dcterms_contributor type="array">'

filedata = filedata.replace('<dcterms_contributor type="array">', '')


# --- Remove <dcterms_contributor type="array"/>


s = '<dcterms_contributor type="array"/>'

filedata = filedata.replace('<dcterms_contributor type="array"/>', '')

# --- Replace </dcterms_contributor>\r\n<dcterms_contributor> with ; 

if filedata.find('</dcterms_contributor><dcterms_contributor>') is not None:
    filedata = filedata.replace('</dcterms_contributor><dcterms_contributor>', '; ')
print ('Separating multiple dcterms_contributor entries with semicolon and space')


# --- Replace </dcterms_contributor><dcterms_contributor> with ;

if filedata.find('</dcterms_contributor><dcterms_contributor>') is not None:
    filedata = filedata.replace('</dcterms_contributor><dcterms_contributor>', '; ')
print ('Separating multiple dcterms_contributor entries without line break to semicolon and space')


# --- Replace </dcterms_contributor>\r\n</dcterms_contributor> with </dcterms_contributor>

if filedata.find('</dcterms_contributor></dcterms_contributor>') is not None:
    filedata = filedata.replace('</dcterms_contributor></dcterms_contributor>', '</dcterms_contributor>')
print ('Collapsing dcterms_contributor')


# --- Remove <dcterms_creator type="array">


s = '<dcterms_creator type="array">'

filedata = filedata.replace('<dcterms_creator type="array">', '')


# --- Remove <dcterms_creator type="array"/>


s = '<dcterms_creator type="array"/>'

filedata = filedata.replace('<dcterms_creator type="array"/>', '')

# --- Replace </dcterms_creator>\r\n<dcterms_creator> with ; 

if filedata.find('</dcterms_creator><dcterms_creator>') is not None:
    filedata = filedata.replace('</dcterms_creator><dcterms_creator>', '; ')
print ('Separating multiple dcterms_creator entries with semicolon and space')


# --- Replace </dcterms_creator><dcterms_creator> with ;

if filedata.find('</dcterms_creator><dcterms_creator>') is not None:
    filedata = filedata.replace('</dcterms_creator><dcterms_creator>', '; ')
print ('Separating multiple dcterms_creator entries without line break to semicolon and space')


# --- Replace </dcterms_creator>\r\n</dcterms_creator> with </dcterms_creator>

if filedata.find('</dcterms_creator></dcterms_creator>') is not None:
    filedata = filedata.replace('</dcterms_creator></dcterms_creator>', '</dcterms_creator>')
print ('Collapsing dcterms_creator')


# --- Remove <dcterms_description type="array">


s = '<dcterms_description type="array">'

filedata = filedata.replace('<dcterms_description type="array">', '')


# --- Remove <dcterms_description type="array"/>


s = '<dcterms_description type="array"/>'

filedata = filedata.replace('<dcterms_description type="array"/>', '')

# --- Replace </dcterms_description>\r\n<dcterms_description> with ; 

if filedata.find('</dcterms_description><dcterms_description>') is not None:
    filedata = filedata.replace('</dcterms_description><dcterms_description>', '; ')
print ('Separating multiple dcterms_description entries with semicolon and space')


# --- Replace </dcterms_description><dcterms_description> with ;

if filedata.find('</dcterms_description><dcterms_description>') is not None:
    filedata = filedata.replace('</dcterms_description><dcterms_description>', '; ')
print ('Separating multiple dcterms_description entries without line break to semicolon and space')


# --- Replace </dcterms_description>\r\n</dcterms_description> with </dcterms_description>

if filedata.find('</dcterms_description></dcterms_description>') is not None:
    filedata = filedata.replace('</dcterms_description></dcterms_description>', '</dcterms_description>')
print ('Collapsing dcterms_description')


# --- Remove <dcterms_extent type="array">


s = '<dcterms_extent type="array">'

filedata = filedata.replace('<dcterms_extent type="array">', '')


# --- Remove <dcterms_extent type="array"/>


s = '<dcterms_extent type="array"/>'

filedata = filedata.replace('<dcterms_extent type="array"/>', '')

# --- Replace </dcterms_extent>\r\n<dcterms_extent> with ; 

if filedata.find('</dcterms_extent><dcterms_extent>') is not None:
    filedata = filedata.replace('</dcterms_extent><dcterms_extent>', '; ')
print ('Separating multiple dcterms_extent entries with semicolon and space')


# --- Replace </dcterms_extent><dcterms_extent> with ;

if filedata.find('</dcterms_extent><dcterms_extent>') is not None:
    filedata = filedata.replace('</dcterms_extent><dcterms_extent>', '; ')
print ('Separating multiple dcterms_extent entries without line break to semicolon and space')


# --- Replace </dcterms_extent>\r\n</dcterms_extent> with </dcterms_extent>

if filedata.find('</dcterms_extent></dcterms_extent>') is not None:
    filedata = filedata.replace('</dcterms_extent></dcterms_extent>', '</dcterms_extent>')
print ('Collapsing dcterms_extent')


# --- Remove <dcterms_medium type="array">


s = '<dcterms_medium type="array">'

filedata = filedata.replace('<dcterms_medium type="array">', '')


# --- Remove <dcterms_medium type="array"/>


s = '<dcterms_medium type="array"/>'

filedata = filedata.replace('<dcterms_medium type="array"/>', '')

# --- Replace </dcterms_medium>\r\n<dcterms_medium> with ; 

if filedata.find('</dcterms_medium><dcterms_medium>') is not None:
    filedata = filedata.replace('</dcterms_medium><dcterms_medium>', '; ')
print ('Separating multiple dcterms_medium entries with semicolon and space')


# --- Replace </dcterms_medium><dcterms_medium> with ;

if filedata.find('</dcterms_medium><dcterms_medium>') is not None:
    filedata = filedata.replace('</dcterms_medium><dcterms_medium>', '; ')
print ('Separating multiple dcterms_medium entries without line break to semicolon and space')


# --- Replace </dcterms_medium>\r\n</dcterms_medium> with </dcterms_medium>

if filedata.find('</dcterms_medium></dcterms_medium>') is not None:
    filedata = filedata.replace('</dcterms_medium></dcterms_medium>', '</dcterms_medium>')
print ('Collapsing dcterms_medium')


# --- Remove <dcterms_identifier type="array">


s = '<dcterms_identifier type="array">'

filedata = filedata.replace('<dcterms_identifier type="array">', '')


# --- Remove <dcterms_identifier type="array"/>


s = '<dcterms_identifier type="array"/>'

filedata = filedata.replace('<dcterms_identifier type="array"/>', '')

# --- Replace </dcterms_identifier>\r\n<dcterms_identifier> with ; 

if filedata.find('</dcterms_identifier><dcterms_identifier>') is not None:
    filedata = filedata.replace('</dcterms_identifier><dcterms_identifier>', '; ')
print ('Separating multiple dcterms_identifier entries with semicolon and space')


# --- Replace </dcterms_identifier><dcterms_identifier> with ;

if filedata.find('</dcterms_identifier><dcterms_identifier>') is not None:
    filedata = filedata.replace('</dcterms_identifier><dcterms_identifier>', '; ')
print ('Separating multiple dcterms_identifier entries without line break to semicolon and space')


# --- Replace </dcterms_identifier>\r\n</dcterms_identifier> with </dcterms_identifier>

if filedata.find('</dcterms_identifier></dcterms_identifier>') is not None:
    filedata = filedata.replace('</dcterms_identifier></dcterms_identifier>', '</dcterms_identifier>')
print ('Collapsing dcterms_identifier')


# --- Remove <dcterms_language type="array">


s = '<dcterms_language type="array">'

filedata = filedata.replace('<dcterms_language type="array">', '')


# --- Remove <dcterms_language type="array"/>


s = '<dcterms_language type="array"/>'

filedata = filedata.replace('<dcterms_language type="array"/>', '')

# --- Replace </dcterms_language>\r\n<dcterms_language> with ; 

if filedata.find('</dcterms_language><dcterms_language>') is not None:
    filedata = filedata.replace('</dcterms_language><dcterms_language>', '; ')
print ('Separating multiple dcterms_language entries with semicolon and space')


# --- Replace </dcterms_language><dcterms_language> with ;

if filedata.find('</dcterms_language><dcterms_language>') is not None:
    filedata = filedata.replace('</dcterms_language><dcterms_language>', '; ')
print ('Separating multiple dcterms_language entries without line break to semicolon and space')


# --- Replace </dcterms_language>\r\n</dcterms_language> with </dcterms_language>

if filedata.find('</dcterms_language></dcterms_language>') is not None:
    filedata = filedata.replace('</dcterms_language></dcterms_language>', '</dcterms_language>')
print ('Collapsing dcterms_language')


# --- Remove <dcterms_spatial type="array">


s = '<dcterms_spatial type="array">'

filedata = filedata.replace('<dcterms_spatial type="array">', '')


# --- Remove <dcterms_spatial type="array"/>


s = '<dcterms_spatial type="array"/>'

filedata = filedata.replace('<dcterms_spatial type="array"/>', '')

# --- Replace </dcterms_spatial>\r\n<dcterms_spatial> with ; 

if filedata.find('</dcterms_spatial><dcterms_spatial>') is not None:
    filedata = filedata.replace('</dcterms_spatial><dcterms_spatial>', '; ')
print ('Separating multiple dcterms_spatial entries with semicolon and space')


# --- Replace </dcterms_spatial><dcterms_spatial> with ;

if filedata.find('</dcterms_spatial><dcterms_spatial>') is not None:
    filedata = filedata.replace('</dcterms_spatial><dcterms_spatial>', '; ')
print ('Separating multiple dcterms_spatial entries without line break to semicolon and space')


# --- Replace </dcterms_spatial>\r\n</dcterms_spatial> with </dcterms_spatial>

if filedata.find('</dcterms_spatial></dcterms_spatial>') is not None:
    filedata = filedata.replace('</dcterms_spatial></dcterms_spatial>', '</dcterms_spatial>')
print ('Collapsing dcterms_spatial')


# --- Remove <dcterms_publisher type="array">


s = '<dcterms_publisher type="array">'

filedata = filedata.replace('<dcterms_publisher type="array">', '')


# --- Remove <dcterms_publisher type="array"/>


s = '<dcterms_publisher type="array"/>'

filedata = filedata.replace('<dcterms_publisher type="array"/>', '')

# --- Replace </dcterms_publisher>\r\n<dcterms_publisher> with ; 

if filedata.find('</dcterms_publisher><dcterms_publisher>') is not None:
    filedata = filedata.replace('</dcterms_publisher><dcterms_publisher>', '; ')
print ('Separating multiple dcterms_publisher entries with semicolon and space')


# --- Replace </dcterms_publisher><dcterms_publisher> with ;

if filedata.find('</dcterms_publisher><dcterms_publisher>') is not None:
    filedata = filedata.replace('</dcterms_publisher><dcterms_publisher>', '; ')
print ('Separating multiple dcterms_publisher entries without line break to semicolon and space')


# --- Replace </dcterms_publisher>\r\n</dcterms_publisher> with </dcterms_publisher>

if filedata.find('</dcterms_publisher></dcterms_publisher>') is not None:
    filedata = filedata.replace('</dcterms_publisher></dcterms_publisher>', '</dcterms_publisher>')
print ('Collapsing dcterms_publisher')


# --- Remove <dcterms_rights_holder type="array">


s = '<dcterms_rights_holder type="array">'

filedata = filedata.replace('<dcterms_rights_holder type="array">', '')


# --- Remove <dcterms_rights_holder type="array"/>


s = '<dcterms_rights_holder type="array"/>'

filedata = filedata.replace('<dcterms_rights_holder type="array"/>', '')

# --- Replace </dcterms_rights_holder>\r\n<dcterms_rights_holder> with ; 

if filedata.find('</dcterms_rights_holder><dcterms_rights_holder>') is not None:
    filedata = filedata.replace('</dcterms_rights_holder><dcterms_rights_holder>', '; ')
print ('Separating multiple dcterms_rights_holder entries with semicolon and space')


# --- Replace </dcterms_rights_holder><dcterms_rights_holder> with ;

if filedata.find('</dcterms_rights_holder><dcterms_rights_holder>') is not None:
    filedata = filedata.replace('</dcterms_rights_holder><dcterms_rights_holder>', '; ')
print ('Separating multiple dcterms_rights_holder entries without line break to semicolon and space')


# --- Replace </dcterms_rights_holder>\r\n</dcterms_rights_holder> with </dcterms_rights_holder>

if filedata.find('</dcterms_rights_holder></dcterms_rights_holder>') is not None:
    filedata = filedata.replace('</dcterms_rights_holder></dcterms_rights_holder>', '</dcterms_rights_holder>')
print ('Collapsing dcterms_rights_holder')


# --- Remove <dcterms_subject type="array">


s = '<dcterms_subject type="array">'

filedata = filedata.replace('<dcterms_subject type="array">', '')


# --- Remove <dcterms_subject type="array"/>


s = '<dcterms_subject type="array"/>'

filedata = filedata.replace('<dcterms_subject type="array"/>', '')

# --- Replace </dcterms_subject>\r\n<dcterms_subject> with ; 

if filedata.find('</dcterms_subject><dcterms_subject>') is not None:
    filedata = filedata.replace('</dcterms_subject><dcterms_subject>', '; ')
print ('Separating multiple dcterms_subject entries with semicolon and space')


# --- Replace </dcterms_subject><dcterms_subject> with ;

if filedata.find('</dcterms_subject><dcterms_subject>') is not None:
    filedata = filedata.replace('</dcterms_subject><dcterms_subject>', '; ')
print ('Separating multiple dcterms_subject entries without line break to semicolon and space')


# --- Replace </dcterms_subject>\r\n</dcterms_subject> with </dcterms_subject>

if filedata.find('</dcterms_subject></dcterms_subject>') is not None:
    filedata = filedata.replace('</dcterms_subject></dcterms_subject>', '</dcterms_subject>')
print ('Collapsing dcterms_subject')


# --- Remove <dcterms_temporal type="array">


s = '<dcterms_temporal type="array">'

filedata = filedata.replace('<dcterms_temporal type="array">', '')


# --- Remove <dcterms_temporal type="array"/>


s = '<dcterms_temporal type="array"/>'

filedata = filedata.replace('<dcterms_temporal type="array"/>', '')

# --- Replace </dcterms_temporal>\r\n<dcterms_temporal> with ; 

if filedata.find('</dcterms_temporal><dcterms_temporal>') is not None:
    filedata = filedata.replace('</dcterms_temporal><dcterms_temporal>', '; ')
print ('Separating multiple dcterms_temporal entries with semicolon and space')


# --- Replace </dcterms_temporal><dcterms_temporal> with ;

if filedata.find('</dcterms_temporal><dcterms_temporal>') is not None:
    filedata = filedata.replace('</dcterms_temporal><dcterms_temporal>', '; ')
print ('Separating multiple dcterms_temporal entries without line break to semicolon and space')


# --- Replace </dcterms_temporal>\r\n</dcterms_temporal> with </dcterms_temporal>

if filedata.find('</dcterms_temporal></dcterms_temporal>') is not None:
    filedata = filedata.replace('</dcterms_temporal></dcterms_temporal>', '</dcterms_temporal>')
print ('Collapsing dcterms_temporal')


# --- Remove <dcterms_title type="array">


s = '<dcterms_title type="array">'

filedata = filedata.replace('<dcterms_title type="array">', '')


# --- Remove <dcterms_title type="array"/>


s = '<dcterms_title type="array"/>'

filedata = filedata.replace('<dcterms_title type="array"/>', '')

# --- Replace </dcterms_title>\r\n<dcterms_title> with ; 

if filedata.find('</dcterms_title><dcterms_title>') is not None:
    filedata = filedata.replace('</dcterms_title><dcterms_title>', '; ')
print ('Separating multiple dcterms_title entries with semicolon and space')


# --- Replace </dcterms_title><dcterms_title> with ;

if filedata.find('</dcterms_title><dcterms_title>') is not None:
    filedata = filedata.replace('</dcterms_title><dcterms_title>', '; ')
print ('Separating multiple dcterms_title entries without line break to semicolon and space')


# --- Replace </dcterms_title>\r\n</dcterms_title> with </dcterms_title>

if filedata.find('</dcterms_title></dcterms_title>') is not None:
    filedata = filedata.replace('</dcterms_title></dcterms_title>', '</dcterms_title>')
print ('Collapsing dcterms_title')


# --- Remove <dcterms_type type="array">


s = '<dcterms_type type="array">'

filedata = filedata.replace('<dcterms_type type="array">', '')


# --- Remove <dcterms_type type="array"/>


s = '<dcterms_type type="array"/>'

filedata = filedata.replace('<dcterms_type type="array"/>', '')

# --- Replace </dcterms_type>\r\n<dcterms_type> with ; 

if filedata.find('</dcterms_type><dcterms_type>') is not None:
    filedata = filedata.replace('</dcterms_type><dcterms_type>', '; ')
print ('Separating multiple dcterms_type entries with semicolon and space')


# --- Replace </dcterms_type><dcterms_type> with ;

if filedata.find('</dcterms_type><dcterms_type>') is not None:
    filedata = filedata.replace('</dcterms_type><dcterms_type>', '; ')
print ('Separating multiple dcterms_type entries without line break to semicolon and space')


# --- Replace </dcterms_type>\r\n</dcterms_type> with </dcterms_type>

if filedata.find('</dcterms_type></dcterms_type>') is not None:
    filedata = filedata.replace('</dcterms_type></dcterms_type>', '</dcterms_type>')
print ('Collapsing dcterms_type')


# --- Remove <edm_is_shown_at type="array">


s = '<edm_is_shown_at type="array">'

filedata = filedata.replace('<edm_is_shown_at type="array">', '')


# --- Remove <edm_is_shown_at type="array"/>


s = '<edm_is_shown_at type="array"/>'

filedata = filedata.replace('<edm_is_shown_at type="array"/>', '')

# --- Replace </edm_is_shown_at>\r\n<edm_is_shown_at> with ; 

if filedata.find('</edm_is_shown_at><edm_is_shown_at>') is not None:
    filedata = filedata.replace('</edm_is_shown_at><edm_is_shown_at>', '; ')
print ('Separating multiple edm_is_shown_at entries with semicolon and space')


# --- Replace </edm_is_shown_at><edm_is_shown_at> with ;

if filedata.find('</edm_is_shown_at><edm_is_shown_at>') is not None:
    filedata = filedata.replace('</edm_is_shown_at><edm_is_shown_at>', '; ')
print ('Separating multiple edm_is_shown_at entries without line break to semicolon and space')


# --- Replace </edm_is_shown_at>\r\n</edm_is_shown_at> with </edm_is_shown_at>

if filedata.find('</edm_is_shown_at></edm_is_shown_at>') is not None:
    filedata = filedata.replace('</edm_is_shown_at></edm_is_shown_at>', '</edm_is_shown_at>')
print ('Collapsing edm_is_shown_at')


# --- Remove <dlg_local_right type="array">


s = '<dlg_local_right type="array">'

filedata = filedata.replace('<dlg_local_right type="array">', '')


# --- Remove <dlg_local_right type="array"/>


s = '<dlg_local_right type="array"/>'

filedata = filedata.replace('<dlg_local_right type="array"/>', '')

# --- Replace </dlg_local_right>\r\n<dlg_local_right> with ; 

if filedata.find('</dlg_local_right><dlg_local_right>') is not None:
    filedata = filedata.replace('</dlg_local_right><dlg_local_right>', '; ')
print ('Separating multiple dlg_local_right entries with semicolon and space')


# --- Replace </dlg_local_right><dlg_local_right> with ;

if filedata.find('</dlg_local_right><dlg_local_right>') is not None:
    filedata = filedata.replace('</dlg_local_right><dlg_local_right>', '; ')
print ('Separating multiple dlg_local_right entries without line break to semicolon and space')


# --- Replace </dlg_local_right>\r\n</dlg_local_right> with </dlg_local_right>

if filedata.find('</dlg_local_right></dlg_local_right>') is not None:
    filedata = filedata.replace('</dlg_local_right></dlg_local_right>', '</dlg_local_right>')
print ('Collapsing dlg_local_right')


# --- Remove <dlg_subject_personal type="array">


s = '<dlg_subject_personal type="array">'

filedata = filedata.replace('<dlg_subject_personal type="array">', '')


# --- Remove <dlg_subject_personal type="array"/>


s = '<dlg_subject_personal type="array"/>'

filedata = filedata.replace('<dlg_subject_personal type="array"/>', '')

# --- Replace </dlg_subject_personal>\r\n<dlg_subject_personal> with ; 

if filedata.find('</dlg_subject_personal><dlg_subject_personal>') is not None:
    filedata = filedata.replace('</dlg_subject_personal><dlg_subject_personal>', '; ')
print ('Separating multiple dlg_subject_personal entries with semicolon and space')


# --- Replace </dlg_subject_personal><dlg_subject_personal> with ;

if filedata.find('</dlg_subject_personal><dlg_subject_personal>') is not None:
    filedata = filedata.replace('</dlg_subject_personal><dlg_subject_personal>', '; ')
print ('Separating multiple dlg_subject_personal entries without line break to semicolon and space')


# --- Replace </dlg_subject_personal>\r\n</dlg_subject_personal> with </dlg_subject_personal>

if filedata.find('</dlg_subject_personal></dlg_subject_personal>') is not None:
    filedata = filedata.replace('</dlg_subject_personal></dlg_subject_personal>', '</dlg_subject_personal>')
print ('Collapsing dlg_subject_personal')


# --- Remove <edm_is_shown_by type="array">


s = '<edm_is_shown_by type="array">'

filedata = filedata.replace('<edm_is_shown_by type="array">', '')


# --- Remove <edm_is_shown_by type="array"/>


s = '<edm_is_shown_by type="array"/>'

filedata = filedata.replace('<edm_is_shown_by type="array"/>', '')

# --- Replace </edm_is_shown_by>\r\n<edm_is_shown_by> with ; 

if filedata.find('</edm_is_shown_by><edm_is_shown_by>') is not None:
    filedata = filedata.replace('</edm_is_shown_by><edm_is_shown_by>', '; ')
print ('Separating multiple edm_is_shown_by entries with semicolon and space')


# --- Replace </edm_is_shown_by><edm_is_shown_by> with ;

if filedata.find('</edm_is_shown_by><edm_is_shown_by>') is not None:
    filedata = filedata.replace('</edm_is_shown_by><edm_is_shown_by>', '; ')
print ('Separating multiple edm_is_shown_by entries without line break to semicolon and space')


# --- Replace </edm_is_shown_by>\r\n</edm_is_shown_by> with </edm_is_shown_by>

if filedata.find('</edm_is_shown_by></edm_is_shown_by>') is not None:
    filedata = filedata.replace('</edm_is_shown_by></edm_is_shown_by>', '</edm_is_shown_by>')
print ('Collapsing edm_is_shown_by')


# --- Remove <dcterms_provenance type="array">


s = '<dcterms_provenance type="array">'

filedata = filedata.replace('<dcterms_provenance type="array">', '')


# --- Remove <dcterms_provenance type="array"/>


s = '<dcterms_provenance type="array"/>'

filedata = filedata.replace('<dcterms_provenance type="array"/>', '')


# --- Replace </dcterms_provenance>\r\n</dcterms_provenance> with </dcterms_provenance>

if filedata.find('</dcterms_provenance></dcterms_provenance>') is not None:
    filedata = filedata.replace('</dcterms_provenance></dcterms_provenance>', '</dcterms_provenance>')
print ('Collapsing dcterms_provenance')


# --- Remove <other_colls type="array">


s = '<other_colls type="array">'

filedata = filedata.replace('<other_colls type="array">', '')


# --- Remove <other_colls type="array"/>


s = '<other_colls type="array"/>'

filedata = filedata.replace('<other_colls type="array"/>', '')

# --- Replace </other_colls>\r\n<other_colls> with ; 

if filedata.find('</other_colls><other_colls>') is not None:
    filedata = filedata.replace('</other_colls><other_colls>', '; ')
print ('Separating multiple other_colls entries with semicolon and space')


# --- Replace </other_colls><other_colls> with ;

if filedata.find('</other_colls><other_colls>') is not None:
    filedata = filedata.replace('</other_colls><other_colls>', '; ')
print ('Separating multiple other_colls entries without line break to semicolon and space')


# --- Replace </other_colls>\r\n</other_colls> with </other_colls>

if filedata.find('</other_colls></other_colls>') is not None:
    filedata = filedata.replace('</other_colls></other_colls>', '</other_colls>')
print ('Collapsing other_colls')


# --- Remove <dcterms_bibliographic_citation type="array">


s = '<dcterms_bibliographic_citation type="array">'

filedata = filedata.replace('<dcterms_bibliographic_citation type="array">', '')


# --- Remove <dcterms_bibliographic_citation type="array"/>


s = '<dcterms_bibliographic_citation type="array"/>'

filedata = filedata.replace('<dcterms_bibliographic_citation type="array"/>', '')

# --- Replace </dcterms_bibliographic_citation>\r\n<dcterms_bibliographic_citation> with ; 

if filedata.find('</dcterms_bibliographic_citation><dcterms_bibliographic_citation>') is not None:
    filedata = filedata.replace('</dcterms_bibliographic_citation><dcterms_bibliographic_citation>', '; ')
print ('Separating multiple dcterms_bibliographic_citation entries with semicolon and space')


# --- Replace </dcterms_bibliographic_citation><dcterms_bibliographic_citation> with ;

if filedata.find('</dcterms_bibliographic_citation><dcterms_bibliographic_citation>') is not None:
    filedata = filedata.replace('</dcterms_bibliographic_citation><dcterms_bibliographic_citation>', '; ')
print ('Separating multiple dcterms_bibliographic_citation entries without line break to semicolon and space')


# --- Replace </dcterms_bibliographic_citation>\r\n</dcterms_bibliographic_citation> with </dcterms_bibliographic_citation>

if filedata.find('</dcterms_bibliographic_citation></dcterms_bibliographic_citation>') is not None:
    filedata = filedata.replace('</dcterms_bibliographic_citation></dcterms_bibliographic_citation>', '</dcterms_bibliographic_citation>')
print ('Collapsing dcterms_bibliographic_citation')




# --- Insert breaks so file is legible ---
filedata = filedata.replace('><', '>\r\n<')


# --- Look for semicolons at the end of string (CONTENTdm specfic)
#if filedata.find(';<') is not None:
#    filedata = filedata.replace(';<', '<')
#    print('Removing trailing semicolons')

# --- Replace &amp; with &amp to make splitting tags easier ---
if filedata.find('&amp;') is not None:
    filedata = filedata.replace('&amp;', '&amp')

# --- Add &amp; reference back for valid XML ---
if filedata.find('&amp') is not None:
    filedata = filedata.replace('&amp', '&#38;')


'''Output new file with all changes'''
# --- Create new xml file ---
# --- Split filename from extension
filename = xmlFile
(prefix, sep, suffix) = filename.rpartition('.')

# --- Add _flat to filename ---
new_filename = prefix + '_flat.xml'

# --- Write new file --
with open(new_filename, 'w', encoding="utf-8") as prepFile:
  prepFile.write(filedata)

file.close()
prepFile.close()

print('\n', 'Your new file,', new_filename, ', has been created.')

input("Press Enter to close...")
