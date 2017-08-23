import sys
sys.path.append('../lib')
try:
    import xbmc
except ImportError:
    #kodi stubs directory
    sys.path.append(sys.argv[1])
import sublib
import sublib.sub
import sublib.item
import pydocmd
modules = [sublib, sublib.sub, sublib.item]
pages = ["introduction.md", "quickstart.md"]
pydocmd.create(modules, pages, "../README.md")
