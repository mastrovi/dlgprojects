# About dcqToDlgAdmin

##### *Dependencies: [Python 3.x](https://www.python.org/), [Lxml library](https://pypi.python.org/pypi/lxml)*

These programs will convert properly prepared XML records to the DLGadmin nested xml structure. It works with records that have been harvested from either DC or DCQ repositories. Proper formatting includes the following:

* field names [(outlined in the mapping document)](https://docs.google.com/spreadsheets/d/1hwoKAh1_jk6HN6hyBCbwi_VizuR14RktfqoZc6jTIrs/edit?usp=sharing)
* correct namespaces
* removal of extraneous content.


The [pre-processing program](prep.py) and validation program (when it has been written, it doesn't exist yet!) will help to prepare and validate your file for reformatting. A working [example xml](test_testers.xml) file is provided.


### Instructions for use
1. Run prep.py. It will create a new file with `_prep` added to the filename and make the following modifications:
   * Strip the repox prefix
   * Add all necessary namespaces
   * Remove all deleted records
   * Convert any dc:identifier tags containing http to dcterms:isShownAt
   * Remove any dc:identifier tags ending with .jpg (thumbnail links)
2. Run dcqToDlgAdmin.py
3. Provide input for the following questions:
   * What xml file would you like to convert?
   * These records will be public. (enter t or f)
   * These records will be included in DPLA. (enter t or f)
   * These digital objects are hosted at the DLG. (enter t or f)
   * What portal(s) will these items be in? (Enter multiple values with a space between them: georgia crdl amso other)
   * What collection do these records belong to? (enter repo_coll)
   * Do these records need to be added to additional collections? (y or n)
    * If yes: Enter the additional collections with a space between them. (Ex. repo_coll repo_coll)
   * What is the base URL for the item id?
   * Were these harvested as DC or QDC records? (Enter dc or qdc)
3. The new xml file will be created in the directory containing the input file and will be named *inputFilename*_batch.xml
   
### Some notes
If dcqToDlgAdmin.py is in the same directory as your xml enter only the name of the file without the extension (Ex. myXmlFile). If you are running dcqToDlgAdmin.py from a different directory use the full path (Ex. C:\some\place\myXmlFile)


The base url is the part of the isShownAt url that can be eliminated to get the item ID. For example:
   * isShownAt: http://myexample.com/id/test/54
   * base url: http://myexample.com/id/test/
