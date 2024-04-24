#write a program that asks the user for a geometric shape from a list
#("rectangle/triangle/circle/sphare/cube/pyramid")
#than asks for measurements and units of said shape
#list of acceptable units ("inch/feet/mile/yard/meter")
#the program than converts all of the given units to meters
#calculates the area,circumference and volume of the shape if it has any
#than prints the measurments and calculation results

#unit converter

from math import pi
unitlist=("inch/feet/mile/yard/meter")
print("supported units are (inch/feet/mile/yard/meter)")
def unitfix(unit):
    if "inch" in unit.keys():
        meter=(unit.get("inch"))/39.37
        return meter
    
    elif "feet" in unit.keys():
        meter=(unit.get("feet"))/3.281
        return meter 
        
    elif "mile" in unit.keys():
        meter=(unit.get("mile"))*1609
        return meter
    
    elif "yard" in unit.keys():
        meter=(unit.get("yard"))/1.094
        return meter

    else:
        print("unkown unit")
        quit()

#result output function
def results2d(results):
    print("**********************************")
    for i,j in results.items():
        print(shape2d ,i,"is:",j,"m")
    print("**********************************")

def results3d(results):
    print("**********************************")
    for i,j in results.items():
        print(shape3d ,i,"is:",j,"m")
    print("**********************************")

#rectangle function
def rectform():
    print("**********************************")
    measurment={"length":0,"width":0,"area":0,"":0}
    #length
    length=float(input("enter " +shape2d+ " length: "))
    unit=input("enter measuring unit\n"
               +unitlist+": ")
    if unit !="meter":
        length={unit:length}
        length=(unitfix(length))
    measurment.update({"length":length})
    print("**********************************")
    #width
    width=float((input("enter " +shape2d+ " width: ")))
    unit=input("enter measuring unit\n"
               +unitlist+": ")
    if unit !="meter":
        width={unit:width}
        width=(unitfix(width))
    measurment.update({"width":width})
    
    #area and circumference
    measurment.update({"area":(length*width)})
    measurment.update({"circumference":(2*length+2*width)})

    #results
    results2d(measurment)

#triangle function
def triform():
    print("**********************************")
    measurment={"base":0,"height":0,"area":0,"circumference":0}
    #base
    base=float(input("enter triangle base: "))
    unit=input("enter measuring unit\n"
               +unitlist+": ")
    if unit !="meter":
        base={unit:base}
        base=(unitfix(base))
    measurment.update({"base":base})
    print("**********************************")
    #heigh
    height=float((input("enter tritangle height: ")))
    unit=input("enter measuring unit\n"
               +unitlist+": ")
    if unit !="meter":
        height={unit:height}
        height=(unitfix(height))
    measurment.update({"height":height})
    
    #area and circumference
    measurment.update({"area":((height*base)/2)})
    measurment.update({"circumference":(base*3)})

    #results
    results2d(measurment)

#circle
def cirform():
    print("**********************************")
    measurment={"radius":0,"area":0,"circumference":0}
    
    radius=float(input("enter circle radius: "))
    unit=input("enter measuring unit\n"
               +unitlist+": ")
    if unit !="meter":
        radius={unit:radius}
        radius=(unitfix(radius))
    measurment.update({"radius":radius})
    print("**********************************")
    
    #area and circumference
    measurment.update({"area":(pi*(radius**2))})
    measurment.update({"circumference":(2*pi*radius)})

    #results
    results2d(measurment)

#sphere
def sphform():
    print("**********************************")
    measurment={"radius":0,"area":0,"volume":0}
    
    radius=float(input("enter sphere radius: "))
    unit=input("enter measuring unit\n"
               +unitlist+": ")
    if unit !="meter":
        radius={unit:radius}
        radius=(unitfix(radius))
    measurment.update({"radius":radius})
    print("**********************************")
    
    #area, circumference and volume
    measurment.update({"area":(4*pi*(radius**2))})
    measurment.update({"volume":((4*pi*(radius**3))/3)})

    #results
    results3d(measurment)


#cube
def cubeform():
    print("**********************************")
    measurment={"length":0,"width":0,"height":0,"area":0,"volume":0}
    length=float(input("enter cube length: "))
    unit=input("enter measuring unit\n"
               +unitlist+": ")
    if unit !="meter":
        length={unit:length}
        length=(unitfix(length))
    measurment.update({"length":length})
    print("**********************************")
    
    width=float((input("enter cube width: ")))
    unit=input("enter measuring unit\n"
               +unitlist+": ")
    if unit !="meter":
        width={unit:width}
        width=(unitfix(width))
    measurment.update({"width":width})
    print("**********************************")

    height=float((input("enter cube height: ")))
    unit=input("enter measuring unit\n"
               +unitlist+": ")
    if unit !="meter":
        height={unit:height}
        height=(unitfix(height))
    measurment.update({"height":height})
    
    #area, circumference and volume
    measurment.update({"area":(2*(height+width+length))})
    measurment.update({"volume":(height*width*length)})

    #results
    results3d(measurment)

def pyrform():
    print("**********************************")
    measurment={"baselength":0,"basewidth":0,"height":0,'slantheight':0,"area":0,"volume":0}
    baselength=float(input("enter pyramid base length: "))
    unit=input("enter measuring unit\n"
               +unitlist+": ")
    if unit !="meter":
        baselength={unit:baselength}
        baselength=(unitfix(baselength))
    measurment.update({"baselength":baselength})
    print("**********************************")
    
    basewidth=float((input("enter pyramid base width: ")))
    unit=input("enter measuring unit\n"
               +unitlist+": ")
    if unit !="meter":
        basewidth={unit:basewidth}
        basewidth=(unitfix(basewidth))
    measurment.update({"basewidth":basewidth})
    print("**********************************")

    height=float((input("enter pyramid height: ")))
    unit=input("enter measuring unit\n"
               +unitlist+": ")
    if unit !="meter":
        height={unit:height}
        height=(unitfix(height))
    measurment.update({"height":height})

    print("**********************************")

    slantheight=float((input("enter pyramid slantheight: ")))
    unit=input("enter measuring unit\n"
               +unitlist+": ")
    if unit !="meter":
        slantheight={unit:slantheight}
        slantheight=(unitfix(slantheight))
    measurment.update({"slantheight":slantheight})
    
    #area, circumference and volume
    basecir=((2*baselength)+(2*basewidth))
    basearea=(baselength*basewidth)
    measurment.update({"area":((basearea)+((basecir*slantheight)/2))})
    measurment.update({"volume":((height*basewidth*baselength)/3)})

    #results
    results3d(measurment)


def formula2d(shape2d):
    if shape2d == "rectangle":
        rectform()

    elif shape2d == "triangle":
        triform() 

    elif shape2d == "circle":
        cirform()

#3d shape formula
def formula3d(shape3d):  
    if shape3d == "cube":
        cubeform()

    elif shape3d == "sphere":
        sphform()

    elif shape3d == "pyramid":
        pyrform()


shapetype=input("what type of deometric shape do yo have in mind?(2d/3d): ")
shape2dlist=("rectangle/triangle/circle")
shape3dlist=("sphare/cube/pyramid")
print("******************************************")
if shapetype == "2d":
    shape2d=input("enter a 2d shape \n" +shape2dlist+ ": ")
    formula2d(shape2d)

elif shapetype == "3d":
    shape3d=input("enter a 3d shape \n" +shape3dlist+ ": ")
    formula3d(shape3d)
    
    

#if (input("do you want to convert your result units? (y/n)"))=="y":
    #unitcon(measurement)