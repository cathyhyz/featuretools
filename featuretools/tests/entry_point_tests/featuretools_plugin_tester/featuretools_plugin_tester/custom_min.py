import numpy as np

from featuretools.primitives.base import AggregationPrimitive
from featuretools.variable_types import Numeric


class CustomMinPlusOne(AggregationPrimitive):
    """Finds the mininium non-null value of a numeric feature plus one."""
    name = "custom_min_plus_one"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        def min_func(x):
            return np.min(x) + 1
        return min_func