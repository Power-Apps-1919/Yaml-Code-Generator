from abc import ABC, abstractmethod
from typing import Dict

class BaseControl(ABC):
    """
    Abstract base class for all Power Apps controls.
    """

    def __init__(self, name: str, props: Dict):
        self.name = name
        self.props = props or {}

    @abstractmethod
    def get_default_properties(self) -> Dict:
        """
        Define default properties for the control.
        """
        pass

    def get_control_name(self):
        return self.__class__.__name__

    def build(self) -> Dict:
        """
        Merge default props and user props, return YAML-serializable dict.
        """
        merged_props = {**self.get_default_properties(), **self.props}
        return {
            self.name: {
                "Control": self.get_control_name() if hasattr(self, "get_control_name") else self.__class__.__name__,
                "Properties": merged_props
            }
        }
