import os

def find_venv(directory):
    if 'venv' in os.listdir(directory):
        return os.path.join(directory, 'venv', 'bin', 'python')
    return find_venv(os.path.join(directory, '..'))

def Settings(**kwargs):
    return {
        'interpreter_path': find_venv(os.getcwd())
    }
