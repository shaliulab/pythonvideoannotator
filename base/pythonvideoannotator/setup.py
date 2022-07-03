#!/usr/bin/python2
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re, os


PACKAGE_PATH = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(PACKAGE_PATH, 'pythonvideoannotator','__init__.py'), 'r') as fd:
    content = fd.read()
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)

with open(os.path.join(PACKAGE_PATH, '..','..','README.md'), 'r') as fd:
    long_description = fd.read()


# REQUIREMENTS BEGIN
REQUIREMENTS = [
    "geometry_designer==0.4.38",
	"modular-computer-vision-api-gui==0.3.31",
	"pyforms-gui-shaliulab==4.905.154",
	"modular-computer-vision-api==0.3.29",
	"python-video-annotator-models-gui-shaliulab==0.9.0",
	"python-video-annotator-models-shaliulab==0.9.0",
        "python-video-annotator-module-idtrackerai-shaliulab==1.0.6",
	"python-video-annotator-module-timeline==0.6.26",
	"python-video-annotator-module-eventstats==0.5.15",
	"python-video-annotator-module-virtual-object-generator==0.6.26",
	"python-video-annotator-module-deeplab==0.902.21",
	"python-video-annotator-module-contours-images==0.5.28",
	"python-video-annotator-module-tracking==0.6.38",
	"python-video-annotator-module-smooth-paths==0.5.19",
	"python-video-annotator-module-distances==0.5.18",
	"python-video-annotator-module-path-map==0.6.16",
	"python-video-annotator-module-motion-counter==0.5.26",
	"python-video-annotator-module-create-paths==0.5.15",
	"python-video-annotator-module-regions-filter==0.5.18",
	"python-video-annotator-module-import-export==0.5.23",
	"python-video-annotator-module-background-finder==0.5.21",
	"python-video-annotator-module-find-orientation==0.5.18",
	"python-video-annotator-module-path-editor==0.5.28"
]
# REQUIREMENTS END

setup(
    name='Python video annotator-shaliulab',
    version=version,
    description="""""",
    author=['Ricardo Ribeiro'],
    author_email='ricardojvr@gmail.com',
    url='https://bitbucket.org/fchampalimaud/pythonvideoannotator-models',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages=find_packages(),
    install_requires=[
        'simplejson',
        'pypi-xmlrpc',
        'send2trash',
        'scipy',
        'sklearn',
        'confapp',
    ] + REQUIREMENTS,
    entry_points={
        'console_scripts': [
            'start-video-annotator=pythonvideoannotator.__main__:start',
        ],
    },
    package_data={'pythonvideoannotator': [
        'resources/icons/*.png',
        'resources/themes/default/*.css',
        ]
    },
)
