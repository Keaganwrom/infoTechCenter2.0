import random

# Gas level function
def gasLevelGauge():
    gasLevelList = ["Empty","Low","quartar tank","half tank","Full"]
    currentGasLevel = random.choice(gasLevelList)
    print(currentGasLevel)

gasLevelGauge()