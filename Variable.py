from math import ceil, floor

class Variable:
    def __init__(self, name, min, max, step, SD, mean):
        """
        Main object for one variable (X, Y, Z)
        """
        self.name = name
        self.min = float(min)
        self.max = float(max)
        self.step = float(step)
        self.SD = float(SD)
        self.mean = float(mean)
        self.range = self.set_range(self.min, self.max, self.step)

    def set_range(self, min, max, step):
        """
        set range for this value with given step, include min and max value
        first range value = min parameter value;
        last range value = max parameter value;
        if parameter step is integer - start iterating from integer ceil to minimum to integer floor to maximum
        else - iterating from min to max
        """
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