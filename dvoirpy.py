import re

DATA_TEXT = "Je suis allé #visiter la tour #Eiffel hier! C'était incroyable #Paris. Je vais certainement y retourner! #"
def remplacerHashtagparlink(value):
    return re.sub("#[\w]+", lambda x: "<a href=''>{}</a>".format(x.group()), value)
print(remplacerHashtagparlink(DATA_TEXT))