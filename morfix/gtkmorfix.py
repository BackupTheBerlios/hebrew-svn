#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
morfix gtk interface

@copyright: Copyright 2004 by omri <omri.il@gmail.com>
@license: GNU GPL, see COPYING for details
"""

import sys

try:
	import gtk
except ImportError:
	print "PyGTK is not installed, install PyGTK and try again"
	sys.exit(1)

import pango

from morfix import translate

data = [] # We want these to be global
configuration = []

def set_configuration(config_file):
	global configuration
	configuration = __import__(config_file, globals(), locals(), [])

def texttag(name, **properties):
	ret = gtk.TextTag(name)
	for property in properties:
		ret.set_property(property, properties[property])
	return ret

def destroy(window):
	gtk.main_quit()

def about(button, data):
	dialog = gtk.Dialog("About")
	dialog.set_border_width(10)

	close_button = gtk.Button("close")
	dialog.action_area.pack_start(close_button, gtk.TRUE, gtk.TRUE, 0)
	close_button.connect_object("clicked", lambda wid: wid.destroy(), dialog)
	close_button.show()
	
	about_label = gtk.Label("""About
-----------


This is a program for hebrew-english and vice versa translation.


copyright: Copyright 2004 by omri <omri.il@gmail.com>.
license: GNU GPL.""") #TODO: put the needed information here (in an HTML widget, if possible).   (Ofer Waldman)
	dialog.vbox.pack_start(about_label, gtk.TRUE, gtk.TRUE, 0)
	about_label.show()

	dialog.show()
	

def toggle_auto_trans(event, data):
	global configuration
	configuration.automatic_translation = data.get_active()

def clipboard_translate(event, data):
	if configuration.automatic_translation:
		word.get_buffer().set_text("")
		word.get_buffer().set_text(clipboard.wait_for_text())

		trans_click(None)
	
#TODO UImanager should be used here in the future, once pygtk 2.4 becomes standard (Ofer Waldman)
def get_menu(window, menu_data):
	global item_factory   #for some reason the item_factory must not be destroyed with the function
	accel_group = gtk.AccelGroup()
	item_factory = gtk.ItemFactory(gtk.MenuBar, "<main>", accel_group)
	print menu_data
	item_factory.create_items(menu_data)
	window.add_accel_group(accel_group)

	return item_factory.get_widget("<main>")
	

def select_font(button, data):
	font_dialog = gtk.FontSelectionDialog("Font Selection Dialog")
	font_dialog.ok_button.connect("clicked", font_selection_ok, font_dialog)
	font_dialog.cancel_button.connect_object("clicked", lambda wid: wid.destroy(), font_dialog)
	font_dialog.show()

def font_selection_ok(button, font_dialog):  # was that procedural programming in python? damn :)... (Ofer Waldman)
	chosen_font = font_dialog.get_font_name()
	if window:
		word.get_settings().set_string_property('gtk-font-name', chosen_font, '');
		font_dialog.destroy() 

def trans_click_in_textbox(widget, event):
		Enter = 65293	  #65293 is the Enter key value (Ofer Waldman)
		if event.keyval == Enter:  
				trans_click(widget)
				return True   #Do not propagate the "enter" key. it is used for translating, not for entering a new line.
		
		return False

def trans_click(widget):
	combo.set_popdown_strings([])
	
	global data  #the translated data. why is it global? (Ofer Waldman)
	word_to_translate = word.get_buffer().get_text(word.get_buffer().get_start_iter(), word.get_buffer().get_end_iter())
	#note: the intensive use of word.get_buffer() here shows that using a buffer variable might be desirable (Ofer Waldman)
	data = translate(word_to_translate)
	
	if len(data) == 0:
		translation.set_text('')
		translation.insert_with_tags_by_name(translation.get_end_iter(), "Unable to find \"%s\" !\n" % (word_to_translate), 'error')
		return
	
	keys = [i[0] for i in data]
	combo.set_popdown_strings(keys)
	select_click()

def select_click(entry=None):
	solution = combo.entry.get_text().decode('utf-8')
	
	keys = [i[0] for i in data]
	if not solution in [i[0] for i in data]:
		return
	
	item = data[keys.index(solution)][1]
	
	translation.set_text('')
	translation.insert_with_tags_by_name(translation.get_end_iter(), 'matches for "%s":\n'.encode('utf-8') % (solution), 'matches_for')
	for match in item:
		translation.insert_with_tags_by_name(translation.get_end_iter(), '%(word)s (%(type)s):\n%(translation)s\n'.encode('utf-8') % match, 'match')


#==========main=============

#reading the configuration
set_configuration("morfix_conf")

clipboard = gtk.Clipboard(gtk.gdk.display_get_default(), "PRIMARY")

window = gtk.Window()
window.set_position(gtk.WIN_POS_CENTER)
window.set_title("מילון מורפיקס")
window.set_border_width(10)
window.connect('destroy', destroy)
window.connect('focus-in-event', clipboard_translate)

table = gtk.Table(4, 2)
table.set_row_spacings(5)
table.set_col_spacings(5)
window.add(table)

menu_items = (
	("/_Options",                    None,              None,                      0,              "<Branch>"),
	("/Options/set _Font",           "<control>F",      select_font,               0,              None),
	("/Options/auto _Translation",   "<control>T",      toggle_auto_trans,         0,              "<ToggleItem>"),
	("/_Help",                       None,              None,                      0,              "<LastBranch>"),
	("/Help/_About",                 None,              about,                      0,             None),
)
				

menubar = get_menu(window, menu_items)

 # TODO:  this is an ugly, ugly way to get the activeness of the automatic trans menu item.
 # but I cannot see a better way but iterating over all of the menu items, which is even worse.  (Ofer Waldman)
menubar.get_children()[0].get_submenu().get_children()[1].set_active( configuration.automatic_translation )

table.attach(menubar, 0, 2, 0, 1, gtk.EXPAND|gtk.FILL, 0)

#word = gtk.Entry()
word = gtk.TextView()   # the textview instead of entry is needed to allow messing with the PRIMARY clipboard.
word.set_size_request(420, -1)
word.get_buffer().set_text("מילה")
table.attach(word, 0, 1, 1, 2, gtk.EXPAND|gtk.FILL, 0)

trans = gtk.Button("תרגם")
trans.set_size_request(70, -1)
table.attach(trans, 1, 2, 1, 2, 0, 0)

combo = gtk.Combo()
combo.set_size_request(420, -1)
table.attach(combo, 0, 1, 2, 3, gtk.EXPAND|gtk.FILL, 0)

select = gtk.Button("בחר")
select.set_size_request(70, -1)
table.attach(select, 1, 2, 2, 3, 0, 0)



translation = gtk.TextBuffer()

translation_textview = gtk.TextView(translation)
translation_textview.set_wrap_mode(gtk.WRAP_WORD)
translation_textview.set_editable(False)

# Colors
translation.tag_table.add(texttag('error', foreground='#FF0000', weight=pango.WEIGHT_BOLD))
translation.tag_table.add(texttag('matches_for', foreground='#FF0000'))
translation.tag_table.add(texttag('match', foreground='#0000FF'))
# -

scrolled_window = gtk.ScrolledWindow()
scrolled_window.set_size_request(500, 150)
scrolled_window.add_with_viewport(translation_textview)
scrolled_window.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)
table.attach(scrolled_window, 0, 2, 3, 4, gtk.EXPAND|gtk.FILL, gtk.EXPAND|gtk.FILL)


trans.connect('clicked', trans_click)
#word.connect('activate', trans_click) #TODO: doesn't exist in textview. we'll have to define the "enter" manually
word.connect('key-press-event', trans_click_in_textbox)
select.connect('clicked', select_click)
combo.entry.connect('activate', select_click)
#set the program font according to the configuration
word.get_settings().set_string_property('gtk-font-name', configuration.default_font, '')
window.show_all()

gtk.main()
