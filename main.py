# Skyriaus darbuotojai


employees = [
    [
        'Lukas K.', 35, 3000
     ],
    [
        'Edita B.', 38, 1500
    ],
    [
        'Laura U.', 45, 2500
    ],
    [
        'Arina V.', 28, 2200
    ],
    [
        'Tautvydas V.', 30, 1800
    ]
]

def printInfo():
    print('Išsirinkite veiksmą, įrašydami jo eilės numerį:')
    print('1. Darbuotojų sąrašas')
    print('2. Įvesti naują darbuotoją')
    print('3. Redaguoti darbuotojo duomenis')
    print('4. Pašalinti darbuotoją iš sąrašo')
    print('5. Išeiti iš programos')
    print('------------------------------------------------------')

def employeesInfo(emp, num = 1):
    print(f'{num}. Darbuotojas {emp[0]}, amžius - {emp[1]} metai, DU - {emp[2]}')

def printEmployees():
    num = 1
    for emp in employees:
        employeesInfo(emp, num)
        num += 1

def addEmployees():
    print('Darbuotojo vardas ir pirmoji pavardės raidė')
    empName = input()
    print('Darbuotojo amžius')
    empAge = int( input() )
    print('Darbuotojo DU')
    empSalary = int( input() )
    employees.append([empName, empAge, empSalary])

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
    employees[ed - 1] = [empName, empAge, empSalary]

def removeEmployees():
    print('Įveskite darbuotojo eilės numerį, kurio informaciją norite pašalinti')
    rem = int( input() )
    employees.pop(rem - 1)

print('---Skyriaus darbuotojų valdymo sistema---')

# printEmployees()

while True:
    printInfo()
    option = int( input() )
    match option:
        case 1:
            printEmployees()
        case 2:
            addEmployees()
            printEmployees()
        case 3:
            editEmployees()
            printEmployees()
        case 4:
            removeEmployees()
            printEmployees()
        case 5:
                exit(1)
