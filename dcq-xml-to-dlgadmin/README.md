# About dcqToDlgAdmin.py

This Python 3 program will convert properly prepared XML records to the DLGadmin nested xml structure. It works specifically with records that have been harvested using Repox from either DC or DCQ repositories. Proper formatting includes the following:

* field names outlined in the mapping document
* correct namespaces
* removal of extraneous content.

# Instructions for use

1. Drop dcqToDlgAdmin.py into the directory with your xml and run the program. (Alternatively you may run the program and input the complete file path.)
2. Provide input for the following questions:
⋅⋅* These records will be pubic. (enter true or false)
⋅⋅* These records will be included in DPLA. (enter true or false)
