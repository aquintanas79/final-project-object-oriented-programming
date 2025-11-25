class UIManager:
    """
    CRC Card: UI Manager
    Responsibility: Render components, display menus.
    """
    def render_board(self, circuit_board):
        print("\n[GUI RENDER] Drawing Board:")
        for comp in circuit_board.components:
            print(f" - DRAW {comp.name} ({comp.get_type()}) at X:{comp.x} Y:{comp.y}")
    
    def show_menu(self):
        print("[GUI] Displaying Main Menu...")