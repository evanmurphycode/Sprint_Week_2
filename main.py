# Sprint Week 2!

# Author: Evan Murphy & Stephen Menecola

# Date: 03/12/21

import Backpack as BP
from datetime import datetime
HST = 0.15
ClaimNumber = 0

#Reads and initialises from Deflt.dat file
f = open('Deflt.dat', 'r')
ClaimNumber = int(f.readline())
HST = float(f.readline())
f.close()

#This function will process salesperson travel claims
def TravelClaim(ClaimNumber):
    while True:
        EmployeeNumber = 7512 #int(input("Enter employee number: "))
        EmployeeName = "Billy Boob" #input("Enter employee name: ")
        TripLocation = "Punta Cannies" #input("Enter location of travel: ")

        #Format the dates to allow them to be subtracted****

        #newdate1 = time.strptime(date1, "%d/%m/%Y") and newdate2 = time.strptime(date2, "%d/%m/%Y")
        StartDatestr = input("Business trip start date (ie.yyyy-mm-dd): ")
        EndDatestr = input("Business trip end date: ")
        StartDate = datetime.strptime(StartDatestr, "%Y-%m-%d")
        EndDate = datetime.strptime(EndDatestr, "%Y-%m-%d")

        TotalTravelDays = int((EndDate - StartDate).days)

        OwnOrRented = "O" #input("Was the vehicle owned or rented? (O/R): ")
        TotalKilometers = 1362 #int(input("Enter the total kilometers travelled: "))

        if TotalTravelDays <= 3:
            PerDiem = TotalTravelDays * 85.00
        else:
            PerDiem = TotalTravelDays * 100.00

        if OwnOrRented.upper() == "O":
            MileageAmount = TotalKilometers * 0.10
        elif OwnOrRented.upper() == "R":
            MileageAmount = TotalTravelDays * 56.00
        else:
            MileageAmount = 0

        ClaimAmount = PerDiem + MileageAmount
        TaxAmount = PerDiem * 0.15
        ClaimTotal = ClaimAmount + TaxAmount

        #Formatting and printing results

        print()
        print("             NL Chocolate Company - Travel Claim")
        print()
        print("*"*60)
        print()
        print("Employee Number: {}            Employee Name: {}".format(EmployeeNumber, EmployeeName))
        print()
        print("Travel location: {}".format(TripLocation))
        print("Travel Start Date: {}    Travel End Date: {}".format(StartDate, EndDate))
        print()
        print("Total Days Travelled:         {}".format(TotalTravelDays))
        print("Car Status (Owned or Rented): {}".format(OwnOrRented))
        print("Total Kilometers Travelled:   {}".format(TotalKilometers))
        print()
        print("*"*60)
        print()
        print("Daily Cost:   ${:,.2f}".format(PerDiem))
        print("Mileage Cost: ${:,.2f}".format(MileageAmount))
        print("Claim Amount: ${:,.2f}".format(ClaimAmount))
        print("Tax Amount:          ${:,.2f}".format(TaxAmount))
        print("              ----------")
        print("Claim Total:  ${:,.2f}".format(ClaimTotal))
        print()
        print("")

        file = open("Claims.dat", "a")

        #inputs
        file.write("{}, ".format(ClaimNumber))
        file.write("{}, ".format(EmployeeNumber))
        file.write("{}, ".format(EmployeeName))
        file.write("{}, ".format(TripLocation))
        file.write("{}, ".format(StartDate.date()))
        file.write("{}, ".format(EndDate.date()))
        file.write("{}, ".format(TotalTravelDays))
        file.write("{}, ".format(OwnOrRented))
        file.write("{}\n".format(TotalKilometers))

        #outputs
        file.write("{}, ".format(PerDiem))
        file.write("{}, ".format(MileageAmount))
        file.write("{}, ".format(ClaimAmount))
        file.write("{}, ".format(TaxAmount))
        file.write("{}\n".format(ClaimTotal))

        file.close()
        
        #Increase claim number
        ClaimNumber += 1
        
        #Updates Deflt.dat with new claim number
        f = open('Deflt.dat', 'w')
        f.write("{}\n".format(str(ClaimNumber)))
        f.write("{}\n".format(str(HST)))
        f.close()

        print("Claim processed successfully")
        print()

        Continue = input("Process another data claim? (Enter Y for yes or any other key to end): ")
        if Continue.upper() != "Y":
            break










    Anykey = input("Press any key to continue.")


#This function will allow the user to edit the system default values
def EditDefaultValues():
    Anykey = input("Press any key to continue.")


#This function will allow the user to print a travel report
def PrintTravelReport():
    Anykey = input("Press any key to continue.")


#This function will allow the user to graph monthly claim totals
def GraphClaimTotals():
    Anykey = input("Press any key to continue.")





def main():
    while True:
        print()
        print("NL Chocolate Company - Travel Claims Processing System")
        print()
        print("1. Enter an Employee Travel Claim.")
        print("2. Edit System Default Values.")
        print("3. Print the Travel Claim Report.")
        print("4. Graph Monthly Claim Totals.")
        print("5. Quit Program.")
        print()
        while True:
            Choice = int(input("Enter choice (1-5): "))
            IsValid = BP.ValidIntegerNumber(Choice, 1, 5)
            if IsValid:
                Choice = int(Choice)
                break
        if Choice == 1:
            TravelClaim(ClaimNumber)
        elif Choice == 2:
            EditDefaultValues()
        elif Choice == 3:
            PrintTravelReport()
        elif Choice == 4:
            GraphClaimTotals()
        else:
            exit(0)

if __name__ == "__main__":
    main()


