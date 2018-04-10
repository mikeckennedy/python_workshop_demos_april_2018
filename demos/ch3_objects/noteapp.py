import models
# from models import Notebook, TextNote, VideoNote

n = models.Notebook("Biology")

while True:
    cmd = input("What now? [v]ideo note, [t]ext note, [s]how, e[x]it? ")
    if cmd == 'v':
        url = input("What is the URL of the video? ")
        vn = models.VideoNote(url)
        n.notes.append(vn)
    elif cmd == 't':
        text = input("What is the text? ")
        tn = models.TextNote(text)
        n.notes.append(tn)
    elif cmd == 's':
        n.display()
    elif cmd == 'x':
        print("kthxbye")
        break
    print()

# Naming conventions
# variables: thing1, new_thing <-- snake case
# function: same
# file/module/package: same
# Type: CapWord
# Constants: ALL_CAPS
# Variations:
# _thing <-- semiprivate (protected)
# __thing <-- private
# __eq__() <-- magic methods
