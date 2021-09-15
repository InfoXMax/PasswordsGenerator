#!/usr/bin/env python3

import colorama
from colorama import Fore, Style
#pass gen
import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "[]{}()*;/,._-$&=<:!?"
all = lower + upper + number + symbols
length = 16
password = "".join(random. sample(all, length))
#end pass gen



print(Fore.CYAN + " _        ,__         _     _ __   __             ",)
print(Fore.CYAN + " | , __   /  `   __.  `.   /  |    |    ___  _  .-",)
print(Fore.CYAN + " | |'  `. |__  .'   \   \,'   |\  /|   /   `  \,' ",)
print(Fore.CYAN + " | |    | |    |    |  ,'\    | \/ |  |    |  /\  	Pass Gen Manager ",)
print(Fore.CYAN + " / /    | |     `._.' /   \   /    /  `.__/| /  \ ",)
print(Fore.CYAN + "          /                                       ",)


username = input('Type Your Username: ')
email = input('Type Your Email: ')
url = input('Type The URL: ')
print('\n')



print(Fore.WHITE + "Username :",Fore.YELLOW + username)
print(Fore.WHITE + "Email :",Fore.GREEN + email)
print(Fore.WHITE + "Url :",Fore.BLUE + url)
print(Fore.WHITE + "Password :",Fore.MAGENTA + password)



with open('Passwords.csv', 'a') as f:
	print("Username : ", username,'\n', "Email : " , email,'\n', "Url : " , url,'\n', "Password : " , password,file=f)
