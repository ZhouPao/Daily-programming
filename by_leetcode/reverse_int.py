#encoding:utf-8

__author__ = 'zhoupao'
__date__ = '2018/8/25 16:58'

class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 这里需要考虑到 -10~10之间
        if -10<x<10:
            return x
        # 把整数x转为字符串
        str_x=str(x)
        if str_x[0]!='-':
            #不是负号直接反转
            str_x = str_x[::-1]
            # str转为int
            x = int(str_x)
        else:
            # 是负号，则反转负号之后的字符串
            str_x = str_x[1:][::-1]
            # str转int
            x = int(str_x)
            # 加上负号
            x = -x
        # 三目运算符，判断是否溢出
        # 如果-2147483648 < x < 2147483647则返回x，否则返回0
        return x if -2147483648 < x < 2147483647 else 0


if __name__ == '__main__':
    s = Solution()
    reverse_int = s.reverse(-120)
    print(reverse_int)