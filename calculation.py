from math import exp

from Variable import Variable
from xl_book import XL_Book


def calculate_3G_parameters(data: dict) -> None:
    """
    Makes basic calculations. Creates a workbook for the result. Writes the result to the workbook
    :param data:
    :return: None
    """
    x = Variable(data['X']['Name'], data['X']['Min'], data['X']['Max'],
                 data['X']['Step'], data['X']['SD'], data['X']['Mean'])
    y = Variable(data['Y']['Name'], data['Y']['Min'], data['Y']['Max'],
                 data['Y']['Step'], data['Y']['SD'], data['Y']['Mean'])
    z = Variable(data['Z']['Name'], data['Z']['Min'], data['Z']['Max'],
                 data['Z']['Step'], data['Z']['SD'], data['Z']['Mean'])
    xl = XL_Book()
    xl.fill_header(data['X']['Name'], data['Y']['Name'], data['Z']['Name'])
    main_data = [data['X']['Mean'], data['Y']['Mean'], data['Z']['Mean'],
                 data['X']['SD'], data['Y']['SD'], data['Z']['SD'],
                 data['Correlation']['XY'], data['Correlation']['XZ'], data['Correlation']['YZ']]
    for current_x in x.range:
        for current_y in y.range:
            for current_z in z.range:
                k_coef = k_coef_calculation(current_x, current_y, current_z, x, y, z, data['Correlation']['XY'],
                                            data['Correlation']['XZ'], data['Correlation']['YZ'])
                prob = probability(k_coef)
                xl.fill_main_data(main_data)
                xl.fill_calculated_data(current_x, current_y, current_z, k_coef, prob)

    xl.close_book()


def k_coef_calculation(current_x, current_y, current_z, x: Variable, y: Variable, z: Variable,
                       r_xy: float, r_xz: float, r_yz: float) -> float:
    """
    Calculate k-coefficient for some X, Y, Z values from range
    :param current_x: some value of X range variable
    :param current_y: some value of Y range variable
    :param current_z: some value of Z range variable
    :param x: Variable obj for X variable
    :param y: Variable obj for Y variable
    :param z: Variable obj for Z variable
    :param r_xy: Correlation between X variable and Y variable
    :param r_xz: Correlation between X variable and Z variable
    :param r_yz: Correlation between Y variable and Z variable
    :return: k-coefficient
    """
    d_x = current_x - x.mean
    d_y = current_y - y.mean
    d_z = current_z - z.mean

    k = (((d_x / x.SD) ** 2) * ((1 - r_yz) ** 2) +
         ((d_y / y.SD) ** 2) * ((1 - r_xz) ** 2) +
         ((d_z / z.SD) ** 2) * ((1 - r_xy) ** 2) +
         ((2 * d_x * d_y) / (x.SD * y.SD)) * (r_xz * r_yz - r_xy) +
         ((2 * d_x * d_z) / (x.SD * z.SD)) * (r_xy * r_yz - r_xz) +
         ((2 * d_y * d_z) / (y.SD * z.SD)) * (r_xz * r_xy - r_yz)
         )
    return k


def probability(k: float) -> float:
    """
    Calculate probability for given k-coefficient
    :param k: k-coefficient
    :return: probability
    """
    p = 1 - exp(-k / 2)
    return p
