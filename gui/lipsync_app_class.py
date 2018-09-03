'''Papagayo lipsync module for the Application (wx.App).

USAGE: python.exe papagayo-ng.py [audio.(wav|mp3)|lipsync_project.ppg]

See also:
    \\readme.txt    - for program description.
    \\glp.txt       - for licence information.

'''
import wx
#   wx.App
#   wx.ID_ANY
#   wx.InitAllImageHandlers() ### TODO - shoots sparows with canon. Very bloaty :-(

# BEGIN CUT -------------------------------------------------------------------
###   wx.APP_ASSERT_SUPPRESS
###   wx.PYAPP_ASSERT_SUPPRESS ### TODO - wx.PYAPP... is mistake  should be wx.APP...
# END CUT ---------------------------------------------------------------------

from LipsyncFrame import LipsyncFrame




class LipsyncApp(wx.App):
    '''Derive the application from the wx.App class.

    class wx.App().__init__()
    ARGUMENTS :
    
    __init__(self, 
        redirect=False, 
        filename=None, 
        useBestVisual=False, 
        clearSigInt=True
        )
        Construct a wx.App object.
        
        <boolean>redirect 
            Should sys.stdout and sys.stderr be redirected? Defaults to False. 
            If filename is None then output will be redirected to a window that 
            pops up as needed. (You can control what kind of window is created 
            for the output by resetting the class variable outputWindowClass to 
            a class of your choosing.)
        
        <string>filename 
            The name of a file to redirect output to, if redirect is True.
        
        <boolean>useBestVisual 
            Should the app try to use the best available visual provided by the 
            system (only relevant on systems that have more than one visual.) 
            This parameter must be used instead of calling SetUseBestVisual 
            later on because it must be set before the underlying GUI toolkit 
            is initialized.
            
        <boolean>clearSigInt 
            Enable to catch SIGINT (ie. KeyboardInterruptSignal) This allows 
            the app to terminate upon a Ctrl-C in the console like other GUI 
            apps will by default. Set to False to ignore.

    '''

    def OnInit(self):
        '''Initialise the class: LipsyncApp().'''
        
        ### TODO - this seams bloated. in principle load only the need handlers
        ### TODO - verify handlers  are inited. what this ruturn value ???
        wx.InitAllImageHandlers()
        '''Initializes all available image handlers. This function calls 
        wx.Image.AddHandler() for all the available image handlers 

        The following image handlers are available. BMPHandler is always 
        installed by default. To use other image formats, install the 
        appropriate handler with wx.Image.AddHandler or 
        call wx.InitAllImageHandlers .
        
        wx.BMPHandler: For loading (including alpha support) and saving, always installed.
        wx.PNGHandler: For loading and saving. Includes alpha support.
        wx.JPEGHandler: For loading and saving.
        wx.GIFHandler: For loading and saving (see below).
        wx.PCXHandler: For loading and saving (see below).
        wx.PNMHandler: For loading and saving (see below).
        wx.TIFFHandler: For loading and saving. Includes alpha support.
        wx.TGAHandler: For loading and saving. Includes alpha support.
        wx.IFFHandler: For loading only.
        wx.XPMHandler: For loading and saving.
        ICOHandler: For loading and saving.
        CURHandler: For loading and saving.
        ANIHandler: For loading only.
        
        Calling it is the simplest way to initialize wx.Image but it creates 
        and registers even the handlers your program may not use. 
        If you want to avoid the overhead of doing this you need to 
        call wx.Image.AddHandler manually just for the handlers that 
        you do want to use.'''
        
        # BEGIN CUT -----------------------------------------------------------
        
        # As far as i can tell, this assetion fiddling must have been added 
        # because of pre-release wxphoenix bugs with crossed fingers.
        # Ther are no other ASSERT references in the whole repository.
        ##try:
        ##    self.SetAssertMode(wx.PYAPP_ASSERT_SUPPRESS)  ### TODO ERROR PYAPP_* !? APP_* NO SUCH THING !!!
        ##except AttributeError:
        ##    self.SetAssertMode(wx.APP_ASSERT_SUPPRESS)
        '''
        SetAssertMode(self, AppAssertMode)
        Set the mode indicating how the application responds to assertion 
        statements. Valid settings are a combination of the AppAssertMode 
        enumeration flags that provides the following values :

        wx.APP_ASSERT_SUPPRESS	== 1 
        wx.APP_ASSERT_EXCEPTION	== 2 
        wx.APP_ASSERT_DIALOG	== 4 
        wx.APP_ASSERT_LOG	    == 8

        The default behavior is to raise a wx.wxAssertionError exception.

        PHOENIX MIGRATION : wx.PyAssertionError –> wx.wxAssertionError
        This is the exception raised when one of the wxASSERT (or similar) 
        statements in the wx C++ code fails. Since it is a wxWidgets assertion 
        and not a wxPython assertion the name was changed to make that a little 
        more clear. A compatibility alias exists so using wx.PyAssertionError 
        will still work, but you should migrate those uses 
        to wx.wxAssertionError if possible.
        '''
        # END CUT -------------------------------------------------------------



        # Attach a wx.Frame class to this wx.App.
        self.mainFrame = LipsyncFrame(None, wx.ID_ANY, "")
        
        # Prepare the window of this programs and launch the GUI.
        self.SetTopWindow(self.mainFrame)
        self.mainFrame.Show()
        ##return 1
        return True

        

# END OF CLASS LipsyncApp() ===================================================



# END OF FILE #################################################################