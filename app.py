#This will serve as the main application in Python. Other languages to follow

scales = {
    "Gauge 1": 1/32,
    "0 Scale": 1/48,
    "O Gauge": 1/43.5,
    "OO Gauge": 1/76.2,
    "H0 Scale": 1/87,
    "N Scale": 1/160,
    "N Gauge": 1/148
}


measures = {

}


entry = input("Please write the measure you want to convert: ")
entry = int(entry)
entryscale = input("Please write the name of the scale you want to convert to: ") 


def ScaleConverter(entry, entryscale):

    if entryscale in scales:
        operation = entry * scales[entryscale]
        print(operation)

    else:
        print("Sorry, there has been a mistake with one of your entries.")


ScaleConverter(entry, entryscale)
    