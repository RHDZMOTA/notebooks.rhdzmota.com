import os
import json
from typing import Optional

import fire


DEFAULT_NOTEBOOK_SOURCE_DIRECTORY = os.path.join(
    "notebooks",
    "private",
)
DEFAULT_NOTEBOOK_TARGET_DIRECTORY = os.path.join(
    "..",
    "public",
    "reference",
)

class Main:

    def __init__(self):
        with open("notebook-build.json", "r") as file:
            self.configs = json.loads(file.read())

    def notebook_list(self, directory: Optional[str] = None) -> list[str]:
        source_directory = directory or DEFAULT_NOTEBOOK_SOURCE_DIRECTORY
        return [
            file
            for file in os.listdir(source_directory)
            if file.endswith(".ipynb")
        ]

    def notebook_exists(self, name: str, directory: Optional[str] = None, fail: bool = False) -> tuple[str, bool]:
        source_directory = directory or DEFAULT_NOTEBOOK_SOURCE_DIRECTORY
        notebook_path = os.path.join(source_directory, name)
        notebook_exists = os.path.exists(notebook_path)
        if fail and not notebook_exists:
            raise ValueError(
                f"Notebook {name} does not exists in path: {source_directory}"
            )
        return notebook_path, notebook_exists

    def notebooks_publish_all(
            self,
            from_directory: Optional[str] = None,
            into_directory: Optional[str] = None,
    ):
        for notebook_name in self.notebook_list(directory=from_directory):
            self.notebook_publish_config_fallback(
                name=notebook_name,
                from_directory=from_directory,
                into_directory=into_directory,
            )

    def notebook_publish_config_fallback(
            self,
            name: str,
            from_directory: Optional[str] = None,
            into_directory: Optional[str] = None,
    ) -> str:
        default_configs = self.configs["default"]
        notebook_configs = {**default_configs, **self.configs.get(name, default_configs)}
        return self.notebook_publish(
            name=name,
            from_directory=from_directory,
            into_directory=into_directory,
            **notebook_configs,
        ) 

    def notebook_publish(
            self,
            name: str,
            from_directory: Optional[str] = None,
            into_directory: Optional[str] = None,
            rebuild: bool = False
    ):
        notebook_path_source, _ = self.notebook_exists(
            name=name,
            directory=from_directory,
            fail=True
        )
        target_directory = into_directory or DEFAULT_NOTEBOOK_TARGET_DIRECTORY
        notebook_path_target = os.path.join(target_directory, name)
        #if not os.path.exists(target_directory):
        #    raise ValueError(f"Target Directory Not Found: {target_directory}")
        if not rebuild:
            return os.system(f"cp {notebook_path_source} {notebook_path_target}") or "ok"
        return os.system(
            f"jupyter nbconvert --to notebook "
            f"--execute {notebook_path_source} "
            f"--output {notebook_path_target}"
        ) or "ok"


if __name__ == "__main__":
    fire.Fire(Main())

