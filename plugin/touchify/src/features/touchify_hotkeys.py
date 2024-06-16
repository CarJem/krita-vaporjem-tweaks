from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *

from ..docker_manager import DockerManager

from ..variables import KRITA_ID_ACTIONS_SETTINGS_ROOT, TOUCHIFY_AID_LOCK_FLOATING_DOCKERS, TOUCHIFY_ID_ACTIONS_HOTKEY
from ..config import *
from ..components.nu_tools.NtToolbox import NtToolbox
from ..components.nu_tools.NtToolOptions import NtToolOptions
from .. import stylesheet
from PyQt5.QtWidgets import QMessageBox



from krita import *
    
class TouchifyHotkeys:

    def createActions(self, window, subItemPath):
        for i in range(1, 10):
            hotkeyName = '{0}_{1}'.format(TOUCHIFY_ID_ACTIONS_HOTKEY, str(i))
            hotkeyAction = window.createAction(hotkeyName, "Custom action: " + str(i), subItemPath)
            ConfigManager.instance().addHotkey(i, hotkeyAction)

        dockerFloatLockAction = window.createAction(TOUCHIFY_AID_LOCK_FLOATING_DOCKERS, "Lock Floating Dockers", KRITA_ID_ACTIONS_SETTINGS_ROOT)
        dockerFloatLockAction.toggled.connect(self.toggleAction)
        dockerFloatLockAction.setCheckable(True)
        dockerFloatLockAction.setChecked(False)

    def toggleAction(self, value=None):
        DockerManager.instance().toggleLockFloatingDockers(value)
