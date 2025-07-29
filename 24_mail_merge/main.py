with open("Input/Letters/starting_letter.txt") as template_file:
    template = template_file.read()
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

for name in names:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode='w') as letter_file:
        letter_file.write(template.replace("[name]", name.strip()))