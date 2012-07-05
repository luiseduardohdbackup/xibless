TableView
=========

A :class:`View` sublass that represents Cocoa's ``NSTableView``. Note that although it's a view and
that views are added to their superview, ``xibless`` wraps the view into a ``NSScrollView`` and
adds that view to the superview (XCode does the same). The reference to the table view, however
(if you do stuff like ``owner.table = Table(superview)``) will be the reference of the
``NSTableView`` instance.

.. class:: TableView(parent)
    
    :param parent: A :class:`View` instance. Same as :attr:`View.parent`.
    
    .. method:: addColumn(identifier, title, width)
        
        :param identifier: String. See :attr:`TableColumn.identifier`.
        :param title: String. See :attr:`TableColumn.title`.
        :param width: Integer. See :attr:`TableColumn.width`.
        
        Creates a :class:`TableColumn` and adds it to self. The created item is returned by the
        method.
    
TableColumn
-----------

The ``TableColumn`` is created by :meth:`TableView.addColumn` and represents a ``NSTableColumn``.
You shouldn't create it directly, but you can set its attributes.

.. class:: TableColumn(table, identifier, title, width)
    
    :param table: The parent :class:`TableView`.
    :param identifier: String. See :attr:`TableColumn.identifier`.
    :param title: String. See :attr:`TableColumn.title`.
    :param width: Integer. See :attr:`TableColumn.width`.
    
    .. attribute:: identifier
        
        String. The identifier of the column. Equivalent to ``[self identifier]``.
    
    .. attribute:: title
        
        String. The title of the column. Equivalent to ``[[self headerCell] stringValue]``.
    
    .. attribute:: width
        
        Integer. The width of the column. Equivalent to ``[self width]``.
    
    .. attribute:: font
        
        :class:`Font`. The font of the column. Equivalent to ``[[self dataCell] font]``.
    
    .. attribute:: editable
        
        Boolean. Whether the column can be edited. Equivalent to ``[self editable]``.
    