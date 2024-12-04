import unittest
import numpy as np
import numpy.testing as npt
from task import Task


class TestTask(unittest.TestCase):
    def test_solve_ax_equals_b(self):
        task = Task(size=5)

        task.work()

        npt.assert_allclose(np.dot(task.a, task.x), task.b, rtol=1e-5, atol=1e-8)


if __name__ == "__main__":
    unittest.main()
