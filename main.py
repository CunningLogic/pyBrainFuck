import brainfuck as bf


def main():
    helloworld = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
    bf.run(helloworld)


if __name__ == '__main__':
    main()
