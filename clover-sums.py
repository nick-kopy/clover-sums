#finds a particular expected sum
#assumes target sum will be found by adding up adjacent numbers (not random)
#to help with a real world accounting thing

#import
import xlrd #only currently installed on 3.7.6 64bit environment?

def findSum(month, target):
    #for new/moved excel sheet change location
    loc = (r'C:\Users\Nick\Desktop\Clover pos 2018.xlsx') #r means raw string and ignors \U \N etc
    wb = xlrd.open_workbook(loc) #like a handle, workbook, read only once?
    sheet = wb.sheet_by_index(month) #sheet that we'll be working with

    st = list() #tester list where we're keeping our elements to sum up
    wn = list() #list of winning element combos and names that each combo starts with
    numwn = 0 #number of winning combos
    overdraw = 0

    #each iteration is a new place to start adding elements to a tester list
    for i in range(1, sheet.nrows):
        startpos = i
        if sheet.cell_value(startpos, 25) == 'FAIL': #ignores declined purchases
            continue
        if overdraw == 1: #ran out of things to add, can't get up to target, done looking
            break
        i2 = 0

        #second indexer i2 is adding elements until match/overdraw condition
        while True:
            if startpos + i2 == sheet.nrows: #saves some processing power
                overdraw = 1
                break
            if sheet.cell_value(startpos + i2, 25) == 'FAIL': #ignores fails again
                i2 += 1
                continue

            #print(sheet.cell_value(startpos + i2, 13))
            st.append(sheet.cell_value(startpos + i2, 13))
            if sum(st) == target:
                wn.append(sheet.cell_value(startpos, 9))
                wn = wn + st
                numwn += 1
                st = []
                #print('winner found')
                break
                #look for more winners though
            elif sum(st) > target:
                st = [] 
                #print('gone over!')
                break
            else:
                i2 += 1
    
    if len(wn) == 0:
        return 'target not found'
    else:
        print('found', numwn, 'combination(s) that match target')
        return wn

#SELECT MONTH HERE; 0 is jan, 1 is feb, etc
mon = 1 

#SELECT TARGET HERE (does it need to float?)
tar = 8915

output = findSum(mon, tar)
print(output)
