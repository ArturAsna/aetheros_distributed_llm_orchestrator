class GlobalContext:
    def __init__(self):
        self.shared = {}

    def update(self, key, value):
        self.shared[key] = value

    def get(self, key, default=None):
        return self.shared.get(key, default)
