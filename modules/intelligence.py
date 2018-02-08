import markovify

with open("modules/personality/jesus.txt") as f:
    text = f.read()

text_model = markovify.NewlineText(text)

def generate():
    return text_model.make_short_sentence(140)