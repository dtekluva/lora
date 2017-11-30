import re


reference   = ["you", "sorry", "that", "was", "wrong", "answer"]

def check(input):
    probability = 0

    new_sentence = re.split(" ;|-|,| ", input )

    if "lora" in input and "wrong" in input:
        for word in new_sentence:
            if word in reference:
                probability += 1
    
        return probability

    else:
        return 0
    