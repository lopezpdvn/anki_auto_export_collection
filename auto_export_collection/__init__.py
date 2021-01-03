from os.path import join, normpath, dirname
from anki.exporting import AnkiCollectionPackageExporter
from aqt import gui_hooks, mw

def get_export_filepath():
    config = mw.addonManager.getConfig(__name__)
    path_suffix = normpath(config['export_filepath_rel_to_collection_dir'])
    return join(dirname(mw.col.path), path_suffix)

def log(msg):
    print('[{0}]: {1}'.format(__name__, msg))

def f():
    fpath = get_export_filepath()
    log('Exporting to `{0}`...'.format(fpath))

    exporter = AnkiCollectionPackageExporter(mw.col)
    exporter.includeMedia = False

    do_export = lambda: exporter.exportInto(fpath)
    on_done = lambda: log('logged by addon after backup')

    mw.taskman.run_in_background(do_export, on_done)

#gui_hooks.backup_did_complete.append(f)
gui_hooks.profile_will_close.append(f)
