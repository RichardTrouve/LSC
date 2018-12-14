import maya.cmds as cmds
import maya.OpenMayaUI as omui
from functools import partial


from PySide2 import QtWidgets
from PySide2 import QtGui, QtCore
from shiboken2 import wrapInstance

import maya.OpenMaya as om

import LSCUi
reload (LSCUi)


def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)

class ControlMainWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Tool)
        self.ui = LSCUi.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.checkerListWidget.installEventFilter(self)
        self.passedIcon = QtGui.QIcon()
        self.passedIcon.addPixmap(QtGui.QPixmap(":/icons/mark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nopassedIcon = QtGui.QIcon()
        self.nopassedIcon.addPixmap(QtGui.QPixmap(":/icons/nomark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.neutralIcon = QtGui.QIcon()
        self.neutralIcon.addPixmap(QtGui.QPixmap(":/icons/neutral.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.ui.checkerListWidget.item(1).setIcon(passedIcon)
    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.ContextMenu and
            source is self.ui.checkerListWidget):
            item = source.itemAt(event.pos())
            menu = QtWidgets.QMenu()

            if item.text() == 'Delete history':
                self.historyCheckercall(menu,event,source)

            if item.text() == 'world':
                self.test2(menu,event,source)    

            return True
        return super(ControlMainWindow, self).eventFilter(source, event)
#---------------------------------------------

    def historyCheckercall(self,menu,event,source):
        menu.addAction("delete all history",(self.deleteAllHistory))
        menu.addSeparator()
        menu.addAction("reset",(self.reset))
        if menu.exec_(event.globalPos()):
            item = source.itemAt(event.pos())
           
    def test2(self,menu,event,source):
        menu.addAction("set passed",(self.test3))
        menu.addAction("set not passed")
        if menu.exec_(event.globalPos()):
            item = source.itemAt(event.pos())


    def deleteAllHistory(self):

        ObjectsInScene = cmds.ls()

        for i in ObjectsInScene:
            cmds.delete( all=True, constructionHistory=True )
            
        self.ui.checkerListWidget.item(0).setIcon(self.passedIcon)


    def reset(self):
        print ('reset current item icon')
        print ('reset all items icon')



def run():

    global win
    try:
        win.close()
        win.deleteLater()

    except: 
        pass

    win = ControlMainWindow(parent=maya_main_window())
    win.show()