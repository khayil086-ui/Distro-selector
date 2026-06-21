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
    "Installing packages...",
    "Checking swap space...",
    "Re-reading the man pages...",
    "Reticulating splines...",
    "Searching Stack Overflow...",
    "Blaming systemd...",
    "Regretting deleting the french language pack...",
    "Updating packages...",
    "Configuring Xorg servers...",
    "Parsing config files...",
    "Arguing with Windows users...",
    "Fixing broken GRUB bootloader entries...",
    "Waiting for the Debian stable release team...",
    "Recompiling xmonad configuration layout..."
]

FRUSTRATED_REMARKS = [
    "Are you ever going to actually install it?",
    "I am getting warm from all this indecision...",
    "My CPU cycles are dying for your indecisiveness.",
    "Just pick one and run sudo rm -rf / already.",
    "We have been doing this for a while. Are we done yet?",
    "Is this what you do with your free time?"
]


HELP = "--help" in sys.argv or "-h" in sys.argv
ABOUT = "--about" in sys.argv
FORCE_RARE = "--force-rare" in sys.argv
DEBUG = "--debug" in sys.argv or "--verbose" in sys.argv

if HELP:
    print("Distro Selector - Help Menu")
    print("\nUsage:")
    print("  python3 distro-selector.py [flags]")
    print("\nFlags:")
    print("  --help, -h    Show this help menu")
    print("  --about       Show project background and developer credits")
    print("  --force-rare  Bypass random probability to force a TempleOS output")
    print("  --debug       Skip artificial delays and output internal rolling math")
    print("  --verbose     Alias for the --debug command line flag")
    sys.exit(0)

if ABOUT:
    print("Distro Selector - About")
    print("\nA randomized terminal utility built to select Linux distributions.")
    print("Features a 1-in-10 Arch bias and a 1-in-500 TempleOS drop rate.")
    print("\nCopyright (c) 2026")
    print("Developed by:")
    print("  Yaffs2     (https://github.com/Yaffs2)")
    print("  khayil086  (https://github.com/Khayil086-ui)")
    print("  Project    (https://github.com/Khayil086-ui/Distro-selector)")
    sys.exit(0)

rolls = 0

def print_debug(msg):
    """Helper function to print formatted debug logs if flag is active."""
    if DEBUG:
        print(f"[DEBUG] {msg}")

def run_progress_bar(total_duration):
    """Simulates a terminal compilation progress bar over an exact duration."""
    steps = list(range(1, 101))
    delay_per_step = total_duration / len(steps)

    for progress in steps:
        time.sleep(delay_per_step)
        sys.stdout.write(f"\rProgress: [{progress}%]")
        sys.stdout.flush()
    print()

def generate_distro():
    if DEBUG:
        print_debug("Skipping message delays for active debugging.")
        print(random.choice(MESSAGES))
    else:
        message_count = random.randint(3, 10)
        max_unique = min(message_count, len(MESSAGES))
        chosen_messages = random.sample(MESSAGES, max_unique)

        if random.randint(1, 8) == 1:
            chosen_messages.append("Compiling Gentoo packages from source...")

        if random.randint(1, 15) == 1:
            chosen_messages.append("Building Linux From Scratch (LFS) toolchain...")

        random.shuffle(chosen_messages)

        for msg in chosen_messages:
            print(msg)

            if msg == "Compiling Gentoo packages from source...":
                run_progress_bar(5.0)

            elif msg == "Building Linux From Scratch (LFS) toolchain...":
                run_progress_bar(10.0)

            else:
                time.sleep(random.uniform(0.2, 1.3))

    if FORCE_RARE:
        print_debug("Force Rare override active: Bypassing RNG gates.")
        return "TempleOS"

    temple_roll = random.randint(1, 500)
    print_debug(f"TempleOS Roll: Generated {temple_roll} (Triggers on 1)")
    if temple_roll == 1:
        print("[ULTRA RARE DISTRO FOUND]")
        return "TempleOS"

    arch_roll = random.randint(1, 10)
    print_debug(f"Arch Bias Roll: Generated {arch_roll} (Triggers on 1)")
    if arch_roll == 1:
        return "Arch"

    print_debug(f"Proceeding to core pool selection. Pool size: {len(DISTROS)}")
    chosen = random.choice(DISTROS)
    print_debug(f"Selected item index: {DISTROS.index(chosen)} -> Value: '{chosen}'")
    return chosen


print("Random Distro Chooser.")

if DEBUG:
    print("\n==================================")
    print("   VERBOSE DIAGNOSTIC OVERVIEW   ")
    print("==================================")
    print_debug(f"Python Runtime Environment: {sys.version.split()}")
    print_debug(f"Runtime CLI Arguments: {sys.argv[1:]}")
    print_debug(f"Configured Pool Size: {len(DISTROS)} entries")
    print_debug(f"Configured Loading Messages: {len(MESSAGES)} entries")
    print_debug(f"Force Rare Override Status: {FORCE_RARE}")
    print("==================================\n")   
    
try:
    while True:
        input("Press ENTER to generate a random distro...")

        rolls += 1
        print(f"\nRoll #{rolls}")

        
        if rolls > 5 and not DEBUG:
            if random.randint(1, 3) == 1:
                print(f"[{random.choice(FRUSTRATED_REMARKS)}]")
                time.sleep(1.8)

        chosen_distro = generate_distro()

        print("Computer chooses...")
        if not DEBUG:
            time.sleep(random.uniform(1.0, 2.0))

        print(f"====== {chosen_distro} ======\n")

    
        if chosen_distro == "Ubuntu":
            print("you wanna snap today huh?\n")

        elif chosen_distro == "RedStarOS":
            print("The computer will spy on you for the rest of the day...\n")

        elif chosen_distro == "Arch":
            print("The computer has an Arch bias today.\n")

        retry = input("Try again? [Y/N]\n> ")

        if retry.lower() in ["n", "no"]:
            print_debug(f"Graceful teardown. Total session iterations handled: {rolls}")
            print("Okay, bye!")
            break

except KeyboardInterrupt:
    print("\n\n[!] Session interrupted by user. Exiting gracefully. Bye!")
    sys.exit(0)
