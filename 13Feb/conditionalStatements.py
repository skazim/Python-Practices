temp = 25

def thermostatRegulator(temp, low =20,high=27):

    assert high > low , "High temp should be lower than low temp"
    if temp < low:
        state = "Turn on heater"
    elif temp > high:
        state= "Turn on cooler"
    else:
        state = "Do nothing"
    print(state)
thermostatRegulator(temp)