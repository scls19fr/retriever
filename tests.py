"""Database Toolkit Tests

This module, when run, runs all unit tests from all DBTK scripts referenced in
dbtk_wizard.py, for each engine in ALL_ENGINES from dbtk_engines.py. In other
words, it runs tests for each possible combination of database platform and
script.

The tests generally run the script, import the resulting data, and check the
MD5 checksum against a known static value.

"""

import os
import unittest
from lib.engines import ENGINES_TO_TEST, choose_engine
from lib.tools import TEST_ENGINES, get_opts
from scripts.all import MODULE_LIST


TEST_DATA_LOCATION = "test_data"

try:
    os.makedirs(TEST_DATA_LOCATION)
except:
    pass

for engine in ENGINES_TO_TEST:
    opts = get_opts()
    opts["engine"] = engine.abbreviation
    
    TEST_ENGINES[engine.abbreviation] = choose_engine(opts)
    TEST_ENGINES[engine.abbreviation].get_cursor()
    
def get_tests():
    suite = unittest.TestSuite()
    for module in MODULE_LIST:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(module))
    return suite

unittest.main(defaultTest="get_tests")