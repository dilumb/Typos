# Typos
Quickly Scan and Summarize Typos on Your Documents.

Typos is a Python-based tool to quickly scan and summarize common typos in documents such as research papers, reports, and thesis. 
These typos aren't typically detected by your word processor. While it works with both Word (.docx) and PDF files, I have had better results with Word file due to limitations on PDF extractor (better results are expected with this upgrade to PDFMiner.six).

##Prerequisists
Make sure python-docx and pdfminer.six libraries are installed. Else install using:
pip install pdfminer.six python-docx

## How to Run
python Typos <<Word/PDF>> <<File Name and extension including path>>

## Output
Output is saved to a file named Typos.txt on the project folder. This tab seperated file has following format:
Error Term,	Correct Term,	Description,	No of Occurrences,	Pages (absolute)
List of pages is only available while checking PDF documents. When unknwon "-1" is set.

##  More Typos to Track
You can modify existing list of typos to check or add new ones to Patterns.txt file. This tab seperated file has the following format:
Error Term, Correct Term, Description, Type of Check

For example, "at el	et al.	Possible typo	Any" means that "at el" was typed instead of "et al." Moreover, it indicate that need to have the dot at the end "et al.". "Possible typo" is the description. "Any" means check any place in a sentence.

Following "Type of Check"s are currently supprted:
* Any - Check any location within a sentence
* Begin - Check only at the begining of a new sentence
* Case - Check for propoer use of upper or lower case
* RegEx - Check given regular expression
