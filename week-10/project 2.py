class calculations():
    def trapezium(self):
        h = float(input("Input height: "))
        base1 = float(input("Input base1: "))
        base2 = float(input("Input base2: "))
        area_of_trapezium = h / 2 * (base1 * base2)
        print("Area of Trapezium = ", area_of_trapezium)
    def rhombus(self):
        diagonal1 = float(input("First diagonal: "))
        diagonal2 = float(input("Second diagonal: "))
        area_of_rhombus = 1 / 2 * (diagonal1 * diagonal2)
        print("Area of Rhombus = ", area_of_rhombus)
    def parallelogram(self):
        base = float(input("base: "))
        altitude = float(input("Altitude: "))
        area_of_parallelogram = base * altitude
        print("Area of parallelogram = ", area_of_parallelogram)
    def cube(self):
        length = float(input("length:"))
        Area = 6 * (length)  ** 2
        print("Area of cube = ", Area)
    def cylinder(self):
        radius = float(input("radius: "))
        height = float(input("height: "))
        Area = 3.124 * ((radius) ** 2) * height
        print("Area of cylinder = ", Area)

C = calculations()
Input = int(input("Area Calculator"
              "\n1.Trapezium"
              "\n2.Rhombus"
              "\n3.Parallelogram"
              "\n4.Cube"
              "\n5.Cylinder: "))
if Input == 1:
    C.trapezium()
elif Input == 2:
    C.rhombus()
elif Input == 3:
    C.parallelogram()
elif Input == 4:
    C.cube()
elif Input == 5:
    C.cylinder()
else:
    print("Invalid Input")