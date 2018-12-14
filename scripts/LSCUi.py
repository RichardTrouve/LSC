import res_rc

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(230, 446)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkerListWidget = QtWidgets.QListWidget(Dialog)
        self.checkerListWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkerListWidget.setAlternatingRowColors(True)
        self.checkerListWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.checkerListWidget.setIconSize(QtCore.QSize(30, 30))
        self.checkerListWidget.setSpacing(2)
        self.checkerListWidget.setUniformItemSizes(False)
        self.checkerListWidget.setSelectionRectVisible(False)
        self.checkerListWidget.setObjectName("checkerListWidget")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/neutral.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item = QtWidgets.QListWidgetItem(self.checkerListWidget)
        item.setIcon(icon)
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        item = QtWidgets.QListWidgetItem(self.checkerListWidget)
        item.setIcon(icon)
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.checkerListWidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Local Sanity Checker", None, -1))
        __sortingEnabled = self.checkerListWidget.isSortingEnabled()
        self.checkerListWidget.setSortingEnabled(False)
        self.checkerListWidget.item(0).setText(QtWidgets.QApplication.translate("Dialog", "Delete history", None, -1))
        self.checkerListWidget.item(1).setText(QtWidgets.QApplication.translate("Dialog", "and many more to come", None, -1))
        self.checkerListWidget.setSortingEnabled(__sortingEnabled)


