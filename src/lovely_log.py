#!/usr/bin/env python
# -*-coding: utf-8 -*-
import wx
import os

from ll_global import *
import ll_menubar
import ll_textwin
import ll_filterwin


class LovelyLogUI(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'lovely log', style=wx.MAXIMIZE |wx.DEFAULT_FRAME_STYLE)

        self.title = "Lovely log"

        self._handlers = list()
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        #---- Menus ----#
        menuBar = ll_menubar.LlMenuBar()
        self.SetMenuBar(menuBar)
        #---- main window ----#
        self.createWindow()

        #---- Actions to take on menu events ----#
        self._handlers.extend([ # File Menu
                                (ID_OPEN, self.OnOpen),
                                (ID_RELOAD, self.OnReload),
                                (ID_LOAD_FILTERS, self.OnLoadFilters),
                                (ID_SAVE_FILTERS, self.OnSaveFilters),
                                (ID_EXIT, self.OnCloseWindow),

                                # Edit Menu
                                (ID_COPY, self.OnCopy),
                                (ID_SELECTALL, self.OnSelectAll),
                                (ID_FONT, self.OnFont),
                                (ID_FIND, self.OnFind),
                                (ID_FIND_PREVIOUS, self.OnFindPrevious),
                                (ID_FIND_NEXT, self.OnFindNext),

                                # About Menu
                                (ID_ABOUT, self.OnAbout)])

        self.bindHandlerForId()

    def createWindow(self):
        self.win = wx.SplitterWindow(self)
        self.textWin = ll_textwin.LlTextWin(self.win)
        self.filterWin = ll_filterwin.LlFilterWin(self.win)
        self.win.SplitHorizontally(self.textWin, self.filterWin)
        self.win.SetSashGravity(0.7)

    def bindHandlerForId(self):
        for tId, handler in self._handlers:
            self.Bind(wx.EVT_MENU, handler, id=tId)

    def DoOpen(self, evt, fname=u'', lunm=-1):
        print ("do open")
        dlg = wx.FileDialog(self, "Open", os.getcwd(),
                            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR)
        print "open dlg"
        if dlg.ShowModal() == wx.ID_OK:
            print "OK"
            self.filename = dlg.GetPath()
            print "Next set title"
            self.SetTitle(self.title + ' -- ' + self.filename)
            print self.filename
        dlg.Destroy()

    def OnOpen(self, event):
        if event.GetId() == ID_OPEN:
            self.DoOpen(event)
        else:
            pass

    def OnReload(self, event): pass
    def OnLoadFilters(self, event): pass
    def OnSaveFilters(self, event): pass

    def OnCopy(self, event): pass
    def OnSelectAll(self, event): pass
    def OnFont(self, event): pass
    def OnFind(self, event): pass
    def OnFindPrevious(self, event): pass
    def OnFindNext(self, event): pass
    def OnAbout(self, event): pass
    def OnCloseWindow(self, event):
        self.Destroy()

# main function
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = LovelyLogUI(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
