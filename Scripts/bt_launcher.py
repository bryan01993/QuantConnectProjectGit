import os, sys
launcher_path = os.path.join(os.path.dirname(__file__), 'Launchers', 'bt_launcher.py')
with open(launcher_path, 'r') as f:
    exec(compile(f.read(), launcher_path, 'exec'), {'__name__': '__main__', '__file__': launcher_path})
