# Calculator of monthly expenses.
# In this version data is taken from the file with defined format:
# Expense Name, Expense Amount, Expense Date, Expense Category(tag)

# Default Dictionary {Expense Name: Expense Amount, Expense Date, [Expense Category]
expDict = {}

datafile = "SampleDataSimplified2.txt"

print("Using file '" + datafile + "' as a data source.")
print("\n")

# Function opens the datafile, reads this file line by line and fills the dictionary with entries.
# Expense Name is used as a key while other details are stored as values in the dictionary.

def CreatExpDict(datafile):

    with open(datafile, "r") as sample:
        for line in sample:
            line = line.rstrip()
            row = line.split(',')
            expDict[row[0]] = row[1], row[2], row[3]

    return expDict

CreatExpDict(datafile)

# This function calculates the total amount of expenses by iterating over dictionary using key values.
# Expense Amount is being added to TotalExpenses value.

def ExpTotal(expDict):

    TotalExpenses = 0
    for key in expDict:
        TotalExpenses += int(expDict[key][0])
    print("\n" + "Total amount spent is " + str(TotalExpenses) + " CZK" + "\n")
    return TotalExpenses

# ExpTotal(expDict)

# This function is iterating through dictionary of expenses using keys. Then iterates through tag values in dictionary.
# Using tag as key the amount from the previous dictionary is being added to value of specific category.
# Prints the data for categories where amount is higher than 0.


def ExpPerCategory(expDict):

    # Dictionary with description of all expense categories.
    CategoryDescription = {"Rent": "Monthly flat rent payment",
                           "Communications": "Phone and internet payments",
                           "Utilities": "Monthly payments for gas and electricity",
                           "Entertainment": "Any kind of entertainment activities or purchases",
                           "Restaurants": "Eating out in restaurants or cafes",
                           "Health": "Medicine, expenses in pharmacy, therapy",
                           "Sports": "Anything sports related. Supplements, training...",
                           "Self-Development": "Purchasing courses and educational materials",
                           "Alcohol": "Expenses on alcohol",
                           "Electronics": "Expenses on electronic gadgets",
                           "Clothes": "Expenses on new clothes",
                           "Food": "Regular food expenses",
                           "Toiletries": "Persona hygiene products",
                           "Transportation": "Public transportation",
                           "Travel": "Anything travel related. Tickets, accommodation etc.",
                           "Taxi": "Taxi expenses",
                           "Work-related": "Expenses during working hours",
                           "Unidentified": "Uncategorized or incorrectly categorized expenses"}

    categories = {"Rent": 0,
                  "Communications": 0,
                  "Utilities": 0,
                  "Entertainment": 0,
                  "Restaurants": 0,
                  "Health": 0,
                  "Sports": 0,
                  "Self-Development": 0,
                  "Alcohol": 0,
                  "Electronics": 0,
                  "Clothes": 0,
                  "Food": 0,
                  "Toiletries": 0,
                  "Transportation": 0,
                  "Travel": 0,
                  "Taxi": 0,
                  "Work-related": 0,
                  "Unidentified": 0}

    for key in expDict:
        tag = expDict[key][2]
        if tag in categories.keys():
            categories[tag] += int(expDict[key][0])
        else:
            categories["Unidentified"] += int(expDict[key][0])
            print("Some of the expenses in file were not tagged correctly")
            print("Check category descriptions for list of available categories. \n")
            pass

    for cat in categories:
        if categories[cat] != 0:
            print("{:5} CZK was spent on {} category". format(str(categories[cat]), cat))
    return categories


# ExpPerCategory(expDict)

# The function displays percentage distribution of expenses in categories in relation to total amount spent.

def PercPerCategory(categories, TotalExpenses):

    for cat in categories.keys():
        if categories[cat] != 0:
            CatPercentage = int((categories[cat] / TotalExpenses) * 100)
            print("Approximately {:}% of expenses have been spent in {} category".format(str(CatPercentage), cat))

PercPerCategory(ExpPerCategory(expDict), ExpTotal(expDict))


def ExpenseTime(expDict):

    ExpenseInTime = {}
    for key in expDict:
        if expDict[key][1] not in ExpenseInTime.keys():
            ExpenseInTime[expDict[key][1]] = int(expDict[key][0])
        else:
            ExpenseInTime[expDict[key][1]] += int(expDict[key][0])

    # for key in ExpenseInTime:
        # print(ExpenseInTime[key])


    print("\n" + "Expense distribution per date:" + "\n")
    for key in sorted(ExpenseInTime):
        print("On {} you've spend {} CZK".format(key, ExpenseInTime[key]))

ExpenseTime(expDict)
# ahoj
