General
-------
Easy to use expense tracking and budgeting tool.  
Designed to be customizable and usable with minimal effort.  
Also designed to help keep user on a pre-set budget.  
Displays the user's cost/day of living and "true" cost of expense.  
My first foray into app making!!

Data model
-----------
Tables:
Users
	username
	password
	budget
	date
Expenses
	type
	amount
	date
	username
	description
Macros
	username
	key
	value
	standard

Features
--------
Implemented 

1. Account creation and user login
2. Add Expenses 
3. Add macros 
4. Ability to delete Expenses and Macros
5. Individual editing page for each expense & fix data queries to use foreign 
keys
6. CRUD for budget

Need to implement

2. Display dollars remaining/percentage of budget used 
3. Live update cost/day (Think about graphs here as well, how to display above data as graphs) 
4. Bootstrap & design 
5. Reevaluate features, refactpr code and fiddle with performance 
6. Deploy and writeup 
7. Begin mobile app development

Log
----
2014/08/05 - Took out repos, refactored code, live updated of expenses and macros
2014/08/06 - Ability to delete Expenses and Macros
2014/08/08 - Individual editing page for each expense & fix data model & queries to use foreign keys to relate tables
2014/08/09 - CRUD for budget

