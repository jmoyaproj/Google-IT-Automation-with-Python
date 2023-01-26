# Question 1
# 1. Complete the function to return the result of the conversion.
# 2. Call the function to convert the trip distance from miles to kilometers.
# 3. Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result.
def convert_distance(miles):
  km = miles * 1.6
  return km

my_trip_miles = 55

my_trip_km = convert_distance(my_trip_miles)

print("The distance in kilometers is " + str(my_trip_km))

print("The round-trip in kilometers is " + str(2 * my_trip_km))

# Question 2
# This function compares two numbers and returns them in increasing order.
# 1. Fill in the blanks, so the print statement displays the result of the function call in order.
def order_numbers(number1, number2):
  if number2 > number1:
    return number1, number2
  else:
    return number2, number1

smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

# Question 4
# Let's revisit our lucky_number function. We want to change it, so that instead of printing the message,
# it returns the message. This way, the calling line can print the message, or do something else
# with it if needed.
def lucky_number(name):
  number = len(name) * 9
  message = "Hello " + name + ". Your lucky number is " + str(number)
  return message

print(lucky_number("Kay"))
print(lucky_number("Cameron"))