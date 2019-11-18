"""
Advent of Code 2018

https://adventofcode.com/2018/day/21

--- Day 21: Chronal Conversion ---

You should have been watching where you were going, because as you wander the
new North Pole base, you trip and fall into a very deep hole!

Just kidding. You're falling through time again.

If you keep up your current pace, you should have resolved all of the temporal
anomalies by the next time the device activates. Since you have very little
interest in browsing history in 500-year increments for the rest of your life,
you need to find a way to get back to your present time.

After a little research, you discover two important facts about the behavior
of the device:

First, you discover that the device is hard-wired to always send you back
in time in 500-year increments. Changing this is probably not feasible.

Second, you discover the activation system (your puzzle input) for the time
travel module. Currently, it appears to run forever without halting.

If you can cause the activation system to halt at a specific moment, maybe you
can make the device send you so far back in time that you cause an integer
underflow in time itself and wrap around back to your current time!

The device executes the program as specified in manual section one and manual
section two.

Your goal is to figure out how the program works and cause it to halt.
You can only control register 0; every other register begins at 0 as usual.

Because time travel is a dangerous activity, the activation system begins with
a few instructions which verify that bitwise AND (via bani) does a numeric
operation and not an operation as if the inputs were interpreted as strings.
If the test fails, it enters an infinite loop re-running the test instead of
allowing the program to execute normally. If the test passes, the program
continues, and assumes that all other bitwise operations (banr, bori, and borr)
also interpret their inputs as numbers. (Clearly, the Elves who wrote this
system were worried that someone might introduce a bug while trying to emulate
this system with a scripting language.)

What is the lowest non-negative integer value for register 0 that causes the
program to halt after executing the fewest instructions? (Executing the same
instruction multiple times counts as multiple instructions executed.)

Your puzzle answer was 4797782.

--- Part Two ---

In order to determine the timing window for your underflow exploit, you also
need an upper bound:

What is the lowest non-negative integer value for register 0 that causes the
program to halt after executing the most instructions? (The program must
actually halt; running forever does not count as halting.)

Your puzzle answer was 6086461.
"""

def execute_translated_program(registers=None):
    if registers is None:
        registers = [0, 0, 0, 0, 0, 0]

    # -- Verify bitwise AND is on numeric values
    registers[3] = 123                                  #  0 seti 123 0 3
    registers[3] = registers[3] & 456                   #  1 bani 3 456 3
    while not registers[3] == 72:                       #  2 eqri 3 72 3
        print("ERROR: bitwise AND is a numeric operation. Strings given.")
        registers[3] = registers[3] & 456               #  1 bani 3 456 3

    # -- Start actual program
    registers[3] = 0                                    #  5 seti 0 0 3
    run_loop_1 = True
    while run_loop_1:
        print(f"Loop_1: {registers}")
        registers[1] = registers[3] | 65536             #  6 bori 3 65536 1
        registers[3] = 4921097                          #  7 seti 4921097 0 3

        run_loop_2 = True
        while run_loop_2:
            print(f"\tLoop_2: {registers}")
            registers[4] = registers[1] & 255           #  8 bani 1 255 4
            registers[3] += registers[4]                #  9 addr 3 4 3
            registers[3] = registers[3] & 16777215      # 10 bani 3 16777215 3
            registers[3] *= 65899                       # 11 muli 3 65899 3
            registers[3] = registers[3] & 16777215      # 12 bani 3 16777215 3

            # If -> go to end condition else continue
            if 256 > registers[1]:                      # 13 gtir 256 1 4
                if registers[3] == registers[0]:        # 28 eqrr 3 0 4
                    print(register[3])
                    run_loop_1 = False
                run_loop_2 = False
            else:
                registers[4] = 0                        # 17 seti 0 5 4
                run_loop_3 = True
                while run_loop_3:
                    print(f"\t\tLoop_3: {registers}")
                    registers[5] = registers[4] + 1     # 18 addi 4 1 5
                    registers[5] *= 256                 # 19 muli 5 256 5

                    if registers[5] > registers[1]:     # 20 gtrr 5 1 5
                        registers[1] = registers[4]     # 26 setr 4 3 1
                        registers[2] = 7                # 27 seti 7 9 2  -->  8
                        run_loop_3 = False
                    else:
                        registers[4] += 1               # 24 addi 4 1 4
                        registers[2] = 17               # 25 seti 17 8 2 --> 18
    return registers

def find_register_0_bounds_halting_program_execution(registers=None,
        verbose=False):
    register_0_values_halting_program_log = []
    register_0_values_halting_program_log_set = set()

    if registers is None:
        registers = [0, 0, 0, 0, 0, 0]

    # -- Verify bitwise AND is on numeric values
    registers[3] = 123                                  #  0 seti 123 0 3
    registers[3] = registers[3] & 456                   #  1 bani 3 456 3
    while not registers[3] == 72:                       #  2 eqri 3 72 3
        print("ERROR: bitwise AND is a numeric operation. Strings given.")
        registers[3] = registers[3] & 456               #  1 bani 3 456 3

    # -- Start actual program
    registers[3] = 0                                    #  5 seti 0 0 3
    run_loop_1 = True
    while run_loop_1:
        if verbose:
            print(f"Loop_1:\t\t\t{registers}")
        registers[1] = registers[3] | 65536             #  6 bori 3 65536 1
        registers[3] = 4921097                          #  7 seti 4921097 0 3

        run_loop_2 = True
        while run_loop_2:
            if verbose:
                print(f"\tLoop_2:\t\t{registers}")
            registers[4] = registers[1] & 255           #  8 bani 1 255 4
            registers[3] += registers[4]                #  9 addr 3 4 3
            registers[3] = registers[3] & 16777215      # 10 bani 3 16777215 3
            registers[3] *= 65899                       # 11 muli 3 65899 3
            registers[3] = registers[3] & 16777215      # 12 bani 3 16777215 3

            # If -> go to end condition else continue
            if 256 > registers[1]:                      # 13 gtir 256 1 4
                # Log values for register 3 when comparing to register 0
                if registers[3] in register_0_values_halting_program_log_set:
                    return register_0_values_halting_program_log
                register_0_values_halting_program_log_set.add(registers[3])
                register_0_values_halting_program_log.append(registers[3])

                if registers[3] == registers[0]:        # 28 eqrr 3 0 4
                    run_loop_1 = False
                run_loop_2 = False
            else:
                registers[4] = 0                        # 17 seti 0 5 4
                run_loop_3 = True
                while run_loop_3:
                    if verbose:
                        print(f"\t\tLoop_3:\t{registers}")
                    registers[5] = registers[4] + 1     # 18 addi 4 1 5
                    registers[5] *= 256                 # 19 muli 5 256 5

                    if registers[5] > registers[1]:     # 20 gtrr 5 1 5
                        registers[1] = registers[4]     # 26 setr 4 3 1
                        registers[2] = 7                # 27 seti 7 9 2  -->  8
                        run_loop_3 = False
                    else:
                        registers[4] += 1               # 24 addi 4 1 4
                        registers[2] = 17               # 25 seti 17 8 2 --> 18
    return registers

def main():
    register_0_values = find_register_0_bounds_halting_program_execution()
    register_0_least_instructions = register_0_values[0]
    register_0_most_instructions = register_0_values[-1]

    print("Lowest integer value in register 0 to halt program",
        f"(least instructions): {register_0_least_instructions}")

    print("Lowest integer value in register 0 to halt program",
        f"(most instructions): {register_0_most_instructions}")

if __name__ == '__main__':
    main()
