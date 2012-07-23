from .base import GeneratedItem, convertValueToObjc, KeyValueId, Literal, Flags, NonLocalizableString
from .view import View

class TableColumn(GeneratedItem):
    OBJC_CLASS = 'NSTableColumn'
    
    def __init__(self, table, identifier, title, width):
        GeneratedItem.__init__(self)
        self.table = table
        self.identifier = identifier
        self.title = title
        self.width = width
        self.font = table.font
        self.editable = table.editable
        self.userResizable = True
        self.autoResizable = False
        self.dataCell = None
    
    def dependencies(self):
        return [self.font, self.dataCell]
    
    def generateInit(self):
        tmpl = GeneratedItem.generateInit(self)
        tmpl.initmethod = "initWithIdentifier:$identifier$"
        tmpl.identifier = convertValueToObjc(NonLocalizableString(self.identifier))
        self.properties['headerCell.stringValue'] = self.title
        if self.dataCell:
            self.properties['dataCell'] = self.dataCell.accessor.cell
        else:
            if self.font:
                self.properties['dataCell.font'] = self.font
        self.properties['width'] = self.width
        self.properties['editable'] = self.editable
        resizingMask = Flags()
        if self.userResizable:
            resizingMask.add('NSTableColumnUserResizingMask')
        if self.autoResizable:
            resizingMask.add('NSTableColumnAutoresizingMask')
        if resizingMask:
            self.properties['resizingMask'] = resizingMask
        return tmpl
    

class TableView(View):
    OBJC_CLASS = 'NSTableView'
    PROPERTIES = View.PROPERTIES.copy()
    PROPERTIES.update({
        'allowsColumnReordering': '',
        'allowsColumnResizing': '',
        'allowsColumnSelection': '',
        'allowsEmptySelection': '',
        'allowsMultipleSelection': '',
        'allowsTypeSelect': '',
        'rowHeight': '',
        'dataSource': '',
    })
    
    def __init__(self, parent):
        View.__init__(self, parent, 100, 100)
        self.columns = []
        self.font = None
        self.editable = True
    
    def addColumn(self, identifier, title, width):
        column = TableColumn(self, identifier, title, width)
        self.columns.append(column)
        return column
    
    def generateInit(self):
        tmpl = View.generateInit(self)
        viewsetup = """NSScrollView *$varname$_container = [[[NSScrollView alloc] initWithFrame:$rect$] autorelease];
            [$varname$_container setDocumentView:$varname$];
            [$varname$_container setHasVerticalScroller:YES];
            [$varname$_container setHasHorizontalScroller:YES];
            [$varname$_container setAutohidesScrollers:YES];
            [$varname$_container setBorderType:NSBezelBorder];
            [$varname$_container setAutoresizingMask:$autoresize$];
        """
        tmpl.autoresize = convertValueToObjc(self.properties['autoresizingMask'])
        self.properties['columnAutoresizingStyle'] = Literal('NSTableViewUniformColumnAutoresizingStyle')
        for column in self.columns:
            colcode = column.generate()
            colcode += "[$varname$ addTableColumn:%s];\n" % column.varname
            viewsetup += colcode
        tmpl.viewsetup = viewsetup
        return tmpl
    
    def generateAddToParent(self):
        container = KeyValueId(None, self.varname + '_container')
        return self.parent.generateAddSubview(container)
    
    def generateFinalize(self):
        return self.accessor._callMethod('sizeToFit')
    

class OutlineView(TableView):
    OBJC_CLASS = 'NSOutlineView'
    