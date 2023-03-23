class FileHandler:
    @staticmethod
    def read_file(filename):
        try:
            with open(filename, 'r') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: {filename} not found")
    
    @staticmethod
    def write_file(filename, content):
        with open(filename, 'w') as f:
            f.write(content)