def ValidText(TextValue):

    IsValid = True
    allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
    if TextValue == "":
        print("Invalid input - value cannot be blank.")
        IsValid = False
    elif set(TextValue).issubset(allowed_char) == False:
        print("Invalid input - entry contains invalid character.")
        IsValid = False

    return IsValid

def ValidInteger(IntegerValue):

    IsValid = True
    if IntegerValue == "":
        print("Invalid input- value cannot be blank.")
        IsValid = False
    elif IntegerValue.isdigit() == False:
        print("Invalid input - value must be numbers only.")
        IsValid = False

    return IsValid


def ValidPhone(PhoneValue):

    IsValid = True
    if PhoneValue.isdigit() == False:
        print("Invalid input - value must be numbers only - no spaces.")
        IsValid = False
    elif len(PhoneValue) != 10:
        print("Invalid input - must be 10 digits.")
        IsValid = False

    return IsValid

def ValidIntegerNumber(NumberValue, MinValue, MaxValue):

    IsValid = True
    try:
        NumberValue = int(NumberValue)
    except:
        print("Invalid input - must be a valid number.")
        IsValid = False
    else:
        if NumberValue < MinValue or NumberValue > MaxValue:
            print("Invalid input - number must be between " + str(MinValue) + " and " + str(MaxValue) + ".")
            IsValid = False

    return IsValid


def ValidFloatNumber(NumberValue, MinValue, MaxValue):

    IsValid = True
    try:
        NumberValue = float(NumberValue)
    except:
        print("Invalid input - must be a valid number.")
        IsValid = False
    else:
        if NumberValue < MinValue or NumberValue > MaxValue:
            print("Invalid input - number must be between " + str(MinValue) + " and " + str(MaxValue) + ".")
            IsValid = False

    return IsValid

def StrAndPad(DollarValue):
    DollarValueStr = "${:,.2f}".format(DollarValue)
    DollarValuePad = "{:>10}".format(DollarValueStr)

    return DollarValuePad
