from xl_book import XL_book
from Variable import Variable
from Window import Window

def f(w):
    x = w.get_x_param()
    y = w.get_y_param()
    z = w.get_z_param()
    xl = XL_book(x, y, z, w.get_r_xy(), w.get_r_xz(), w.get_r_yz())
    xl.fill_header()
    xl.fill_book()
    xl.close_book()

if __name__ == '__main__':
    main = Window()

    main.add_ok_btn(f, main)
    main.start()

