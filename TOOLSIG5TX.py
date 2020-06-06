import re, termcolor, requests, os, sys
from termcolor import colored
import var_animate
from tqdm import tqdm
os.system('clear')
class gaje:
	def __init__(self):
		self.req = requests.Session()
		self.header = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.1; CPH1605) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36"}
		self.banner()
	def banner(self):
		ga = var_animate.banner('TOOLS IG','ABIN XD.5TX','0.1')
		print(ga)
		print(colored("Instagram : abinayanafaiq",'white'))
		print(colored("Youtube : BENJAMIN ID",'green'))
		print(colored("Github : https://github.com/abinayanafaiq",'blue'))
		print(colored("[!]======================================================[!]",'yellow'))
		print(colored("[1].Download Dp Instagram",'red'))
		print(colored("[2].Download Image Post",'green'))
		print(colored("[3].Download Video Post",'blue'))
		gan = input(colored("PILIH:",'blue'))
		if gan == "1":
			hayyuk = input(colored("Username IG  : ",'white'))
			gass = self.req.get('https://www.instadp.com/fullsize/'+hayyuk,headers=self.header)
			pe = input(colored("SIMPAN DI? EX /sdcard/",'red'))
			print(colored("WAIT",'red'))
			ga = self.req.get(re.search(r'class="picture" src="(.*)"',gass.text).group(1), stream=True)
			progres = tqdm(total=int(ga.headers.get('content-length', 0)), unit='B', unit_scale=True)
			with open(pe+hayyuk+'.png', 'wb') as f:
				for data in ga.iter_content(1024):
					progres.update(len(data))
					f.write(data)
					progres.close()
			print(colored("Oke File Tersimpan di memori internal",'red'))
			self.banner()
gaje()