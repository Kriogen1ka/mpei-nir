import sympy as sym
import random

class Domain():
    def __init__(self):
        self.variant_labels = ["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "C1", "C2", "C3", "D1", "D2", "D3", "D4", "D5",
                        "A12", "A22", "A32", "A42", "A52", "B12", "B22", "B32", "B4G", "B5G", "B6G", "B7G", "B8G", "C12", "C22", "C32",
                        "C4G", "C5G", "C6G", "C7G", "C8G", "D12", "D22", "D32", "D42", "D52", "D6G", "D7G", "D8G", "D9G", "D0G"]
        
        self.variant_1 = [1, 4, 2, 1, 1, 3, 2, 3, 4, 2, 2, 3, 3, 1, 2, 1, 0, 4, 2, 3, 1, 1, 1, 4, 3, 2, 3, 1, 2, 4, 4, 3, 2, 2, 1, 3, 4, 2, 1, 4, 3, 3, 2, 1, 2, 2, 2]   
        self.variant_2 = [4, 0, 3, 2, 4, 3, 1, 1, 2, 4, 4, 1, 3, 1, 4, 1, 4, 1, 3, 4, 3, 4, 4, 1, 1, 3, 2, 2, 3, 1, 1, 4, 1, 3, 2, 2, 1, 1, 4, 4, 4, 3, 1, 1, 3, 3, 2]  
        self.variant_3 = [3, 3, 0, 4, 2, 4, 2, 3, 3, 3, 3, 4, 4, 3, 3, 2, 2, 0, 4, 2, 4, 3, 2, 2, 4, 3, 4, 1, 2, 4, 4, 3, 2, 2, 1, 3, 4, 2, 1, 4, 3, 3, 2, 1, 2, 2, 2] 
        self.variant_4 = [0, 1, 3, 4, 1, 2, 4, 2, 1, 1, 4, 3, 4, 2, 1, 1, 2, 2, 2, 1, 2, 3, 3, 4, 1, 2, 4, 3, 1, 2, 2, 3, 4, 2, 4, 4, 1, 3, 3, 1, 4, 4, 1, 2, 3, 4, 2] 
        self.variant_5 = [2, 3, 0, 4, 1, 4, 3, 1, 2, 4, 3, 1, 1, 2, 4, 1, 1, 2, 3, 4, 3, 2, 1, 3, 4, 4, 3, 2, 2, 1, 1, 4, 3, 3, 4, 2, 1, 4, 3, 2, 4, 1, 1, 3, 3, 4, 2] 
        self.variant_6 = [2, 3, 2, 3, 2, 4, 1, 1, 1, 4, 4, 2, 3, 2, 3, 1, 4, 4, 4, 2, 3, 1, 1, 2, 3, 4, 4, 3, 2, 1, 1, 1, 2, 4, 3, 2, 1, 3, 3, 2, 4, 3, 4, 1, 2, 3, 3]  
        self.variant_7 = [3, 3, 2, 4, 3, 2, 2, 1, 3, 4, 2, 4, 2, 4, 2, 4, 1, 1, 1, 3, 2, 4, 4, 3, 2, 2, 2, 4, 3, 3, 3, 3, 4, 1, 4, 3, 2, 4, 1, 1, 1, 2, 3, 3, 4, 1, 2]  
        self.variant_8 = [4, 4, 2, 3, 2, 1, 3, 1, 1, 4, 4, 3, 2, 2, 2, 4, 1, 0, 1, 1, 2, 4, 2, 4, 3, 3, 2, 1, 1, 2, 3, 2, 3, 4, 4, 1, 2, 1, 4, 4, 2, 2, 3, 1, 3, 4, 4]  
        self.variant_9 = [4, 2, 0, 2, 4, 1, 3, 4, 3, 1, 2, 4, 2, 3, 3, 1, 1, 2, 0, 3, 4, 4, 1, 3, 2, 2, 4, 3, 3, 1, 1, 3, 2, 1, 4, 3, 2, 4, 3, 1, 3, 4, 2, 1, 3, 3, 1]  
        self.variant_10 = [1, 0, 4, 2, 1, 2, 3, 2, 4, 1, 2, 1, 3, 2, 4, 4, 0, 1, 2, 2, 3, 3, 4, 4, 2, 3, 1, 1, 1, 4, 2, 3, 3, 2, 2, 4, 4, 1, 2, 3, 4, 3, 2, 2, 2, 4, 2]  
        self.variant_11 = [2, 2, 2, 2, 2, 2, 3, 1, 2, 3, 4, 2, 4, 1, 2, 3, 3, 4, 4, 3, 2, 1, 1, 1, 4, 4, 2, 2, 3, 2, 1, 4, 3, 1, 2, 1, 4, 1, 3, 3, 1, 3, 2, 3, 2, 3, 3]
        self.variant_12 = [2, 3, 2, 3, 4, 2, 4, 1, 4, 3, 1, 1, 4, 2, 2, 1, 1, 1, 0, 4, 4, 2, 3, 3, 3, 3, 1, 1, 4, 2, 2, 4, 1, 3, 1, 2, 2, 1, 4, 3, 2, 3, 4, 1, 2, 4, 3] 
        self.variant_13 = [0, 1, 4, 3, 2, 3, 1, 4, 3, 2, 1, 4, 1, 3, 1, 2, 3, 1, 2, 1, 4, 1, 2, 3, 3, 4, 1, 3, 1, 3, 1, 2, 1, 4, 3, 2, 3, 2, 4, 4, 4, 1, 2, 3, 4, 3, 2] 
        self.variant_14 = [2, 1, 3, 4, 2, 1, 4, 2, 3, 4, 4, 1, 1, 1, 2, 2, 3, 0, 2, 2, 2, 1, 3, 4, 1, 2, 3, 4, 3, 1, 2, 2, 3, 2, 4, 4, 4, 1, 1, 2, 1, 1, 3, 2, 1, 1, 3] 
        self.variant_15 = [2, 0, 3, 3, 1, 1, 3, 3, 3, 3, 1, 2, 1, 1, 1, 2, 1, 1, 0, 2, 1, 2, 3, 4, 4, 4, 3, 2, 1, 1, 2, 3, 3, 4, 4, 3, 2, 2, 1, 1, 3, 2, 3, 4, 4, 4, 3]
        self.variant_16 = [2, 1, 1, 2, 1, 2, 4, 4, 3, 3, 1, 2, 2, 1, 3, 3, 3, 2, 0, 1, 1, 1, 1, 1, 2, 3, 2, 4, 4, 4, 1, 4, 3, 2, 2, 3, 4, 4, 1, 1, 4, 2, 4, 3, 4, 4, 3]
        self.variant_17 = [0, 4, 1, 3, 4, 1, 1, 2, 3, 2, 2, 1, 4, 1, 4, 4, 4, 4, 4, 3, 3, 2, 2, 1, 2, 4, 4, 1, 3, 4, 3, 3, 3, 1, 2, 4, 1, 1, 2, 3, 4, 3, 4, 3, 4, 3, 4]
        self.variant_18 = [4, 3, 0, 2, 1, 4, 3, 2, 2, 2, 3, 4, 1, 1, 2, 4, 0, 2, 2, 2, 2, 2, 3, 3, 4, 4, 2, 3, 3, 2, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 3, 1, 1, 2, 3, 4]
        self.variant_19 = [4, 0, 4, 4, 4, 1, 2, 2, 3, 2, 3, 4, 4, 2, 2, 1, 1, 1, 4, 4, 4, 3, 2, 3, 1, 1, 2, 3, 3, 4, 1, 3, 2, 2, 1, 3, 2, 4, 2, 1, 4, 3, 3, 3, 3, 3, 3]
        self.variant_20 = [2, 3, 3, 4, 4, 4, 4, 4, 2, 3, 2, 2, 1, 1, 1, 1, 0, 1, 1, 2, 4, 4, 3, 3, 2, 3, 2, 1, 4, 1, 1, 2, 4, 4, 4, 1, 1, 1, 2, 3, 3, 1, 3, 2, 1, 1, 2]
        self.variant_21 = [4, 1, 1, 2, 2, 2, 2, 2, 4, 1, 4, 4, 3, 3, 3, 3, 0, 3, 3, 4, 2, 2, 1, 1, 4, 1, 4, 3, 2, 3, 3, 4, 2, 2, 2, 3, 3, 3, 4, 1, 1, 2, 1, 4, 3, 3, 4]
        self.variant_22 = [4, 1, 0, 2, 3, 2, 1, 3, 4, 2, 1, 3, 3, 4, 2, 3, 3, 4, 1, 2, 1, 4, 3, 1, 2, 2, 1, 4, 4, 3, 3, 2, 1, 1, 2, 4, 3, 2, 1, 4, 2, 3, 3, 1, 1, 2, 4] 
        self.variant_23 = [4, 1, 4, 1, 4, 2, 3, 3, 3, 2, 2, 4, 1, 4, 1, 3, 1, 1, 1, 4, 1, 3, 3, 4, 1, 2, 2, 1, 4, 3, 3, 3, 4, 2, 1, 4, 3, 1, 1, 4, 2, 1, 2, 3, 4, 1, 1] 
        self.variant_24 = [1, 1, 4, 2, 1, 4, 4, 3, 1, 2, 4, 2, 4, 2, 4, 2, 3, 3, 3, 1, 4, 2, 4, 1, 4, 4, 4, 2, 1, 1, 1, 1, 2, 3, 2, 1, 4, 2, 3, 3, 3, 4, 1, 1, 2, 3, 4]  
        self.variant_25 = [2, 2, 4, 1, 4, 3, 1, 3, 3, 2, 2, 1, 4, 4, 4, 2, 3, 4, 3, 3, 4, 2, 4, 2, 1, 1, 4, 3, 3, 4, 1, 4, 1, 2, 2, 3, 4, 3, 2, 2, 4, 4, 1, 3, 1, 2, 2]
        self.variant_generated = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.variants = [self.variant_1, self.variant_2, self.variant_3, self.variant_4, self.variant_5, self.variant_6, self.variant_7, self.variant_8, self.variant_9,
                         self.variant_10, self.variant_11, self.variant_12, self.variant_13, self.variant_14, self.variant_15, self.variant_16, self.variant_17,
                         self.variant_18, self.variant_19, self.variant_20, self.variant_21, self.variant_22, self.variant_23, self.variant_24, self.variant_25, self.variant_generated]
        
        # часть 1       
        self.step_0 = [0, 'X1\'=', 'Ввод уравнений связи. Введите правую часть первого уравнения связи:', 'Уравнение связи 1:']
        self.step_1 = [1, 'X2\'=', 'Ввод уравнений связи. Введите правую часть второго уравнения связи:', 'Уравнение связи 2:']
        self.step_2 = [2, 'X3\'=', 'Ввод уравнений связи. Введите правую часть третьего уравнения связи:', 'Уравнение связи 3:']
        self.step_3 = [3, 'H=', 'Введите гамильтониан:', 'Гамильтониан:']
        self.step_4 = [4, 'L=', 'Введите лагранжиан:', 'Лагранжиан:']
        self.step_5 = [5, 'P1\'=', 'Введите правую часть первого уравнения сопряженного состояния:', 'Уравнение сопряженного состояния 1:']
        self.step_6 = [6, 'P2\'=', 'Введите правую часть второго уравнения сопряженного состояния:', 'Уравнение сопряженного состояния 2:']
        self.step_7 = [7, 'P3\'=', 'Введите правую часть третьего уравнения сопряженного состояния:', 'Уравнение сопряженного состояния 3:']
        self.step_8 = [8, 'U1opt=', 'Введите U1-оптимальное:', 'U1-оптимальное:']
        self.step_9 = [9, 'X1\'=', 'Уравнения для определения оптимальной траектории. Введите правую часть первого уравнения (подставьте решение для U1):', 'Первое уравнение для определения оптимальной траектории:']
        self.step_10 = [10, 'X2\'=', 'Уравнения для определения оптимальной траектории. Введите правую часть второго уравнения (подставьте решение для U1):', 'Второе уравнение для определения оптимальной траектории:']
        self.step_11 = [11, 'X3\'=', 'Уравнения для определения оптимальной траектории. Введите правую часть третьего уравнения (подставьте решение для U1):', 'Третье уравнение для определения оптимальной траектории:']
        self.steps_p1 = [self.step_0, self.step_1, self.step_2, self.step_3, self.step_4, self.step_5, self.step_6,
                         self.step_7, self.step_8, self.step_9, self.step_10, self.step_11]
        #часть2

        self.step_0_2 = [0, 'X1\'=', 'Ввод уравнений связи. Введите правую часть первого уравнения связи:', 'Уравнение связи 1:']
        self.step_1_2 = [1, 'X2\'=', 'Ввод уравнений связи. Введите правую часть второго уравнения связи:', 'Уравнение связи 2:']
        self.step_2_2 = [2, 'X3\'=', 'Ввод уравнений связи. Введите правую часть третьего уравнения связи:', 'Уравнение связи 3:']
        self.step_3_2 = [3, 'H=', 'Введите гамильтониан:', 'Гамильтониан:']
        self.step_4_2 = [4, 'L=', 'Введите лагранжиан:', 'Лагранжиан:']
        self.step_5_2 = [5, 'P1\'=', 'Введите правую часть первого уравнения сопряженного состояния:', 'Уравнение сопряженного состояния 1:']
        self.step_6_2 = [6, 'P2\'=', 'Введите правую часть второго уравнения сопряженного состояния:', 'Уравнение сопряженного состояния 2:']
        self.step_7_2 = [7, 'P3\'=', 'Введите правую часть третьего уравнения сопряженного состояния:', 'Уравнение сопряженного состояния 3:']
        self.step_8_2 = [8, 'P1(T1)=', 'Введите условие трансверсальности по x1 для свободного конца траектории:', 'Условие трансверсальности по X1:']
        self.step_9_2 = [9, 'P2(T1)=', 'Введите условие трансверсальности по x2 для свободного конца траектории:', 'Условие трансверсальности по X2:']
        self.step_10_2 = [10, 'P3(T1)=', 'Введите условие трансверсальности по x3 для свободного конца траектории:', 'Условие трансверсальности по X3:']
        self.step_11_2 = [11, '0=', 'Введите условие стационарности по T1:', 'Условие стационарности по T1:']
        self.step_12_2 = [12, 'U1opt=', 'Введите U1-оптимальное при |U1| <= U1max:', 'U1-оптимальное при |U1| <= U1max:']
        self.step_13_2 = [13, 'U2opt=', 'Введите U2-оптимальное при |U2| <= U2max:', 'U2-оптимальное при |U2| <= U2max:']
        self.step_14_2 = [14, 'X1\'=', 'Введите U1-оптимальное при |U1| >= U1max:', 'U1-оптимальное при |U1| >= U1max:']
        self.step_15_2 = [15, 'X2\'=', 'Введите U2-оптимальное при |U2| >= U2max:', 'U2-оптимальное при |U2| >= U2max:']
        #self.step_14_2 = [14, 'X1\'=', 'Уравнения для определения оптимальной траектории. Введите правую часть первого уравнения:', 'Первое уравнение для определения оптимальной траектории:']
        #self.step_15_2 = [15, 'X2\'=', 'Уравнения для определения оптимальной траектории. Введите правую часть второго уравнения:', 'Второе уравнение для определения оптимальной траектории:']
        #self.step_16_2 = [16, 'X3\'=', 'Уравнения для определения оптимальной траектории. Введите правую часть третьего уравнения:', 'Третье уравнение для определения оптимальной траектории:']
        self.steps_p2 = [self.step_0_2, self.step_1_2, self.step_2_2, self.step_3_2, self.step_4_2, self.step_5_2, self.step_6_2,
                         self.step_7_2, self.step_8_2, self.step_9_2, self.step_10_2, self.step_11_2, self.step_12_2, self.step_13_2,
                         self.step_14_2, self.step_15_2] # , self.step_16_2
        self.steps = [self.steps_p1, self.steps_p2]
        self.current_step_p1 = 0
        self.current_step_p2 = 0
        self.history_p1 = ""
        self.history_p2 = ""
        self.history = [self.history_p1, self.history_p2]
        self.usr_var = 0
        self.usr_var_picked = False
        self.completed_p1 = False
        self.completed_p2 = False

    def equation_template(self):
        #data from variants
        A1, A2, A3, A4, A5 = sym.symbols("A1 A2 A3 A4 A5")
        B1, B2, B3 = sym.symbols("B1 B2 B3")
        C1, C2, C3 = sym.symbols("C1 C2 C3")
        D1, D2, D3, D4, D5 = sym.symbols("D1 D2 D3 D4 D5")
        A12, A22, A32, A42, A52 = sym.symbols("A12 A22 A32 A42 A52")
        B12, B22, B32, B4G, B5G, B6G, B7G, B8G = sym.symbols("B12 B22 B32 B4G B5G B6G B7G B8G") 
        C12, C22, C32, C4G, C5G, C6G, C7G, C8G = sym.symbols("C12 C22 C32 C4G C5G C6G C7G C8G")
        D12, D22, D32, D42, D52, D6G, D7G, D8G, D9G, D0G = sym.symbols("D12 D22 D32 D42 D52 D6G D7G D8G D9G D0G")

        self.eq_tmp_var = [A1, A2, A3, A4, A5, B1, B2, B3, C1, C2, C3, D1, D2, D3, D4, D5, A12, A22, A32, A42, A52, B12, B22, B32, B4G, B5G, B6G, B7G, B8G, C12, C22, C32, C4G, C5G, C6G, C7G, C8G, D12, D22, D32, D42, D52, D6G, D7G, D8G, D9G, D0G]

        #local data
        U1, U2, X1, X2, X3, T1, T2, T3 = sym.symbols("U1 U2 X1 X2 X3 T1 T2 T3")
        LA0, LA1, LA2, P1, P2, P3, G0, G1, G2 = sym.symbols("LA0 LA1 LA2 P1 P2 P3 G0 G1 G2")
        dX1, dX2, dX3 = sym.symbols("dX1 dX2 dX3")
        #equations
        us1v=X2
        us2v=X3
        us3v=A4*U1-A3*X1-A2*X2-A1*X3
        H=-(LA1*(B1*X1+B2*X2)+LA2*(C1*X1+C2*X2))+P1*X2+P2*X3+P3*(A4*U1-A1*X3-A2*X2-A3*X1)
        Lg=LA1*(B1*X1+B2*X2)+LA2*(C1*X1+C2*X2)+P1*(dX1-X2)+P2*(dX2-X3)+P3*(dX3-A4*U1+A1*X3+A2*X2+A3*X1)
        sx1=LA1*B1+LA2*C1+P3*A3
        sx2=LA1*B2+LA2*C2-P1+P3*A2
        sx3=-P2+P3*A1
        u1o=A5*sym.sign(P3)
        X1d=X2
        X2d=X3
        X3d=A4*u1o-A1*X3-A2*X2-A3*X1
        X3d.subs(u1o, A5*sym.sign(P3))

        self.eq_tmp_p1 = [us1v, us2v, us3v, H, Lg, sx1, sx2, sx3, u1o, X1d, X2d, X3d]

        us12=X2
        us22=X3
        us32=A42*U1+A52*U2-A12*X3-A22*X2-A32*X1
        Lg2=LA0*(D12*X1+D22*X2+D32*X3+D42*U1*U1+D52*U2*U2)+LA1*(B12*X1+B22*X2)+LA2*(C12*X1+C22*X2)+P1*(dX1-X2)+P2*(dX2-X3)+P3*(dX3-A42*U1-A52*U2+A12*X3+A22*X2+A32*X1)
        H2=-(LA0*(D12*X1+D22*X2+D32*X3+D42*U1*U1+D52*U2*U2)+LA1*(B12*X1+B22*X2)+LA2*(C12*X1+C22*X2))+P1*X2+P2*X3+P3*(A42*U1+A52*U2-A12*X3-A22*X2-A32*X1)
        sx12=LA0*D12+LA1*B12+LA2*C12+P3*A32
        sx22=LA0*D22+LA1*B22+LA2*C22-P1+P3*A22
        sx32=LA0*D32-P2+P3*A12
        P1T=-LA0*D8G-LA1*B6G-LA2*C6G
        P2T=-LA0*D9G-LA1*B7G-LA2*C7G
        P3T=-LA0*D0G-LA1*B8G-LA2*C8G
        dfl2=LA0*G0+LA1*G1+LA2*G2+LA0*(D6G+D8G*dX1+D9G*dX2+D0G*dX3)+LA1*(B4G+B6G*dX1+B7G*dX2+B8G*dX3)+LA2*(C4G+C6G*dX1+C7G*dX2+C8G*dX3)
        u1o2=(P3*A42)/(2*LA0*D42)
        u2o2=(P3*A52)/(2*LA0*D52)
        u1o3=B32*sym.sign(P3)
        u2o3=C32*sym.sign(P3)
        #X1d2=X2
        #X2d2=X3
        #X3d2=A42*u1o2+A52*u2o2-A12*X3-A22*X2-A32*X1
        #X3d2.subs(u1o2, (P3*A42)/(2*LA0*D42))
        #X3d2.subs(u2o2, (P3*A52)/(2*LA0*D52))

        self.eq_tmp_p2 = [us12, us22, us32, H2, Lg2, sx12, sx22, sx32, P1T, P2T, P3T, dfl2, u1o2, u2o2, u1o3, u2o3]
        self.equations = [self.eq_tmp_p1, self.eq_tmp_p2]
        return 

    def equation_variant(self, variant_i):
        keys = self.variant_labels
        values = variant_i
        subs_dict = dict(zip(keys, values))
        self.eq_var_p1 = self.eq_tmp_p1.copy()
        self.eq_var_p2 = self.eq_tmp_p2.copy()
        self.eqs_var = [self.eq_var_p1, self.eq_var_p2]
        for i in range(len(self.eqs_var)):
            for j in range(len(self.eqs_var[i])):
                self.eqs_var[i][j] = self.equations[i][j].subs(subs_dict)
        return

    def make_latex(self, variant_i):
        self.var_latex = variant_i.copy()
        for i in range(len(self.var_latex)):
            self.var_latex[i] = sym.latex(variant_i[i])
        self.latex_1_p1 = r'$\frac{d^3 x}{dt^3}+' + self.var_latex[0] + r'\frac{d^2 x}{dt^2}+' + self.var_latex[1] + r'\frac{dx}{dt}+' + self.var_latex[2] + r'x=' + self.var_latex[3] + r'u_1$'
        self.latex_2_p1 = r'$\int_{t_0}^{t_1} (' + self.var_latex[5] + r'x_1+' + self.var_latex[6] + r'x_2) dt' + r'=0$'
        self.latex_3_p1 = r'$\int_{t_0}^{t_1} (' + self.var_latex[8] + r'x_1+' + self.var_latex[9] + r'x_2) dt' + r'=0$'
        self.latex_4_p1 = r'$J=\int_{t_0}^{t_1} dt\rightarrow min$'
        self.latex_5_p1 = r'$x(t_0) \: и \: x(t_1) \: заданы$'
        self.latex_6_p1 = r'$\mid u_1 \mid \leq' + self.var_latex[4] + r'$'
    

        self.latex_1_p2 = r'$\frac{d^3 x}{dt^3}+' + self.var_latex[16] + r'\frac{d^2 x}{dt^2}+' + self.var_latex[17] + r'\frac{dx}{dt}+' + self.var_latex[18] + r'x=' + self.var_latex[19] + r'u_1+' + self.var_latex[20] + r'u_2$'
        self.latex_2_p2 = r'$\int_{t_0}^{t_1} (' + self.var_latex[21] + r'x_1+' + self.var_latex[22] + r'x_2) dt +' + self.var_latex[24] + r't_1+' + self.var_latex[26] + r'x_1(t_1)+' + self.var_latex[27] + r'x_2(t_1)+' + self.var_latex[28] + r'x_3(t_1)=0$'
        self.latex_3_p2 = r'$\int_{t_0}^{t_1} (' + self.var_latex[29] + r'x_1+' + self.var_latex[30] + r'x_2) dt +' + self.var_latex[32] + r't_1+' + self.var_latex[34] + r'x_1(t_1)+' + self.var_latex[35] + r'x_2(t_1)+' + self.var_latex[36] + r'x_3(t_1)=0$'
        self.latex_4_p2 = r'$\int_{t_0}^{t_1} (' + self.var_latex[37] + r'x_1+' + self.var_latex[38] + r'x_2+' + self.var_latex[39] + r'x_3+' + self.var_latex[40] + r'u_1^2+' + self.var_latex[41] + r'u_2^2) dt+' + self.var_latex[42] + r't_1+' + self.var_latex[44] + r'x_1(t_1)+' + self.var_latex[45] + r'x_2(t_1)+' + self.var_latex[46] + r'x_3(t_1)\rightarrow min$'
        self.latex_5_p2 = r'$Значения \: x(t_1) \: и \: t_1 \: не \: заданы$'
        self.latex_6_p2 = r'$\mid u_1\mid \leq' + self.var_latex[23] + r'\mid u_2\mid \leq' + self.var_latex[31] + r'$'
        
        return

    def check_equations(self, input_data, target_equation):
        try:
            stripped_input_data = input_data.replace("(T1)", "")
            sym_input_data = sym.sympify(stripped_input_data)
            if ((sym_input_data == target_equation)
            or (sym.simplify(sym_input_data) == sym.simplify(target_equation))
            or (sym.expand(sym_input_data) == sym.expand(target_equation))
            ):
                res = True
            else:
                res = False
        except Exception:
            res = False
        return res

    def check_step(self, input_data, cur_step, cur_part):
        #self.prompt1 = self.steps[cur_part-1][cur_step][1] 
        #self.prompt2 = self.steps[cur_part-1][cur_step][2]
        self.prompt3 = self.steps[cur_part-1][cur_step][3]
        target_equation = self.eqs_var[cur_part-1][cur_step]
        if (self.check_equations(input_data, target_equation)):
            res = True
            new_str = self.prompt3 + "\r\n" + input_data + "\r\n"
            self.history[cur_part-1] += new_str
        else:
            res = False
        return res
    
    def generateVariant(self):
        self.usr_var = 26 # SAME HERE CHANGE IT LATER
        random.seed()
        for i in range(len(self.variant_generated)):
            rnd_int = random.randint(1, 5)
            self.variant_generated[i] = rnd_int
        if self.usr_var_picked == True:
            self.current_step_p1 = 0
            self.current_step_p2 = 0
            self.completed_p1 = False
            self.completed_p2 = False
        else:
            self.usr_var_picked = True
        new_str = "Выбран сгенерированный вариант \r\n"
        self.history[0] += new_str
        self.history[1] += new_str
        self.equation_template()
        self.equation_variant(self.variants[int(self.usr_var)-1])
        # ОТЛАДОЧНЫЙ ВЫВОД
        #print(self.variant_generated)
        return

    def setVariant(self, var_i):
        self.usr_var = var_i
        if self.usr_var_picked == True:
            self.current_step_p1 = 0
            self.current_step_p2 = 0
            self.completed_p1 = False
            self.completed_p2 = False
        else:
            self.usr_var_picked = True
        new_str = "Выбран вариант " + str(var_i) + "\r\n"
        self.history[0] += new_str
        self.history[1] += new_str
        self.equation_template()
        self.equation_variant(self.variants[int(self.usr_var)-1])
        return

    def next_input_p1(self, input_data):
        if (self.check_step(input_data, self.current_step_p1, 1)):
            if (self.current_step_p1 < (len(self.steps_p1) - 1)):
                self.current_step_p1 += 1
                res = True
            else:
                self.current_step_p1 = 0
                res = True
                self.completed_p1 = True
        else:
            res = False
        return res

    def next_input_p2(self, input_data):
        if (self.check_step(input_data, self.current_step_p2, 2)):
            if (self.current_step_p2 < (len(self.steps_p2) - 1)):
                self.current_step_p2 += 1
                res = True
            else:
                self.current_step_p2 = 0
                res = True
                self.completed_p2 = True
        else:
            res = False
        return res
