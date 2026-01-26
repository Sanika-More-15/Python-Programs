import threading

def Thread1(lst):
    total=0
    for no in lst:
        total=total + no 
    print("Sum of elements :",total)    
    
            
def Thread2(lst):
    prod=1
    for no in lst:
        prod=prod * no
    print("Product of elements :",prod)  
    

List=list(map(int,input("Enter numbers :").split()))    

if __name__=="__main__":
    
    t1=threading.Thread(target=Thread1,args=(List,))
    t2=threading.Thread(target=Thread2,args=(List,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main thread")