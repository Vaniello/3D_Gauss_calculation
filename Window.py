from tkinter import *
from tkinter import ttk
import tkinter.messagebox

from Variable import Variable

class Window:
    def __init__(self):
        self.root = Tk()
        self.root.title('3G калькулятор')
        self.root.iconbitmap('C:\\Users\\vanfi\\Desktop\\Python\\3G\\3G.ico')
        # row 0  ---  Main label
        self.main_label = Label(text="Введите показания для рассчетов:")
        self.main_label.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
        # row 1  ---  Parameters labels (X, Y, Z)
        self.x_lab = Label(text='X')
        self.x_lab.grid(row=1, column=1, padx=10, pady=10)
        self.y_lab = Label(text='Y')
        self.y_lab.grid(row=1, column=2, padx=10, pady=10)
        self.z_lab = Label(text='Z')
        self.z_lab.grid(row=1, column=3, padx=10, pady=10)
        # row 2  ---   Fields for parameter names
        self.name_lab = Label(text='Имя ряда:')
        self.name_lab.grid(row=2, column=0, padx=10, pady=10)
        self.x_name = Entry(width=15)
        self.x_name.grid(row=2, column=1, padx=10, pady=10)
        self.y_name = Entry(width=15)
        self.y_name.grid(row=2, column=2, padx=10, pady=10)
        self.z_name = Entry(width=15)
        self.z_name.grid(row=2, column=3, padx=10, pady=10)
        # row 3  ---  Fields for the minimal values of each parameter
        self.min_lab = Label(text='Min:')
        self.min_lab.grid(row=3, column=0, padx=10, pady=10)
        self.x_min = Entry(width=15)
        self.x_min.grid(row=3, column=1, padx=10, pady=10)
        self.y_min = Entry(width=15)
        self.y_min.grid(row=3, column=2, padx=10, pady=10)
        self.z_min = Entry(width=15)
        self.z_min.grid(row=3, column=3, padx=10, pady=10)
        # row 4  ---  Fields for the maximum values of each parameter
        self.max_lab = Label(text='Max:')
        self.max_lab.grid(row=4, column=0, padx=10, pady=10)
        self.x_max = Entry(width=15)
        self.x_max.grid(row=4, column=1, padx=10, pady=10)
        self.y_max = Entry(width=15)
        self.y_max.grid(row=4, column=2, padx=10, pady=10)
        self.z_max = Entry(width=15)
        self.z_max.grid(row=4, column=3, padx=10, pady=10)
        # row 5  ---  Fields for the values step of each parameter
        self.step_lab = Label(text='Шаг:')
        self.step_lab.grid(row=5, column=0, padx=10, pady=10)
        self.x_step = Entry(width=15)
        self.x_step.grid(row=5, column=1, padx=10, pady=10)
        self.y_step = Entry(width=15)
        self.y_step.grid(row=5, column=2, padx=10, pady=10)
        self.z_step = Entry(width=15)
        self.z_step.grid(row=5, column=3, padx=10, pady=10)
        # row 6  ---  Fields for the Standard Division(SD) of each parameter
        self.SD_lab = Label(text='SD:')
        self.SD_lab.grid(row=6, column=0, padx=10, pady=10)
        self.x_SD = Entry(width=15)
        self.x_SD.grid(row=6, column=1, padx=10, pady=10)
        self.y_SD = Entry(width=15)
        self.y_SD.grid(row=6, column=2, padx=10, pady=10)
        self.z_SD = Entry(width=15)
        self.z_SD.grid(row=6, column=3, padx=10, pady=10)
        # row 7  ---  Fields for the mean values of each parameter
        self.mean_lab = Label(text='Среднее:')
        self.mean_lab.grid(row=7, column=0, padx=10, pady=10)
        self.x_mean = Entry(width=15)
        self.x_mean.grid(row=7, column=1, padx=10, pady=10)
        self.y_mean = Entry(width=15)
        self.y_mean.grid(row=7, column=2, padx=10, pady=10)
        self.z_mean = Entry(width=15)
        self.z_mean.grid(row=7, column=3, padx=10, pady=10)
        # row 8  ---  Correlation label
        self.r_lab = Label(text="Введите показания корреляции для рядов:")
        self.r_lab.grid(row=8, column=1, columnspan=2, padx=10, pady=10)
        # row 9  ---  Label of parameter pairs for correlation
        self.r_xy_lab = Label(text='XY')
        self.r_xy_lab.grid(row=9, column=1, padx=10, pady=10)
        self.r_xz_lab = Label(text='XZ')
        self.r_xz_lab.grid(row=9, column=2, padx=10, pady=10)
        self.r_yz_lab = Label(text='YZ')
        self.r_yz_lab.grid(row=9, column=3, padx=10, pady=10)
        # row 10  ---  Fields for correlation values of parameter pairs
        self.r_xy = Entry(width=15)
        self.r_xy.grid(row=10, column=1, padx=10, pady=10)
        self.r_xz = Entry(width=15)
        self.r_xz.grid(row=10, column=2, padx=10, pady=10)
        self.r_yz = Entry(width=15)
        self.r_yz.grid(row=10, column=3, padx=10, pady=10)
        # row 11  ---   Footer text
        self.copyright = Label(text='©Created by Ivan Kostyrko', font=("Comic Sans MS", 7))
        self.copyright.grid(row=11, column=0, padx=10, pady=10)

    def add_ok_btn(self, func, w):
        def ff(func, w):
            try:
                func(w)
                tkinter.messagebox.showinfo(title="Выполнено", message="Файл успешно обработан!\n"
                                                                  "Результат записан в файл '3G_output...xslx'")
                continue_work = tkinter.messagebox.askyesno(title='?', message='Желаете продолжить?')
                if not continue_work:
                    self.root.destroy()

            except ValueError:
                tkinter.messagebox.showerror(title='Ошибка', message='Параметры записаны неправильно или пропущены!')
            # except TypeError:
            #     tkinter.messagebox.showerror(title='Ошибка', message='Параметры записаны неправильно или пропущены!')

        self.ok_btn = Button(text='Выполнить', command=lambda: ff(func,w))
        self.ok_btn.grid(row=11, column=3, padx=30, pady=30)

    def start(self):
        mainloop()

    def get_x_param(self):
        x = Variable(self.x_name.get(), self.x_min.get(), self.x_max.get(), self.x_step.get(), self.x_SD.get(), self.x_mean.get())
        return x

    def get_y_param(self):
        y = Variable(self.y_name.get(), self.y_min.get(), self.y_max.get(), self.y_step.get(), self.y_SD.get(), self.y_mean.get())
        return y

    def get_z_param(self):
        z = Variable(self.z_name.get(), self.z_min.get(), self.z_max.get(), self.z_step.get(), self.z_SD.get(), self.z_mean.get())
        return z

    def get_r_xy(self):
        return float(self.r_xy.get())

    def get_r_xz(self):
        return float(self.r_xz.get())

    def get_r_yz(self):
        return float(self.r_yz.get())