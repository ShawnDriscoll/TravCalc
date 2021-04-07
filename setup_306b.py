#
# Use 'pyuic4 -x mainwindow_306b.ui -o mainwindow_306b.py' to create a Python file from the
# PyQt4 .ui file.
#
# Use 'pyuic4 -x aboutdialog_306b.ui -o aboutdialog_306b.py' to create a Python file from the
# PyQt4 .ui file.
#
# Use 'pyrcc4 travcalc_306.qrc -o travcalc_306_rc.py' to create a Python resource file
# from the PyQt4 .qrc file (XML file containing paths to PNG app icons and MP3 files).
#
#
# Perform the build process by running 'setup_306b.py'.
#
# If everything works well, you should find a subdirectory named 'dist'
# containing some files, with travcalc306b.exe being amoung them.


from distutils.core import setup
import py2exe
import sys
import glob

sys.argv.append('py2exe')

opts = {'py2exe': {'includes': ['matplotlib.backends',
                                'matplotlib.backends.backend_qt4agg',
                                'matplotlib.figure', 'pylab', 'numpy'],
                                #'matplotlib.backends.backend_tkagg'],
                   'excludes': ['_gtkagg', '_tkagg', '_agg2', 'bsddb', 'curses',
                                'email', 'pywin.debugger', 'pywin.debugger.dbgcon',
                                'pywin.dialogs', '_cairo', '_cocoaagg', '_fltkagg',
                                '_gtk', '_gtkcairo', 'tcl', 'Tkconstants', 'Tkinter'],
                   'packages': [],
                   'dll_excludes': ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll',
                                    'tcl84.dll', 'tk84.dll']
                  }
        }
 
data_files = [(r'mpl-data', glob.glob(r'C:\Python25\Lib\site-packages\matplotlib\mpl-data\*.*')),
                  (r'mpl-data', [r'C:\Python25\Lib\site-packages\matplotlib\mpl-data\matplotlibrc']),
                  (r'mpl-data\images', glob.glob(r'C:\Python25\Lib\site-packages\matplotlib\mpl-data\images\*.*')),
                  (r'mpl-data\fonts', glob.glob(r'C:\Python25\Lib\site-packages\matplotlib\mpl-data\fonts\*.*')),
##                  (r'sounds', [r'sounds\activated.mp3',
##                               r'sounds\running_silent.mp3',
##                               r'sounds\exceptional_failure.mp3',
##                               r'sounds\exceptional_success.mp3',
##                               r'sounds\marginal_failure.mp3',
##                               r'sounds\marginal_success.mp3',
##                               r'sounds\average_failure.mp3',
##                               r'sounds\average_success.mp3',
##                               r'sounds\skill_check.mp3',])
##                  (r'sounds', glob.glob(r'sounds\*.mp3'))
                  (r'phonon_backend', [r'C:\Python25\Lib\site-packages\PyQt4\plugins\phonon_backend\phonon_ds94.dll']),
                  (r'.', [r'C:\windows\system32\MSVCP71.dll']),
                  (r'.', [r'C:\windows\system32\MSVCR71.dll']),
                  (r'.', [r'C:\Python25\MSVCP90.dll']),
                  (r'.', [r'C:\Python25\MSVCR90.dll']),
                  (r'.', [r'sc_icon_16x16.ico']),
                  (r'fonts', [r'fonts\OPTIMA-1.TTF']),
                  (r'fonts', [r'fonts\OPTIMA-2.TTF']),
                  (r'fonts', [r'fonts\OPTIMA-3.TTF']),
                  (r'fonts', [r'fonts\OPTIMA-N.TTF']),
                  (r'docs', [r'ReadMe_306b.txt']),
                  (r'.', [r'travcalc_ref.pdf'])
              ]

setup(
    
# for console program use "console = [{'script': 'travcalc306b.py'}]"
# for windows program use "windows = [{'script': 'travcalc306b.pyw'}]"
      
    console = [{'script': 'travcalc306b.py'}],

    # The first three parameters are not required, if at least a
    # 'version' is given, then a versioninfo resource is built from
    # them and added to the executables.
    version = '3.0.6',
    description = 'Calculator for Mongoose Traveller',
    name = 'TravCalc (Beta)',
    options = opts,
    data_files = data_files,    
)
