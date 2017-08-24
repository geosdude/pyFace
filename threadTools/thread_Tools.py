#!/bin/bash
# -*- codign:utf-8 -*-
# pyFace.threadTools.thread_Tools
# Coded by Richard Polk
#----------------------------------------------------

impLst = ['from threading import Thread',
          'import threading', 'import inspect']

for command in impLst:
  try:
    print '    |' + __name__ + '|', command
    exec(command)
  except ImportError:
    print  "ImportError! Failure of --> " + command + " <-- detected!"
print '    |' + __name__ + '| ---'

class ThreadedClient:
    """This class is a base class"""

#  some code that might work.
#  for j in ('90.','52.62263.','26.5651.','10.8123.'):
#    if j == '90.':
#        z = ('0.')
#    elif j == '52.62263.':
#        z = ('0.', '72.', '144.', '216.', '288.')
#
#    for k in z:
#        exepath = os.path.join(exe file location here)
#        exepath = '"' + os.path.normpath(exepath) + '"'
#        cmd = [exepath + '-j' + str(j) + '-n' + str(z)]
#
#        process=Popen('echo ' + cmd, shell=True, stderr=STDOUT )
#        print process

  #"""
  #  echo            = methDct[methodName][0]
  #  verbose         = methDct[methodName][1]
  #  message         = methDct[methodName][2]
  #  option or debug = methDct[methodName][3]
  #  keyword Dict    = methDct[methodName][4]
  #"""

    def __init__(self, root=None, *args, **kwargs):
      """  """
      #! If these lines are present at the top of a function, metadata
      #  on the function gets populated in the method dictionary.
      methodName = 'ThreadedClient.__init__'
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
      # set up tk root from a passed in Tk() instance.
      #if not root:
      self.root = root
      #? Create an independent GUI output.
      # Create the queue
      self.queue = Queue.Queue()

    def getThreadCount(self):
      return str(threading.activeCount())

    def getThreadList(self):
      return threading.enumerate()

    def runThread(self, fnStr=''):
      methodName = Mn(Sk())
      isEchoKey(methodName)
      echo    = echoDct[methodName][0]
      verbose = echoDct[methodName][1]
      message = echoDct[methodName][2]
      if echo:
        M(Sk(), offset=7)
      # Set up the thread to do asynchronous I/O
      # More can be made if necessary
      self.running = 1
      self.thread1 = threading.Thread(target=self.workerThread1(fnStr))
      self.thread1.start()

      # Start the periodic call in the GUI to check if the queue contains
      # anything
      self.periodicCall()

    def periodicCall(self):
      """
      Check every 100 ms if there is something new in the queue.
      """
      methodName = Mn(Sk())
      isEchoKey(methodName)
      echo    = echoDct[methodName][0]
      verbose = echoDct[methodName][1]
      message = echoDct[methodName][2]
      if echo:
        M(Sk(), offset=11)
      self.processIncoming()
      #if not self.running:
        # This is the brutal stop of the system. You may want to do
        # some cleanup before actually shutting it down.
        #import sys
        #sys.exit(1)

      # requires a Tk() instance
      if not isinstance(self.root, NoneType):
        self.root.after(100, self.periodicCall)

    def workerThread(self):
      """
      This is where we handle the asynchronous I/O. For example, it may be
      a 'select()'.
      One important thing to remember is that the thread has to yield
      control.
      """
      while self.running:
        # To simulate asynchronous I/O, we create a random number at
        # random intervals. Replace the following 2 lines with the real
        # thing.
        time.sleep(rand.random() * 0.3)
        msg = rand.random()
        self.queue.put(msg)

    def workerThread1(self, fnStr):
      """
      This is where we handle the asynchronous I/O. For example, it may be
      a 'select()'.
      One important thing to remember is that the thread has to yield
      control.
      """
      methodName = Mn(Sk())
      isEchoKey(methodName)
      echo    = echoDct[methodName][0]
      verbose = echoDct[methodName][1]
      message = echoDct[methodName][2]
      if echo:
        M(Sk(), offset=13)
      while self.running:
        # To simulate asynchronous I/O, we create a random number at
        # random intervals. Replace the following 2 lines with the real
        # thing.
        #exec(fnStr)
        #f = locals()["virtualFunction"](self)
        #msg = self.singlePipe(fnStr)
        msg = os.popen(fnStr).readlines()
        self.queue.put(msg)


    def endThread(self):
      self.running = 0

    #? move this to the Threaded client. Drop the Code_Tools class and merge with ThreadedClient
    def execPyFile(self):
      methodName = Mn(Sk())
      isEchoKey(methodName)
      echo    = echoDct[methodName][0]
      verbose = echoDct[methodName][1]
      message = echoDct[methodName][2]
      if echo:
        M(Sk(), offset=7)
      #? maybe use the pyThrower or start a new thread
      #self.start_new_thread("os.startfile(os.path.normpath(self.askFileName('Select a file.', 'py')))")
      #? need to redirect the output.  try Pied Piper in a thread.
      # needs File_Tools class
      try:
        command = os.path.normpath(self.askFileName('Select a file.', 'py'))
      except NameError:
        print "can not find askFileName method."
        command = os.path.normpath(askopenfilename(title='Select a file.', filetypes='py'))
      print command
      command = """
def virtualFunction(self): """ + "\n  " + command + "\n" + "  self.running = 0"
      #print command
      self.runThread(command)

# Experimental code.
#------------------------------------------------------------------------------------
#    def exeVirtualMethod(self, *args, **kwargs):
#      """
#      Usage:  Caller must pass in kwargs fnLst and bypass in that order.
#      Example: self.exeVirtualMethod(fnLst=['self.clear()'], bypass=0)
#      """
#      methodName = Mn(Sk())
#      try:
#        echo    = echoDct[methodName][0]
#        verbose = echoDct[methodName][1]
#        message = echoDct[methodName][2]
#        option  = echoDct[methodName][3]
#        kw      = echoDct[methodName][4]
#      except StandardError:
#        self.isEchoKey(methodName)
#        echo    = echoDct[methodName][0]
#        verbose = echoDct[methodName][1]
#        message = echoDct[methodName][2]
#        option  = echoDct[methodName][3]
#        kw      = echoDct[methodName][4]
#      if kwargs:
#        kwargs['args'] = args
#        kw.update(kwargs)
#        echoDct[methodName][4] = kw
#      if echo:
#        M(Sk(), offset=20)
#      fnStr = self.processPyCode(kw['fnLst'], kw['bypass']) + \
#"""
#  self.blankLine()
#"""
#      try:
#        if echo:
#          print 'Executing this virtual  function: '
#          print fnStr
#
#        exec(fnStr)
#        f = locals()["virtualFunction"](self)
#
#      except StandardError:
#        error = "command failed: \n" + fnStr + '\n\n'
#        print error
#        import traceback
#        print traceback.format_exc()
#

#! The above code needs to me implemented to deprecate the below.
    #def exeVirtualMethod(self, **kwargs):
    def exeVirtualMethod(self, fnLst=[], bypass=0, **kwargs):
      """Execute a function passed in as a list of strings representing lines of code."""
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
        M(Sk(), verbose=1, offset=20)
      if kw.has_key('preCmdLst'):
        for command in kw['preCmdLst']:
          exec(command)

      #print ('farg ' + str(farg) + ' ' + str(type(farg))) + '\n' + \
      #('*args ' + str(args) + ' ' + str(type(args))) + '\n' + \
      #('**kwargs ' + str(kwargs) + ' ' + str(type(kwargs))).strip()      #this strips off self. and () from the function string.

      tmpStr  = self.processPyCode(fnLst, bypass)
      if verbose:
        print tmpStr
      fnStr = tmpStr + \
"""
  BL()
"""
#"""
#  self.blankLine()
#"""
      try:
        if echo:
          print 'Executing this virtual  function: '
          print fnStr
        #? Can't get threads to work yet. This would need a flag to switch it on or off.
        #self.runThread(fnStr)
        exec(fnStr)
        f = locals()["virtualFunction"](self)
        #self.set('verbose', 0)
      except StandardError:
        error = "command failed: \n" + fnStr + '\n\n'
        print error
        import traceback
        print traceback.format_exc()

    def processPyCode(self, x, bypass, **kwargs):
      """
      Args: list of code strings, mode
      mode 0 inserts def virtualFunction(self): with cr and bumps remaining code strings over 2 spaces.
      mode 1 does not alter the code strings but attempts to execute as is.
      mode 2 strips off newlines from the code strings and attempts to execute it.
      """
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
        M(Sk(), verbose=1, offset=25)
      if kw.has_key('preCmdLst'):
        for command in kw['preCmdLst']:
          exec(command)

      fnStr = ""
      fnLst = []
      if isinstance(x, types.ListType):
        pass
      else:
        fnLst = x.split('\n')
        fnLst.insert(0, "def virtualFunction(self):")
      if bypass == 0:
        #insert def after imports
        fnLst.insert(1, "def virtualFunction(self):")
        for x in range(len(fnLst)):
          if x < 2:
            #build function string
            fnStr = fnStr + fnLst[x] + '\n'
          else:
            #bump remaining code over by two spaces
            fnStr = fnStr + "  " + fnLst[x] + '\n'
      elif bypass == 1:
        fnStr = str(fnLst)
      elif bypass == 2:
        for x in range(len(fnLst)):
          if x == 0:
            fnStr = fnStr.strip() + '\n' + fnLst[x]
          else:
            fnStr = fnStr + '\n  ' + fnLst[x]
      if echo:
        print fnStr
      return fnStr

    def processIncoming(self):
      """
      Handle all the messages currently in the queue (if any).
      """
      while self.queue.qsize():
        try:
          msg = self.queue.get(0)
          # Check contents of message and do what it says
          # As a test, we simply print it
          #print msg
          try:
            self.writeThreadedOutput(msg)
          except NameError:
            print msg
          #self.announce(msg)
        except Queue.Empty:
          pass

'''endfile'''
# Experimental unimplemented code.  Maybe it can be of use.


#    def sleep(self, seconds):
#        #time.sleep(seconds)
#        self.after(int(seconds*1000))
#        return
#        print 'sleep', seconds
#        timeout = int(seconds*1000)
#        self.sleep_var = 0
#        while timeout > 0:
#            self.update()
#            self.update_idletasks()
#            if self.sleep_var:
#                break
#            self.after(100)
#            timeout -= 100
#        print 'finish sleep'
#        return
#        if self.after_id:
#            self.after_cancel(self.after_id)
#        self.after_id = self.after(int(seconds*1000), self._sleepEvent)
#        self.sleep_var.set(1)
#        self.update()
#        self.wait_variable(self.sleep_var)
#        if self.after_id:
#            self.after_cancel(self.after_id)
#            self.after_id = None
#        print 'finish sleep'
#
#    def _sleepEvent(self, *args):
#        return
#        print '_sleepEvent', args
#        self.interruptSleep()
#        return EVENT_PROPAGATE
#
#    def interruptSleep(self):
#        return
#        print 'interruptSleep'
#        self.update()
#        self.update_idletasks()
#        self.sleep_var = 1
#        #self.sleep_var.set(0)
#        #self.after_idle(self.sleep_var.set, 0)
#
#    #
#    #
#    #
#
#    def update(self):
#        Tkinter.Tk.update(self)
#
#    def wmDeleteWindow(self):
#        if self.app and self.app.menubar:
#            self.app.menubar.mQuit()
#        else:
#            ##self.after_idle(self.quit)
#            pass