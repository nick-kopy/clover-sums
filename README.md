This is a python script (?) meant to help with a real world accounting problem.

The data used in this project was transaction data from a Clover point of sale device.
For consumer protection this data is not included in this repository.

The purpose of this script was to help organize accounting and banking information.

At a particular company, during tax reconciliation, bank account information and Clover records needed to be compared against one another.
Bank information came in seemingly arbitrary sums of transactions while Clover records were listed one transaction at a time.
Further confusing the issue was that charges were always made for all customers on the first of the month.

This script helped by taking one of these bank statement sums and giving back which Clover transactions add up to that sum.

Example:
A bank statment includes $1400 on 7/1, which transactions on Clover do we reconcile this with?
Run ($1400, June) through the python script and...
Returns names and charges that add up to $1400 from the month of June.
"found 1 combination that matches target"
"Reyez, 200..."

This script did not completely reconcile the accounts, but was a useful tool for the accountant to cut significantly reduce work time adding numbers.