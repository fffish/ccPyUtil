import socket
import re


def get_local_ip():
	# 创建一个UDP套接字
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		# 连接一个公共的IP地址和端口
		sock.connect(("8.8.8.8", 80))
		# 获取套接字的本地地址信息
		local_ip = sock.getsockname()[0]
	finally:
		# 关闭套接字
		sock.close()

	return local_ip


# linux的控制台输出颜色
# 示例：this is a [red] red color txt [-]
def print_color(txt):
	color_def = {
		"blue": "\033[34m",
		"green": "\033[32m",
		"yellow": "\033[33m",
		"red": "\033[31m",
	}
	colors = re.findall(r"\[(\w+)]", txt)
	for color in colors:
		if color in color_def:
			txt = re.sub(rf"\[{color}]", color_def[color], txt)
			txt = re.sub(r"\[-]", "\033[0m", txt)
	print(txt)
