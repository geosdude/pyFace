#!/bin/bash
# -*- codign:utf-8 -*-
# pyface.contextMenu.py
# Coded by Richard Polk
#----------------------------------------------------

import tkFont
from Tkinter import *

class Context_Menu:
    # Kurry instance may already be present.  check this.
    """
    Must be instantiated by passing in parent self instance containing the definition of
    self.envDct.
    Instaniate like this: Context_Menu.__init__(self)
    """

    def __init__(self):
      #self.ct_killVar.set(0)

      # replaced with environment dictionary value.  Need to be in gui dictionary
      self.ct_Dct = {}

    def askListItem(self, event, widget=''):
      methodName = Mn(Sk())
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        self.write(methodName)
        M(Sk())

      self.setTkVar('widgetVar', widget)

    def ct_Reload(self):
      methodName = Mn(Sk())
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        self.write(methodName)
        M(Sk())

      if self.debugVar.get() == 1:
        self.writeLine("Running under debug mode: ", self.debugVar.get(), "\n")
        self.writeLine('\nEntering ct_Reload')
        #P("\nct_Reload")
      if self.ct_killVar.get():
        if self.event:
          self.ct_destroyWindow()
          self.handleEvent(self.event)
        else:
          if not self.ctRun.get():
            self.write("Can't reload the context menu without a previous click event.\n")
        self.ctRun.set(0)

    def ct_Scroll(self, function=None):
      methodName = Mn(Sk())
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        self.write(methodName)
        M(Sk())

      self.clearProcLst()
      self.announce(function)
      if isinstance(function, NoneType):
        function = "self.nullFunction"
        self.setProcList(self.ct_Dct.keys())
      else:
        try:
          exec(function)
        except StandardError:
          Err(Mn(Sk()), function, sys.exc_info()[2])

      ## Need to execute a passed function that defines the procLst
      # Menu won't launch if procLst is empty.
      if self.debugVar.get() == 1:
        self.writeLine("Running under debug mode: ", self.debugVar.get(), "\n")
        self.sinVar.set(1)
        P("\nct_Scroll")

      cts_Lst = self.cts_Buttons()
      cts_btnLst = cts_Lst[0]
      cts_maxLen  = cts_Lst[1] # Convert to pixel size

      self.cts_width  = int(round(cts_Lst[3] * 1.20)) + 1 #pixWidth
      self.cts_height = cts_Lst[4] * len(cts_btnLst) + 2  #pixHeight

      # context frame.  Placed during a right click event.
      # Could have used a frame but Toplevel windows have
      # more powerful methods for controlling behavior.
      self.ct_list_frame = Toplevel(self.root,
                                 name="ct_list_frame",
                                 relief=RAISED,
                                 bd=self.bd,
                                 bg=self.bg,
                                 )

      #self.setVar("ctsFlag", self.ct_list_frame.winfo_exists())
      #
      #if self.debugVar.get() == 1:
      #    self.writeLine("Context Flag is: ", BT.getVar(self.guiDct, 'ctsFlag'))
      self.ct_list_frame.geometry('%dx%d+%d+%d'%(self.cts_width,self.ct_height,self.cts_rightBound,self.ct_upperBound))
      self.ct_list_frame.transient()
      self.ct_list_frame.overrideredirect(1)
      self.ct_list_frame.lift()

      self.ct_Listbox = Listbox(self.ct_list_frame,
                                name='ct_Listbox',
                                selectmode=EXTENDED,
                                relief=SUNKEN,
                                font=self.fonts[1],
                                fg='black',
                                bg='white')


      # The entire event pattern is surrounded by angle brackets.
      # Inside the angle brackets are zero or more modifiers, an event type, and
      # an extra piece of information (detail) identifying a particular button or keysym.
      # Any of the fields may be omitted, as long as at least one of type and detail is
      # present. The fields must be separated by white space or dashes.

      # <modifier-modifier-type-detail>
      self.ct_Listbox.bind('<ButtonPress-1>', self.handleEvent)
      self.ct_Listbox.bind('<ButtonRelease-1>', self.handleEvent)
      # The third form of pattern is used to specify a user-defined, named virtual event. It
      # has the following syntax:
      # <<name>>
      # The entire virtual event pattern is surrounded by double angle brackets. Inside the
      # angle brackets is the user-defined name of the virtual event. Modifiers, such as
      # Shift or Control, may not be combined with a virtual event to modify it. Bindings on
      # a virtual event may be created before the virtual event is defined, and if the
      # definition of a virtual event changes dynamically, all windows bound to that virtual
      # event will respond immediately to the new definition.


      #### Create scrollbar objects and assign them to a text object
      widgetname = "listbox_vsb"

      self.ct_listbox_vsb = Scrollbar(self.ct_list_frame, name='listbox_vsb')
      self.widgetLst.append(widgetname)

      #### Pack objects by order of appearence needed
      self.ct_listbox_vsb.pack(side=LEFT, fill=Y)
      self.ct_Listbox.pack(side=TOP, fill=BOTH, expand=YES)

      ### Configure text objects
      self.ct_Listbox.config(yscrollcommand=self.ct_listbox_vsb.set)

      ### Configure scrollbar objects
      self.ct_listbox_vsb.config(command=self.ct_Listbox.yview)

      #self.ct_Listbox.insert(END, "Test_value")
      for item in self.procLst:
         self.ct_Listbox.insert(END, item)

    def ct_Menu(self):
      methodName = Mn(Sk())
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        self.write(methodName)
        M(Sk())

      #self.ct_Buttons returns the list [btnLst, maxLen, maxHeight, pixWidth, pixHeight]
      ct_Lst = self.ct_Buttons()
      #ct_Lst = self.ct_Buttons(self.widgetVar.get(), self.modeVar.get())

      if self.debugVar.get() == 1:
        self.blankLine()
        self.writeLine("Running under debug mode: ", self.debugVar.get(), "\n")
        P("\nct_Menu- process ct_Lst?")

      widgetname = 'ct_'+ string.lower(self.modeVar.get())

      ct_btnLst  = ct_Lst[0]
      if self.debugVar.get() == 1:
        self.writeLine("Running under debug mode: ", self.debugVar.get(), "\n")
        for item in ct_btnLst:
          self.writeLine(item)

      ct_maxLen  = ct_Lst[1]  # Convert to pixel size
      #maxHeight  = ct_Lst[2] # Not used

      self.ct_width   = int(round(ct_Lst[3] * 1.20)) + 2  #pixWidth
      self.cts_width  = 0
      self.ct_height  = ct_Lst[4] * len(ct_btnLst)        #pixHeight
      self.cts_height = 0

      self.ct_lowerExtent  = self.ct_height + self.event.y_root # ct extent vers determine if the menu will be placed
      self.ct_rightExtent  = self.ct_width + self.event.x_root  # out of the extent of the text frame
      self.cts_rightExtent = (self.ct_width + self.cts_width) + self.event.x_root # will use cts_width

      if self.ct_rightExtent > self.root.width:
          self.ct_rightBound  = self.event.x_root - (self.ct_rightExtent - self.root.width)
          self.cts_rightBound = self.ct_rightBound - (self.ct_width)
      else:
          self.ct_rightBound = self.event.x_root
          if self.cts_rightExtent > self.root.width:
            self.cts_rightBound = self.ct_rightBound - (self.ct_width)
          else:
            self.cts_rightBound = self.ct_rightBound + self.ct_width

      if self.ct_lowerExtent > self.root.height:
          self.ct_upperBound = self.event.y_root - (self.ct_lowerExtent - self.root.height)
      else:
          self.ct_upperBound = self.event.y_root

      self.ct_Dct = {'ct_width':self.ct_width, 'ct_height':self.ct_height, 'cts_width':self.cts_width,
                     'cts_height':self.cts_height, 'ct_lowerExtent':self.ct_lowerExtent,
                     'ct_rightExtent':self.ct_rightExtent, 'ct_rightBound':self.ct_rightBound,
                     'ct_upperBound':self.ct_upperBound, 'cts_rightExtent':self.cts_rightExtent,
                     'cts_rightBound':self.cts_rightBound}

      if self.debugVar.get() == 1:
        self.blankLine()
        self.writeLine("Running under debug mode: ", self.debugVar.get(), "\n")
        for key, value in self.ct_Dct.iteritems():
          self.writeLine(key, ' ', value)

      # context frame.  Placed during a right click event.
      # Could have used a frame but Toplevel windows have
      # more powerful methods for controlling behavior.
      #if self.debugVar.get() == 1:
      #  self.blankLine()
      #  P("\nct_Menu-contest_frame")
      widgetname = "context_frame"
      self.context_frame = Toplevel(self.root,
                                    name=widgetname,
                                    relief=RAISED,
                                    bd=self.bd,
                                    bg=self.bg,
                                    )
      self.context_frame.bind('<ButtonRelease-1>', self.handleEvent)

      self.envDct["ctFlag"] = self.context_frame.winfo_exists()

      if self.debugVar.get() == 1:
        self.writeLine("Running under debug mode: ", self.debugVar.get(), "\n")
        self.writeLine("Context Flag is: ", BT.getVar(self.guiDct, 'ctFlag'))
      self.context_frame.geometry('%dx%d+%d+%d'%(self.ct_width,self.ct_height,self.ct_rightBound,self.ct_upperBound))
      self.context_frame.transient()
      self.context_frame.overrideredirect(1)
      #if self.context_frame.state() == "withdrawn":
      #self.context_frame.deiconify()
      self.context_frame.lift()
      self.setTempFocus()
      #code = str(self.event.type) + str(self.event.num)
      if self.eventCode == '43':
      # command binding -- using Kurry    This is WAY cool!!!
          cnt = 0
          for item in ct_btnLst:
              cnt = cnt + 1
              if type(item) == TupleType:
                  widgetname = string.lower(item[0].replace(' ', '_'))
              if '...' in widgetname:
                  widgetname = widgetname.replace('...', '')
              elif '--' in widgetname:
                  widgetname = 'null_' + str(cnt)
              #for args passed to Kurry, item[2] is the function, item[1] is a numeric arg for control of ct_destroyWindow method.
              if 'null_' in widgetname:
                  docstring = """ = Button(self.context_frame, text=item[0],
name=widgetname, font=self.fonts[7], width=ct_maxLen,
anchor="w", relief=FLAT, justify=LEFT, pady=0,
borderwidth=0, command=Kurry(self.ct_ButtonHandler, item[2], item[1])).pack(side=TOP)""" + '\n'  # It is this: borderwidth=0, command=Kurry(self.callHandler, item[2])).pack(side=TOP)
              else:                                                                # or is it this: borderwidth=0, command=Kurry(self.ct_buttonHandler, item[2])).pack(side=TOP)
                  docstring = """ = Button(self.context_frame, text=item[0],
name=widgetname, font=self.fonts[7], width=ct_maxLen,
anchor="w", relief=FLAT, justify=LEFT, pady=0,
borderwidth=0, command=Kurry(self.ct_ButtonHandler, item[2], item[1])).pack(side=TOP)""" + '\n'
              button = 'self.' + widgetname + docstring
              if self.debugVar.get() or self.debug == 1:
                self.writeLine("Running under debug mode: ", self.debugVar.get(), "\n")
                self.writeLine(button)

              exec(button)

      ct_Lst = []
      #self.ct_Dct = {}

    def font_Obj(self, font_Specs):
      methodName = Mn(Sk())
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        self.write(methodName)
        M(Sk())

      font = tkFont.Font(font=font_Specs)
      return font

    def font_Height(self, font_Specs):
      methodName = Mn(Sk())
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        self.write(methodName)
        M(Sk())

      pixHeight = int(round(self.font_Obj(font_Specs).metrics('linespace') * 1.25))
      return pixHeight

    def font_Width(self, inStr, font_Specs):
      methodName = Mn(Sk())
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        self.write(methodName)
        M(Sk())

      pixWidth = self.font_Obj(font_Specs).measure(inStr)
      return pixWidth


    #def ct_getClassTree()

    #def ct_loadFuncAttrs(self, widget):
    def ct_loadFuncAttrs(self):
      methodName = Mn(Sk())
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        self.write(methodName)
        M(Sk())

      """
      Usage example: inDct, pad=0, inMax=0, sort=1, call='loadClassAttributes', sepChar='= '
      """
      self.write(echoDict(self.funDct, pad=0, inMax=0, sort=1, call='loadClassAttributes', sepChar='= ')[4])
      #self.ct_Scroll(widget)
      self.ct_Scroll()

    #def ct_loadMethAttrs(self, widget):
    def ct_loadMethAttrs(self):
      methodName = Mn(Sk())
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        self.write(methodName)
        M(Sk())

      self.write(echoDict(self.boundMetDct, 0, 0, 1, 'ct_loadMethAttrs'))
      #self.ct_Scroll(widget)
      self.ct_Scroll()

    #def ct_loadMapAttrs(self, widget):
    def ct_loadMapAttrs(self):
      methodName = Mn(Sk())
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        self.write(methodName)
        M(Sk())

      self.echoMap(self.mapDct)

    def cts_Buttons(self):
      methodName = Mn(Sk())
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        self.write(methodName)
        M(Sk())

      #if self.debugVar.get() == 1:
      #  self.blankLine()
      #  P("\ncts_Buttons")
      btnLst = self.procLst

      maxLen = 0
      maxHeight = len(btnLst)
      pixWidth  = 0
      pixHeight = int(round(self.font_Height(self.fonts[1]) * 1.05))

      for item in btnLst:
        if len(item) > maxLen:
          maxLen = len(item)
          pixWidth = self.font_Width(item, self.fonts[1]) + 1
        else:
          pass

      maxLen = maxLen + 1

      return(btnLst, maxLen, maxHeight, pixWidth, pixHeight)

    def ct_Lock(self):
      methodName = Mn(Sk())
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        self.write(methodName)
        M(Sk())

      if self.debugVar.get() == 1:
        self.blankLine()
        P("\nct_Lock")
      self.ct_LockVar.set(1)
      self.messVar.set("Context menu locked.")

    def ct_Unlock(self):
      methodName = Mn(Sk())
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        self.write(methodName)
        M(Sk())

      self.ct_LockVar.set(0)
      self.messVar.set("Context menu released.")

    #def ct_Buttons(self, widget, mode):
    def ct_Buttons(self):
      methodName = Mn(Sk())
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        self.write(methodName)
        M(Sk())

      btnLst = []
      tmpLst = []
      ct_textLst = []

      # These are the button getting set.
      #
      #if self.debugVar.get() > 0:
      #    self.announce(widget, ' ', mode)
      # Depends on mode and widget getting the right click event.
      # Turned off.  Only using text widget for now
#     if widget == 'r_listbox':
#         if mode in ('SDO', 'ALL'):
#             tmpLst = [('Describe',                 1, 'self.processSelection("self.describeOratab(")'),
#                       ('Show Columns',             1, 'self.processSelection("self.getColumnNames(")'),
#                       ('Show Records',             1, 'self.processSelection("self.getRecords(")'),
#                       ('Show Ora Metadata',        1, 'self.processSelection("self.getOraMetadata(")'),
#                       ('Show SDO Info',            1, 'self.processSelection("self.show_SDO_Info(")'),
#                       ('Show DIM Info',            1, 'self.processSelection("self.generate_DIM_Info(1")'),
#                       ('Drop SE Anno Cad',         1, 'self.processSelection("self.dropAnnoCadField(")'),
#                       ('Drop Table',               1, 'self.processSelection("self.dropOratab(")'),
#                       ('Copy Table',               1, 'self.processSelection("self.copyOratab(")'),
#                       ('Dump',                     1, 'self.processSelection("self.dumpOratab(")'),
#                       ('SDE Reg',                  1, 'self.SDE_reg_procedure(1)'),
#                       ('List Spatial Index',       1, 'self.printSpatialIndex()'),
#                       ('Add Spatial Index',        1, 'self.addSpatialIndex()'),
#                       ('Drop Spatial Index',       1, 'self.dropSpatialIndex()'),
#                       ('Oracle Export',            1, 'self.oraExport()'),
#                       ('Add Ora Metadata',         1, 'self.addOraMetadata()'),
#                       ('Add Ora Metadata Measure', 1, 'self.addOraMetadataM()'),
#                       ('Drop Ora Metadata',        1, 'self.dropOraMetadata()'),
#                       ]
#
#         elif mode == 'OGR':
#             tmpLst = [('OGR 2 OGR',                1, 'self.processSelection("self.OGR_2_OGR"'),
#                       ('OGR Info',                 1, 'self.processSelection("self.OGR_Info"'),
#                      ]
#
#         elif mode == 'SDE':
#             tmpLst = [('Table Describe Reg',       1, 'self.SDE_table_describe_reg()'),
#                       ('Table Unregister',         1, 'self.SDE_table_unregister()'),
#                       ('Table Delete',             1, 'self.SDE_table_delete()'),
#                       ('Layer Describe Long',      1, 'self.SDE_layer_describe(0)'),
#                       ('Layer Describe',           1, 'self.SDE_layer_describe(1)'),
#                       ('Layer Register',           1, 'self.SDE_layer_register()'),
#                       ('Layer Delete',             1, 'self.SDE_layer_delete()'),
#                       ('Show Ora Metadata',        1, 'self.getOraMetadata()'),
#                       ('Show SDO Info',            1, 'self.processSelection("self.show_SDO_Info(")'),
#                       ('Show DIM Info',            1, 'self.processSelection("self.generate_DIM_Info(1")'),
#                       ('Drop SE Anno Cad',         1, 'self.dropAnnoCadField()'),
#                       ('Drop Table',               1, 'self.dropOratab()'),
#                       ('Copy Table',               1, 'self.copyOratab()'),
#                       ('OGR Info',                 1, 'self.OGR_Info()'),
#                       ('OGR 2 OGR',                1, 'self.OGR_2_OGR()'),
#                       ('List Spatial Index',       1, 'self.printSpatialIndex()'),
#                       ('Add Spatial Index',        1, 'self.addSpatialIndex()'),
#                       ('Drop Spatial Index',       1, 'self.dropSpatialIndex()'),
#                       ('Oracle Export',            1, 'self.oraExport()'),
#                       ('Add Ora Metadata',         1, 'self.addOraMetadata()'),
#                       ('Drop Ora Metadata',        1, 'self.dropOraMetadata()'),
#                       ]
#
#         elif mode == 'GDB':
#             tmpLst = [('Get GDB ID',               1, 'self.SDE_GDB_ObjectClass_ID()'),
#                       ]
#
#         elif mode in ('SELF', 'Self'):
#             tmpLst = [('Reload Module',           1, 'self.reloadModule()'),
#                       ('Read Module',             1, 'self.readModule()'),
#                       ]
#
#         elif mode in ('FILE', 'File', 'file'):  # Set this list to vary depending on file extension.
#             tmpLst = [('Open',                    1, 'self.fastOpen()'),
#                       ('OGR Info',                1, 'self.OGR_Info()'),
#                       ]
#         else:
#             tmpLst = [('Sort List',               1, 'self.disabled()'),
#                       ('Show Stats',              1, 'self.disabled()'),
#                       ('Show Stats',              1, 'self.disabled()'),
#                       ]
#
#         tmpLst.insert(0, ('Remove Selection',       1, 'self.removeRight()'),)
#         tmpLst.insert(0, ('Print Scroll List',      1, 'self.printScrollList()'),)
#         tmpLst.insert(0, ('Scroll 2 Proc List',     1, 'self.scroll_2_procLst("r")'),)
#         tmpLst.insert(0, ('Proc List 2 Stroll',     1, 'self.procLst_2_scroll("r")'),)
#         tmpLst.insert(0, ('Selection to Proc List', 1, 'self.selection_2_procLst("r")'),)
#         tmpLst.insert(0, ('Clear Selection',        1, 'self.clearSelections()'),)
#
#      elif widget == 'l_listbox':
#          if mode == 'File':
#              tmpLst = [('Change Dir',              1, 'self.onNewPath()'),
#                        ('Back',                    1, 'self.goBack()'),
#                        ]
#          elif mode == 'SDO':
#              tmpLst = [('SDO User Index',          1, 'self.getSDO_Index_Info()'),
#                        ]
#          elif mode == 'SDE':
#              tmpLst = [('Get SDE User Tables',     1, 'self.getSDE_Owner_Tabs()'),
#                        ]
#          elif mode == 'GDB':
#              tmpLst = [('User GDB Obj Class Tabs', 1, 'self.get_SDE_GDB_ObjectClasses()'),
#                        ('Kill GDB Orphans',        1, 'self.SDE_GDB_ObjectClass_ID()'),
#                        ('Get SDE Schema Tables',   1, 'self.getSDE_Tabs()'),
#                        ]
#          elif mode == 'Self':
#              tmpLst = [('Get Attribute Value',     1, 'self.getAttributeValue()'),
#                        ('Get Current List',        1, 'self.getCurrentList()'),
#                        ('Get Current Dictionary',  1, 'self.disable()'),
#                        ]
#          else:
#              tmpLst = [('Connect',                 1, 'self.disabled()'),
#                        ]
#          if mode in ('SDO', 'SDE', 'ALL', 'GMD'):
#              tmpLst.insert(0, ('Refresh Tables',             1, 'self.refresh_User_Dictionary(0)'))
#              tmpLst.insert(1, ('Blank Out User Tables',      1, 'self.blankOutUserTables(1)'))
#              tmpLst.insert(2, ('Filter User Tables by List', 1, 'self.filterUserTables()'))
#
#          if mode in ('SDO', 'SDE', 'GMD'):
#              tmpLst.insert(3, ('Filter Tables by Point', 1, 'self.filterByGeometry(1)'))
#              tmpLst.insert(4, ('Filter Tables by Line',  1, 'self.filterByGeometry(2)'))
#              tmpLst.insert(5, ('Filter Tables by Area',  1, 'self.filterByGeometry(3)'))

      maxLen = 0
      maxHeight = len(btnLst)
      pixWidth  = 0
      pixHeight = int(round(self.font_Height(self.fonts[7]) * 1.05))

      if not ('Clear Text', 1, self.clearText) in btnLst:    #Include in all ct menus
        btnLst.append(('Clear Text', 1, 'self.clearText()')) #Append the tuple

      # Return a list from a read config file. This eliminates the need for mode testing
      # because the config file is created based on the current mode.
      # scratchLst = self.callHandler("self.ct_getBtnLst()") # remarked out due to unknown error.
      scratchLst = self.ct_getBtnLst()
      #if self.debugVar.get() == 1:
      #  self.blankLine()
      #  self.write(type(scratchLst), ' ', str(len(scratchLst)))
      #  for item in scratchLst:
      #    self.write(item)
        #P("\nct_Buttons- process scratchLst")

      for thingy in scratchLst:
        BT.s('inLoop', 1)
        thingyLst = string.split(thingy, ',')
        for thing in thingyLst:
          if thing.isdigit():
            thing = int(thing)
        inTup = tuple(thingyLst)
        btnLst.append(inTup)
        if len(inTup[0]) > maxLen:
          maxLen = len(inTup[0])
          pixWidth = self.font_Width(inTup[0], self.fonts[7]) + 12
        else:
          pass

      maxLen = maxLen + 2

      if not ('Cancel', 1, self.ct_destroyWindow) in btnLst:
        btnLst.append(('Cancel', 1, 'self.ct_destroyWindow()'))

      if not ('Quit', 1, self.onQuit) in btnLst:
        btnLst.append(('Quit', 1, 'self.onQuit()'))

      if 0 < self.debugVar.get() < 2:
        for item in btnLst:
          self.writeLine(item)
        self.blankLine()

      return(btnLst, maxLen, maxHeight, pixWidth, pixHeight)

    def ct_getBtnLst(self):
      methodName = Mn(Sk())
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        self.write(methodName)
        M(Sk())
      '''
      This builds the context config file name from the current mode.
      Example: The returned config file for the 'xml' mode would be ct_xmlFile.conf
      '''
      #self.methInfo(self.echoVar.get(), self.messVar.get(), stackLst=S()[0])
      #if self.debugVar.get() == 1:
      #  self.blankLine()
      #  P("\nct_getBtnLst")
      # Need to code in filecheck method.

      #fileName = self.concatNSP('ct_', string.lower(self.modeVar.get()), 'File.conf')
      fileName = BT.conCat('ct_', string.lower(self.modeVar.get()), 'File.conf')
      configFile = BT.setSlash("F", os.path.join(self.guiDct['confPath'], fileName))
      #if self.debugVar.get() == 1:
      #  self.blankLine()
      #message = self.concat('ct_fileName = ', configFile, '\n', 'ct_getBtnLst- checkFileObject Existance = ', str(BT.checkFileObject(configFile)))
      #P(message)
      # Breaking readfile in getFileAsList
      #if BT.checkFileObject(configFile):
      if BT.checkFileObject(configFile):
        btnLst = BT.getFileAsList(configFile)[0]
      #if self.debugVar.get() == 1:
      #  self.blankLine()
      #  print btnLst
      #  P("\nct_getBtnLst- getFileAsList")

        if isinstance(btnLst, NoneType): # Need to restore last known stable state instead of default.
          self.write("NoneType encountered in context button file.  Restoring default context state.")
          self.modeVar.set('LST')
          btnLst = BT.getFileAsList(BT.setSlash("F", os.path.join(self.guiDct['confPath'], 'ct_lstFile.conf')))[0]
        BT.fileWriteList(BT.setSlash("F", os.path.join(self.guiDct['confPath'], 'ct_BackupFile.conf')), btnLst)
      else:
        btnLst = ['*']

      return btnLst


    # Kurry passes ct_ButtonHandler the function string and an arg read on the fly from the
    # the button conf files
    # ct_ButtonHandler passes callHandler the function string but not the Kurried arg.
    # I am already nesting callHandler but can't pass callHandler an arg yet.
    #? Kurry needs to be worked into the callHandler process for nested function passing

    def ct_preHandler(self, event, argument1, argument2, argument3):
      #if self.echoVar.get():
        #M(S()) #self.methInfo(self.echoVar.get(), self.messVar.get(), stackLst=S()[0])
      if self.debugVar.get() == 1:
        self.blankLine()
        self.writeLine("ct_preHandler received event", event)
        #P("\nct_preHandler")
      self.ct_ButtonHandler(argument1, argument2, argument3)

    def ct_ButtonHandler(self, function, *args):     # Similar to self.callHandler in pylister.pyw but specialized
      methodName = Mn(Sk())
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        self.write(methodName)
        M(Sk())

      if self.debugVar.get() == 1:
        self.blankLine()
        #P("\nct_ButtonHandler")
      try:
        self.ct_killVar.set(args[0])
      except IndexError:
        self.ct_killVar.set(0)

      if self.debugVar.get() == 2:
        self.blankLine()
        self.writeLine('ct_ButtonHandler')
        self.writeLine('Function passed is: ', str(function))
        self.writeLine('args are: ', args)
        self.writeLine('of ', type(args))
        self.writeLine('with length of: ', len(args))
        self.writeLine('ctFlag is: ', self.ct_killVar.get())
        self.blankLine()
        # frames are not seen until ct_ButtonHandler is done executing.
        # some sort of block or thread is being set
        # I might need to learn threading processes.
        try:
          self.writeLine('Context frame returned: ', self.context_frame.winfo_exists())
          self.writeLine('Context list frame returned: ', self.ct_list_frame.winfo_exists())
          self.context_frame.focus_set()
        except AttributeError:
          pass
        self.blankLine()

      try:
        print M(Sk())
        print 'Calling function: ', function
        exec(function)
        self.err_exception = 0
      except StandardError:
        import traceback
        #self.errVar.set(sys.stderr.getvalue())
        self.err_exception = 1
        #self.errVar.set(sys.stderr.readlines())
        #self.textVar.set(sys.stderr.getvalue())
        self.write(traceback.format_exc())
        #self.blankLine()
      finally:
        self.ct_destroyWindow()

        if self.widgetVar.get() == 'r_listbox':
            self.clearSelRight()
        elif self.widgetVar.get() == 'l_listbox':
            self.clearSelLeft()
        else:
            pass

        self.resetCounter()

    def ct_ScrollOff(self):
      methodName = Mn(Sk())
      if self.echoThis == methodName or self.echoVar.get() == self.echoLevel:
        self.write(methodName)
      try:
        self.ct_list_frame.unbind('<ButtonRelease-1>')
        self.ct_list_frame.destroy()
      except AttributeError:
        pass

    def ct_destroyWindow(self, widget=None):
      if self.debugVar.get() == 1:
        self.blankLine()
        #P("\nct_destroyWindow")
        self.write(__file__)
        self.write(self.__class__.__name__)
        self.write(S()[0][3])

      # Visibility Methods

      # deiconify(). Display the window. New windows are displayed by default, so you only have to
      # use this method if you have used iconify or withdraw to remove the window from the screen.

      # iconify(). Turn the window into an icon (without destroying it). To redraw the window, use
      # deiconify. Under Windows, the window will show up in the taskbar.
      # When the window has been iconified, the state method returns "iconic".

      # withdraw(). Remove the window from the screen (without destroying it). To redraw the
      # window, use deiconify.
      # When the window has been withdrawn, the state method returns "withdrawn".

      # state(). Returns the current state of self. This is one of the values "normal", "iconic" (see
      # iconify), "withdrawn" (see withdraw) or "icon" (see iconwindow).

      if not self.ct_LockVar.get():
        try:
          if self.ct_killVar.get():
              if 'list' in self.widgetVar.get():
                  command = BT.conCat('self.', self.widgetVar.get(), '.select_clear(0, END)')
                  exec(command)
              try:
                self.context_frame.destroy()
                self.ct_list_frame.destroy()
              except TclError:
                pass
              #self.callHandler('self.activateLeft()')

              #  #print "Houston; This is Tranquility Base. The Eagle has landed."
          else:
              pass
        except AttributeError: pass
      else:
        pass


class ct_MenuError(Exception):
    def __init__(self, value):
      self.value = value
    def __str__(self):
      return repr(self.value)
