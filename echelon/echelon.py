from aqt import mw
from aqt.browser import Browser
from aqt.qt import QIcon, QAction, QMenu, QCursor, QInputDialog, QLineEdit, QMessageBox
from anki.hooks import wrap

from . import SEPARATOR, FULL_TAG, DEPTH
from .rename import rename, verify


def _userTagTree(self, root, _old):
    tags = sorted(getHiers(self.col.tags.all()))
    tags_tree = {}

    for t in tags:
        if isParent(t):

            def fil_func(partial_tag=t):
                return self.setFilter(
                    "(tag:" + partial_tag + " or tag:" + partial_tag + SEPARATOR + "*)"
                )

        else:

            def fil_func(partial_tag=t):
                return self.setFilter("tag", partial_tag)

        if genParent(t) == "":
            parent = root
        else:
            parent = tags_tree[genParent(t)]

        item = self.CallbackItem(parent, formatted(t), fil_func)
        item.full_name = t
        item.is_tag = True
        item.setIcon(0, QIcon(":/icons/tag.svg"))

        tags_tree[t] = item

    self.sidebarTree.expandToDepth(DEPTH)


def formatted(tag):
    if FULL_TAG:
        # full tag with parents and sep
        return tag
    else:
        # only last sub-tag
        return tag.split(SEPARATOR)[-1]


def isParent(tag):
    tags = mw.col.tags.all()
    for t in tags:
        if tag == genParent(t):
            return True
    return False


def genParent(tag):
    parts = tag.split(SEPARATOR)
    if len(parts) < 2:
        return ""
    else:
        return SEPARATOR.join(parts[:-1])


def getHier(name):
    res = []
    parts = name.split(SEPARATOR)

    for x in range(len(parts)):
        res.append(SEPARATOR.join(parts[: (x + 1)]))
    return res


def getHiers(tags):
    tmp = []
    for t in tags:
        tmp += getHier(t)
    return list(set(tmp))


def customMenuEvent(self, event):
    try:
        event.button = lambda: False
        self.menu = QMenu(self)
        a_rename = QAction("Rename Tag", self)
        a_rename.triggered.connect(lambda x: renameAction(self, event))
        self.menu.addAction(a_rename)
        # add other required actions
        self.menu.popup(QCursor.pos())
    except:
        pass


def renameAction(self, event):
    try:
        row = self.sidebarTree.currentItem().full_name
    except:
        QMessageBox.about(self, "Title", "Item not a Tag")
        return
    q, status = QInputDialog.getText(self, "Rename Tag", 'Rename Tag:"%s" as:' % row)
    if status and verify(q):
        rename(row, q)
    elif status and not verify(q):
        QMessageBox.about(self, "Title", "Invalid Tag Name")


def modInit(self, mw):
    self.sidebarTree.contextMenuEvent = lambda x: customMenuEvent(self, x)


Browser._userTagTree = wrap(Browser._userTagTree, _userTagTree, "around")
Browser.__init__ = wrap(Browser.__init__, modInit, "after")
