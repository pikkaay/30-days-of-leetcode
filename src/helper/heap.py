# heap


class Heap:
    def __init__(self,lis,n):
        self.length=n          #size of heap
        self.heap=[None]*(n+1) #intialize an empty list
        self.last=0            #index where the last item was inserted
        for x in lis:
            self.heap_insert(x)

    def heap_insert(self,item):
        self.last+=1             
        if self.last<=self.length:
            self.heap[self.last]=item
        else:
            self.length+=1            #if the heap is already full
            self.heap+=[None]
            self.heap[self.last]=item
        self.bubble_up()
        
    def bubble_up(self):
        """
        Find appropriate location for the item being inserted
        that satisy either min-heap or max-heap property
        O(Lg N) operation
        Min-heap: self.heap[parent]>self.heap[current]
        Max-heap: self.heap[parent]<self.heap[current]
        """
        parent=self.last/2
        current=self.last
        while self.heap[parent]>self.heap[current] and parent>0:  #for min-heap
            self.heap[parent],self.heap[current]=self.heap[current],self.heap[parent]
            current=parent
            parent=parent/2
    def extract_minmax(self):
        if self.length>=1:
            minn=self.heap[1]         
            self.length-=1
            self.heap[1],self.heap[self.last]=self.heap[self.last],self.heap[1]  #swap root with last element
            self.last-=1               #decrement length
            self.heap.pop(-1)          #pop the root that was moved to the last element
            if self.length>1:          #coz first item is None
                if self.length<=2:
                    self.heap[1:]=sorted(self.heap[1:]) #use reverse=True for max-heap
                else:
                    self.bubble_down()
            return minn
    def bubble_down(self):
        """
        After removal of the root this operation is 
        done to maintain the heap property, called Heapify.
        O(log N) operation.
        """
        current=1
        child1=current*2
        child2=(current*2)+1
        while True:
            if child1<=self.length and child2<=self.length and ( current <=(self.length/2) and
                                (self.heap[current] > self.heap[child1] or self.heap[current] > self.heap[child2]) ):
                """
                If both children indexes are within self.length
                """
                #use max for max-heap
                #find the index of the element largest of the three
                #current element and two children
                ind=min((child1,child2),key=lambda x:self.heap[x])
                self.heap[current],self.heap[ind]=self.heap[ind],self.heap[current]
                current=ind
                child1=current*2
                child2=(current*2)+1
            elif child1==self.length  and (current <=(self.length/2) and (self.heap[current] > self.heap[child1])):
                """
                if child1 is the last element in the heap
                """
                self.heap[current],self.heap[ind]=self.heap[ind],self.heap[current]
                break
            else:
                """
                If none of the children indexes lie withing self.length
                """
                break