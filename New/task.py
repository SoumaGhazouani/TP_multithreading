import time
import numpy as np
import json


class Task:
    def __init__(self, identifier=0, size=None):
        self.identifier = identifier
        # choosee the size of the problem
        self.size = size or np.random.randint(300, 3_000)
        # Generate the input of the problem
        self.a = np.random.rand(self.size, self.size)
        self.b = np.random.rand(self.size)
        # prepare room for the results
        self.x = np.zeros((self.size))
        self.time = 0

    def work(self):
        start = time.perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        self.time = time.perf_counter() - start

    def to_json(self) -> str:
        """Convert the Task object to a JSON string."""
        return json.dumps({
            "identifier": self.identifier,
            "size": self.size,
            "a": self.a.tolist(),  
            "b": self.b.tolist(),
            "x": self.x.tolist(),
            "time": self.time
        })
    
    @staticmethod
    def from_json(text: str) -> "Task":
        """Create a Task object from a JSON string."""
        data = json.loads(text)
        task = Task(identifier=data["identifier"], size=data["size"])
        task.a = np.array(data["a"]) 
        task.b = np.array(data["b"])
        task.x = np.array(data["x"])
        task.time = data["time"]
        return task
    
    def __eq__(self, other: "Task") -> bool:
        """Check if two Task objects are equal."""
        if not isinstance(other, Task):
            return NotImplemented
        return (self.identifier == other.identifier and
                self.size == other.size and
                np.array_equal(self.a, other.a) and
                np.array_equal(self.b, other.b) and
                np.array_equal(self.x, other.x) and
                self.time == other.time)
   