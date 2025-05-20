class ParrotException(Exception):
    error: str
    details: str

    def __init__(self, error: str, details: str, *args):
        super().__init__(*args)
        self.error = error
        self.details = details
