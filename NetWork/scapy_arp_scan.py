#coding=utf-8

#����������ɨ����  ʹ��ARPɨ��
#����ɨ��,��������д����,���������д��ݵĲ�����
from scapy.all import *
import time
wifi="Intel(R) Ethernet Connection (2) I219-LM"
#�������ݰ�   Ether()�����ʡ�Թ�������,��ΪĬ�Ͼ���,��Ȼ����д��,���Լӿ��ٶ�
ip=sys.argv[1]
p=Ether(dst="ff:ff:ff:ff:ff:ff",src="b8:81:98:e0:46:6a")/ARP(pdst=ip)
#���ݰ�����,srpͬʱ�յ���Ӧ���ݰ��Ͳ���Ӧ���ݰ�,��Ҫ���������������ա�
#ans������������Ӧ,unansֻ������û����Ӧ
ans,unans=srp(p,iface=wifi,timeout=2)
print("һ��ɨ�赽��%d������"%len(ans))
result=[]
#ans��Ԫ�����ʽ,���Բ���ans[0],���ֽ����Ԫ�����ʽ
for s,r in ans:
    result.append([r[ARP].psrc,r[ARP].hwsrc])   #��Ŀ���IP�Լ�MAC��ַ���뵽�µ��б�

result.sort()   #���б��������
#�����б�,��ӡip�Լ���Ӧ��mac��ַ
for ip,mac in result:
    print(ip,"--->",mac)