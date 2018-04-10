import datetime


class Notebook:
    def __init__(self, name):
        self.name = name
        self.created = datetime.datetime.now()
        self.notes = []

    def save(self, filename):
        print(f"Would save {self.name} to {filename}")

    def display(self):
        print("---------------------------------")
        print(f" NOTEBOOK: {self.name}")
        print("---------------------------------")
        print()
        for note in self.notes:
            note.display()
        print()

    # def add_note(self, note):
    #     if not isinstance(note, Note):
    #         raise Exception("Wrong type...")
    #     self.notes.append(note)


class Note:
    def __init__(self):
        self.created = datetime.datetime.now()

    def display(self):
        print(f'Generic note created at {self.created}.')

    def seconds(self):
        t0 = datetime.datetime.now()
        dt = t0 - self.created
        return dt.total_seconds()


class VideoNote(Note):
    def __init__(self, video_url):
        super().__init__()
        self.video_url = video_url

    def display(self):
        print(f"[{self.seconds()} sec] Click to play: {self.video_url}")


class TextNote(Note):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def display(self):
        print(f"TEXT: [{self.seconds()} sec] {self.text}")



n = Notebook("Biology")

while True:
    cmd = input("What now? [v]ideo note, [t]ext note, [s]how, e[x]it? ")
    if cmd == 'v':
        url = input("What is the URL of the video? ")
        vn = VideoNote(url)
        n.notes.append(vn)
    elif cmd == 't':
        text = input("What is the text? ")
        tn = TextNote(text)
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
