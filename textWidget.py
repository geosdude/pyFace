#!/bin/bash
# -*- codign:utf-8 -*-
# pyface.textWidget.Text_Widget
# Coded by Richard Polk
#----------------------------------------------------

from Tkinter import *

class Text_Widget:
    def __init__(self, fNums=0):

      self.txtTracer_W       = self.textVar.trace_variable('w', self.textPoll)
      self.txtTracer_R       = self.textVar.trace_variable('r', self.textPoll)

      self.wrapTracer_W      = self.wrapVar.trace_variable('w', self.wrapPoll)
      #self.wrapTracer_R      = self.wrapVar.trace_variable('r', self.wrapPoll)


      self.selectedText = None

      # Text metrics
      #? need to code a checkvars method.
      if not 'sub_frame_height' in self.__dict__:
        self.sub_frame_height = .04

      frame_height = 1.0 - (self.sub_frame_height * fNums)
      frame_relheight = frame_height
      frame_relwidth = 1

      #print self.__dict__['rely']
      if not 'rely' in self.__dict__:
        self.rely = 0

      frame_rely = self.rely
      # increment for next frame placement.  will place below text frame
      self.rely = self.rely + frame_relheight

      print "text metrics"
      print 'self.sub_frame_height = ', self.sub_frame_height
      print 'frame_height = ', frame_height
      print 'frame_relheight = ', frame_relheight
      print 'frame_relwidth = ', frame_relwidth

      #self.callTempWidget()

      # text metrics
      # self.sub_frame_height =  0.04
      # frame_height =  0.85
      # frame_relheight =  0.85
      # frame_relwidth =  1


      ### text_frame
      widgetname = "text_frame"
      self.setTkVar('widgetVar', widgetname)
      self.text_frame = Frame(self.root,
                              name=widgetname,
                              bg="red",borderwidth=5,
                              relief=RIDGE)
      self.text_frame.place(rely=frame_rely,
                            relheight=frame_height,
                            relwidth=frame_relwidth)
      self.widgetLst.append(widgetname)
      self.setWidgetID(widgetname)

      widgetname = "text"
      self.setTkVar('widgetVar', widgetname)

      #
      #self.text = Text(self.TTW,
      self.text = Text(self.text_frame,
                       bg='beige',
                       name=widgetname,
                       padx=5,
                       wrap='none')
      self.widgetLst.append(widgetname)
      self.setWidgetID(widgetname)

      widgetname = "text_vsb"
      self.setTkVar('widgetVar', widgetname)
      self.text_vsb      = Scrollbar(self.text_frame,   name=widgetname)
      self.widgetLst.append(widgetname)

      widgetname = "text_hsb"
      self.setTkVar('widgetVar', widgetname)
      self.text_hsb      = Scrollbar(self.text_frame,   name=widgetname, orient='horizontal')
      self.widgetLst.append(widgetname)

      self.text_vsb.pack(side=RIGHT, fill=Y)
      self.text_hsb.pack(side=BOTTOM, fill=X)
      self.text.pack(side=TOP, fill=BOTH, expand=YES)

      self.text.config(yscrollcommand=self.text_vsb.set)
      self.text.config(xscrollcommand=self.text_hsb.set)
      self.text.config(font=self.fonts[1], fg=self.colors[12]['bg'], bg="beige")
      self.text.config(wrap='none')

      ### Configure scrollbar objects
      self.text_vsb.config(command=self.text.yview)
      self.text_hsb.config(command=self.text.xview)

      self.textBind()

      if self.modeVar.get() == "TXT":
        self.text.focus_set()

      #print self.text_frame.children   # A dictionary of children to the text_frame.
      #P()

      #self.text.update()

    def textBind(self):
      self.text.bind('<Button-1>',    self.handleEvent)
      self.text.bind('<Button-2>',    self.handleEvent)
      self.text.bind('<Button-3>',    self.handleEvent)
      self.text.bind('<KeyPress-F3>', self.handleEvent)
      #self.text.bind('<Enter>',       self.handleEvent)
      #self.text.bind('<B1-Motion>', self.onLeftDrag)

    #def generateClickEvent(self, widget, x, y):
    #  command = "self." + widget + ".event_generate(" + widget + "," + x + "," + y + ")"
    def generateTextEvent(self):
        self.text.event_generate('<<Button-1>>', x=self.last_text_x, y=self.last_text_y)

    #def executeSelection(self, inStr=""):
    # we are using an instance variable for the input, not passing it in.
    # We are passing in the local mode
    #? consider kw args 2-28-11

    def textPoll(self, varName, index, mode):
      methodName = Mn(Sk())
      varVal = self.root.globalgetvar(varName)
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        if self.bypass == 0:
          self.clearText()
        self.printTkVar(methodName, varVal, varName, index, mode)
        M(Sk())
      #if self.debugVar.get() == 1:
        #self.printTkVar('textPoll', varVal, varName, index, mode)
      #else:
        #self.write(self.textVar.get())

    def wrapPoll(self, varName, index, mode):
      varVal = self.root.globalgetvar(varName)
      methodName = Mn(Sk())
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        if self.bypass == 0:
          self.clearText()
        self.printTkVar(methodName, varVal, varName, index, mode)
        #self.write(methodName, varVal, varName, index, mode)
        M(Sk())
      if varVal == 0:
        self.text.config(wrap='none')
        self.announce("Text wrap is off.")
      else:
        self.text.config(wrap='char')
        self.announce("Text wrap is on.")

    def executeSelection(self, mode=0):
      try:
        self.selectedText = self.text.get(SEL_FIRST, SEL_LAST)
        if self.modeVar.get() == 'TXT':
            #self.start_new_thread("os.startfile(os.path.normpath(self.selectedText))")
            #? need to process this as a path
            os.startfile(os.path.normpath(self.selectedText))
        else:
          if self.commonCmdsDct.has_key(self.selectedText):
            exec(self.commonCmdsDct[self.selectedText])
          else:
            self.exeVirtualMethod(self.selectedText, mode)

      except WindowsError:
        self.write("WindowsError encountered.  Execution failed.")
        # filtered through callHandler methods try except clause.
        #try:
        #  os.startfile(self.selectedText)
        #except:
        #  self.write("Error encountered.  Execution failed.")

    def getSelectedText(self):
      #self.runThread(self.selectText())
      if not self.text.tag_ranges(SEL):
        self.cmdVar.set("Select some text.")
      #if self.selectedText
      #print self.selectedText

    def selectionCallback(self, function): # check for a selected block of text
      if not self.text.tag_ranges(SEL):
        self.text.bell()
        showerror('selectionCallback', 'No text selected')
        self.selectedText = ''
      else:
        try:
          exec(function)
        except TclError:
          self.text.bell()
          showerror('TclError!', 'Exception thrown!')
          return

    def selectText(self):
      self.selectionCallback('self.selectedText = self.text.get(SEL_FIRST, SEL_LAST)')
      self.text.unbind('<ButtonRelease-1>')
      return self.selectedText

    def onCopy(self):
      """Get text selected by mouse,etc and save in cross-app clipboard."""
      if not self.text.tag_ranges(SEL):
          self.text.bell()
          showerror('Lister_Tools', 'No text selected')
      else:
          self.selectedText = self.text.get(SEL_FIRST, SEL_LAST)
          self.text.clipboard_clear()
          self.text.clipboard_append(self.selectedText)

    #def onCopy(self):
    #  # get text selected by mouse,etc
    #  text = self.selectText()
    #  if isinstance(text, StringType):
    #    self.text.clipboard_clear()                               # save in cross-app clipboard
    #    self.text.clipboard_append(text)
    #  else:
    #    showerror('Copy', 'No text copied')

    def onCut(self):
      # save and delete selected text
      self.onCopy()
      self.onDelete()

    def onDelete(self):
      # delete selected text, no save
      self.selectionCallback('self.text.delete(SEL_FIRST, SEL_LAST)')

    def onPaste(self, mode=0):
      try:
        if mode == 0:
          #text = self.selection_get(selection='CLIPBOARD')
          text = self.selectText()
        else:
          text = self.getWinClip()
      except TclError:
        self.text.bell()
        showerror('Paste', 'Nothing to paste.')
        return
      self.text.insert(INSERT, text)                              # add at current insert cursor
      self.text.tag_remove(SEL, '1.0', END)
      self.text.tag_add(SEL, INSERT+'-%dc' % len(text), INSERT)
      self.text.see(INSERT)                                       # select it, so it can be cut

    def onSelectAll(self):
      self.text.tag_add(SEL, '1.0', END+'-1c')                    # select entire text
      self.text.mark_set(INSERT, '1.0')                           # move insert point to top
      self.text.see(INSERT)                                       # scroll to top

    def restoreText(self):
      self.disabled()
      #self.toggleScroll()
      #self.wrapLine(sys.stdout.getvalue()) # Get text from buffer.

    def onGoto(self, inVal=None):
      if not inVal:
        line = self.lastLine or askinteger('Goto', 'Enter line number')
      else:
        line = inVal
      self.lastLine = line
      self.text.update()
      self.text.focus()
      if line is not None:
        maxindex = self.text.index(END+'-1c')
        maxline  = int(string.split(maxindex, '.')[0])
        if line > 0 and line <= maxline:
          self.text.mark_set(INSERT, '%d.0' % line)           # goto line
          self.text.tag_remove(SEL, '1.0', END)               # delete selects
          #self.text.tag_add(SEL, INSERT, 'insert + 1l')       # select line
          self.text.see(INSERT)                               # scroll to line
        else:
          self.text.bell()
          showerror('GeoTools', 'Bad line number')

    def Find(self, lastkey=None):
      key = lastkey or askstring('Find', 'Enter search string')
      self.text.update()
      self.text.focus()
      self.lastfind = key
      if key:
        where = self.text.search(key, INSERT, END)              # don't wrap
        if not where:
          self.text.bell()
          showerror('GeoTools', 'String not found')
        else:
          pastkey = where + '+%dc' % len(key)                 # index past key
          self.text.tag_remove(SEL, '1.0', END)               # remove any sel
          self.text.tag_add(SEL, where, pastkey)              # select key
          self.text.mark_set(INSERT, pastkey)                 # for next find
          self.text.see(where)                                # scroll display

#    def findWord(self, lastkey=None):  use instance var self.lastKey

    def findWord(self, lastKey=None, inStr=None):
      self.initFind = 1
      if self.text.tag_ranges(SEL):
        thisKey = lastKey or askstring('Find', 'Enter search string', initialvalue=self.text.tag_ranges(SEL)) #Borked.
      else:
        thisKey = askstring('Find', 'Enter search string', initialvalue=self.lastKey)  #fixed

      BT.s('lastKey', thisKey)

      self.text.update()
      self.text.focus()

      #if isinstance(inStr, None):
      #  inStr = 'Looking for thisKey: ' + str(thisKey) + '\n'
      #  self.text.insert(INSERT, inStr, FIRST)
      #
      #  self.text.see(INSERT)
      #  self.text.update()
      #  self.text.focus()

      if thisKey:
        where = self.text.search(thisKey, INSERT, END)              # don't wrap
        if not where:
          self.text.bell()
          showerror('GeoTools', 'String not found')
        else:
          pastKey = where + '+%dc' % len(thisKey)                 # index past key
          self.text.tag_remove(SEL, '1.0', END)                   # remove any sel
          self.text.tag_add(SEL, where, pastKey)                  # select key
          self.text.mark_set(INSERT, pastKey)                     # for next find
          self.text.see(where)                                    # scroll display

    def findNextWord(self):
      self.initFind = 0
      self.findWord(self.lastKey)

    def onChange(self):
      new = Toplevel(self)
      Label(new, text='Find text:').grid(row=0, column=0)
      Label(new, text='Change to:').grid(row=1, column=0)
      self.change1 = Entry(new)
      self.change2 = Entry(new)
      self.change1.grid(row=0, column=1, sticky=EW)
      self.change2.grid(row=1, column=1, sticky=EW)
      Button(new, text='Find',
             command=self.onDoFind).grid(row=0, column=2, sticky=EW)
      Button(new, text='Apply',
             command=self.onDoChange).grid(row=1, column=2, sticky=EW)
      new.columnconfigure(1, weight=1)                            # expandable entrys

    def onDoFind(self):
      self.findWord(self.change1.get())                             # Find in change box

    def onDoChange(self):
      if self.text.tag_ranges(SEL):                               # must find first
        self.text.delete(SEL_FIRST, SEL_LAST)                   # Apply in change
        self.text.insert(INSERT, self.change2.get())            # deletes if empty
        self.text.see(INSERT)
        self.findWord(self.change1.get())                         # goto next appear
        self.text.update()                                      # force refresh



#########################################################################################
# GUI text output functions...
#########################################################################################
    def clearText(self):

      # set up switch so clearText is optional.
      self.text.delete('1.0', END)
      self.resetMessenger()
      #os.system('cls') # Toggle this with a widget for more output control

    #class GUI_Output:

    def blankline(self, repeat=1, char='', num=0):
      self.blankLine(repeat=1, char='', num=0)

    def blankLine(self, repeat=1, char='', num=0):
      while repeat > 0:
        chars = char * num
        text = chars + '\n'
        self.text.insert(END, text)
        self.text.mark_set(INSERT, END)
        self.text.see(INSERT)
        self.text.update()
        repeat = repeat - 1

    def close(self):
      pass

    def writeStr(self, *args):
      text = ''
      #try:
      #  if debug == 1:
      #    text = '--DEBUG:  '
      #  else:
      #    text = ''
      #except AttributeError:
      #  if self.debugVar.get() == 1:
      #    text = '--DEBUG:  '
      #  else:
      #    text = ''

          # self.text.config(fg=self.fg_ColorVar.get())
      try:
        if self.guiState:
          text = text + BT.conCat(args).strip() + '\n'
        else:
          text = text + BT.conCat(args) + '\n'

        #self.text.config(wrap='none', fg=self.textColor.get())
        self.text.config(wrap='none')
        self.text.insert(END, text)
        self.text.mark_set(INSERT, END)
        self.text.see(INSERT)
        self.text.update()
      except StandardError:
        Err(Mn(Sk()), text, sys.exc_info())

    def writeStdErr(self):
        self.write(self.stderr.getvalue())

    def writeStdOut(self):
        self.write(self.stdout.getvalue())

    def saveStdOut(self, filename, mode):
        """
            input sent to writeToFile.
            Gets args:
              filename
              text
              mode='w'"""
        self.writeToFile(filename, self.stdout.getvalue(), mode)

    def writeThreadedOutput(self, *args):
        #? need to code new threaded output window so as to not
        #  clog up the main text window.
        self.write(args)

    def writeFileAsStr(self):
        self.write(self.getFileAsString('', 'Pick a python module.', 'py'))
        #self.onGoto(3)

    def done(self):
        self.write('Job complete!')

    def write(self, *args):
        # need to code a flag which indicates wheither a white space or return should
        # be appended to the end of the t_string or not.
        t_string = ''
        for arg in args:
            if not isinstance(arg, StringType):
                if isinstance(arg, IntType):
                    #? This is borked...
                    arg = str(arg)
                elif isinstance(arg, IntType):
                    arg = str(arg)
                elif isinstance(arg, TupleType):
                    for i in range(len(arg)):
                        t_string = t_string + str(arg[i])
                elif isinstance(arg, ListType):
                    for i in range(len(arg)):
                        t_string = t_string + str(arg[i])
                elif isinstance(arg, DictType):
                    for key, value in arg.iteritems():
                        t_string = t_string + key + ' ' + str(value) + '\n'
            else:
                arg = arg.strip() + ' '
                t_string = t_string + arg

        #! exit messages and errors could be written to a pickle file.
        #for k,v in self.text_frame.children.iteritems():
        #  print "k ", k
        #  print "v ", v
        #P()
        try:
          t_string = t_string.strip() + '\n'
          self.text.config(wrap='char')
          self.text.insert(END, t_string)         # move insert point to bottom
          self.text.mark_set(INSERT, END)         # scroll to bottom, insert set
          self.text.see(INSERT)
          self.text.update()                      # force refresh
        #except (AttributeError, NameError, RuntimeError):
        except (StandardError):
          #self.stderr.write(t_string.strip())
          #if sys.stderr.isatty():
          sys.stderr.write(t_string.strip())
        finally:
          pass #print type(t_string.strip())


    #def write(self, farg=0, *args):
    #    # need to code a flag which indicates wheither a white space or return should
    #    # be appended to the end of the t_string or not.
    #    t_string = ''
    #    for arg in args:
    #        if not isinstance(arg, StringType):
    #            if isinstance(arg, IntType):
    #                arg = str(arg)
    #            elif isinstance(arg, IntType):
    #                arg = str(arg)
    #            elif isinstance(arg, TupleType):
    #                for i in range(len(arg)):
    #                    t_string = t_string + str(arg[i])
    #            elif isinstance(arg, ListType):
    #                for i in range(len(arg)):
    #                    t_string = t_string + str(arg[i])
    #            elif isinstance(arg, DictType):
    #                for key, value in arg.iteritems():
    #                    t_string = t_string + key + ' ' + str(value) + '\n'
    #        else:
    #            t_string = t_string + arg
    #    if farg == 0:
    #      t_string = t_string
    #    elif farg == 1:
    #      t_string = " " + t_string
    #    elif farg == 2:
    #      t_string = "\n" + t_string
    #    elif farg == 3:
    #      t_string = t_string + " "
    #    elif farg == 4:
    #      t_string = t_string + "\n"
    #
    #    #self.text.config(wrap='char')
    #    self.text.config(wrap='none')
    #    self.text.insert(END, t_string)         # move insert point to bottom
    #    self.text.mark_set(INSERT, END)         # scroll to bottom, insert set
    #    self.text.see(INSERT)
    #    self.text.update()                      # force refresh

    def writeLine(self, *args):
      #Obsolete.  write performs same function   redirect to write
      self.write(*args)

    def writeLines(self, lines):
      # lines already have '\n'
      # this might break if the text_frame does not exist...example, trying to writeLines after gui is down.
      self.text.config(wrap='none')
      for line in lines:
        self.write(line)

    def wrapLine(self, *args):
      self.wrapVar.set(1)
      if self.debugVar.get() == 1:
          text = '\n--DEBUG:  ' + BT.conCat(args) + '\n'
      else:
          text = BT.conCat(args) + '\n'
      self.wrapVar.set(0)
      self.text.config(wrap=WORD)
      #self.textVar.set(text)
      #self.text.insert(END, text)
      #self.text.mark_set(INSERT, END)
      #self.text.see(INSERT)
      #self.text.update()

    def write_exception(self):
      self.write("Unexpected error:", sys.exc_info()[0])
      raise
