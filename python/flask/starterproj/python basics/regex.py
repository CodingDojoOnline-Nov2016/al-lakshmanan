import re

def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
    for elem in words:
        if re.search(regex, elem):
            print elem
        else:
            print "none"

pttrn = "[v]"
get_matching_words(pttrn)

pttrn = "s{2}"
get_matching_words(pttrn)

pttrn = "\we$"
get_matching_words(pttrn)

pttrn = "[aeiou]"
get_matching_words(pttrn)
