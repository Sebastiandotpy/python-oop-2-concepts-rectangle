from check import print_rectangle_properties
from rectangle import Rectangle

def main():
    rectangle1 = Rectangle(9.0, 12.0)
    rectangle2 = Rectangle(17.0, 13.0)

    print_rectangle_properties(rectangle1)
    print_rectangle_properties(rectangle2)

if __name__ == "__main__":
    main()
