"""
Advent of Code 2017

https://adventofcode.com/2017/day/8

--- Day 8: I Heard You Like Registers ---

You receive a signal directly from the CPU. Because of your recent assistance
with jump instructions, it would like you to compute the result of a series
of unusual register instructions.

Each instruction consists of several parts: the register to modify, whether
to increase or decrease that register's value, the amount by which
to increase or decrease it, and a condition. If the condition fails, skip
the instruction without modifying the register. The registers all start at 0.
The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10

These instructions would be processed as follows:

  * Because a starts at 0, it is not greater than 1, and so b is not modified.
  * a is increased by 1 (to 1) because b is less than 5 (it is 0).
  * c is decreased by -10 (to 10) because a is now greater than or
    equal to 1 (it is 1).
  * c is increased by -20 (to -10) because c is equal to 10.

After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU doesn't have the bandwidth to tell you what all the registers are named, and leaves that to you to determine.

What is the largest value in any register after completing the instructions in your puzzle input?

Your puzzle answer was 3745.


--- Part Two ---

To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to allocate to these operations. For example, in the above instructions, the highest value ever held was 10 (in register c after the third instruction was evaluated).

Your puzzle answer was 4644.
"""

def process_instructions(register_instructions):
    registers = dict()
    max_register_values = []
    for each in register_instructions:
        # Parse instruction
        instruction, condition = each.split(' if ')
        instr_register, instr_operator, instr_value = instruction.split(' ')
        cond_register, cond_operator, cond_value = condition.split(' ')
        instr_value, cond_value = int(instr_value), int(cond_value)

        # Initialise missing registers
        if instr_register not in registers:
            registers[instr_register] = 0
        if cond_register not in registers:
            registers[cond_register] = 0

        # Perform instruction
        if ((cond_operator == '>' and registers[cond_register] > cond_value)
        or (cond_operator == '>=' and registers[cond_register] >= cond_value)
        or (cond_operator == '<' and registers[cond_register] < cond_value)
        or (cond_operator == '<=' and registers[cond_register] <= cond_value)
        or (cond_operator == '==' and registers[cond_register] == cond_value)
        or (cond_operator == '!=' and registers[cond_register] != cond_value)):
            if instr_operator == 'inc':
                registers[instr_register] += instr_value
            elif instr_operator == 'dec':
                registers[instr_register] -= instr_value

        max_register_values.append(max(registers.values()))

    return registers, max_register_values

def find_largest_register_value(register_instructions):
    registers, max_register_values = process_instructions(register_instructions)
    return max(registers.values())

def find_largest_register_value_ever(register_instructions):
    registers, max_register_values = process_instructions(register_instructions)
    return max(max_register_values)

def main():
    filename = 'day_8_register_instructions.txt'
    with open(filename, 'r') as instructions_file:
        register_instructions = instructions_file.readlines()
    print("Largest value:", find_largest_register_value(register_instructions))
    print("Largest value (overall):",
          find_largest_register_value_ever(register_instructions))

if __name__ == '__main__':
    main()
