ownerclass = 'AppDelegate'
result = NSMenu("Apple")
fileMenu = result.addMenu("File")
editMenu = result.addMenu("Edit")
windowMenu = result.addMenu("Window")
helpMenu = result.addMenu("Help")

fileMenu.addItem("About MyApp")
fileMenu.addItem("test", Action(owner, 'fooAction'))
fileMenu.addSeparator()
NSApp.servicesMenu = fileMenu.addMenu("Services")
fileMenu.addSeparator()
fileMenu.addItem("Hide MyApp", Action(NSApp, 'hide:'), 'cmd+h')
fileMenu.addItem("Hide Others", Action(NSApp, 'hideOtherApplications:'), 'cmd+alt+h')
fileMenu.addItem("Hide Others", Action(NSApp, 'unhideAllApplications:'))
fileMenu.addSeparator()
fileMenu.addItem("Quit MyApp", Action(NSApp, 'terminate:'), 'cmd+q')

editMenu.addItem("Undo", Action(None, 'undo:'), 'cmd+z')
editMenu.addItem("Redo", Action(None, 'redo:'), 'cmd+shift+z')
editMenu.addSeparator()
editMenu.addItem("Cut", Action(None, 'cut:'), 'cmd+x')
editMenu.addItem("Copy", Action(None, 'copy:'), 'cmd+c')
editMenu.addItem("Paste", Action(None, 'paste:'), 'cmd+v')
editMenu.addItem("Paste And Match Style", Action(None, 'pasteAsPlainText:'), 'cmd+alt+shift+v')
editMenu.addItem("Delete", Action(None, 'delete:'))
editMenu.addItem("Select All", Action(None, 'selectAll:'), 'cmd+a')
editMenu.addSeparator()
findMenu = editMenu.addMenu("Find")
findMenu.addItem("Find...", Action(None, 'performFindPanelAction:'), 'cmd+f', tag=const.NSFindPanelActionShowFindPanel)
findMenu.addItem("Find Next", Action(None, 'performFindPanelAction:'), 'cmd+g', tag=const.NSFindPanelActionNext)
findMenu.addItem("Find Previous", Action(None, 'performFindPanelAction:'), 'cmd+shift+g', tag=const.NSFindPanelActionPrevious)
findMenu.addItem("Use Selection for Find", Action(None, 'performFindPanelAction:'), 'cmd+e', tag=const.NSFindPanelActionSetFindString)
findMenu.addItem("Jump to Selection", Action(None, 'centerSelectionInVisibleArea:'), 'cmd+j')
spellingMenu = editMenu.addMenu("Spelling")
spellingMenu.addItem("Spelling...", Action(None, 'showGuessPanel:'), 'cmd+:')
spellingMenu.addItem("Check Spelling", Action(None, 'checkSpelling:'), 'cmd+;')
spellingMenu.addItem("Check Spelling as You Type", Action(None, 'toggleContinuousSpellChecking:'))

windowMenu.addItem("Minimize", Action(None, 'performMinimize:'), 'cmd+m')
windowMenu.addItem("Zoom", Action(None, 'performZoom:'))
windowMenu.addSeparator()
windowMenu.addItem("Bring All to Front", Action(None, 'arrangeInFront:'))

helpMenu.addItem("MyApp Help", Action(NSApp, 'showHelp:'), 'cmd+?')