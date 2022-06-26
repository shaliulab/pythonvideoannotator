# !/usr/bin/python2
# -*- coding: utf-8 -*-
SETTINGS_PRIORITY = 10

import os
from pyforms_gui.utils.plugins_finder import PluginsFinder

# LOGGING CONFIGURATION #################################
import logging
APP_LOG_HANDLER_LEVEL      = logging.INFO
APP_LOG_HANDLER_FILE       = 'video-annotator.log'
APP_LOG_HANDLER_FILE_LEVEL = logging.INFO
#########################################################

VIDEO_FILE_PATH = None
CHART_FILE_PATH = None
VIDEOANNOTATOR_PROJECTPATH    = None

USERSTATS_TIMEOUT_DAYS = 30
USERSTATS_APP_ID = 'TPYg57bdaMLFlC8c0XHVjKnvDqSzRJrZoQ'
USERSTATS_URL = "https://stats.cf-sw.org"

#VIDEOANNOTATOR_PROJECTPATH = '/home/ricardo/bitbucket/idtracker-project/session_session0'
#VIDEOANNOTATOR_PROJECTPATH = '/home/ricardo/Downloads/to-delete'

SAVED_GRAPH_FILE_PATH 	= ""
SAVED_BONSAI_FILE_PATH 	= ""

MAIN_WINDOW_GEOMETRY = 0, 50, 1000, 800
#MAIN_WINDOW_GEOMETRY = 1700, 50, 1400, 1000

#VIDEO_FILE_PATH = '/home/ricardo/Downloads/fc2_save_2013-10-29-124117-0001.avi'
#VIDEO_FILE_PATH = 'C:/Users/swp/Downloads/fc2_save_2013-10-29-124117-0001.avi'
#CHART_FILE_PATH = '/home/ricardo/Desktop/01Apollo201403210900/01Apollo201403210900_out.csv', 0, 1

PYFORMS_STYLESHEET 			= os.path.join( os.path.dirname(__file__), 'resources','themes', 'default', 'stylesheet.css')
#PYFORMS_STYLESHEET_LINUX 	= os.path.join('pythonvideoannotator', 'resources','themes', 'default', 'stylesheet_darwin.css')

######################################################################
##### MODULES CONFIG #################################################
######################################################################
MODULES = PluginsFinder()

#VIDEOANNOTATOR_MODULES += 'pythonvideoannotator_module_eventsstats'
MODULES += 'pythonvideoannotator_module_importexport'
MODULES += 'pythonvideoannotator_module_virtualobjectgenerator'
MODULES += 'pythonvideoannotator_module_findorientation'
MODULES += 'pythonvideoannotator_module_motioncounter'
MODULES += 'pythonvideoannotator_module_distances'
MODULES += 'pythonvideoannotator_module_smoothpaths'
MODULES += 'pythonvideoannotator_module_createpaths'
MODULES += 'pythonvideoannotator_module_backgroundfinder'
MODULES += 'pythonvideoannotator_module_contoursimages'
MODULES += 'pythonvideoannotator_module_regionsfilter'
MODULES += 'pythonvideoannotator_module_tracking'
MODULES += 'pythonvideoannotator_module_timeline'
MODULES += 'pythonvideoannotator_module_patheditor'
MODULES += 'pythonvideoannotator_module_pathmap'
MODULES += 'pythonvideoannotator_module_deeplab'
MODULES += 'pythonvideoannotator_module_idtrackerai'



SHORT_KEYS = {

    # TIMELINE
    'Move the end of the selected event to the left.':      'Alt+Shift+Num+Left',
    'Move the end of the selected event to the right.':     'Alt+Shift+Num+Right',
    'Move the begin of the selected event to the left.':    'Ctrl+Alt+Num+Left',
    'Move the begin of the selected event to the right.':   'Ctrl+Alt+Num+Right',
    'Move the selected event to the left.':                 'Alt+Num+Left',
    'Move the selected event to the right.':                'Alt+Num+Right',
    'Move the selected event to the track above.':          'Alt+Num+Up',
    'Move the selected event to the track bellow.':         'Alt+Num+Down',
    'Delete the selected event.':                           'Alt+Del',
    'Open or close a new event.':                           'Alt+C',
    'Lock or unlock the selected event.':                   'Alt+L',
    'Select the first event.':                              'Alt+Q',
    'Select the last event.':                               'Alt+D',
    'Select the next event.':                               'Alt+D',
    'Select the previous event.':                           'Alt+A',

    # PLAYER
    'Play or pause the video.':                             'Ctrl+P',
    'Jumps 1 frame backward.':                              'Ctrl+I',
    'Jumps 1 frame forward.':                               'Ctrl+O',
    'Jumps 20 seconds backward.':                           'Ctrl+K',
    'Jumps 20 seconds forward.':                            'Ctrl+L',
    'Set player speed to 1x.':                              'Ctrl+1',
    'Set player speed to 2x.':                              'Ctrl+2',
    'Set player speed to 3x.':                              'Ctrl+3',
    'Set player speed to 4x.':                              'Ctrl+4',
    'Set player speed to 5x.':                              'Ctrl+5',
    'Set player speed to 6x.':                              'Ctrl+6',
    'Set player speed to 7x.':                              'Ctrl+7',
    'Set player speed to 8x.':                              'Ctrl+8',
    'Set player speed to 9x.':                              'Ctrl+9',
    'Set player speed to 10x.':                              'Alt+1',
    'Set player speed to 20x.':                              'Alt+2',
    'Set player speed to 30x.':                              'Alt+3',
    'Set player speed to 40x.':                              'Alt+4',
    'Set player speed to 50x.':                              'Alt+5',
    'Set player speed to 60x.':                              'Alt+6',
    'Set player speed to 70x.':                              'Alt+7',
    'Set player speed to 80x.':                              'Alt+8',
    'Set player speed to 90x.':                              'Alt+9',
    

    # SPECIAL KEYS
    #'Go to the next event and then click the mark the point button.':           'Ctrl+I',
    #'Select the path of the next object and click the mark the point button.':  'Ctrl+U',
    #'"Click" the Mark Point button in the current Path.':                       'Ctrl++'
}

from AnyQt.QtWidgets import QColorDialog, QFileDialog
PYFORMS_COLORDIALOGS_OPTIONS = QColorDialog.ShowAlphaChannel