import hashlib
import requests
import questionary
from rich import print
import subprocess

subprocess.run("clear")
print("TuffDB - The [bold]TUFFIEST[/bold] password scanner!")

while True:
    password = questionary.password("What is your password? :").ask()

    h = hashlib.sha1()
    h.update(password.encode("utf-8"))
    hash = h.hexdigest().upper()
    suffix = hash[5:]
    prefix = hash[:5]
    answer = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")

    if suffix in answer.text:
        print("[red]Compromise[/red]! You [bold]must[/bold] change your password. :(")
        print("Made by @Fluff2513 on GitHub.")
    else:
        print("[bright_green]Safe[/bright_green]! Your password as not been leaked.:)")
        print("Made by @Fluff2513 on GitHub.")