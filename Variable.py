from math import ceil
from numpy import arange

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
        self.range = self.set_range()

    def set_range(self):
        """
        set range for this value with given step, include min and max value
        first range value = min parameter value;
        last range value = max parameter value;
        if parameter step is integer - start iterating from integer ceil to minimum to integer floor to maximum
        else - iterating from min to max
        """

        if int(self.step) == self.step:  # Check is step equals integer
            var_range = [self.min] + list(arange(ceil(self.min), ceil(self.max), self.step)) + [self.max]
        else:
            var_range = list(arange(self.min, self.max, self.step))
            if var_range[-1] != self.max:
                var_range.append(self.max)

        return var_range