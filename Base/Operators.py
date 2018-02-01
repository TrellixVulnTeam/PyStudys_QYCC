#######运算符#######

# 算术运算符
#   +  -  *  /  %   **(幂次，a**b为  a的b次方)  //（取整数）
a=2
b=4
print(a**b)  #2的4次方

c=20
d=3
print(c//d)  #20除3的结果整数

# 比较运算符
# ==  !=   >  <  >=  <=  (python2中<>表示不等于)
print(c!=d)

# 赋值运算符
#  =  +=  -=  *=  /=  %=  **=  //=
c*=a  # c=c*a

# 位运算符 把数字看作二进制来进行计算
'''
& 按位与运算符：参与运算的两个值如果两个相应位都为1，则该位的结果为1，否则为0
| 按位或运算符：只要对应的两个二进位有一个为1时，结果位就为1
^ 按位异或运算符：当两对应的二进位相异时，结果为1
~ 按位取反运算符：对数据的每个二进制位取反，即把1变为0，0变为1 ~x类似于 -x-1
<< 左移运算符：运算数的各二进位全部左移若干位，由<<右边的数字指定了移动的位数，高位丢弃，地位补0
>> 右移运算符：把"<<"左边的运算数的各二进位全部右移若干位，>>右边的数字指定了移动的位数
'''
q=60  #0011 1100
w=13  #0000 1101
print(q&w)  #12=0000 1100
print(q|w)  #61=0011 1101
print(q^w)  #49=0011 0001
print(~q)   #-61=1100 0011
print(q<<2) #240=1111 0000
print(q>>2) #15=0000 1111

#逻辑运算符
# and 布尔型的‘与’ or 布尔型的‘或’  not 布尔型的‘非’
print(a and b) #如果a and b为false，则返回b的值
print(a or b)  #如果a不是0，则返回a的值，否则返回b的值
print(not(a and b)) #a and b的 反值

#成员运算符
'''
in 如果在指定序列中可以找到值返回true，否则为false
not in 如果唉指定序列中找不到值返回true，否则返回false
'''
list=[1,2,3,5,6,7];
print(a in list)
print( b not in list)

#身份运算符
'''
is 判断两个标识符是否引用一个对象
is not 判断两个标识符是否引用自不同对象
'''
print(a is b)
print(a is not b)
'''
is 与 == 的区别： is用于判断两个变量引用对象是否为同一个，== 用于判断引用变量的值是否相等
类似传值和传址的区别
is判断是否指向内存中同一个地址块，我的电脑和你的电脑（是两台电脑）
==判断的是值是否相同，我的电脑和你的电脑（都是电脑）
'''
s=[1,2,3,4]
a=s
print(a is s)
print(a == s)
a=s[:]   #  s[:]=[s,s,None]  将s的全部内容替换给了[s,s,None],s没有变化，只是内容不一样了
print(a is s) #false
print(a == s)

#运算符优先级
'''
**	        指数 (最高优先级)
~ + -	    按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //	乘，除，取模和取整除
+ -	        加法减法
>> <<	    右移，左移运算符
&	        位 'AND'
^ |     	位运算符
<= < > >=	比较运算符
<> == !=	等于运算符
= %= /= //= -= += *= **=	赋值运算符
is is not	身份运算符
in not in	成员运算符
not or and	逻辑运算符
'''

