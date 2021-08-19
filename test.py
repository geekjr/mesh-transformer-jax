print(
    "import sys\nimport os\nimport tempfile\nimport shutil\n\nimport python2\nimport python3\n\n\nimport pkg_resources\nif python3:\n    basestring = str\n\n\ndef _get_relative_path(filename, dest_dir):\n    \n    Wrapper for ``pkg_resources.get_filename()``.\n\n    It will find the ``dest_dir`` and ``filename`` relative, then\n    it will return it in the destination directory.\n\n: param dest_dir: The directory to search in\n: param filename: The file to search in\n: returns: ``filename`` relative to ``dest_dir``\n    \n    dest_dir=os.path.abspath(dest_dir)\n    dest_dir=os.path.abspath(dest_dir)\n    dest_dir=os.path.abspath(dest_dir)\n return os.path.relpath(filename, dest_dir)\n\n\ndef _find_test_files(filename, dest_dir, tests_file_name): \n    \n    Wrapper for ``pkg_resources.find_test_files()``.\n\n    It will find the tests file and returns it in the test directory.\n    If the tests file is not found then it will return a list of all\n    files in the test directory.\n\n: param tests_file_name: The file to look for\n: param dest_dir: The directory to look in\n: param tests_file_name: The file to look in\n\n: returns: A list of files in the test directory\n    \n    tests_file=pkg_resources.find_test_file(tests_file_name, dest_dir)\n if not tests_file: \n return [\'*\']\n\n    return [\n        f for f in files\n        if f.startswith(os.path.join(\'test\', \'\', \'*\'))\n   '")
