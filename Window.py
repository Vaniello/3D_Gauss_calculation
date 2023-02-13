import os

from tkinter import *
import tkinter.messagebox

from calculation import calculate_3G_parameters


class Window:
    def __init__(self):
        self.root = Tk()
        self.root.title('3D-Gauss калькулятор')
        self.root.iconbitmap(os.path.join(os.getcwd(), 'icon', '3G.ico'))
        # row 0  ---  Main label
        self.main_label = Label(text="Введіть значення параметрів для розрахунку:")
        self.main_label.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
        # row 1  ---  Parameters labels (X, Y, Z)
        self.x_lab = Label(text='X')
        self.x_lab.grid(row=1, column=1, padx=10, pady=10)
        self.y_lab = Label(text='Y')
        self.y_lab.grid(row=1, column=2, padx=10, pady=10)
        self.z_lab = Label(text='Z')
        self.z_lab.grid(row=1, column=3, padx=10, pady=10)
        # row 2  ---   Fields for parameter names
        self.name_lab = Label(text="Назва раду:")
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
        self.step_lab = Label(text='Крок:')
        self.step_lab.grid(row=5, column=0, padx=10, pady=10)
        self.x_step = Entry(width=15)
        self.x_step.grid(row=5, column=1, padx=10, pady=10)
        self.y_step = Entry(width=15)
        self.y_step.grid(row=5, column=2, padx=10, pady=10)
        self.z_step = Entry(width=15)
        self.z_step.grid(row=5, column=3, padx=10, pady=10)
        # row 6  ---  Fields for the Standard Division(SD) of each parameter
        self.SD_lab = Label(text='SD(СКВ):')
        self.SD_lab.grid(row=6, column=0, padx=10, pady=10)
        self.x_SD = Entry(width=15)
        self.x_SD.grid(row=6, column=1, padx=10, pady=10)
        self.y_SD = Entry(width=15)
        self.y_SD.grid(row=6, column=2, padx=10, pady=10)
        self.z_SD = Entry(width=15)
        self.z_SD.grid(row=6, column=3, padx=10, pady=10)
        # row 7  ---  Fields for the mean values of each parameter
        self.mean_lab = Label(text='Середнє:')
        self.mean_lab.grid(row=7, column=0, padx=10, pady=10)
        self.x_mean = Entry(width=15)
        self.x_mean.grid(row=7, column=1, padx=10, pady=10)
        self.y_mean = Entry(width=15)
        self.y_mean.grid(row=7, column=2, padx=10, pady=10)
        self.z_mean = Entry(width=15)
        self.z_mean.grid(row=7, column=3, padx=10, pady=10)
        # row 8  ---  Correlation label
        self.r_lab = Label(text="Введіть значення корреляції для рядів:")
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
        # Add 'OK' button
        self.ok_btn = Button(text='Выполнить', command=self.ok_button_callback)
        self.ok_btn.grid(row=11, column=3, padx=30, pady=30)

    def start(self) -> None:
        """
        Run TK window
        :return:
        """
        mainloop()

    def collect_data(self) -> dict:
        """
        Collection of all variables characteristics from Window fields into a dictionary
        :return: data dictionary
        """
        data = {
            'X': {
                'Name': self.x_name.get(),
                'Mean': self.x_mean.get(),
                'Min': self.x_min.get(),
                'Max': self.x_max.get(),
                'SD': self.x_SD.get(),
                'Step': self.x_step.get()
            },
            'Y': {
                'Name': self.y_name.get(),
                'Mean': self.y_mean.get(),
                'Min': self.y_min.get(),
                'Max': self.y_max.get(),
                'SD': self.y_SD.get(),
                'Step': self.y_step.get()
            },
            'Z': {
                'Name': self.z_name.get(),
                'Mean': self.z_mean.get(),
                'Min': self.z_min.get(),
                'Max': self.z_max.get(),
                'SD': self.z_SD.get(),
                'Step': self.z_step.get()
            },
            'Correlation': {
                'XY': float(self.r_xy.get()),
                'XZ': float(self.r_xz.get()),
                'YZ': float(self.r_yz.get())
            }
        }
        return data

    def ok_button_callback(self) -> None:
        """
        Callback function of the OK button. Calculation of 3D-Gauss (3G) parameters after pressing this button.
        :return: None
        """
        try:
            data = self.collect_data()
            calculate_3G_parameters(data)
            tkinter.messagebox.showinfo(title="Готово", message="Файл успішно оброблено!\n"
                                                                "Результат збережений в файлі '3G_output...xslx'")
            continue_work = tkinter.messagebox.askyesno(title='Продовжуємо роботу?', message='Бажаєте продолжити?')
            if not continue_work:
                self.root.destroy()

        except ValueError:
            tkinter.messagebox.showerror(title='Помилка', message='Значення введені невірно або були пропущені!')
        except Exception as ex:
            tkinter.messagebox.showerror(title='Помилка', message='Щось пішло не так, перевірте введені значення та спробуйте ще!')
            print(ex)
