
def insertion_Sort(A): #מיון הכנסה
    for i in range(len(A)):
        min_index = i
        for j in range(i, len(A)):
            if A[j] < A[min_index]:
                A[j], A[min_index] = A[min_index], A[j]
    return A

def bucket_sort(A):
    print(A)
    B = [[] for i in range(0, len(A))]
    print(B)
    for i in A:
        B[(int(i * len(A)))].append(i)
    for i in B:
        insertion_Sort(i)
    C = []
    for i in B:
        for j in i:
            C.append(j)
    print(C)



#stack -- FILO
class stack:
    def __init__(self):
        self.top = 0
        self.st = []

    def is_empty(self): #האם מחסנית ריקה
        return len(self.st) == 0

    def push(self, value): #הכנסה
        self.st.append(value)
        self.top += 1

    def pop(self): #הוצאה
        while not self.is_empty():
            x = self.st.pop()
            self.top -= 1
            return x

    def peek(self): #מה יש בtop
        return self.top

#queue -- FIFO
class queue:
    def __init__(self, n = 5):
        self.head = 0
        self.tail = 0
        self.Q = [] * n

    def get_size(self):
        return len(self.Q)

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.tail+1) % self.get_size() == self.head

    def enqueue(self, value):
        while not self.is_full():
            self.Q.append(value)
            self.tail += 1

    def dequeue(self):
        x = self.Q.pop()
        return x

    def print1(self):
        for i in range(0, len(self.Q)):
            print(self.Q[i])


def main():
    '''
    #  A = [0.4, 0.3, 0.8, 0.51, 0.5, 0.73, 0.17, 0.52]
    B = [0.1, 0.9, 0.032, 0.3, 0.5, 0.23, 0.5, 0.1, 0.7]

    bucket_sort(B)
   st = stack()
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    st.push(5)
    st.push(8)
    print(st.st)
    st.peek()

    print(st.pop())
    print(st.pop())
    print(st.pop())
    print(st.pop())
    print(st.pop())
    print(st.pop())
    '''

    q = queue()
    q.enqueue(4)
    #q.enqueue(3)
    #q.enqueue(2)
    #queue.get_size()
    '''
    queue1.dequeue()
    queue1.enqueue(32)
    queue1.enqueue(331)

    queue1.print1()
    '''





if __name__ == '__main__':
    main()

