#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
#
# generated by wxGlade 0.7.0 on Sat Apr 16 23:14:31 2016
#

# This is an automatically generated file.
# Manual changes will be overwritten without warning!

import warnings
try:
    # as of wxPython v4.0.3 it seems that all is working (few depreciation warnings to be heeded)

    import wxversion

    if wxversion.checkInstalled('2.8'):
        wxversion.select('2.8')
    else:
        warnings.warn("You are running an unsupported Version of wx. Please test this with wx Version 2.8 before reporting errors!")
except ImportError:
    warnings.warn("You either don't have wx installed or you are using wxphoenix. Please test this with wx Version 2.8 before reporting errors!")


import wx
import os
import sys

# ### TODO : feature request : Add international support.

# UNUSED MODULE
import gettext
##    Internationalization and localization support.
##
##    https://docs.python.org/3/library/gettext.html?highlight=gettext#module-gettext
##
##    This module provides internationalization (I18N) and localization (L10N)
##    support for a Python program by providing an interface to the GNU gettext
##    message catalog library. I18N refers to the operation by which a program is
##    made aware of multiple   languages.  L10N refers to the adaptation of your
##    program, once internationalized, to the local language and cultural habits.
##
##    [As far as i can tell, This is automatically inserted by wxGlade code generator
##    and is not used anywhere in this projecy (yet) ]\eZ
# ### TODO : strip _() message functions - this is a job for grep x-d:-)


from LipsyncFrame import LipsyncFrame


class LipsyncApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        try:
            self.SetAssertMode(wx.PYAPP_ASSERT_SUPPRESS)
        except AttributeError:
            self.SetAssertMode(wx.APP_ASSERT_SUPPRESS)
        self.mainFrame = LipsyncFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.mainFrame)
        self.mainFrame.Show()
        return 1

# end of class LipsyncApp


if __name__ == "__main__":

    # UNUSED module gettext
    # Setup for GNU (I18N) and (L10N)
    try:
        gettext.install("papagayo-ng", unicode=True)
    except TypeError:
        gettext.install("papagayo-ng")
    # END OF UNUSED BLOCK

    papagayo = LipsyncApp(0)
    papagayo.mainFrame.TheApp = papagayo
    papagayo.mainFrame.waveformView.TheApp = papagayo
    if len(sys.argv) > 1:
        papagayo.mainFrame.Open(os.path.abspath(sys.argv[1]))
    papagayo.MainLoop()
