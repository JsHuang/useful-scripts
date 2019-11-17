#coding=utf-8

#局域网主机扫描器  使用ARP扫描
#主机扫描,主机不是写死的,接收命令行传递的参数。
from scapy.all import *
import time
wifi="Intel(R) Ethernet Connection (2) I219-LM"
#构造数据包   Ether()层可以省略构造内容,因为默认就是,当然可以写上,可以加快速度
ip=sys.argv[1]
p=Ether(dst="ff:ff:ff:ff:ff:ff",src="b8:81:98:e0:46:6a")/ARP(pdst=ip)
#数据包发送,srp同时收到响应数据包和不响应数据包,需要用两个变量来接收。
#ans中有请求有响应,unans只有请求没有响应
ans,unans=srp(p,iface=wifi,timeout=2)
print("一共扫描到了%d个主机"%len(ans))
result=[]
#ans是元组的形式,可以测试ans[0],发现结果是元组的形式
for s,r in ans:
    result.append([r[ARP].psrc,r[ARP].hwsrc])   #把目标的IP以及MAC地址加入到新的列表

result.sort()   #对列表进行排序
#遍历列表,打印ip以及对应的mac地址
for ip,mac in result:
    print(ip,"--->",mac)