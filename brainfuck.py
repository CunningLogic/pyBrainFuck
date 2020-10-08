import readchar

code = ''
ptr = 0
pc = 0
cells = bytearray(b'\x00' * 1000)
braces = {}


def map_braces(insn):
    global braces
    for pc in range(0, len(insn)):
        if insn[pc] is '[':
            c = 0
            for i in range(pc + 1, len(insn)):
                if insn[i] is '[':
                    c += 1
                elif insn[i] is ']':
                    if c is not 0:
                        c -= 1
                    else:
                        braces[pc] = i
                        break


def run(insn):
    global code
    global ptr
    global pc
    global cells
    global braces
    code = insn
    progress = ''
    map_braces(code)
    while pc < len(code):
        progress += code[pc]

        op = opcodes.get(code[pc])
        pc += 1
        op()


def inc_ptr():
    global ptr
    ptr += 1


def dec_ptr():
    global ptr
    ptr -= 1


def inc():
    global ptr
    global cells
    cells[ptr] += 1


def dec():
    global ptr
    global cells
    cells[ptr] -= 1


def write():
    print(chr(cells[ptr]), end='')


def read():
    global ptr
    global cells
    c = readchar.readchar()
    cells[ptr] = c


def start_loop():
    global pc
    global ptr
    global cells
    global braces
    if cells[ptr] is 0:
        pc = braces[pc - 1] + 1


def end_loop():
    global pc
    global ptr
    global cells
    global braces
    if cells[ptr] is not 0:
        jump = list(braces.keys())[list(braces.values()).index(pc - 1)]
        pc = jump


opcodes = {
    '>': inc_ptr,
    '<': dec_ptr,
    '+': inc,
    '-': dec,
    '.': write,
    ',': read,
    '[': start_loop,
    ']': end_loop,
}
