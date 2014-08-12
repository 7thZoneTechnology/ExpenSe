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
7. Display dollars remaining/percentage of budget used 
8. Live update cost/day (Think about graphs here as well, how to display above data as graphs) 
9. Bootstrap & design 
Issues after bootstrapping:
	Add macro editing page - put in navbar
	Fix up budget stat logic - put in navbar
Convert expenses to table on dashboard
Monthly budget next to add expense in jumbotron
put macros in jumbotron
Fix all buttons
Add logo and color theme
Limit expenses to only top 10 entries then click to view all.

Need to implement



Display ten expenses at a time on main page --> Tried unsuccessfully to achieve with AJAX, will just reload page...
Select by month on all expenses page - can be done with page reloads
Select by expense type 

Better stats for different expense types (based on macros, e.g. pie graph of expense type/total)
Let users pick custom colors dashboard! Will need new database
Deploy and writeup 

Log
----
2014/08/05 - Took out repos, refactored code, live updated of expenses and macros
2014/08/06 - Ability to delete Expenses and Macros
2014/08/08 - Individual editing page for each expense & fix data model & queries to use foreign keys to relate tables
2014/08/09 - CRUD for budget, Display dollars remaining/percentage of budget used, Live update cost/day (Think about graphs here as well, how to display above data as graphs) 
2014/08/10 - Add macro editing page - put in navbarFix up budget stat logic - put in navbar, Convert expenses to table on dashboard, Monthly budget next to add expense in jumbotron, READY TO DEPLOY! 


