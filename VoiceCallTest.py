from subprocess import check_output
from subprocess import call

#call("dir C:\\")
#myStr = check_output("dir C:\\", shell=True).decode()
myStr = check_output("balcon -n Zira -t \"Hello time to kill\"", shell=True).decode()
print( myStr )
#os.system("dir")
#check_output(["dir"])