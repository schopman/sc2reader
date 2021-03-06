from .processors import *
from .readers import *
from .utils import AttributeDict

ALL_FILES = [
    'replay.initData',
    'replay.details',
    'replay.attributes.events',
    'replay.message.events',
    'replay.game.events'
]

files = AttributeDict(
    all=[
        'replay.initData',
        'replay.details',
        'replay.attributes.events',
        'replay.message.events',
        'replay.game.events'],

    partial=[
        'replay.initData',
        'replay.details',
        'replay.attributes.events',
        'replay.message.events',],

    basic=[
        'replay.initData',
        'replay.details',
        'replay.attributes.events'],

    minimal=[
        'replay.initData',],

    none=[]
)

default_options = AttributeDict(
    directory="",
    processors=[],
    debug=False,
    verbose=False,
    parse_events=True,
    include_regex=None,
    exclude_dirs=[],
    recursive=True,
    depth=-1,
    follow_symlinks=True,
    files=files.all
)

class ReaderMap(dict):
    def __init__(self):
        self.set1 = {
                'replay.initData': InitDataReader(),
                'replay.details': DetailsReader(),
                'replay.attributes.events': AttributeEventsReader(),
                'replay.message.events': MessageEventsReader(),
                'replay.game.events': GameEventsReader(),
            }

        self.set2 = {
                'replay.initData': InitDataReader(),
                'replay.details': DetailsReader(),
                'replay.attributes.events': AttributeEventsReader(),
                'replay.message.events': MessageEventsReader(),
                'replay.game.events': GameEventsReader_16561(),
            }

        self.set3 = {
                'replay.initData': InitDataReader(),
                'replay.details': DetailsReader(),
                'replay.attributes.events': AttributeEventsReader_17326(),
                'replay.message.events': MessageEventsReader(),
                'replay.game.events': GameEventsReader_16561(),
            }

        self.set4 = {
                'replay.initData': InitDataReader(),
                'replay.details': DetailsReader(),
                'replay.attributes.events': AttributeEventsReader_17326(),
                'replay.message.events': MessageEventsReader(),
                'replay.game.events': GameEventsReader_18574(),
        }

        for key in (16117,16195,16223,16291):
            self[key] = self.set1

        for key in (16561,16605,16755,16939):
            self[key] = self.set2

        for key in (17326,17682,17811,18092,18221,18317):
            self[key] = self.set3

        for key in (18574,):
            self[key] = self.set4

    def __getitem__(self,key):
        try:
            return super(ReaderMap,self).__getitem__(key)
        except KeyError:
            return self.set4

readers = ReaderMap()
