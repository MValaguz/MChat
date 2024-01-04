# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MChat_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MChat_window(object):
    def setupUi(self, MChat_window):
        MChat_window.setObjectName("MChat_window")
        MChat_window.resize(332, 406)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MChat_window.sizePolicy().hasHeightForWidth())
        MChat_window.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/MChat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MChat_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MChat_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(7, 4, 7, 5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.e_invia_messaggio = QtWidgets.QLineEdit(self.centralwidget)
        self.e_invia_messaggio.setObjectName("e_invia_messaggio")
        self.verticalLayout_3.addWidget(self.e_invia_messaggio)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.o_messaggi = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.o_messaggi.sizePolicy().hasHeightForWidth())
        self.o_messaggi.setSizePolicy(sizePolicy)
        self.o_messaggi.setObjectName("o_messaggi")
        self.verticalLayout_2.addWidget(self.o_messaggi)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MChat_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MChat_window)
        self.statusbar.setObjectName("statusbar")
        MChat_window.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MChat_window)
        self.toolBar.setIconSize(QtCore.QSize(30, 20))
        self.toolBar.setObjectName("toolBar")
        MChat_window.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtWidgets.QMenuBar(MChat_window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 332, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuAs_Server = QtWidgets.QMenu(self.menuBar)
        self.menuAs_Server.setObjectName("menuAs_Server")
        self.menuAs_Client = QtWidgets.QMenu(self.menuBar)
        self.menuAs_Client.setObjectName("menuAs_Client")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MChat_window.setMenuBar(self.menuBar)
        self.actionClear_my_chat = QtWidgets.QAction(MChat_window)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/clear.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClear_my_chat.setIcon(icon1)
        self.actionClear_my_chat.setObjectName("actionClear_my_chat")
        self.actionReduce_to_systray = QtWidgets.QAction(MChat_window)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/systray.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReduce_to_systray.setIcon(icon2)
        self.actionReduce_to_systray.setObjectName("actionReduce_to_systray")
        self.actionProgram_Info = QtWidgets.QAction(MChat_window)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/info.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProgram_Info.setIcon(icon3)
        self.actionProgram_Info.setObjectName("actionProgram_Info")
        self.actionHelp = QtWidgets.QAction(MChat_window)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/help.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon4)
        self.actionHelp.setObjectName("actionHelp")
        self.actionSplash_window = QtWidgets.QAction(MChat_window)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/dexclamation.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSplash_window.setIcon(icon5)
        self.actionSplash_window.setObjectName("actionSplash_window")
        self.actionPreferences = QtWidgets.QAction(MChat_window)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/gears.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreferences.setIcon(icon6)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionStart_as_server = QtWidgets.QAction(MChat_window)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/create_server.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStart_as_server.setIcon(icon7)
        self.actionStart_as_server.setObjectName("actionStart_as_server")
        self.actionClient_connection = QtWidgets.QAction(MChat_window)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/call.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClient_connection.setIcon(icon8)
        self.actionClient_connection.setObjectName("actionClient_connection")
        self.toolBar.addAction(self.actionStart_as_server)
        self.toolBar.addAction(self.actionClient_connection)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPreferences)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClear_my_chat)
        self.toolBar.addAction(self.actionReduce_to_systray)
        self.toolBar.addAction(self.actionSplash_window)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionProgram_Info)
        self.menuBar.addAction(self.menuAs_Server.menuAction())
        self.menuBar.addAction(self.menuAs_Client.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.label_2.setBuddy(self.e_invia_messaggio)
        self.label.setBuddy(self.o_messaggi)

        self.retranslateUi(MChat_window)
        self.e_invia_messaggio.returnPressed.connect(MChat_window.slot_invia_il_messaggio) # type: ignore
        self.actionProgram_Info.triggered.connect(MChat_window.slot_program_info) # type: ignore
        self.actionHelp.triggered.connect(MChat_window.slot_visualizza_help) # type: ignore
        self.actionPreferences.triggered.connect(MChat_window.slot_preferences) # type: ignore
        self.actionClear_my_chat.triggered.connect(MChat_window.slot_pulisci_chat) # type: ignore
        self.actionStart_as_server.triggered.connect(MChat_window.slot_crea_server_chat) # type: ignore
        self.actionReduce_to_systray.triggered.connect(MChat_window.slot_riduci_a_systray) # type: ignore
        self.actionSplash_window.triggered.connect(MChat_window.slot_splash_window) # type: ignore
        self.actionClient_connection.triggered.connect(MChat_window.slot_crea_client_chat) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MChat_window)
        MChat_window.setTabOrder(self.o_messaggi, self.e_invia_messaggio)

    def retranslateUi(self, MChat_window):
        _translate = QtCore.QCoreApplication.translate
        MChat_window.setWindowTitle(_translate("MChat_window", "MChat 1.3"))
        self.label_2.setText(_translate("MChat_window", "Send:"))
        self.label.setText(_translate("MChat_window", "Messages:"))
        self.toolBar.setWindowTitle(_translate("MChat_window", "toolBar"))
        self.menuAs_Server.setTitle(_translate("MChat_window", "Server"))
        self.menuAs_Client.setTitle(_translate("MChat_window", "Client"))
        self.menuHelp.setTitle(_translate("MChat_window", "Help"))
        self.actionClear_my_chat.setText(_translate("MChat_window", "Clear my chat"))
        self.actionClear_my_chat.setToolTip(_translate("MChat_window", "Clear my chat (F1 shortcut key)"))
        self.actionClear_my_chat.setShortcut(_translate("MChat_window", "F1"))
        self.actionReduce_to_systray.setText(_translate("MChat_window", "Reduce to systray"))
        self.actionReduce_to_systray.setToolTip(_translate("MChat_window", "Reduce to systray (F2 shortcut key)"))
        self.actionReduce_to_systray.setShortcut(_translate("MChat_window", "F2"))
        self.actionProgram_Info.setText(_translate("MChat_window", "Program Info"))
        self.actionProgram_Info.setToolTip(_translate("MChat_window", "Program Info"))
        self.actionHelp.setText(_translate("MChat_window", "Help"))
        self.actionHelp.setToolTip(_translate("MChat_window", "Help"))
        self.actionSplash_window.setText(_translate("MChat_window", "Splash window"))
        self.actionSplash_window.setToolTip(_translate("MChat_window", "Activate/Deactivate splash window when a new message was received (F3 shortcut key)"))
        self.actionSplash_window.setShortcut(_translate("MChat_window", "F3"))
        self.actionPreferences.setText(_translate("MChat_window", "Preferences"))
        self.actionPreferences.setToolTip(_translate("MChat_window", "Preferences"))
        self.actionPreferences.setShortcut(_translate("MChat_window", "F3"))
        self.actionStart_as_server.setText(_translate("MChat_window", "Start as server"))
        self.actionStart_as_server.setToolTip(_translate("MChat_window", "Starts MCat waiting for a user connection"))
        self.actionClient_connection.setText(_translate("MChat_window", "Client connection"))
        self.actionClient_connection.setToolTip(_translate("MChat_window", "Connect to a MChat server "))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MChat_window = QtWidgets.QMainWindow()
    ui = Ui_MChat_window()
    ui.setupUi(MChat_window)
    MChat_window.show()
    sys.exit(app.exec_())