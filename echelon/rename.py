from anki import notes
from aqt import mw

from . import SEPARATOR

def rename(old_name, new_name):
    tags = mw.col.tags.all()
    rename_dict = {old_name : new_name} # {old : new}

    for tag in tags:
        parts = tag.split(SEPARATOR)
        for i in range(len(parts)):
            if old_name == SEPARATOR.join(parts[:i]):
                retained_stub = SEPARATOR.join(parts[i:len(parts)])
                rename_dict[tag] = SEPARATOR.join([new_name, retained_stub])
    
    mw.checkpoint("Rename Tag")
    mw.progress.start()
    nids = mw.col.db.list('select id from notes')
    for id in nids:
        note = mw.col.getNote(id)

        for k,v, in rename_dict.items():
            if note.hasTag(k):
                note.delTag(k)
                note.addTag(v)
                note.flush()
    mw.reset()
    mw.progress.finish()

def verify(name):
    if name.endswith(SEPARATOR):
        return False
    if name.startswith(SEPARATOR):
        return False
    if ' ' in name:
        return False
    if '' is name:
        return False

    return True
    

if __name__ == '__main__':
    print(rename('a::b::c::d', 'hello'))