# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        if not Calculator.objectName():
            Calculator.setObjectName(u"Calculator")
        Calculator.resize(592, 586)
        self.centralwidget = QWidget(Calculator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(300, 500))
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Result = QLineEdit(self.centralwidget)
        self.Result.setObjectName(u"Result")
        self.Result.setMaxLength(10)
        self.Result.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Result.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.Result)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_0, 3, 1, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_1, 2, 0, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_2, 2, 1, 1, 1)

        self.btn_equ = QPushButton(self.centralwidget)
        self.btn_equ.setObjectName(u"btn_equ")
        sizePolicy.setHeightForWidth(self.btn_equ.sizePolicy().hasHeightForWidth())
        self.btn_equ.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_equ, 3, 2, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_3, 2, 2, 1, 1)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_clear, 3, 0, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_4, 1, 0, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_5, 1, 1, 1, 1)

        self.btn_min = QPushButton(self.centralwidget)
        self.btn_min.setObjectName(u"btn_min")
        sizePolicy.setHeightForWidth(self.btn_min.sizePolicy().hasHeightForWidth())
        self.btn_min.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_min, 1, 3, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_6, 1, 2, 1, 1)

        self.btn_div = QPushButton(self.centralwidget)
        self.btn_div.setObjectName(u"btn_div")
        sizePolicy.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_div, 3, 3, 1, 1)

        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_add, 0, 3, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        self.btn_7.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_7, 0, 0, 1, 1)

        self.btn_mul = QPushButton(self.centralwidget)
        self.btn_mul.setObjectName(u"btn_mul")
        sizePolicy.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_mul, 2, 3, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_9, 0, 2, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_8, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        Calculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calculator)

        QMetaObject.connectSlotsByName(Calculator)
    # setupUi

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(QCoreApplication.translate("Calculator", u"Calculator", None))
        self.Result.setText(QCoreApplication.translate("Calculator", u"1", None))
        self.btn_0.setText(QCoreApplication.translate("Calculator", u"0", None))
#if QT_CONFIG(shortcut)
        self.btn_0.setShortcut(QCoreApplication.translate("Calculator", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.btn_1.setText(QCoreApplication.translate("Calculator", u"1", None))
#if QT_CONFIG(shortcut)
        self.btn_1.setShortcut(QCoreApplication.translate("Calculator", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.btn_2.setText(QCoreApplication.translate("Calculator", u"2", None))
#if QT_CONFIG(shortcut)
        self.btn_2.setShortcut(QCoreApplication.translate("Calculator", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_equ.setText(QCoreApplication.translate("Calculator", u"=", None))
#if QT_CONFIG(shortcut)
        self.btn_equ.setShortcut(QCoreApplication.translate("Calculator", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.btn_3.setText(QCoreApplication.translate("Calculator", u"3", None))
#if QT_CONFIG(shortcut)
        self.btn_3.setShortcut(QCoreApplication.translate("Calculator", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.btn_clear.setText(QCoreApplication.translate("Calculator", u"CE", None))
#if QT_CONFIG(shortcut)
        self.btn_clear.setShortcut(QCoreApplication.translate("Calculator", u"C", None))
#endif // QT_CONFIG(shortcut)
        self.btn_4.setText(QCoreApplication.translate("Calculator", u"4", None))
#if QT_CONFIG(shortcut)
        self.btn_4.setShortcut(QCoreApplication.translate("Calculator", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.btn_5.setText(QCoreApplication.translate("Calculator", u"5", None))
#if QT_CONFIG(shortcut)
        self.btn_5.setShortcut(QCoreApplication.translate("Calculator", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.btn_min.setText(QCoreApplication.translate("Calculator", u"-", None))
#if QT_CONFIG(shortcut)
        self.btn_min.setShortcut(QCoreApplication.translate("Calculator", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.btn_6.setText(QCoreApplication.translate("Calculator", u"6", None))
#if QT_CONFIG(shortcut)
        self.btn_6.setShortcut(QCoreApplication.translate("Calculator", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.btn_div.setText(QCoreApplication.translate("Calculator", u"/", None))
#if QT_CONFIG(shortcut)
        self.btn_div.setShortcut(QCoreApplication.translate("Calculator", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.btn_add.setText(QCoreApplication.translate("Calculator", u"+", None))
#if QT_CONFIG(shortcut)
        self.btn_add.setShortcut(QCoreApplication.translate("Calculator", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.btn_7.setText(QCoreApplication.translate("Calculator", u"7", None))
#if QT_CONFIG(shortcut)
        self.btn_7.setShortcut(QCoreApplication.translate("Calculator", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_mul.setText(QCoreApplication.translate("Calculator", u"x", None))
#if QT_CONFIG(shortcut)
        self.btn_mul.setShortcut(QCoreApplication.translate("Calculator", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.btn_9.setText(QCoreApplication.translate("Calculator", u"9", None))
#if QT_CONFIG(shortcut)
        self.btn_9.setShortcut(QCoreApplication.translate("Calculator", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.btn_8.setText(QCoreApplication.translate("Calculator", u"8", None))
#if QT_CONFIG(shortcut)
        self.btn_8.setShortcut(QCoreApplication.translate("Calculator", u"8", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

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