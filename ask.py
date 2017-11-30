import datawriter as loader

dataset = loader.from_jason()


def quiz():
    iter = 0
    for question in dataset["questions"]:
        answer = input(question + " : ")
        
        if answer != dataset["answers"][iter] :
            print("Sorry that was wrong")
            print(dataset["answers"][iter])

        iter += 1

quiz()