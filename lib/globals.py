import json
from lib import recipe, item


class Globals:

    def __init__(
        self,
        json_file: str,
    ):
        with open(json_file) as globals_json:
            g = json.load(globals_json)
            self.recipes = [
                recipe.Recipe(
                    name=r["name"],
                    inputs=[
                        item.Item(
                            name=i["name"], rate=i["rate"], state="solid", is_raw=False
                        )
                        for i in r["inputs"]
                    ],
                    outputs=[
                        item.Item(
                            name=o["name"], rate=o["rate"], state="solid", is_raw=False
                        )
                        for o in r["outputs"]
                    ],
                    machine=r["machine"],
                    is_alternate=r["is_alternate"],
                )
                for r in g["recipes"]
            ]
            self.items = [
                item.Item(name=i["name"], rate=0, state=i["state"], is_raw=i["is_raw"])
                for i in g["items"]
            ]
            self.machines = [m for m in g["machines"]]
