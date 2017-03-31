# About dcqToDlgAdmin.py

##### *Dependencies: [Python 3.x](https://www.python.org/), [Lxml library](https://pypi.python.org/pypi/lxml)*

This program will convert properly prepared XML records to the DLGadmin nested xml structure. It works specifically with records that have been harvested using Repox from either DC or DCQ repositories. Proper formatting includes the following:

* field names outlined in the mapping document
* correct namespaces
* removal of extraneous content.


The 'link to file' will help to prepare and validate your file for reformatting. An [example xml](test_testers.xml) file is provided.


### Instructions for use
1. Drop dcqToDlgAdmin.py into the directory with your xml and run the program. (Alternatively you may run the program and input the complete file path.)
2. Provide input for the following questions:
   * What xml file would you like to add rights statement to? (do not enter file extension)
   * These records will be public. (enter true or false)
   * These records will be included in DPLA. (enter true or false)
   * These digital objects are hosted at the DLG. (enter true or false)
   * What portal(s) will these items be in? (Enter multiple values with a space between them: georgia crdl amso other)
   * What collection do these records belong to? (enter repo_coll)
   * Do these records need to be added to additional collections? (y or n)
    * If yes: Enter the additional collections with a space between them. (Ex. repo_coll repo_coll)
   * What is the base URL for the item id?
   * Were these harvested as DC or QDC records? (Enter dc or qdc)
   
### Some notes
If dcqToDlgAdmin.py is in the same directory as your xml enter only the name of the file without the extension (Ex. myXmlFile). If you are running dcqToDlgAdmin.py from a different directory use the full path (Ex. C:\some\place\myXmlFile)


The base url is the part of the isShownAt url that can be eliminated to get the item ID. For example:
   * isShownAt: http://myexample.com/id/test/54
   * base url: http://myexample.com/id/test/
