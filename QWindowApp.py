from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication, QGridLayout, QPushButton, QVBoxLayout
from PyQt6.uic import loadUi
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class QWindowApp(QMainWindow):
    def __init__(self, domain):
        self.app = QApplication(sys.argv)
        super().__init__()
        loadUi("Lab1_optimal.ui", self)
        self.domain = domain
        self.pushButton_OK.clicked.connect(self.pick_var)
        self.pushButton_Input1.clicked.connect(self.input_eq_1)
        self.pushButton_Input2.clicked.connect(self.input_eq_2)
        self.set_init_visibility()
        method_str = """Правила, которых необходимо придерживаться при работе с программой:
         • В окно ввода следует записывать только правые части выражений
         • Переменные, применяемые для ввода формул, выглядят так:
                U1 - управление по первому входу;
                U2 - управление по второму входу;
                X1 - переменная состояния 1;
                X2 - переменная состояния 2';
                X3 - переменная состояния 3';
         • Написание строчными буквами недопустимо!
         • Операция умножения должна быть записана с помощью символа «*»
         • Операция возведения в степень обозначается как «**»
         • Операция дифференцирования записывается следующим образом: dХ, где Х - дифференцируемое выражение (d – строчная буква)
         • Множители Лагранжа следует вводить как LAi, i=0,1,2
         • В условии стационарности по t1 слагаемые, содержащие произведения множителей Лагранжа на интегранты в момент времени t1,
           записываются следующим образом: LAi*Gi(T1), i=0,1,2
        """
        self.label_24.setText(method_str)
        #self.LaTeX_rendered = False

    def renderLaTeX(self, qWidget, latex):
        bg = self.palette().window().color() #change to widget color!
        cl = (bg.redF(), bg.greenF(), bg.blueF())
        # Create figure, using window bg color
        fig = Figure(edgecolor=cl, facecolor=cl)
        # Add FigureCanvasQTAgg widget to form
        canvas = FigureCanvasQTAgg(fig) 
        qWidget.setLayout(QVBoxLayout(self))
        qWidget.layout().addWidget(canvas)
        # Clear figure
        fig.clear()
        # Set figure title
        fig.suptitle(latex, x=0.0, y=0.5, horizontalalignment='left', verticalalignment='center', fontsize=12)
        canvas.draw()
        return

    def fill_TeX_labels(self):
        self.domain.make_latex(self.domain.variants[self.usr_var-1])
        self.renderLaTeX(self.widget, self.domain.latex_1_p1)
        self.renderLaTeX(self.widget_4, self.domain.latex_2_p1)
        #"""
        self.renderLaTeX(self.widget_5, self.domain.latex_3_p1)
        self.renderLaTeX(self.widget_3, self.domain.latex_4_p1)
        self.renderLaTeX(self.widget_2, self.domain.latex_5_p1)
        self.renderLaTeX(self.widget_6, self.domain.latex_1_p2)
        self.renderLaTeX(self.widget_7, self.domain.latex_2_p2)
        self.renderLaTeX(self.widget_8, self.domain.latex_3_p2)
        self.renderLaTeX(self.widget_10, self.domain.latex_4_p2)
        self.renderLaTeX(self.widget_9, self.domain.latex_5_p2)
        #"""
        return  

    def run(self):
        self.show()
        self.app.exec()

    def set_init_visibility(self): 
        self.label_11.setVisible(False)
        self.label_12.setVisible(False)
        self.label_14.setVisible(False)
        self.label_15.setVisible(False)
        return
    
    def set_pick_visibility(self):
        self.label_11.setVisible(True)
        self.label_12.setVisible(True)
        self.label_14.setVisible(True)
        self.label_15.setVisible(True)
        return

    def fill_prompt_labels(self):
        self.label_11.setText(self.domain.step_0[2])
        self.label_12.setText(self.domain.step_0[1])
        self.label_14.setText(self.domain.step_0_2[2])
        self.label_15.setText(self.domain.step_0_2[1])
        return

    def pick_var(self):
        self.usr_var = int(self.spinBox.text())
        self.domain.setVariant(self.usr_var)
        self.set_pick_visibility()
        self.fill_TeX_labels()
        self.fill_prompt_labels()
        return
    
    def input_eq_1(self):
        input_data = self.plainTextEdit.toPlainText()
        # CHECK INPUT !!!
        if (self.domain.next_input_p1(input_data)):
            self.plainTextEdit_3.setPlainText(self.domain.history[0])
            self.label_11.setText(self.domain.steps_p1[self.domain.current_step_p1][2])
            self.label_12.setText(self.domain.steps_p1[self.domain.current_step_p1][1])
            self.plainTextEdit.clear()
        else:
            self.error = QMessageBox()
            self.error.setWindowTitle("Ошибка")
            self.error.setText("Значения введены неверно")
            self.error.exec()
        return
    
    def input_eq_2(self):
        input_data = self.plainTextEdit_2.toPlainText()
        # CHECK INPUT !!!
        if (self.domain.next_input_p2(input_data)):
            self.plainTextEdit_4.setPlainText(self.domain.history[1])
            self.label_14.setText(self.domain.steps_p2[self.domain.current_step_p2][2])
            self.label_15.setText(self.domain.steps_p2[self.domain.current_step_p2][1])
            self.plainTextEdit_2.clear()
        else:
            self.error = QMessageBox()
            self.error.setWindowTitle("Ошибка")
            self.error.setText("Значения введены неверно")
            self.error.exec()
        return

    def exit():
        # обработчик выхода
        return

    def credits():
        # информация о разработчике
        return