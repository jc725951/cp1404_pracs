from programming_languages import ProgrammingLanguage

def main():

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    programming_language = [ruby, python, visual_basic]

    print("The dynamically typed languages are:")
    for language in programming_language:
        if language.is_dynamic():
            print(language.name)

main()