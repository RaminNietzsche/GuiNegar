import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
setup(
    name = "GNegar",
    version = "0.1",
    author = "Ramin Najjarbashi",
    author_email = "Ramin.Najarbashi@gmail.com",
    packages = find_packages() + ['lib'],
    scripts=['bin/GNegar_Main.py'],
    description = "Negar is a spell corrector and Persian text editor",
    license = "GPL",
    keywords = "spellcheck Persian editor",
    url = "http://raminnietzsche.github.com/GuiNegar/",
    long_description=read
    ('README.txt'),    
)


