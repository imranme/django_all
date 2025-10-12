# Sample Excel Files for Testing

You can create these sample Excel files to test the application:

## Sample File 1: Employee Data (employees.xlsx)
```
Name          | Department | Salary | Start Date
John Doe      | IT         | 75000  | 2022-01-15
Jane Smith    | HR         | 65000  | 2021-06-01
Mike Johnson  | IT         | 80000  | 2020-03-10
Sarah Wilson  | Marketing  | 70000  | 2022-08-20
```

## Sample File 2: Sales Data (sales.xlsx)
```
Product    | Q1 Sales | Q2 Sales | Q3 Sales | Q4 Sales
Laptop     | 150000   | 180000   | 220000   | 250000
Mouse      | 15000    | 18000    | 22000    | 25000
Keyboard   | 25000    | 30000    | 35000    | 40000
Monitor    | 120000   | 140000   | 160000   | 180000
```

## Sample File 3: Inventory Data (inventory.xlsx)
```
Item ID | Item Name  | Category    | Stock | Unit Price
ITM001  | Laptop     | Electronics | 50    | 1200.00
ITM002  | Mouse      | Electronics | 200   | 25.00
ITM003  | Keyboard   | Electronics | 150   | 45.00
ITM004  | Monitor    | Electronics | 75    | 300.00
ITM005  | Desk Chair | Furniture   | 30    | 250.00
```

## How to Create These Files:

1. **Using Microsoft Excel:**
   - Open Excel
   - Create a new workbook
   - Enter the data as shown above
   - Save as .xlsx format

2. **Using Google Sheets:**
   - Create a new Google Sheet
   - Enter the data
   - Download as Excel (.xlsx) format

3. **Using LibreOffice Calc:**
   - Open LibreOffice Calc
   - Enter the data
   - Save as Excel 2007-365 (.xlsx) format

4. **Using Python (programmatically):**
   ```python
   import pandas as pd
   
   # Employee data
   employees = {
       'Name': ['John Doe', 'Jane Smith', 'Mike Johnson', 'Sarah Wilson'],
       'Department': ['IT', 'HR', 'IT', 'Marketing'],
       'Salary': [75000, 65000, 80000, 70000],
       'Start Date': ['2022-01-15', '2021-06-01', '2020-03-10', '2022-08-20']
   }
   pd.DataFrame(employees).to_excel('employees.xlsx', index=False)
   
   # Sales data
   sales = {
       'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
       'Q1 Sales': [150000, 15000, 25000, 120000],
       'Q2 Sales': [180000, 18000, 30000, 140000],
       'Q3 Sales': [220000, 22000, 35000, 160000],
       'Q4 Sales': [250000, 25000, 40000, 180000]
   }
   pd.DataFrame(sales).to_excel('sales.xlsx', index=False)
   
   # Inventory data
   inventory = {
       'Item ID': ['ITM001', 'ITM002', 'ITM003', 'ITM004', 'ITM005'],
       'Item Name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Desk Chair'],
       'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Furniture'],
       'Stock': [50, 200, 150, 75, 30],
       'Unit Price': [1200.00, 25.00, 45.00, 300.00, 250.00]
   }
   pd.DataFrame(inventory).to_excel('inventory.xlsx', index=False)
   ```

## Testing the Application:

1. Create the three sample files above
2. Start the Django server: `python manage.py runserver`
3. Visit `http://127.0.0.1:8000/`
4. Go to the Upload page
5. Select all three Excel files
6. Click "Upload and Process Files"
7. View the results on the data display page

The application will show all three files' data in separate, organized tables with options to export, toggle visibility, and more.