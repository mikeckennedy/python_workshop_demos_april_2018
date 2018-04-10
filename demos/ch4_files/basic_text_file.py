from models import Notebook, TextNote, VideoNote

bio = Notebook("Bio 201 Notes")

bio.notes.append(TextNote("This is the first day of Bio 201"))
bio.notes.append(TextNote("Final exam is 95%."))
bio.notes.append(VideoNote("https://www.youtube.com/watch?v=PKffm2uI4dk"))

bio.display()
bio.save("bio201.txt")
bio.load("bio201.txt")

print(bio.to_json())
