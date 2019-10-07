"""
Advent of Code 2017 - Day 23

https://adventofcode.com/2017/day/23

--- Day 23: Coprocessor Conflagration ---

You decide to head directly to the CPU and fix the printer from there.
As you get close, you find an experimental coprocessor doing so much work
that the local programs are afraid it will halt and catch fire. This would
cause serious issues for the rest of the computer, so you head in and see
what you can do.

The code it's running seems to be a variant of the kind you saw recently on
that tablet. The general functionality seems very similar, but some
of the instructions are different:

  * set X Y sets register X to the value of Y.
  * sub X Y decreases register X by the value of Y.
  * mul X Y sets register X to the result of multiplying the value contained
    in register X by the value of Y.
  * jnz X Y jumps with an offset of the value of Y, but only if the value
    of X is not zero. (An offset of 2 skips the next instruction, an offset
    of -1 jumps to the previous instruction, and so on.)

Only the instructions listed above are used. The eight registers here,
named a through h, all start at 0.

The coprocessor is currently set to some kind of debug mode, which allows
for testing, but prevents it from doing any meaningful work.

If you run the program (your puzzle input), how many times is the mul
instruction invoked?

Your puzzle answer was 6241.

--- Part Two ---

Now, it's time to fix the problem.

The debug mode switch is wired directly to register a. You flip the switch,
which makes register a now start at 1 when the program is executed.

Immediately, the coprocessor begins to overheat. Whoever wrote this program
obviously didn't choose a very efficient implementation. You'll need to
optimize the program if it has any hope of completing before Santa needs
that printer working.

The coprocessor's ultimate goal is to determine the final value left in
register h once the program completes. Technically, if it had that... it
wouldn't even need to run the program.

After setting register a to 1, if the program were to run to completion,
what value would be left in register h?

Your puzzle answer was 909.
"""

def coprocessor(registers, instructions, verbose=False):
    mul_instruction_counter = 0
    position = 0
    while position < len(instructions):
        operation, operand_1, operand_2 = instructions[position].split()
        if operand_2 in registers:
            operand_2 = registers[operand_2]
        else:
            operand_2 = int(operand_2)

        if verbose:
            print(f"Registers: {registers}")
            print(f"Line {position}: {instructions[position]}")

        if operation == 'jnz':
            if operand_1 in registers:
                conditional = registers[operand_1]
            else:
                conditional = operand_1
            if conditional != 0:
                position += operand_2
            else:
                position += 1
        else:
            if operation == 'set':
                registers[operand_1] = operand_2
            elif operation == 'sub':
                registers[operand_1] -= operand_2
            elif operation == 'mul':
                registers[operand_1] *= operand_2
                mul_instruction_counter += 1
            position += 1

    return registers, mul_instruction_counter

def coprocessor_instructions_in_python(registers):
    mul_instruction_counter = 0

    registers['b']  = 81                            #  1 set b 81
    registers['c']  = registers['b']                #  2 set c b
    if registers['a'] != 0:                         #  3 jnz a 2     --> 5
        # if 1 == 0:                                #  4 jnz 1 5     --> 9
        registers['b'] *= 100                       #  5 mul b 100
        mul_instruction_counter += 1
        registers['b'] -= -100000                   #  6 sub b -100000
        registers['c']  = registers['b']            #  7 set c b
        registers['c'] -= -17000                    #  8 sub c -17000
    while True:
        registers['f']  = 1                         #  9 set f 1    <--  4, 32
        registers['d']  = 2                         # 10 set d 2
        while True:
            registers['e']  = 2                     # 11 set e 2    <--  11
            while True:
                registers['g']  = registers['d']    # 12 set g d
                registers['g'] *= registers['e']    # 13 mul g e
                mul_instruction_counter += 1
                registers['g'] -= registers['b']    # 14 sub g b
                if registers['g'] == 0:             # 15 jnz g 2     --> 17
                    registers['f'] = 0              # 16 set f 0
                registers['e'] -= -1                # 17 sub e -1   <--  15
                registers['g']  = registers['e']    # 18 set g e
                registers['g'] -= registers['b']    # 19 sub g b
                if registers['g'] == 0:             # 20 jnz g -8    --> 12
                    break
            registers['d'] -= -1                    # 21 sub d -1
            registers['g']  = registers['d']        # 22 set g d
            registers['g'] -= registers['b']        # 23 sub g b
            if registers['g'] == 0:                 # 24 jnz g -13   --> 11
                break
        if registers['f'] == 0:                     # 25 jnz f 2     --> 27
            registers['h'] -= -1                    # 26 sub h -1
        registers['g']  = registers['b']            # 27 set g b    <--  25
        registers['g'] -= registers['c']            # 28 sub g c
        if registers['g'] == 0:                     # 29 jnz g 2     --> 31
            break
        # if 1 != 0:                                # 30 jnz 1 3     --> 33
        registers['b'] -= -17                       # 31 sub b -17  <--  29
        # if 1 != 0:                                # 32 jnz 1 -23   -->  9
                                                    # 33 EOL        <--  30
    return registers, mul_instruction_counter

def coprocessor_instructions_in_python_optimised_step_1(registers):
    """
    a indicates if b and c are initialised differently
    b initialised as 108_100, incremented by 17, until it equals c
    c initialised as 125_100, unchanged
    d initialised as 2, incremented by 1, while smaller than b
    e initialised as 2, incremented by 1, while smaller than b
    f initialised as 0, set to 1 if d*e == b -> breaks loop, reset to 2
    g -- auxiliary variable --
    h initialised as 0, incremented by 1 if f was set to 0 in inner loops
    """
    mul_instruction_counter = 0

    # Initialise b and c
    registers['b'] = 81
    if registers['a'] != 0:
        mul_instruction_counter += 1
        registers['b'] = registers['b'] * 100 + 100_000  # b = 108_100
        registers['c'] = registers['b'] + 17_000         # c = 125_100
    else:
        registers['c'] = registers['b']                  # c, b = 81, 81

    while True: # input: b, c, h -- changed: b, h -- reset: d, f
        registers['f'] = 1 # Reset findings indicator
        registers['d'] = 2
        while True: # input: d -- changed: d -- reset: e
            registers['e'] = 2
            while True: # input: b, d, e, f  -- changed: e, f
                mul_instruction_counter += 1
                if registers['d'] * registers['e'] - registers['b'] == 0:
                    registers['f'] = 0 # Indicates something was found
                registers['e'] += 1
                if registers['e'] - registers['b'] == 0: # e == b
                    break

            registers['d'] += 1
            if registers['d'] - registers['b'] == 0: # d == b
                break

        if registers['f'] == 0:
            registers['h'] += 1 # Collects the result
        if registers['b'] - registers['c'] == 0:
            break
        registers['b'] += 17

    return registers, mul_instruction_counter

def coprocessor_instructions_in_python_optimised_step_2(registers):
    """
    Count non-prime numbers between the values in registers b and c.
    Registers b and c are initialised beforehand and b is incremented by 17
    (step size) until it equals c.
    """
    mul_instruction_counter = 0

    # Initialise b and c
    registers['b'] = 81
    if registers['a'] != 0:
        registers['b'] = registers['b'] * 100 + 100_000  # b = 108_100
        mul_instruction_counter += 1
        registers['c'] = registers['b'] + 17_000         # c = 125_100
    else:
        registers['c'] = registers['b']                  # c, b = 81, 81

    while True: # input: b, c, -- changed: b, h
        registers['f'] = 1 # Reset findings indicator
        registers['d'] = 2
        while True:
            registers['e'] = 2
            mul_instruction_counter += (registers['b'] - registers['e'])
            if registers['b'] % registers['d'] == 0:
                registers['f'] = 0

            registers['d'] += 1
            if registers['d'] - registers['b'] == 0: # d == b
                break

        if registers['f'] == 0:
            registers['h'] += 1 # Collects the result
        if registers['b'] - registers['c'] == 0:
            break
        registers['b'] += 17 # 1,000 times

    return registers, mul_instruction_counter

def main():
    with open("day_23_instructions.txt", 'r') as instructions_file:
        instructions = instructions_file.readlines()
    registers = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0
    }
    registers, mul_instruction_counter = coprocessor(registers, instructions)
    print(f"Number of 'mul' instructions: {mul_instruction_counter}")

    registers = {
        'a': 1, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0
    }
    registers, mul_instruction_counter = coprocessor_instructions_in_python_optimised_step_2(registers)
    print(f"Register h (number of non-prime numbers): {registers['h']}")

if __name__ == '__main__':
    main()

