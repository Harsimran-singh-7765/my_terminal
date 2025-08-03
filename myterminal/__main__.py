import sys
from myterminal.core import get_command, run_command

# 🧠 Import git functions
from myterminal.gitops import git_start, git_push

def main():
    if len(sys.argv) < 2:
        print("Please enter a command like: myterminal 'check disk space'")
        return

    cmd = sys.argv[1]

    if cmd == "git":
        if len(sys.argv) < 3:
            print("Please use 'myterminal git start' or 'myterminal git push [filename] [branch]'")
            return

        subcmd = sys.argv[2]

        if subcmd == "start":
            git_start()

        elif subcmd == "push":
            filename = sys.argv[3] if len(sys.argv) >= 4 else "."
            branch = sys.argv[4] if len(sys.argv) >= 5 else None
            git_push(filename, branch)

        else:
            print(f"Unknown git subcommand: {subcmd}")
        return

    # 🌐 Default: natural language to command
    natural_input = " ".join(sys.argv[1:])
    terminal_command = get_command(natural_input)
    output = run_command(terminal_command)
    print(output)

if __name__ == "__main__":
    main()
