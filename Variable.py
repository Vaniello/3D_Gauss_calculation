from math import ceil
from numpy import arange


class Variable:
    def __init__(self, name: str, min: str, max: str, step: str, SD: str, mean: str):
        """
        Main object for one variable (X, Y, Z)
        """
        self._name = name
        self._min = float(min)
        self._max = float(max)
        self._step = float(step)
        self._SD = float(SD)
        self._mean = float(mean)
        self._range = self.set_range()

    def set_range(self) -> list:
        """
        set range for this value with given step, include min and max value
        first range value = min parameter value;
        last range value = max parameter value;
        if parameter step is integer - start iterating from integer ceil to minimum to integer floor to maximum
        else - iterating from min to max
        :return: variable range list
        """

        if int(self._step) == self._step:  # Check is step equals integer
            var_range = [self._min] + list(arange(ceil(self._min), ceil(self._max), self._step)) + [self._max]
        else:
            var_range = list(arange(self._min, self._max, self._step))
            if var_range[-1] != self._max:
                var_range.append(self._max)

        return var_range

    @property
    def SD(self) -> float:
        return self._SD

    @property
    def mean(self) -> float:
        return self._mean

    @property
    def range(self) -> list:
        return self._range
