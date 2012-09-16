from distutils.core import setup
from setuptools import  find_packages

if __name__ == '__main__':

    setup(	
        name = "gnegar",
        version = "0.1.1",
        author = "Ramin Najjarbashi",
        author_email = "Ramin.Najarbashi@gmail.com",
        #packages = find_packages() + ['lib'],
        package_dir = {'':'lib'},
        packages = [''],
        scripts=['bin/gnegar'],
        description = "Negar is a spell corrector and Persian text editor",
        license = "GPL",
        url = "http://RaminNietzsche.github.com/GuiNegar",
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


