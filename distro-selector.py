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
DEBUG = "--debug" in sys.argv or "--verbose" in sys.argv

rolls = 0

def print_debug(msg):
    """Helper function to print formatted debug logs if flag is active."""
    if DEBUG:
        print(f"[DEBUG] {msg}")

def generate_distro():
    # Bypass long time.sleep delays if debugging to speed up profiling
    if DEBUG:
        print_debug("Skipping message delays for active debugging.")
        print(random.choice(MESSAGES))
    else:
        for _ in range(3):
            print(random.choice(MESSAGES))
            time.sleep(1)

    if FORCE_RARE:
        print_debug("Force Rare override active: Bypassing RNG gates.")
        return "TempleOS"

    # TempleOS Roll (1 in 500)
    temple_roll = random.randint(1, 500)
    print_debug(f"TempleOS Roll: Generated {temple_roll} (Triggers on 1)")
    if temple_roll == 1:
        print("[ULTRA RARE DISTRO FOUND]")
        return "TempleOS"

    # Arch Bias Roll (1 in 10)
    arch_roll = random.randint(1, 10)
    print_debug(f"Arch Bias Roll: Generated {arch_roll} (Triggers on 1)")
    if arch_roll == 1:
        print("The computer has an Arch bias today.")
        return "Arch"

    # Standard Pool Draw
    print_debug(f"Proceeding to core pool selection. Pool size: {len(DISTROS)}")
    chosen = random.choice(DISTROS)
    print_debug(f"Selected item index: {DISTROS.index(chosen)} -> Value: '{chosen}'")
    return chosen


print("Random Distro Chooser.")

# Startup Diagnostics Report
if DEBUG:
    print("\n==================================")
    print("   VERBOSE DIAGNOSTIC OVERVIEW   ")
    print("==================================")
    print_debug(f"Python Runtime Environment: {sys.version.split()[0]}")
    print_debug(f"Runtime CLI Arguments: {sys.argv[1:]}")
    print_debug(f"Configured Pool Size: {len(DISTROS)} entries")
    print_debug(f"Configured Loading Messages: {len(MESSAGES)} entries")
    print_debug(f"Force Rare Override Status: {FORCE_RARE}")
    print("==================================\n")

# Wrap the execution loop to safely intercept SIGINT / Ctrl+C signals
try:
    while True:
        input("Press ENTER to generate a random distro...")

        rolls += 1
        print(f"\nRoll #{rolls}")

        chosen_distro = generate_distro()

        print("Computer chooses...")
        if not DEBUG:
            time.sleep(1.5) # Instant resolution during active debugging

        print(f"====== {chosen_distro} ======\n")

        retry = input("Try again? [Y/N]\n> ")

        if retry.lower() in ["n", "no"]:
            print_debug(f"Graceful teardown. Total session iterations handled: {rolls}")
            print("Okay, bye!")
            break

except KeyboardInterrupt:
    print("\n\n[!] Session interrupted by user. Exiting gracefully. Bye!")
    sys.exit(0)
