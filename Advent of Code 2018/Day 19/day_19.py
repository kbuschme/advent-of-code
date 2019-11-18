from collections import namedtuple, defaultdict
"""
Advent of Code 2018

https://adventofcode.com/2018/day/19

--- Day 19: Go With The Flow ---

With the Elves well on their way constructing the North Pole base, you turn
your attention back to understanding the inner workings of programming the
device.

You can't help but notice that the device's opcodes don't contain any flow
control like jump instructions. The device's manual goes on to explain:

"In programs where flow control is required, the instruction pointer can be
bound to a register so that it can be manipulated directly. This way,
setr/seti can function as absolute jumps, addr/addi can function as relative
jumps, and other opcodes can cause truly fascinating effects."

This mechanism is achieved through a declaration like #ip 1, which would
modify register 1 so that accesses to it let the program indirectly access
the instruction pointer itself. To compensate for this kind of binding,
there are now six registers (numbered 0 through 5); the five not bound to
the instruction pointer behave as normal. Otherwise, the same rules apply
as the last time you worked with this device
(https://adventofcode.com/2018/day/16).

When the instruction pointer is bound to a register, its value is written to
that register just before each instruction is executed, and the value of
that register is written back to the instruction pointer immediately after
each instruction finishes execution. Afterward, move to the next instruction
by adding one to the instruction pointer, even if the value in the
instruction pointer was just updated by an instruction. (Because of this,
instructions must effectively set the instruction pointer to the instruction
before the one they want executed next.)

The instruction pointer is 0 during the first instruction, 1 during the
second, and so on. If the instruction pointer ever causes the device to
attempt to load an instruction outside the instructions defined in the
program, the program instead immediately halts. The instruction pointer
starts at 0.

It turns out that this new information is already proving useful: the CPU
in the device is not very powerful, and a background process is occupying
most of its time. You dump the background process' declarations and
instructions to a file (your puzzle input), making sure to use the names
of the opcodes rather than the numbers.

For example, suppose you have the following program:

#ip 0
seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5

When executed, the following instructions are executed. Each line contains
the value of the instruction pointer at the time the instruction started,
the values of the six registers before executing the instructions (in square
brackets), the instruction itself, and the values of the six registers after
executing the instruction (also in square brackets).

ip=0 [0, 0, 0, 0, 0, 0] seti 5 0 1 [0, 5, 0, 0, 0, 0]
ip=1 [1, 5, 0, 0, 0, 0] seti 6 0 2 [1, 5, 6, 0, 0, 0]
ip=2 [2, 5, 6, 0, 0, 0] addi 0 1 0 [3, 5, 6, 0, 0, 0]
ip=4 [4, 5, 6, 0, 0, 0] setr 1 0 0 [5, 5, 6, 0, 0, 0]
ip=6 [6, 5, 6, 0, 0, 0] seti 9 0 5 [6, 5, 6, 0, 0, 9]

In detail, when running this program, the following events occur:

  * The first line (#ip 0) indicates that the instruction pointer should be
    bound to register 0 in this program. This is not an instruction, and so
    the value of the instruction pointer does not change during the processing
    of this line.
  * The instruction pointer contains 0, and so the first instruction is
    executed (seti 5 0 1). It updates register 0 to the current instruction
    pointer value  (0), sets register 1 to 5, sets the instruction pointer
    to the value of register 0 (which has no effect, as the instruction did
    not modify register 0), and then adds one to the instruction pointer.
  * The instruction pointer contains 1, and so the second instruction,
    seti 6 0 2, is executed. This is very similar to the instruction before
    it: 6 is stored in register 2, and the instruction pointer is left with
    the value 2.
  * The instruction pointer is 2, which points at the instruction addi 0 1 0.
    This is like a relative jump: the value of the instruction pointer, 2, is
    loaded into register 0. Then, addi finds the result of adding the value
    in register 0 and the value 1, storing the result, 3, back in register 0.
  * Register 0 is then copied back to the instruction pointer, which will
    cause it to end up 1 larger than it would have otherwise and skip the next
    instruction (addr 1 2 3) entirely. Finally, 1 is added to the instruction
    pointer.
  * The instruction pointer is 4, so the instruction setr 1 0 0 is run.
    This is like an absolute jump: it copies the value contained in register
    1, 5, into register 0, which causes it to end up in the instruction
    pointer. The instruction pointer is then incremented, leaving it at 6.
  * The instruction pointer is 6, so the instruction seti 9 0 5 stores 9 into
    register 5. The instruction pointer is incremented, causing it to point
    outside the program, and so the program ends.

What value is left in register 0 when the background process halts?

Your puzzle answer was 1848.

--- Part Two ---

A new background process immediately spins up in its place. It appears
identical, but on closer inspection, you notice that this time, register 0
started with the value 1.

What value is left in register 0 when this new background process halts?

Your puzzle answer was 22157688.
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

def parse_program(program):
    instruction_pointer = int(program[0].split()[1])
    instructions = []
    for line in program[1:]:
        opcode, in_1, in_2, out = line.split()
        instructions.append((opcode, int(in_1), int(in_2), int(out)))
    return instructions, instruction_pointer

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

def execute_program(program, ip_register, registers=None, verbose=False):
    if registers is None:
        registers = [0, 0, 0, 0, 0, 0]
    running = True
    log = []
    while running:
        if verbose:
            message = [
                f"ip={registers[ip_register]}",
                registers[:],
                " ".join(str(each) for each in program[registers[ip_register]])
            ]

        registers = execute_instruction(*program[registers[ip_register]],
                                        registers)

        if verbose:
            message.append(registers[:])
            log.append(tuple(message))
        registers[ip_register] += 1
        if registers[ip_register] >= len(program):
            running = False

    if verbose:
        return log
    return registers

# --- Optimised program below ---
def main_loop(registers):
    registers[3] = 1                                          #  1 seti 1  9 3

    run_outer_loop = True
    while run_outer_loop:
        registers[2] = 1                                      #  2 seti 1  6 2
        run_inner_loop = True

        while run_inner_loop:
            registers[5] = registers[3] * registers[2]        #  3 mulr 3  2 5

            if registers[5] == registers[1]:                  #  4 eqrr 5  1 5
                registers[0] += registers[3]                  #  7 addr 3  0 0
                registers[5] = 1
            else:
                registers[5] = 0
            registers[2] += 1                                 #  8 addi 2  1 2

            if registers[2] > registers[1]:                   #  9 gtrr 2  1 5
                run_inner_loop = False
                registers[3] += 1                             # 12 addi 3  1 3
                registers[5] = 1
            else:
                registers[5] = 0

        if registers[3] > registers[1]:                       # 13 gtrr 3  1 5
            run_outer_loop = False
            registers[5] = 1
        else:
            registers[5] = 0

    # Before exiting: Set register 4
    registers[4] = 16**2 + 1
    return registers

def main_loop_pythonic(registers):
    """Return the sum of all divisors of register[1]."""
    target = registers[1]
    result = 0
    for factor_1 in range(1, target+1):
        for factor_2 in range(1, target+1):
            if factor_1 * factor_2 == target:
                result += factor_2
    registers[4] = 16**2 + 1
    registers[5] = 1
    return [result, target, factor_1+1, factor_2+1, registers[4], registers[5]]

def main_loop_optimised(registers):
    """Return the sum of all divisors of register[1]."""
    target = registers[1]
    divisors = []
    for divisor in range(1, target+1):
        if target % divisor == 0:
            divisors.append(divisor)
    result = sum(divisors)
    registers[4] = 16**2 + 1
    registers[5] = 1
    return [result, target, target+1, target+1, registers[4], registers[5]]

def execute_translated_program(registers=None,
        main_loop_fun=main_loop_optimised, verbose=False):
    if registers is None:
        registers = [0, 0, 0, 0, 0, 0]

    registers[1] = (registers[1] + 2)**2 * 19 * 11  # (0+2)**2*19*11 = 836
    registers[5] = (registers[5] + 1) * 22 + 2      #   (0+1)*22 + 2 = 24
    registers[1] += registers[5]                    #       836 + 24 = 860

    # Depending on register 0, continue initialising, start main loop or halt
    if registers[0] >= 10:
        return registers

    if registers[0] == 1:
        registers[5] = (27 * 28 + 29) * 30 * 14 * 32 #
    elif registers[0] == 2:
        registers[5] = (registers[5] * 28 + 29) * 30 * 14 * 32
    elif registers[0] == 3:
        registers[5] = (registers[5] + 29) * 30 * 14 * 32
    elif registers[0] == 4:
        registers[5] = registers[5] * 30 * 14 * 32
    elif registers[0] == 5:
        registers[5] = registers[5] * 14 * 32
    elif registers[0] == 6:
        registers[5] = registers[5] * 32

    if 0 < registers[0] <= 7:
        registers[1] += registers[5]
    if 0 < registers[0] <= 8:
        registers[0] = 0

    registers[4] = 1

    if verbose:
        print(f"Set-up complete: {registers}")
    return main_loop_fun(registers)

def main():
    program = []
    with open('day_19_program.txt', 'r') as program_file:
        program = program_file.read().splitlines()

    program, ip_register = parse_program(program)
    registers = execute_program(program, ip_register)
    print(f"Register 0: {registers[0]}")

    registers = [1, 0, 0, 0, 0, 0]
    registers = execute_translated_program(registers)
    print(f"Register 0 (optimised program): {registers[0]}")

if __name__ == '__main__':
    main()
