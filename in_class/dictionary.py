# what will this code print?
words = {
	"más": "more",
	"otro": "other",
	"agua": "water"
}

first_word = "agua"
print(words[first_word])

# does this work? Why or why not?
print(words[0])

# what will this print?
spiders = {
  "smeringopus": {
    "name": "Pale Daddy Long-leg",
    "length": 7
  },
  "holocnemus pluchei": {
    "name": "Marbled cellar spider",
    "length": (5, 7)
  }
}

print(spiders["holocnemus pluchei"]["length"])
