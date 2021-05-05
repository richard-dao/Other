# Python
class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        productDigits = 1
        sumDigits = 0
        temp = n
        
        while(temp != 0):
            productDigits = productDigits * (temp % 10)
            sumDigits = sumDigits + (temp % 10)
            temp = temp/10
        return productDigits - sumDigits
