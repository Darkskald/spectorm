from spectorm.exceptions import InvalidSpectrumError
from spectorm.spectrum.spectrum_meta import MetaSpectrum
import matplotlib.pyplot as plt
import numpy as np


class BasicPlotter:
    """The class to handle basic plotting functionality, usually acting on a list of spectrum objects"""

    def __init__(self, spec_list):
        temp = list(filter(BasicPlotter.check_metaclass, spec_list))
        if False in temp:
            raise InvalidSpectrumError("At least one member of spec_list is not valid spec object!")
        self.spec_list = spec_list

    def plot_all(self, title="Default", style="default", save=False, save_path=None):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xlabel(self.spec_list[0].x_unit)
        ax.set_ylabel(self.spec_list[0].y_unit)

    @staticmethod
    def check_metaclass(item):
        if type(type(item)) != MetaSpectrum:
            return False
        else:
            return True
