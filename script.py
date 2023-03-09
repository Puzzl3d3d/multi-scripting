import threading
import os

DEBUG_MODE = True

def Debug(*args, **kwargs):
    """ For debug printing """
    if DEBUG_MODE:
        print("DEBUG |",*args, **kwargs)
def _NewThread(target: function, *args, **kwargs):
    Debug(*args, *kwargs)
    thread = threading.Thread(target, *kwargs)
    thread.join()
    return thread

scripts = []

class script:
    """ Main class """
    def __init__():
        pass
    def parse_file(file, *args, **kwargs):
        def target():
            execfile(os.path.abspath(file))
        thread = NewThread(target, *kwargs)
        self.thread = thread
    def parse_func(target, *args, **kwargs):
        thread = NewThread(target, *kwargs)
        self.thread = thread
    def parse_str(str, *args, **kwargs):
        def target():
            exec(compile(str, "<string>", "exec"))
        thread = NewThread(target, *kwargs)
        self.thread = thread
        scripts[self] = thread
    def start():
        self.thread.start()
    def run():
        self.thread.run()
    def is_alive():
        return self.thread.is_alive()

    @staticmethod
    def start_all_scripts():
        for script in scripts:
            script.start()
    @staticmethod
    def get_scripts():
        return scripts
