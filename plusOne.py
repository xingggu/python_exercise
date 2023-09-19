class Solution:
    """
    在不考虑0置首位，考虑999，9等情况，转换为string更方便计算
    """
    def plusOne(self, digits: List[int]) -> List[int]: 
        to_str = ""
        to_str = "".join([str(i) for i in digits])
        to_int = int(to_str)+1
        digits = [int(digit) for digit in str(to_int)]
        return digits
