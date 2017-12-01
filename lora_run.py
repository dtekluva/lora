import datawriter as source
import re

brain = source.from_jason()
recurence = []
previous  = []
chosen_reply = {"index": 0, "probability": 0}
alt_reply    = {"index": 0, "probability": 0}

def converse(recurence, chosen_reply, alt_reply):

    user_input = input("Ask me a question : ")
    user = re.split(" ;|-| ", user_input )
    if user_input :
        import correction
        if not correction.check(user_input) >= 1:
            global previous
            previous = []
            previous.append(user_input)

    quest_iter   = 0
    for question in brain["questions"]:

        if alt_reply["probability"] > chosen_reply["probability"] and len(recurence) != 0:
            chosen_reply["index"]       = alt_reply["index"]
            chosen_reply["probability"] = alt_reply["probability"]

        new_sentence = re.split(" ;|-|,| ", question )
        prob_iter   = 0
        quest_iter += 1

        for word in user:

            for text in new_sentence:

                if word == text:
                    prob_iter += 1

            recurence.append(prob_iter)

        alt_reply["index"]       = quest_iter
        alt_reply["probability"] = (recurence[len(recurence)-1])

    print(chosen_reply)
    print("\n",brain["answers"][chosen_reply["index"]-1], "\n")
    print(recurence)

    main(user_input)


def main(user_input):

    if user_input :
        import correction
        if correction.check(user_input) >= 2:
            import learn
            learn.begin(previous[0])   

    recurence = []
    chosen_reply = {"index": 0, "probability": 0}
    alt_reply    = {"index": 0, "probability": 0}

    converse(recurence, chosen_reply, alt_reply)

main("")