{'application':{'type':'Application',
          'name':'BAHAFUCHA',
    'backgrounds': [
    {'type':'Background',
          'name':'bgMin',
          'title':'Bahafucha',
          'size':(416, 213),

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
    'name':'PasteBtn', 
    'position':(292, 80), 
    'size':(70, -1), 
    'font':{'faceName': u'Sans', 'size': 12}, 
    'label':'Paste', 
    },

{'type':'Button', 
    'name':'CopyBtn', 
    'position':(210, 80), 
    'size':(70, -1), 
    'font':{'faceName': u'Sans', 'size': 12}, 
    'label':'Copy', 
    },

{'type':'Button', 
    'name':'ExitBtn', 
    'position':(292, 126), 
    'size':(70, -1), 
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
    'position':(210, 126), 
    'size':(70, -1), 
    'font':{'faceName': u'Sans', 'size': 12}, 
    'label':'Mirror', 
    },

{'type':'Button', 
    'name':'UndoBtn', 
    'position':(128, 126), 
    'size':(70, -1), 
    'font':{'faceName': u'Sans', 'size': 12}, 
    'label':'Undo', 
    },

{'type':'Button', 
    'name':'ResetBtn', 
    'position':(46, 126), 
    'size':(70, -1), 
    'font':{'faceName': u'Sans', 'size': 12}, 
    'label':'Clear', 
    },

{'type':'Button', 
    'name':'InvertBtn', 
    'position':(46, 80), 
    'size':(151, -1), 
    'font':{'faceName': u'Sans', 'size': 12}, 
    'label':'Invert', 
    },

{'type':'TextField', 
    'name':'TextField1', 
    'position':(46, 9), 
    'size':(317, 56), 
    'backgroundColor':(229, 228, 220), 
    'font':{'faceName': u'Sans', 'size': 12}, 
    },

] # end components
} # end background
] # end backgrounds
} }
