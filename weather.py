temperature= int(input("enter the temperature"))
if temperature<20:
    outfit= "jacket"
    print("it is cold today")
    print("wear a", outfit)
else:
    outfit= "t-shirt"
    print("it is warm today")
    print("wear an", outfit)
is_rain= (input("is it raining today(yes/no):"))
if is_rain:
    print("bring an umbrella")

wind_speed= int(input("enter the wind speed in km/hr:"))
if wind_speed>30:
    needs_windbreaker= "yes"
    print("it is windy today")
    print("wear a windbreaker over your", outfit)
else:
    needs_windbreaker= "no"
    print("it is calm today")
    print("no windbreaker needed over your", outfit)
print("")
print("weather check complete")
print("weather outfit picker")
print("temperature:", temperature)
print("outfit chosen:", outfit)
print("raining:", is_rain)
print("windbreaker needed:", needs_windbreaker)