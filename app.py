from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QGridLayout, QWidget
from typing import Callable, Optional


# Létrehozzuk a Calculator osztályt, ami tartalmazza a számológép funkcionalitását.
class Calculator:
    def __init__(self) -> None:
        # Fő ablak és widget kreálása a gomboknak.
        self.window = QMainWindow()
        self.window.setWindowTitle('Számológép')

        self.main_widget = QWidget() # Fő widget definiáláa
        self.layout = QGridLayout()  # Grid layout gomb elrenezéshez
        self.main_widget.setLayout(self.layout)

        # Beviteli (és egyben eredmény) mező létrehozása
        self.entry = QLineEdit()
        self.entry.returnPressed.connect(self.calculate)  # Enterre is számoljon
        self.layout.addWidget(self.entry, 0, 0, 1, 4)  # Hozzáadás a layouthoz.

        # Gombok definiálása
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '+']
        ]

        # Gombok létrehozása és érték/funkció hozzárendelése
        for i, button_row in enumerate(buttons):
            for j, button_text in enumerate(button_row):
                self.create_button(button_text, self.click_button, i + 1, j)

        # "C" és "=" gombok létrehozása
        self.create_button("C", self.clear_button, 5, 0) # törlés
        self.create_button("=", self.calculate, 5, 3)  # számolás

        # Fő widget definiálása
        self.window.setCentralWidget(self.main_widget)

    # Függvény a kattintható gombok létrehozására.
    def create_button(self, text: str, command: Callable, row: int, col: int) -> None:
        button = QPushButton(text)
        button.clicked.connect(lambda: command(text))  # Funkció hozzárendelés.
        self.layout.addWidget(button, row, col)  # Hozzáadás a layout-hoz.

    # Gomb érték hozzáadása a műveleti mezőhöz klikkeléskor
    def click_button(self, button_text: str) -> None:
        current_value = self.entry.text()
        self.entry.setText(current_value + button_text)

    # "C" gomhoz tartozó függvény a beviteli mező törléshez
    def clear_button(self, _: Optional[str] = None) -> None:
        self.entry.setText("")

    # Beviteli mező kiszámítása
    def calculate(self, _: Optional[str] = None) -> None:
        try:
            result = eval(self.entry.text())
            self.entry.setText(str(result))
        except SyntaxError:
            self.entry.setText("Hibás kifejezés")


# A main függvény létrehozza az alkalmazást és megjeleníti az ablakot.
def main() -> None:
    app = QApplication([])
    calc = Calculator()
    calc.window.show()
    app.exec_()


# Main meghívása
if __name__ == "__main__":
    main()