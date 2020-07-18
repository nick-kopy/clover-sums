## Clover sums search tool

This search tool was meant to help with a real world accounting problem.

### Privacy notice

The data used in this project was transaction data from a Clover point of sale device.
For consumer protection this data is not included in this repository.
However a sample in roughly the same format was included for demonstration.

### Purpose

The purpose of this script was to help organize accounting and banking information.

A company I recently worked for had an accounting problem. Their bank account information and Clover records needed to be compared against one another.
Their bank deposits came in seemingly arbitrary chunks of transactions all lumped together while their Clover records were listed one transaction at a time.
Further confusing the issue was that charges were always made for all customers on the first of the month so we couldn't cross reference dates.

This program helped by taking one of these bank statement sums and giving back which Clover transactions add up to that sum.

**Example:**
A bank deposit is listed as $3755 on 7/1, which transactions on Clover match this deposit?
Run $3755 and June through the program and...

it returns names and charges that add up to $3755 from the month of June!
"found 1 combination that matches target"
"Logan, 255..."

This script did not completely reconcile the accounts, but was a useful tool for the accountant to save a lot of time adding numbers.

### Installation
##### Download the data
- Download transaction_data.xlsx
  - This can be viewed in any spreadsheet software to get an overview of the data
- Download clover-sums.py
##### Set up the python environment
- Load up any environment that can run Python 3
- Your environment should include the xlrd library to read spreadsheets
  - This is noted in requirements.txt as 'xlrd==1.2.0'

### Running the search tool
Wherever you have clover-sums.py opened up you can change what month to look in and what dollar amount to look for.

Single match suggestion:
'''
month = 1
target = 1930
'''
'''
found 1 combination that matches target
Elijah, 1260.0, 255.0, 415.0
'''
Result will be a list of numbers in sequence that add up to your target, preceeded by the name associated with the first number.

Multiple match suggestion:
