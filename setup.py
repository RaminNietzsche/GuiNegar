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
        scripts=['bin/gnegar'],
        description = "Negar is a spell corrector and Persian text editor",
        license = "GPL",
        url = "http://RaminNietzsche.github.com/GuiNegar",
        long_description=read
            ('README'),
 	keywords=['spellcheck','Persian','editor','python'],
 	data_files = [('share/doc/gnegar',['README', 'COPYING', 'CHANGES']),
 	('share/man/man1/', ['man/gnegar.1']) ],
 	classifiers=[
 	'Development Status :: 0 - Beta',
 	'Intended Audience :: Persian Users',
 	'Intended Audience :: Persian Programmers',
	'License :: OSI Approved :: GNU General Public License v3',
 	'Operating System :: POSIX',
 	'Programming Language :: Python',
 	'Topic :: Editor',
 	'Topic :: Persian',
 	'Topic :: Spellcheck'
 	],    
)


