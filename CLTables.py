class CLTable:
    def __init__(self, columnNames: list, rowNames: list, valueMatrix: list):
        self.columnNames = columnNames
        self.rowNames = rowNames
        self.values = valueMatrix

    def printTable(self):
        #Building first line (Column names)
        columnString = " "*len(max(self.rowNames, key=len)) + " |"

        for columnIndex in range(0,len(self.columnNames)):
            #Building filler if row item is larger than columnName
            columnFillString = ""
            for row in self.values:
                if len(row[columnIndex]) > len(self.columnNames[columnIndex]):
                    if len(row[columnIndex]) > len(columnFillString):
                        columnFillString = " "*(len(row[columnIndex])-len(self.columnNames[columnIndex]))
            #Asigning filler
            self.columnNames[columnIndex] = self.columnNames[columnIndex] + columnFillString
            #Building columString
            columnString += " " + self.columnNames[columnIndex] +" |"


        #Building split string between rows
        rowSplitString = ""
        for c in columnString:
            if c=="|":
                rowSplitString += "|"
            else:
                rowSplitString += "-"

        print(columnString)
        print(rowSplitString)


        #Building rows
        longestRow = len(max(self.rowNames, key=len))
        for rowIndex in range(0, len(self.rowNames)):
            fillStringLength = longestRow-len(self.rowNames[rowIndex])
            fillString = ""
            if fillStringLength > 0:
                fillString = " "*fillStringLength
            rowString = self.rowNames[rowIndex] + fillString + " |"
            for columnIndex in range(0, len(self.values[rowIndex])):
                rowString += " " + self.values[rowIndex][columnIndex] + " "*(len(self.columnNames[columnIndex])-len(self.values[rowIndex][columnIndex])) + " |"
            print(rowString)
            print(rowSplitString)