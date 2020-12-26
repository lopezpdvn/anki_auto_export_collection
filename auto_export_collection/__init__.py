from anki import hooks

def log(msg):
    print('[{0}]: {1}'.format(__name__, msg))
