# string concatenation ( how do yo put strings together)
# suppose we want to create a string that says "subscribe to _____"
#youtuber = " Jenny Augustin"  # some string variable

# a few ways to do this
#print("subscribe to"+youtuber)
#print("subscribe to{}".format(youtuber))  # put any youtuber you type into {}
#print(f"subscribe to{youtuber}")  # f string the cleanest way to express string concatenation



nom_complet = input("nom:") #adj is an variable, we have to define it
nom = input("country of birth:")
date_birth = input("date birth:")
age = input("age:")
country_residence = input("country residence:")
work = input("work:")
career = input("career:")
Datos_personales= f"My name is {nom_complet}. I was born in {nom},{date_birth} so I am {age}. \
I live in {country_residence} I work at {work}. I am studying {career}. Boy, Bye."

print(Datos_personales)
