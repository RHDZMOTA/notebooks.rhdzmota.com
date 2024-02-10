import os
import json
import datetime as dt
from typing import Optional

import fire
from jupyter_server.auth import passwd


JUPYTER_PWD = os.environ.get("JUPYTER_PWD")


class Main:

    def create(self, pwd: Optional[str] = None, save: bool = False, display: bool = False) -> str:
        pwd_payload = {
            "pwd_plain": (pwd_plain := pwd or JUPYTER_PWD or input("Set Jupyter PWD")),
            "pwd_hash": passwd(pwd_plain)
        }
        content = json.dumps(pwd_payload, indent=4)
        if save:
            with open(dt.datetime.utcnow().isoformat() + "pwd-info.json", "w") as file:
                file.write(content)
        if display:
            print(content)
        return pwd_payload["pwd_hash"]


if __name__ == "__main__":
    fire.Fire(Main())

