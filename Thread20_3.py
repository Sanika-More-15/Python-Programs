import threading

def EvenList(arr):
    even=[]
    sum=0
    for i in arr:
        if i % 2 ==0:
            even.append(i)
            sum=sum+i
  
    print("even list :",even)
    print("Sum of even list :",sum)
            

def OddList(arr):
    odd=[]
    sum=0
    for i in arr:
        if i % 2 ==1:
            odd.append(i)
            sum=sum+i
    
    print("odd list :",odd)
    print("Sum of odd list :",sum)

List=list(map(int,input("Enter numbers :").split()))    

if __name__=="__main__":
    
    t1=threading.Thread(target=EvenList,args=(List,))
    t2=threading.Thread(target=OddList,args=(List,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main thread")