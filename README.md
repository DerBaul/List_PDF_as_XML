# List_PDF_as_XML
I wrote this script to automate a task that usually took up to half an hour to complete.
My colleges now only need to run the script and upload the XML where it is needed.


Takes every PDF in a Folder and lists them in one XML file, plus their required Metadata for further steps.


The script is meant as one step in a more extensive process. It automates tasks that had to be done by hand prior.

The PDF files folder must be named correctly for the script to work.
"HZ ET XX.XX.XXXX"
"HZ ET 30.11.2021"

The script will take the Date from the Folder name and, to prevent wrong XML files from being generated, won't run if the folder is named wrong. 
