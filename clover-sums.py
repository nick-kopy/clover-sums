'''Finds a particular expected sum in an excel file.
Assumes target sum will be found sequentially (not randomly).
Used to help with a real world accounting problem.
'''

# SELECT MONTH HERE; 1 is jan, 2 is feb, etc
month = 7

# SELECT TARGET HERE; no dollar sign, cents are ok (120.55)
target = 1275

import xlrd

def findSum(month, target):
    '''Return combinations of numbers that match given target in a given month.

    Arguments:
        month (int): The number of a given month (1 is Jan, 2 is Feb...)
        target (int, float): The sum of charges to be found
    
    Returns:
        num_win (int): number of combinations that match target
        matches (str): flattened list of combinations that match target
        (str): returns string if no combinations found
    '''

    # Replace 'transaction_data.xlsx' to your machine's 'local_path/transactiondata.xlsx'
    # Do not delete the r
    loc = (r'transaction_data.xlsx')
    sheet = xlrd.open_workbook(loc).sheet_by_index(month)

    # Tester list is used to sum up charges and compare against target
    sums = list()

    # List of winning element combinations and names to be returned
    matches = list()

    num_win = 0

    # Each iteration sequentially looks for a target matching sum starting from a new row
    for row in range(1, sheet.nrows):
        
        if sheet.cell_value(row, 25) == 'FAIL':  # Ignores declined purchases
            continue
        
        # Indexer i used to count values below the starting row
        i = 0

        for i in range(sheet.nrows - row):

            if sheet.cell_value(row + i, 25) == 'FAIL':
                continue

            elif sum(sums) == target:
                matches.append(sheet.cell_value(row, 9))
                matches = matches + sums
                num_win += 1
                sums = []
            
            sums.append(sheet.cell_value(row + i, 13))
            
            if sum(sums) > target:
                sums = []
                break
    
    if len(matches) == 0:
        return 'target not found'

    elif num_win == 1:
        print('found', num_win, 'combination that matches target')
        return ', '.join(map(str,matches))
        
    else:
        print('found', num_win, 'combinations that match target')
        return ', '.join(map(str,matches))


print(findSum(month-1, target))
