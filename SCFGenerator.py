# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Tue Dec 02 14:24:57 2014
#      by: PyQt4 UI code generator 4.11.3
# Author: Han Liu 
# Contact: hanangellove@icloud.com
# WARNING! All changes made in this file will be lost!
import os
import re
import string
from xml.etree import ElementTree
from PyQt4 import QtCore, QtGui

LNBTS_ATTRIB_DIC = {'BtsId':0,'CellId':1,'version':'LNT4.0','ADJ_ENBC':0,'ADJ_OAMC':0,'ADJL':0,'ADJW':0,'REL':0,'RELW':0}

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
        Form.setFixedSize(400, 470)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setAutoFillBackground(True)

        self.label_ADJWithEnbControll = QtGui.QLabel(Form)
        self.label_ADJWithEnbControll.setGeometry(QtCore.QRect(80, 150, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ADJWithEnbControll.setFont(font)
        self.label_ADJWithEnbControll.setObjectName(_fromUtf8("label_ADJWithEnbControll"))
        self.label_ADJWithoamControll = QtGui.QLabel(Form)
        self.label_ADJWithoamControll.setGeometry(QtCore.QRect(80, 120, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ADJWithoamControll.setFont(font)
        self.label_ADJWithoamControll.setObjectName(_fromUtf8("label_ADJWithoamControll"))

        self.label_SelectVersion = QtGui.QLabel(Form)
        self.label_SelectVersion.setGeometry(QtCore.QRect(20, 70, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_SelectVersion.setFont(font)
        self.label_SelectVersion.setObjectName(_fromUtf8("label_SelectVersion"))
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
        self.label_ADJW.setGeometry(QtCore.QRect(20, 210, 40, 21))
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
        self.label_RELW.setGeometry(QtCore.QRect(20, 270, 32, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_RELW.setFont(font)
        self.label_RELW.setObjectName(_fromUtf8("label_RELW"))

        self.label_CellId = QtGui.QLabel(Form)
        self.label_CellId.setGeometry(QtCore.QRect(20, 300, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_CellId.setFont(font)
        self.label_CellId.setObjectName(_fromUtf8("label_CellId"))

        self.lineEdit_SourceFilePath = QtGui.QLineEdit(Form)
        self.lineEdit_SourceFilePath.setGeometry(QtCore.QRect(20, 345, 211, 21))
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
        self.lineEdit_TargetFilePath.setGeometry(QtCore.QRect(20, 395, 211, 21))
        self.lineEdit_TargetFilePath.setObjectName(_fromUtf8("lineEdit_TargetFilePath"))
        self.lineEdit_CellId = QtGui.QLineEdit(Form)
        self.lineEdit_CellId.setGeometry(QtCore.QRect(80, 300, 71, 21))
        self.lineEdit_CellId.setObjectName(_fromUtf8("lineEdit_CellId"))

        

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
        self.comboBox.addItem(_fromUtf8(""))
  
        self.pushButton_Exit = QtGui.QPushButton(Form)
        self.pushButton_Exit.setGeometry(QtCore.QRect(250, 430, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Exit.setFont(font)
        self.pushButton_Exit.setObjectName(_fromUtf8("pushButton_Exit"))

        self.pushButton_CreatNewFile = QtGui.QPushButton(Form)
        self.pushButton_CreatNewFile.setGeometry(QtCore.QRect(250, 390, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_CreatNewFile.setFont(font)
        self.pushButton_CreatNewFile.setObjectName(_fromUtf8("pushButton_CreatNewSCF"))

        self.pushButton_SelectSourceSCF = QtGui.QPushButton(Form)
        self.pushButton_SelectSourceSCF.setGeometry(QtCore.QRect(250, 340, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_SelectSourceSCF.setFont(font)
        self.pushButton_SelectSourceSCF.setObjectName(_fromUtf8("pushButton_SelectSourceSCF"))

        self.retranslateUi(Form)

        self.lineEdit_CellId.textChanged.connect(self.onChangeed)
        self.lineEdit_ADJWithEnbControll.textChanged.connect(self.onChangeed)
        self.lineEdit_ADJWithOamControlled.textChanged.connect(self.onChangeed)
        self.lineEdit_ADJL.textChanged.connect(self.onChangeed)
        self.lineEdit_ADJW.textChanged.connect(self.onChangeed)
        self.lineEdit_REL.textChanged.connect(self.onChangeed)
        self.lineEdit_RELW.textChanged.connect(self.onChangeed)

        self.pushButton_SelectSourceSCF.clicked.connect(self.SelectSourceSCF)
        QtCore.QObject.connect(self.pushButton_Exit, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def onChangeed(self,text):

        sender = self.sender()
        senderName = str(sender.objectName())

        try:
            senderText = int(sender.text())
        except ValueError, e:
            if sender.text().isEmpty():
                #judge if the input is empty, to avoid popup messageBox when lineEdit is cleared.
                return 0
            else:
                QtGui.QMessageBox.question(self,'Message',"Here must be a number!")
                sender.clear()
                return 0
        ###################
        #print "sender.objectName is",str(sender.objectName()) 
        #print "sender.text() is ",sender.text() , type(sender.text())
        #print "senderText is:", senderText,type(senderText)
        ####################
        #convert QString u'123' to int 123.
        #print text, type(text)
        #string = unicode(text)      
        #senderText = int(string)
        ####################

        if senderName == "lineEdit_CellId":
            LNBTS_ATTRIB_DIC['CellId'] = senderText
        elif senderName == "lineEdit_ADJWithOamControlled":
            LNBTS_ATTRIB_DIC['ADJ_OAMC'] = senderText
        elif senderName == "lineEdit_ADJWithEnbControll":
            LNBTS_ATTRIB_DIC['ADJ_ENBC'] = senderText
        elif senderName == "lineEdit_ADJL":
            LNBTS_ATTRIB_DIC['ADJL'] = senderText
        elif senderName == "lineEdit_ADJW":
            LNBTS_ATTRIB_DIC['ADJW'] = senderText
        elif senderName == "lineEdit_REL":
            LNBTS_ATTRIB_DIC['REL'] = senderText
        elif senderName == "lineEdit_RELW":
            LNBTS_ATTRIB_DIC['RELW'] = senderText

        #print  LNBTS_ATTRIB_DIC

    def SelectSourceSCF(self):        
        options = QtGui.QFileDialog.DontUseNativeDialog

        filename = QtGui.QFileDialog.getOpenFileName(self,"file",self.lineEdit_SourceFilePath.text(),
            "Text Files (*.xml);;All Files (*)")
        print filename
        if filename:
            self.lineEdit_SourceFilePath.setText(filename)
            oFile = os.path.splitext(str(filename))
            print oFile
            if ".xml" == oFile[1]:
                fh = open(filename,'a+')
                filestring = fh.read()
                # add functions that parse xml File. 
                BtsId_list =  self.parsexml(filestring)
     
                print ""
                print "--------------------------------" 
                print "BtsId is :" , BtsId_list[0]                                                               
                print "LNBTS_ATTRIB_DIC is:", LNBTS_ATTRIB_DIC

                fh.close()

    def parsexml(slef,string):
        xmlstr = string
        rootEleTree = ElementTree.fromstring(xmlstr)
        print rootEleTree.tag, rootEleTree.attrib
        print "================================="
        if 'btsId' in xmlstr:
            print "Find btsId!";
            for childTree in rootEleTree:
                print childTree.tag , childTree.attrib
                for grandsonTree in childTree:
                    #print grandsonTree.tag, grandsonTree.attrib
                    for key in grandsonTree.attrib:
                        if key=='class' and grandsonTree.attrib[key]=='LNBTS':  
                            print str(grandsonTree)                                  
                            print  grandsonTree.attrib
                            LNBTS_ATTRIB_DIC['version'] = grandsonTree.attrib['version']
                            BtsId_list = re.findall(r'[\d\.]+',grandsonTree.attrib['distName'])
                            LNBTS_ATTRIB_DIC['BtsId'] = BtsId_list[0]
                            #print BtsId_list[0]
                            return BtsId_list 


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "SCF Generator", None))
        self.pushButton_Exit.setText(_translate("Form", "Exit", None))
        self.pushButton_CreatNewFile.setText(_translate("Form", "Creat New SCF", None))
        self.pushButton_SelectSourceSCF.setText(_translate("Form", "Select Source SCF", None))

        self.label_ADJWithEnbControll.setText(_translate("Form", "enbControlled", None))
        self.label_SelectVersion.setText(_translate("Form", "Please select the SCF version", None))
        self.label_ADJ.setToolTip(_translate("Form", "Default is oamControll", None))
        self.label_ADJ.setText(_translate("Form", "ADJ", None))
        self.label_ADJL.setToolTip(_translate("Form", "ADJL Amount Per LNADJ", None))
        self.label_ADJL.setText(_translate("Form", "ADJL", None))
        self.label_ADJW.setText(_translate("Form", "ADJW", None))
        self.label_REL.setText(_translate("Form", "REL", None))
        self.label_RELW.setText(_translate("Form", "RELW", None))
        self.label_Welcome.setText(_translate("Form", "Welcome use SCF Generator", None))
        self.label_ADJWithoamControll.setText(_translate("Form", "oamControlled", None))
        self.label_CellId.setText(_translate("Form", "CellId", None))
        
        ###################
        #comboBox has 4 senderTexts.Default is None.If you choose another senderTexts like lNT5.0, then it will be effective during creat new SCF files.
        ###################
        self.comboBox.setItemText(0, _translate("Form", "", None))
        self.comboBox.setItemText(1, _translate("Form", "LNT4.0", None))
        self.comboBox.setItemText(2, _translate("Form", "LNT5.0", None))
        self.comboBox.setItemText(3, _translate("Form", "TL15A", None))

        
        

