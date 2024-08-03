# Income and Expense Tracking Console App

This console application allows you to track your expenses, categorize them, and manage your records efficiently. It is built using Python and stores data in a JSON file.

## Getting Started

### Prerequisites

- Python 3.12.2

### Installation

1. Clone the repository or download the source code.
   ```sh
   git clone https://github.com/your-username/expense-tracker.git

## Features

- **Add Expense**: Add a new expense record with details such as category, title, amount, and date.
- **Show All Expenses**: Display a list of all recorded expenses.
- **Delete Expense**: Delete an expense record by its ID.
- **Update Expense**: Update the details of an existing expense record.

## Functionality

### Adding an Expense

- You will be prompted to enter the category, title, amount, and date of the expense.
- The categories are predefined as follows:
    - food
    - transportation
    - utilities
    - health
    - education
    - entertainment
    - savings
    - debt
    - others

### Showing All Expenses

- Displays a list of all expense records with their details such as ID, category, title, amount, date, and currency.

### Deleting an Expense

- You will be prompted to enter the ID of the expense record you wish to delete.
- If the ID exists, the record will be deleted; otherwise, an error message will be displayed.

### Updating an Expense

- You will be prompted to enter the ID of the expense record you wish to update.
- If the ID exists, you will be able to update the category, title, amount, or date of the record.

### File Structure

- main.py: The main script containing the console application logic.
- data.json: The JSON file where expense records are stored.

### Data Persistence

- The expense records are stored in a JSON file (data.json).
- The data is loaded from the file when the application starts and saved back to the file when the application exits.

## Contact

- For any inquiries or issues, please contact your-email@example.com.