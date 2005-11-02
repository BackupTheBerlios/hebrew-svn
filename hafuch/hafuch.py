#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2005/10/22 14:13:31 $"
"""


from PythonCard import model
from PythonCard import dialog

class Hafuch (model.Background):
    
    def on_ToHebBtn_mouseClick(self, event):
        self.components.StaticText2.text = self.components.TextField1.text
        orig_word=self.components.TextField1.text
        dest_word=''
        for x in orig_word:
            if x=='a' or x=='A':
		dest_word=dest_word+unicode('ש','UTF-8')
            elif x=='b' or x=='B':
                dest_word=dest_word+unicode('נ','UTF-8')
            elif x=='c' or x=='C':
                dest_word=dest_word+unicode('ב','UTF-8')
            elif x=='d' or x=='D':
                dest_word=dest_word+unicode('ג','UTF-8')
            elif x=='e' or x=='E':
                dest_word=dest_word+unicode('ק','UTF-8')
            elif x=='f' or x=='F':
                dest_word=dest_word+unicode('כ','UTF-8')
            elif x=='g' or x=='G':
                dest_word=dest_word+unicode('ע','UTF-8')
            elif x=='h' or x=='H':
                dest_word=dest_word+unicode('י','UTF-8')
            elif x=='i' or x=='I':
                dest_word=dest_word+unicode('ן','UTF-8')
            elif x=='j' or x=='J':
                dest_word=dest_word+unicode('ח','UTF-8')
            elif x=='k' or x=='K':
                dest_word=dest_word+unicode('ל','UTF-8')
            elif x=='l' or x=='L':
                dest_word=dest_word+unicode('ך','UTF-8')
            elif x=='m' or x=='M':
                dest_word=dest_word+unicode('צ','UTF-8')
            elif x=='n' or x=='N':
                dest_word=dest_word+unicode('מ','UTF-8')
            elif x=='o' or x=='O':
                dest_word=dest_word+unicode('ם','UTF-8')
            elif x=='p' or x=='P':
                dest_word=dest_word+unicode('פ','UTF-8')
            elif x=='q' or x=='Q':
                dest_word=dest_word+unicode('/','UTF-8')
            elif x=='r' or x=='R':
                dest_word=dest_word+unicode('ר','UTF-8')
            elif x=='s' or x=='S':
                dest_word=dest_word+unicode('ד','UTF-8')
            elif x=='t' or x=='T':
                dest_word=dest_word+unicode('א','UTF-8')
            elif x=='u' or x=='U':
                dest_word=dest_word+unicode('ו','UTF-8')
            elif x=='v' or x=='V':
                dest_word=dest_word+unicode('ה','UTF-8')
            elif x=='w' or x=='W':
                dest_word=dest_word+unicode("'",'UTF-8')
            elif x=='x' or x=='X':
                dest_word=dest_word+unicode('ס','UTF-8')
            elif x=='y' or x=='Y':
                dest_word=dest_word+unicode('ט','UTF-8')
            elif x=='z' or x=='Z':
                dest_word=dest_word+unicode('ז','UTF-8')
            elif x==',' :
                dest_word=dest_word+unicode('ת','UTF-8')
            elif x==';':
                dest_word=dest_word+unicode('ף','UTF-8')
            elif x=='.':
                dest_word=dest_word+unicode('ץ','UTF-8')
            else:    
                dest_word=dest_word+x
        self.components.TextField1.text = dest_word
	self.components.TextField1.setFocus()
    
    def on_ToEngBtn_mouseClick(self, event):
        self.components.StaticText2.text = self.components.TextField1.text
        orig_word=self.components.TextField1.text
        dest_word=''
        for x in orig_word:
            if x==u'\u05d0':
                dest_word=dest_word +'t'
            elif x==u'\u05d1':
                dest_word=dest_word +'c'
            elif x==u'\u05d2':
                dest_word=dest_word +'d'
            elif x==u'\u05d3':
                dest_word=dest_word +'s'
            elif x==u'\u05d4':
                dest_word=dest_word +'v'
            elif x==u'\u05d5':
                dest_word=dest_word +'u'
            elif x==u'\u05d6':
                dest_word=dest_word +'z'
            elif x==u'\u05d7':
                dest_word=dest_word +'j'
            elif x==u'\u05d8':
                dest_word=dest_word +'y'
            elif x==u'\u05d9':
                dest_word=dest_word +'h'
            elif x==u'\u05db':
                dest_word=dest_word +'f'
            elif x==u'\u05da':
                dest_word=dest_word +'l'
            elif x==u'\u05dc':
                dest_word=dest_word +'k'
            elif x==u'\u05de':
                dest_word=dest_word +'n'
            elif x==u'\u05dd':
                dest_word=dest_word +'o'
            elif x==u'\u05e0':
                dest_word=dest_word +'b'
            elif x==u'\u05df':
                dest_word=dest_word +'i'
            elif x==u'\u05e1':
                dest_word=dest_word +'x'
            elif x==u'\u05e2':
                dest_word=dest_word +'g'
            elif x==u'\u05e4':
                dest_word=dest_word +'p'
            elif x==u'\u05e3':
                dest_word=dest_word +';'
            elif x==u'\u05e6':
                dest_word=dest_word +'m'
            elif x==u'\u05e5':
                dest_word=dest_word +'.'
            elif x==u'\u05e7':
                dest_word=dest_word +'e'
            elif x==u'\u05e8':
                dest_word=dest_word +'r'
            elif x==u'\u05e9':
                dest_word=dest_word +'a'
            elif x==u'\u05ea':
                dest_word=dest_word +','
            elif x=='/':
                dest_word=dest_word +'q'
            elif x=="'":
                dest_word=dest_word +'w'
            elif x==".":
                dest_word=dest_word +'/'   
            else:
                dest_word=dest_word+x
        self.components.TextField1.text = dest_word
	self.components.TextField1.setFocus()
              
                
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
	result = dialog.alertDialog(self, 'Hafuch Al Hafuch \n \n Shavit Ilan\n    Ver 0.1', 'About: Hafuch Al Hafuch')
	    
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

