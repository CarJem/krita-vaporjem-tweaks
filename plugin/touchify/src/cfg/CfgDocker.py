from ..ext.extensions import Extensions


class CfgDocker:
    display_name: str = ""
    docker_name: str = ""
    icon: str = ""
    hotkeyNumber: int = 0

    def create(args):
        obj = CfgDocker()
        Extensions.dictToObject(obj, args)
        return obj

    def forceLoad(self):
        pass

    def __str__(self):
        return self.display_name.replace("\n", "\\n")

    def propertygrid_groups(self):
        groups = {}
        return groups
    
    def propertygrid_labels(self):
        labels = {}
        labels["display_name"] = "Display Name"
        labels["docker_name"] = "Docker ID"
        labels["icon"] = "Preview Icon"
        labels["hotkeyNumber"] = "Activation Hotkey"
        return labels

    def propertygrid_restrictions(self):
        restrictions = {}
        restrictions["docker_name"] = {"type": "docker_selection"}
        restrictions["hotkeyNumber"] = {"type": "range", "min": 0, "max": 10}
        restrictions["icon"] = {"type": "icon_selection"}
        return restrictions