#!/usr/bin/env python
# -*-coding: utf-8 -*-
import wx
import ll_global
import ll_menubar
import ll_textwin
import ll_filterwin


class LovelyLogUI(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'lovely log', style=wx.MAXIMIZE |wx.DEFAULT_FRAME_STYLE)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        #---- Menus ----#
        menuBar = ll_menubar.LlMenuBar()
        self.SetMenuBar(menuBar)
        #---- main window ----#
        self.createWindow()

    def createWindow(self):
        self.win = wx.SplitterWindow(self)
        self.textWin = ll_textwin.LlTextWin(self.win)
        self.filterWin = ll_filterwin.LlFilterWin(self.win)
        self.win.SplitHorizontally(self.textWin, self.filterWin)
        self.win.SetSashGravity(0.7)

    def OnOpen(self, event): pass
    def OnReload(self, event): pass
    def OnLoadFilters(self, event): pass
    def OnSaveFilters(self, event): pass

    def OnFont(self, event): pass
    def OnCopy(self, event): pass
    def OnAbout(self, event): pass
    def OnCloseWindow(self, event):
        self.Destroy()

# main function
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = LovelyLogUI(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
