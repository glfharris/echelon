from aqt import mw

config = mw.addonManager.getConfig(__name__)

# Separator used between hierarchies
SEPARATOR = config["separator"]

# Display full tag name (with parents and Separator) or only the sub-tag
FULL_TAG = config["full_tag"]

DEPTH = config["default_depth"]

from . import echelon
