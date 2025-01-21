#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde6
from pisi.actionsapi import pisitools

def setup():
    kde6.configure()

def build():
    kde6.make()

def install():
    kde6.install()

    pisitools.removeDir("/usr/share/dbus-1")
    pisitools.removeDir("/usr/share/polkit-1")

    pisitools.dodoc("README.md")
