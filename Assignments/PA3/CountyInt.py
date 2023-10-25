from Polynomial import Polynomial

class CountyInt:
    def __init__(self,val,add_count,sub_count,mul_count):
        self.val=val
        self.add_count=add_count
        self.sub_count=sub_count
        self.mul_count=mul_count

    @staticmethod
    def from_int(val):
        return CountyInt(val,0,0,0)

    def combine_counts(self,other):
        return self.add_count+other.add_count, self.sub_count+other.sub_count, self.mul_count+other.mul_count
    
    def __add__(self,other):
        assert(isinstance(other,CountyInt))
        ci = CountyInt(self.val+other.val,*self.combine_counts(other))
        ci.add_count+=1
        return ci

    def __sub__(self,other):
        assert(isinstance(other,CountyInt))
        ci = CountyInt(self.val-other.val,*self.combine_counts(other))
        ci.sub_count+=1
        return ci

    def __mul__(self,other):
        assert(isinstance(other,CountyInt))
        ci = CountyInt(self.val*other.val,*self.combine_counts(other))
        ci.mul_count+=1
        return ci

    def rep(self):
        return (self.val,self.add_count,self.sub_count,self.mul_count)

    def __repr__(self):
        return str(self.rep())
    
    def __eq__(self,other):
        assert(isinstance(other,CountyInt))
        return self.rep()==other.rep()

def CountyPolynomial(Polynomial):
    zero=CountyInt(0,0,0,0)

    # this breaks mul_test, because convolution and __mul__ are no longer equal    
