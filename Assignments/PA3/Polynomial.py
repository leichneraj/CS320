
class Polynomial:
    zero=0
    
    # coef is a list of coefficients
    # creates a polynomial of degree n-1
    def __init__(self,coef):
        self.coef=coef
        self.n=len(self.coef)
    
    # tostring
    def __repr__(self):
        return f"Polynomial: {self.n} {self.coef}"

    # overloads [] operator (allows indexing and slicing of coef list)
    # e.g. `poly[i]` or `poly[i:j]`
    def __getitem__(self,i):
        return self.coef[i]

    # overloads (==) operator
    # e.g. `poly1==poly2` or `poly1!=poly2`
    def __eq__(self,other):
        if not isinstance(other,self.__class__) or self.n!=other.n:
            return False
        eq_coef = [self[i]==other[i] for i in range(self.n)]
        return all(eq_coef)
    
    # overloads (+) operator
    # e.g. `poly1+poly2`
    # poly1 and poly must be same length
    def __add__(self,other):
        assert(isinstance(other,self.__class__))
        assert(self.n==other.n)

        add_coef=[]
        # STUDENT_CODE: Implement addition for two polynomials of the same length
        for i in range(len(self)) :
            add_coef[i] = self[i] + other[i]
        
        return self.__class__(add_coef)

    # overloads (-) operator
    # e.g. `poly1-poly2`
    # poly1 and poly2 must be same length
    def __sub__(self,other):
        assert(isinstance(other,self.__class__))
        assert(self.n==other.n)
    
        sub_coef=[]
        # STUDENT_CODE: Implement subtraction for two polynomials of the same length
        for i in range(len(self)) :
            sub_coef[i] = self[i] - other[i]

        return self.__class__(sub_coef)
 
    # overloads (*) operator
    # e.g. `poly1*poly2`
    # poly1 and poly2 must be same length, and length must be power of 2
    def __mul__(self,other):
        assert(isinstance(other,self.__class__))
        assert(self.n==other.n)
        
        if self.n==1:
            base_coef=[]
            
            # STUDENT_CODE: implement base case

            return self.__class__(base_coef)

        assert(self.n%2==0)
        n=self.n
        half=self.n//2

        a_coef=[]
        b_coef=[]
        c_coef=[]
        d_coef=[]

        # STUDENT_CODE: assign the correct values to {a,b,c,d}_coef

        a=self.__class__(a_coef)
        b=self.__class__(b_coef)
        c=self.__class__(c_coef)
        d=self.__class__(d_coef)

        # STUDENT_CODE: implement Karatsuba's algorithm using a,b,c,d
        
        mul_coef_len=0 # STUDENT_CODE: replace with the correct mul_coef_len

        mul_coef=[self.__class__.zero for i in range(mul_coef_len)]

        # STUDENT_CODE: combine results of Karatsuba's algorithm to compute mul_coef
            
        return self.__class__(mul_coef)

    # O(n^2) implementation of polynomial multiplication
    # use for testing
    def convolution(self,other):
        assert(isinstance(other,self.__class__))
        assert(self.n==other.n)

        n=self.n
        
        mul_coef=[self.__class__.zero for i in range(2*n-1)]
        for i in range(n):
            for j in range(i+1):
                mul_coef[i]+=self[j]*other[i-j]
        for i in range(n,2*n-1):
            for j in range(i-n+1,n):
                mul_coef[i]+=self[j]*other[i-j]
            
        return self.__class__(mul_coef)

    def test_mul(self,other):
        assert(isinstance(other,self.__class__))
        assert(self.n==other.n)

        conv=self.convolution(other)
        mul=self*other

        assert conv==mul, f"convolution and __mul__ are not equal on inputs:\n  p: {self}\n  q: {other}\n  conv:  {conv}\n  mul:   {mul}"

    

if __name__=="__main__":
    p=Polynomial([1,2,3,4])
    q=Polynomial([3,4,5,6])

    print(p*q)
    Polynomial.test_mul(p,q)
