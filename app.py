import random

excuse_starters = [
    "Hey coach I'm sorry, but",
    "Unfortunately",
    "Due to unforeseen circumstances,"
]

excuse_reasons = [
    "I didn't eat the whole day",
    "my dog ate my knee sleeves",
    "I only had 3 hours of sleep and one Redbull today",
    "I forgot to drink my creatine",
    "I had rpe 11 squat yesterday"
]

excuse_endings = [
    "so my lifts didn't show up today.",
    "so I pulled my back.",
    "and deadlifts felt heavy today.",
    "and I couldn't lift a plate."
]


def generate_excuse():
    #Random Generator
    random_starter = random.choice(excuse_starters)
    random_reason = random.choice(excuse_reasons)
    random_ending = random.choice(excuse_endings)
    
    #Concatenate all the excuses 
    final_excuse = random_starter + " " + random_reason + " " + random_ending
    return final_excuse

#print the excuse 
print("Generating Excuse: ")
print(final_excuse)
