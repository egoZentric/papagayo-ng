import wx
#   wx.App
#   wx.InitAllImageHandlers()
#   wx.PYAPP_ASSERT_SUPPRESS
#   wx.APP_ASSERT_SUPPRESS
#   wx.ID_ANY

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
