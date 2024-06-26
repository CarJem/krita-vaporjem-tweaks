from re import A
from ..ext.typedlist import TypedList
from ..ext.extensions import Extensions

class CfgToolboxPanelDocker:
    id: str = ""
    size_x: int = 0
    size_y: int = 0
    nesting_mode: str = "normal"
    panel_y: int = 0

    def create(args):
        obj = CfgToolboxPanelDocker()
        Extensions.dictToObject(obj, args)
        return obj

    def __str__(self):
        name = self.id.replace("\n", "\\n")
        return name

    def propertygrid_labels(self):
        labels = {}
        labels["id"] = "Docker ID"
        labels["size_x"] = "Docker Width (leave unset for auto)"
        labels["size_y"] = "Docker Height (leave unset for auto)"
        labels["panel_y"] = "Panel Row"
        labels["nesting_mode"] = "Nesting Mode"
        return labels

    def propertygrid_groups(self):
        groups = {}
        return groups

    def propertygrid_restrictions(self):
        restrictions = {}
        restrictions["id"] = {"type": "docker_selection"}
        restrictions["nesting_mode"] = {"type": "values", "entries": ["normal", "docking"]}
        restrictions["panel_x"] = {"type": "range", "min": 0, "max": 10}
        restrictions["panel_y"] = {"type": "range", "min": 0, "max": 10}
        return restrictions

class CfgToolboxPanel:
    id: str = ""
    icon: str = ""
    size_x: int = 0
    size_y: int = 0
    isEnabled: bool = False
    row: int = 0
    additional_dockers: TypedList[CfgToolboxPanelDocker] = []

    def create(args):
        obj = CfgToolboxPanel()
        Extensions.dictToObject(obj, args)
        additional_dockers = Extensions.default_assignment(args, "additional_dockers", [])
        obj.additional_dockers = Extensions.list_assignment(additional_dockers, CfgToolboxPanelDocker)
        return obj

    def forceLoad(self):
        self.additional_dockers = TypedList(self.additional_dockers, CfgToolboxPanelDocker)

    def __str__(self):
        name = self.id.replace("\n", "\\n")
        if not self.isEnabled:
            name = "(Disabled) " + name
        return name

    def propertygrid_labels(self):
        labels = {}
        labels["id"] = "Panel ID (must be unique)"
        labels["icon"] = "Display Icon"
        labels["isEnabled"] = "Active"
        labels["size_x"] = "Panel Width"
        labels["size_y"] = "Panel Height"
        labels["row"] = "Tab Row"
        labels["additional_dockers"] = "Dockers"
        return labels

    def propertygrid_groups(self):
        groups = {}
        return groups

    def propertygrid_restrictions(self):
        restrictions = {}
        restrictions["icon"] = {"type": "icon_selection"}
        return restrictions

class CfgToolboxAction:
    id: str = ""
    icon: str = ""
    row: int = 0
    isEnabled: bool = False

    def create(args):
        obj = CfgToolboxAction()
        Extensions.dictToObject(obj, args)
        return obj

    def __str__(self):
        name = self.id.replace("\n", "\\n")
        if not self.isEnabled:
            name = "(Disabled) " + name
        return name

    def forceLoad(self):
        pass

    def propertygrid_labels(self):
        labels = {}
        labels["id"] = "Action ID"
        labels["icon"] = "Display Icon"
        labels["isEnabled"] = "Active"
        labels["row"] = "Tab Row"
        return labels

    def propertygrid_groups(self):
        groups = {}
        return groups

    def propertygrid_restrictions(self):
        restrictions = {}
        restrictions["icon"] = {"type": "icon_selection"}
        restrictions["id"] = {"type": "action_selection"}
        return restrictions

class CfgToolshelf:

    panels: TypedList[CfgToolboxPanel] = []
    actions: TypedList[CfgToolboxAction] = []
    
    titleButtonHeight: int = 10
    dockerButtonHeight: int = 32
    dockerBackHeight: int = 16
    sliderHeight: int = 16
    actionHeight: int = 16

    def create(args):
        obj = CfgToolshelf()
        Extensions.dictToObject(obj, args)
        panels = Extensions.default_assignment(args, "panels", [])
        obj.panels = Extensions.list_assignment(panels, CfgToolboxPanel)
        actions = Extensions.default_assignment(args, "actions", [])
        obj.actions = Extensions.list_assignment(actions, CfgToolboxAction)
        return obj
    
    def forceLoad(self):
        self.panels = TypedList(self.panels, CfgToolboxPanel)
        self.actions = TypedList(self.actions, CfgToolboxAction)

    def propertygrid_labels(self):
        labels = {}
        labels["panels"] = "Panels"
        labels["actions"] = "Actions"
        labels["titleButtonHeight"] = "Title Button Height"
        labels["dockerButtonHeight"] = "Docker Button Height"
        labels["dockerBackHeight"] = "Back Button Height"
        labels["sliderHeight"] = "Slider Height"
        labels["actionHeight"] = "Action Button Height"
        return labels

    def propertygrid_groups(self):
        groups = {}
        return groups

    def propertygrid_restrictions(self):
        restrictions = {}
        return restrictions


