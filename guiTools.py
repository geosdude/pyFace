#!/bin/bash
# -*- codign:utf-8 -*-
# pyFace.guiVars.GUI_Tools
# Coded by Richard Polk, Jr
#
#----------------------------------------------------


class GUI_Tools():

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
