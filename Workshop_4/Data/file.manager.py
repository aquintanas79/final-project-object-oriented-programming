import json

class FileManager:

    def save(self, circuit, filename="circuit_design.json"):
        data = {
            "components": [c.name for c in circuit.components],
            "connections": [(a.name, b.name) for a, b in circuit.connections]
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load(self, circuit, filename="circuit_design.json"):
        with open(filename, "r") as f:
            data = json.load(f)

        name_to_component = {}

        for name in data["components"]:
            name_to_component[name] = Component(name)
            circuit.add_component(name_to_component[name])

        for a, b in data["connections"]:
            circuit.connect(name_to_component[a], name_to_component[b])

