from aqt import mw

config = mw.addonManager.getConfig(__name__)

# Separator used between hierarchies
SEPARATOR = config['separator']


from . import echelon
