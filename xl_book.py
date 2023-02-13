from os import getcwd
from math import exp
from datetime import datetime
import xlsxwriter


class XL_book:
    def __init__(self, x_obj, y_obj, z_obj, r_xy, r_xz, r_yz):
        self.x = x_obj
        self.y = y_obj
        self.z = z_obj
        self.book = xlsxwriter.Workbook(getcwd()+ '\\3G_output_' + datetime.now().strftime('%H-%M-%S') + '.xlsx')
        self.bold = self.book.add_format({'bold': True})
        self.worksheet = self.book.add_worksheet('3G')
        self.r_xy = r_xy
        self.r_xz = r_xz
        self.r_yz = r_yz
        self.paste_row = 2

    def fill_header(self):
        self.worksheet.merge_range(0, 0, 0, 8, 'Параметри розподілу', self.bold)
        self.worksheet.merge_range(0, 9, 0, 11, 'Змінні', self.bold)
        self.worksheet.merge_range(0, 12, 0, 13, 'Результат', self.bold)

        self.worksheet.write(0, 15, 'X - ' + self.x.name, self.bold)
        self.worksheet.write(1, 15, 'Y - ' + self.y.name, self.bold)
        self.worksheet.write(2, 15, 'Z - ' + self.z.name, self.bold)

        self.worksheet.write(1, 0, 'x_cep')
        self.worksheet.write(1, 1, 'y_cep')
        self.worksheet.write(1, 2, 'z_cep')

        self.worksheet.write(1, 3, 'x_CKB')
        self.worksheet.write(1, 4, 'y_СКВ')
        self.worksheet.write(1, 5, 'z_СКВ')

        self.worksheet.write(1, 6, 'r_xy')
        self.worksheet.write(1, 7, 'r_xz')
        self.worksheet.write(1, 8, 'r_yz')

        self.worksheet.write(1, 9, self.x.name, self.bold)
        self.worksheet.write(1, 10, self.y.name, self.bold)
        self.worksheet.write(1, 11, self.z.name, self.bold)

        self.worksheet.write(1, 12, 'k^2', self.bold)
        self.worksheet.write(1, 13, 'Pk', self.bold)

    def k_coef(self, x, y, z):
        d_x = x - self.x.mean
        d_y = y - self.y.mean
        d_z = z - self.z.mean

        k = (((d_x/self.x.SD)**2) * ((1 - self.r_yz)**2) +
             ((d_y/self.y.SD)**2) * ((1 - self.r_xz)**2) +
             ((d_z/self.z.SD)**2) * ((1 - self.r_xy)**2) +
             ((2 * d_x * d_y) / (self.x.SD * self.y.SD)) * (self.r_xz * self.r_yz - self.r_xy) +
             ((2 * d_x * d_z) / (self.x.SD * self.z.SD)) * (self.r_xy * self.r_yz - self.r_xz) +
             ((2 * d_y * d_z) / (self.y.SD * self.z.SD)) * (self.r_xz * self.r_xy - self.r_yz)
            )
        return k

    def probability(self, k):
        p = 1 - exp(-k/2)
        return p

    def fill_main_info(self):
        self.worksheet.write(self.paste_row, 0, self.x.mean)
        self.worksheet.write(self.paste_row, 1, self.y.mean)
        self.worksheet.write(self.paste_row, 2, self.z.mean)

        self.worksheet.write(self.paste_row, 3, self.x.SD)
        self.worksheet.write(self.paste_row, 4, self.y.SD)
        self.worksheet.write(self.paste_row, 5, self.z.SD)

        self.worksheet.write(self.paste_row, 6, self.r_xy)
        self.worksheet.write(self.paste_row, 7, self.r_xz)
        self.worksheet.write(self.paste_row, 8, self.r_yz)

    def fill_row(self, x, y, z):
        self.worksheet.write(self.paste_row, 9, x)
        self.worksheet.write(self.paste_row, 10, y)
        self.worksheet.write(self.paste_row, 11, z)

        k = self.k_coef(x, y, z)

        self.worksheet.write(self.paste_row, 12, k)
        self.worksheet.write(self.paste_row, 13, self.probability(k))

        self.paste_row += 1

    def fill_book(self):
        self.fill_main_info()
        for i in self.x.range:
            for j in self.y.range:
                for k in self.z.range:
                    self.fill_row(i, j, k)

    def close_book(self):
        self.book.close()

