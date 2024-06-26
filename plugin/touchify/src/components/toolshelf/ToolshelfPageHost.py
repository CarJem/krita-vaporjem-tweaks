from typing import Dict
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from ...cfg.CfgToolshelf import CfgToolboxPanel
from ...cfg.CfgToolshelf import CfgToolboxPanelDocker

from ...docker_manager import DockerManager

class ToolshelfPageHost(QWidget):


    def __init__(self, parent: QStackedWidget, ID: any):
        super(ToolshelfPageHost, self).__init__(parent)

        self.toolshelfRoot: QStackedWidget = parent
        self.ID = ID

        self.shelfLayout = QVBoxLayout()
        self.shelfLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.shelfLayout)

    def unloadDockers(self):
        pass

    def loadDockers(self):
        pass

    def activate(self):
        self.parentWidget().changePanel(self.ID)

    def setSizeHint(self, size):
        pass

    def sizeHint(self):
        return super().sizeHint()

    

    