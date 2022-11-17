from pathlib import Path
from typing import Union
from dataclasses import dataclass

@dataclass(frozen=True)
class ProjectPath:
    root: Path
    data_original: Path
    data_input: Path
    data_output: Path
    data_plot: Path

class Project:
    """
    Class describes ebilab project
    Current path can be acquired by :py:func:`get_current_project` function.
    """
    _root_dir: Path

    def __init__(self, root: Union[str, Path]):
        if isinstance(root, str):
            root = Path(root)
        if not (root / "ebilab.ini").exists():
            raise Exception("ebilab project directory not exist.")
        self._root_dir = root

    @property
    def path(self) -> ProjectPath:
        """
        Information about filepath of project
        """
        return ProjectPath(
            root=self._root_dir,
            data_original=self._root_dir / "data" / "original",
            data_input=self._root_dir / "data" / "input",
            data_output=self._root_dir / "data" / "output",
            data_plot=self._root_dir / "data" / "plot",
        )

def _get_current_project() -> Project:
    _paths = [Path(".").resolve()] + list(Path(".").resolve().parents)
    for path in _paths:
        root = path
        if (root / "ebilab.ini").exists():
            break
    else:
        raise Exception("Could not ebilab project data directory.")
    return Project(root)

_current_project = None
def get_current_project() -> Project:
    """
    Search project file and return project class
    """

    global _current_project
    if _current_project:
        return _current_project
    _current_project = _get_current_project()
    return _current_project