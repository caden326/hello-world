# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
yourname = "Caden"
print("Hello", (yourname))  # with a comma
print("Hello " + (yourname))  # with a +
# 3. print "Hello 42!" with the number in a variable
favnum = 8
favnum2 = "8"
print("Hello", (favnum))  # with a comma
print("Hello " + (favnum2))  # with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pho"
print("I love to eat {f1} and {f2}".format(
    f1=fave_food1, f2=fave_food2))  # with .format()
print("I love to eat %s and %s" % (fave_food1, fave_food2))  # with an f string
