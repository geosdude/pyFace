#!/bin/bash
# -*- codign:utf-8 -*-
# pyface.output.py
# Coded by Richard Polk
#----------------------------------------------------

class GUI_Output():

  def __init__(self):
    self.stderr = None
    self.stdout = None

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
