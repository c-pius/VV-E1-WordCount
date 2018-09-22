from pathlib import Path

class InputReader:
    identifier: str = ""
    def readInput(self):
        pass

class CommandLineReader(InputReader):
    """
    Reads input from the command line (line by line)
    """

    prompt: str = None

    def __init__(self, prompt: str = ""):
        self.identifier = prompt
        self.prompt = prompt

    def readInput(self):
        return input(self.prompt)

class FileReader(InputReader):
    """
    Reads input from a file (whole file at once)
    """

    path: Path = None

    def __init__(self, filePath):
        self.identifier = filePath

        # assign the path from the parameter
        if isinstance(filePath, str):
            self.path = Path(filePath)
        elif isinstance(filePath, Path):
            self.path = filePath
        else:
            raise(ValueError("expected str or Path"))

        # check if the file exists
        assert self.path.is_file(), "file does not exist"

    def readInput(self):
        """
        Reads the contents of the file and returns it (reads the whole file at once)
        """
        with open(self.path) as file:
            s = file.read()
            return s