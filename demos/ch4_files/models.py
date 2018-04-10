import datetime
import os


class Notebook:
    def __init__(self, name):
        self.name = name
        self.created = datetime.datetime.now()
        self.notes = []

    def save(self, filename):
        # fout = open(filename, 'w', encoding='utf-8')
        #
        # fout.write("{}\n".format(self.name))
        # for note in self.notes:
        #     fout.write(f"{note}\n")
        #
        # fout.close()

        full_name = os.path.abspath( os.path.join('data', filename) )
        with open(full_name, 'w', encoding='utf-8') as fout:
            fout.write("{}\n".format(self.name))
            for note in self.notes:
                fout.write(f"{note}\n")

    def load(self, filename):
        full_name = os.path.abspath(os.path.join('data', filename))
        with open(full_name, 'r', encoding='utf-8') as fin:
            print("LOADED --->")
            title = fin.readline()
            print("TITLE: " + title.rstrip())
            lines = fin.readlines()
            for l in lines:
                print("LINE: " + l.rstrip())

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

    def to_json(self):
        data = {'name': self.name, 'notes': []}
        for n in self.notes:
            data['notes'].append(n.to_json())

        return data




class Note:
    def __init__(self):
        self.created = datetime.datetime.now()

    def display(self):
        print(f'Generic note created at {self.created}.')

    def seconds(self):
        t0 = datetime.datetime.now()
        dt = t0 - self.created
        return dt.total_seconds()

    def to_json(self):
        data = dict(self.__dict__)
        data['created'] = data['created'].isoformat()
        return data


class VideoNote(Note):
    def __init__(self, video_url):
        super().__init__()
        self.video_url = video_url

    def __repr__(self):
        return "VideoNote: url=" + self.video_url

    def display(self):
        print(f"[{self.seconds()} sec] Click to play: {self.video_url}")


class TextNote(Note):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def __repr__(self):
        return "TextNote: text=" + self.text

    def display(self):
        print(f"TEXT: [{self.seconds()} sec] {self.text}")



# https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python
# import tkinter as tk
# from tkinter import filedialog
#
# root = tk.Tk()
# root.withdraw()
#
# file_path = filedialog.askopenfilename()
