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
    excuse_parts = []
    excuse_parts.append(random.choice(excuse_starters))
    excuse_parts.append(random.choice(excuse_reasons))
    excuse_parts.append(random.choice(excuse_endings))
    return " ".join(excuse_parts)

#user input for customization
num_excuses = int(input("Enter the number of excuses to generate: "))

#Generate and excuses in bulk 
print("Generated Excuses: ")
for _ in range(num_excuses):
    excuse = generate_excuse();
    print(excuse)
    print("-" * 40) #separator for better readability 