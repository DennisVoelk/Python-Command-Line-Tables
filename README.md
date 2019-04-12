# PythonCLTables
A simple tool for creating tables inside the command line.

![SampleOutput](screenshot.png)


## Usage
1. Define a matrix with the table content.  
`matrix = [["row1column1", "row1column2"],
          ["row2column1", "row2verylongcolumn2name"]]`

2. Define a list with the column names.  
`columnNames = ["Column1", "Column2", "Column3"]`

3. Define a list with the row names.  
`rowNames = ["Row1", "Row2", "Row3Long"]`

4. Create the table object.  
`table = CLTable(columnNames, rowNames, matrix)`

5. Print the table.  
`table.printTable()`