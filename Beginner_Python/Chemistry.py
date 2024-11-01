import re
from sympy import Matrix, lcm 


def start():
    conversionsOrChemistry = int(input("Are you converting units or doing chem shit? 1 for units, 2 for chem: "))
    if conversionsOrChemistry == 1:
        conversions()
    elif conversionsOrChemistry == 2:
        chemistry()
    else:
        print("Chose 1 or 2 buddy")
        start()

def conversions():
    measurmentChoice = int(input("What are you converting? 1 for Length, 2 for Area, 3 for Volume, 4 for Mass, 5 for Density, 6 for Force, 7 for Pressure, 8 for Energy, 9 for Power, 10 for Temperature. "))
    if measurmentChoice == 1:
        convertLength()
    elif measurmentChoice == 2:
        convertArea()
    elif measurmentChoice == 3:
        convertVolume()
    elif measurmentChoice == 4:
        convertMass()
    elif measurmentChoice == 5:
        convertDensity()
    elif measurmentChoice == 6:
        convertForce()
    elif measurmentChoice == 7:
        convertPressure()
    elif measurmentChoice == 8:
        convertEnergy()
    elif measurmentChoice == 9:
        convertPower()
    elif measurmentChoice == 10:
        convertTemperature()
    else:
        print("Make sure to input a number between 1-10 please")
        conversions()

def convertLength():
    meters = float()
    centimeters = 0
    ansgstrom = 0
    inches = 0
    feet = 0
    miles = 0
    unitOfChoice = int(input("What unit are you inputting? 1 for centimeters, 2 for meters, 3 for Å(Angstrom), 4 for inches, 5 for feet, 6 for miles. "))
    magnitudeOfUnit = float(input("What is the magnitude? "))
    if unitOfChoice == 1:
        meters = (magnitudeOfUnit/100)
    elif unitOfChoice == 2:
        meters = magnitudeOfUnit
    elif unitOfChoice == 3:
        meters = (magnitudeOfUnit/(1*pow(10,10)))
    elif unitOfChoice == 4:
        meters = (magnitudeOfUnit/39.370)
    elif unitOfChoice == 5:
        meters = (magnitudeOfUnit/3.28084)
    elif unitOfChoice == 6:
        meters = (magnitudeOfUnit/(6.21371*pow(10,-4)))
    else:
        print("Please make sure you input one of the given units. 1-6")
        convertLength()
    centimeters = (meters*100)
    meters = meters
    ansgstrom = (meters*(1*pow(10,10)))
    inches = (meters * 39.370)
    feet = (meters * 3.28084)
    miles = (meters*(6.21371*pow(10,-4)))
    
    print(f"That would be: {centimeters} cm, {meters} m, {ansgstrom} Å, {inches} in, {feet} ft, {miles} mi.")
    gameOver()

def convertArea():
    meters = 0
    centimeters = 0
    inches = 0
    feet = 0
    acres = 0
    unitOfChoice = int(input("What unit are you inputting? 1 for centimeters squared, 2 for meter squared, 3 for inches squared, 4 for feet squared, 5 for acres. "))
    magnitudeOfUnit = float(input("What is the magnitude? "))
    if unitOfChoice == 1:
        meters = (magnitudeOfUnit/(pow(10,4)))
    elif unitOfChoice == 2:
        meters = magnitudeOfUnit
    elif unitOfChoice == 3:
        meters = (magnitudeOfUnit/1550.0031)
    elif unitOfChoice == 4:
        meters = (magnitudeOfUnit/10.7639)
    elif unitOfChoice == 5:
        meters = (magnitudeOfUnit/(2.47105*pow(10,-4)))
    else:
        print("Please make sure you input one of the given units. 1-5")
        convertArea()
    
    centimeters = meters * (pow(10,4))
    meters = meters
    inches = (meters * 1550.0031)
    feet = (meters * 10.7639)
    acres = (meters * (2.47105*pow(10,-4)))

    print(f"That would be: {centimeters} cm^2, {meters} m^2, {inches} in^2, {feet} ft^2, {acres} acre. ")
    gameOver()

def convertVolume():
    meters = 0
    liters = 0
    inches = 0
    gallons = 0
    imperialGallons = 0
    unitOfChoice = int(input("What unit are you inputting? 1 for meters cubed, 2 for liters, 3 for inches cubed, 4 for gallons, 5 for imperial gallons. "))
    magnitudeOfUnit = float(input("What is the magnitude? "))
    if unitOfChoice == 1:
        meters = magnitudeOfUnit
    elif unitOfChoice == 2:
        meters = (magnitudeOfUnit/1000)
    elif unitOfChoice == 3:
        meters = (magnitudeOfUnit/(6.10237*pow(10,4)))
    elif unitOfChoice == 4:
        meters = (magnitudeOfUnit/264.172)
    elif unitOfChoice == 5:
        meters = (magnitudeOfUnit/219.969)
    else:
        print("Please make sure you input one of the given units. 1-5")
        convertVolume()
    
    meters = meters
    liters = (meters * 1000)
    inches = (meters * (6.10237*pow(10,4)))
    gallons = (meters * 264.172)
    imperialGallons = (meters * 219.969)

    print(f"That would be: {meters} m^3, {liters} L, {inches} in^3, {gallons} gal(US), {imperialGallons} gal(Imp). ") 
    gameOver()

def convertMass():
    grams = 0
    kilograms = 0
    pounds = 0
    ounces = 0
    tonnes = 0
    unitOfChoice = int(input("What unit are you inputting? 1 for grams, 2 for killograms, 3 for pounds, 4 for ounces, 5 for metric tonnes. "))
    magnitudeOfUnit = float(input("What is the magnitude? "))
    if unitOfChoice == 1:
        kilograms = magnitudeOfUnit/1000
    elif unitOfChoice == 2:
        kilograms = magnitudeOfUnit
    elif unitOfChoice == 3:
        kilograms = magnitudeOfUnit/2.20462
    elif unitOfChoice == 4:
        kilograms = magnitudeOfUnit/35.274
    elif unitOfChoice == 5:
        kilograms = magnitudeOfUnit/(pow(10,-3))
    else:
        print("Please make sure you input one of the given units. 1-5")
        convertMass()
    
    grams = kilograms * 1000
    kilograms = kilograms
    pounds = kilograms * 2.20462
    ounces = kilograms * 35.274
    tonnes = kilograms * (pow(10,-3))

    print(f"That would be: {grams} g, {kilograms} kg, {pounds} lb, {ounces} oz, {tonnes} tonnes. ")  
    gameOver()

def convertDensity():
    grams = 0
    kilograms = 0
    gramsPerLiter = 0
    pounds = 0
    poundsPerGalon = 0
    unitOfChoice = int(input("What unit are you inputting? 1 for grams/centimeters^3, 2 for killograms/meters^3, 3 for grams/liter, 4 for pounds/feet^3, 5 for pounds/galon. "))
    magnitudeOfUnit = float(input("What is the magnitude? "))
    if unitOfChoice == 1:
        grams = magnitudeOfUnit
    elif unitOfChoice == 2:
        grams = magnitudeOfUnit/1000
    elif unitOfChoice == 3:
        grams = magnitudeOfUnit/1000
    elif unitOfChoice == 4:
        grams = magnitudeOfUnit/62.4280
    elif unitOfChoice == 5:
        grams = magnitudeOfUnit/8.34541
    else:
        print("Please make sure you input one of the given units. 1-5")
        convertDensity()
    
    grams = grams
    kilograms = grams*1000
    gramsPerLiter = grams * 1000
    pounds = grams * 62.4280
    poundsPerGalon = grams * 8.34531

    print(f"That would be: {grams} g/cm^3, {kilograms} kg/m^3, {gramsPerLiter} g/L, {pounds} lb/ft^3, {poundsPerGalon} lb/gal. ")   
    gameOver()

def convertForce():
    neutons = 0
    dyne = 0
    pounds = 0
    kilograms = 0
    poundsFeetPerSeconds = 0
    unitOfChoice = int(input("What unit are you inputting? 1 for neutons, 2 for dynes, 3 for pounds, 4 for killograms, 5 for pound-feet/s^2. "))
    magnitudeOfUnit = float(input("What is the magnitude? "))
    if unitOfChoice == 1:
        neutons = magnitudeOfUnit
    elif unitOfChoice == 2:
        neutons = magnitudeOfUnit/(pow(10,5))
    elif unitOfChoice == 3:
        neutons = magnitudeOfUnit/0.224809
    elif unitOfChoice == 4:
        neutons = magnitudeOfUnit/0.10197
    elif unitOfChoice == 5:
        neutons = magnitudeOfUnit/7.23301
    else:
        print("Please make sure you input one of the given units. 1-5")
        convertForce()
    
    neutons = neutons
    dyne = neutons*(pow(10,5))
    pounds = neutons * 0.224809
    kilograms = neutons * 0.10197
    poundsFeetPerSeconds = neutons * 7.23301

    print(f"That would be: {neutons} N, {dyne} dyne, {pounds} lb, {kilograms} kg, {poundsFeetPerSeconds} lb-ft/s^2. ")  
    gameOver() 

def convertPressure():
    atm = 0
    Pa = 0
    kPa = 0
    bar = 0
    psi = 0
    torr = 0
    unitOfChoice = int(input("What unit are you inputting? 1 for atm, 2 for Pa, 3 for kPa, 4 for bar, 5 for psi, 6 for mmHg. "))
    magnitudeOfUnit = float(input("What is the magnitude? "))
    if unitOfChoice == 1:
        atm = magnitudeOfUnit
    elif unitOfChoice == 2:
        atm = magnitudeOfUnit/101325
    elif unitOfChoice == 3:
        atm = magnitudeOfUnit/101.325
    elif unitOfChoice == 4:
        atm = magnitudeOfUnit/1.01325
    elif unitOfChoice == 5:
        atm = magnitudeOfUnit/14.6959
    elif unitOfChoice == 6:
        atm = magnitudeOfUnit/760
    else:
        print("Please make sure you input one of the given units. 1-6")
        convertPressure()
    
    atm = atm
    Pa = atm*101325
    kPa = atm*101.325
    bar = atm*1.01325
    psi = atm*14.6959
    torr = atm*760

    print(f"That would be: {atm} atm, {Pa} Pa, {kPa} kPa, {bar} bar, {psi} psi, {torr} mmHg. ")  
    gameOver()  

def convertEnergy():
    joules = 0
    btu = 0
    calories = 0
    feetPound = 0
    electronVolt = 0
    unitOfChoice = int(input("What unit are you inputting? 1 for joules, 2 for Btu, 3 for cal, 4 for foot-pound, 5 for electronVolt. "))
    magnitudeOfUnit = float(input("What is the magnitude? "))
    if unitOfChoice == 1:
        joules = magnitudeOfUnit
    elif unitOfChoice == 2:
        joules = magnitudeOfUnit/(9.4782*pow(10,-4))
    elif unitOfChoice == 3:
        joules = magnitudeOfUnit/0.239006
    elif unitOfChoice == 4:
        joules = magnitudeOfUnit/0.737562
    elif unitOfChoice == 5:
        joules = magnitudeOfUnit/(6.24145*pow(10,18))
    else:
        print("Please make sure you input one of the given units. 1-5")
        convertEnergy()
    
    joules = joules
    btu = joules*(9.4782*pow(10,-4))
    calories = joules*0.239006
    feetPound = joules*0.737562
    electronVolt = joules*(6.24145*pow(10,18))

    print(f"That would be: {joules} J, {btu} Btu, {calories} cal, {feetPound} ft-lb, {electronVolt} eV. ")  
    gameOver()  

def convertPower():
    watts = 0
    kilograms = 0 #kg*m^2/s^3
    btu = 0 #Btu/h
    horsepower = 0 
    erg = 0 #erg/s
    unitOfChoice = int(input("What unit are you inputting? 1 for Watts, 2 for Killograms-Meters Squared per Seconds cubed, 3 for Btu perh hour, 4 for horsepower, 5 for ergs per second. "))
    magnitudeOfUnit = float(input("What is the magnitude? "))
    if unitOfChoice == 1:
        watts = magnitudeOfUnit
    elif unitOfChoice == 2:
        watts = magnitudeOfUnit
    elif unitOfChoice == 3:
        watts = magnitudeOfUnit/3.4121
    elif unitOfChoice == 4:
        watts = magnitudeOfUnit/(1.34102*pow(10,-3))
    elif unitOfChoice == 5:
        watts = magnitudeOfUnit/(pow(10,17))
    else:
        print("Please make sure you input one of the given units. 1-5")
        convertPower()
    
    watts = watts
    kilograms = watts
    btu = watts*3.4121
    horsepower = watts*(1.34102*pow(10,-3))
    erg = watts*pow(10,17)

    print(f"That would be: {watts} W, {kilograms} kg*m^2/s^3, {btu} Btu/h, {horsepower} hp, {erg} erg/s. ")  
    gameOver()   

def convertTemperature():
    celsius = 0
    fahrenheit = 0 
    kelvin = 0 
    unitOfChoice = int(input("What unit are you inputting? 1 for Celsius, 2 for Fahrenheit, 3 for Kelvin. "))
    magnitudeOfUnit = float(input("What is the magnitude? "))
    if unitOfChoice == 1:
        celsius = magnitudeOfUnit
    elif unitOfChoice == 2:
        celsius = (magnitudeOfUnit-32)*(5/9)
    elif unitOfChoice == 3:
        celsius = magnitudeOfUnit-273.15
    else:
        print("Please make sure you input one of the given units. 1-3")
        convertTemperature()
    
    celsius = celsius
    fahrenheit = (celsius*(9/5)) + 32
    kelvin = celsius + 273.15

    print(f"That would be: {celsius} °C, {fahrenheit} °F, {kelvin} K.")  
    gameOver()   

def chemistry():
    x = int(input("Are you inputting an element or a compound or an reaction? 1 for element, 2 for compound, 3 for reaction: "))
    if x == 1:
        element()
    elif x ==2: 
        compound()
    elif x == 3:
        equations()
    else:
         print("Make sure to chose 1 or 2 or 3 next time")
         chemistry()

def element():
    elements = [
            {"Symbol": "H", "Name": "Hydrogen", "Atomic Number": 1, "Molar Mass": 1.008},
            {"Symbol": "He", "Name": "Helium", "Atomic Number": 2, "Molar Mass": 4.0026},
            {"Symbol": "Li", "Name": "Lithium", "Atomic Number": 3, "Molar Mass": 6.94},
            {"Symbol": "Be", "Name": "Beryllium", "Atomic Number": 4, "Molar Mass": 9.0122},
            {"Symbol": "B", "Name": "Boron", "Atomic Number": 5, "Molar Mass": 10.81},
            {"Symbol": "C", "Name": "Carbon", "Atomic Number": 6, "Molar Mass": 12.011},
            {"Symbol": "N", "Name": "Nitrogen", "Atomic Number": 7, "Molar Mass": 14.007},
            {"Symbol": "O", "Name": "Oxygen", "Atomic Number": 8, "Molar Mass": 15.999},
            {"Symbol": "F", "Name": "Fluorine", "Atomic Number": 9, "Molar Mass": 18.998},
            {"Symbol": "Ne", "Name": "Neon", "Atomic Number": 10, "Molar Mass": 20.180},
            {"Symbol": "Na", "Name": "Sodium", "Atomic Number": 11, "Molar Mass": 22.990},
            {"Symbol": "Mg", "Name": "Magnesium", "Atomic Number": 12, "Molar Mass": 24.305},
            {"Symbol": "Al", "Name": "Aluminum", "Atomic Number": 13, "Molar Mass": 26.982},
            {"Symbol": "Si", "Name": "Silicon", "Atomic Number": 14, "Molar Mass": 28.085},
            {"Symbol": "P", "Name": "Phosphorus", "Atomic Number": 15, "Molar Mass": 30.974},
            {"Symbol": "S", "Name": "Sulfur", "Atomic Number": 16, "Molar Mass": 32.06},
            {"Symbol": "Cl", "Name": "Chlorine", "Atomic Number": 17, "Molar Mass": 35.45},
            {"Symbol": "Ar", "Name": "Argon", "Atomic Number": 18, "Molar Mass": 39.948},
            {"Symbol": "K", "Name": "Potassium", "Atomic Number": 19, "Molar Mass": 39.098},
            {"Symbol": "Ca", "Name": "Calcium", "Atomic Number": 20, "Molar Mass": 40.078},
            {"Symbol": "Sc", "Name": "Scandium", "Atomic Number": 21, "Molar Mass": 44.956},
            {"Symbol": "Ti", "Name": "Titanium", "Atomic Number": 22, "Molar Mass": 47.867},
            {"Symbol": "V", "Name": "Vanadium", "Atomic Number": 23, "Molar Mass": 50.942},
            {"Symbol": "Cr", "Name": "Chromium", "Atomic Number": 24, "Molar Mass": 51.996},
            {"Symbol": "Mn", "Name": "Manganese", "Atomic Number": 25, "Molar Mass": 54.938},
            {"Symbol": "Fe", "Name": "Iron", "Atomic Number": 26, "Molar Mass": 55.845},
            {"Symbol": "Co", "Name": "Cobalt", "Atomic Number": 27, "Molar Mass": 58.933},
            {"Symbol": "Ni", "Name": "Nickel", "Atomic Number": 28, "Molar Mass": 58.693},
            {"Symbol": "Cu", "Name": "Copper", "Atomic Number": 29, "Molar Mass": 63.546},
            {"Symbol": "Zn", "Name": "Zinc", "Atomic Number": 30, "Molar Mass": 65.38},
            {"Symbol": "Ga", "Name": "Gallium", "Atomic Number": 31, "Molar Mass": 69.723},
            {"Symbol": "Ge", "Name": "Germanium", "Atomic Number": 32, "Molar Mass": 72.630},
            {"Symbol": "As", "Name": "Arsenic", "Atomic Number": 33, "Molar Mass": 74.922},
            {"Symbol": "Se", "Name": "Selenium", "Atomic Number": 34, "Molar Mass": 78.971},
            {"Symbol": "Br", "Name": "Bromine", "Atomic Number": 35, "Molar Mass": 79.904},
            {"Symbol": "Kr", "Name": "Krypton", "Atomic Number": 36, "Molar Mass": 83.798},
            {"Symbol": "Rb", "Name": "Rubidium", "Atomic Number": 37, "Molar Mass": 85.468},
            {"Symbol": "Sr", "Name": "Strontium", "Atomic Number": 38, "Molar Mass": 87.62},
            {"Symbol": "Y", "Name": "Yttrium", "Atomic Number": 39, "Molar Mass": 88.906},
            {"Symbol": "Zr", "Name": "Zirconium", "Atomic Number": 40, "Molar Mass": 91.224},
            {"Symbol": "Nb", "Name": "Niobium", "Atomic Number": 41, "Molar Mass": 92.906},
            {"Symbol": "Mo", "Name": "Molybdenum", "Atomic Number": 42, "Molar Mass": 95.95},
            {"Symbol": "Tc", "Name": "Technetium", "Atomic Number": 43, "Molar Mass": 98},
            {"Symbol": "Ru", "Name": "Ruthenium", "Atomic Number": 44, "Molar Mass": 101.07},
            {"Symbol": "Rh", "Name": "Rhodium", "Atomic Number": 45, "Molar Mass": 102.91},
            {"Symbol": "Pd", "Name": "Palladium", "Atomic Number": 46, "Molar Mass": 106.42},
            {"Symbol": "Ag", "Name": "Silver", "Atomic Number": 47, "Molar Mass": 107.87},
            {"Symbol": "Cd", "Name": "Cadmium", "Atomic Number": 48, "Molar Mass": 112.41},
            {"Symbol": "In", "Name": "Indium", "Atomic Number": 49, "Molar Mass": 114.82},
            {"Symbol": "Sn", "Name": "Tin", "Atomic Number": 50, "Molar Mass": 118.71},
            {"Symbol": "Sb", "Name": "Antimony", "Atomic Number": 51, "Molar Mass": 121.76},
            {"Symbol": "Te", "Name": "Tellurium", "Atomic Number": 52, "Molar Mass": 127.60},
            {"Symbol": "I", "Name": "Iodine", "Atomic Number": 53, "Molar Mass": 126.90},
            {"Symbol": "Xe", "Name": "Xenon", "Atomic Number": 54, "Molar Mass": 131.29},
            {"Symbol": "Cs", "Name": "Cesium", "Atomic Number": 55, "Molar Mass": 132.91},
            {"Symbol": "Ba", "Name": "Barium", "Atomic Number": 56, "Molar Mass": 137.33},
            {"Symbol": "La", "Name": "Lanthanum", "Atomic Number": 57, "Molar Mass": 138.91},
            {"Symbol": "Ce", "Name": "Cerium", "Atomic Number": 58, "Molar Mass": 140.12},
            {"Symbol": "Pr", "Name": "Praseodymium", "Atomic Number": 59, "Molar Mass": 140.91},
            {"Symbol": "Nd", "Name": "Neodymium", "Atomic Number": 60, "Molar Mass": 144.24},
            {"Symbol": "Pm", "Name": "Promethium", "Atomic Number": 61, "Molar Mass": 145},
            {"Symbol": "Sm", "Name": "Samarium", "Atomic Number": 62, "Molar Mass": 150.36},
            {"Symbol": "Eu", "Name": "Europium", "Atomic Number": 63, "Molar Mass": 151.96},
            {"Symbol": "Gd", "Name": "Gadolinium", "Atomic Number": 64, "Molar Mass": 157.25},
            {"Symbol": "Tb", "Name": "Terbium", "Atomic Number": 65, "Molar Mass": 158.93},
            {"Symbol": "Dy", "Name": "Dysprosium", "Atomic Number": 66, "Molar Mass": 162.50},
            {"Symbol": "Ho", "Name": "Holmium", "Atomic Number": 67, "Molar Mass": 164.93},
            {"Symbol": "Er", "Name": "Erbium", "Atomic Number": 68, "Molar Mass": 167.26},
            {"Symbol": "Tm", "Name": "Thulium", "Atomic Number": 69, "Molar Mass": 168.93},
            {"Symbol": "Yb", "Name": "Ytterbium", "Atomic Number": 70, "Molar Mass": 173.04},
            {"Symbol": "Lu", "Name": "Lutetium", "Atomic Number": 71, "Molar Mass": 174.97},
            {"Symbol": "Hf", "Name": "Hafnium", "Atomic Number": 72, "Molar Mass": 178.49},
            {"Symbol": "Ta", "Name": "Tantalum", "Atomic Number": 73, "Molar Mass": 180.95},
            {"Symbol": "W", "Name": "Tungsten", "Atomic Number": 74, "Molar Mass": 183.84},
            {"Symbol": "Re", "Name": "Rhenium", "Atomic Number": 75, "Molar Mass": 186.21},
            {"Symbol": "Os", "Name": "Osmium", "Atomic Number": 76, "Molar Mass": 190.23},
            {"Symbol": "Ir", "Name": "Iridium", "Atomic Number": 77, "Molar Mass": 192.22},
            {"Symbol": "Pt", "Name": "Platinum", "Atomic Number": 78, "Molar Mass": 195.08},
            {"Symbol": "Au", "Name": "Gold", "Atomic Number": 79, "Molar Mass": 196.97},
            {"Symbol": "Hg", "Name": "Mercury", "Atomic Number": 80, "Molar Mass": 200.59},
            {"Symbol": "Tl", "Name": "Thallium", "Atomic Number": 81, "Molar Mass": 204.38},
            {"Symbol": "Pb", "Name": "Lead", "Atomic Number": 82, "Molar Mass": 207.2},
            {"Symbol": "Bi", "Name": "Bismuth", "Atomic Number": 83, "Molar Mass": 208.98},
            {"Symbol": "Po", "Name": "Polonium", "Atomic Number": 84, "Molar Mass": 209},
            {"Symbol": "At", "Name": "Astatine", "Atomic Number": 85, "Molar Mass": 210},
            {"Symbol": "Rn", "Name": "Radon", "Atomic Number": 86, "Molar Mass": 222},
            {"Symbol": "Fr", "Name": "Francium", "Atomic Number": 87, "Molar Mass": 223},
            {"Symbol": "Ra", "Name": "Radium", "Atomic Number": 88, "Molar Mass": 226},
            {"Symbol": "Ac", "Name": "Actinium", "Atomic Number": 89, "Molar Mass": 227},
            {"Symbol": "Th", "Name": "Thorium", "Atomic Number": 90, "Molar Mass": 232.04},
            {"Symbol": "Pa", "Name": "Protactinium", "Atomic Number": 91, "Molar Mass": 231.04},
            {"Symbol": "U", "Name": "Uranium", "Atomic Number": 92, "Molar Mass": 238.03},
            {"Symbol": "Np", "Name": "Neptunium", "Atomic Number": 93, "Molar Mass": 237},
            {"Symbol": "Pu", "Name": "Plutonium", "Atomic Number": 94, "Molar Mass": 244},
            {"Symbol": "Am", "Name": "Americium", "Atomic Number": 95, "Molar Mass": 243},
            {"Symbol": "Cm", "Name": "Curium", "Atomic Number": 96, "Molar Mass": 247},
            {"Symbol": "Bk", "Name": "Berkelium", "Atomic Number": 97, "Molar Mass": 247},
            {"Symbol": "Cf", "Name": "Californium", "Atomic Number": 98, "Molar Mass": 251},
            {"Symbol": "Es", "Name": "Einsteinium", "Atomic Number": 99, "Molar Mass": 252},
            {"Symbol": "Fm", "Name": "Fermium", "Atomic Number": 100, "Molar Mass": 257},
            {"Symbol": "Md", "Name": "Mendelevium", "Atomic Number": 101, "Molar Mass": 258},
            {"Symbol": "No", "Name": "Nobelium", "Atomic Number": 102, "Molar Mass": 259},
            {"Symbol": "Lr", "Name": "Lawrencium", "Atomic Number": 103, "Molar Mass": 262},
            {"Symbol": "Rf", "Name": "Rutherfordium", "Atomic Number": 104, "Molar Mass": 267},
            {"Symbol": "Db", "Name": "Dubnium", "Atomic Number": 105, "Molar Mass": 270},
            {"Symbol": "Sg", "Name": "Seaborgium", "Atomic Number": 106, "Molar Mass": 271},
            {"Symbol": "Bh", "Name": "Bohrium", "Atomic Number": 107, "Molar Mass": 270},
            {"Symbol": "Hs", "Name": "Hassium", "Atomic Number": 108, "Molar Mass": 277},
            {"Symbol": "Mt", "Name": "Meitnerium", "Atomic Number": 109, "Molar Mass": 282},
            {"Symbol": "Ds", "Name": "Darmstadtium", "Atomic Number": 110, "Molar Mass": 285},
            {"Symbol": "Rg", "Name": "Roentgenium", "Atomic Number": 111, "Molar Mass": 286},
            {"Symbol": "Cn", "Name": "Copernicium", "Atomic Number": 112, "Molar Mass": 289},
            {"Symbol": "Nh", "Name": "Nihonium", "Atomic Number": 113, "Molar Mass": 290},
            {"Symbol": "Fl", "Name": "Flerovium", "Atomic Number": 114, "Molar Mass": 293},
            {"Symbol": "Mc", "Name": "Moscovium", "Atomic Number": 115, "Molar Mass": 294},
            {"Symbol": "Lv", "Name": "Livermorium", "Atomic Number": 116, "Molar Mass": 293},
            {"Symbol": "Ts", "Name": "Tennessine", "Atomic Number": 117, "Molar Mass": 294},
            {"Symbol": "Og", "Name": "Oganesson", "Atomic Number": 118, "Molar Mass": 294}
        ]
    element = input("Whats the name, atomic symbol, or the atomic number of the element you have? ")
    mass = 0
    moles = 0
    molarMass = 0

    for i in elements:
            if i['Symbol'].lower() == element.lower() or i['Name'].lower() == element.lower() or str(i['Atomic Number']) == element:
                molarMass = i['Molar Mass']
                print(i)
                x = int(input("Do you have mass or moles? 1 for mass, 2 for moles: "))
                if x == 1:
                    mass = float(input(f"How many grams of {i['Name']} do you have? "))
                    moles = mass/molarMass
                elif x == 2:
                    moles = float(input(f"How many moles of {i['Name']} do you have? "))
                    mass = moles*molarMass
                else:
                    print("Make sure you chose 1 or 2 next time. ")
                    chemistry()

                print(f"{mass} grams of {i['Name']} is {moles} moles. ")
                gameOver()
    print("Make sure its a real element!")
    chemistry()

def compound():
    elements = [
            {"Symbol": "H", "Name": "Hydrogen", "Atomic Number": 1, "Molar Mass": 1.008},
            {"Symbol": "He", "Name": "Helium", "Atomic Number": 2, "Molar Mass": 4.0026},
            {"Symbol": "Li", "Name": "Lithium", "Atomic Number": 3, "Molar Mass": 6.94},
            {"Symbol": "Be", "Name": "Beryllium", "Atomic Number": 4, "Molar Mass": 9.0122},
            {"Symbol": "B", "Name": "Boron", "Atomic Number": 5, "Molar Mass": 10.81},
            {"Symbol": "C", "Name": "Carbon", "Atomic Number": 6, "Molar Mass": 12.011},
            {"Symbol": "N", "Name": "Nitrogen", "Atomic Number": 7, "Molar Mass": 14.007},
            {"Symbol": "O", "Name": "Oxygen", "Atomic Number": 8, "Molar Mass": 15.999},
            {"Symbol": "F", "Name": "Fluorine", "Atomic Number": 9, "Molar Mass": 18.998},
            {"Symbol": "Ne", "Name": "Neon", "Atomic Number": 10, "Molar Mass": 20.180},
            {"Symbol": "Na", "Name": "Sodium", "Atomic Number": 11, "Molar Mass": 22.990},
            {"Symbol": "Mg", "Name": "Magnesium", "Atomic Number": 12, "Molar Mass": 24.305},
            {"Symbol": "Al", "Name": "Aluminum", "Atomic Number": 13, "Molar Mass": 26.982},
            {"Symbol": "Si", "Name": "Silicon", "Atomic Number": 14, "Molar Mass": 28.085},
            {"Symbol": "P", "Name": "Phosphorus", "Atomic Number": 15, "Molar Mass": 30.974},
            {"Symbol": "S", "Name": "Sulfur", "Atomic Number": 16, "Molar Mass": 32.06},
            {"Symbol": "Cl", "Name": "Chlorine", "Atomic Number": 17, "Molar Mass": 35.45},
            {"Symbol": "Ar", "Name": "Argon", "Atomic Number": 18, "Molar Mass": 39.948},
            {"Symbol": "K", "Name": "Potassium", "Atomic Number": 19, "Molar Mass": 39.098},
            {"Symbol": "Ca", "Name": "Calcium", "Atomic Number": 20, "Molar Mass": 40.078},
            {"Symbol": "Sc", "Name": "Scandium", "Atomic Number": 21, "Molar Mass": 44.956},
            {"Symbol": "Ti", "Name": "Titanium", "Atomic Number": 22, "Molar Mass": 47.867},
            {"Symbol": "V", "Name": "Vanadium", "Atomic Number": 23, "Molar Mass": 50.942},
            {"Symbol": "Cr", "Name": "Chromium", "Atomic Number": 24, "Molar Mass": 51.996},
            {"Symbol": "Mn", "Name": "Manganese", "Atomic Number": 25, "Molar Mass": 54.938},
            {"Symbol": "Fe", "Name": "Iron", "Atomic Number": 26, "Molar Mass": 55.845},
            {"Symbol": "Co", "Name": "Cobalt", "Atomic Number": 27, "Molar Mass": 58.933},
            {"Symbol": "Ni", "Name": "Nickel", "Atomic Number": 28, "Molar Mass": 58.693},
            {"Symbol": "Cu", "Name": "Copper", "Atomic Number": 29, "Molar Mass": 63.546},
            {"Symbol": "Zn", "Name": "Zinc", "Atomic Number": 30, "Molar Mass": 65.38},
            {"Symbol": "Ga", "Name": "Gallium", "Atomic Number": 31, "Molar Mass": 69.723},
            {"Symbol": "Ge", "Name": "Germanium", "Atomic Number": 32, "Molar Mass": 72.630},
            {"Symbol": "As", "Name": "Arsenic", "Atomic Number": 33, "Molar Mass": 74.922},
            {"Symbol": "Se", "Name": "Selenium", "Atomic Number": 34, "Molar Mass": 78.971},
            {"Symbol": "Br", "Name": "Bromine", "Atomic Number": 35, "Molar Mass": 79.904},
            {"Symbol": "Kr", "Name": "Krypton", "Atomic Number": 36, "Molar Mass": 83.798},
            {"Symbol": "Rb", "Name": "Rubidium", "Atomic Number": 37, "Molar Mass": 85.468},
            {"Symbol": "Sr", "Name": "Strontium", "Atomic Number": 38, "Molar Mass": 87.62},
            {"Symbol": "Y", "Name": "Yttrium", "Atomic Number": 39, "Molar Mass": 88.906},
            {"Symbol": "Zr", "Name": "Zirconium", "Atomic Number": 40, "Molar Mass": 91.224},
            {"Symbol": "Nb", "Name": "Niobium", "Atomic Number": 41, "Molar Mass": 92.906},
            {"Symbol": "Mo", "Name": "Molybdenum", "Atomic Number": 42, "Molar Mass": 95.95},
            {"Symbol": "Tc", "Name": "Technetium", "Atomic Number": 43, "Molar Mass": 98},
            {"Symbol": "Ru", "Name": "Ruthenium", "Atomic Number": 44, "Molar Mass": 101.07},
            {"Symbol": "Rh", "Name": "Rhodium", "Atomic Number": 45, "Molar Mass": 102.91},
            {"Symbol": "Pd", "Name": "Palladium", "Atomic Number": 46, "Molar Mass": 106.42},
            {"Symbol": "Ag", "Name": "Silver", "Atomic Number": 47, "Molar Mass": 107.87},
            {"Symbol": "Cd", "Name": "Cadmium", "Atomic Number": 48, "Molar Mass": 112.41},
            {"Symbol": "In", "Name": "Indium", "Atomic Number": 49, "Molar Mass": 114.82},
            {"Symbol": "Sn", "Name": "Tin", "Atomic Number": 50, "Molar Mass": 118.71},
            {"Symbol": "Sb", "Name": "Antimony", "Atomic Number": 51, "Molar Mass": 121.76},
            {"Symbol": "Te", "Name": "Tellurium", "Atomic Number": 52, "Molar Mass": 127.60},
            {"Symbol": "I", "Name": "Iodine", "Atomic Number": 53, "Molar Mass": 126.90},
            {"Symbol": "Xe", "Name": "Xenon", "Atomic Number": 54, "Molar Mass": 131.29},
            {"Symbol": "Cs", "Name": "Cesium", "Atomic Number": 55, "Molar Mass": 132.91},
            {"Symbol": "Ba", "Name": "Barium", "Atomic Number": 56, "Molar Mass": 137.33},
            {"Symbol": "La", "Name": "Lanthanum", "Atomic Number": 57, "Molar Mass": 138.91},
            {"Symbol": "Ce", "Name": "Cerium", "Atomic Number": 58, "Molar Mass": 140.12},
            {"Symbol": "Pr", "Name": "Praseodymium", "Atomic Number": 59, "Molar Mass": 140.91},
            {"Symbol": "Nd", "Name": "Neodymium", "Atomic Number": 60, "Molar Mass": 144.24},
            {"Symbol": "Pm", "Name": "Promethium", "Atomic Number": 61, "Molar Mass": 145},
            {"Symbol": "Sm", "Name": "Samarium", "Atomic Number": 62, "Molar Mass": 150.36},
            {"Symbol": "Eu", "Name": "Europium", "Atomic Number": 63, "Molar Mass": 151.96},
            {"Symbol": "Gd", "Name": "Gadolinium", "Atomic Number": 64, "Molar Mass": 157.25},
            {"Symbol": "Tb", "Name": "Terbium", "Atomic Number": 65, "Molar Mass": 158.93},
            {"Symbol": "Dy", "Name": "Dysprosium", "Atomic Number": 66, "Molar Mass": 162.50},
            {"Symbol": "Ho", "Name": "Holmium", "Atomic Number": 67, "Molar Mass": 164.93},
            {"Symbol": "Er", "Name": "Erbium", "Atomic Number": 68, "Molar Mass": 167.26},
            {"Symbol": "Tm", "Name": "Thulium", "Atomic Number": 69, "Molar Mass": 168.93},
            {"Symbol": "Yb", "Name": "Ytterbium", "Atomic Number": 70, "Molar Mass": 173.04},
            {"Symbol": "Lu", "Name": "Lutetium", "Atomic Number": 71, "Molar Mass": 174.97},
            {"Symbol": "Hf", "Name": "Hafnium", "Atomic Number": 72, "Molar Mass": 178.49},
            {"Symbol": "Ta", "Name": "Tantalum", "Atomic Number": 73, "Molar Mass": 180.95},
            {"Symbol": "W", "Name": "Tungsten", "Atomic Number": 74, "Molar Mass": 183.84},
            {"Symbol": "Re", "Name": "Rhenium", "Atomic Number": 75, "Molar Mass": 186.21},
            {"Symbol": "Os", "Name": "Osmium", "Atomic Number": 76, "Molar Mass": 190.23},
            {"Symbol": "Ir", "Name": "Iridium", "Atomic Number": 77, "Molar Mass": 192.22},
            {"Symbol": "Pt", "Name": "Platinum", "Atomic Number": 78, "Molar Mass": 195.08},
            {"Symbol": "Au", "Name": "Gold", "Atomic Number": 79, "Molar Mass": 196.97},
            {"Symbol": "Hg", "Name": "Mercury", "Atomic Number": 80, "Molar Mass": 200.59},
            {"Symbol": "Tl", "Name": "Thallium", "Atomic Number": 81, "Molar Mass": 204.38},
            {"Symbol": "Pb", "Name": "Lead", "Atomic Number": 82, "Molar Mass": 207.2},
            {"Symbol": "Bi", "Name": "Bismuth", "Atomic Number": 83, "Molar Mass": 208.98},
            {"Symbol": "Po", "Name": "Polonium", "Atomic Number": 84, "Molar Mass": 209},
            {"Symbol": "At", "Name": "Astatine", "Atomic Number": 85, "Molar Mass": 210},
            {"Symbol": "Rn", "Name": "Radon", "Atomic Number": 86, "Molar Mass": 222},
            {"Symbol": "Fr", "Name": "Francium", "Atomic Number": 87, "Molar Mass": 223},
            {"Symbol": "Ra", "Name": "Radium", "Atomic Number": 88, "Molar Mass": 226},
            {"Symbol": "Ac", "Name": "Actinium", "Atomic Number": 89, "Molar Mass": 227},
            {"Symbol": "Th", "Name": "Thorium", "Atomic Number": 90, "Molar Mass": 232.04},
            {"Symbol": "Pa", "Name": "Protactinium", "Atomic Number": 91, "Molar Mass": 231.04},
            {"Symbol": "U", "Name": "Uranium", "Atomic Number": 92, "Molar Mass": 238.03},
            {"Symbol": "Np", "Name": "Neptunium", "Atomic Number": 93, "Molar Mass": 237},
            {"Symbol": "Pu", "Name": "Plutonium", "Atomic Number": 94, "Molar Mass": 244},
            {"Symbol": "Am", "Name": "Americium", "Atomic Number": 95, "Molar Mass": 243},
            {"Symbol": "Cm", "Name": "Curium", "Atomic Number": 96, "Molar Mass": 247},
            {"Symbol": "Bk", "Name": "Berkelium", "Atomic Number": 97, "Molar Mass": 247},
            {"Symbol": "Cf", "Name": "Californium", "Atomic Number": 98, "Molar Mass": 251},
            {"Symbol": "Es", "Name": "Einsteinium", "Atomic Number": 99, "Molar Mass": 252},
            {"Symbol": "Fm", "Name": "Fermium", "Atomic Number": 100, "Molar Mass": 257},
            {"Symbol": "Md", "Name": "Mendelevium", "Atomic Number": 101, "Molar Mass": 258},
            {"Symbol": "No", "Name": "Nobelium", "Atomic Number": 102, "Molar Mass": 259},
            {"Symbol": "Lr", "Name": "Lawrencium", "Atomic Number": 103, "Molar Mass": 262},
            {"Symbol": "Rf", "Name": "Rutherfordium", "Atomic Number": 104, "Molar Mass": 267},
            {"Symbol": "Db", "Name": "Dubnium", "Atomic Number": 105, "Molar Mass": 270},
            {"Symbol": "Sg", "Name": "Seaborgium", "Atomic Number": 106, "Molar Mass": 271},
            {"Symbol": "Bh", "Name": "Bohrium", "Atomic Number": 107, "Molar Mass": 270},
            {"Symbol": "Hs", "Name": "Hassium", "Atomic Number": 108, "Molar Mass": 277},
            {"Symbol": "Mt", "Name": "Meitnerium", "Atomic Number": 109, "Molar Mass": 282},
            {"Symbol": "Ds", "Name": "Darmstadtium", "Atomic Number": 110, "Molar Mass": 285},
            {"Symbol": "Rg", "Name": "Roentgenium", "Atomic Number": 111, "Molar Mass": 286},
            {"Symbol": "Cn", "Name": "Copernicium", "Atomic Number": 112, "Molar Mass": 289},
            {"Symbol": "Nh", "Name": "Nihonium", "Atomic Number": 113, "Molar Mass": 290},
            {"Symbol": "Fl", "Name": "Flerovium", "Atomic Number": 114, "Molar Mass": 293},
            {"Symbol": "Mc", "Name": "Moscovium", "Atomic Number": 115, "Molar Mass": 294},
            {"Symbol": "Lv", "Name": "Livermorium", "Atomic Number": 116, "Molar Mass": 293},
            {"Symbol": "Ts", "Name": "Tennessine", "Atomic Number": 117, "Molar Mass": 294},
            {"Symbol": "Og", "Name": "Oganesson", "Atomic Number": 118, "Molar Mass": 294}
        ]
    compound = input("Whats the compound? For example: (C2H4 or NaCl): ")
    brokenUpCompound = re.findall(r'([A-Z][a-z]*)(\d*)',compound) #re or regex findall patterns that follow [A-Z] CapitalLetter then it will match it with 0 or more lower case letters [a-z]* then it matches it with 0 or more number \d*. By putting (\d*) in its own paranthesis it tells python to save it as a seperate entity or ground. so instead of [('H2'), ('C2')] you get [('H', '2'), ('C', '2')

    #This results in brokenUpComound being a list of tuples that contain 2 parts. 1st part is the element 2nd part is the amount of.
    brokenUpCompoundTwo = [] #Making a new list to include the new tuples after u switch the 0's with 1's
    
    for element, count in brokenUpCompound: #splits the brokenUpCompound which is a tuple. first half is the element sign, 2nd half is the number of.
        count = int(count) if count else 1 #makes the number of into an integer if a number is present. if its not. it turns into into one
        brokenUpCompoundTwo.append((element,count)) #adds them back together

    molarMass = 0
    mass = 0
    moles = 0
    numberOfElements = 0
    for i in brokenUpCompoundTwo:
        for t in elements:
            if i[0] == t['Symbol']: # with tuples u specify the number of the group starting at zero rather than the name
                molarMass += t['Molar Mass'] * i[1]
                numberOfElements += 1
    if  numberOfElements >= len(brokenUpCompoundTwo): #If the numberOfElements is bigger or equal to the number of tuples or elements inside the list. This makes it that if there is a tuple that contains a fake element the numberOfElements would be smaller than the number of elements inside the list and the code would stop.
        print(f"The Molar Mass of {compound} is {molarMass} g/mol")
        x = int(input("Are you looking for number of Moles or Mass? 1 for moles, 2 for mass: "))
        if x == 1:
            moles = float(input(f"How many moles of {compound} do you have? "))
            mass = moles * molarMass
        elif x == 2:
            mass = float(input(f"How many grams of {compound} do you have? "))
            moles = mass/molarMass
        else:
            print("Make sure you put a number between 1 or 2 next time")
            compound()
        print(f"{mass} grams of {compound} is {moles} moles.")
        gameOver()

    else:
        print("Make sure you are putting in the compound correctly and that the elements exist. Its case sensitive so He is not HE or he")
        chemistry()

def equations():
    elements = [
            {"Symbol": "H", "Name": "Hydrogen", "Atomic Number": 1, "Molar Mass": 1.008},
            {"Symbol": "He", "Name": "Helium", "Atomic Number": 2, "Molar Mass": 4.0026},
            {"Symbol": "Li", "Name": "Lithium", "Atomic Number": 3, "Molar Mass": 6.94},
            {"Symbol": "Be", "Name": "Beryllium", "Atomic Number": 4, "Molar Mass": 9.0122},
            {"Symbol": "B", "Name": "Boron", "Atomic Number": 5, "Molar Mass": 10.81},
            {"Symbol": "C", "Name": "Carbon", "Atomic Number": 6, "Molar Mass": 12.011},
            {"Symbol": "N", "Name": "Nitrogen", "Atomic Number": 7, "Molar Mass": 14.007},
            {"Symbol": "O", "Name": "Oxygen", "Atomic Number": 8, "Molar Mass": 15.999},
            {"Symbol": "F", "Name": "Fluorine", "Atomic Number": 9, "Molar Mass": 18.998},
            {"Symbol": "Ne", "Name": "Neon", "Atomic Number": 10, "Molar Mass": 20.180},
            {"Symbol": "Na", "Name": "Sodium", "Atomic Number": 11, "Molar Mass": 22.990},
            {"Symbol": "Mg", "Name": "Magnesium", "Atomic Number": 12, "Molar Mass": 24.305},
            {"Symbol": "Al", "Name": "Aluminum", "Atomic Number": 13, "Molar Mass": 26.982},
            {"Symbol": "Si", "Name": "Silicon", "Atomic Number": 14, "Molar Mass": 28.085},
            {"Symbol": "P", "Name": "Phosphorus", "Atomic Number": 15, "Molar Mass": 30.974},
            {"Symbol": "S", "Name": "Sulfur", "Atomic Number": 16, "Molar Mass": 32.06},
            {"Symbol": "Cl", "Name": "Chlorine", "Atomic Number": 17, "Molar Mass": 35.45},
            {"Symbol": "Ar", "Name": "Argon", "Atomic Number": 18, "Molar Mass": 39.948},
            {"Symbol": "K", "Name": "Potassium", "Atomic Number": 19, "Molar Mass": 39.098},
            {"Symbol": "Ca", "Name": "Calcium", "Atomic Number": 20, "Molar Mass": 40.078},
            {"Symbol": "Sc", "Name": "Scandium", "Atomic Number": 21, "Molar Mass": 44.956},
            {"Symbol": "Ti", "Name": "Titanium", "Atomic Number": 22, "Molar Mass": 47.867},
            {"Symbol": "V", "Name": "Vanadium", "Atomic Number": 23, "Molar Mass": 50.942},
            {"Symbol": "Cr", "Name": "Chromium", "Atomic Number": 24, "Molar Mass": 51.996},
            {"Symbol": "Mn", "Name": "Manganese", "Atomic Number": 25, "Molar Mass": 54.938},
            {"Symbol": "Fe", "Name": "Iron", "Atomic Number": 26, "Molar Mass": 55.845},
            {"Symbol": "Co", "Name": "Cobalt", "Atomic Number": 27, "Molar Mass": 58.933},
            {"Symbol": "Ni", "Name": "Nickel", "Atomic Number": 28, "Molar Mass": 58.693},
            {"Symbol": "Cu", "Name": "Copper", "Atomic Number": 29, "Molar Mass": 63.546},
            {"Symbol": "Zn", "Name": "Zinc", "Atomic Number": 30, "Molar Mass": 65.38},
            {"Symbol": "Ga", "Name": "Gallium", "Atomic Number": 31, "Molar Mass": 69.723},
            {"Symbol": "Ge", "Name": "Germanium", "Atomic Number": 32, "Molar Mass": 72.630},
            {"Symbol": "As", "Name": "Arsenic", "Atomic Number": 33, "Molar Mass": 74.922},
            {"Symbol": "Se", "Name": "Selenium", "Atomic Number": 34, "Molar Mass": 78.971},
            {"Symbol": "Br", "Name": "Bromine", "Atomic Number": 35, "Molar Mass": 79.904},
            {"Symbol": "Kr", "Name": "Krypton", "Atomic Number": 36, "Molar Mass": 83.798},
            {"Symbol": "Rb", "Name": "Rubidium", "Atomic Number": 37, "Molar Mass": 85.468},
            {"Symbol": "Sr", "Name": "Strontium", "Atomic Number": 38, "Molar Mass": 87.62},
            {"Symbol": "Y", "Name": "Yttrium", "Atomic Number": 39, "Molar Mass": 88.906},
            {"Symbol": "Zr", "Name": "Zirconium", "Atomic Number": 40, "Molar Mass": 91.224},
            {"Symbol": "Nb", "Name": "Niobium", "Atomic Number": 41, "Molar Mass": 92.906},
            {"Symbol": "Mo", "Name": "Molybdenum", "Atomic Number": 42, "Molar Mass": 95.95},
            {"Symbol": "Tc", "Name": "Technetium", "Atomic Number": 43, "Molar Mass": 98},
            {"Symbol": "Ru", "Name": "Ruthenium", "Atomic Number": 44, "Molar Mass": 101.07},
            {"Symbol": "Rh", "Name": "Rhodium", "Atomic Number": 45, "Molar Mass": 102.91},
            {"Symbol": "Pd", "Name": "Palladium", "Atomic Number": 46, "Molar Mass": 106.42},
            {"Symbol": "Ag", "Name": "Silver", "Atomic Number": 47, "Molar Mass": 107.87},
            {"Symbol": "Cd", "Name": "Cadmium", "Atomic Number": 48, "Molar Mass": 112.41},
            {"Symbol": "In", "Name": "Indium", "Atomic Number": 49, "Molar Mass": 114.82},
            {"Symbol": "Sn", "Name": "Tin", "Atomic Number": 50, "Molar Mass": 118.71},
            {"Symbol": "Sb", "Name": "Antimony", "Atomic Number": 51, "Molar Mass": 121.76},
            {"Symbol": "Te", "Name": "Tellurium", "Atomic Number": 52, "Molar Mass": 127.60},
            {"Symbol": "I", "Name": "Iodine", "Atomic Number": 53, "Molar Mass": 126.90},
            {"Symbol": "Xe", "Name": "Xenon", "Atomic Number": 54, "Molar Mass": 131.29},
            {"Symbol": "Cs", "Name": "Cesium", "Atomic Number": 55, "Molar Mass": 132.91},
            {"Symbol": "Ba", "Name": "Barium", "Atomic Number": 56, "Molar Mass": 137.33},
            {"Symbol": "La", "Name": "Lanthanum", "Atomic Number": 57, "Molar Mass": 138.91},
            {"Symbol": "Ce", "Name": "Cerium", "Atomic Number": 58, "Molar Mass": 140.12},
            {"Symbol": "Pr", "Name": "Praseodymium", "Atomic Number": 59, "Molar Mass": 140.91},
            {"Symbol": "Nd", "Name": "Neodymium", "Atomic Number": 60, "Molar Mass": 144.24},
            {"Symbol": "Pm", "Name": "Promethium", "Atomic Number": 61, "Molar Mass": 145},
            {"Symbol": "Sm", "Name": "Samarium", "Atomic Number": 62, "Molar Mass": 150.36},
            {"Symbol": "Eu", "Name": "Europium", "Atomic Number": 63, "Molar Mass": 151.96},
            {"Symbol": "Gd", "Name": "Gadolinium", "Atomic Number": 64, "Molar Mass": 157.25},
            {"Symbol": "Tb", "Name": "Terbium", "Atomic Number": 65, "Molar Mass": 158.93},
            {"Symbol": "Dy", "Name": "Dysprosium", "Atomic Number": 66, "Molar Mass": 162.50},
            {"Symbol": "Ho", "Name": "Holmium", "Atomic Number": 67, "Molar Mass": 164.93},
            {"Symbol": "Er", "Name": "Erbium", "Atomic Number": 68, "Molar Mass": 167.26},
            {"Symbol": "Tm", "Name": "Thulium", "Atomic Number": 69, "Molar Mass": 168.93},
            {"Symbol": "Yb", "Name": "Ytterbium", "Atomic Number": 70, "Molar Mass": 173.04},
            {"Symbol": "Lu", "Name": "Lutetium", "Atomic Number": 71, "Molar Mass": 174.97},
            {"Symbol": "Hf", "Name": "Hafnium", "Atomic Number": 72, "Molar Mass": 178.49},
            {"Symbol": "Ta", "Name": "Tantalum", "Atomic Number": 73, "Molar Mass": 180.95},
            {"Symbol": "W", "Name": "Tungsten", "Atomic Number": 74, "Molar Mass": 183.84},
            {"Symbol": "Re", "Name": "Rhenium", "Atomic Number": 75, "Molar Mass": 186.21},
            {"Symbol": "Os", "Name": "Osmium", "Atomic Number": 76, "Molar Mass": 190.23},
            {"Symbol": "Ir", "Name": "Iridium", "Atomic Number": 77, "Molar Mass": 192.22},
            {"Symbol": "Pt", "Name": "Platinum", "Atomic Number": 78, "Molar Mass": 195.08},
            {"Symbol": "Au", "Name": "Gold", "Atomic Number": 79, "Molar Mass": 196.97},
            {"Symbol": "Hg", "Name": "Mercury", "Atomic Number": 80, "Molar Mass": 200.59},
            {"Symbol": "Tl", "Name": "Thallium", "Atomic Number": 81, "Molar Mass": 204.38},
            {"Symbol": "Pb", "Name": "Lead", "Atomic Number": 82, "Molar Mass": 207.2},
            {"Symbol": "Bi", "Name": "Bismuth", "Atomic Number": 83, "Molar Mass": 208.98},
            {"Symbol": "Po", "Name": "Polonium", "Atomic Number": 84, "Molar Mass": 209},
            {"Symbol": "At", "Name": "Astatine", "Atomic Number": 85, "Molar Mass": 210},
            {"Symbol": "Rn", "Name": "Radon", "Atomic Number": 86, "Molar Mass": 222},
            {"Symbol": "Fr", "Name": "Francium", "Atomic Number": 87, "Molar Mass": 223},
            {"Symbol": "Ra", "Name": "Radium", "Atomic Number": 88, "Molar Mass": 226},
            {"Symbol": "Ac", "Name": "Actinium", "Atomic Number": 89, "Molar Mass": 227},
            {"Symbol": "Th", "Name": "Thorium", "Atomic Number": 90, "Molar Mass": 232.04},
            {"Symbol": "Pa", "Name": "Protactinium", "Atomic Number": 91, "Molar Mass": 231.04},
            {"Symbol": "U", "Name": "Uranium", "Atomic Number": 92, "Molar Mass": 238.03},
            {"Symbol": "Np", "Name": "Neptunium", "Atomic Number": 93, "Molar Mass": 237},
            {"Symbol": "Pu", "Name": "Plutonium", "Atomic Number": 94, "Molar Mass": 244},
            {"Symbol": "Am", "Name": "Americium", "Atomic Number": 95, "Molar Mass": 243},
            {"Symbol": "Cm", "Name": "Curium", "Atomic Number": 96, "Molar Mass": 247},
            {"Symbol": "Bk", "Name": "Berkelium", "Atomic Number": 97, "Molar Mass": 247},
            {"Symbol": "Cf", "Name": "Californium", "Atomic Number": 98, "Molar Mass": 251},
            {"Symbol": "Es", "Name": "Einsteinium", "Atomic Number": 99, "Molar Mass": 252},
            {"Symbol": "Fm", "Name": "Fermium", "Atomic Number": 100, "Molar Mass": 257},
            {"Symbol": "Md", "Name": "Mendelevium", "Atomic Number": 101, "Molar Mass": 258},
            {"Symbol": "No", "Name": "Nobelium", "Atomic Number": 102, "Molar Mass": 259},
            {"Symbol": "Lr", "Name": "Lawrencium", "Atomic Number": 103, "Molar Mass": 262},
            {"Symbol": "Rf", "Name": "Rutherfordium", "Atomic Number": 104, "Molar Mass": 267},
            {"Symbol": "Db", "Name": "Dubnium", "Atomic Number": 105, "Molar Mass": 270},
            {"Symbol": "Sg", "Name": "Seaborgium", "Atomic Number": 106, "Molar Mass": 271},
            {"Symbol": "Bh", "Name": "Bohrium", "Atomic Number": 107, "Molar Mass": 270},
            {"Symbol": "Hs", "Name": "Hassium", "Atomic Number": 108, "Molar Mass": 277},
            {"Symbol": "Mt", "Name": "Meitnerium", "Atomic Number": 109, "Molar Mass": 282},
            {"Symbol": "Ds", "Name": "Darmstadtium", "Atomic Number": 110, "Molar Mass": 285},
            {"Symbol": "Rg", "Name": "Roentgenium", "Atomic Number": 111, "Molar Mass": 286},
            {"Symbol": "Cn", "Name": "Copernicium", "Atomic Number": 112, "Molar Mass": 289},
            {"Symbol": "Nh", "Name": "Nihonium", "Atomic Number": 113, "Molar Mass": 290},
            {"Symbol": "Fl", "Name": "Flerovium", "Atomic Number": 114, "Molar Mass": 293},
            {"Symbol": "Mc", "Name": "Moscovium", "Atomic Number": 115, "Molar Mass": 294},
            {"Symbol": "Lv", "Name": "Livermorium", "Atomic Number": 116, "Molar Mass": 293},
            {"Symbol": "Ts", "Name": "Tennessine", "Atomic Number": 117, "Molar Mass": 294},
            {"Symbol": "Og", "Name": "Oganesson", "Atomic Number": 118, "Molar Mass": 294}
        ]    
    reactans = input("What are the reactants of the reaction? Put a plus sign between them. For example (CH4 + 02): ")
    reactantsSplitUp = re.split(r'\+| \+ ', reactans)
    reactantsFullySplitUp = [[reactant] for reactant in reactantsSplitUp]

    
    brokenUpReactantsCompoundsTwo = []
    element_pattern = r'([A-Z][a-z]*)(\d*)'
    group_pattern = r'\((.*?)\)(\d*)'  # Capture groups within parentheses and their counts

    # Process each reactant compound
    for reactant in reactantsFullySplitUp:
        compound = reactant[0]
        compound_list = []

        # Process groups with parentheses first
        for group, group_count in re.findall(group_pattern, compound):
            group_count = int(group_count) if group_count else 1
            # Find each element inside the group and apply the group count
            for element, count in re.findall(element_pattern, group):
                count = int(count) if count else 1
                compound_list.append((element, count * group_count))

        # Process elements outside any parentheses
        compound_no_groups = re.sub(group_pattern, '', compound)  # Remove groups already processed
        for element, count in re.findall(element_pattern, compound_no_groups):
            count = int(count) if count else 1
            compound_list.append((element, count))

        # Add processed compound to the final list
        brokenUpReactantsCompoundsTwo.append(compound_list)



    molarMassOfCompoundReactants = []
    compoundNumber = -1

    for i in brokenUpReactantsCompoundsTwo:
        numberOfElements = 0
        compoundNumber += 1
        molarMassOfElement = []
        for k in i:
            for t in elements:
                if k[0] == t['Symbol']: # with tuples u specify the number of the group starting at zero rather than the name
                    molarMassOfElement.append(t['Molar Mass'] * k[1])
                    numberOfElements += 1
        if len(i) > numberOfElements or len(i) == 0:
            print(f"{reactantsSplitUp[compoundNumber]} is not a real compound. Make sure to put in real compounds. Its case sensitive He is not equivalent to HE or he.")
            equations()
        molarMassOfCompoundReactants.append(sum(molarMassOfElement))



    numberOfElementsReactants = [
    ]
    for i in brokenUpReactantsCompoundsTwo:
        for k in i:
            isThere = False
            for f in numberOfElementsReactants:
                if k[0] == f['Element']:
                    f['Count'] += k[1]
                    isThere = True
                    break
            if isThere == False:
                numberOfElementsReactants.append(dict(Element = k[0], Count = k[1]))



    products = input("What are the products of the reaction? Put a plus sign between them. For example (CO2 + H2O): ")
    productsSplitUp = re.split(r'\+| \+ ', products)
    productsFullySplitUp = [[product] for product in productsSplitUp] #A list comperehansion where it makes a list [product] for every object or product in productsSplitUp. [Product works as a placeholder and needs to be the same before the "for" and after]
    
    brokenUpProductsCompoundsTwo = []
    element_pattern = r'([A-Z][a-z]*)(\d*)'
    group_pattern = r'\((.*?)\)(\d*)'  # Capture groups within parentheses and their counts

    # Process each product compound
    for product in productsFullySplitUp:
        compound = product[0]
        compound_list = []

        # Process groups with parentheses first
        for group, group_count in re.findall(group_pattern, compound):
            group_count = int(group_count) if group_count else 1
            # Find each element inside the group and apply the group count
            for element, count in re.findall(element_pattern, group):
                count = int(count) if count else 1
                compound_list.append((element, count * group_count))

        # Process elements outside any parentheses
        compound_no_groups = re.sub(group_pattern, '', compound)  # Remove groups already processed
        for element, count in re.findall(element_pattern, compound_no_groups):
            count = int(count) if count else 1
            compound_list.append((element, count))

        # Add processed compound to the final list
        brokenUpProductsCompoundsTwo.append(compound_list)


    molarMassOfCompoundProducts = []
    compoundNumber = -1

    for i in brokenUpProductsCompoundsTwo:
        numberOfElements = 0
        compoundNumber += 1
        molarMassOfElement = []
        for k in i:
            for t in elements:
                if k[0] == t['Symbol']: # with tuples u specify the number of the group starting at zero rather than the name
                    molarMassOfElement.append(t['Molar Mass'] * k[1])
                    numberOfElements += 1
        if len(i) > numberOfElements or len(i) == 0:
            print(f"{productsSplitUp[compoundNumber]} is not a real compound. Make sure to put in real compounds. Its case sensitive He is not equivalent to HE or he.")
            equations()
        molarMassOfCompoundProducts.append(sum(molarMassOfElement))



    numberOfElementsProducts = [
    ]
    for i in brokenUpProductsCompoundsTwo:
        for k in i:
            isThere = False
            for f in numberOfElementsProducts:
                if k[0] == f['Element']:
                    f['Count'] += k[1]
                    isThere = True
                    break
            if isThere == False:
                numberOfElementsProducts.append(dict(Element = k[0], Count = k[1]))


        
    if len(numberOfElementsProducts) != len(numberOfElementsReactants):
        print("This equation is not balancable and most likely impossible.")
        gameOver()



    elementsinReactant =[[0]*len(numberOfElementsProducts) for i in brokenUpReactantsCompoundsTwo]
    elementsInProduct = [[0]*len(numberOfElementsProducts) for i in brokenUpProductsCompoundsTwo]
 

    element_index_map = {reactant['Element']: idx for idx, reactant in enumerate(numberOfElementsReactants)} #creates a dictionary that maps each element symbol in numberOfElementsReactants to its position (index) in the list elementsInProduct.
    # enumerate() is a Python function that takes a sequence (like a list) and returns both the index (position) and the item in that position.
    # (0, {'Element': 'C', 'Count': 1}) for the first element, (1, {'Element': 'H', 'Count': 4}) for the second element.
    #outputs: {'C': 0, 'H': 1, 'O': 2} so each element is given a location
    

    for i, compound in enumerate(brokenUpReactantsCompoundsTwo): #so for (i, {'Element': 'C', 'Count': 1})
        for element, count in compound: #for each tuple in {'Element': 'C', 'Count': 1} it unpacks it to 
         if element in element_index_map: # if element 'C' is found in element_index_map which looks like {'C': 0, 'H': 1, 'O': 2}
            idx = element_index_map[element] #This line retrieves the index for element from element_index_map. For example, if element is 'C', idx would be 0.
            elementsinReactant[i][idx] = count  # Update the count

    for i, compound in enumerate(brokenUpProductsCompoundsTwo): #so for (i, {'Element': 'C', 'Count': 1})
        for element, count in compound: #for each tuple in {'Element': 'C', 'Count': 1} it unpacks it to 
         if element in element_index_map: # if element 'C' is found in element_index_map which looks like {'C': 0, 'H': 1, 'O': 2}
            idx = element_index_map[element] #This line retrieves the index for element from element_index_map. For example, if element is 'C', idx would be 0 
            elementsInProduct[i][idx] = count * -1  # Update the count but makes everything negative cuz product side


    elementMatrix = elementsinReactant + elementsInProduct
    elementMatrix = Matrix(elementMatrix)
    elementMatrix = elementMatrix.transpose()
    solution = elementMatrix.nullspace()[0] #ignores the 0's since technically 0 is a solution
    multiple = lcm([val.q for val in solution]) #looks for lcm thats not a fraction
    solution = multiple*solution
    solution = solution.tolist()
    solution = sum(solution,[])
    solutionAsStr = [str(x) for x in solution]

    reactantsFullySplitUp = sum(reactantsFullySplitUp,[])
    productsFullySplitUp = sum(productsFullySplitUp,[])
    
    balancedEquation = ''
    number = -1

    for i in reactantsFullySplitUp:
        number +=1
        if solutionAsStr[number] == '1':
            balancedEquation = balancedEquation + i + ' + '
        else: 
            balancedEquation = balancedEquation + solutionAsStr[number] + i + ' + '
    balancedEquation = balancedEquation.rstrip(' + ') + ' ---> ' #rstrip removes the trailing ' + '
    for i in productsFullySplitUp:
        number +=1
        if solutionAsStr[number] == '1':
            balancedEquation = balancedEquation + i + ' + '
        else: 
            balancedEquation = balancedEquation + solutionAsStr[number] + i + ' + '
    balancedEquation = balancedEquation.rstrip(' + ')
    
    print(balancedEquation)
    print("The molar masses in order are:")
    print(molarMassOfCompoundReactants + molarMassOfCompoundProducts)

    molesOfReactants = []
    molesOfProducts = []
    massOfReactants = []
    massOfProducts = []
    reactantNumber = -1
    productNumber = -1
    limiting = 0
    molesUsed = []
    molesRemaining = []
    molesRemaingProducts = []


    x = str(input("Would you like to solve for anything? 1 for yes, anything else for no: "))
    if x == '1':
        x = int(input("Do you have moles or mass? 1 for moles, 2 for mass: "))
        if x == 1:
            x = int(input("Do you have the moles of the reactants or the products? 1 for reactants, 2 for products: "))
            if x == 1:
                for i in reactantsFullySplitUp:
                    reactantNumber += 1
                    molesOfEach = float(input(f"How many moles of {reactantsFullySplitUp[reactantNumber]} do you have? 'inf' for excess: "))
                    molesOfReactants.append(molesOfEach)
                    limiting, molesOfProducts, molesUsed, molesRemaining = findingLimitingReactant(molesOfReactants,solution,len(molarMassOfCompoundProducts))
                    molesRemaingProducts = [0] * len(molesOfProducts)
                    limiting = reactantsFullySplitUp[limiting]

            elif x == 2:
                for i in productsFullySplitUp:
                    productNumber += 1
                    molesOfEach = float(input(f"How many moles of {productsFullySplitUp[productNumber]} were made? 'inf' for excess: "))
                    molesOfProducts.append(molesOfEach)
                limiting, molesOfReactants, molesOfProducts, molesRemaingProducts = findingLimitingProduct(molesOfProducts,solution,len(molarMassOfCompoundReactants))
                molesUsed = molesOfReactants
                molesRemaining = [0] * len(molesOfReactants)
                limiting = productsFullySplitUp[limiting]

            else:
                print("Make sure to press 1 or 2 netx time")
                chemistry()
            
            #look for limiting reactants or product


        elif x == 2:
            x = int(input("Do you have the mass of the reactanats or the products? 1 for reactants, 2 for products: "))
            if x == 1:
                for i in reactantsFullySplitUp:
                    reactantNumber += 1
                    massOfEach = []
                    massOfEach = float(input(f"How many grams of {reactantsFullySplitUp[reactantNumber]} do you have? 'inf' for excess: "))
                    massOfReactants.append(massOfEach)
                reactantNumber = -1

                for i in massOfReactants:
                    reactantNumber += 1
                    molesOfEach = massOfReactants[reactantNumber]/molarMassOfCompoundReactants[reactantNumber]
                    molesOfReactants.append(molesOfEach)
                limiting, molesOfProducts, molesUsed, molesRemaining = findingLimitingReactant(molesOfReactants,solution,len(molarMassOfCompoundProducts))
                molesRemaingProducts = [0] * len(molesOfProducts)
                limiting = reactantsFullySplitUp[limiting]

            elif x == 2:
                for i in productsFullySplitUp:
                    productNumber +=1
                    massOfEach = []
                    massOfEach = float(input(f"How many grams of {productsFullySplitUp[productNumber]} were made? 'inf' for excess: "))
                    massOfProducts.append(massOfEach)
                productNumber = -1

                for i in massOfProducts:
                    productNumber += 1
                    molesOfEach = massOfProducts[productNumber]/molarMassOfCompoundProducts[productNumber]
                    molesOfProducts.append(molesOfEach)
                limiting, molesOfReactants, molesOfProducts, molesRemaingProducts = findingLimitingProduct(molesOfProducts,solution,len(molarMassOfCompoundReactants))
                molesUsed = molesOfReactants
                molesRemaining = [0] * len(molesOfReactants)
                limiting = productsFullySplitUp[limiting]

            else:
                print("Make sure to press 1 or 2 netx time")
                chemistry()

        else:
            print("Make sure to press 1 or 2 netx time")
            chemistry()

    else:
        gameOver()

    print(f"The balanced equation was \n{balancedEquation}")
    print(f"The limiting reactant/product is {limiting}")
    print(f"The moles that are used are \n{molesUsed}")
    print(f"The moles that are remaining are \n{molesRemaining}")    
    print(f"The moles that are produced are \n{molesOfProducts}")
    print(f"The excess products are \n{molesRemaingProducts}")


    gameOver()        

def findingLimitingReactant(molesOfReactants,solution,numberOfProducts):
    molesOfProducts = []
    compoundNumber = -1
    molesUsed = []
    molesRemaining = []
    for i in molesOfReactants:
        molesOfEach = []
        compoundNumber += 1
        for k in range(numberOfProducts):
            molesOfEach.append(i * (solution[k + len(molesOfReactants)]/solution[compoundNumber])) 
        molesOfProducts.append(molesOfEach)
    
    limitingReactant = min(range(len(molesOfProducts)), key=lambda i: sum(molesOfProducts[i])) # key tells min() what to use as the comparison values for each idex and for each index i key=lambda i: sum(molesOfProduct[i]) computes the sum of the sublist at that index. 
        #range(len(list_of_lists)) provides indices [0, 1, 2, 3].
        # key=lambda i: sum(list_of_lists[i]) tells min() to consider each sublist's sum.
        # min() then returns the index with the smallest sum, not the sum itself.

    compoundNumber = -1
    for i in molesOfReactants:
        compoundNumber += 1
        molesUsed.append(molesOfReactants[limitingReactant] * (solution[compoundNumber]/solution[limitingReactant]))
        molesRemaining.append(i - molesUsed[compoundNumber])

    return(limitingReactant,molesOfProducts[limitingReactant],molesUsed,molesRemaining)

def findingLimitingProduct(molesOfProducts,solution,numberOfReactants):
    molesOfReactants = []
    compoundNumber = -1
    molesProduced = []
    molesRemaining = []
    for i in molesOfProducts:
        molesOfEach = []
        compoundNumber += 1
        for k in range(numberOfReactants):
            molesOfEach.append(i * (solution[k]/solution[compoundNumber])) 
        molesOfReactants.append(molesOfEach)
    
    limitingProduct = min(range(len(molesOfReactants)), key=lambda i: sum(molesOfReactants[i])) # key tells min() what to use as the comparison values for each idex and for each index i key=lambda i: sum(molesOfProduct[i]) computes the sum of the sublist at that index. 
        #range(len(list_of_lists)) provides indices [0, 1, 2, 3].
        # key=lambda i: sum(list_of_lists[i]) tells min() to consider each sublist's sum.
        # min() then returns the index with the smallest sum, not the sum itself.

    x = molesOfReactants[limitingProduct]
    x = x[0]

    for i in range(len(molesOfProducts)):
        molesProduced.append(x * (solution[numberOfReactants + i]/solution[0]))
        molesRemaining.append(molesOfProducts[i] - (x * (solution[numberOfReactants + i]/solution[0])))

    return(limitingProduct,molesOfReactants[limitingProduct],molesProduced,molesRemaining)

def gameOver():
    input("Press enter to start over again ")
    start()

start()


