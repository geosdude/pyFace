#!/bin/bash
# -*- codign:utf-8 -*-
# pyface
# Coded by Richard Polk
#----------------------------------------------------
# I am a package directory listed in import statements

import baseTools
from baseTools import *

impLst = ['import Tkinter',
          'from Tkinter import *',
          'from tkSimpleDialog import *',
          'from tkFileDialog import *',
          'from tkMessageBox import *',
          'from baseTools.pickleTools.pickle_Tools import *',
          'from baseTools.commonTools.common_Tools import *',
          'from pyFace.threadTools.thread_Tools import ThreadedClient',
          'from pyFace.guiOutput import GUI_Output',
          'from pyFace.guiTools import GUI_Tools',
          'from pyFace.textWidget import Text_Widget',
          'from pyFace.menuWidget import Menu_Widget',
          'from pyFace.contextMenu import Context_Menu',
          'from pyFace.contextMenu import ct_MenuError',
          ]

for command in impLst:
  try:
    print '  |' + __name__ + '|', command
    exec(command)
  except ImportError:
    message = "ImportError! Failure of --> " + command + " <-- detected!"
    P(message)
print '  |' + __name__ + '| ---'

#P(M(Sk()))

x = baseTools.Stops_Class()                # Create an instance of Stops_Class.
P = x.stop
M = x.modInfo                  # This returns formatted info from the trace stack.


file  = os.path.splitext(os.path.split(__file__)[1])[0]

file_    = sys.argv[0]
debug    = sys.argv[1]
test     = sys.argv[2]
echo     = sys.argv[3]
verbose  = sys.argv[4]

envDct['debug']   = debug
envDct['test']    = test
envDct['echo']    = echo
envDct['verbose'] = verbose
saveState(envDct['envPF'])
#saveDbase(envDct['envPF'], envDct)

def main():
    """
    Module - A python file containing class definitions.
      If ran from main, it may be refered to as a script.

    Class - A template for creating user-defined objects.
      Class definitions normally contain method definitions which operate on instances of the
      class.

    Method - A function which is defined inside a class body.
      If called as an attribute of an instance of that class, the method will get the instance
      object as its first argument (which is usually called self).

    Function - A series of statements which returns some value to a caller.
      It can also be passed zero or more arguments which may be used in the execution of the body.

    """
    print "\nLaunch sequence initialized. T - 10 and counting:\n"
    timestamp = strftime("%d %b %Y %H:%M:%S", localtime())
    print "Main imports on.\n"
    Launch_GUI()


class Widget_Tools:

    def __init__(self):
      #self.echoMthdName('Widget_Tools.__init__')
      self.AttachVarCallbacks()
      if self.modeVar.get() == "CMD":
        pass
      else:
        pass
      #experimental code
      #self.text.bind("KeyPress-F3", self.keyCallback)

    #def radHandler(self, function, args=None):
    #    if self.debugVar.get() > 0:
    #        self.writeLine(str(function), ' ', args)
    #    try:
    #        exec(function)
    #    except StandardError:
    #        message = self.concatNSP(str(function), ' ', args, 'radHandler')
    #        self.writeLine(message)
    #        self.onError('White', 'Red', message)

    def pollErr(self, varName, index, mode):  
      varVal = self.root.globalgetvar(varName)
      self.printTkVar('pollErr', varVal, varName, index, mode)

    def debugPoll(self, varName, index, mode):
      methodName = Mn(Sk())
      varVal = self.root.globalgetvar(varName)
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        self.printTkVar(methodName, varVal, varName, index, mode)
        M(Sk())
      self.envDct['debug'] = varVal
      saveState(self.envDct['envPF'])

    def echoPoll(self, varName, index, mode):
      methodName = Mn(Sk())
      varVal = self.root.globalgetvar(varName)
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        self.printTkVar(methodName, varVal, varName, index, mode)
        M(Sk())
      self.envDct['echo'] = varVal
      saveState(self.envDct['envPF'])
      #self.saveDbase(self.envDct['envPF'], self.envDct)

    def AttachVarCallbacks(self):
      # To trigger a callback when a Tk variable is changed, use trace_variable:
      # traceName            = tkvar.trace_variable(mode, callback)

      #self.txtTracer_W       = self.textVar.trace_variable('w', self.textPoll)
      #self.txtTracer_R       = self.textVar.trace_variable('r', self.textPoll)

      self.debugTracer_W     = self.debugVar.trace_variable('w', self.debugPoll)
      self.echoTracer_W      = self.echoVar.trace_variable('w', self.echoPoll)

      self.errorTracer_W     = self.errVar.trace_variable('w', self.pollErr)
      self.errorTracer_R     = self.errVar.trace_variable('r', self.pollErr)

      #self.funcTracer_W      = self.funcVar.trace_variable('w', self.funcPoll)
      #self.fileTracer_W      = self.curFile.trace_variable('w', self.filePoll)
      #self.scrollTracer_W    = self.scrollVar.trace_variable('w', self.scrollPoll)
      #self.percentTracer_W   = self.percentVar.trace_variable('w', self.percentPoll)
      #
      #self.R_choiceTracer_W  = self.R_choiceVar.trace_variable('w', self.R_choicePoll)
      #self.R_scrollTracer_W  = self.R_scrollVar.trace_variable('w', self.R_scrollPoll)
      #self.R_indexTracer_W   = self.R_indexVar.trace_variable('w', self.R_indexPoll)
      #
      #self.L_choiceTracer_W  = self.L_choiceVar.trace_variable('w', self.L_choicePoll)
      #self.L_scrollTracer_W  = self.L_scrollVar.trace_variable('w', self.L_scrollPoll)
      #self.L_indexTracer_W   = self.L_indexVar.trace_variable('w', self.L_indexPoll)
      #
      #self.slideTracer_W     = self.slideVar.trace_variable('w', self.slidePoll)
      #self.processTracer_W   = self.processVar.trace_variable('w', self.processPoll)



      #self.funcTracer_R      = self.funcVar.trace_variable('r', self.funcPoll)
      #self.fileTracer_R      = self.curFile.trace_variable('r', self.filePoll)
      #self.scrollTracer_R    = self.scrollVar.trace_variable('r', self.scrollPoll)
      #self.percentTracer_R   = self.percentVar.trace_variable('r', self.percentPoll)
      #
      #self.R_choiceTracer_R  = self.R_choiceVar.trace_variable('r', self.R_choicePoll)
      #self.R_scrollTracer_R  = self.R_scrollVar.trace_variable('r', self.R_scrollPoll)
      #
      #self.L_scrollTracer_R  = self.L_scrollVar.trace_variable('r', self.L_scrollPoll)
      #self.L_indexTracer_R   = self.L_indexVar.trace_variable('r', self.L_indexPoll)
      #
      #self.slideTracer_R     = self.slideVar.trace_variable('r', self.slidePoll)
      #self.processTracer_R   = self.processVar.trace_variable('r', self.processPoll)

      self.traceDct = BT.defineDict(['self.txtTracer_W', self.txtTracer_W, 'self.errorTracer_W', self.errorTracer_W,
                                       'self.txtTracer_R', self.txtTracer_R, 'self.errorTracer_R', self.errorTracer_R])

      #self.traceDct = BT.defineDict(['self.txtTracer_W', self.txtTracer_W, 'self.errorTracer_W', self.errorTracer_W,
      #                 'self.funcTracer_W', self.funcTracer_W, 'self.fileTracer_W', self.fileTracer_W,
      #                 'self.locTracer_W', self.locTracer_W, 'self.locTracer_R', self.locTracer_R,
      #                 'self.txtTracer_R', self.txtTracer_R, 'self.errorTracer_R', self.errorTracer_R,
      #                 'self.funcTracer_R', self.funcTracer_R, 'self.fileTracer_R', self.fileTracer_R,
      #                 'self.cmdTracer_R', self.cmdTracer_R, 'self.cmdTracer_W', self.cmdTracer_W,])
      #                 'self.slideTracer_R', self.slideTracer_R, 'self.slideTracer_W', self.slideTracer_W])
      #                 'self.scrollTracer_R', self.scrollTracer_R, 'self.scrollTracer_W', self.scrollTracer_W])


    def printTkVar(self, method, varVal, varName, index, mode):
      #self.writeLine(method, ' ', mode, " callback called with name=%r, index=%r, mode=%r" % (varName, index, mode))
      #self.writeLine("Variable value = %r" % varVal)
      #self.root.setvar(varName, varVal)
      #self.writeLine(method, ' ', varName, " modified by %r callback" % (mode))
      #self.writeLine(self.root.trace_vinfo())

      text = BT.conCat('Change in Tk variable dectected. \nmethod: ', method, '\n','varName: ',varName,'\n','varVal: ',
                     varVal,'\n','index: ',index,'\n','mode: ', mode)
      #self.textVar.set(text)
      self.write(text)

    def resetCounter(self):
      self.cntVar.set(0)
      #self.announce("Count: ", self.cntVar.get())

    def setWidgetID(self, widgetname):
        #print widgetname
        #print self.guiDct['widgetDct']
        command = "self.widgetDct[widgetname] = self." + widgetname + ".winfo_id()"
        exec(command)
    def clearAll(self):
        self.clearText()
        self.resetMessenger()
        self.cmdVar.set('')

    def setWidgetName(self):
      """ parent is container frame containing the click event. """
      widget = ''
      tmpStr = str(self.root.winfo_containing(self.event.x_root, self.event.y_root)).replace('.', ' ')
      #tmpStr = str(self.io_frame.winfo_containing(self.event.x_root, self.event.y_root)).replace('.', ' ')
      tmpLst = tmpStr.split()
      for item in tmpLst:
        if 'frame' in item:
          pass
        else:
          widget = item

      self.setTkVar('widgetVar', widget)  #Superceeds the below code.

      #self.guiDct['widgetVar'] = widget
      #self.widgetVar.set(widget)
      #self.guiDct['curWidget'] = widget

      if self.debugVar.get() == 1:
        #self.blankLine()
        self.writeLine('Current widget according to self.guiDct is: ', self.guiDct['widgetVar'])
        self.writeLine('Current widget according to PyFace instance is: ', self.widgetVar.get())
        self.writeLine('Click Event Code: ', self.eventCode, '\n--DEBUG:  Click occured in widget: ', widget, '\n--DEBUG:  Click occured under mode: ', self.modeVar.get())
        self.writeLine("X Click ", self.event.x, "  ----  ", "Y Click ", self.event.y)
        self.writeLine("X Root ", self.event.x_root, "  ----  ", "Y Root ", self.event.y_root)
        if widget == "r_listbox":
          self.writeLine("Right Start ", self.R_start.get(), "  ----  ", "Stop ", self.R_stop.get(), "  ----  ", "Count ", self.selCnt.get(), '\n')
        elif widget == "l_listbox":
          self.writeLine("\nLeft Start ", self.L_start.get(), "  ----  ", "Stop ", self.L_stop.get(), "  ----  ", "Count ", self.selCnt.get(), '\n')

      return widget

    def callTempWidget(self):
      '''
      Creates a Temporary Text Widget instance.
      '''
      #print "Called Temp_Widget"
      self.TTW = Temp_Widget.__init__(self)

    def setTempFocus(self):
      methodName = Mn(Sk())
      if self.echoThis == methodName or self.echoVar.get() == self.echoLevel:
        self.write(methodName)
#    def setTempFocus(self, *args):
#      print 'args', args, type(args)

#    def setTempFocus(self, farg):
#      print 'farg', farg, type(farg)

#    def setTempFocus(self, **kwargs):
#      self.write('kwargs: ', kwargs, type(kwargs))

      try:
        if isinstance(self.temp_text, InstanceType):
          self.temp_text.focus_set()
      except (AttributeError, TclError):
        pass

    def killTemp(self):
      self.temp_frame.destroy()
      self.TTW = None

    def exit(self):
      self.guiState = 0
      self.root.destroy()

    def closeGui(self, t=0.1):
      '''
      Kill GUI after t seconds.
      '''
      self.guiState = 0
      time.sleep(t)
      self.root.destroy()

class Event_Handlers:
    '''
Instances of this type are generated if one of the following events occurs:

  KeyPress, KeyRelease - for keyboard events
  ButtonPress, ButtonRelease, Motion, Enter, Leave, MouseWheel - for mouse events
  Visibility, Unmap, Map, Expose, FocusIn, FocusOut, Circulate,
  Colormap, Gravity, Reparent, Property, Destroy, Activate,
  Deactivate - for window events.

  If a callback function for one of these events is registered
  using bind, bind_all, bind_class, or tag_bind, the callback is
  called with an Event as first argument. It will have the
  following attributes (in braces are the event types for which
  the attribute is valid):

  serial - serial number of event
  num - mouse button pressed (ButtonPress, ButtonRelease)
  focus - whether the window has the focus (Enter, Leave)
  height - height of the exposed window (Configure, Expose)
  width - width of the exposed window (Configure, Expose)
  keycode - keycode of the pressed key (KeyPress, KeyRelease)
  state - state of the event as a number (ButtonPress, ButtonRelease,
                          Enter, KeyPress, KeyRelease,
                          Leave, Motion)
  state - state as a string (Visibility)
  time - when the event occurred
  x - x-position of the mouse
  y - y-position of the mouse
  x_root - x-position of the mouse on the screen
           (ButtonPress, ButtonRelease, KeyPress, KeyRelease, Motion)
  y_root - y-position of the mouse on the screen
           (ButtonPress, ButtonRelease, KeyPress, KeyRelease, Motion)
  char - pressed character (KeyPress, KeyRelease)
  send_event - see X/Windows documentation
  keysym - keysym of the event as a string (KeyPress, KeyRelease)
  keysym_num - keysym of the event as a number (KeyPress, KeyRelease)
  type - type of the event as a number
  widget - widget in which the event occurred
  delta - delta of wheel movement (MouseWheel)
    '''

    def handleEvent(self, event):
        methodName = Mn(Sk())
        if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
          if self.bypass == 0:
            self.clearText()
          self.write(methodName)
          M(Sk())

        fullWidget = str(event.widget)
        widget = (os.path.splitext(fullWidget)[1]).replace('.', '')
        self.announce(('Focused on: ' + widget), 'black')

        self.event = event   # save event as global

        if str(event.num) == "??":
          if str(event.keysym_num) == "??":
            self.eventCode = str(event.type) + '0'
          else:
            self.eventCode = str(event.keysym_num)
        else:
          self.eventCode = str(event.type) + str(event.num)

        # index(index) -- integer
        # Return the numerical index (0 to size()-1) corresponding to the given index. This is
        # typically ACTIVE, but can also be ANCHOR, or a string having the form "@x,y" where x and
        # y are widget-relative pixel coordinates.

        #sendEvent = event.send_event

        self.eventDct = {"serial":event.serial, "num":event.num, "height":event.height,
                         "width":event.width, "keycode":event.keycode, "state":event.state,
                         "time":event.time, "x":event.x, "y":event.y, "x_root":event.x_root,
                         "y_root":event.y_root, "char":event.char, "keysym":event.keysym,
                         "keysym_num":event.keysym_num, "type":event.type, "widget":widget,
                         "delta":event.delta}

                         #"y_root":event.y_root, "char":event.char, "send_event":event.send_event,

        #self.eventDct["widgetID"] = widgetID
        if self.widgetDct.has_key(widget):
          self.eventDct["widgetID"] = self.widgetDct[widget]
        else:
          self.eventDct["widgetID"] = 000

        self.eventDct["eventCode"]  = self.eventCode
        try:
          self.eventDct["detail"]  = event.detail
        except AttributeError:
          pass # need to code an error log instead of clogging up the GUI with error messages.
          #self.write("AttributeError Encountered!!! Can not add event.detail to event dictionary.'\n'")

        if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
          self.write(echoDict(self.eventDct)[3])
          try:
            self.write("detail      = ", event.detail)
          except StandardError:
            self.write("detail      = ??")
          self.blankLine(1, '-', 100)
          self.blankLine()

        coords = "@"+str(event.x)+","+str(event.y)

        if self.eventDct["widgetID"] == self.widgetDct['cmdLine']:
          self.last_cmd_x = str(event.x)
          self.last_cmd_y = str(event.y)
        else:
          self.last_text_x = str(event.x)
          self.last_text_y = str(event.y)

        if self.eventCode == '80' and self.eventDct["widgetID"] == self.widgetDct['cmdLine']:
          self.cmdCnt = len(self.cmdDct.keys())
          self.announce('cmdCnt:' + str(self.cmdCnt))
          #self.text.focus_force()
          #self.text.focus()
          #self.toggleMode()

        if self.eventCode == '70':
          #self.text.focus_force()
          self.text.focus()
          self.generateTextEvent()
          if self.modeVar.get() == "CMD":
            self.toggleMode()


        if self.eventCode == '43' and self.eventDct["widgetID"] == self.widgetDct['text']:
          # Don't toggle since commands can be typed into the text widget and execuded under
          # the 'CMD' context.
          self.ct_Menu()

        elif self.eventCode == '43' and self.eventDct["widgetID"] == self.widgetDct['cmdLine']:
          self.modeVar.set("CMD")
          #self.ct_Menu() #? Need context menu for this widget

        if self.eventCode == '42' and self.eventDct["widgetID"] == self.widgetDct['text']:
          if self.modeVar.get() == "CMD":
            if self.lastModeVar.get() == "CMD":
              self.setMode("TXT")
            else:
              self.toggleMode()

        elif self.eventCode == '42' and self.eventDct["widgetID"] == self.widgetDct['cmdLine']:
          self.modeVar.set("CMD")

        if self.eventCode == '41' and self.eventDct["widgetID"] == self.widgetDct['text']:
          # Don't toggle since commands can be typed into the text widget and execuded under
          # the 'CMD' context.
          pass
          #if self.modeVar.get() == "CMD":
          #  if self.lastModeVar.get() == "CMD":
          #    self.setMode("TXT")
          #  else:
          #    self.toggleMode()

        elif self.eventCode == '41' and self.eventDct["widgetID"] == self.widgetDct['cmdLine']:
          self.setMode("CMD")

        # Return key
        elif self.eventCode == '65293' and self.eventDct["widgetID"] == self.widgetDct['cmdLine']:
          self.cmdLine.focus_force()
          self.processCommand()

        # Right arrow key
        elif self.eventCode == '65363' and self.eventDct["widgetID"] == self.widgetDct['cmdLine']:
          self.getCmdForward()

        # Left arrow key
        elif self.eventCode == '65361' and self.eventDct["widgetID"] == self.widgetDct['cmdLine']:
          self.getCmdBack()

        # F3 key
        elif self.eventCode == '65472':
          self.findWord()


    def showPosEvent(self, event):
      if self.verbose:
        print 'Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y)

    def showAllEvent(self, event):
      if self.verbose:
        print event
      for attr in dir(event):
          print attr, '=>', getattr(event, attr)

    def onLeftDrag(self, event):
      methodName = Mn(Sk())
      self.text.bind('<KeyRelease-1>', self.onKeyRelease)
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        self.write(methodName)
        print 'Got left mouse button drag:', self.showPosEvent(event)

    def setEvent(self, event):
      self.event = event

    def onKeyPress(self, event):
      self.cmdVar.set('')
      fullWidget = str(event.widget)
      widget = (os.path.splitext(fullWidget)[1]).replace('.', '')

      if self.widgetDct.has_key(widget):
        widgetID = self.widgetDct[widget]
      else:
        widgetID = 000

      self.event = event   # save event as global
      if str(event.num) == "??":
        #self.eventCode = str(event.keycode)
        self.eventCode = str(event.keysym_num)
      else:
        self.eventCode = str(event.type) + str(event.num)

      self.cnt = 0
      self.write('Got event.widget:', widget)# .winfo_id()
      self.write('Got widgetID:', str(widgetID))
      self.write("Got event.num:", event.num)
      self.write("Got event.char:", event.char)
      self.write('Got event.keysym:', event.keysym)
      self.write('Got event.keysym_num:', str(event.keysym_num))
      if self.cnt == 0:
        self.write('Event code is:', self.eventCode)
        self.cnt = self.cnt + 1
      self.blankLine(1, '-', 100)
      self.blankLine()

    def getBoundEvents(self):
      pass
      #self.write(echoDict(self.root.seqDct)[3])



class Command_Widget(Tkinter.Entry):
    def __init__(self):
      self.tmpVar = StringVar()
      self.setTkVar('tmpVar', 'some temp text')

      self.cmdVar = StringVar()
      self.setTkVar('cmdVar', '')

      self.sinVar = IntVar()
      self.setTkVar('sinVar', 0)

      # AttachVarCallbacks to trace vars
      # To trigger a callback when a Tk variable is changed, use trace_variable:
      # traceName            = tkvar.trace_variable(mode, callback)
      self.cmdTracer_W       = self.cmdVar.trace_variable('w', self.cmdPoll_W)
      #self.cmdTracer_R       = self.cmdVar.trace_variable('r', self.cmdPoll_R)

      self.sinTracer_R      = self.sinVar.trace_variable('r', self.sinPoll)
      self.sinTracer_W      = self.sinVar.trace_variable('w', self.sinPoll)

      # Message metrics
      if not 'lower_frame_height' in self.__dict__:
        self.lower_frame_height  = .0375

      frame_height = self.lower_frame_height
      frame_relheight = frame_height * .66
      #print 'frame_relheight = ', frame_relheight
      #frame_relwidth = .70
      frame_relwidth = 1

      if not 'rely' in self.__dict__:
        self.rely = 0

      frame_rely = self.rely

      self.rely = self.rely + frame_relheight

      # sin frame
      widgetname = "sin_frame"
      self.sin_frame = Frame(self.root,
                       name=widgetname,
                       relief=FLAT,
                       bd=self.bd,
                       bg=self.bg)

      self.sin_frame.place(rely=frame_rely,
                           relheight=frame_relheight,
                           relwidth=frame_relwidth - .94)
      self.widgetLst.append(widgetname)

      widgetname = "sinT"
      self.sinToggle = Checkbutton(self.sin_frame,
                                   name=widgetname,
                                   text='Std In',
                                   variable=self.sinVar,
                                   command=self.trigger).pack(anchor='w', side=LEFT)
      self.widgetLst.append(widgetname)

      # cmd frame
      widgetname = "command_frame"
      self.command_frame = Frame(self.root,
                                 name=widgetname,
                                 relief=RIDGE,
                                 bd=self.bd + 2)

      self.command_frame.place(rely=frame_rely,
                               relx=.06,
                               relheight=frame_relheight,
                               relwidth=frame_relwidth - .06,
                               bordermode="outside")

      self.widgetLst.append(widgetname)
      self.setWidgetID(widgetname)

      Tkinter.Entry.__init__(self, self.command_frame)
      sys.stdin = StringIO.StringIO()

      widgetname = "cmdLine"
      self.cmdLine = Entry(self.command_frame,
                            name=widgetname,
                            textvariable = self.cmdVar,
                            justify=LEFT,
                            relief=SUNKEN,
                            bg='white')
      self.widgetLst.append(widgetname)
      self.setWidgetID(widgetname)

      #self.cmdLine.pack(fill=BOTH)
      self.cmdLine.pack(side=BOTTOM, fill=X)

      self.cmdBind()

      if self.modeVar.get() == "CMD":
        self.cmdLine.focus_set()

    #def cmdPoll(self, name, index, mode):
    #  varVal = self.root.globalgetvar(name)
    #  if self.envDct['verbose'] == 1:
    #    self.write('cmdPoll', ': ', varVal, ' ', name, ' ', index, ' ', mode)
    #  #self.setTkVar('cmdVar', self.cmdVar.get())
    #  #command = "self.setTkVar(" + varName + ", " + varVal + ")"
    #  #command = "self.textVar.set(" + command + ")"
    #  #self.callHandler(command)

    def cmdBind(self):

      bindLst = ['<Return>', '<Right>', '<Left>', '<Button-1>', '<Button-2>', '<Button-3>']#, '<Leave>']
      for x in range(len(bindLst)):
        #if x < 3:
          #self.cmdLine.unbind(bindLst[x])
        self.cmdLine.bind(bindLst[x], self.handleEvent)


      #self.cmdLine.bind('<Key>', self.onKeyPress)
      #self.cmdLine.bind('<Return>', self.handleEvent)
      #self.cmdLine.bind('<Up>', self.handleEvent)
      #self.cmdLine.bind('<Down>', self.handleEvent)
      #self.cmdLine.bind('<Button-1>', self.handleEvent)
      #self.cmdLine.bind('<Button-2>', self.handleEvent)
      #self.cmdLine.bind('<Button-3>', self.handleEvent)

    def cmdPoll_R(self, varName, index, mode):
      varValue = self.root.globalgetvar(varName)
      #print "cmdPoll_R called with name=%r, index=%r, mode=%r" % (name, index, mode)
      self.write("cmdPoll_R called with name=%r, index=%r, mode=%r" % (varName, index, mode))
      print "    and variable value = %r" % varValue
      # modify the value, just to show it can be done
      #self.root.globalsetvar(name, varValue + " modified by %r cmdPoll_R" % (mode,))

    def cmdPoll_W(self, varName, index, mode):
      varVal = self.root.globalgetvar(varName)
      #print "cmdPoll_W called with name=%r, index=%r, mode=%r" % (name, index, mode)
      #self.write("cmdPoll_W called with name=%r, index=%r, mode=%r" % (name, index, mode))

      #print "    and variable value = %r" % varValue
      # modify the value, just to show it can be done
      #self.root.globalsetvar(name, varValue + " modified by %r cmdPoll_W" % (mode,))

    def sinPoll(self, varName, index, mode):
      varVal = self.root.globalgetvar(varName)
      if self.envDct['verbose'] == 1:
        self.write('sinPoll', ': ', varVal, ' ', varName, ' ', index, ' ', mode)
      self.setTkVar('sinVar', self.sinVar.get())

    def trigger(self):
      self.write('sinVar returned: ' + str(self.sinVar.get()))

    #def read(self, *size):                      # optional argument
    #    if not size:                            # read N bytes, or all
    #        res, self.text = self.text, ''
    #    else:
    #        res, self.text = self.text[:size[0]], self.text[size[0]:]
    #    return res
    #
    #def readline(self):
    #    eoln = text.find('\n')             # find offset of next eoln
    #    if eoln == -1:                          # slice off through eoln
    #        res, self.text = self.text, ''
    #    else:
    #        res, self.text = self.text[:eoln+1], self.text[eoln+1:]
    #    return res

    def readline(self):
        save = self.reading
        try:
            self.reading = 1
            #self.top.mainloop()  # nested mainloop()
        finally:
            self.reading = save
        line = self.cmdVar.get() #self.text.get("iomark", "end-1c")
        if len(line) == 0:  # may be EOF if we quit our mainloop with Ctrl-C
            line = "\n"
        if isinstance(line, unicode):
            from idlelib import IOBinding
            try:
                line = line.encode(IOBinding.encoding)
            except UnicodeError:
                pass
        self.resetoutput()
        if self.canceled:
            self.canceled = 0
            if not use_subprocess:
                raise KeyboardInterrupt
        if self.endoffile:
            self.endoffile = 0
            line = ""
        return line

    def bindCmdDefaults(self):
      self.unbindCmdKeys()
      bindLst = ['<Return>', '<Right>', '<Left>', '<Button-1>', '<Button-2>', '<Button-3>']  # , '<Leave>'
      for x in range(len(bindLst)):
        self.cmdLine.bind(bindLst[x], self.handleEvent)

    def bindCmdKeys(self):
      self.unbindCmdKeys()
      self.cmdLine.bind('<KeyPress>', self.onKeyPress)
      self.cmdLine.bind('<Alt-KeyPress>', self.onKeyPress)
      self.cmdLine.bind('<Shift-KeyPress>', self.onKeyPress)
      self.cmdLine.bind('<Control-KeyPress>', self.onKeyPress)

    def unbindCmdKeys(self):
      self.cmdLine.unbind('<KeyPress>')
      self.cmdLine.unbind('<Alt-KeyPress>')
      self.cmdLine.unbind('<Shift-KeyPress>')
      self.cmdLine.unbind('<Control-KeyPress>')
      self.cmdLine.unbind('<Return>')
      self.cmdLine.unbind('<Right>')
      self.cmdLine.unbind('<Left>')

    def getCmdBack(self):
      #? run these through a dictionary using a cursor of some sort
      methodName = Mn(Sk())
      if methodName in self.verboseLst:
        Verbose = 1
      else:
        Verbose = 0
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        if self.bypass == 0:
          self.clearText()
        self.write(methodName)
        M(Sk(), verbose=Verbose)

      if self.cmdCnt > 0:
        self.decrement('cmdCnt')
      else:
        #self.decrement('cmdCnt', 1)
        BT.s('cmdCnt', 1)

      if self.cmdDct.has_key(self.cmdCnt):
        #self.generateCmdEvent()
        self.cmdVar.set(self.cmdDct[self.cmdCnt])
        if self.cmdCnt == 1:
          self.announce('You are at the bottom of the command stack.  No older commands can be retrieved.')
        else:
          self.announce('Command ' + str(self.cmdCnt) + ' retrieved.')
      else:
        self.announce('No command retrieved.')

    def getCmdForward(self):
      methodName = Mn(Sk())
      if methodName in self.verboseLst:
        Verbose = 1
      else:
        Verbose = 0
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        if self.bypass == 0:
          self.clearText()
        self.write(methodName)
        M(Sk(), verbose=Verbose)

      if self.cmdCnt < len(self.cmdDct.keys()):
        self.increment('cmdCnt')
      else:
        #self.increment('cmdCnt', len(self.cmdDct.keys()))
        BT.s('cmdCnt', len(self.cmdDct.keys()))

      if self.cmdDct.has_key(self.cmdCnt):
        #self.generateCmdEvent()
        self.cmdVar.set(self.cmdDct[self.cmdCnt])
        if self.cmdCnt == len(self.cmdDct.keys()):
          self.announce('You are at the top of the command stack.  No newer commands can be retrieved.')
        else:
          self.announce('Command ' + str(self.cmdCnt) + ' retrieved.')
      else:
        self.announce('No command retrieved.')

    def generateCmdEvent(self):
      self.cmdLine.focus()
      self.cmdLine.event_generate('<<Button-1>>', x=self.last_cmd_x, y=self.last_cmd_y)
      #print 'Virtual cmd event x, y:', self.last_cmd_x, self.last_cmd_y

    def purgeCommandHistory(self):
      BT.s('cmdDct', dict())

    def recordCommand(self):
      methodName = Mn(Sk())
      cmdNo = len(self.cmdDct.keys()) + 1
      self.cmdDct[cmdNo] = self.cmdVar.get()

      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        self.write(methodName)
        M(Sk())
        self.write('There are ', str(cmdNo), ' commands stored.')
      #saveState(self.guiDct['cmdPF'])
      saveDbase(self.guiDct['cmdPF'], self.cmdDct)

      #command = "self.cmdDct[" + str(cmdNo) + "] = " + self.cmdVar.get()
      #try:
      #  exec(command)
      #except StandardError:
      #  Err(Mn(Sk()), command, sys.exc_info()[2])

    def processCommand(self, *args):
      methodName = Mn(Sk())
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        self.write(methodName)
        M(Sk())
        #self.write("cmdVar is:", self.cmdVar.get())
        #self.write('sinVar', self.sinVar.get())
      self.recordCommand()
      if self.sinVar.get():
        sys.stdin.truncate(0)
        sys.stdin.write(self.cmdVar.get())
      else:
        #? The commonCmdsDct has great potential in setting aliases for common commands
        #? thus making command line entry more user friendly.
        #? Set this up to take args and Kurry it.
        if self.commonCmdsDct.has_key(self.cmdVar.get()):
          exec(self.commonCmdsDct[self.cmdVar.get()])
        else:
          #self.exeVirtualMethod(self.cmdVar.get(), 2)
          #self.ThreadedClient.exeVirtualMethod(fnLst=list(self.cmdVar.get()), bypass=2)
          self.exeVirtualMethod(self.cmdVar.get(), 2)
      #? write method to track commands issued. Similar to how we build self.extLst
      #? prevent user from resetting program variables to different type
      #? place context controls in widget for back, forward, clear, exec

      self.cmdVar.set('')



class Debug_Widget:
    def __init__(self):

      self.button_width = 8

      # Button metrics
      if not 'sub_frame_height' in self.__dict__:
        self.sub_frame_height = .04

      frame_height = self.sub_frame_height
      frame_relheight = frame_height
      self.debug_frame_relwidth = .1

      if not 'rely' in self.__dict__:
        self.rely = 0

      frame_rely = self.rely
      #self.rely = self.rely + frame_relheight  # Dont increment frame height for frame on same
      # y coord.

      # buttons frame
      widgetname = "debug_frame"

      self.debug_frame = Frame(self.root,
                               name=widgetname,
                               relief=FLAT,
                               bd=self.bd,
                               bg=self.bg)

      self.debug_frame.place(rely=frame_rely,
                             relheight=frame_relheight,
                             relwidth=self.debug_frame_relwidth)

      self.widgetLst.append(widgetname)

      widgetname = "debugWdgt"
      #? Use kurry here and set command as arg to callHandler
      self.debugWdgt = Button(self.debug_frame, name=widgetname, command=self.toggleDebug)

      self.widgetLst.append(widgetname)
      if self.debugVar.get() == 0:
          self.debugWdgt.configure(text="Debug Off", background=self.bg)
      elif self.debugVar.get() == 1:
          self.debugWdgt.configure(text="Debug 1", background="red")
      elif self.debugVar.get() == 2:
          self.debugWdgt.configure(text="Debug 2", background="orange")
      elif self.debugVar.get() == 3:
          self.debugWdgt.configure(text="Debug 3", background="yellow")
      elif self.debugVar.get() == 4:
          #self.echoVar.set(1)
          #self.echoWdgt.configure(text="Echo On", background="green")
          self.debugWdgt.configure(text="Debug 4", background="green")
      else:
          self.debugVar.set(0)
          self.debugWdgt.configure(text="Debug Off", background=self.bg)
      self.debugWdgt.configure(width=self.button_width)
      self.debugWdgt.pack(anchor="s", side=BOTTOM)

      #BT.s('debug', self.debug)

      #self.debugVar.set(self.guiDct['debug'])

      """debug values are controled with tkVar after this point."""

      #self.debugWdgt.bind("<Return>", self.statusClick_a)
      #self.configWdgts()

    def toggleDebug(self):
      # These levels should be reversed.
      # It is more logical to have higher level debug with higher mode number.
      if self.debugVar.get() == 0:     # If 0 go to 1.
          self.debugVar.set(1)
          self.debugWdgt.configure(text="Debug 1", background="red")
          #self.announce('Debug level 1. Critical error mode. Oracle list mode is static.')
          BT.s('debug', 1)

      elif self.debugVar.get() == 1:   # If 1 go to 2.
          self.debugVar.set(2)
          self.debugWdgt.configure(text="Debug 2", background="orange")
          #self.announce('Debug level 2. Self echo mode with error checks.  Oracle list mode is static.')
          BT.s('debug', 2)

      elif self.debugVar.get() == 2:   # If 2 go to 3.
          self.debugVar.set(3)
          self.debugWdgt.configure(text="Debug 3", background="yellow")
          #self.announce('Debug level 3. Module echo mode.  Oracle list mode is dynamic.')
          BT.s('debug', 3)

      elif self.debugVar.get() == 3:   # If 3 go to 4.
          self.debugVar.set(4)
          self.debugWdgt.configure(text="Debug 4", background="green")
          BT.s('debug', 4)
          #self.announce('Debug level 4.')
          #self.write(self.debugVar.get())

      elif self.debugVar.get() == 4:   # If 4 go back to 0.
          self.debugVar.set(0)
          self.echoVar.set(1)
          self.debugWdgt.configure(text="Debug Off", background="DarkGray")
          BT.s('debug', 0)

      self.setTkVar('debugVar', self.debugVar.get())
      message = "Debug set to: " + str(self.debugVar.get())
      self.textVar.set(message)


    def setEcho(self, echo=0):
      BT.s('verbose', echo)
      self.setTkVar('echoVar', echo)
      if echo:
        self.write('Echo On')
      else:
        self.write('Echo Off')

    def toggleEcho(self, arg=''):
      if self.verbose:
        self.setTkVar('echoVar', 0)
        self.echoWdgt.configure(text="Echo Off", background="DarkGray")
      else:
        self.setTkVar('echoVar', 1)
        self.echoWdgt.configure(text="Echo On", background="green")
      BT.s('verbose', self.echoVar.get())

    def configWdgts(self):
      if self.verbose == 0:
          self.echoWdgt.configure(text="Echo Off", background="DarkGray")
      elif self.verbose == 1:
          self.echoWdgt.configure(text="Echo On", background="green")
      else:
          self.verbose = 0
          self.echoWdgt.configure(text="Echo Off", background="DarkGray")
      self.echoWdgt.configure(width=self.button_width)  ### (1)
      self.echoWdgt.pack(anchor="s", side=BOTTOM)

class Buttons_Widget:
    def __init__(self):

      self.button_width = 8

      # AttachVarCallbacks to trace vars
      # To trigger a callback when a Tk variable is changed, use trace_variable:
      # traceName            = tkvar.trace_variable(mode, callback)
      self.modeTracer_W      = self.modeVar.trace_variable('w', self.radPoll)

      # buttonfile needs to be passed as an arg.
      # File tools needs to be imported if it is not already there.
      #print 'button file is: ',  self.guiDct['buttonFile']
      #P()
      _buttonLst = BT.getFileAsList(self.guiDct['buttonFile'])[0]
      for x in range(len(_buttonLst)):
        _buttonLst[x] = tuple(string.split(_buttonLst[x].strip(), ','))  # strip return character,
      self.buttonLst = _buttonLst                                        # split into a list and convert it to a tuple

      #changeLst.append("<gui_Tools.Buttons_Widget.__init__. self.modeLst> This should be handled by new picked environment file.)
      self.modeLst = []
      for item in BT.getFileAsList(self.guiDct['modeFile'])[0]:
        self.modeLst.append(tuple(string.split(item, ',')))

      # Button metrics
      if not 'sub_frame_height' in self.__dict__:
        self.sub_frame_height = .04

      frame_height = self.sub_frame_height
      frame_relheight = frame_height
      frame_relwidth = 1 - self.debug_frame_relwidth

      if not 'rely' in self.__dict__:
        self.rely = 0

      frame_rely = self.rely
      self.rely = self.rely + frame_relheight

      frame_relx = self.debug_frame_relwidth

      # buttons frame
      widgetname = "buttons_frame"
      self.buttons_frame = Frame(self.root,
                                 name=widgetname,
                                 relief=FLAT,
                                 bd=self.bd,
                                 bg=self.bg)

      #print 'frame_rely', frame_rely
      #print 'frame_relx', frame_relx
      #print 'frame_relheight', frame_relheight
      #print 'frame_relwidth', frame_relwidth

      self.buttons_frame.place(rely=frame_rely,
                               relx=frame_relx,
                               relheight=frame_relheight,
                               relwidth=frame_relwidth)

      ### Standard radio buttons from dictionary

      self.widgetLst.append(widgetname)
      #self.setWidgetID(widgetname)

      for radName, mode in self.modeLst:
          rad = mode + "Rad"
          widgetname = string.lower(rad)
          self.widgetLst.append(widgetname)
          Radiobutton(self.buttons_frame,
                      name=widgetname,
                      text=radName,
                      variable=self.modeVar,
                      value=radName).pack(anchor='nw', side=RIGHT)
         #self.setWidgetID(widgetname)
      # command binding -- using Kurry  THIS is the cat's meow!!! or the gnat's ass!!!
      #? Mode needs to be a slider
      for item in self.buttonLst:
          if type(item) == TupleType:
              widgetname = string.lower(item[0].replace(' ', '_')) + 'Wdgt'
              if '...' in widgetname:
                  widgetname = widgetname.replace('...', '')
              # item[1] is the function being passed to Kurry
              # The callHandler is breaking when onQuit is called.
              # callHandler writes errors to stdout which is redirected to a tkVar.
              # if onQuit is called, the gui is taken down before the tkVar writes attempted
              # the end result is that no tkVars exist when the write is attempted.
              # solution is to test for the existance of the tkVars in the callHandler.
              # write to them if they are present.
              # cant fix it.  remove quit from docstring
              if item[1] == "self.onQuit()":
                docstring = """ = Button(self.buttons_frame, text=item[0],
name=widgetname, justify=LEFT, command=self.onQuit).pack(anchor="s", side=LEFT)""" + '\n'
              else:
                docstring = """ = Button(self.buttons_frame, text=item[0],
name=widgetname, justify=LEFT, command=Kurry(self.callHandler, item[1])).pack(anchor="s", side=LEFT)""" + '\n'
              command = 'self.' + widgetname + docstring
              exec(command)

#########################################################################################
# End __init__ method ...
#########################################################################################

    def radPoll(self, varName, index, mode):
      methodName = Mn(Sk())
      varVal = self.root.getvar(varName)
      if methodName in self.echoThis or self.echoVar.get() == self.echoLevel:
        self.write(methodName)
        self.write('radPoll', ': ', varVal, ' ', varName, ' ', index, ' ', mode)
        M(Sk())
      # This value will never equal 'CMD'.  Use it for toggle mode testing.
      if varVal != 'CMD':
        self.setTkVar('saveModeVar', varVal)
        message = "Save Mode: " + varVal
        self.announce(message)
      else:
        self.resetMessenger()
      self.setTkVar('modeVar', self.modeVar.get())
      #self.setMode(self.modeVar.get())

    def setFocus(self):
      #Redirect functionality based on mode value.
      self.disabled()
      #self.write('Tk focus is:', self.focus.get())
     #if self.modeVar.get() == "CMD":
     #  self.cmdLine.focus_force()
     #else:
     #  self.text.focus_force()

    def setMode(self, mode=''):
      #Redirect functionality based on mode value.
      #if mode == "CMD":
        #self.setTkVar('lastModeVar', self.saveModeVar.get())
      #else:
        #self.setTkVar('lastModeVar', mode)

      self.setTkVar('lastModeVar', self.modeVar.get())
      message = "Last Mode: " + self.lastModeVar.get() + " Current Mode: " + mode
      if len(mode) > 0:
        self.setTkVar('modeVar', mode)
      else:
        if self.modeVar.get() == "CMD":
          self.cmdLine.focus_force()
        else:
          self.text.focus_force()
        #self.write('Mode set to: ', self.modeVar.get())
      self.announce(message)

    def toggleMode(self):
      self.setMode(self.lastModeVar.get())
      #if self.modeVar.get() == "CMD":
      #  self.setMode(self.saveModeVar.get())
      #else:
      #  self.setMode(self.lastModeVar.get())

class Message_Widget:
    def __init__(self):
      #! Move these to gui_Vars.
      self.messVar  = StringVar()
      self.setTkVar('messVar', 'Test Message.')

      self.bg_colorVar  = StringVar()
      self.fg_colorVar  = StringVar()

      self.setTkVar('fg_colorVar', 'black')
      self.setTkVar('bg_colorVar', 'DarkGray') # 'white'

      self.messLst = []

      # AttachVarCallbacks to trace vars
      # To trigger a callback when a Tk variable is changed, use trace_variable:
      # traceName            = tkvar.trace_variable(mode, callback)

      self.messTracer_W      = self.messVar.trace_variable('w', self.messPoll)

      # Widget metrics
      if not 'lower_frame_height' in self.__dict__:
        self.lower_frame_height  = .0375

      frame_height = self.lower_frame_height * 1.2
      frame_relheight = frame_height
      frame_relwidth = 1

      if not 'rely' in self.__dict__:
        self.rely = 0

      frame_rely = self.rely
      # add this widgets rely to self.rely so the next widget will know where to place.
      self.rely = self.rely + frame_relheight

      # Message frame
      widgetname = "message_frame"
      self.message_frame = Frame(self.root,
                                 name=widgetname,
                                 #bg='yellow',
                                 relief=RIDGE,
                                 bd=self.bd + 2
                                 )

      self.message_frame.place(rely=frame_rely,
                               relheight=frame_relheight,
                               relwidth=frame_relwidth,
                               bordermode="outside")
      self.widgetLst.append(widgetname)

      widgetname = "messenger"
      self.messenger = Label(self.message_frame,
                            name=widgetname,
                            textvariable = self.messVar,
                            #fg=self.fg_colorVar.get(),
                            #bg=self.bg_colorVar.get(),
                            justify=LEFT,
                            anchor=W,
                            relief=SUNKEN)
      self.widgetLst.append(widgetname)

      self.messenger.pack(fill=BOTH)


    def messPoll(self, varName, index, mode):
      varVal = self.root.globalgetvar(varName)
      #self.printTkVar('messPoll', varVal, varName, index, mode)
      #if self.debugVar.get() == 1:
        #self.printTkVar('textPoll', varVal, varName, index, mode)
      #else:
        #self.write(self.textVar.get())

    def resetMessenger(self): #! obsolete.  use announce with no params passed in.
      #time.sleep(2)
      self.setTkVar('fg_colorVar', 'black')
      self.setTkVar('bg_colorVar', 'DarkGray')
      #self.setTkVar('bg_colorVar', 'white')
      self.configMessenger()
      self.messVar.set(' ')
      #self.ct_destroyWindow()

    def testAnnounce(self):
      self.announce('This is a test message.', 'red', 'black')
      #time.sleep(10)
      #self.resetMessenger()
      #

    def announce(self, message='', fg='black', bg='DarkGray'):
      self.setTkVar('fg_colorVar', fg)
      self.setTkVar('bg_colorVar', bg)
      self.configMessenger()
      self.setTkVar('messVar', message)


    def configMessenger(self):
        self.messenger.config(text=self.messVar.get(), bg=self.bg_colorVar.get(),
                              fg=self.fg_colorVar.get(), justify=LEFT, anchor=W)



    #def announce(self, *argLst, **keyDct):
      #Make complient with cmd.py announce method.
      # argLst is a list of characters.
      #argStr = ''
      #for arg in argLst:
      #  argStr = argStr + str(arg)
      #self.messVar.set(argStr)
      #record = self.concatNSP(argLst)
      ##record = self.conCat(argLst)
      #
      ##inStr = record.strip('\n')
      #
      ##self.messLst.append(inStr)
      ##self.write(self.conCatWSP('messLen', len(self.messLst), type(self.messLst)))
      #
      #self.write('messLen ', len(self.messLst), ' ', type(self.messLst))
      #
      #keys = keyDct.keys()
      #keys.sort()
      #for k in keys:
      #  self.write(k, ':', keyDct[k])
      #
      #if 'multi' in keys:
      #  print 'multi: ', keyDct['multi']
      #  duration = 15000 * keyDct['multi']    #30000 msecs = 30 seconds
      #else:
      #  duration = 15000

      #
      ##print args, type(args)  #text colors should be passed in.
      #
      #
      ##file = open(self.guiDct['messFile'], 'w')  # Write messages to history file.
      ##file.write(record)
      ##file.close()
      #
      #inStr = record.strip('\n')  # fixme  Only returns the last item from args.
      #self.messLst.append(inStr)
      #print self.messLst
      ##for message in self.messLst:
      ##  self.messVar.set(message)
      ##  self.configMessenger()
      ##  self.messenger.after(duration, self.resetMessenger)
      #if 'reset' in keys:
      #  print 'reset: ', keyDct['reset']
      #  self.messLst = []

class GUI_Vars:

    def setTkVar(self, key, value=None):
      #? future rename setTkVar with setGuiVar to make ready for wxPython gui roll-in.
      #? Most likely, code a setGuiVar method to switch to this setTkVar or setWxVar method.
      # This builds a function string to set tk vars dynamically from the guiDct and
      # IT ROCKS !!!!!!
      # Each time it is called, the code is altered based on the current value of key at runtime.

      self.guiDct[key] = value
      #saveState(self.guiDct['guiPF']) #This crashes the GUI with a NameError because pickle_Tools dosent have self.guiDct in its namespace.
                                       #I might have to put guiDct into builtins
      saveDbase(self.guiDct['guiPF'], self.guiDct)

      #? code to filter out UnicodeType values from intended StringType
      if isinstance(value, UnicodeType):
        value = str(value)

      if key[-3:] == 'Var':
#print 'Attempting to set Tk variable ' + str(self.""" + key + """) + 'self.""" + key + """' + 'to', value
#print 'Attempting to set Tk variable ', self.""" + key + """, 'self.""" + key + """', 'to', value
        fnStr = \
"""
def setTk(self, value):

    if self.envDct['verbose'] == 1:
      print
      self.write('From setTk ...')
      self.write('Value passed in is <' + str(value) + '> of ' + str(type(value)))
    var = 'self.""" + key + """'
    #command = 'self.""" + key + """.get()'
    if self.envDct['verbose'] == 1:
      self.write('Attempting to set Tk variable <' + str(self.""" + key + """) + ' - self.""" + key + """>' + ' to ' + str(value))
      #print 'Attempting to set Tk variable ', self.""" + key + """, 'self.""" + key + """', 'to', value
    if isinstance(eval(var), InstanceType):
      self.""" + key + """.set(value)
      if self.envDct['verbose'] == 1:
        self.write('Setting Tk variable <' + str(self.""" + key + """) + ' - self.""" + key + """>' + ' to ' + str(value))
        print
        #print 'Setting Tk variable', self.""" + key + """, 'self.""" + key + """', 'to', value
    else:
      if self.envDct['verbose'] == 1:
        print 'Tk variable ', var, 'does not exist. Trying to create it...'
      if isinstance(value, StringType):
        self.""" + key + """ = StringVar()
      elif isinstance(value, IntType):
        self.""" + key + """ = IntVar()

"""
        # define the method/function
        #? handle with handleCall() #! this fails.  nested exec() methods are not allowed.
        # If exec(fnStr) and handleCall use exec(), than a 'nested exec() methods' condition exists.

        # define the virtual method.
        exec(fnStr)
        #this equates to calling the function like this
        #self.setTk(value)
        #set or replace the function in the locals() namespace.
        # call the virtual method setTk.
        f = locals()["setTk"](self, value)
        #It is actually redundant since it is equal to f = locals()["setTk"](self, value)
        #f(self, value)
      else:
        #sys.stdout.write("Variable is not a Tk variable.")
        print "Variable is not a Tk variable."

    def initTkVars(self):
      StringVar = Tkinter.StringVar
      IntVar = Tkinter.IntVar

      if self.test:
        print 'checking for guiDct instance.'
        print isinstance(self.guiDct, bt.DictType)

      for key,value in self.guiDct.iteritems():
        if key[-3:] == 'Var':
          try:
            # need to use guiDct here. The tkVar 'self.verbose' might not be instanciated yet.
            if self.verbose == 1:
              print 'tkVar is:', key, '= ', value, 'of type', type(value)
            #? Need to code a flag to tell this method what the intended datatype the tk var should be.
            if isinstance(value, IntType):
              tkVar = 'self.' + key + ' = IntVar()'
              #tkVal = 'self.' + k + '.set(' + eval(v) + ')'
            elif isinstance(value, StringType):
              tkVar = 'self.' + key + ' = StringVar()'
              #tkVal = 'self.' + k + '.set(' + v + ')'
            #self.write("Executing ", tkVar)
            # For some reason, the sourceVar value is typed as unicode.
            elif isinstance(value, UnicodeType):
              tkVar = 'self.' + key + ' = StringVar()'
            #print 'tkVar =', tkVar
            #P()
            exec(tkVar)
            self.setTkVar(key,value)

          except StandardError:
            pass
      #P()
      self.guiState = 1


    def getTkVars(self, inDct):
      for k,v in inDct.iteritems():
        if k[-3:] == 'Var':
          message = k + " = "
          print message.strip('\n')
          command = 'print self.' + k + '.get()'
          exec(command)

    def writeTkVars(self, inDct):
      pass
      #for k,v in inDct.iteritems():
      #  if k[-3:] == 'Var':
      #    #print k[-3:]
      #    tkVal = 'inDct[' + k + '] = self.' + k + '.get()'
      #    self.callHandler("exec(tkVal)")
      #    #Kurry(tkVal)


        #self.outExtVar.set(self.outExt)
        #self.outPathVar.set(self.outPath)
        #self.kwVar.set(self.kw)
        #self.baseVar.set(self.basedir)
        #self.sourceVar.set(self.source)
        #self.lastSourceVar.set(self.lastSource)
        #
        #self.ct_LockVar.set(self.ctLock)
        ##self.debugVar.set(self.debug)  #set at Debug widget init
        #self.echoVar.set(self.verbose)
        #self.ctRun.set(self.run)
        #self.runFlag.set(self.run)
        #self.cntVar.set(0)
        #self.ct_killVar.set(0)

    def reportTkVars(self):
      for k,v in self.guiDct.iteritems():
        if k[-3:] == 'Var':
          tkVal = 'self.' + k + '.get()'
          Kurry("self.write() ", tkVal)

    def callHandler(self, function, **kwargs):
      """  """
      methodName = Mn(Sk())
      try:
        echo    = methDct[methodName][0]
        verbose = methDct[methodName][1]
        message = methDct[methodName][2]
        option  = methDct[methodName][3]
        kw      = methDct[methodName][4]
      except StandardError:
        isEchoKey(methodName)
        echo    = methDct[methodName][0]
        verbose = methDct[methodName][1]
        message = methDct[methodName][2]
        option  = methDct[methodName][3]
        kw      = methDct[methodName][4]
      if kwargs:
        kw.update(kwargs)
        methDct[methodName][4] = kw
      if echo:
        M(Sk(), offset=20)
      if kw.has_key('cmdLst'):
        for command in kw['cmdLst']:
          exec(command)

      # If the function is an event instance, redirect to the event handler.
      if isinstance(function, InstanceType):
        event = function
        function = 'self.handleEvent(event)'
      # Strip out 'self.' and '() from the passed in function string.
      self.function = function[5:(len(function) - 2)]
      try:
          exec(function)
          self.err_exception = 0
      except StandardError:
          error = 'Error in ' + str(function)
          print error
          import traceback
          print traceback.format_exc()
          sys.exc_clear()
          self.err_exception = 1

      return self.err_exception


    def clearProcLst(self):
      #self.writeLine('Clearing ', self.procLstFile, '...')
      ##self.blankOutFile(self.procLstFile)
      #fileobject = self.fileOpen(self.procLstFile, 'w')
      #fileobject.write(' ')
      #fileobject.close()
      #self.procLst = []
      BT.s('procLst', [])

    def printProcList(self):
      #self.writeLine('procLst has ', str(len(self.procLst)), ' items.')
      for item in self.procLst:
        self.writeLine(item)
      #self.writeLine('procLst has ', str(len(self.procLst)), ' items.')
      self.blankLine()

    def setProcList(self, inLst):
      self.procLst = inLst
      self.procLst.sort()
      # neet to write out values to self.procLstFile


    def eventHandler(self, event, *args, **kwargs):
      """ """
      methodName = Mn(Sk())
      try:
        echo    = methDct[methodName][0]
        verbose = methDct[methodName][1]
        message = methDct[methodName][2]
        option  = methDct[methodName][3]
        kw      = methDct[methodName][4]
      except StandardError:
        isEchoKey(methodName)
        echo    = methDct[methodName][0]
        verbose = methDct[methodName][1]
        message = methDct[methodName][2]
        option  = methDct[methodName][3]
        kw      = methDct[methodName][4]
      if kwargs:
        kw.update(kwargs)
        methDct[methodName][4].update(kwargs)
      if echo:
        if 'clearText' in message:
          self.clearText()
        M(Sk(), verbose=1, offset=22)

      fullWidget = str(event.widget)
      wigLst = (fullWidget.replace('.', ' ')).split()
      widget = wigLst[-1]

      #print 'event is: ' + str(event)
      #print 'fullWidget widget is: ' + fullWidget
      #print 'wigLst is: ' + str(wigLst)
      #print 'widget is: ' + widget
      #print 'event.widget is: ' + str(event.widget)
      # This gui stuff needs to leave.  baseTools isn't supposed to have any gui attributes.
      if not guiDct.has_key('widgetHistLst'):
        self.setVarDctKey(inDct='guiDct', key='widgetHistLst', value=[])

      guiDct['widgetHistLst'].append(widget)

      if len(guiDct['widgetHistLst']) >= 11:
        # drop the oldest one
        del guiDct['widgetHistLst'][0]

      if len(guiDct['widgetHistLst']) >= 3:
        BT.s('lastWidget', guiDct['widgetHistLst'][-2])
        BT.s('curWidget', guiDct['widgetHistLst'][-1])
      else:
        BT.s('lastWidget', '')
        BT.s('curWidget' , '')

      if verbose > 1:
        if args:
          print 'args: ' + str(args)
        if kwargs:
          print 'kwargs: ' + str(kwargs)


      self.event = event   # save event as app instance var #? maybe save the eventDct as global.

      if str(event.num) == "??":
        if str(event.keysym_num) == "??":
          self.eventCode = str(event.type) + '0'
        else:
          self.eventCode = str(event.keysym_num)
      else:
        self.eventCode = str(event.type) + str(event.num)

      #if not guiDct.has_key('e_codeDct'):
        #self.setVarDctKey(inDct='guiDct', key='e_codeDct', value={})



      # index(index) -- integer
      # Return the numerical index (0 to size()-1) corresponding to the given index. This is
      # typically ACTIVE, but can also be ANCHOR, or a string having the form "@x,y" where x and
      # y are widget-relative pixel coordinates.

      #sendEvent = event.send_event

      self.eventDct = {"serial":event.serial, "num":event.num, "height":event.height,
                       "width":event.width, "keycode":event.keycode, "state":event.state,
                       "time":event.time, "x":event.x, "y":event.y, "x_root":event.x_root,
                       "y_root":event.y_root, "char":event.char, "keysym":event.keysym,
                       "keysym_num":event.keysym_num, "type":event.type, "widget":widget,
                       "lastWidget":self.lastWidget, "eventCode":self.eventCode,
                       "event":self.eventCode}
                       #"event":guiDct['e_codeDct'][self.eventCode]}

      #print "guiDct['e_codeDct'][self.eventCode] ", guiDct['e_codeDct'][self.eventCode]

      #span = len(args)
      #if len(args) > 0:
      #  for x in range(span):
      #    keyname = 'arg_' + str(x)
      #    self.eventDct[keyname] = args[x]
      #    print 'args['+str(x)+'] is: ' + str(args[x]) + str(type(args[x]))
      #
      if len(args) > 0:
        for x in range(len(args[0])):
          if x == 0:
            self.eventDct['menu_choice'] = self.quoteStr(args[0][0], 1)
          elif x == 1:
            self.eventDct['ctFlag'] = args[0][1]
          elif x == 2:
            self.eventDct['fn'] = args[0][2]
          elif x == 3:
            self.eventDct['evnt2fnDct'] = self.dictFromList(string.split(args[0][3], ','))

      if len(kw.keys()) > 0:
        for k,v in kw.iteritems():
          self.eventDct[k] = v
      self.eventDct["coords"] = coords = "@"+str(event.x)+","+str(event.y)



class Launch_GUI(GUI_Vars, GUI_Output, GUI_Tools, Widget_Tools, Event_Handlers, \
                 ThreadedClient, Menu_Widget, Command_Widget, Text_Widget, \
                 Debug_Widget, Buttons_Widget, Message_Widget, Context_Menu, \
                 ):

    def __init__(self):
      '''
      This class must be on the bottom of the execution stack.  i.e. end of the file.
      '''
      if envDct['test']:
        print "Status: = TEST SEQUENCE COMPLETE.  ALL SYSTEMS ARE GO."
        pass
      else:
        #if self.getModulo(run): # This is returning 0 after initial run.
        #try:
        print "T time = ", timestamp
        print "\nIgnition.  \nControl passed from main."
        print '\nLift off!\n'
      try:
        #ThreadedClient.__init__(self)
        ThreadedClient.__init__(self, Tk()) # originally, I would pass the Tk instance to ThreadedClient.
   
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
        
        #self.root.iconify()
        
        

        #P(M(Sk()))
        # all the __init__ stuff will have to be moved into gui_Tools which is responsible for actually building the GUI
        self.debug   = envDct['debug']
        self.test    = envDct['test']
        self.echo    = envDct['echo']
        self.verbose = envDct['verbose']
        self.bypass  = envDct['bypass']

        self.expandVars = BT.expandVars
        #self.callHandler = BT.callHandler
        self.envDct = envDct

        #self.envDct = globals()['envDct']
        ##self.guiDct = self.pickleJar("/GeoPy/conf/guiPF")
        ##self.cmdDct = self.pickleJar("C:/GIS/GeoPy/conf/cmdPF") commonCmdsDct
        self.guiDct = pickleJar(self.envDct['guiPF'])
        self.commonCmdsDct = {'exit':"self.exit()", 'quit':"self.closeGui()"}
        self.guiDct['commonCmdsDct'] = self.commonCmdsDct
        #saveState(self.guiDct['commonCmdsPF'])
        saveDbase(self.guiDct['commonCmdsPF'], self.commonCmdsDct) #Obsolete use saveState first
        #pickleJar(self.guiDct['
        self.widgetDct = self.guiDct['widgetDct']
        self.echoThis = self.guiDct['echoThis']
        self.echoLevel = self.guiDct['echoLevel']
        #echoDict(self.guiDct)
        self.cmdDct = pickleJar(self.guiDct['cmdPF'])

        self.initTkVars()

        self.expandVars(self.guiDct)

        # vars such as sub_frame_ht are not being self instanciated.
        self.reading = None
        self.envDct['reading'] = None
        self.guiDct['cmdDct'] = self.cmdDct
        #self.guiDct['buttonFile'] = '/usr/lib/python2.7/dist-packages/pyFace/conf'
        #if self.debug:
        #  lst = self.guiDct.keys()
        #  lst.sort()
        #  for l in lst:
        #    print l
        #  print '******************'
        #  lst = self.envDct.keys()
        #  lst.sort()
        #  for l in lst:
        #    print l

        #self.getTkVars(self.guiDct)

        if sys.platform[:3] != 'win':
          self.FontScale     = 3
        else:
          self.FontScale     = 0

        #self.event = None
        #self.guiDct['event'] = None
        #self.guiDct['widgetLst'] = []
        #self.saveState(self.guiDct['guiPF']) #broken
        self.envDct['guiDct'] = self.guiDct
        # why am I trying to save the guiDct on init.  It is fresh.
        #self.saveDbase(self.guiDct['guiPF'], self.guiDct) #Obsolete use saveState first
        self.sub_frame_height = self.guiDct['sub_frame_height']
        self.rely = self.guiDct['rely']
        self.bd = self.guiDct['bd']
        self.guiDct['bg'] = 'gray85'
        self.bg = self.guiDct['bg']
        self.colors = self.guiDct['colors']
        self.fonts = self.guiDct['fonts']
        self.widgetLst = self.guiDct['widgetLst']
        self.event = self.guiDct['event']  
        #print dir(GUI_Vars)    
        GUI_Output.__init__(self)
        self.verNo = ET.verNo
        self.root.title('PyFace 4.0.1 on <python ' + self.verNo + '>')
        self.root.X_adjust = (self.root.winfo_screenwidth() * .005)
        self.root.Y_adjust = (self.root.winfo_screenheight() -  (self.root.winfo_screenheight() * .9650))
        self.root.X_offset = 0
        self.root.Y_offset = 0
        self.root.width  = self.root.winfo_screenwidth()  - self.root.X_adjust
        self.root.height = self.root.winfo_screenheight() - self.root.Y_adjust
        self.root.geometry('%dx%d+%d+%d'%(self.root.width,self.root.height,self.root.X_offset,self.root.Y_offset))
        self.root.config(bg='black', relief=RIDGE)
        Menu_Widget.__init__(self)
        Command_Widget.__init__(self)
        Text_Widget.__init__(self, 3.75)
        if not self.debug:
          sys.stderr = self        #redirect stderr and stdout to text widget
          sys.stdout = self        #This only works after self defines a write method.
        else:
          sys.stderr = self
          sys.stdout = self
        Debug_Widget.__init__(self)
        Buttons_Widget.__init__(self)
        Message_Widget.__init__(self)

        self.root.mainloop()
      except StandardError:
        Err('Launch_GUI.__init__', None, sys.exc_info()[2])
        sys.stdin = sys.__stdin__
        P(M(Sk()))


if __name__ == '__main__':
  tmpvar = "Some test sentence."
  main()

  '''endfile'''