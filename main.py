# TRIANGLE
import time
input1 = int(input("Enter the base: "))
input2 = int(input("Enter the height: "))    
def area_of_triangle(base,height):
    area = base * height / 2
    print("Calculating the area...")

    time.sleep(2.5)
    return area
    

triangle = area_of_triangle(input1,input2)

"""If the area is greater than 10000"""
# if triangle > 1000:
#     triangle = input1 - input2
#     c = str(triangle)
#     print("The number is " + c)
# else:
#     c = str(triangle)
#     print("The number is " + c)
c = str(triangle)
print("The number is " + c)
# Circle
radious = int(input("Enter your radious: "))
def area_of_circle(radius):
    """Area of a circle"""
    area = radius * radious * 3.142
    print("Calculating area...")
    time.sleep(2)
    return area
circle = area_of_circle(radious)
c = str(circle)
print("The area of the circle is " + c)

# Area of rectangle
input1 = int(input("Enter the length: "))
input2 = int(input("Enter the width: "))

def area_of_rectangle(lenght,width):
    area = lenght * width
    print("Calculating the area...")

    time.sleep(2.5)
    # print(square)
    return area

rectangle = area_of_rectangle(input1,input2)
c = str(rectangle)
print("The number is " + c)




