#!venv/bin/python

# This Python file uses the following encoding: utf-8
import sys
import os, json

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import QEvent, QMargins, QUrl, Qt
from PySide6.QtWebEngineWidgets import QWebEngineView

# Important:
# You need to run the following command to generate the ui_form.py file
#     venv/bin/pyside6-uic form.ui -o ui_form.py
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
# os.system("venv/bin/pyside6-uic form.ui -o ui_form.py")

from ui_form import Ui_TestWindow

class AnswerView(QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.borderSize = 5
        marging=QMargins(self.borderSize, self.borderSize, self.borderSize, self.borderSize)
        styleStr = '''
                    QWebEngineView:hover {
                        border: %dpx solid blue;
                    }
                    ''' % (self.borderSize)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setAttribute(Qt.WA_Hover, True)
        self.setContentsMargins(marging)
        self.setStyleSheet(styleStr)
 

class TestWindow(QDialog):
    def __init__(self, parent=None, question=None):
        super().__init__(parent)
        self.ui = Ui_TestWindow()
        self.ui.setupUi(self)
        self.setObjectName('TestWindow')
        self.setupQuestion(question)
        

    def setupQuestion(self, question):
        self.borderSize = 5
        marging=QMargins(self.borderSize, self.borderSize, self.borderSize, self.borderSize)
        (qwe,ans) = decode_question(question)
       
        view = QWebEngineView()
        view.setContentsMargins(marging)
        view.setUrl(qwe)
        self.qwe=view
        self.ui.QweLayout.addWidget(self.qwe)
 
        self.ans = []
        self.ans_obj = []
        for a in ans:
            view = AnswerView()
            view.setUrl(a)
            self.ans.append(view)
            self.ui.AnsLayout.addWidget(view)
            focusProxy = view.focusProxy()
            self.ans_obj.append(focusProxy)
            focusProxy.installEventFilter(self)

                        
    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonDblClick:
            selectedAnswer = self.ans_obj.index(obj)+1
            self.done(selectedAnswer)
            return True
        return super().eventFilter(obj, event)


def decode_question(question):
    return (question[0], question[1])

def readConfig(fName):
    f = open(fName, mode='r')
    questions = json.load(f)
    f.close()
    return questions


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow=QMainWindow()
    MainWindow.show()
    question = (QUrl(u"file:///home/jack/devel/mgg-test/files/mzhg1/4.html"),
                [QUrl(u"file:///home/jack/devel/mgg-test/files/mzhg1/4.1.html"),
                QUrl(u"file:///home/jack/devel/mgg-test/files/mzhg1/4.2.html"),
                QUrl(u"file:///home/jack/devel/mgg-test/files/mzhg1/4.3.html")])

    baseUrl=QUrl("file:///home/jack/devel/mgg-test/files/mzhg1/")
    confFile = 'mgg1.json'
    questions = readConfig(confFile)
    for q in questions:
        qName = baseUrl.resolved(QUrl(q['qwe']['fName']))
        aNames = []
        for ans in q['ans']:
            aNames.append(baseUrl.resolved(QUrl(ans['fName'])))

        question = (qName, aNames)
        dialog = TestWindow(MainWindow, question)
        result = dialog.exec()
        print(result)
        if result==0:
            break
    sys.exit(app.exec())
