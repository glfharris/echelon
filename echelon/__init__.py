from aqt import mw

def get_config():
    return mw.addonManager.getConfig(__name__)

from . import echelon
