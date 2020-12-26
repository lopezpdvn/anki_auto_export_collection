from anki.exporting import AnkiCollectionPackageExporter
from aqt import gui_hooks, mw

def log(msg):
    print('[{0}]: {1}'.format(__name__, msg))

def f():
    fpath = r'C:\pathh\a.cokpkg'

    exporter = AnkiCollectionPackageExporter(mw.col)
    exporter.includeMedia = False
    exporter.exportInto(fpath)

    log('logged by addon after backup')

#gui_hooks.backup_did_complete.append(f)
gui_hooks.profile_will_close.append(f)
