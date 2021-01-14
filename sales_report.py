"""Generate sales report showing total melons each salesperson sold."""

#general comments: 
    # define a function for one to continue adding sale reports
    # be more descriptive of the data type contained in each variable
    # vary the variable names for easier distinction
    # use more docstrings to describe the process 

salespeople = []
# creates an empty list to store names of sales people
melons_sold = []
# creates a list to store number of melons sold in each transaction
# suggestion: create an dictionary to contain names as keys
            # the name key has a value of a dictionary, where the keys are 
            # total amount and number of melons sold

f = open('sales-report.txt')
# opens the sales-report text file
for line in f:
    #creates a for loop to iterate over every line in the text file
    line = line.rstrip()
    # this strips every line of the whitespace to the right of the last character
    entries = line.split('|')
    # this removes pipelines and splits all characeters into separate items, divided by
        # where the pipelines were before
    #suggestion: combine rstrip() and rsplit('|') in the same line: entries_list = line.rstrip().split('|')

    salesperson = entries[0]
    # assigns the first item to be a salesperson's name
    melons = int(entries[2])
    # assigns the third item to be the number of melons sold
    # list unpacking of entries list

    if salesperson in salespeople:
        # if a salesperson's name is found in the salespeople list
        position = salespeople.index(salesperson)
        # position is equal to the index at the name of the salesperson in the salespeople list
        melons_sold[position] += melons
        # the index number represented by position variable is += to the number of melons sold
    else:
        # if a salesperson's name is not found in the salespeople list
        salespeople.append(salesperson)
        # the name of the salesperson is added to the list of names
        melons_sold.append(melons)
        # the number of melons sold by that person is added to the list of melonds sold


for i in range(len(salespeople)):
    # looping through the indices of the salespeople (names) list
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
    # prints that the name of the salesperson at n index sol the number at n index melons
