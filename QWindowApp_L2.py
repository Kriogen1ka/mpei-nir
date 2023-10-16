from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication, QGridLayout, QPushButton, QVBoxLayout
from PyQt6.uic import loadUi
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class QWindowApp(QMainWindow):
    def __init__(self, domain):
        self.app = QApplication(sys.argv)
        super().__init__()
        loadUi("UI_L2.ui", self)
        self.domain = domain
        self.pushButton_OK.clicked.connect(self.pick_var)
        self.pushButton_generate.clicked.connect(self.generate_var)
        self.pushButton_Input1.clicked.connect(self.input_eq_1)
        self.pushButton_Input2.clicked.connect(self.input_eq_2)
        self.actionQuit.triggered.connect(self.exit)
        self.actionAbout.triggered.connect(self.credits)
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
         • Операция возведения в степень обозначается как «**» или «^»
         • Операция дифференцирования записывается следующим образом: dХ, где Х - дифференцируемое выражение (d – строчная буква)
         • Множители Лагранжа следует вводить как LAi, i=0,1,2
         • В условии стационарности по t1 слагаемые, содержащие произведения множителей Лагранжа на интегранты в момент времени t1,
           записываются следующим образом: LAi*Gi(T1), i=0,1,2
         • Ввод функции сопряженных состояний Pi, i=0,1,2,3.
        """
        self.label_24.setText(method_str)
        #self.LaTeX_rendered = False
        self.tabWidget.setCurrentWidget(self.tab_var)

    def renderLaTeX(self, qWidget, latex):
        fig = Figure()
        fig.suptitle(latex, x=0.0, y=0.5, horizontalalignment='left', verticalalignment='center', fontsize=12)

        canvas = FigureCanvasQTAgg(fig)
        canvas.draw()

        layout = qWidget.layout()
        if not layout:
            layout = QVBoxLayout(qWidget)

        if layout.count():
            layout.removeWidget(layout.itemAt(0).widget())
        layout.addWidget(canvas)

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
        self.renderLaTeX(self.widget_13, self.domain.latex_6_p2)
        self.renderLaTeX(self.widget_12, self.domain.latex_6_p1)
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
        self.tabWidget.setCurrentWidget(self.tab_p1)
        self.plainTextEdit_3.setPlainText(self.domain.history[0])
        self.plainTextEdit_4.setPlainText(self.domain.history[1])
        return
    
    def generate_var(self):
        self.usr_var = 26 # CHANGE THAT LATER SOMEHOW
        self.domain.generateVariant()
        self.set_pick_visibility()
        self.fill_TeX_labels()
        self.fill_prompt_labels()
        self.tabWidget.setCurrentWidget(self.tab_p1)
        self.plainTextEdit_3.setPlainText(self.domain.history[0])
        self.plainTextEdit_4.setPlainText(self.domain.history[1])
        return

    def input_eq_1(self):
        input_data = self.plainTextEdit.toPlainText()
        # CHECK INPUT !!!
        if (self.domain.next_input_p1(input_data)):
            self.plainTextEdit_3.setPlainText(self.domain.history[0])
            self.label_11.setText(self.domain.steps_p1[self.domain.current_step_p1][2])
            self.label_12.setText(self.domain.steps_p1[self.domain.current_step_p1][1])
            self.plainTextEdit.clear()
            if (self.domain.completed_p1):
                self.information = QMessageBox()
                self.information.setWindowTitle("Поздравляю!")
                self.information.setText("Первая часть лабораторной работы выполнена успешно, скопируйте историю в отчёт")
                self.information.exec()
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
            if (self.domain.completed_p2):
                self.information = QMessageBox()
                self.information.setWindowTitle("Поздравляю!")
                self.information.setText("Вторая часть лабораторной работы выполнена успешно, скопируйте историю в отчёт")
                self.information.exec()
        else:
            self.error = QMessageBox()
            self.error.setWindowTitle("Ошибка")
            self.error.setText("Значения введены неверно")
            self.error.exec()
        return

    def exit(self):
        # обработчик выхода
        ret = QMessageBox.question(self, "Закрыть программу?", "Данные будут утеряны")
        if ret == QMessageBox.StandardButton.Yes:
            self.app.quit()
        return

    def credits(self):
        QMessageBox.information(self, "О прогамме",
"""Программный комплекс для проведения лабораторной работы по курсу «Оптимальное управление».

Тема лабораторной работы: «Решение задач оптимального управления на основе принципа максимума».

Создан на кафедре управления и интеллектуальных технологий НИУ «МЭИ» (uit.mpei.ru).
Разработчик: Мирошников А. М., студент группы А-03-19.

Москва, 2023""")
