#!/usr/bin/env python

"""
This file is part of qnotero.

qnotero is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

qnotero is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with qnotero.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import glob
import pygaze
from setuptools import setup


def files(path):

	l = [fname for fname in glob.glob(path) if os.path.isfile(fname) \
		and not fname.endswith('.pyc')]
	print(l)
	return l


def data_files():

	"""
	desc:
		The OpenSesame plug-ins are installed as additional data. Under Windows,
		there is no special folder to put these plug-ins in, so we skip this
		step.

	returns:
		desc:	A list of data files to include.
		type:	list
	"""

	return [
		("share/opensesame_plugins/pygaze_init/resources/locale",
			files("opensesame_plugins/pygaze_init/resources/locale/*")),
		("share/opensesame_plugins/pygaze_init",
			files("opensesame_plugins/pygaze_init/*")),
		("share/opensesame_plugins/pygaze_drift_correct",
			files("opensesame_plugins/pygaze_drift_correct/*")),
		("share/opensesame_plugins/pygaze_log",
			files("opensesame_plugins/pygaze_log/*")),
		("share/opensesame_plugins/pygaze_start_recording",
			files("opensesame_plugins/pygaze_start_recording/*")),
		("share/opensesame_plugins/pygaze_stop_recording",
			files("opensesame_plugins/pygaze_stop_recording/*")),
		("share/opensesame_plugins/pygaze_wait",
			files("opensesame_plugins/pygaze_wait/*")),
		("pygaze/resources/fonts",
			files("resources/fonts/*"))
		]

setup(
	name="python-pygaze",
	version=pygaze.__version__,
	description="A Python library for eye tracking",
	author="Edwin Dalmaijer",
	author_email="edwin.dalmaijer@psy.ox.ac.uk",
	url="http://www.pygaze.org/",
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering',
		'Environment :: MacOS X',
		'Environment :: Win32 (MS Windows)',
		'Environment :: X11 Applications',
		'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
		'Programming Language :: Python :: 2',
	],
	include_package_data=False,
	packages = [
		"pygaze",
		"pygaze._display",
		"pygaze._eyetracker",
		"pygaze._joystick",
		"pygaze._keyboard",
		"pygaze._logfile",
		"pygaze._misc",
		"pygaze._mouse",
		"pygaze._screen",
		"pygaze._sound",
		"pygaze._time",
		"pygaze.plugins",
		],
	data_files=data_files()
	)
