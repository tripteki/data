import toml
from .Helpers.ApplicationPath import application_path

class Version:

    def __call__ (self) -> str:
        """
        :rtype: str
        """
        version = toml.load (application_path ("pyproject.toml")).get ("project", {}). get ("version", "1.0.0")

        return version
