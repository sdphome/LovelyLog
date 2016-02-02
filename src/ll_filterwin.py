#!/usr/bin/env python
import wx


class LlFilterWin(wx.Panel):
    def __init__(self, parent):
        super(LlFilterWin, self).__init__(parent, style = wx.SUNKEN_BORDER)
        self.SetBackgroundColour("white")
