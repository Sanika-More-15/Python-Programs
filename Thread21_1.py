import threading

def Prime(no):
    for i in range(2,no):
        if no % i ==0:
            return
    print("Prime No")

def NonPrime(no):
    for i in range(2,no):
        if no % i ==0:
            print("Not Prime No")
            return

num=int(input("Enter any number :"))

if __name__=="__main__":
    
    t1=threading.Thread(target=Prime, args=(num,))
    t2=threading.Thread(target=NonPrime,args=(num,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    print("End of main thread")

