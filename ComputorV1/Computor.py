toSolve = input("input\n")

def my_root(val):
    st = str(val)
    left = ""
    right = ""

    if(st.find(".")!= -1) :
        left = st[:st.find(".")]
        right = st[st.find(".") + 1:]
    else :
        left = st
    down = ""
    leftTotal = 0
    midTotal = 0
    mid = ""
    rt = ""
    while True:
        if len(left) == 0 :
            break
        if len(left)  == 1 or len(left)  == 2:
            down = left
            left = ""
        elif (len(left) % 2 ) > 0:
            down = left[:1]
            left = left[1:]
        elif (len(left) % 2) == 0 :
            down = left[:2]
            left = left[2:]
        adder = 0
        mid = str(midTotal) + down
        midTotal = int(mid)
        subtrector = 0 
        if (leftTotal == 0) : 
            while (adder * adder) < midTotal:
                adder += 1
            adder -=1
            subtrector = adder * adder
            hold = str(leftTotal) + str(adder)
            leftTotal = int(hold) + adder
            midTotal = midTotal - subtrector
        else :
            while (adder * int(str(leftTotal) +  str(adder))) < midTotal:
                adder += 1
            adder -=1
            subtrector = adder * int(str(leftTotal) +  str(adder))
            leftTotal = int(str(leftTotal) +  str(adder)) + adder
            midTotal = midTotal - subtrector
        
        rt = rt + str(adder)
    
    
    if (midTotal > 0 or len(right)  > 0) :
       rt = rt + "."
  
    z = 0
    while z < 2:
        if midTotal < 1 and len(right) == 0 :
             break
        elif midTotal > 0 and len(right) == 0 :
            mid = str(midTotal) + "00"
            midTotal = int(mid)
        if (len(right) ) > 2 :
            down = right[:2]
            right = right[2:]
        elif len(right)  == 1 :
            down = right + "0"
            right = ""
        elif  len(right)  == 2:
            down = right
            right = ""
        
        adder = 0
        midTotal = int(str(midTotal) + down)
        subtrector = 0 
        
        while (adder * int(str(leftTotal) +  str(adder))) < midTotal: 
            adder += 1
        adder -=1
        
        subtrector = adder * int(str(leftTotal) +  str(adder))
        leftTotal = int(str(leftTotal) +  str(adder)) + adder
        midTotal = midTotal - subtrector    
        rt = rt + str(adder)
        z +=1
        
    return rt


if (toSolve is None ):
   print("error")
   exit()

if(toSolve.find("=") == -1) :
    print("error")
    exit()

sp = toSolve.split(" ")
digree = -1
digree2 = -1
digree3 = -1

for st in sp :
    
    if(st.find("X^1") != -1 ) :
        digree = 1
        if(st.find("." ) != -1):
            print("input error")
            exit()

    if(st.find("X^2") != -1 ) :
        digree2 = 2
        if(st.find("." ) != -1):
            print("input error")
            exit()

    if(st.find("X^3") != -1 ) :
        digree3 = 3
        if(st.find("." ) != -1):
            print("input error")
            exit()

itr = 0
itr2 = 0
if(digree == 1 or digree == 2):
    for st in sp :
        if(st.find("X^0") != -1):
            sp[itr] = "1"
        if(st.find("X^1") != -1):
            sp[itr] = "b"
        if(st.find("X^2") != -1):
            sp[itr] = "a"
        itr +=1
    
if(digree3 > 2):
    if(digree3 == 3):
        print("Digree : "+ str(digree))
    print("The polynomial degree is stricly greater than 2, I can\'t solve.")
    exit()

if(itr > 0):
    toSolve = " ".join(sp)
    toSolve = toSolve.replace(" ", "")
    toSolve = toSolve.replace("*1", "")
    toSolve = toSolve.replace("*a", "a")
    toSolve = toSolve.replace("*b", "b")
    if(toSolve.find("X^") != -1):
        print("input error.")
        exit()
    if(digree == 1 or digree2 == 2) :
        sp = toSolve.split("=")
        leftSide = sp[0]
        rightSide = sp[1]
        c = 0
        b = 0
        a = 0
        while True :
            plus = leftSide.find("+")
            minus = leftSide.find("-")
            if(plus == 0) :
                plus = leftSide.find("+", 1)
            if(minus == 0) :
                minus = leftSide.find("-", 1)
            if(plus < minus and plus > 0) :
                if(leftSide[plus-1] == 'a'):
                    a = a +  (float(leftSide[:plus -1])) 
                elif(leftSide[plus-1] == 'b'):
                    b = b + (float(leftSide[:plus -1]) ) 
                else :
                    c = c + (float(leftSide[:plus]) ) 
                leftSide = leftSide[plus:]
            if( minus == -1 and plus > 0) :
                if(leftSide[plus-1] == 'a'):
                    a = a +  (float(leftSide[:plus -1]) ) 
                elif(leftSide[plus-1] == 'b'):
                    b = b + (float(leftSide[:plus -1]) ) 
                else :
                    c = c + (float(leftSide[:plus]) ) 
                leftSide = leftSide[plus:]
            elif(plus > minus and minus > 0) :
                if(leftSide[minus-1] == 'b'):
                    b = b + (float(leftSide[:minus -1]) ) 
                else :
                    c = c + (float(leftSide[:minus]) ) 
                leftSide = leftSide[minus:]
            elif(minus == plus and minus != -1) :
                if(leftSide[minus -1] == 'a'):
                    a = a +  (float(leftSide[:minus -1])) 
                elif(leftSide[minus -1] == 'b'):
                    b = b + (float(leftSide[:minus -1])) 
                else :
                    c = c + (float(leftSide[:minus] )) 
                leftSide = leftSide[minus:]
            elif(minus > 0 and plus == -1) :
                if(leftSide[minus -1] == 'a'):
                    a = a +  (float(leftSide[:minus -1])) 
                elif(leftSide[minus -1] == 'b'):
                    b = b + (float(leftSide[:minus -1]) ) 
                else :
                    c = c + (float(leftSide[:minus] )) 
                leftSide = leftSide[minus:]
            elif( plus > 0 and minus == -1) :
                if(leftSide[plus -1] == 'a'):
                    a = a +  (float(leftSide[:plus -1]) ) 
                elif(leftSide[plus -1] == 'b'):
                   b = b + (float(leftSide[:plus -1]) ) 
                else :
                    c = c + (float(leftSide[:plus] )) 
                leftSide = leftSide[plus:]
            elif (minus == -1 and plus == -1) :
                if(leftSide[len(leftSide) -1] == 'a'):
                    a = a +  (float(leftSide[:len(leftSide) -1]) ) 
                elif(leftSide[len(leftSide) -1] == 'b'):
                    b = b + (float(leftSide[:len(leftSide) -1] )) 
                else :
                    c = c + (float(leftSide)) 
                break

        while True :
            plus = rightSide.find("+")
            minus = rightSide.find("-")
            if(plus == 0) :
                plus = rightSide.find("+", 1)
            if(minus == 0) :
                minus = rightSide.find("-", 1)
            if(plus < minus and plus > 0) :
                if(rightSide[plus-1] == 'a'):
                   a = a +  (float(rightSide[:plus -1]) ) * (-1)
                elif(rightSide[plus-1] == 'b'):
                    b = b + (float(rightSide[:plus -1]) ) * (-1)
                else :
                    c = c + (float(rightSide[:plus]) ) * (-1)
                rightSide = rightSide[plus:]
            if( minus == -1 and plus > 0) :
                if(rightSide[plus-1] == 'a'):
                    a = a +  (float(rightSide[:plus -1]) ) * (-1)
                elif(rightSide[plus-1] == 'b'):
                    b = b + (float(rightSide[:plus -1]) ) * (-1)
                else :
                    c = c + (float(rightSide[:plus]) ) * (-1)
                rightSide = rightSide[plus:]
            elif(plus > minus and minus > 0) :
                if(rightSide[minus-1] == 'b'):
                    b = b + (float(rightSide[:minus -1]) ) * (-1)
                else :
                    c = c + (float(rightSide[:minus]) ) * (-1)
                rightSide = rightSide[minus:]
            elif(minus == plus and minus != -1) :
                if(rightSide[minus -1] == 'a'):
                   a = a +   (float(rightSide[:minus -1])) * (-1)
                elif(rightSide[minus -1] == 'b'):
                    b = b + (float(rightSide[:minus -1]) ) * (-1)
                else :
                    c = c + (float(rightSide[:minus] )) * (-1)
                rightSide = rightSide[minus:]
            elif(minus > 0 and plus == -1) :
                if(rightSide[minus -1] == 'a'):
                    a = a +  (float(rightSide[:minus -1])) * (-1)
                elif(rightSide[minus -1] == 'b'):
                    b = b + (float(rightSide[:minus -1]) ) * (-1)
                else :
                    c = c + (float(rightSide[:minus] )) * (-1)
                rightSide = rightSide[minus:]
            elif( plus > 0 and minus == -1) :
                if(rightSide[plus -1] == 'a'):
                    a = a +  (float(rightSide[:plus -1])) * (-1)
                elif(rightSide[plus -1] == 'b'):
                    
                    b = b + (float(rightSide[:plus -1]) ) * (-1)
                else :
                    c = c + ((float(rightSide[:plus] )) * (-1))
                rightSide = rightSide[plus:]
            elif (minus == -1 and plus == -1) :
                if(rightSide[len(rightSide) -1] == 'a'):
                    a = a +  (float(rightSide[:len(rightSide) -1])) * (-1)
                elif(rightSide[len(rightSide) -1] == 'b'):
                    b = b + (float(rightSide[:len(rightSide) -1] )) * (-1)
                else :
                    c = c + (float(rightSide)) * (-1)  
                break
        if a % 2 == 0:
            a = int(a)
        if b % 2 == 0:
            b = int(b)
        if c % 2 == 0:
            c = int(c)
        if (digree2 == 2) :
            reduced = "Reduced form: " + str(a)+ " * X^2 " 
            if b > -1:
                reduced += " + " + str(b)+" * X^1 "
            else:
                 reduced +=  str(b)+" * X^1 "
            if c > -1:
                reduced += " + " + str(c)+" * X^0 = 0"
            else:
                 reduced +=  str(c)+" * X^0 = 0"
            print(reduced)
            print("Digree : "+ str(digree2))
            print("Discriminant is strictly positive, the two solutions are:")
            f = (b * b) - (4 * (a * c))
            if(f < 0) :
                 print("No Real Solution")
                 exit()
            x =  ((-1 * b) + float(my_root(f))) / (2*a)
           
            print(x)
            f = (b * b) - (4 * (a * c))
            if(f < 0) :
                print("No Real Solution")
                exit()
            x =  ((-1 * b) - float(my_root(f))) / (2*a)
            print(x)
            exit()
        elif (digree == 1):
            reduced = "Reduced form: " + str(b)+ " * X^1 " 
            if c > -1:
                reduced += " + " + str(c)+" * X^0 = 0"
            else:
                 reduced +=  + str(c)+" * X^0 = 0"
            print(reduced)
            print("Digree : "+ str(digree))
            print("the solution is:")
            x = c / (-1* b)
            print(x) 
            exit()
toSolve = toSolve.replace(" ", "")
st = toSolve.split("=")
if(st[0].find(st[1]) == -1) :
    print("there are no solutions")
else :
    print("all real numbers are the solution")