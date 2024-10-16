# Skyriaus darbuotojai


employees = [
    [
        'Lukas K.', 35, 3000, 1, 'vyras'
     ],
    [
        'Edita B.', 38, 1500, 0.5, 'moteris'
    ],
    [
        'Laura U.', 45, 2500, 1, 'moteris'
    ],
    [
        'Arina V.', 28, 2200, 1, 'moteris'
    ],
    [
        'Tautvydas V.', 30, 1800, 0.75, 'vyras'
    ]
]

def printInfo():
    print('------------------------------------------------------')
    print('Išsirinkite veiksmą, įrašydami jo eilės numerį:')
    print('1. Darbuotojų sąrašas')
    print('2. Įvesti naują darbuotoją')
    print('3. Redaguoti darbuotojo duomenis')
    print('4. Pašalinti darbuotoją iš sąrašo')
    print('5. Filtruoti duomenis')
    print('6. Išeiti iš programos')
    print('------------------------------------------------------')

def employeesInfo(emp, num = 1):
    print(f'{num}. Darbuotojas {emp[0]}, amžius - {emp[1]} metai, DU - {emp[2]}, užimtumas: {emp[3]}, lytis: {emp[4]}')

def printEmployees(lst = employees):
    print('---DARBUOTOJŲ SĄRAŠAS---')
    num = 1
    for emp in lst:
        employeesInfo(emp, num)
        num += 1

def addEmployees():
    print('Darbuotojo vardas ir pirmoji pavardės raidė')
    empName = input()
    print('Darbuotojo amžius')
    empAge = int( input() )
    print('Darbuotojo DU')
    empSalary = int( input() )
    print('Darbuotojo užimtumas')
    empEmployment = float(input())
    print('Darbuotojo lytis')
    empGender = input()
    employees.append([empName, empAge, empSalary, empEmployment, empGender])

def editEmployees():
    print('Įveskite darbuotojo eilės numerį, kurio informaciją norite redaguoti')
    ed = int( input() )
    employeesInfo(employees[ed - 1])
    print('Suveskite naujas reikšmes')
    print('Darbuotojo vardas ir pirmoji pavardės raidė')
    empName = input()
    print('Darbuotojo amžius')
    empAge = int(input())
    print('Darbuotojo DU')
    empSalary = int(input())
    print('Darbuotojo užimtumas')
    empEmployment = float(input())
    print('Darbuotojo lytis')
    empGender = input()
    employees[ed - 1] = [empName, empAge, empSalary, empEmployment, empGender]

def removeEmployees():
    print('Įveskite darbuotojo eilės numerį, kurio informaciją norite pašalinti')
    rem = int( input() )
    employees.pop(rem - 1)

print('---Skyriaus darbuotojų valdymo sistema---')

while True:
    printInfo()
    option = int( input() )
    match option:
        case 1:
            printEmployees()
            continue
        case 2:
            addEmployees()
        case 3:
            editEmployees()
            # printEmployees()
        case 4:
            removeEmployees()
            # printEmployees()
        case 5:
            print('Pasirinkite pagal ką filtruoti (įrašykite eilės numerį):')
            print('1. Pagal užimtumą')
            print('2. Pagal lytį')
            filterNum = int(input())
            if filterNum == 1:
                print('Įveskite eteto dydį("PL" - pilnas / "NPL" - nepilnas / "DPL" - daugiau negu pilnas)')
                flEmpl = input()
                PL = 1
                # tempList0 =[]
                for emp in employees:
                    if emp[3] == flEmpl:

            if filterNum == 2:
                print('Įveskite lytį (vyras/moteris)')
                filterGen = input().lower()
                # count = 0
                tempList = []
                for emp in employees:
                    if emp[4] == filterGen:
                        # count += 1
                        # employeesInfo(emp, count)
                        tempList.append(emp)
                #some kind of woodo magic
                lst = sorted(tempList, key=lambda x: x[0])
                print('Išfiltruoti duomenys pagal lytį ir surušiuota pagal vardą (A-Z)')
                printEmployees(lst)

        case 6:
                exit(1)
    printEmployees()

