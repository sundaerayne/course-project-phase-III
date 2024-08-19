#Jennifer Endres    
#CIS 261
#Course Project Phase III

def getEmployeeName():
    employeeName = input("Please enter employee's name: ")
    return employeeName

def getDatesWorked():
    fromDate = input("Please enter the employee's start date in the format (mm/dd/yyyy): ")
    toDate = input("Please enter the employee's last date of work in the format (mm/dd/yyyy): ")
    return fromDate, toDate 

def getHoursWorked():
    hoursWorked = float(input("Please enter the number of hours employee has worked: "))
    return hoursWorked

def getHourlyRate():
    hourlyRate = float(input("Please enter the employee's hourly pay rate: "))
    return hourlyRate

def getTaxRate():
    taxRate = float(input("Please enter the employee's tax rate: "))
    return taxRate 

def CalculateTaxAndNetPay(hoursWorked, hourlyRate, taxRate):
    grossPay = hoursWorked * hourlyRate
    incomeTax = grossPay * taxRate
    netPay = grossPay - incomeTax 
    return grossPay, incomeTax, netPay 

def printinfo(employeeDetailsList):
    TotalEmployees = 0
    TotalHoursWorked = 0.00
    TotalGrossPay = 0.00
    TotalTax = 0.00
    TotalNetPay = 0.00
    for employeeList in employeeDetailsList:
        fromDate = employeeList[0]
        toDate = employeeList[1]
        employeeName = employeeList[2]
        hoursWorked = employeeList[3]
        hourlyRate = employeeList[4] 
        taxRate = employeeList[5] 
        grossPay, incomeTax, netPay = CalculateTaxAndNetPay(hoursWorked, hourlyRate, taxRate)
        print(fromDate, toDate, employeeName, f"{hoursWorked:,.2f}", f"{hourlyRate:,.2f}", f"{grossPay:,.2f}", f"{taxRate:,.1%}", f"{incomeTax:,.2f}", f"{netPay:,.2f}")
        TotalEmployees += 1
        TotalHoursWorked += hoursWorked 
        TotalGrossPay += grossPay 
        TotalTax += incomeTax 
        TotalNetPay += netPay 
        employeeTotals["TotalEmployees"] = TotalEmployees
        employeeTotals["TotalHoursWorked"] = TotalHoursWorked 
        employeeTotals["TotalGrossPay"] = TotalGrossPay
        employeeTotals["TotalTax"] = TotalTax
        employeeTotals["TotalNetPay"] = TotalNetPay 
        
def PrintTotals(employeeTotals):
    print()
    print(f"Total number of employees: {employeeTotals['TotalEmployees']}")
    print(f"Total number of hours worked: {employeeTotals['TotalHoursWorked']}")
    print(f"Total amount of gross pay: {employeeTotals['TotalGrossPay']:,.2f}")
    print(f"Total amount of income tax: {employeeTotals['TotalTax']:,.1%}")
    print(f"Total amount of net pay: {employeeTotals['TotalNetPay']:,.2f}")

def WriteEmployeeInformation(employee):
    file = open("employeeinfo.txt", "a")

    file.write('{}|{}|{}|{}|{}|{}|\n'.format(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))


def getFromDate():
    valid = False
    fromDate = ""

    while not valid:
        fromDate = input("Please enter the employee's start date in the format (mm/dd/yyyy): ")
        if (len(fromDate.split('/')) != 3 and fromDate.upper() != 'ALL'):
            print("Invalid date format!")
        else:
            valid = True 
    return fromDate 

def ReadEmployeeInformation(fromDate):
    employeeDetailsList = []

    file = open("employeeinfo.txt", "r")
    data = file.readlines()
    condition = True 
    if fromDate.upper() == 'ALL':
        condition = False 
    for employee in data:
        employee = [x.strip() for x in employee.strip().split("|")]
        if not condition:
           employeeDetailsList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
        else:
            if fromDate == employee[0]:
                employeeDetailsList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
    return employeeDetailsList 

if __name__ == "__main__":
    employeeDetailsList = []
    employeeTotals = {}
    
    while True:
        employeeName = getEmployeeName()
        if (employeeName.upper() == "END"):
            break
        fromDate, toDate = getDatesWorked()
        hoursWorked = getHoursWorked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
       
        print()

        employeeDetails = [fromDate, toDate, employeeName, hoursWorked, hourlyRate, taxRate]
        WriteEmployeeInformation(employeeDetails)
    print()
    print()
    fromDate = getFromDate()

    employeeDetailsList = ReadEmployeeInformation(fromDate)

    print()
    printinfo(employeeDetailsList)
    print()
    PrintTotals(employeeTotals)

