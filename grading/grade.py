"""
Grade a given ipynb file with okpy tests
"""
import json
import argparse
from glob import glob
import os
import doctest
import copy
from contextlib import redirect_stdout, redirect_stderr

def code_from_ipynb(path, ignore_errors=True):
    """
    Get the code for a given notebook

    nb is passed in as a dictionary that's a parsed ipynb file
    """
    globs = {}
    with open(path) as f:
        nb = json.load(f)
        for cell in nb['cells']:
            if cell['cell_type'] == 'code':
                # transform the input to executable Python
                source = '\n'.join(cell['source']).replace('%matplotlib inline', '')
                try:
                    with open('/dev/null', 'w') as f, redirect_stdout(f), redirect_stderr(f):
                        exec(source, globs)
                except Exception as e:
                    if not ignore_errors:
                        raise
    return globs

def run_tests(ipynb_path, globs):
    base_path = os.path.dirname(ipynb_path)
    test_files = glob(os.path.join(base_path, 'tests/q*.py'))
    tests = []
    doctestparser = doctest.DocTestParser()
    results = []
    for test_file in test_files:
        test_file_globals = {}
        with open(test_file) as f:
            doctestrunner = doctest.DocTestRunner()

            exec(f.read(), test_file_globals)
            defined_test = test_file_globals['test']
            assert len(defined_test['suites']) == 1
            assert defined_test['points'] == 1

            for case in defined_test['suites'][0]['cases']:
                examples = doctestparser.parse(
                    case['code'],
                    defined_test['name'],
                )
                test = doctest.DocTest(
                    [e for e in examples if type(e) is doctest.Example],
                    globs,
                    defined_test['name'],
                    None,
                    None,
                    None
                )
                with open('/dev/null', 'w') as f, redirect_stdout(f), redirect_stderr(f):
                    doctestrunner.run(test, clear_globs=False)
            with open('/dev/null', 'w') as f, redirect_stdout(f), redirect_stderr(f):
                result = doctestrunner.summarize()
            results.append(1 if result.failed == 0 else 0)
    return (sum(results) / len(results))

def main():
    argparser = argparse.ArgumentParser()

    argparser.add_argument(
        'ipynb_path',
        help='Path to python file to grade'
    )

    args = argparser.parse_args()
    ipynb_path = os.path.abspath(args.ipynb_path)
    os.chdir(os.path.dirname(ipynb_path))

    globs = code_from_ipynb(ipynb_path)

    print(run_tests(ipynb_path, globs))

main()