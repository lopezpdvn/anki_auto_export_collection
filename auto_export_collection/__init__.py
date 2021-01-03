from os.path import join, normpath, dirname
from anki import Collection
from anki.exporting import AnkiCollectionPackageExporter
from aqt import gui_hooks, mw

fpath = None
collection_path = None

def get_export_filepath():
    config = mw.addonManager.getConfig(__name__)
    path_suffix = normpath(config['export_filepath_rel_to_collection_dir'])
    return join(dirname(mw.col.path), path_suffix)

def log(msg):
    print('[{0}]: {1}'.format(__name__, msg))

def get_paths():
    global fpath, collection_path
    fpath = get_export_filepath()
    collection_path = mw.col.path

def export_col():
    if not collection_path or not fpath:
        return
    col = Collection(collection_path)
    exporter = AnkiCollectionPackageExporter(col)
    exporter.includeMedia = False
    log('Exporting to `{0}`...'.format(fpath))
    exporter.exportInto(fpath)

gui_hooks.profile_will_close.append(get_paths)
gui_hooks.backup_did_complete.append(export_col)
