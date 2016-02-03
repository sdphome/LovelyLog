#!/usr/bin/env python
import wx
import wx.stc

# Margins
MARK_MARGIN = 0
NUM_MARGIN  = 1
FOLD_MARGIN = 2

class LlStc(wx.stc.StyledTextCtrl):
    def __init__(self, parent, id=wx.ID_ANY,
                 pos=wx.DefaultPosition, size=wx.DefaultSize, style=0):
        super(LlStc, self).__init__(parent, id, pos, size, style)

        self.SetMarginType(MARK_MARGIN, wx.stc.STC_MARGIN_SYMBOL)
        self.SetMarginMask(MARK_MARGIN, ~wx.stc.STC_MASK_FOLDERS)
        self.SetMarginSensitive(MARK_MARGIN, True)
        self.SetMarginWidth(MARK_MARGIN, 16)

        self.SetMarginType(NUM_MARGIN, wx.stc.STC_MARGIN_NUMBER)
        self.SetMarginMask(NUM_MARGIN, 0)

        self.SetMarginType(FOLD_MARGIN, wx.stc.STC_MARGIN_SYMBOL)
        self.SetMarginMask(FOLD_MARGIN, wx.stc.STC_MASK_FOLDERS)
        self.SetMarginSensitive(FOLD_MARGIN, True)

class LlTextWin(wx.PyPanel):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=0, name="TextWindow"):
        super(LlTextWin, self).__init__(parent, id, pos, size, style)
        self.SetBackgroundColour("white")
        self.stc = LlStc(self)
