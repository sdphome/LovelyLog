#!/usr/bin/env python
# -*-coding: utf-8 -*-
import wx

class LovelyLogUI(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'lovely log', style=wx.MAXIMIZE |wx.DEFAULT_FRAME_STYLE)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.createMenuBar()
        self.createWindow()

    def menuData(self):
        return(("&File",
               ("&Open", "Open in status bar", self.OnOpen),
               ("&Reload", "Reload the text", self.OnReload),
               ("", "", ""),
               ("Load Filters", "Load the filters to filter log", self.OnLoadFilters),
               ("Save Filters", "Save current filters", self.OnSaveFilters),
               ("", "", ""),
               ("&Quit", "Quit", self.OnCloseWindow)),
               ("&Edit",
               ("&Copy", "Copy", self.OnCopy),
               ("", "", ""),
               ("&Font", "setup the font", self.OnFont),
               ("", "", ""),
               ("&Find", "Find", self.OnCopy),
               ("&Find Previous", "Find Previous", self.OnCopy),
               ("&Find Next", "Find Next", self.OnCopy)),
               ("About",
               ("&About", "About this software", self.OnAbout)))

    def createMenuBar(self):
        menuBar = wx.MenuBar()
        for eachMenuData in self.menuData():
            menuLabel = eachMenuData[0]     #menu框的名字
            menuItems = eachMenuData[1:]
            menuBar.Append(self.createMenu(menuItems), menuLabel)
        self.SetMenuBar(menuBar)  #只有调用了SetMenuBar才可以显示menu

    def createMenu(self, menuData):
        menu = wx.Menu()
        for eachLabel, eachStatus, eachHandler in menuData:
            if not eachLabel:
                menu.AppendSeparator()  #给目录下拉框加一条分界线
                continue
            menuItem = menu.Append(-1, eachLabel, eachStatus)  #目录的下拉菜单创建，按照先后顺序
            self.Bind(wx.EVT_MENU, eachHandler, menuItem)  #给目录点击事件绑定一个处理函数
        return menu

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

