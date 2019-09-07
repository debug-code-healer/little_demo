#普通二维码

'''
#命令行执行
>myqr http://sqdxwz.com
'''

'''
#-n ：自定义二维码的名称
#-d : 自定义二维码的路径
#命令行执行
>myqr http://sqdxwz.com -n Python3X.jpg -d E:\
'''

'''
#-v ：定义二维码的大小，范围为 1 ~ 40，默认大小取决于输入的内容。
#-l ： 定义二维码纠错率，也就是说二维码被遮挡一部分仍然被识别出来，有四个等级，分别是L(7%)、M(15%)、Q(25%)、H(30%)。默认情况是最高等级的H
#命令行执行
>myqr http://sqdxwz.com  -v 10 -l M
'''


#艺术二维码

'''
#-p：加背景图(黑白色)
#命令行执行
>myqr http://sqdxwz.com -p peiqi.jpg
'''

'''
#-c：彩色背景图
#命令行执行
>myqr http://sqdxwz.com -p peiqi.jpg -c

-con：修改图片的对比度，默认值为1.0
-bri ：修改图片的亮度，默认值也为1.0
'''

#动态二维码
'''
#命令行执行
>myqr http://sqdxwz.com -p pig.gif -n Python3X.gif -c

'''
