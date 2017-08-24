#!/bin/bash
# -*- codign:utf-8 -*-
# pyface.menuWidget.Menu_Widget
# Coded by Richard Polk
#----------------------------------------------------

from Tkinter import *

class Menu_Widget:

    def __init__(self):
      # Menu metrics
      frame_height = self.sub_frame_height = self.guiDct['sub_frame_height']
      frame_relheight = frame_height
      frame_relwidth = 1
      frame_rely = self.rely = self.guiDct['rely']
      self.rely = self.rely + frame_relheight

      # menu frame
      widgetname = "menu_frame"

      self.menu_frame = Frame(self.root,
                              name=widgetname,
                              relief=FLAT,
                              bd=self.bd,
                              bg=self.bg)

                              # bg='DarkGray')

      self.menu_frame.place(rely=frame_rely,
                            relheight=frame_relheight,
                            relwidth=frame_relwidth)

      #? 2-28-11 these need to be migrated into conf files.
      #? What are the integers for?
      self.menuLst = [
        ('File', 0,
             [('Open...',           0, "self.disabled()"),
              ('Save',              0, "self.disabled()"),
              ('Save As...',        5, "self.disabled()"),
              ('New',               0, "self.disabled()"),
              'separator',
              ('Recent Files List', 0, "self.disabled()"),
              'separator',
              ('Quit...',           0, "self.onQuit(3)"),
              ]
        ),
        ('Edit', 0,
             [('Cut',               0, "self.onCut()"),
              ('Copy',              1, "self.onCopy()"),
              ('Paste',             0, "self.onPaste(0)"),
              'separator',
              ('Delete',            0, "self.onDelete()"),
              ('Select All',        0, "self.onSelectAll()"),
              'separator',
              ('Clear text',        0, "self.clearText()"),
              ('Restore text',      0, "self.disabled()"),
              'separator',
              ('Goto...',           0, "self.onGoto()"),
              ('Find...',           0, "self.findWord()"),
              ('Find Next',         0, "self.findNextWord()"),
              ('Change',            0, "self.onChange()"),
              ]
        ),
        ('Search', 0,
             [('Files by List',                     0, "self.disabled()"),
              ('List all Files',                    0, "self.disabled()"),
              ('File By Extension',                 0, "self.disabled()"),
              ('File By Extension List',            0, "self.disabled()"),
              ('File By Substring',                 0, "self.disabled()"),
              ('File By Substring and Extension',   0, "self.disabled()"),
               'separator',
              ('Tree List',                         0, "self.disabled()"),
              ('Tree List by Substring',            0, "self.disabled()"),
              ]
        ),
        ('List', 0,
             [('Copy Files By List',                0, "self.disabled()"),
              ('Path List',                         0, "self.disabled()"),
              ('Sort List by Index',                0, "self.disabled()"),
               'separator',
              ('List File Dicts',                   0, "self.disabled()"),
               'separator',
              ('Get List Files',                    0, "self.disabled()"),
              ('Get Current List',                  0, "self.disabled()"),
              ]
        ),
        ('GUI', 0,
             [('Font List',          0, "self.disabled()"),
              ('Pick Bg...',         4, "self.disabled()"),
              ('Pick Fg...',         0, "self.disabled()"),
              ('Color List',         0, "self.disabled()"),
               'separator',
              ('Reload GUI',         0, "self.reloadGUI()"),
               'separator',
              ('Update Py Path',     0, "self.disabled()"),
               'separator',
              ('Save User Settings', 0, "self.disabled()"),
               'separator',
              ('Refresh Modules',    0, "self.disabled()"),
              ('Update Idle Tasks',  0, "self.disabled()"),
              'separator',
              ('Preferences',       0, "self.disabled()"),
              ]
        ),
        ('Context', 0,
              [("Lock Context Menu",    0, "self.ct_Lock()"),
              ("Unlock Context Menu",   0, "self.ct_Unlock()"),
              ]
        ),
        ('System', 0,
              [("Register dll's",    1, "self.dllReg()"),
              ("Shut the Hell Up!",  1, "self.stopAnnoyingMe()"),
              ("Shutdown",           1, "self.disabled()"),
              ]
        ),
        ('Report', 0,
             [('Environment',           0, "self.disabled()"),
              ('Variables',             0, "self.disabled()"),
              ('Methods',               0, "self.disabled()"),
              ('Display',               0, "self.disabled()"),
              ('GUI Widgets',           0, "self.disabled()"),
              ('GeoTools',              0, "self.disabled()"),
               'separator',
              ('System Env',            0, "self.disabled()"),
              ('Path Values',           0, "self.disabled()"),
               'separator',
              ('Network',               0, "self.disabled()"),
              ('Mapped Drives',         0, "self.disabled()"),
              ('Process',               0, "self.disabled()"),
               'separator',
              ('Permissions',           0, "self.disabled()"),
               'separator',
              ('Port Usage',            0, "self.disabled()"),
              ('Open Port Scan',        0, "self.disabled()"),
              ('GUI Port Scan',         0, "self.disabled()"),
              ('Ports',                 0, "self.disabled()"),
              'separator',
              ('Software',              0, "self.disabled()"),
              ]
        ),
        ('Input/Output', 0,
             [("Echo On",               0, "self.setEcho(1)"),
              ("Echo Off",              0, "self.setEcho(0)"),
               'separator',
              ('Print StdOut',          0, "self.writeStdOut()"),
              ('Print StdErr',          0, "self.writeStdErr()"),
               'separator',

              ]
        ),
        ('Help', 0,
             [('GeoTools',           0, "self.disabled()"),
              ('Python',             0, "self.pyHelp()"),
              ('ActiveState',        0, "self.pyHelp2()"),
              ('Lundh''s Tk Intro',  0, "self.TkinterHelp(1)"),
              ('NM Tech''s Tk Ref',  0, "self.TkinterHelp(2)"),
               'separator',
              ('About Python',       0, "self.pyVersion()"),
              ]
        ),
        ]

      # Standard pulldown menus from list
      for (menuName, key, items) in self.menuLst:

        widgetname = string.lower(menuName.replace(' ', '_'))
        self.mbutton = Menubutton(self.menu_frame,
                                  name=widgetname,
                                  text=menuName,
                                  font=self.fonts[7],
                                  underline=key)

        self.widgetLst.append(widgetname)
        self.mbutton.pack(side=LEFT)
        widgetname = string.lower(widgetname + "_pulldwn")
        self.pulldown = Menu(self.mbutton, name=widgetname)
        self.widgetLst.append(widgetname)
        for item in items:                   # scan nested items list
          if item == 'separator':            # string: add separator
            self.pulldown.add_separator({})
          elif type(item) == ListType:       # list: disabled item list
            for num in item:
                self.pulldown.entryconfig(num, state=DISABLED)
          elif type(item[2]) != ListType: # Added Curry logic here 2-28-11.
            docstring = """self.pulldown.add_command(label = item[0],
underline = item[1], command=Kurry(self.callHandler, item[2]))""" + '\n'
            command = 'self.' + docstring
            exec(docstring)
          else:
            self.pullover = Menu(menu)
            self.addMenuItems(pullover, item[2])              # sublist:
            self.pulldown.add_cascade(label = item[0],        # make submenu
                                      underline = item[1],    # add cascade
                                      menu      = pullover)

        self.mbutton.config(menu=self.pulldown)

      # wrapVar is polled by wrapPoll
      widgetname = "wrapT"
      self.wrapToggle = Checkbutton(self.menu_frame, 
                                    name=widgetname, 
                                    text='Text Wrap', 
                                    variable=self.wrapVar).pack(anchor='w', side=LEFT)
      self.widgetLst.append(widgetname)
