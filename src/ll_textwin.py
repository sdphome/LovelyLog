#!/usr/bin/env python
import wx


class LlTextWin(wx.Panel):
    def __init__(self, parent):
        super(LlTextWin, self).__init__(parent, style=wx.SUNKEN_BORDER)
        self.SetBackgroundColour("white")
