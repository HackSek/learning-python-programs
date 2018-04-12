martial_arts_dictionary = {
    "Thailand": "Muay Thai",
    "Brazil": "BJJ",
    "South Korea": "Tae Kwon Do",
    "Japan": "Judo",
    "United Kingdom": "Boxing",
    "Netherlands": "Kickboxing"
}

martial_arts_dictionary_b = dict(
    Thailand = "Muay Thai",
    Brazil = "BJJ",
    South_Korea = "Tae Kwon Do",
    Japan = "Judo",
    United_Kingdom = "Boxing",
    Netherlands = "Kickboxing"
)

keys = list(martial_arts_dictionary.keys())
values = list(martial_arts_dictionary.values())

print(keys)
print(values)
print(keys.count('Chile'))
print(martial_arts_dictionary_b.items())
