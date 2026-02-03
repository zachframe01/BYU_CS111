user_shape = input("enter a shape (circle, triangle, square, rectangle): ")

if user_shape == "circle":
    print("you picked a circle. I will give you the Area")
    radius = int(input("what is the radius? : "))
    r_squared = (radius*radius)
    Area = (r_squared*3.14)
    print(f"here is ther area of your shape! :", Area)

if user_shape == "triangle":
    print("you picked a triangle")
    height = int(input("what is the hight? : "))
    length = int(input("what is the length? : "))
    Area = (height*length*.5)
    print(f"here is ther area of your shape! :", Area)

if user_shape == "square":
    print("you picked a square")
    height = int(input("what is the hight? : "))
    Area = (height*2)
    print(f"here is ther area of your shape! :", Area)

if user_shape == "rectangle":
    print("you picked a rectangle")
    height = int(input("what is the hight? : "))
    length = int(input("what is the length? : "))
    Area = (height*length)
    print(f"here is ther area of your shape! :", Area)