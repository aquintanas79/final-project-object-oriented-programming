class Simulator:
    def run(self, circuit):
        for source, target in circuit.connections:
            if hasattr(target, "update_state"):
                target.update_state(source.state)
