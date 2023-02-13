from math import ceil, floor

class Variable:
    def __init__(self, name, min, max, step, SD, mean):
        self.name = name
        self.min = float(min)
        self.max = float(max)
        self.step = float(step)
        self.SD = float(SD)
        self.mean = float(mean)
        self.range = self.set_range(self.min, self.max, self.step)

    def set_range(self, min, max, step):
        var_range = []
        if step == 1:
            step_int = True
        else:
            step_int = False
        if step_int:
            i = ceil(min)
            fin = floor(max)
            var_range.append(min)
        else:
            i = min
            fin = max

        while i <= fin:
            var_range.append(i)
            i += step

        if step_int:
            var_range.append(max)
        elif var_range[-1] != fin:
            var_range.append(max)

        return var_range