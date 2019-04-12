from CLTables import *

matrix = [["row1column1", "row1column2", "row1column3"],                  #Values for row 1
          ["row2column1", "row2verylongcolumn2name", "row2column3"],      #Values for row 2
          ["row3column1", "row2column2", "row3longercolumn3"]]            #Values for row 3

columnNames = ["Column1", "Column2", "Column3"]                           #Column names
rowNames = ["Row1", "Row2", "Row3Long"]                                   #Row names

table = CLTable(columnNames, rowNames, matrix)                            #Creating the table -> CLTable(columnNames: list, rowNames: list, matrix: list)

table.printTable()                                                        #Printing the table