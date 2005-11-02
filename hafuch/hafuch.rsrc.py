{'application':{'type':'Application',
          'name':'Hfuch Al Hafuch',
    'backgrounds': [
    {'type':'Background',
          'name':'bgMin',
          'title':'Hfuch  Al  Hafuch',
          'size':(457, 273),

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':u'E&xit\tAlt+X',
                   'command':'exit',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuEdit',
             'label':u'&Edit',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuEditCopy',
                   'label':u'&Copy\tCtrl+C',
                  },
                  {'type':'MenuItem',
                   'name':'menuEditPaste',
                   'label':u'&Paste\tCtrl+V',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuHelp',
             'label':u'&Help',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuHelpAbout',
                   'label':u'About',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'Button', 
    'name':'ExitBtn', 
    'position':(307, 176), 
    'font':{'faceName': u'Sans', 'size': 12}, 
    'label':'Exit', 
    },

{'type':'StaticText', 
    'name':'StaticText2', 
    'position':(10, 251), 
    'backgroundColor':(239, 235, 231), 
    'text':'StaticText', 
    'visible':False, 
    },

{'type':'Button', 
    'name':'MirrorBtn', 
    'position':(225, 176), 
    'size':(70, -1), 
    'font':{'faceName': u'Sans', 'size': 12}, 
    'label':'Mirror', 
    },

{'type':'Button', 
    'name':'UndoBtn', 
    'position':(143, 176), 
    'size':(70, -1), 
    'font':{'faceName': u'Sans', 'size': 12}, 
    'label':'Undo', 
    },

{'type':'Button', 
    'name':'ResetBtn', 
    'position':(61, 175), 
    'size':(70, -1), 
    'font':{'faceName': u'Sans', 'size': 12}, 
    'label':'Clear', 
    },

{'type':'Button', 
    'name':'ToEngBtn', 
    'position':(61, 127), 
    'size':(331, -1), 
    'font':{'faceName': u'Sans', 'size': 12}, 
    'label':'English <--- Hebrew', 
    },

{'type':'Button', 
    'name':'ToHebBtn', 
    'position':(61, 80), 
    'size':(331, -1), 
    'font':{'faceName': u'Sans', 'size': 12}, 
    'label':'Hebrew <--- English', 
    },

{'type':'TextField', 
    'name':'TextField1', 
    'position':(61, 9), 
    'size':(331, 56), 
    'font':{'faceName': u'Sans', 'size': 12}, 
    },

] # end components
} # end background
] # end backgrounds
} }
