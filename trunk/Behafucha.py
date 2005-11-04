#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
__version__ = "$Revision: 0.2 $"
__date__ = "$Date: 2005/10/22 14:13:31 $"
"""
# changelog:
#  Ver 0.2:          (4.11.2005)
#  Changing the name of the software to "Bahafucha"
#  Creating only one button called "Invert" instead of 2 separate buttons
#  Adding Copy + Paste Button
#  Cancel "ugly" code (elsif sequences...) and use dictionary structure instead
#  Changing the display background colour
#  Replacing the host project server to berlios
#  Adding automatic language recognition
#  Adding 'Behaficha.png' icon
#  Focus on the Textbox when launching the software (ready for typing or paste command)
   

from PythonCard import model
from PythonCard import dialog

class Hafuch (model.Background):
    
    def on_initialize(self, event):
        self.components.TextField1.setFocus()
        
    def on_InvertBtn_mouseClick(self, event):
        Eng2Heb= {"a":"ש","b":"נ","c":"ב","d":"ג","e":"ק","f":"כ","g":"ע","h":"י","i":"ן","j":"ח","k":"ל","l":"ך","m":"צ","n":"מ","o":"ם","p":"פ","q":"/","r":"ר","s":"ד","t":"א","u":"ו","v":"ה","w":"'","x":"ס","y":"ט","z":"ז","A":"ש","B":"נ","C":"ב","D":"ג", "E":"ק","F":"כ","G":"ע","H":"י","I":"ן","J":"ח","K":"ל","L":"ך","M":"צ","N":"מ","O":"ם","P":"פ","Q":"/","R":"ר","S":"ד","T":"א","U":"ו","V":"ה","W":"'","X":"ס","Y":"ט","Z":"ז",";":"ף",".":"ץ",",":"ת"}
        Heb2Eng= {u'א':'t',u'ב':'c',u'ג':'d',u'ד':'s',u'ה':'v',u'ו':'u',u'ז':'z',u'ח':'j',u'ט':'y',u'י':'h',u'כ':'f',u'ל':'k',u'מ':'n',u'נ':'b',u'ס':'x',u'ע':'g',u'פ':'p',u'צ':'m',u'ק':'e',u'ר':'r',u'ש':'a',u'ת':',','/':'q',".":'q',u'ף':';',u'ץ':'.','.':'/',"'":'w',u'ם':'o',u'ך':'l',u'ן':'i'}
        self.components.StaticText2.text = self.components.TextField1.text
        orig_word=self.components.TextField1.text
        dest_word=''
        try:
            test_lang=Eng2Heb[orig_word[0]]
            lang="English"
        except:
            lang="Hebrew"
        
        if lang=="English":
            for index in orig_word:
                try:
                    dest_word=dest_word+unicode(Eng2Heb[index],'UTF-8')
                except:
                    dest_word=dest_word+index
        elif lang=="Hebrew":
            for index in orig_word:
                try:
                    dest_word=dest_word+Heb2Eng[index]
                except:
                   dest_word=dest_word+index
                   
        self.components.TextField1.text = dest_word
        self.components.TextField1.setFocus()
     
    def on_CopyBtn_mouseClick(self, event):
        self.components.TextField1.setFocus()
        widget = self.findFocus()
        if hasattr(widget, 'editable') and widget.canCopy():
            widget.copy()
    
    def on_PasteBtn_mouseClick(self, event):
        self.components.TextField1.setFocus()
        widget = self.findFocus()
        if hasattr(widget, 'editable') and widget.canPaste():
            widget.paste()
    
    def on_ResetBtn_mouseClick(self, event):
        self.components.StaticText2.text = self.components.TextField1.text
        self.components.TextField1.text = ''
        self.components.TextField1.setFocus()
        
    def on_UndoBtn_mouseClick(self, event):
        self.components.TextField1.text = self.components.StaticText2.text
        self.components.TextField1.setFocus()
        
    def on_MirrorBtn_mouseClick(self, event):
        self.components.StaticText2.text = self.components.TextField1.text
        orig_word = self.components.TextField1.text
        mirror_word=''
        i=len(orig_word) -1
        j=0
        while i>=0:
            mirror_word=mirror_word+orig_word[i]
            i=i-1
            j=j+1
        self.components.TextField1.text = mirror_word
        self.components.TextField1.setFocus()
    
    def on_ExitBtn_mouseClick(self, event):
        self.Close()

    def on_menuHelpAbout_select(self,event):
        result = dialog.alertDialog(self, '           Behafucha - Ver 0.2 / Shavit Ilan\n\n https://developer.berlios.de/projects/hebrew', 'About: Hafuch Al Hafuch')
	    
    def on_menuEditCopy_select(self,event):
        self.components.TextField1.setFocus()
        widget = self.findFocus()
        if hasattr(widget, 'editable') and widget.canCopy():
            widget.copy()
    
    def on_menuEditPaste_select(self,event):
        self.components.TextField1.setFocus()
        widget = self.findFocus()
        if hasattr(widget, 'editable') and widget.canPaste():
            widget.paste()


if __name__ == '__main__':
    app = model.Application(Hafuch)
    app.MainLoop()

