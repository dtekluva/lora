print("Loading")
import datawriter as writer

def ready():
    data = writer.from_jason()
    return data

def write(source):
    writer.to_jason(source)


def begin(quest_input):
    source = ready()

    if len(quest_input) < 1:
        quest_input = input("Please ask me a question: ")
        ans_input   = input("pleeease tell me the answer: ")

    if len(quest_input) > 2:
        ans_input   = input("please tell how to answer that question : ")

    source["questions"].append(quest_input)
    source["answers"].append(ans_input)
    write(source)
    print("\n Thanks i'll remember that next time \n")

    

