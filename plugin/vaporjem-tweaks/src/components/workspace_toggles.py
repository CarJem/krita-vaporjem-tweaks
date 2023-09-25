from krita import Krita, Extension
from PyQt5 import QtWidgets, QtGui
import os
import json
import sys
import importlib.util
from ..classes.config import *
from ..classes.resources import *

class WorkspaceToggles:

    def toggleWorkspace(self, path):
        main_menu = Krita.instance().activeWindow().qwindow().menuBar()
        for root_items in main_menu.actions():
            if root_items.objectName() == 'window':
                for sub_item in root_items.menu().actions():
                    if sub_item.text() == 'Wor&kspace':
                        for workspace in sub_item.menu().actions():
                            if workspace.text() == path:
                                workspace.trigger()
                                break
                break

    def addWorkspace(self, window, menu, actionName, id, text, actionPath):
        action = window.createAction(actionName, "Workspace: " + text, actionPath)    
        icon = ResourceManager.iconLoader(id, 'workspaces', True)
        action.setIcon(icon)

        menu.addAction(action)
        action.triggered.connect(lambda: self.toggleWorkspace(id))

    def reloadWorkspaces(self):
        cfg = ConfigManager.getJSON()

        Workspaces = []
        main_menu = Krita.instance().activeWindow().qwindow().menuBar()

        for root_items in main_menu.actions():
            if root_items.objectName() == 'window':
                for sub_item in root_items.menu().actions():
                    if sub_item.text() == 'Wor&kspace':
                        for workspace in sub_item.menu().actions():
                            if workspace.isSeparator():
                                break
                            else:
                                action = Config_Workspace()
                                action.display_name = workspace.text()
                                action.id = workspace.text()
                                Workspaces.append(action)
                break
        
        cfg.workspaces = Workspaces
        cfg.save()

    def createActions(self, window, actionPath):

        sectionName = "VaporJem_Workspaces"
        root = window.createAction(sectionName, "Workspaces", actionPath)
        root_menu = QtWidgets.QMenu(sectionName, window.qwindow())
        root.setMenu(root_menu)

        subItemPath = actionPath + "/" + sectionName

        cfg = ConfigManager.getJSON()
        for workspace in cfg.workspaces:
            self.addWorkspace(window, root_menu, 'WorkspaceToggles_{0}'.format(workspace.id), workspace.id, '{0}'.format(workspace.display_name), subItemPath)