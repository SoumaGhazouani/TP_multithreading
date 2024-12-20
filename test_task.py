import unittest
import numpy as np
import numpy.testing as npt
from task import Task


class TestTask(unittest.TestCase):
    def test_solve_ax_equals_b(self):
        task = Task(size=5)

        task.work()

        npt.assert_allclose(np.dot(task.a, task.x), task.b, rtol=1e-5, atol=1e-8)

    def test_task_serialization(self):
        # Instanciation d'une première tâche
        a = Task(identifier=1)
        a.work()

        # Sérialisation en JSON
        txt = a.to_json()

        # Désérialisation pour créer une deuxième tâche
        b = Task.from_json(txt)

        # Vérification que les deux tâches sont identiques
        self.assertEqual(a, b, "The deserialized task is not equal to the original task.")

if __name__ == "__main__":
    unittest.main()
