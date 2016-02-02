#!/usr/bin/env python
# -*-coding: utf-8 -*-
import wx
import ll_glob
import ll_menubar


class LovelyLogUI(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'lovely log', style=wx.MAXIMIZE |wx.DEFAULT_FRAME_STYLE)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        #---- Menus ----#
        menuBar = ll_menubar.LlMenuBar()
        self.SetMenuBar(menuBar)
        self.createWindow()

    def createWindow(self):
        self.win = wx.SplitterWindow(self)
        self.logPanel = wx.Panel(self.win, style=wx.SUNKEN_BORDER)
        self.logPanel.SetBackgroundColour("white")
        self.filterPanel = wx.Panel(self.win, style=wx.SUNKEN_BORDER)
        self.filterPanel.SetBackgroundColour("white")
        self.win.SplitHorizontally(self.logPanel, self.filterPanel)
        self.win.SetSashGravity(0.7)

    def OnReload(self, event): pass
    def OnLoadFilters(self, event): pass
    def OnSaveFilters(self, event): pass
    def OnFont(self, event): pass
    def OnOpen(self, event): pass
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

