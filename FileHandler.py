class FileHandler:
    @staticmethod
    def readFile(filename):
        try:
            with open(filename, 'r') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: {filename} not found")
    
    @staticmethod
    def writeFile(filename, content):
        with open(filename, 'w') as f:
            f.write(content)