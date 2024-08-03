import json
from atexit import register

class Budget():
    def __init__(self):
        # Dump the expense records just before exiting the program
        register(self.dumpJson)
        self.currency = 'inr'
        self.categories = [
            "food",
            "transportation",
            "utilities",
            "health",
            "education",
            "entertainment",
            "savings",
            "debt",
            "others",
        ]
        self.records = self.loadJson()

    def loadJson(self):
        data = []
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
            return data
        except json.JSONDecodeError:
            return data
    
    def dumpJson(self):
        with open('data.json', 'w') as file:
            json.dump(self.records, file, indent=4)

    def getCatgories(self):
        return self.categories

    def addRecord(self, record):
        self.records.append({
            'id': self.records[-1]['id'] + 1 if len(self.records) >= 1 else 1,
            'category': record['category'],
            'title': record['title'],
            'amount': record['amount'],
            'currency': self.currency,
            'date': record['date'],
        })

    def searchByKey(self, key, value):
        return [record for record in self.records if record.get(key) == value]

    def getRecord(self, key=None, value=None, all=False):
        if all:
            return self.records
        else:
            return self.searchByKey(key, value)
        
    def deleteRecord(self, id):
        for i, record in enumerate(self.records):                   
            if record.get('id') == id:
                self.records.pop(i)
                return True
        return False
    
    def updateRecord(self, id):
        for i, record in enumerate(self.records):
            if record.get('id') == id:
                print('\nID Found, What do You Want to Change:')
                while True:
                    print('1. Category')
                    print('2. Title')
                    print('3. Amount')
                    print('4. Date')
                    option = input('Please Enter the Number Your Want to Change: ')

                    match option:
                        case '1':
                            category = getCategoryFromStream()
                            self.records[i]['category'] = category
                            break
                        case '2':
                            title = getTitleFromStream()
                            self.records[i]['title'] = title
                            break
                        case '3':
                            amount = getAmountFromStream()
                            self.records[i]['amount'] = amount
                            break
                        case '4':
                            date = getDateFromStream()
                            self.records[i]['date'] = date
                            break
                        case _:
                            print('\nERROR: Please Enter Valid Number\n')
                return True
        return False

def getDaysMonths():
    days = []
    for day in range(1, 32):
        if 1 <= day <= 9:
            days.append('0'+str(day))
        else:
            days.append(str(day))
    months = []
    for month in range(1, 13):
        if 1 <= month <= 9:
            months.append('0'+str(month))
        else:
            months.append(str(month))
    return days, months

def getCategoryFromStream():
    category = ''
    while True:
        print('\nEnter Category from Provided Options: ')
        categories = budget.getCatgories()
        for i, cat in enumerate(categories):
            print(f'{i+1}. {cat}')
        category = input(': ')
        if category not in categories:
            print('\nERROR: Please Check the Spelling and Enter Category Again: ')
        else:
            break
    return category

def getDateFromStream():
    date = ''
    while True:
        date = input('Enter Date of Expense [format: day-month-year, example: 05-12-2023]: ')
        if date[:2] not in days:
            print('ERROR: Please Check the day format and Re-Enter Date')
        elif date[3:5] not in months:
            print('ERROR: Please Check the month format and Re-Enter Date')
        else:
            break  
    return date

def getTitleFromStream():
    return input('\nEnter Title of Expense [example: Outing with Friends]: ')

def getAmountFromStream():
    return input('Enter Amount in INR [example: 300]: ')

if __name__ == "__main__":
    budget = Budget()
    days, months = getDaysMonths() # Will be used by getDateFromStream Function
    
    while True:
        print('\nIncome and Expense Tracking Console App')
        print('Main Menu:')
        print('1. Add Expense')
        print('2. Show All Expenses')
        print('3. Delete Expense')
        print('4. Update Expense')
        print('5. Exit')

        option = input('\nPlease Enter Respective Number to Choose Menu Option: ')

        match option:
            case '1':
                # Add Expense
                category = getCategoryFromStream()
                title = getTitleFromStream()
                amount = getAmountFromStream()
                date = getDateFromStream()
                budget.addRecord({
                    'category': category,
                    'title': title,
                    'date': date,
                    'amount': amount,
                })

                record = budget.getRecord()[-1]
                print('\n**Your Expense is Added Successfully!\n')
                print(f'Category: {record['category']}')
                print(f'Title: {record['title']}')
                print(f'Date: {record['date']}')
            case '2':
                # Show All Expenses
                records = budget.getRecord(all=True)
                print('\n**List of All Expenses')
                for record in records:
                    print('-'*20)
                    print(f'ID: {record['id']}')
                    print(f'Category: {record['category']}')
                    print(f'Title: {record['title']}')
                    print(f'Amount: {record['amount']}/-')
                    print(f'Date: {record['date']}')
                    print(f'Currency: {record['currency']}')
                print('-'*20)
            case '3':
                # Delete Expense
                id = int(input('\nPlease Enter the ID of the Expense Record You Want to Delete: '))
                if budget.deleteRecord(id=id):
                    print('\nRecord is Deleted Successfully!')
                else:
                    print('\nERROR: ID not found, Please Check again and Enter a Valid ID')
            case '4':
                # Update Expense
                id = int(input('\nPlease Enter the ID of the Expense Record You Want to Update: '))
                if budget.updateRecord(id=id):
                    print('\nRecord is Updated Successfully!')
                else:
                    print('\nERROR: ID not found, Please Check again and Enter a Valid ID')

            case '5':
                # Exiting from Program
                print('\nExiting the Program....')
                break
            case _:
                pass

    print()
