from aqt import mw

config = mw.addonManager.getConfig(__name__)

# Separator used between hierarchies
SEPARATOR = config["separator"]
DEPTH = config["default_depth"]


from . import echelon
