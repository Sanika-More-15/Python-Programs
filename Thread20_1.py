import threading

def Even():
    for i in range(1,11):
        if i % 2 ==0:
            print("Even :",i)

def Odd():
    for i in range(1,11):
        if i % 2 ==1:
            print("Odd :",i)
    

if __name__=="__main__":
    
    t1=threading.Thread(target=Even)
    t2=threading.Thread(target=Odd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main thread")