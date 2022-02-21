from fibonacci.sequence import *


def run_fibonacci():
    command = input()
    sequence = []

    while not command == "Stop":
        args = command.split()

        if args[0] == "Create":
            sequence = create_seq(int(args[2]))
            print(*sequence)
        elif args[0] == "Locate":
            number = int(args[1])
            locate(number, sequence)

        command = input()
