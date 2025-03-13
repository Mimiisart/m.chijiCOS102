#simple interest
option=int(input("what do you want to calculate:\n press '1' for Simple interest\n press '2' for compound interest\n press '3' for annuity plan\n: "))


if option==1:
    p=float (input('Enter p: '))
    r =float(input('Enter r: '))
    t = float (input('Enter t: '))
    A=p * (1+(r/100)*t)
    print('simple interest is', A )

elif option ==2:
    p=float (input('Enter p: '))
    r =float(input('Enter r: '))
    t = float (input('Enter t: '))
    n=float (input('Enter n: '))
    A=p * (1+(r/n)**n*t)
    print('Compound interest is', A )

elif option ==3:
    p=float (input('Enter p: '))
    r =float(input('Enter r: '))
    t = float (input('Enter t: '))
    n=float (input('Enter n: '))
    m =float (input('Enter m: '))
    A=p * m * t * ((1+(r/n))**n*t-1/(r/n))
    print('Annuity plan is', A )

