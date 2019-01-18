# coding=utf-8

from idaapi import *
import time

symbol_interval = 16 # 符号表间隔
load_address = 0x10000 # 加载基址
symbol_table_start = 0x301e60 + load_address
symbol_table_end = 0x3293b0 + load_address
ea = symbol_table_start

# rebase 程序到加载基址
rebase_program(load_address, 0x0008)

# ida自动分析
autoWait()

while ea < symbol_table_end:
	offset = 4 # 4字节为一组数据
	# 函数名指针转换为字符串
	MakeStr(Dword(ea + offset), BADADDR)
	# 函数名变量赋值
	sName = GetString(Dword(ea + offset), -1, ASCSTR_C)
	print(sName)
	if sName:
		# 修复函数名
		eaFunc = Dword(ea + offset + 4)
		MakeName(eaFunc, sName)
		MakeCode(eaFunc)
		MakeFunction(eaFunc, BADADDR)
	ea = ea + symbol_interval