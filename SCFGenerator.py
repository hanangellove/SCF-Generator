# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Tue Dec 02 14:24:57 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import os
from xml.etree import ElementTree
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(393, 449)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setAutoFillBackground(True)

        self.label_ADJWithEnbControll = QtGui.QLabel(Form)
        self.label_ADJWithEnbControll.setGeometry(QtCore.QRect(80, 150, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ADJWithEnbControll.setFont(font)
        self.label_ADJWithEnbControll.setObjectName(_fromUtf8("label_ADJWithEnbControll"))
        self.label_CellID = QtGui.QLabel(Form)
        self.label_CellID.setGeometry(QtCore.QRect(20, 70, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_CellID.setFont(font)
        self.label_CellID.setObjectName(_fromUtf8("label_CellID"))
        self.label_ADJ = QtGui.QLabel(Form)
        self.label_ADJ.setGeometry(QtCore.QRect(20, 120, 31, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ADJ.setFont(font)
        self.label_ADJ.setObjectName(_fromUtf8("label_ADJ"))
        self.label_ADJL = QtGui.QLabel(Form)
        self.label_ADJL.setGeometry(QtCore.QRect(20, 180, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ADJL.setFont(font)
        self.label_ADJL.setObjectName(_fromUtf8("label_ADJL"))
        self.label_ADJW = QtGui.QLabel(Form)
        self.label_ADJW.setGeometry(QtCore.QRect(20, 210, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ADJW.setFont(font)
        self.label_ADJW.setObjectName(_fromUtf8("label_ADJW"))
        self.label_REL = QtGui.QLabel(Form)
        self.label_REL.setGeometry(QtCore.QRect(20, 240, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_REL.setFont(font)
        self.label_REL.setObjectName(_fromUtf8("label_REL"))
        self.label_RELW = QtGui.QLabel(Form)
        self.label_RELW.setGeometry(QtCore.QRect(20, 270, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_RELW.setFont(font)
        self.label_RELW.setObjectName(_fromUtf8("label_RELW"))

        self.lineEdit_SourceFilePath = QtGui.QLineEdit(Form)
        self.lineEdit_SourceFilePath.setGeometry(QtCore.QRect(20, 320, 211, 31))
        self.lineEdit_SourceFilePath.setObjectName(_fromUtf8("lineEdit_SourceFilePath"))
        self.lineEdit_ADJWithEnbControll = QtGui.QLineEdit(Form)
        self.lineEdit_ADJWithEnbControll.setGeometry(QtCore.QRect(210, 150, 71, 21))
        self.lineEdit_ADJWithEnbControll.setObjectName(_fromUtf8("lineEdit_ADJWithEnbControll"))
        self.lineEdit_ADJWithOamControlled = QtGui.QLineEdit(Form)
        self.lineEdit_ADJWithOamControlled.setGeometry(QtCore.QRect(210, 120, 71, 21))
        self.lineEdit_ADJWithOamControlled.setText(_fromUtf8(""))
        self.lineEdit_ADJWithOamControlled.setObjectName(_fromUtf8("lineEdit_ADJWithOamControlled"))
        self.lineEdit_ADJL = QtGui.QLineEdit(Form)
        self.lineEdit_ADJL.setGeometry(QtCore.QRect(80, 180, 71, 21))
        self.lineEdit_ADJL.setObjectName(_fromUtf8("lineEdit_ADJL"))
        self.lineEdit_ADJW = QtGui.QLineEdit(Form)
        self.lineEdit_ADJW.setGeometry(QtCore.QRect(80, 210, 71, 21))
        self.lineEdit_ADJW.setObjectName(_fromUtf8("lineEdit_ADJW"))
        self.lineEdit_REL = QtGui.QLineEdit(Form)
        self.lineEdit_REL.setGeometry(QtCore.QRect(80, 240, 71, 21))
        self.lineEdit_REL.setObjectName(_fromUtf8("lineEdit_REL"))
        self.lineEdit_RELW = QtGui.QLineEdit(Form)
        self.lineEdit_RELW.setGeometry(QtCore.QRect(80, 270, 71, 21))
        self.lineEdit_RELW.setObjectName(_fromUtf8("lineEdit_RELW"))
        self.lineEdit_TargetFilePath = QtGui.QLineEdit(Form)
        self.lineEdit_TargetFilePath.setGeometry(QtCore.QRect(20, 370, 211, 31))
        self.lineEdit_TargetFilePath.setObjectName(_fromUtf8("lineEdit_TargetFilePath"))

        self.label_Welcome = QtGui.QLabel(Form)
        self.label_Welcome.setGeometry(QtCore.QRect(70, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Welcome.setFont(font)
        self.label_Welcome.setObjectName(_fromUtf8("label_Welcome"))

        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(210, 70, 69, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))

        self.label_ADJWithoamControll = QtGui.QLabel(Form)
        self.label_ADJWithoamControll.setGeometry(QtCore.QRect(80, 120, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ADJWithoamControll.setFont(font)
        self.label_ADJWithoamControll.setObjectName(_fromUtf8("label_ADJWithoamControll"))
        
        self.pushButton_Exit = QtGui.QPushButton(Form)
        self.pushButton_Exit.setGeometry(QtCore.QRect(250, 410, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Exit.setFont(font)
        self.pushButton_Exit.setObjectName(_fromUtf8("pushButton_Exit"))

        self.pushButton_CreatNewFile = QtGui.QPushButton(Form)
        self.pushButton_CreatNewFile.setGeometry(QtCore.QRect(250, 370, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_CreatNewFile.setFont(font)
        self.pushButton_CreatNewFile.setObjectName(_fromUtf8("pushButton_CreatNewSCF"))

        self.pushButton_SelectSourceSCF = QtGui.QPushButton(Form)
        self.pushButton_SelectSourceSCF.setGeometry(QtCore.QRect(250, 320, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_SelectSourceSCF.setFont(font)
        self.pushButton_SelectSourceSCF.setObjectName(_fromUtf8("pushButton_SelectSourceSCF"))

        

        self.retranslateUi(Form)
        self.pushButton_SelectSourceSCF.clicked.connect(self.SelectSourceSCF)
        QtCore.QObject.connect(self.pushButton_Exit, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def SelectSourceSCF(self):
        options = QtGui.QFileDialog.DontUseNativeDialog
        print options

        filename = QtGui.QFileDialog.getOpenFileName(self,"file",self.lineEdit_SourceFilePath.text(),
            "Text Files (*.xml);;All Files (*)")
        print filename
        if filename:
            self.lineEdit_SourceFilePath.setText(filename)
            oFile = os.path.splitext(str(filename))
            eleTree = ElementTree.fromstring(filename)
            if ".xml" == oFile[1]:
                fh = open(filename,'a+')
                cstr = fh.read()#Need to add functions that parse xml File. 

                if 'btsId' in cstr:
                    print "Find btsId!";
                    node_child = eleTree.Find('btsId')
                    print node_child
                fh.close()


        


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "SCF Generator", None))
        self.pushButton_Exit.setText(_translate("Form", "Exit", None))
        self.pushButton_CreatNewFile.setText(_translate("Form", "Creat New SCF", None))
        self.pushButton_SelectSourceSCF.setText(_translate("Form", "Select Source SCF", None))

        self.label_ADJWithEnbControll.setText(_translate("Form", "enbControlled", None))
        self.label_CellID.setText(_translate("Form", "Please select the SCF version", None))
        self.label_ADJ.setToolTip(_translate("Form", "Default is oamControll", None))
        self.label_ADJ.setText(_translate("Form", "ADJ", None))
        self.label_ADJL.setToolTip(_translate("Form", "ADJL Amount Per LNADJ", None))
        self.label_ADJL.setText(_translate("Form", "ADJL", None))
        self.label_ADJW.setText(_translate("Form", "ADJW", None))
        self.label_REL.setText(_translate("Form", "REL", None))
        self.label_RELW.setText(_translate("Form", "RELW", None))
        self.label_Welcome.setText(_translate("Form", "Welcome use SCF Generator", None))
        self.label_ADJWithoamControll.setText(_translate("Form", "oamControlled", None))

        self.comboBox.setItemText(0, _translate("Form", "LNT4.0", None))
        self.comboBox.setItemText(1, _translate("Form", "LNT5.0", None))
        self.comboBox.setItemText(2, _translate("Form", "TL15A", None))

        
        

