# Cyber Jarvis - Command Dispatcher Prototype (v0.1)
# Author: Amir Mohammad Taji
#
# Description:
# A terminal-based command dispatcher, the first building
# block of Cyber Jarvis. Each command is an object that
# stores a name and a function, and runs it when called.
# New commands can be added without changing the core loop.
#
# Commands:
# - hello     : greeting
# - time      : placeholder time check
# - even      : even/odd checker
# - password  : password strength checker (Weak/Medium/Strong)
# - port      : port number validator + well-known ports
# - ip address: IPv4 format and range validator
# - caesar    : Caesar cipher (encrypt / decrypt)
# - help      : list available commands
# - exit      : quit
#
# Concepts Used:
# - Object-Oriented Programming (OOP): classes, objects, methods
# - Functions as values (passing functions without calling them)
# - Dictionaries
# - while loop, for loop
# - if / elif / else
# - String methods (lower, isdigit, isupper, islower, split)
# - ord() / chr() and modulo (%)
# - Type conversion (int)
# - User input
# ==========================================
import socket
import platform
import uuid
import secrets
import string


class Command:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def run(self):
        self.action()


def network_info():
    hostname = socket.gethostname()
    print(f"Host name: {hostname}")

    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"Local IP address: {ip_address}")
    except socket.gaierror as error:
        print(f"Could not find IP address: {error}")

    system = platform.system()
    print(f"Operating system: {system}")

    mac_address = uuid.getnode()
    mac = ':'.join(f'{(mac_address >> i) & 0xff:02x}'
                   for i in range(40, -1, -8))
    print(f"Mac addres: {mac}")


def check_connection():
    try:
        socket.create_connection(("1.1.1.1", 53), timeout=3)
        print("Network connection is available")
    except OSError:
        print("Network connection failed")


def check_time():
    print("Chacking time .....")


def say_hello():
    print("Hi! Amir")


def check_even():
    number = int(input("Enter number:"))
    if number % 2 == 0:
        print("it`s even")
    else:
        print("it`s odd")


def generate_password():

    character = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = ""

        for i in range(12):

            i = secrets.choice(character)
            password = password + i

        has_number = False
        has_upper = False
        has_special = False

        for ch in password:
            if ch.isdigit():
                has_number = True
            elif ch.isupper():
                has_upper = True
            elif ch in string.punctuation:
                has_special = True
        if has_number and has_upper and has_special:
            break

    print(password)


def check_password():
    Password = input("Enter your password:")

    if len(Password) >= 8:
        print("len is good")
    elif len(Password) < 8:
        print("need more character")

    has_number = False

    for i in Password:
        if i.isdigit():
            has_number = True

    if has_number:
        print("Password has number")
    else:
        print("need at least one number")

    has_upper = False

    for u in Password:
        if u.isupper():
            has_upper = True

    if has_upper:
        print("password has uper")
    else:
        print("Enter uper crakter")

    special_characters = "~`!@#$%^&*()_-=+}[]/?.>;:'"

    has_special_charakter = False

    for s in Password:
        if s in special_characters:
            has_special_charakter = True

    if has_special_charakter:
        print("it has special character")
    else:
        print("Enter special character")

    score = 0

    if len(Password) >= 8:
        score = score + 1

    if has_number:
        score = score + 1

    if has_upper:
        score = score + 1

    if has_special_charakter:
        score = score + 1

    if score <= 1:
        print("it`s WEAK")
    elif 2 <= score <= 3:
        print("it`s MEDIUM")
    elif score == 4:
        print("it`s SRONG")


def check_port():
    try:
        port = int(input("Enter your port address:"))
    except ValueError:
        print("Please enter valid number")
        return

    special_port = [22, 443, 80]

    if port in special_port:
        print(f"It`s special port : {port}")

    elif 0 < port <= 65535:
        print("port is valid")

    else:
        print("it`s not valid")


def check_ip():
    ip_address = input("Enter IP address: ")

    part = ip_address.split(".")
    print(part)

    if len(part) != 4:
        print("Invalid IP format")
        return

    for p in part:
        try:
            number = int(p)
        except ValueError:
            print("IP must contain only numbers")
            return

        if number < 0 or number > 255:
            print("Each part must be between 0 and 255")
            return

    print("IP address is valid")


def caesar(text, shift):
    result = ""

    for i in text:
        if i.islower():
            position = ord(i) - ord("a")
            new_position = (position + shift) % 26
            new_text = chr(new_position + ord("a"))
            result = result + new_text

        elif i.isupper():
            position = ord(i) - ord("A")
            new_position = (position + shift) % 26
            new_text = chr(new_position + ord("A"))
            result = result + new_text

        else:
            result = result + i
    return result


def run_caesar():
    text = input("Enter your text: ")
    mode = input("Encrypt or decrypt? (e/d): ").lower()
    shift = int(input("Enter shift number: "))

    if mode == "e":
        print(caesar(text, shift))
    elif mode == "d":
        print(caesar(text, -shift))
    else:
        print("Invalid mode,use e or d")


def calculate():
    try:
        num1 = float(input("Enter your first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter your second number: "))

        if operator == "+":
            print(num1 + num2)
        elif operator == "-":
            print(num1 - num2)
        elif operator == "*":
            print(num1 * num2)
        elif operator == "/":
            print(num1 / num2)
        else:
            print("invalid operator")

    except ValueError:
        print("that is not a number!")
    except ZeroDivisionError:
        print("Divide to zero it`s not available")


calculate()


obj1 = Command("hello", say_hello)
obj2 = Command("time", check_time)
obj3 = Command("even", check_even)
obj4 = Command("password", check_password)
obj5 = Command("port", check_port)
obj6 = Command("ip address", check_ip)
obj7 = Command("caesar", run_caesar)
obj8 = Command("network info", network_info)
obj9 = Command("check connection", check_connection)
obj10 = Command("calculate", calculate)
obj11 = Command("generat password", generate_password)

Commands = {
    "hello": obj1,
    "time": obj2,
    "even": obj3,
    "password": obj4,
    "port": obj5,
    "ip address": obj6,
    "caesar": obj7,
    "network info": obj8,
    "check connection": obj9,
    "calculate": obj10,
    "generat password": obj11
}

while True:
    choice = input("Enter a command:").lower()
    if choice in Commands:
        Commands[choice].run()

    elif choice == "exit":
        break
    elif choice == "help":
        for i in Commands:
            print(i)
    else:
        print("command is not avilible")
