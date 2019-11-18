from collections import namedtuple, defaultdict
"""
Advent of Code 2018

https://adventofcode.com/2018/day/16

--- Day 16: Chronal Classification ---

As you see the Elves defend their hot chocolate successfully, you go back to
falling through time. This is going to become a problem.

If you're ever going to return to your own time, you need to understand how
this device on your wrist works. You have a little while before you reach your
next destination, and with a bit of trial and error, you manage to pull up
a programming manual on the device's tiny screen.

According to the manual, the device has four registers (numbered 0 through 3)
that can be manipulated by instructions containing one of 16 opcodes.
The registers start with the value 0.

Every instruction consists of four values: an opcode, two inputs (named A and
B), and an output (named C), in that order. The opcode specifies the behavior
of the instruction and how the inputs are interpreted. The output, C, is
always treated as a register.

In the opcode descriptions below, if something says "value A", it means to
take the number given as A literally. (This is also called an "immediate"
value.) If something says "register A", it means to use the number given as
A to read from (or write to) the register with that number. So, if the opcode
addi adds register A and value B, storing the result in register C, and
the instruction addi 0 7 3 is encountered, it would add 7 to the value
contained by register 0 and store the sum in register 3, never modifying
registers 0, 1, or 2 in the process.

Many opcodes are similar except for how they interpret their arguments.
The opcodes fall into seven general categories:

Addition:

  * addr (add register) stores into register C the result of adding
    register A and register B.
  * addi (add immediate) stores into register C the result of adding
    register A and value B.

Multiplication:

  * mulr (multiply register) stores into register C the result of multiplying
    register A and register B.
  * muli (multiply immediate) stores into register C the result of multiplying
    register A and value B.

Bitwise AND:

  * banr (bitwise AND register) stores into register C the result of the
    bitwise AND of register A and register B.
  * bani (bitwise AND immediate) stores into register C the result of the
    bitwise AND of register A and value B.

Bitwise OR:

  * borr (bitwise OR register) stores into register C the result of the bitwise
    OR of register A and register B.
  * bori (bitwise OR immediate) stores into register C the result of the
    bitwise OR of register A and value B.

Assignment:

  * setr (set register) copies the contents of register A into register C.
    (Input B is ignored.)
  * seti (set immediate) stores value A into register C. (Input B is ignored.)

Greater-than testing:

  * gtir (greater-than immediate/register) sets register C to 1 if value A
    is greater than register B. Otherwise, register C is set to 0.
  * gtri (greater-than register/immediate) sets register C to 1 if register A
    is greater than value B. Otherwise, register C is set to 0.
  * gtrr (greater-than register/register) sets register C to 1 if register A
    is greater than register B. Otherwise, register C is set to 0.

Equality testing:

  * eqir (equal immediate/register) sets register C to 1 if value A is equal
    to register B. Otherwise, register C is set to 0.
  * eqri (equal register/immediate) sets register C to 1 if register A is equal
    to value B. Otherwise, register C is set to 0.
  * eqrr (equal register/register) sets register C to 1 if register A is equal
    to register B. Otherwise, register C is set to 0.

Unfortunately, while the manual gives the name of each opcode, it doesn't seem
to indicate the number. However, you can monitor the CPU to see the contents
of the registers before and after instructions are executed to try to work
them out. Each opcode has a number from 0 through 15, but the manual doesn't
say which is which. For example, suppose you capture the following sample:

Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]

This sample shows the effect of the instruction 9 2 1 2 on the registers.
Before the instruction is executed, register 0 has value 3, register 1 has
value 2, and registers 2 and 3 have value 1. After the instruction is
executed, register 2's value becomes 2.

The instruction itself, 9 2 1 2, means that opcode 9 was executed with A=2,
B=1, and C=2. Opcode 9 could be any of the 16 opcodes listed above, but only
three of them behave in a way that would cause the result shown in the sample:

  * Opcode 9 could be mulr: register 2 (which has a value of 1) times
    register 1 (which has a value of 2) produces 2, which matches the value
    stored in the output register, register 2.
  * Opcode 9 could be addi: register 2 (which has a value of 1) plus value 1
    produces 2, which matches the value stored in the output register,
    register 2.
  * Opcode 9 could be seti: value 2 matches the value stored in the output
    register, register 2; the number given for B is irrelevant.

None of the other opcodes produce the result captured in the sample.
Because of this, the sample above behaves like three opcodes.

You collect many of these samples (the first section of your puzzle input).
The manual also includes a small test program (the second section of your
puzzle input) - you can ignore it for now.

Ignoring the opcode numbers, how many samples in your puzzle input behave
like three or more opcodes?

Your puzzle answer was 624.


--- Part Two ---

Using the samples you collected, work out the number of each opcode and execute the test program (the second section of your puzzle input).

What value is contained in register 0 after executing the test program?

Your puzzle answer was 584.
"""

Sample = namedtuple('Sample', ['before', 'after', 'instruction'])
opcodes = [
    'addr', 'addi',
    'mulr', 'muli',
    'banr', 'bani',
    'borr', 'bori',
    'setr', 'seti',
    'gtir', 'gtri', 'gtrr',
    'eqir', 'eqri', 'eqrr'
]

def parse_samples(samples):
    parsed_samples = []
    for i in range(0, len(samples), 4):
        sample = samples[i:i+3]
        before, instruction, after = sample
        before = [int(reg) for reg in before[9:-1].split(",")]
        after = [int(reg) for reg in after[9:-1].split(",")]
        instruction = [int(each) for each in instruction.split()]
        parsed_samples.append(Sample(before=before, after=after,
                                     instruction=instruction))

    return parsed_samples

def execute_instruction(opcode, input_1, input_2, output_reg, registers):
    # Addition
    if opcode == 'addr':
        registers[output_reg] = registers[input_1] + registers[input_2]
    elif opcode == 'addi':
        registers[output_reg] = registers[input_1] + input_2
    # Multiplication
    elif opcode == 'mulr':
        registers[output_reg] = registers[input_1] * registers[input_2]
    elif opcode == 'muli':
        registers[output_reg] = registers[input_1] * input_2
    # Bitwise AND
    elif opcode == 'banr':
        registers[output_reg] = registers[input_1] & registers[input_2]
    elif opcode == 'bani':
        registers[output_reg] = registers[input_1] & input_2
    # Bitwise OR
    elif opcode == 'borr':
        registers[output_reg] = registers[input_1] | registers[input_2]
    elif opcode == 'bori':
        registers[output_reg] = registers[input_1] | input_2
    # Assignment
    elif opcode == 'setr':
        registers[output_reg] = registers[input_1]
    elif opcode == 'seti':
        registers[output_reg] = input_1
    # Greater than testing
    elif opcode == 'gtir':
        if input_1 > registers[input_2]:
            registers[output_reg] = 1
        else:
            registers[output_reg] = 0
    elif opcode == 'gtri':
        if registers[input_1] > input_2:
            registers[output_reg] = 1
        else:
            registers[output_reg] = 0
    elif opcode == 'gtrr':
        if registers[input_1] > registers[input_2]:
            registers[output_reg] = 1
        else:
            registers[output_reg] = 0
    # Equality testing
    elif opcode == 'eqir':
        if input_1 == registers[input_2]:
            registers[output_reg] = 1
        else:
            registers[output_reg] = 0
    elif opcode == 'eqri':
        if registers[input_1] == input_2:
            registers[output_reg] = 1
        else:
            registers[output_reg] = 0
    elif opcode == 'eqrr':
        if registers[input_1] == registers[input_2]:
            registers[output_reg] = 1
        else:
            registers[output_reg] = 0

    return registers

def execute_program(program):
    registers = [0, 0, 0, 0]
    for line in program:
        registers = execute_instruction(*line, registers)

    return registers

def find_samples_with_n_plus_opcodes(samples, n=3):
    n_plus_opcodes = {}
    for i, sample in enumerate(samples):
        _, input_1, input_2, output_reg = sample.instruction
        correct_opcodes = 0
        for opcode in opcodes:
            registers = execute_instruction(opcode, input_1, input_2,
                                            output_reg, sample.before[:])
            if registers == sample.after:
                correct_opcodes = correct_opcodes + 1

        n_plus_opcodes[i] = correct_opcodes

    return len([correct_opcodes for correct_opcodes in n_plus_opcodes.values()
                                if correct_opcodes >= n])

def find_opcode_assignment(samples):
    possible_assignment = defaultdict(set)
    for sample in samples:
        i, input_1, input_2, output_reg = sample.instruction
        for opcode in opcodes:
            result = execute_instruction(opcode, input_1, input_2,
                                         output_reg, sample.before[:])
            if result == sample.after:
                possible_assignment[i].add(opcode)

    true_assignment = {}
    while len(possible_assignment) > 0:
        for index, possible_opcodes in possible_assignment.items():
            if len(possible_opcodes) == 1:
                possible_assignment = {
                    i: set(code for code in codes if code not in possible_opcodes)
                    for i, codes in possible_assignment.items()}

                true_assignment[index] = possible_opcodes.pop()
                possible_assignment.pop(index)

    return true_assignment

def main():
    samples = []
    with open('day_16_samples.txt', 'r') as samples_file:
        samples = samples_file.read().splitlines()
    samples = parse_samples(samples)
    n_plus_opcodes = find_samples_with_n_plus_opcodes(samples[:])
    print(f"Samples behaving like 3 or more opcodes: {n_plus_opcodes}")

    # Part 2
    opcode_assignment = find_opcode_assignment(samples)
    program = []
    with open('day_16_program.txt', 'r') as program_file:
        for line in program_file.read().splitlines():
            opcode, in_1, in_2, out = line.split()
            program.append([
                opcode_assignment[int(opcode)],
                int(in_1), int(in_2), int(out)])

    result = execute_program(program)
    print(f"Resulting registers: {result}")

if __name__ == '__main__':
    main()
