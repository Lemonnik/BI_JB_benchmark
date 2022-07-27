from abc import ABC, abstractmethod

from torch.nn import Module


class DtiModel(Module, ABC):
    """
    Base Class for making models which are compatible with our DTI benchmark.
    It is necessary to have ``return_type`` attribute and ``__call__`` method.

    Attributes
    ----------
    return_type: list
        Defines what features should be returned by ``__getitem__`` method of DTI dataset.
        Read-only.
    """

    @property
    def return_type(self):
        return self._return_type

    @abstractmethod
    def __call__(self, data, train=True):
        """
        Should call ``forward`` method and return:
            loss in `train` mode
            correct_labels, predicted_labels, predicted_scores if not in `train` mode
        """
        ...
