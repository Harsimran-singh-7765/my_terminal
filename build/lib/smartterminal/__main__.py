import sys
from smartterminal.core import get_command, run_command

def main():
    if len(sys.argv) < 2:
        print("Please enter a command like: smartterm 'check disk space'")
        return

    natural_input = " ".join(sys.argv[1:])
    terminal_command = get_command(natural_input)
    output = run_command(terminal_command)
    print(output)

if __name__ == "__main__":
    main()
