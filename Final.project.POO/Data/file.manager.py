import json

class FileManager:

    def save(self, circuit, filename="circuit.json"):
        data = {
            "components": [
                {"type": c.__class__.__name__, "name": c.name}
                for c in circuit.components
            ],
            "connections": [
                (s.name, t.name) for s, t in circuit.connections
            ]
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load(self, circuit, filename="circuit.json"):
        from Model.components import Switch, Light

        with open(filename, "r") as f:
            data = json.load(f)

        name_map = {}

        for comp in data["components"]:
            if comp["type"] == "Switch":
                obj = Switch(comp["name"])
            else:
                obj = Light(comp["name"])

            circuit.add_component(obj)
            name_map[comp["name"]] = obj

        for s, t in data["connections"]:
            circuit.connect(name_map[s], name_map[t])
