import random
import time
import sys

DISTROS = [
    "Debian", "Ubuntu", "Kali", "PeppermintOS", "Mint", "Pop!_OS",
    "ElementaryOS", "ZorinOS", "KDE Neon", "Deepin", "Arch", "Artix",
    "Arco Linux", "Archman", "Garuda", "EndeavourOS", "Manjaro",
    "RedHat", "Fedora", "Nobara", "Slackware", "Gentoo",
    "OpenSuse", "Alpine", "NixOS", "Void", "Puppy Linux",
    "Hannah Montanna Linux", "RedStarOS", "AmogOS",
    "Guix", "Crux Linux", "LFS", "Asahi Linux",
    "Solus"
    
]

MESSAGES = [
    "Generating random binary...",
    "Consulting the Linux gods...",
    "Reading ancient forum posts...",
    "Compiling kernel in my head...",
    "Contemplating life choices...",
    "Sacrificing RAM to the penguin...",
    "Downloading more RAM...",
    "Arguing about systemd...",
    "Installing packages..."
]

FORCE_RARE = "--force-rare" in sys.argv

rolls = 0

def generate_distro():
    for _ in range(3):
        print(random.choice(MESSAGES))
        time.sleep(1)

    if FORCE_RARE:
        print("[DEBUG] Force Rare Mode Enabled")
        return "TempleOS"

    if random.randint(1, 500) == 1:
        print("[ULTRA RARE DISTRO FOUND]")
        return "TempleOS"

    if random.randint(1, 10) == 1:
        print("The computer has an Arch bias today.")
        return "Arch"

    return random.choice(DISTROS)


print("Random Distro Chooser.")

while True:
    input("Press ENTER to generate a random distro...")

    rolls += 1
    print(f"\nRoll #{rolls}")

    chosen_distro = generate_distro()

    print("Computer chooses...")
    time.sleep(1.5)

    print(f"====== {chosen_distro} ======\n")

    retry = input("Try again? [Y/N]\n> ")

    if retry.lower() in ["n", "no"]:
        print("Okay, bye!")
        break
