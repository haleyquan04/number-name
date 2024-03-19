def single_digit_written(digit):
    digit_written = ""
    if digit == "0":
        digit_written = "zero"
    if digit == "1":
        digit_written = "one"
    if digit == "2":
        digit_written = "two"
    if digit == "3":
        digit_written = "three"
    if digit == "4":
        digit_written = "four"
    if digit == "5":
        digit_written = "five"
    if digit == "6":
        digit_written = "six"
    if digit == "7":
        digit_written = "seven"
    if digit == "8":
        digit_written = "eight"
    if digit == "9":
        digit_written = "nine"
    return digit_written

def tens_written(digit):
    digit_written = ""
    if digit == "1":
        pass
    if digit == "2":
        digit_written = "twenty"
    if digit == "3":
        digit_written = "thirty"
    if digit == "4":
        digit_written = "forty"
    if digit == "5":
        digit_written = "fifty"
    if digit == "6":
        digit_written = "sixty"
    if digit == "7":
        digit_written = "seventy"
    if digit == "8":
        digit_written = "eighty"
    if digit == "9":
        digit_written = "ninety"
    return digit_written

def teens_written(digit):
    if digit == "10":
        digit_written = "ten"
    if digit == "11":
        digit_written = "eleven"
    if digit == "12":
        digit_written = "twelve"
    if digit == "13":
        digit_written = "thirteen"
    if digit == "14":
        digit_written = "fourteen"
    if digit == "15":
        digit_written = "fifteen"
    if digit == "16":
        digit_written = "sixteen"
    if digit == "17":
        digit_written = "seventeen"
    if digit == "18":
        digit_written = "eighteen"
    if digit == "19":
        digit_written = "nineteen"
    return digit_written

def three_digit_segment_written(segment):
    segment_written = ""
    hundreds_place = ""
    add_and = ""
    tens_place = ""
    add_dash = ""
    ones_place = ""

    if len(segment) == 3:
        if (segment[0]) == '0':
            pass
        else:
            hundreds_place = single_digit_written(segment[0]) + " hundred"
            if (segment[1] + segment[2] != '00'):
                add_and = " and "

    if len(segment) >= 2:
        if segment[-2] == '1':
            tens_place = teens_written(segment[-2:])
        else:
            if segment[-2] != '0':
                tens_place = tens_written(segment[-2])
                if segment[-1] != '0':
                    add_dash = "-"
            if segment[-1] != '0':
                ones_place = single_digit_written(segment[-1])
    
    if len(segment) == 1:
        ones_place = single_digit_written(segment)
    
    segment_written = hundreds_place + add_and + tens_place + add_dash + ones_place
    return segment_written

def check_if_valid():
    while True:
        number = input("\n> ")
        digits_only = number
        original_input = number

        if '.' in digits_only:
            first_decimal = digits_only.find('.')
            digits_only = number[:first_decimal] + number[first_decimal + 1:]
            if '.' in digits_only:
                print("Your input has too many decimal points.")
        if '-' in digits_only:
            first_negative = digits_only.find('-')
            if first_negative != 0:
                print("Invalid number format, negative sign must be at the beginning.")
                print("Please input a number that follows the above guidelines.")
                continue
            digits_only = digits_only[1:]
            if '-' in digits_only:
                print("Invalid number format, only one negative sign allowed.")

        if not digits_only.isdigit():
            print("Please input a number that follows the above guidelines.")
            continue

        if float(number) < -1000000.0 or float(number) > 1000000.0:
            print("This number is not within the specified range. Try again.")
            continue
        
        if number[0] == '0':
            first_non_zero_digit = 0
            digits_list = []
            for digit in number:
                if (digit != '0') and (digit != '.'):
                    digits_list.append(digit)
            if digits_list == []:
                number = '0'
            if digits_list != []:
                first_non_zero_digit = number.find(digits_list[0])
        
            decimal_place = 0
            if '.' in number:
                decimal_place = number.find('.')
                if decimal_place < first_non_zero_digit:
                    number = number[decimal_place - 1:]
                else:
                    number = number[first_non_zero_digit:]
            else:
                number = number[first_non_zero_digit:]
        
        if number[0:2] == '-0':
            digits_list = []
            for digit in number:
                if (digit != '0') and (digit != '.') and (digit != '-'):
                    digits_list.append(digit)
            if digits_list == []:
                print("There's no such thing as negative zero! Try again.")
                continue
            if digits_list != []:
                first_non_zero_digit = number.find(digits_list[0])
        
            decimal_place = 0
            if '.' in number:
                decimal_place = number.find('.')

            if decimal_place < first_non_zero_digit:
                number = '-' + number[decimal_place - 1:]
            else:
                number = '-' + number[first_non_zero_digit:]
        return original_input, number

integer_written = ""
decimal_written = ""
negative_written = ""
bypass_number_written = ""

print("""
Type any number!
- The number should be between -1000000 and 1000000
- Input should only contain numberical digits, a negative sign, and a decimal point""")

original_input, number = check_if_valid()
if original_input != number:
    print("Your input of " + original_input + " has been simplified to " + number)

positive_integer = number
if "-" in number:
    negative_written = "negative "
    positive_number = number.replace("-","")
else:
    positive_number = number

if "." in positive_number:
    decimal_place = positive_number.find(".")
    decimal_digits_list = []
    decimal_places_written = ""
    for digit in positive_number[decimal_place + 1:]:
        if digit != '0':
            decimal_digits_list.append(digit)
    if decimal_digits_list == []:
        decimal_places_written = " zero"
    else:
        for digit in positive_number[decimal_place + 1:]:
            decimal_places_written += " " + single_digit_written(digit)

    positive_integer = positive_number[:positive_number.find(".")]
    decimal_written = " point" + decimal_places_written
else:
    positive_integer = positive_number

if positive_integer == "0":
    integer_written = "zero"
elif positive_integer == "1000000":
    integer_written = "one million"

elif len(positive_integer) > 3:
    if positive_integer[-3:] == '000':
        segment_1_written = three_digit_segment_written(positive_integer[-len(positive_integer):-3]) + " thousand"
    elif positive_integer[-3] != '0':
        segment_1_written = three_digit_segment_written(positive_integer[-len(positive_integer):-3]) + " thousand, "
    else:
        segment_1_written = three_digit_segment_written(positive_integer[-len(positive_integer):-3]) + " thousand and "

    segment_2_written = three_digit_segment_written(positive_integer[-3:])
    integer_written = segment_1_written  + segment_2_written
elif 1 <= len(positive_integer) <= 3:
    integer_written = three_digit_segment_written(positive_integer)


number_written = negative_written + integer_written + decimal_written + "\n"
print(number_written)