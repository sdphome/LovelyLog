#!/usr/bin/env python
# -*-coding: utf-8 -*-
import wx
import ll_glob

class LlMenuBar(wx.MenuBar):
    def __init__(self, style=0):
        super(LlMenuBar, self).__init__(style)

        self.createFileMenu()
        self.createEditMenu()
        self.createAboutMenu()

    def createFileMenu(self):
        fileMenu = wx.Menu()
        fileMenu.Append(ll_glob.ID_OPEN, "&Open", "Open a log file")
        fileMenu.Append(ll_glob.ID_RELOAD, "&Reload", "Reload the log file")
        fileMenu.AppendSeparator()
        fileMenu.Append(ll_glob.ID_LOAD_FILTERS, "&Load Filters", "Load the filters to filter log")
        fileMenu.Append(ll_glob.ID_SAVE_FILTERS, "&Save Filters", "Save current filters")
        fileMenu.AppendSeparator()
        fileMenu.Append(ll_glob.ID_EXIT, "&Exit", "Exit")
        self.Append(fileMenu, "&File")

    def createEditMenu(self):
        editMenu = wx.Menu()
        editMenu.Append(ll_glob.ID_COPY, "&Copy", "Copy the selected lines")
        editMenu.AppendSeparator()
        editMenu.Append(ll_glob.ID_FONT, "Font", "Change the default font")
        editMenu.AppendSeparator()
        editMenu.Append(ll_glob.ID_FIND, "&Find", "Find")
        editMenu.Append(ll_glob.ID_FIND_PREVIOUS, "Find Previous", "Find previous")
        editMenu.Append(ll_glob.ID_FIND_NEXT, "Find Next", "Find next")
        self.Append(editMenu, "&Edit")

    def createAboutMenu(self):
        aboutMenu = wx.Menu()
        aboutMenu.Append(ll_glob.ID_ABOUT, "&About", "About the software")
        self.Append(aboutMenu, "&About")
