# Copyright 2009-2011 Ram Rachum.
# This program is distributed under the LGPL2.1 license.

'''
This module defines the `` class.

See its documentation for more information.
'''

import wx

from garlicsim_wx.widgets.general_misc.cute_button import CuteButton


class CuteBitmapButton(wx.BitmapButton, CuteButton):
    ''' '''
    def __init__(self, parent, id=-1, bitmap=wx.NullBitmap,
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.BU_AUTODRAW, validator=wx.DefaultValidator,
                 name=wx.ButtonNameStr, tool_tip=None, help_text=None):
        
        wx.BitmapButton.__init__(self, parent=parent, id=id, bitmap=bitmap,
                                 pos=pos, size=size, style=style,
                                 validator=validator, name=name)
        
        self.set_tool_tip_and_help_text(tool_tip, help_text)
        