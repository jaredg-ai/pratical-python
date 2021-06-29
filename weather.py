temperature = 95

if temperature > 80:
    print("It's too hot!")
    print("Stay inside!")
elif temperature < 60:
    print("It's too cold!")
    print("Stay inside!")
else:
    print("Go outside!")


# you can also do this.
# in this case, either the > 80 can be ture. Or the < 60 can be ture to print stay inside.

if temperature > 80 or temperature < 60:
    print("stay inside!")
else:
    print("Enjoy the outdoors!")

# you can also use and 
# for this, both the < 80 and the forcast need to be true for go oustide to run.
#because the forcast is false, the else statement will run.
temperature = 75
forecast = "rain" #if this was "sunny" then the forcast would be true and fo outside will run.

if temperature < 80 and forecast != "rain":
    print("Go outside!")
else:
    print("stay inside!")

#using the "not"

forecast = "rain"
#since forcast does == "rain", the not makes the ture into a false. So the else will run.
if not forecast == "rain":
    print("go outside!")
else:
    print("stay indoors!")

#you can also use booleans
raining = True

if raining:
    print("Stay inside!")


#again, using the "not" will tun it the opposite. So true becomes false.
raining = True
#in this case the else will run.
if not raining:
    print("Go outside!")
else:
    print("Stay inside!")