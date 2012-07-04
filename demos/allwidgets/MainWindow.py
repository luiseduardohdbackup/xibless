# Init
result = Window(200, 200, 350, 350, "All Supported Widgets")
tabView = TabView(result)
fooTab = tabView.addTab("foo")
barTab = tabView.addTab("bar")
bazTab = tabView.addTab("baz")
label = Label(fooTab.view, text="Label")
label.font = Font("Verdana", 12, [FontTrait.Bold, FontTrait.Italic])
label.textColor = Color(0.42, 0.42, 0.84)
label.alignment = const.NSCenterTextAlignment
textfield = TextField(fooTab.view, text="TextField")
button1 = Button(fooTab.view, title="Button")
button2 = Button(fooTab.view, title="Button")
button2.bezelStyle = const.NSRoundRectBezelStyle
checkbox = Checkbox(fooTab.view, title="Checkbox")
popup = Popup(fooTab.view, items=["One", "Two", "Three"])
combobox = Combobox(fooTab.view, items=["One", "Two", "Three"])
combobox.autoComplete = True
radioButtons = RadioButtons(fooTab.view, items=["One", "Two", "Three", "Four"], columns=2)
progress = ProgressIndicator(fooTab.view)
table = TableView(barTab.view)
table.addColumn("col1", title="Column 1", width=50)
table.addColumn("col2", title="Column 2", width=100)
table.addColumn("col3", title="Column 3", width=150)
textview = TextView(bazTab.view)
textview.text = "multi\nline\ntext"
textview.font = Font(FontFamily.System, 16)
imageview = ImageView(bazTab.view, "NSApplicationIcon")

tabView.packToCorner(Pack.UpperLeft)
tabView.fill(Pack.Right)
tabView.fill(Pack.Below)
tabView.setAnchor(Pack.UpperLeft, growX=True, growY=True)

# foo tab
label.packToCorner(Pack.UpperLeft)
label.fill(Pack.Right)
textfield.packRelativeTo(label, side=Pack.Below, align=Pack.Left)
button1.packRelativeTo(textfield, side=Pack.Below, align=Pack.Left)
button2.packRelativeTo(button1, side=Pack.Right, align=Pack.Above)
checkbox.packRelativeTo(button1, side=Pack.Below, align=Pack.Left)
popup.packRelativeTo(checkbox, side=Pack.Below, align=Pack.Left)
combobox.packRelativeTo(popup, side=Pack.Below, align=Pack.Left)
radioButtons.width = 150
radioButtons.height = 50
radioButtons.packRelativeTo(combobox, side=Pack.Below, align=Pack.Left)
progress.packRelativeTo(radioButtons, side=Pack.Below, align=Pack.Left)

#bar tab
table.packToCorner(Pack.UpperLeft)
table.fill(Pack.Right)
table.fill(Pack.Below)
table.setAnchor(Pack.UpperLeft, growX=True, growY=True)

#baz tab
textview.height = 50
textview.packToCorner(Pack.UpperLeft)
textview.fill(Pack.Right)
textview.setAnchor(Pack.UpperLeft, growX=True)
imageview.packRelativeTo(textview, side=Pack.Below, align=Pack.Left)
imageview.fill(Pack.Right)
imageview.setAnchor(Pack.UpperLeft, growX=True)
