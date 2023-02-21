import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from design import Ui_Calculator


class calculator(QMainWindow):

    result="0"
    operator=""
    def __init__(self):
        super(calculator, self).__init__()
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)

        self.btn_0

    def zeroProssed(self):
        val=self.txtResult.text()
        if not val=="0":
            self.txtResult.setText(f"{val}0")
        else:
            self.txtResult.setText("0")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = calculator()
    window.show()

    sys.exit(app.exec())