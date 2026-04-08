queue=[]
while True:
    print("\n queue operation menu")
    print("1.enqueue")
    print("2.dequeue")
    print("3.front")
    print("4.rear")
    print("5.isempty")
    print("6.display")
    print("7.exit")
    choice=int(input("enter choice:"))
    if choice == 1:
        val=int(input("enter value:"))
        queue.append(val)
        print("enqueued:",val)
    elif choice==2:
        if len(queue)==0:
            print("Queue underflow")
        else:
            print("Dequeued:",queue.pop(0))
    elif choice==3:
        if len(queue)==0:
            print("queue is empty")
        else:
            print("front elemnt:",queue[0])
    elif choice==4:
        if len (queue)==0:
            print("queue id empty")
        else:
            print("rear element:",queue[-1])
    elif choice==5:
        print("is queue empty?",len(queue)==0)
    elif choice==6:
        print("queue:",queue)
    elif choice==7:
        break
else:
    print("invalid choice!")