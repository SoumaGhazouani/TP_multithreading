import unittest
import numpy.testing as npt
from task import Task


class TestTask(unittest.TestCase):
    def test_matrix_multiplication(self):
        size = 10
        task = Task(size=size)
        task.work()

        # Vérification des résultats
        npt.assert_allclose(
            task.a @ task.x,
            task.b,
            rtol=1e-5,
            atol=0,
            err_msg="Erreur : la solution calculée n'est pas correcte",
        )

    def test_task_serialization(self):
        # Instanciation d'une première tâche
        a = Task(identifier=1)
        a.work()

        # Sérialisation en JSON
        txt = a.to_json()

        # Désérialisation pour créer une deuxième tâche
        b = Task.from_json(txt)

        # Vérification que les deux tâches sont identiques
        self.assertEqual(
            a, b, "The deserialized task is not equal to the original task."
        )


if __name__ == "__main__":
    unittest.main()
