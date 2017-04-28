from prac7.programminglanguage import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    languages = ["ruby"]
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    languages.append("python")
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    languages.append("vb")

    print(ruby)

    print("\nThe dynamically typed languages are:")
    for i in languages:
        #if i.is_dynamic():
            print(i)


main()