#opdracht 1a
def opdracht1a():
    aantalUren = int(input())
    uurBedragTotaal = aantalUren * 40
    totaalBedrag = uurBedragTotaal + 60

    print(totaalBedrag)

# opdracht1a()

#opdracht 1b

def opdracht1b():
    klantAankoopBedrag = int(input())
    if klantAankoopBedrag > 400:
        return klantAankoopBedrag / 100 * 90
    else:
        return klantAankoopBedrag

# print(opdracht1b())

#opdracht 2

def opdracht2():
    behaaldePunten = int(input())
    mogelijkePunten = int(input())

    eindCijfer = behaaldePunten / mogelijkePunten * 9 + 1
    return eindCijfer

# print(opdracht2())

#opdracht 3

def opdracht3a():
    tempType = int(input("typ 1 voor fahrenheit typ 2 voor celsius "))
    temp = int(input("typ je temperatuur "))

    if tempType == 1:
        return (temp - 32) * 5/9
    elif tempType == 2:
        return (temp * 9/5) + 32
    else:
        print("kies 1 of 2")

# print(opdracht3a())

#opdracht 3

def opdracht3b():
    tempType = int(input("typ 1 voor fahrenheit typ 2 voor celsius typ 3 voor kelvin "))
    temp = int(input("typ je temperatuur "))

    if tempType == 1:
        calcCelsius = (temp - 32) * 5/9
        calcKelvin = calcCelsius + 273.15
        return "de temperatuur in celcius = ", calcCelsius, "de temperatuur in kelvin = ", calcKelvin
    elif tempType == 2:
        calcFahrenheit = (temp * 9/5) + 32
        calcKelvin = temp + 273.15
        return "de temperatuur in Fahrenheit = ", calcFahrenheit, "de temperatuur in kelvin = ", calcKelvin
    elif tempType == 3:
        calcCelsius = temp - 273.15
        calcFahrenheit = (temp - 273.15) * 9/5 + 32
        return "de temperatuur in Fahrenheit = ", calcFahrenheit, "de temperatuur in celsius = ", calcCelsius 
    else:
        print("kies 1,2 of 3")

# print(opdracht3b())

#interactive story

def beginStory():
    username = str(input("Wat is je naam?"))
    print("Hallo!", username)

