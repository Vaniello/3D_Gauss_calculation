import os
from datetime import datetime
import xlsxwriter


class XL_book:
    def __init__(self):
        """
        Initialization an Excel workbook to writing calculation results
        """
        self.book = xlsxwriter.Workbook(os.path.join(os.getcwd(), f'3G_output_{datetime.now().strftime("%H-%M-%S")}.xlsx'))
        self.bold = self.book.add_format({'bold': True})
        self.worksheet = self.book.add_worksheet('3D-Gauss')
        self.current_data_row = 2

    def fill_header(self, x_name: str, y_name: str, z_name: str) -> None:
        """
        create and fill header of the table
        :param x_name: Name of the X variable
        :param y_name: Name of the Y variable
        :param z_name: Name of the Z variable
        :return: None
        """
        self.worksheet.merge_range(0, 0, 0, 8, 'Параметри розподілу', self.bold)
        self.worksheet.merge_range(0, 9, 0, 11, 'Змінні', self.bold)
        self.worksheet.merge_range(0, 12, 0, 13, 'Результат', self.bold)

        self.worksheet.write(0, 15, f'X - {x_name}', self.bold)
        self.worksheet.write(1, 15, f'Y - {y_name}', self.bold)
        self.worksheet.write(2, 15, f'Z - {z_name}', self.bold)

        self.worksheet.write(1, 0, 'x_cep')
        self.worksheet.write(1, 1, 'y_cep')
        self.worksheet.write(1, 2, 'z_cep')

        self.worksheet.write(1, 3, 'x_CKB')
        self.worksheet.write(1, 4, 'y_СКВ')
        self.worksheet.write(1, 5, 'z_СКВ')

        self.worksheet.write(1, 6, 'r_xy')
        self.worksheet.write(1, 7, 'r_xz')
        self.worksheet.write(1, 8, 'r_yz')

        self.worksheet.write(1, 9, x_name, self.bold)
        self.worksheet.write(1, 10, y_name, self.bold)
        self.worksheet.write(1, 11, z_name, self.bold)

        self.worksheet.write(1, 12, 'k^2', self.bold)
        self.worksheet.write(1, 13, 'Pk', self.bold)

    def fill_main_data(self, main_data: list) -> None:
        """
        Write main data (mean, SD, correlations) of each variables
        The order in which the data should be:
        [x_mean, y_mean, z_mean, x_SD, y_SD, z_SD, r_xy, r_xz, r_yz]
        :param main_data:
        :return: None
        """
        self.worksheet.write_row(self.current_data_row, 0, main_data)

    def fill_calculated_data(self, x, y, z, k, probability) -> None:
        """
        Write calculated data
        :param x: Value X for which the k-index and probability are calculated
        :param y: Value Y for which the k-index and probability are calculated
        :param z: Value Z for which the k-index and probability are calculated
        :param k: k-index value for given x,y,z
        :param probability: probability value for giver x,y,z
        :return: None
        """
        self.worksheet.write(self.current_data_row, 9, x)
        self.worksheet.write(self.current_data_row, 10, y)
        self.worksheet.write(self.current_data_row, 11, z)
        self.worksheet.write(self.current_data_row, 12, k)
        self.worksheet.write(self.current_data_row, 13, probability)

        self.current_data_row += 1

    def close_book(self) -> None:
        """
        Save and close this book
        :return: None
        """
        self.book.close()

