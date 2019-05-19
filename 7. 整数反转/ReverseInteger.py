class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp=0
        if x==0:
            return 0
        elif x<0:
            x=abs(x)
            length=len(str(x))
            while length>0:
               temp=temp+(x%10)*pow(10,length-1)
               x=x//10
               length-=1
            temp=-1*temp
        elif x>0:
            x=abs(x)
            length=len(str(x))
            while length>0:
               temp=temp+(x%10)*pow(10,length-1)
               x=x//10
               length-=1
        if temp<2147483647 and temp>-2147483648:
            return temp
        else:
            return 0
