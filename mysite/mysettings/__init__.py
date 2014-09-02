
import os


def factory():
    if 'NODE_ENV' in os.environ and os.environ['NODE_ENV'] == 'dev':
        from .dev import MyDevelSettings
        return MyDevelSettings()
    else:
        from .prod import MyProductionSettings
        return MyProductionSettings()
