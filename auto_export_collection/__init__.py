from aqt import gui_hooks

def log(msg):
    print('[{0}]: {1}'.format(__name__, msg))

def f():
    log('logged by addon after backup')

gui_hooks.backup_did_complete.append(f)
