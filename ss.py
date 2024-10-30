from typing import List
def Solutions(self, A: List[int]) -> List[int]:
    i=1
    for i in range(len(A)):
        temp = 0
        if(A[i-1]==0):
            A[i-1], A[i] = A[i], A[i-1]
    return A
B = [2,4,5,0,2,3,4,0]
print(Solutions[B])            