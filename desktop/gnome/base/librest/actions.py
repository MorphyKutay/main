#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    options = "--prefix=/usr \
               -Dgtk_doc=false \
               -Dsoup2=true \
               --sysconfdir=/etc \
              "
               
    if get.buildTYPE() == "_emul32":
        options += " --libdir=/usr/lib32 \
                     --bindir=/_emul32/bin \
                     --sbindir=/_emul32/sbin \
                   "
                     
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        
    mesontools.configure(options)

    #pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    mesontools.build()

def install():
    mesontools.install()
    
    pisitools.dodoc("AUTHORS", "COPYING*", "README*")
