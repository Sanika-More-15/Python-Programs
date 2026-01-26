# print 5 star [ Internally, Python does this: print("Hello", end="\n") ]

def Star():

    for i in range (1,6):
        print("*",end=" ") # end is a parameter of the print() function.
                           #It decides what is printed at the end of the line

Star()