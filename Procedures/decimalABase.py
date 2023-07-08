def decimalToBase(number:float,base:int,tables):
    print("number in decimal:",number)
    #integer
    convertionTableIntegerBase = [["original","integer","decimal","position"]]
    integerBase =list()
    integer = int(number)
    decimal = number-integer
    i = 0
    while(integer != 0):
        division = integer % base
        integer = int(integer / base)
        convertionTableIntegerBase.append([integer*base,integer,division,f"B{i}"])
        integerBase.append(f"{division}") 
        i+=1
    integerBase.reverse()
    integerBase =  "".join(integerBase)
    if(tables == True and len(convertionTableIntegerBase) >1 ):
        for line in convertionTableIntegerBase:
            print(line)
        print(f"Integer in base {base}: ",integerBase)

    #decimal
    decimalBase = list()
    convertionTableBase = [["integer","deciamal","postion"]]
    i = 0
    while(decimal != 0):
        integer = int(decimal*base) 
        decimal = decimal *base - integer
        convertionTableBase.append([int(integer/base),integer,decimal,f"B{i}"])
        decimalBase.append(f"{integer}")
        i+=1
    decimalBase =  "".join(decimalBase)
    if(tables == True and len(convertionTableBase) >1):
        for line in convertionTableBase:
            print(line)
        print(f"decimal in base {base}",decimalBase)
    if(integerBase != "" and  decimalBase != ""):
        result = f"{integerBase}.{decimalBase}"
    if(integerBase == "" and  decimalBase != ""):
        result = f"0.{decimalBase}"
    if(integerBase != "" and  decimalBase == ""):
        result = f"{integerBase}.0"
    print(f"Number in base {base}:",result)
    return result

def baseToDecimal(numberInBase,base,tables):
    if(tables):
        print(f"number in base {base}:",numberInBase)
    #integer
    convertion = ""
    parts = numberInBase.split('.')
    integer = 0
    i=0
    for digit in reversed(parts[0]):
        if(int(digit) == base):
            print("the number is not valid in this base")
            return None
    
        convertion += f"{digit}X{base}^{i} + "
        integer += int(digit)*(base**i)
        i+=1
    if(tables):
        print("Integer: ",convertion)
        print("Integer: ",integer)
    #deciamal
    decimal = 0
    convertion = ""
    if(len(parts)>1):
        i=1
        for digit in parts[1]:
            if(int(digit) == base):
                print("the number is not valid in this base")
                return None
            convertion += f"{digit}X(1^({base}/{i})) + "
            decimal += int(digit)*(1/(base**i))
            i+=1
        if(tables):
            print("decimal: ",convertion)
            print("decimal: ",decimal)
    number = integer + decimal
    print("The number in deciamal base:",number)
    return number

numberInBase = decimalToBase(58.578125,4,True)
print("#"*50)
baseToDecimal(numberInBase,4,True)
