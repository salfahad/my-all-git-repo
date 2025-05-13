##Combining Multiple Logical Operators:

temperature = 22
is_raining = False
is_snowing = False

if (temperature > 20 and not is_raining) or is_snowing:
    print("weather is suitable for outdoor activities.")

else:
    print("weather conditions are not ideal")

##Using not for Negation:
is_sunny = True
is_cloudy = False

if not is_sunny and is_cloudy:
    print("It might rain today.")
else:
    print("It's a beautiful sunny day.")