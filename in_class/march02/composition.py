# function composition
def happy(text):
    return "☻" + text + "☻"

def sad(text):
    return "☹" + text + "☹"

def composer(f, g):
    def composed(x):
        return f(g(x))
    return composed

print(sad(happy("CS 111!")))

msg1 = composer(sad, happy)("CS 111!")
print(msg1)

composed = composer(sad, happy)
print(composed("CS 111!"))


# function composition 2
def happy(text):
    return "☻" + text + "☻"

def make_texter(emoji):
    def texter(text):
        return emoji + text + emoji
    return texter

def composer(f, g):
    def composed(x):
        return f(g(x))
    return composed

print(composer(happy, make_texter("☃︎"))('snow day!'))
