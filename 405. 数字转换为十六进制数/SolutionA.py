class Solution:
    def toHex(self, num: int) -> str:
        dic={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        if num==0:
            return '0'
        s=(bin(((1 << 32) - 1) & num)[2:]).zfill(32)
        res=''
        for i in range(0, 29, 4):
            tmp = int(s[i: i + 4], 2)
            if not tmp and (not res):
                continue
            res+=dic[int(s[i:i+4],2)]
        return res