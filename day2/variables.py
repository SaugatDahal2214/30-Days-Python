import math 
##Day 2: 30 Days of python programming

first_name = "Saugat"
last_name = "Dahal"
full_name = "Saugat Dahal"
country = "Nepal"
city = "Kathmandu"

age = 23
year = 2024

is_married = False
is_true = True
is_light_on = False


x, y, z = "Apple", 10, 3.14


print(first_name, last_name, full_name)
print(country, city, age, year)
print(is_married, is_true, is_light_on)
print(x, y, z)


##Exercise two

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(x))
print(type(y))
print(type(z))


print(len(first_name))


if (len(first_name) > len(last_name)):
    print("First Name is Greater")
else:
    print("Last Name is Greater")


num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print("The total is: ", total)
print("The difference is: ", diff)
print("The product is: ", product)
print("The division is: ", division)
print("The remainder is: ", remainder)
print("The exp is: ", exp)
print("The floor division is: ", floor_division)


radius = 30

_area_of_circle = math.pi*radius*radius
print("Area of Circle:", _area_of_circle)

_circum_of_cirlce =  2*math.pi*radius
print("Circumference:", _circum_of_cirlce)

rad = float(input("Enter the radius: "))

area_of_cirlce = math.pi*(rad**2)
print("Area:", area_of_cirlce)


firstName = str(input("Enter your first name"))
print(firstName)

lastName = str(input("Enter your last name"))
print(lastName)

country_inp = str(input("Enter your country"))
print(country_inp)

age_inp = int(input("Enter your age"))
print(age_inp)






