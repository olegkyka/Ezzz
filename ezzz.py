import os
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
os.system('resize -s 24 80 > /dev/null')
#-----------------------------------------------------
def check():
	exst = str(os.path.exists('.agreement.txt'))
	if exst == "True":
		f = open(".agreement.txt","r")
		if f.mode =="r":
			contents = f.read()
			if contents[0] == "y" or contents[0] == "Y" or contents[0:3] == "yes" or contents[0:3] == "YES":
				os.system('python3 main.py')
			elif contents[0] == "n" or contents[0] == "N" or contents[0:3] == "no" or contents[0:3] == "NO":
				print(color.YELLOW+color.BOLD+"You need to accept agreement first to use the tool.\n"+color.END)
				os.system('rm -r .agreement.txt')
		f.close()
	else:
		os.system('clear')
		accept = input(color.RED+color.BOLD+"\nEzzz tool is only for testing, education purposes and can only be used where strict consent has been given. Any coincidence because of using this tool represents only and only result of your actions. The author does not hold any responsibility for the illegal/unethical use of this tool."+color.GREEN+"\n\nDo you accept this agreement? (Y/N) : "+color.END)
		if accept != "y" and accept != "Y" and accept != "yes" and accept != "YES" and accept != "n" and accept != "N" and accept != "no" and accept != "NO":
			check()
		else:
			a = "touch .agreement.txt | echo "+accept+" > .agreement.txt"
			os.system(a)
			check()
check()
