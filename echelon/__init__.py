from aqt import mw

def get_config():
    return mw.addonManager.getConfig(__name__)

config = get_config()
DEPTH = config["default_depth"]
SEPARATOR = config["separator"]
FULL_TAG = config["full_tag"]

from . import echelon
