class Struct:
    def __init__(self, input: dict):
        assert isinstance(input, dict)
        for key, val in input.items():
            if isinstance(val, (list, tuple)):
                setattr(self, key, [DictObj(x) if isinstance(x, dict) else x for x in val])
            else:
                setattr(self, key, DictObj(val) if isinstance(val, dict) else val)
