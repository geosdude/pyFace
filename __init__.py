#!/bin/bash
# -*- codign:utf-8 -*-
# pyface.__init__
# Coded by Richard Polk
#----------------------------------------------------
# I am a package directory listed in import statements

import baseTools
from baseTools import *
#from Tkinter import *

impLst = ['import Tkinter',
          'from baseTools.pickleTools.pickle_Tools import *',
          'from baseTools.commonTools.common_Tools import *',
          'from baseTools.threadTools.thread_Tools import ThreadedClient',
          'from tkSimpleDialog import *',
          'from tkFileDialog import *',
          'from tkMessageBox import *',
          'import tkFont',
          ]

for command in impLst:
  try:
    print '  |' + __name__ + '|', command
    exec(command)
  except ImportError:
    message = "ImportError! Failure of --> " + command + " <-- detected!"
    P(message)
print '  |' + __name__ + '| ---'


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

class TST_Class2():
    def __init__(self, instr):
      print "Inside TST_Class2"
      self.instr2 = instr


class TST_Class(TST_Class2):
    def __init__(self, instr):
      print "Inside TST_Class"
      print instr
      TST_Class2.__init__(self, instr)
      print self.instr2 + "2"


class GUI_Vars():
    def __init__(self):
        #P(M(Sk()))
        # all the __init__ stuff will have to be moved into gui_Tools which is responsible for actually building the GUI
        self.debug   = envDct['debug']
        self.test    = envDct['test']
        self.echo    = envDct['echo']
        self.verbose = envDct['verbose']
        self.bypass  = envDct['bypass']



        self.expandVars = BT.expandVars
        self.callHandler = BT.callHandler
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
        #self.guiDct['bg'] = 'gray54'
        self.bg = self.guiDct['bg']
        self.colors = self.guiDct['colors']
        self.fonts = self.guiDct['fonts']
        self.widgetLst = self.guiDct['widgetLst']
        self.event = self.guiDct['event']
        #self.guiDct['windowsColorsLst'] = ['SystemButtonFace', 'SystemButtonText', 'SystemDisabledText', 'SystemHighlight', 'SystemHightlightText',
                                           #'SystemMenu', 'SystemMenuText', 'SystemScrollbar', 'SystemWindow', 'SystemWindowFrame', 'SystemWindowText']



    #def TkVar2EnvDct(self): #needs to be called be a TkVar listener
    #    # The envDct var must exist in env.conf file.
    #
    #    #BT.s("ct_LockVar", self.ct_LockVar.get())
    #    #BT.s("ct_killVar", self.ct_killVar.get())
    #    #BT.s('kwVar', self.kwVar.get())
    #    #BT.s('debugVar', self.debugVar.get())
    #    #BT.s('echoVar', self.echoVar.get())
    #    #BT.s('baseVar', self.baseVar.get())
    #    #BT.s('sourceVar', self.sourceVar.get())
    #    #BT.s('lastSourceVar', self.lastSourceVar.get())
    #
    #    self.envDct['ct_LockVar']    = self.ct_LockVar.get()
    #    self.envDct['ct_killVar']    = self.ct_killVar.get()
    #    self.envDct['kwVar']         = self.kwVar.get()
    #    self.envDct['debugVar']      = self.debugVar.get()
    #    self.envDct['echoVar']       = self.echoVar.get()
    #    self.envDct['baseVar']       = self.baseVar.get()
    #    self.envDct['sourceVar']     = self.sourceVar.get()
    #    self.envDct['lastSourceVar'] = self.lastSourceVar.get()


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
      self.root = Tk() # This keeps getting moved around because I can't seem to find the best place to make the call to Tk
                       # Tk must be instanciated before I can use the StringVar class or others
                       # trying to shorten the code by rolling my own StringVar
      StringVar = Tkinter.StringVar
      IntVar = Tkinter.IntVar

      if self.test:
        print 'checking for guiDct instance.'
        print isinstance(self.guiDct, DictType)

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
          # TC from baseTools __builtins__
          #self.exeVirtualMethod(self.cmdVar.get(), 2)
          #TC.exeVirtualMethod(fnLst=list(self.cmdVar.get()), bypass=2)
          TC.exeVirtualMethod(self.cmdVar.get(), 2)
      #? write method to track commands issued. Similar to how we build self.extLst
      #? prevent user from resetting program variables to different type
      #? place context controls in widget for back, forward, clear, exec

      self.cmdVar.set('')

class Context_Menu:
    # Kurry instance may already be present.  check this.
    """
    Must be instantiated by passing in parent self instance containing the definition of
    self.envDct.
    Instaniate like this: Context_Menu.__init__(self)
    """

    def __init__(self):
      #self.ct_killVar.set(0)

      # replaced with environment dictionary value.
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
        #print 'Calling function: ', self.function
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


#class ProgressBar(tk.Frame):
#    """A simple progress bar that shows a percentage progress in
#    the given colour."""
#
#    def __init__(self, *args, **kwargs):
#        apply(tk.Frame.__init__, (self,) + args, kwargs)
#        self.canvas = tk.Canvas(self, height='20', width='60',
#                                background='white', borderwidth=3)
#        self.canvas.pack(fill=tk.X, expand=1)
#        self.rect = self.text = None
#        self.canvas.bind('<Configure>', self.paint)
#        self.setProgressFraction(0.0)
#
#    def setProgressFraction(self, fraction, color='blue'):
#        self.fraction = fraction
#        self.color = color
#        self.paint()
#        self.canvas.update_idletasks()
#
#    def paint(self, *args):
#        totalWidth = self.canvas.winfo_width()
#        width = int(self.fraction * float(totalWidth))
#        height = self.canvas.winfo_height()
#        if self.rect is not None: self.canvas.delete(self.rect)
#        if self.text is not None: self.canvas.delete(self.text)
#        self.rect = self.canvas.create_rectangle(0, 0, width, height,
#                                                 fill=self.color)
#        percentString = "%3.0f%%" % (100.0 * self.fraction)
#        self.text = self.canvas.create_text(totalWidth/2, height/2,
#                                            anchor=tk.center,
#                                            text=percentString)


class Debug_Widget:
    # Need to code debug and echo by mode.
    #def __init__(self, debug):
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

      #docstring = """ = Button(self.debug_frame, name=widgetname, command=Kurry(self.callHandler, self.toggleDebug))""" + '\n'
      #command = 'self.' + widgetname + docstring
      #exec(command)


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
      #self.textVar.set(self.debugVar.get()) # textVar borked
      #self.write("Debug set to: ", self.debugVar.get())
      message = "Debug set to: " + str(self.debugVar.get())
      self.textVar.set(message)


      #self.bugger.set((self.debugVar.get() * 10) + self.echo.get())
      #self.announce(self.bugger.get())
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
      #self.bugger.set((self.debugVar.get() * 10) + self.echo.get())
      #self.announce(self.bugger.get())

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

#from gui_Tools import *
# traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "D:\GeoPy\lib\GUI\gui_Tools.py", line 2773, in <module>
#     Scroll_Tools, Widget_Tools, Temp_Widget):
# TypeError: Error when calling the metaclass bases
#     Cannot create a consistent method resolution
# order (MRO) for bases Menu_Widget, Scroll_Tools, Temp_Widget, Debug_Widget, GUI_Vars, Widget_Tools,
# Context_Menu, Base, Buttons_Widget, Text_Widget, Command_Widget
# Breaks with class Menu_Widget(GUI_Vars):

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


class Scroll_Tools:

    def __init__(self, show=1):
        # Activate these if guiPF breaks and backup is lost
        #self.guiDct['CLCVar'] = 0
        #self.guiDct['CLIVar'] = 0
        #self.guiDct['CRCVar'] = 0
        #self.guiDct['CRIVar'] = 0

        #self.CLCVar       = StringVar()  # Current Left Choice from left scroll box
        #self.CLIVar       = IntVar()     # Current Left Index from left scroll box
        #self.CRCVar       = StringVar()  # Current Right Choice from right scroll box
        #self.CRIVar       = IntVar()     # Current Right Index from right scroll box

        if show == 1:
          self.r_list_frame = Toplevel(self.root,
                                       name="r_list_frame",
                                       relief=RAISED,
                                       bd=self.bd,
                                       bg=self.bg,
                                       )

          #self.r_list_frame.geometry('%dx%d+%d+%d'%(self.cts_width,self.ct_height,self.cts_rightBound,self.ct_upperBound))
          self.r_list_frame.transient()
          self.r_list_frame.overrideredirect(1)
          self.r_list_frame.lift()

          self.r_listbox = Listbox(self.r_list_frame,
                                   name='r_Listbox',
                                   selectmode=EXTENDED,
                                   relief=SUNKEN,
                                   font=self.fonts[1],
                                   fg='black',
                                   bg='white')

          self.l_list_frame = Toplevel(self.root,
                                       name="l_list_frame",
                                       relief=RAISED,
                                       bd=self.bd,
                                       bg=self.bg,
                                       )


          self.l_list_frame.transient()
          self.l_list_frame.overrideredirect(1)
          self.l_list_frame.lift()

          self.l_listbox = Listbox(self.l_list_frame,
                                   name='l_Listbox',
                                   selectmode=EXTENDED,
                                   relief=SUNKEN,
                                   font=self.fonts[1],
                                   fg='black',
                                   bg='white')

          self.getDimensions()
        else:
          pass

          #if self.slideVar.get():
          #    self.scrollOn()
          #else:
          #    self.scrollOff()

#-------------------------------------------------------------------------
# Set up handles for list boxes
#-------------------------------------------------------------------------
    def adjustIOFrames(self):
        self.forgetAll()
        self.getDimensions()
        self.configFrames()
        self.packFrames()
        self.placeLeft()
        self.placeText()
        self.placeRight()

    def placeLeft(self):
        self.l_listbox.place(in_=self.l_list_frame, x=0, y=0, anchor='nw', bordermode=INSIDE,
                             relwidth=.95, relheight=.97)
        self.l_listbox_vsb.place(in_=self.l_list_frame, rely=0, relx=.90, relwidth=.1, relheight=1)
        self.l_listbox_hsb.place(in_=self.l_list_frame, rely=.97, relx=0, relwidth=.90, relheight=.03)
        if self.verbose:
          print 'self.l_listbox_vsb.winfo_width() = ', self.l_listbox_vsb.winfo_width()

    def placeRight(self):
        self.r_listbox.place(in_=self.r_list_frame, x=0, y=0, anchor='nw', bordermode=INSIDE,
                             relwidth=.95, relheight=.97)
        self.r_listbox_vsb.place(in_=self.r_list_frame, rely=0, relx=.90, relwidth=.1, relheight=1)
        self.r_listbox_hsb.place(in_=self.r_list_frame, rely=.97, relx=0, relwidth=.90, relheight=.03)

    def placeText(self):
        self.text.place(in_=self.text_frame, x=0, y=0, anchor='nw', bordermode=INSIDE,
                        relwidth=.97, relheight=.97)
        self.text_vsb.place(in_=self.text_frame, rely=0, relx=.97, relwidth=.03, relheight=1)
        self.text_hsb.place(in_=self.text_frame, rely=.97, relx=0, relwidth=.97, relheight=.03)

    def forgetPackText(self):
        self.text_vsb.pack_forget()
        self.text_hsb.pack_forget()
        self.text.pack_forget()
        self.text_frame.pack_forget()

    def scrollOn(self):
        # Pack all objects by order of appearence needed
        if self.slideVar.get() > 1:
            self.forgetPlaceLeft()
        self.forgetPackText()
        self.packFrames()
        self.packLeft()
        self.packText()
        self.packRight()

    def scrollOff(self):
        self.forgetPackLeft()
        self.forgetPackRight()

    def forgetAll(self):
        if self.slideVar.get() > 1:
            #self.forgetPlaceLeft()
            self.forgetPlaceText()
        self.forgetPackLeft()
        self.forgetPackText()
        self.forgetPackRight()

    def configFrames(self):
        self.l_list_frame.config(width=self.l_list_frame_widthVar.get())
        self.r_list_frame.config(width=self.r_list_frame_widthVar.get())
        self.text_frame.config(width=self.text_frame_widthVar.get())

    def idleUpdate(self):
        self.root.update_idletasks()

    def setPercentages(self):
        rx = float(self.slideVar.get() * .05)

    def getDimensions(self):
        x = int(round((self.l_list_frame_widthVar.get() * 2) + self.text_frame_widthVar.get()))
        a = int(round(x * (.10 + (self.slideVar.get() * .05))))
        b = int(round(x - (a * 2)))
        c = a - 4
        d = b - 4

        #print 'Total width is: ', x
        #print 'List frame width is: ', a
        #print 'Text frame width is: ', b
        #print 'Listbox width is: ', c
        #print 'Textbox width is: ', d
        #print
        #print 'UL corner for left list frame is: ', '(', self.l_list_frame.winfo_rootx(), ', ', self.l_list_frame.winfo_rooty(), ')'
        #print 'UL corner for left listbox is: ', '(', self.l_listbox.winfo_rootx(), ', ', self.l_listbox.winfo_rooty(), ')'
        #print
        #print 'UL corner for right list frame is: ', '(', self.r_list_frame.winfo_rootx(), ', ', self.r_list_frame.winfo_rooty(), ')'
        #print 'UL corner for right listbox is: ', '(', self.r_listbox.winfo_rootx(), ', ', self.r_listbox.winfo_rooty(), ')'
        #print

        self.l_list_frame_widthVar.set(a)
        self.r_list_frame_widthVar.set(a)
        self.text_frame_widthVar.set(b)

    def packFrames(self):
        if self.slideVar.get() < 1:
            self.l_list_frame.pack(side=LEFT, fill=BOTH, expand=NO)
            self.r_list_frame.pack(side=RIGHT, fill=BOTH, expand=NO)
            self.text_frame.pack(side=RIGHT, fill=BOTH, expand=YES)
        elif self.slideVar.get() > 6:
            self.l_list_frame.pack(side=LEFT, fill=BOTH, expand=YES)
            self.r_list_frame.pack(side=RIGHT, fill=BOTH, expand=YES)
            self.forgetPackText()
        else:
            self.l_list_frame.pack(side=LEFT, fill=BOTH, expand=YES)
            self.r_list_frame.pack(side=RIGHT, fill=BOTH, expand=YES)
            self.text_frame.pack(side=RIGHT, fill=BOTH, expand=YES)

    def forgetPlaceLeft(self):
        self.l_listbox.place_forget()

    def forgetPlaceText(self):
        self.text.place_forget()

    def toggleScroll(self):
       if self.slideVar.get() != 0:
           self.slideVar.set(1)
       else:
           self.slideVar.set(0)

    def ioResize(self, inVal=None):
        inVal = int(inVal)
        #self.catchVar(inVal, 1)
        self.slideValVar.set(inVal)
        self.slideVar.set(inVal)
        self.guiDct['slideVar'] = inVal
        if inVal == 0:
            self.scrollOff()
        elif inVal == 1:
            self.getDimensions()
            self.adjustIOFrames()
            self.scrollOn()
        else:
            self.getDimensions()
            self.adjustIOFrames()

    #def catchVar(self, inVal=0, mode=0):
    #    if mode == 1:
    #        self.slideValVar.set(inVal)
    #        self.slideVar.set(inVal)
    #        self.guiDct['slideVar'] = inVal
    #    elif mode == 2:
    #        inNum = inVal / 100
    #        self.percentVal.set(inNum)
    #        self.percentVar.set(inVal)
    #        self.guiDct['percentVar'] = inVal
    #        self.guiDct['percentVal'] = inNum
    #    else:
    #        pass

    def getPercent(self, inVal=None):
        #inVal = int(inVal)
        ##self.catchVar(inVal, 2)
        #inNum = inVal / 100
        #self.percentVal.set(inNum)
        #self.percentVar.set(inVal)
        #self.guiDct['percentVar'] = inVal
        #self.guiDct['percentVal'] = inNum
        #self.writeLine('percent is: ', inNum)
        self.percentVal.set(self.percentVar.get() * .01) #This should work in the percentPoll but am unsure why it does not.
        if self.debugVar.get() > 0:
            self.writeLine('percentVar is: ', self.percentVar.get())
            self.writeLine('percentVal is: ', self.percentVal.get())

    def clearLists(self):
        self.clearLeft()
        self.clearRight()

    #def clearText(self):
    #    # set up switch so clearText is optional.
    #    self.text.delete('1.0', END)            # clear text in widget
    #    self.announce('')
    #    self.clearSelRight()

    def clearRight(self):
        self.r_listbox.delete(0, END)

    def clearSelRight(self):
        self.r_listbox.selection_clear(0, END)
        self.R_choiceLst = []
        self.R_indexLst = []

    def insertRight(self, item, loc):
        self.r_listbox.insert(loc, item)

    def removeRight(self):
        #if self.R_start.get() > self.R_stop.get():
        #    self.r_listbox.delete(self.R_start.get())
        #else:
        #    self.r_listbox.delete(self.R_start.get(), self.R_stop.get())
        self.r_listbox.delete(self.R_start.get(), self.R_stop.get())
        self.R_scrollLst = self.r_listbox.get(0, END)

    def activateRight(self):
        self.r_listbox.activate(self.R_start.get())
        self.r_listbox.select_set(self.R_start.get(), self.R_stop.get())

    def clearLeft(self):
        self.l_listbox.delete(0, END)

    def clearSelLeft(self):
        self.l_listbox.selection_clear(0, END)

    def insertLeft(self, item, loc):
        self.l_listbox.insert(loc, item)

    def removeLeft(self):
        self.l_listbox.delete(self.L_start.get(), self.L_stop.get())
        self.L_scrollLst = self.l_listbox.get(0, END)

    def activateLeft(self):        # replaces self.L_index with self.guiDct['L_index'] but guiDct or envDct must have it defined.
        self.l_listbox.activate(self.guiDct['L_index'])
        self.l_listbox.select_set(self.guiDct['L_index'])
        self.CLCVar.set(self.l_listbox.get(self.guiDct['L_index']))
        self.setCurrentUser(self.CLCVar.get())
        self.guiDct['lastSchema'] = self.l_listbox.get(self.guiDct['L_index'])

        if self.modeVar.get() == "GDB":
            self.loadScroll(0, 'r', self.curTabLst)
        else:
            self.loadScroll(1, 'r', self.curTabLst)

    def loadScroll(self, wipe=1, mode='r', inLst=[]):
        listbox = BT.conCat(mode, '_listbox')
        if mode == 'r':
            lock = self.R_LockFlag.get()
        else:
            lock = self.L_LockFlag.get()
        if lock:
            pass
        else:
            if wipe:
                command = BT.conCat('self.', listbox, '.delete(0, END)')
                exec(command)
                if len(inLst) >= 1:
                    inLst.sort()
                    self.R_scrollLst = inLst
                    command = BT.conCat('self.', listbox, '.insert(END, item)')
                    for item in inLst:
                        exec(command)

    def procLst_2_scroll(self, mode='r'):
        self.loadScroll(1, mode, self.procLst)

    def scroll_2_procLst(self, mode='r'):
        if mode == 'r':
            self.processVar.set(str(self.R_scrollLst))
        else:
            self.processVar.set(str(self.L_scrollLst))
        for item in self.procLst:
            self.writeLine(item)
        inLst = self.convStr2Lst(self.processVar.get())[1]
        outLst = inLst.replace(' ', '\n')
        #self.writeLine(text)
        BT.fileWriteList(self.procLstFile, outLst)

    def L_event_Generate(self):
        self.l_listbox.event_generate('<<ButtonRelease-1>>', x=self.last_text_x, y=self.last_text_y)

    def selection_2_procLst(self, mode='r'):
        if mode == 'r':
          self.processVar.set(str(self.R_choiceLst))
        else:
          self.processVar.set(str(self.L_choiceLst))
        # writeToFile gets these args: filename, text, mode
        inLst = self.convStr2Lst(self.processVar.get())[1]
        outLst = inLst.replace(' ', '\n')
        #self.writeLine(text)
        BT.fileWriteList(self.procLstFile, outLst)

    def clearSelections(self):
        self.r_listbox.selection_clear(0, END)
        self.l_listbox.selection_clear(0, END)
        #self.clearProcLst()

    def printSelections(self):
        #self.writeLine('R_choiceLst has ', str(len(self.R_choiceLst)), ' items.')
        self.setProcLst(self.R_choiceLst)
        #self.writeLine('procLst has ', str(len(self.procLst)), ' items.')
        if 0 < self.debugVar.get() < 2:
            self.writeLine("Right index List is: ", self.R_indexLst)
            self.writeLine("Right choice list is: ", self.R_choiceLst, '\n')
            self.blankLine()
        for item in self.R_choiceLst:
            self.writeLine(item)
        #self.writeLine('R_choiceLst has ', str(len(self.R_choiceLst)), ' items.')
        #self.writeLine('procLst has ', str(len(self.procLst)), ' items.')
        self.blankLine()

    def processSelection(self, function, args=None):
        #if self.debugVar.get() == 0:
        #  self.scrollOff()
        #  self.slideVar.set(0)
        #  self.slideValVar.set(0)
        for item in self.procLst:
          self.input = item
          #command = self.concatNSP(function, "('", item, "')")
          command = BT.conCat(function, ")")
          self.setMethodHistory(function.strip())
          self.writeLine('command is: ', command, '\nfunction is: ', function)
          message = BT.conCat(command, ' ', args, 'processSelection')
          if self.debugVar.get() == 4:
              self.writeLine("Issuing ", command, " with input ", self.input)
              self.writeLine("Currying function: ", message)
          try:
              exec(command)
          except StandardError:
              message = BT.conCat(str(function), ' ', args, 'callHandler')
              #self.onError('White', 'Red', message)

        #self.writeLine(echoDict(self.procDct)[7])

    def printScrollList(self):
        for item in self.R_scrollLst:
            self.writeLine(item)
        self.blankLine()

    def getAttributeValue(self, attr=''): # put in type_Tools class.
        if len(attr) < 1:
            attr = self.CLCVar.get().replace('self.', '')
        item = self.__dict__[attr]
        self.writeLine(type(item))
        #if 'PY_VAR' in item:
        #    varVal = self.root.getvar(item)
        #    #self.writeLine('TK Variable encountered.')
        #    #varVal = self.master.getvar(item.strip())
        #    #self.textVar.set(varVal)

        if isinstance(item, DictType):
            self.writeLine(echoDict(item)[4])
        elif isinstance(item, ListType):
            for index in item:
                self.writeLine(index)

    def binder(self):
        self.disabled()
        #self.slider.bind("<ButtonRelease>", self.ioResize)

    def disable(self):  # in case if spell error.
        self.disabled()

    def disabled(self):
        self.setTkVar('fg_colorVar', 'red')
        self.announce('This tool is currently off-line!')

    def reportDisplay(self):
        messages = [
        ('Master x coord is:               ' + str(self.root.winfo_rootx())),
        ('Master Screen width is:          ' + str(self.root.winfo_screenwidth())),
        ('Master Screen height is:         ' + str(self.root.winfo_screenheight())),
        ('Master X_adjust is:              ' + str(self.root.X_adjust)),
        ('Master Y_adjust is:              ' + str(self.root.Y_adjust)),
        ('Master X_offset is:              ' + str(self.root.X_offset)),
        ('Master Y_offset is:              ' + str(self.root.Y_offset)),
        ('Adjusted master frame width is:  ' + str(self.root.width)),
        ('Adjusted master frame height is: ' + str(self.root.height)),
        ('Text frame height is:            ' + str(self.text_frame_height.get())),
        ('Text frame width is:             ' + str(self.text_frame_widthVar.get())),
        ('Text width is:                   ' + str(self.text_width.get())),
        ('Left list frame width is:        ' + str(self.l_list_frame_widthVar.get())),
        ('Left listbox width is:           ' + str(self.l_listbox_width.get())),
        ('Right list frame width is:       ' + str(self.r_list_frame_widthVar.get())),
        ('Right listbox width is:          ' + str(self.r_listbox_width.get()))]

        for message in messages:
            self.writeLine(message)
        self.blankLine()
        self.writeLine('UL corner for left list frame is: ', '(', self.l_list_frame.winfo_rootx(), ', ', self.l_list_frame.winfo_rooty(), ')' )
        self.writeLine('UL corner for left listbox is: ', '(', self.l_listbox.winfo_rootx(), ', ', self.l_listbox.winfo_rooty(), ')' )
        self.blankLine()
        self.writeLine('UL corner for right list frame is: ', '(', self.r_list_frame.winfo_rootx(), ', ', self.r_list_frame.winfo_rooty(), ')' )
        self.writeLine('UL corner for right listbox is: ', '(', self.r_listbox.winfo_rootx(), ', ', self.r_listbox.winfo_rooty(), ')' )
        self.blankLine()

    def packLeft(self):
        self.l_listbox_vsb.pack(side=RIGHT, fill=Y)#, expand=YES)
        self.l_listbox_hsb.pack(side=BOTTOM, fill=X)
        self.l_listbox.pack(side=LEFT, fill=BOTH, expand=YES)

    def packRight(self):
        self.r_listbox_vsb.pack(side=RIGHT, fill=Y)#, expand=YES)
        self.r_listbox_hsb.pack(side=BOTTOM, fill=X)
        self.r_listbox.pack(side=LEFT, fill=BOTH, expand=YES)

    def forgetPackLeft(self):
        self.l_listbox.pack_forget()
        self.l_listbox_vsb.pack_forget()
        self.l_listbox_hsb.pack_forget()
        self.l_list_frame.pack_forget()

    def forgetPackRight(self):
        self.r_listbox.pack_forget()
        self.r_listbox_vsb.pack_forget()
        self.r_listbox_hsb.pack_forget()
        self.r_list_frame.pack_forget()

    def packText(self):
        self.text_vsb.pack(side=RIGHT, fill=Y)
        self.text_hsb.pack(side=BOTTOM, fill=X)
        self.text.pack(side=TOP, fill=BOTH, expand=YES)

    def forgetPackText(self):
        self.text_vsb.pack_forget()
        self.text_hsb.pack_forget()
        self.text.pack_forget()
        self.text_frame.pack_forget()

class Temp_Widget:
    def __init__(self):
      self.temp_frame = Toplevel(self.root,
                                   name="temp_frame",
                                   relief=RAISED,
                                   bd=self.bd,
                                   bg=self.bg,
                                   )

      self.temp_frame.transient()
      self.temp_frame.overrideredirect(1)
      self.temp_frame.lift()
      self.temp_text = Listbox(self.temp_frame,
                               name="temp_text" ,
                               relief=SUNKEN,
                               font=self.fonts[1],
                               fg='black',
                               bg='white')


      self.temp_vsb      = Scrollbar(self.temp_frame,   name="temp_vsb" )
      self.temp_hsb      = Scrollbar(self.text_frame,   name="temp_hsb" , orient='horizontal')

      self.temp_vsb.pack(side=RIGHT, fill=Y)
      self.temp_hsb.pack(side=BOTTOM, fill=X)
      self.temp_text.pack(side=TOP, fill=BOTH, expand=YES)

      self.temp_text.config(yscrollcommand=self.temp_vsb.set)
      self.temp_text.config(xscrollcommand=self.temp_hsb.set)
      #self.temp_text.config(font=self.fonts[1], fg=self.colors[12]['bg'], bg="beige")

      # Configure scrollbar objects
      self.temp_vsb.config(command=self.temp_text.yview)
      self.temp_hsb.config(command=self.temp_text.xview)
      #
      #self.temp_text.bind('<ButtonPress-1>', self.handleEvent)
      #
      #self.temp.bind('<KeyPress-F3>',self.onKeyPress)
      #self.temp.bind('<B1-Motion>', self.onLeftDrag)
      #
      #if self.modeVar.get() == "FTR":
      self.temp_text.focus_set()

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

      if not 'rely' in self.__dict__:
        self.rely = 0

      frame_rely = self.rely
      # increment for next frame placement.  will place below text frame
      self.rely = self.rely + frame_relheight

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

class GUI_Tools():
    def __init__(self):
       self.stderr = None
       self.stdout = None

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

    # this method refers to ESRI arcpy tools
    #def callHandler3(self, fn):
    #    #! This really should be in base_Tools
    #    # This strips out 'self.' and '() from the passed in function string.
    #    arcFlag = 0
    #    P(L(S()[0]) + fn[6:len(fn)])
    #    if fn[6:len(fn)] == 'arcpy':
    #      arcFlag = 1
    #      self.function = fn
    #    else:
    #      self.function = fn[5:(len(fn) - 2)]
    #    try:
    #        if self.debug > 0:
    #          P(L(S()[0]) + self.function + ' Succeded.')
    #        exec(fn)
    #        err_exception = 1
    #    except StandardError:
    #        error = "\nError in " + str(fn)
    #        if arcFlag:
    #          arcpy.AddMessage(arcpy.GetMessages(2))
    #          error = error + "\n" + arcpy.GetMessages(2)
    #        print error
    #        import traceback
    #        print traceback.format_exc()
    #        sys.exc_clear()
    #        err_exception = 0
    #        P(L(S()[0]) + self.function + ' Failed.')

    def pyHelp(self):
      os.startfile('C:\Python25\Doc\Python25.chm')
    def pyHelp2(self):
      os.startfile('http://docs.activestate.com/activepython/3.1/python/')

    def disabled(self):
        self.blankLine()
        self.write('This tool is currently off-line!')
        self.blankLine()
        #if self.ctFlag.get():
          #self.ct_Reload()

    def findFile(self):
        self.basedir = askdirectory(title='Select a source directory.', initialdir=self.lastDir)
        self.setPathHistory(self.basedir)
        self.searchFile = askstring('Find a File', 'Enter the file name.', )
        #self.guiDct['lastSearchExt'] = self.searchFile this var is already used
        filename = 'searchResults.lst'
        listFile = os.path.join(self.outLstPath, filename)
        self.write(BT.conCat("Looking for file", self.searchFile, ".  Saving results to ", filename, "."))
        self.write("Searching ...\n\n")
        tempDct = {}

        self.f_Lst = open(listFile, 'w')

        cnt = 1

        for root, dirs, files in os.walk(self.basedir):
            #walk() generates the file names in a directory tree, by walking the tree
            #either top down or bottom up. For each directory in the tree rooted at
            #directory top (including top itself), it yields a 3-tuple
            #(dirpath, dirnames, filenames).
            tempLst = []
            root = string.replace(root, '/', os.sep)
            #ext = string.lower(self.searchStr)
            previous = ''

            for file in files:
              if isinstance(file, None):
                pass
              else:
                file = string.lower(file) #make all characters lower case.
                if file == string.lower(self.searchFile):
                    text = root + os.sep + file + '\n'
                    tempLst.append(file)
                    self.f_Lst.write(text)
                    self.write(text)
                    key = root
                    value = tempLst
                    tempDct[key] = value

            cnt = cnt + 1

        self.f_Lst.close()
        self.blankLine(2)

    def filterList(self, mode, filename=None):
      '''
      Args passed in:
      filename, mode
      Mode indicated either a negitave or positive filter.
      Negative does not include the string in the new file.
      Positive only include the string.
      '''
    #? should use the file_filter in file tools.
      filterString = ""
      filterStr = askstring('Filter', 'Enter a string.', initialvalue=self.selectedText)
      tmpLst = []
      #if isinstance(filename, NoneType):
      #  procTup = BT.getFileAsList()
      #  procLst = procTup[0]
      #  filename = procTup[1]
      #else:
      #  procTup = BT.getFileAsList(filename)
      #  procLst = procTup[0]
      query = ''
      caption="Select a list file."
      ext="lst"

      filename = self.askFileName(caption, ext)
      fileObject = open(filename, 'r')

      self.write('Reading ', filename)
      newFileName = os.path.splitext(filename)[0] + "_flt." + os.path.splitext(filename)[1].replace('.', '')
      self.fileCreate(newFileName)

      if mode == 0:
        while 1:
          line = fileObject.readline()
          if filterStr.lower() in line.lower():
            tmpLst.append(line)
          if not line:
            break

      elif mode == 1:
        while 1:
          line = fileObject.readline()
          if not line:
            break
          else:
            if filterStr.lower() in line.lower():
              tmpLst.append(line)
            else:
              pass
      else:
        tmpLst.append("Null")

      fileObject.close()

      BT.fileWriteList(newFileName, tmpLst)
      self.done()
      #self.listOpen()
      #self.blankLine()
      #self.write(filterString)

    def listOpen(self):
        filename = self.listAskName()
        if filename == None:
          self.write("No filename was returned or user canceled operation.")
        else:
          self.write(BT.conCat("You chose file: ", filename))
          BT.s('procLst', BT.getFileAsList(filename)[0])
          length = len(self.procLst)
          self.write('File of ', str(length), ' lines opened.')
          self.blankLine()
          BT.s('lastFile', filename)
          #self.guiDct['lastFile'] = filename
          self.post_Ops()
          for item in self.procLst:
            self.write(item.strip())
            self.onGoto(3)

    def pathTreeInit(self):
        self.disabled()

    def pathCompare(self):

      cDir1 = "G:/NAD83_GeoTIFF"
      cDir2 = "H:/NAD83_GeoTIFF"

      basedir1 = askdirectory(initialdir=cDir1, title='Select directory 1.')
      basedir2 = askdirectory(initialdir=cDir2, title='Select directory 2.')
      cmpOutput = filecmp.cmpfiles(basedir1, basedir2, common)
      self.write(cmpOutput)

    def listByFolder(self):
        #! Obsolite.  Roll into getList method below.
        self.disabled("listByFolder is obsolete.  Will be rolled into getList method.")
        # Need to set a list of source paths to process in a loop.
        # Refer to Path_Tools.setSource()
        #self.baseVar.set(self.askPath('Select a source directory.', self.baseVar.get()))
        #
        #if self.baseVar.get() == None:
        #  self.write("No pathname was returned or user canceled operation.\n")
        #else:
        #  filename = os.path.split(self.baseVar.get())[1] + '_all.lst'
        #  listFile = self.setSlash('F', os.path.join(self.outLstPath, filename))
        #  if BT.checkFileObject(listFile):
        #    self.write("Searching ", self.basedir, " ...\n\n")
        #    tempDct = {}
        #
        #    self.f_Lst = self.fileOpen(listFile, 'w')
        #
        #    cnt = 1
        #
        #    root = string.replace(self.baseVar.get(), '/', os.sep)
        #
        #    for file in os.listdir(root):
        #      file = string.lower(file) #make all characters lower case.
        #      text = file + '\n'
        #      inStr = root + os.sep + file
        #      self.f_Lst.writeStr(text)
        #      self.write(inStr)
        #
        #    self.f_Lst.close()
        #    self.write("\nFinished!")

    def getList(self, mode=1):
        '''
        Mode 0 will batch process by a list of extensions.
        Mode 1 will process by one extension.
        Mode 2 will process by one keyword anywhare in the file name.
        Mode 3 will process by folder.
        '''
        def kwProc(kw, filename, qStr=''):
          query = ''
          cnt = 0
          procFlag = 0
          self.setTkVar('kwVar', kw)
          #? what does procFlag do?
          listFile = BT.setSlash("F", os.path.join(self.outPathVar.get(), filename))
          self.write('Using this outputFile: ', listFile)
          if 'None' in listFile:
            self.write('Nonetype encountered in filename.  Program aborted operation.')
          else:
            #? create an option in checkFileObject for creating blank files.
            while not BT.checkFileObject(listFile):
              if cnt > 5:
                self.write('File creation failed...bailing out')
                procFlag = 1
                break
              self.fileCreate(listFile)
              cnt = cnt + 1
            if not procFlag:
              self.write(BT.conCat("Looking for extension <", kw, ">.  Saving results to ", listFile, ".\n"))
              tempDct = {}
              self.f_Lst = self.fileOpen(listFile, 'w')
              cnt = 1

              for root, dirs, files in os.walk(self.sourceVar.get()):
                #walk() generates the file names in a directory tree, by walking the tree
                #either top down or bottom up. For each directory in the tree rooted at
                #directory top (including top itself), it yields a 3-tuple
                #(dirpath, dirnames, filenames).
                tempLst = []
                root = string.replace(root, '/', os.sep)
                previous = ''

                for file in files:
                  if mode != 2:
                    file = string.lower(file)
                  query = repr(file) + qStr
                  #if cnt < 10:
                    #print 'query:', query, eval(query)
                  if eval(query):
                    text = root + os.sep + file + '\n'
                    inStr = root + os.sep + file
                    self.pathLst.append(text.strip())
                    tempLst.append(file)
                    self.f_Lst.write(text)
                    if self.echoVar.get():
                      self.write(inStr)
                    key = root
                    value = tempLst
                    tempDct[key] = value

                  cnt = cnt + 1

              self.fileDct = tempDct
              self.fileLst = self.pathLst
              self.f_Lst.close()
              self.write("Finished!\n")

        self.setInPath()

        if mode == 0:
          if len(self.kwLst) == 0:
            self.setKeyWordList()
          for kw in self.kwLst:
            kwProc(kw)
        else:
          if self.setKeyWord():
            if mode == 1:
              filename = self.kwVar.get() + '.' + self.outExtVar.get()
              qStr = '.endswith(string.lower(' + repr(self.kwVar.get()) + '))'
            elif mode == 2:
              filename = self.kwVar.get() + '_kw.lst'
              qStr = '.count(' + repr(self.kwVar.get()) + ') > 0'
            elif mode == 3:
              self.listByFolder()
            kwProc(self.kwVar.get(), filename, qStr)

          # Need to raise our own error here.

    def listFileDct(self):
        self.write(echoDict(self.fileDct, 0, 0, 1, 'listFileDct')[4])

    def listFileLst(self):
        for file in self.fileLst:
          self.write(file)

    def setOutPath(self):  #move to Path_Tools???
        titleStr = 'Select an output path.'
        #self.write('Last path was: ', self.lastoutLstPath) # shorten to lastOutPath or last distination
        #path = self.setSlash("F", askdirectory(title=titleStr, initialdir=self.setSlash("F", self.outPath)))
        path = BT.setSlash("F", askdirectory(title=titleStr, initialdir=self.outPathVar.get()))
        #if len(path) == 0:
        #  #self.write("Zero length path encountered. User canceled operation or entered a blank return.")
        #  self.outPathVar.set(self.setSlash("F", self.outPath))#combine these see fixme.lst
        if self.pathCheck(path):
          self.setTkVar('outPathVar', path)
          #BT.s('outPath', path)  #combine these
          #self.outPathVar.set(path)#combine these see fixme.lst

        self.write("All list output files will be saved in: ", self.outPathVar.get())

    def setInPath(self): #select input path
        titleStr = 'Select the source path.' # \n\nLast path used = \n' + self.setSlash("F", self.sourceVar.get())
        #path = self.setSource(self.lastSourceVar.get())    borked.
        #? Have setSlash return only strings.
        path = BT.setSlash("F", askdirectory(title=titleStr, initialdir=self.sourceVar.get()))

        #? Path is coming across as unicode again for some unknown reason.
        #? Stop using Tk's askdirectory.  Roll my own.

        #print "pathcheck", self.pathCheck(path)
        #self.write("Path check returned: ", self.pathCheck(path), "\n")
        #? sourceVar is always populated with the last used value.  lastSourceVar is redundant
        #if len(path) == 0:
        #  self.write("Zero length path encountered. User canceled operation or entered a blank return.")
        #  #self.setTkVar('sourceVar', self.lastSourceVar.get())#? combine these see fixme.lst
        #  self.write('Using this path instead: ', self.lastSourceVar.get())
        #else:
        if self.pathCheck(path):
          #self.setVar('lastSource', self.source)
          #self.setTkVar('lastSourceVar', self.source)
          #self.setVar('source', path)
          #? Only the tkVar needs to be used.  self.source is redundant.
          self.setTkVar('sourceVar', path)
          #self.write('Searching this source path: ', self.sourceVar.get())
          #? self.sourceVar.get() is failing to return a value.  Use path as a workaround.
          self.write('Searching this source path: ', path)
          self.setPathHistory(path)
        else:
          self.write("Path check didnt work.")
          #self.setTkVar('sourceVar', self.setSlash("F", self.source))
          #self.write('Using this path instead: ', self.source)

    def setOutExt(self):  #set restrants to limit choice to valid ascii text extensions.
        inStr = askstring('Set output file extension.', 'Enter the output file extension to use.', initialvalue=self.outExtVar.get())
        if isinstance(inStr, NoneType):
          inStr = self.outExtVar.get()
          self.write("Nonetype extension encountered. Using the default value of ", inStr, ".")
        elif isinstance(inStr, UnicodeType):
          inStr = str(inStr)
        elif isinstance(inStr, StringType):
          if len(inStr) == 0:
            inStr = self.outExtVar.get()
            self.write("Zero length extension encountered. Using the default value of ", inStr, ".")
          else:
            if '.' in inStr:
              inStr = inStr.replace('.', '')
            #BT.s('outExt', inStr) redundant use the TkVar instead
            self.setTkVar('outExtVar', inStr)
            #self.outExtVar.set(inStr)
            self.write("All list output files will now have the extension of ", inStr, ".")

    def setKeyWord(self):
        #Tk var extVar is not getting a value set at first run. Initial value returns 'None'
        #? replace askstring with input from GUI widget.  Cross between tk and wx

        #inStr = askstring('Set Keyword', 'Enter a search key word.', initialvalue=self.kwVar.get(), minlength=1)

        #inStr = askstring('Set Keyword', 'Enter a search key word.', initialvalue=self.kwVar.get(), show='*')

        inStr = askstring('Set Keyword', 'Enter a search key word.', initialvalue=self.kwVar.get())

        if isinstance(inStr, NoneType) or len(inStr) == 0:

          self.callBailOut(self.methInfo(0, "ValueError:  Zero Length Keyword Encountered!!!", stackLst=stack()[0]))
          return 0
          #self.write("Nonetype keyword encountered.  User aborted operation.")


        #  self.write("Zero length keyword encountered. Using last known good value.")
        #  #kwVar will/should always be a string upon retrival.
        #  inStr = self.kwVar.get()
        #el
        else:
          if isinstance(inStr, UnicodeType):
            inStr = str(inStr)
          elif isinstance(inStr, StringType):
            #BT.s('kw', inStr)
            #? future rename setTkVar to setGuiVar
            self.setTkVar('kwVar', inStr)
            if self.echoVar.get():
              self.write("Using this keyword: ", inStr, ".")
          return 1

    def setKeyWordList(self):
        tmpLst = []
        while self.setKeyWord():
          if not self.kwVar.get() in tmpLst:
            tmpLst.append(self.kwVar.get())  #? make procLst???
            self.write("Added ", self.kwVar.get(), " to keyword process list.")
            self.setKeyWord()

        BT.s('kwLst', tmpLst)

    def viewKeyWords(self, mode=0):
        # clear list and append the last keyword value
        # to avoid a blank list.
        if mode == 0:
          for item in self.kwLst:
            self.write(item)
        elif mode == 1:
          self.write(self.kwVar.get())

    def clearKeyWordList(self, flag=0):
        # clear list and append the last keyword value
        # to avoid a blank list.
        self.kwLst = []

    def listAskName(self, file_Types='lst'):
        #self.clear()
        file_Types=[('List files', str(file_Types)), ('All files', '*')]
        filename = askopenfilename(title='Select a file.', initialdir=self.listPath, filetypes=file_Types)
        if os.path.exists(filename):
          return filename
        else:
          return None

    def reportProgDict(self):
        self.write(echoDict(self.passDct)[2])

    def reportEnvDict(self):
        print "self.envDct = ", self.envDct

        self.write(echoDict(self.envDct)[2])

    def reportEnvVars(self):

        maxLen = 0
        for k,v in os.environ.iteritems():
            x = len(k.strip())
            if x > maxLen:
                maxLen = x + 3

        for k,v in os.environ.iteritems():
            varVal = os.getenv(k.strip(), 'Null')
            spacer = ' ' * (maxLen - len(k.strip()))
            spacer2 = ' ' * (maxLen + 1)
            rep    =  ';\n' + spacer2
            self.write(BT.conCat(k.strip(), spacer, ' = ', varVal.replace(';', rep)))

    def reloadGUI(self):
        self.write(list_tools)
        self.write(Lister_Tools)
        #del list_tools
        #list_tools = Lister_Tools(0, e.debug, root)

    def execVirtualModule(self):
        fnStr = BT.getFileAsList('', 'Pick a python module.', 'py')[0]
        self.virtualMethod(fnStr)

    def modImport(self):
        #Maybe need to set a thread here to trace un-import???
        self.callHandler("from user_Tools import *")

    def modSetName(self, inStr=None):
        inStr = askstring('Reload method', 'Name a method to reload.')
        self.method = 'self.' + inStr
        command = 'self.module = inspect.getmodule(' + self.method + ')'
        exec(command)
        self.modName = self.module.__name__
        self.modFile = self.module.__file__
        command = 'self.sourceFile = inspect.getsourcefile(' + self.method + ')'
        exec(command)
        self.write('self.module     = ', self.module,     type(self.module), '\n',
                   'self.modName    = ', self.modName,    type(self.modName), '\n',
                   'self.modFile    = ', self.modFile,    type(self.modFile), '\n',
                   'self.sourceFile = ', self.sourceFile, type(self.sourceFile), '\n',
                   )
        self.blankLine()
        command = 'self.classTree = inspect.getclasstree()'
        #message = self.conCat("Setting params ----- <method '" + self.method + "'>:  ", str(self.module), ":  <source '", self.sourceFile, "'>")
        #self.messVar.set(message)
        members = inspect.getmembers(self)
        #self.write(type(members), str(len(members)))
        value = ''
        itype = ''
        for item in members:
          self.write(item)

    def modCompile(self):
        message = BT.conCat("Compiling module ----- <method '" + self.method + "'>:  ", str(self.module), ":  <source '", self.sourceFile, "'>")
        self.messVar.set(message)
        compiler.compileFile(self.sourceFile)

    def modReload(self):
        message = BT.conCat("Reloading module ----- <method '" + self.method + "'>:  ", str(self.module), ":  <source '", self.sourceFile, "'>")
        self.messVar.set(message)

        #self.write(knee.import_hook(self.modName))

        keyLst = sys.modules.keys()
        keyLst.sort()

        #object = self.modName

        #module = sys.modules[object.__class__.__module__]
        #mod_doc = sys.modules[self.__class__.__module__].__doc__
        #mod_name = sys.modules[self.__class__.__module__].__name__

        modDct = {}
        for key in keyLst:  # Build a sorted dictionary to list in alpabetic order.
          if isinstance(sys.modules[key], NoneType):
            pass
          else:
            self.write(sys.modules[key])
          #self.write(key, sys.modules[key])
          modDct[key] = sys.modules[key]
        self.write(echoDict(modDct)[2])

        #for k in self.module.__dict__.keys():
        #  self.write("Unregistering module ", k)
        #  if k in ('__file__', '__name__'):
        #    continue
        #  del self.module.__dict__[k]


        #self.modUnload()
        #try:
        #  # Need to try reload() here.
        #  #import self.modName
        #  self.modCompile()
        #  __import__(self.modName)
        #  if self.modName in sys.modules:
        #    self.write("Re-Import of '%s' sucessfull." % self.modName)
        #  else:
        #    self.write("Re-Import of '%s' failed." % self.modName)
        #except ImportError:
        #    self.messVar.set("ImportError encountered with module '%s'" % self.modName)
        #

        #else:
        #    self.write("'%s' was not re-imported" % self.modName)

        #del sys.modules[self.modName]
        #reload(self.modName)
        #if self.modName in sys.modules:
        #  try:
        #    from imp import reload
        #  except ImportError:
        #    pass # builtin in py2k
        #  reload(sys.modules[self.modName])
        #  self.messVar.set("reload succeeded.")
        #self.messVar.set("no reload performed.")

    def modUnload(self):
        if self.modName in sys.modules:
          self.write("Deleting '%s' from sys.modules." % self.modName)
          del sys.modules[self.modName]
          if self.modName not in sys.modules:
            self.write("Delete of '%s' sucessfull." % self.modName)
          else:
            self.write("Delete of '%s' failed." % self.modName)
        self.loadClassAttributes()

    def loadClassAttributes(self):
        #for k,v in vars().iteritems():
          #print k, ': ', v
        # use this
# vars( [object])
# Without arguments, return a dictionary corresponding to the current local symbol table.
# With a module, class or class instance object as argument (or anything else that has a
# __dict__ attribute), returns a dictionary corresponding to the object's symbol table.
# The returned dictionary should not be modified: the effects on the corresponding symbol
# table are undefined.2.4


        self.memDct = {}

        self.boundMetDct = {}
        self.funDct = {}   #functional attributes
        self.mapDct = {}

        self.attrDct = {}
        members = inspect.getmembers(self)
        #self.write(type(members), str(len(members)))
        value = ''
        itype = ''
        for item in members:

          if isinstance(item[1], MethodType):
            if str(item[1].im_func.__module__) == '__main__':
              value = BT.conCat(os.path.splitext(sys.argv[0])[0], '.', str(item[1].im_class.__name__), '.', str(item[1].im_func.__name__))
              module = os.path.splitext(sys.argv[0])[0]
              path = os.path.normpath(os.path.join(self.guiDct['homePath'], sys.argv[0]))
              #path = os.path.normpath(os.path.join(self.envDct['homePath'], sys.argv[0]))
            else:
              value = BT.conCat(str(item[1].im_func.__module__), '.', str(item[1].im_func.__name__))
              module = str(item[1].im_func.__module__)
              if isinstance(inspect.getsourcefile(item[1]), NoneType):
                path = str(inspect.getsourcefile(item[1]))
              else:
                path = os.path.normpath(inspect.getsourcefile(item[1]))

            file = os.path.splitext(os.path.basename(path))[0]

            #module = item[1].im_func.__module__
            function = str(item[1].im_func.__name__)

            if not file in self.funDct.keys():
              self.funDct[file] = []
            else:
              if not function in self.funDct[file]:
                self.funDct[file].append(function)

            self.boundMetDct[function] = path

            #self.write(module, ' ', function, ' ', file)
            #print "MethodType", str(len(self.boundMetDct))
          else:
            if str(item[0]) == 'memDct':
              pass
            else:
              value = item[1]
              self.mapDct[str(item[0])] = value
              #self.write(echoDict(self.mapDct, 0, 0, 1, 'loadClassAttributes')[4])
              #self.write(str(item[0]), '  value is ',  type(value))
              #print "OtherType", str(len(self.mapDct))


          self.memDct[str(item[0])] = str(type(item[1])) + ' ' + str(item[1])

        self.memLst = self.memDct.keys()
        self.memLst.sort()

        #if self.verbose:
        #  self.write(echoDict.__doc__)
        #  self.write(echoDict(self.funDct, 0, 0, 1, 'loadClassAttributes')[4])
        # Review this code for possible usage in this def. In order to set a method attribute,
        # you need to explicitly set it on the underlying function object:
        # class C:
        #     def method(self):
        #         pass
        #
        # c = C()
        # c.method.im_func.whoami = 'my name is c'

        #self.write(inspect.ismodule(self.memDct['askFileName']))

        #for item in dir(self):
        #  if hasattr(self, item.strip()):
        #    object = 'self.' + item.strip() + '.func_code'
        #
        #    if not isinstance(object, NoneType):
        #      command = object + '.co_varnames'
        #      cmdStr  = 'output = ' + command
        #      try:
        #        exec(cmdStr)
        #        msg = item.strip() + str(output)
        #        self.write(msg)
        #
        #      except AttributeError:
        #        pass
        #    msg     = ""
        #    command = ""
        #    cmdStr  = ""
        #  else:
        #    #self.write(self.concat(item.strip(), ' does not belong to self instance.'))
        #    self.write(self.conCat(item.strip(), ' does not belong to Lister_Tools instance.'))

    def pathSplit(self, pathstring):
        pathlist = string.split(pathstring, os.pathsep)
        return self.formatLst(pathlist, pathlist)

    def formatlist(self, lst, rawform):
        return ('[\n' + string.join(lst, ',\n') + '\n]' + '\n\nRAW=>\n')

    def nullFunction(self):
        pass

    def shapeCopy(self):
        tmpDct = {}
        self.cntyDct = {}
        fileObject = open(self.cntyFile, 'r')
        #procBat = self.setSlash('F', os.path.join(self.processPath, 'copy.bat'))
        #fileObject2 = open(procBat, 'w')

        self.cntyLst = fileObject.readlines()
        #tmpDct = self.Env_Tools.defineDict(self.cntyLst)
        tmpDct = BT.defineDict(self.cntyLst) # from Map_Class
        for k,v in tmpDct.iteritems():
          self.cntyDct[k] = v.split()

        tmpLst = sorted(echoDict(self.cntyDct)[10])
        strLst = []
        #for item in tmpLst:
        #  self.write(item, '\n')

        if len(self.pathLst) == 0:
          self.write('\n\nNull list encountered.  Bailing out of batchMerge!')
        else:
          for item in self.pathLst:
            for k,v in self.cntyDct.iteritems():
              region = v[2]
              regPath = 'reg' + str(region)
              if v[0] in item:
                root = os.path.dirname(item)
                base = os.path.splitdrive(root)[0]
                cntyName = os.path.split(root)[1]
                processPath = os.path.join(self.processPath, regPath)
                outPath = os.path.join(processPath, cntyName)
                outFile = os.path.join(base, outPath)
                #self.write(root, '\n\n')
                #self.write(self.conCat(self.processPath, ' ', root, ' ', base, ' ', outPath, ' ', outFile))
                os.chdir(root)
                outputlist = win32pipe.popen('dir /a').readlines()
                #self.write(str(len(outputlist)), '\n')
                copyLst = []
                for x in range(len(outputlist)):
                  if x > 6 and x < (len(outputlist) - 2):
                    #self.write(str(x), ' ', outputlist[x])
                    strLst = outputlist[x].split()
                    filename = BT.setSlash("F", (os.path.join(root, strLst[len(strLst) - 1])))
                    for item in self.shapeExtLst:
                      if item in filename and 'xml' not in filename:
                        copyFile = BT.setSlash("F", (outFile + os.path.splitext(filename)[1]))
                        command = "copy " + filename + ' ' + copyFile
                        command = command.replace('/', os.sep).strip()
                        text = command + '\n'
                        copyLst.append(text)
                        tmpLst = win32pipe.popen(command).readlines()
                        for item in tmpLst:
                          copyLst.append(item)
                        copyLst.append('Finished copy\n')
                        self.write(copyLst, '\n')

                        #self.write(filename, '\n')
                        #self.write(copyFile, '\n')

                    #self.write(len(strLst), ' ', outputlist[x])
                self.blankLine()

                #self.write(item, '\n')

    def post_Init(self):

        # set some defaults
        # Have the pyw file write the py file.

        #if self.guiState == 'Shell':
        #if os.environ['guiState'] = 'Shell'
          #self.stderrRedirect()

        #if os.path.splitext(sys.argv[0])[1] == '.pyw':
        #if os.environ['guiState'] == 'GUI':

        print "Command and control passed from __init__. Go with throttle up."

        self.loadClassAttributes()
        # put a timer on this.
        #self.clearText()

        #self.getPathHistory()
        #self.dateVar.set(strftime("%a, %d %b %Y", localtime()))
        #self.clockVar.set(strftime("%H:%M:%S", localtime()))
        #self.setAttributeList()

        #self.processVar.set(BT.getFileAsList(str(self.procLstFile)[0]))

    def throwError(self):
        """Throw a simulated error message to test self.stderr and associated Tkvars."""
        #sys.stderr.write("\nSimulated Error message sent to sys.stderr.\n")
        #self.stderr.write("\nSimulated Error message sent to sys.stderr.write()\n")
        # self.textVar.set(self.stderr.getvalue()) # repeats the above message.
        try:
          raise FakeError("Fake Error")
        except FakeError:
          if self.guiState == 'GUI':
            self.textVar.set(BT.conCat("\n", "Simulated Error flew by!!!  Error sent to: ", self.guiState, " via sys.stderr.write()\n"))
            #self.write("Simulated Error flew by!!!  Error sent to: ", self.guiState, ' via self.write()')
          elif self.guiState == 'Shell':
            print BT.conCat("\n", "Simulated Error flew by!!!  Error sent to: ", self.guiState, " via sys.stderr.write()\n")
            #sys.stderr.write(self.conCat("\n", "Simulated Error flew by!!!  Error sent to: ", self.guiState, " via sys.stderr.write()\n"))
          raise
# need to code a toggle stderr function.

    def stderrRedirect(self):
      #BT.s('guiState', 'GUI')
      BT.s('guiState', 'GUI')
      os.environ['guiState'] = 'GUI'
      self.stderr = sys.stderr

    def stderrRestore(self):
      BT.s('guiState', 'Shell')
      os.environ['guiState'] = 'Shell'
      sys.stderr = self.stderr

    def stdoutRedirect(self):
      BT.s('stdoutFlag', 'GUI')
      os.environ['stdoutFlag'] = 'GUI'
      self.stdout = sys.stdout

    def stdoutRestore(self):
      BT.s('stdoutFlag', 'Shell')
      os.environ['stdoutFlag'] = 'Shell'
      sys.stdout = self.stdout

    def redirectIO(self):
      self.stderrRedirect()
      self.stdoutRedirect()

    def restoreIO(self):
      self.stderrRestore()
      self.stdoutRestore()

    def onQuit(self):
      self.post_Ops()
      self.closeGui(1.5)

    def post_Ops(self):
        """post_Ops
        Writes out environment dictionary key, value pairs to file. (seperated by newline character)"""
        try:
          self.envDct['run'] = 0 # Set run back to false state
          print "Saving persistant state environment"
          #self.setSysEnvVars() #setSysEnvVars does not exist. Might need to reverse engineer it. Also, need to make sure the tkVar values are getting into the guiDct
          self.setGuiVars()
          saveState(self.stDct['stPF'])
          saveState(self.envDct['envPF'])
          saveState(self.guiDct['guiPF'])
          saveState(self.guiDct['cmdPF'])
          #self.saveDbase(self.stDct['stPF'], self.stDct)
          #self.saveDbase(self.envDct['envPF'], self.envDct)
          #self.saveDbase(self.guiDct['guiPF'], self.guiDct)
        except StandardError:
          print "PostOps boinked."
          P()
        finally:
          self.restoreIO()
          #self.traceBack = sys.exc_info()[2]
          #print "self.traceBack", self.traceBack
          #import traceback
          #print traceback.print_exc()

class FakeError(Exception):
    def __init__(self, value):
      self.value = value
    def __str__(self):
      return repr(self.value)

class Launch_GUI(GUI_Vars, GUI_Tools, Menu_Widget, Command_Widget, Text_Widget, \
                 Debug_Widget, Buttons_Widget, Message_Widget, Context_Menu,       \
                 Scroll_Tools, Event_Handlers, Widget_Tools, Temp_Widget,  \
                 Tkinter.Entry):

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
        GUI_Vars.__init__(self)
        self.verNo = ET.verNo
        self.root.title('PyFace 3.0.1 on <python ' + self.verNo + '>')
        self.root.X_adjust = (self.root.winfo_screenwidth() * .005)
        self.root.Y_adjust = (self.root.winfo_screenheight() -  (self.root.winfo_screenheight() * .9650))
        self.root.X_offset = 0
        self.root.Y_offset = 0
        self.root.width  = self.root.winfo_screenwidth()  - self.root.X_adjust
        self.root.height = self.root.winfo_screenheight() - self.root.Y_adjust
        self.root.geometry('%dx%d+%d+%d'%(self.root.width,self.root.height,self.root.X_offset,self.root.Y_offset))
        self.root.config(bg='black', relief=RIDGE)
        GUI_Tools.__init__(self)
        #self.callHandler("GUI_Vars.__init__(self)")
        Menu_Widget.__init__(self)
        #P("Paused before Command_Widget.__init__(self, 3)")
        Command_Widget.__init__(self)
        #sys.stdin = self
        #P("Paused before Text_Widget.__init__(self, 3)")
        Text_Widget.__init__(self, 3.75)
        if not self.debug:
          sys.stderr = self        #redirect stderr and stdout to text widget
          sys.stdout = self        #This only works after self defines a write method.
        else:
          sys.stderr = self
          sys.stdout = self
        #P("Paused before Debug_Widget.__init__(self)")
        Debug_Widget.__init__(self)
        #P("Paused before Buttons_Widget.__init__(self)")
        Buttons_Widget.__init__(self)
        #self.sinVar.set(1)
        #P("Paused before Message_Widget.__init__(self)")
        Message_Widget.__init__(self)
        #P("Paused before Context_Menu.__init__(self)")
        Context_Menu.__init__(self)
        #P("Paused before Scroll_Tools.__init__(self)")
        Scroll_Tools.__init__(self)
        #P("Paused before Widget_Tools.__init__(self")
        Widget_Tools.__init__(self)
        #P("Paused before self.root.mainloop()")
        self.root.mainloop()
      except StandardError:
        #import traceback
        #print traceback.print_exc()
        Err('Launch_GUI.__init__', None, sys.exc_info()[2])
        sys.stdin = sys.__stdin__
        P(M(Sk()))
      #! As soon as we define a write method, we redirect sys.stdout to it.
      #! Do the same for sys.stderr, sys.stdin.
      #! This might can be done sooner since base_Tools.Default_Output has a write method as well.

      #self.root.mainloop()

    #def processIncoming(self):
    #  """
    #  Handle all the messages currently in the queue (if any).
    #  """
    #  while self.queue.qsize():
    #    try:
    #      msg = self.queue.get(0)
    #      # Check contents of message and do what it says
    #      # As a test, we simply print it
    #      #print msg
    #      self.writeThreadedOutput(msg)
    #      #self.announce(msg)
    #    except Queue.Empty:
    #      pass

'''endfile'''


if __name__ == '__main__':
  tmpvar = "Some test sentence."
  main()






