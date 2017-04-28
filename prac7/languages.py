from prac7.programminglanguage import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)

    #for i in :
    #    print(i)

    print(dir(ProgrammingLanguage))

main()