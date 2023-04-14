import sys
from PyQt6.QtCore import Qt, QModelIndex
from PyQt6.QtWidgets import QApplication, QTableWidgetItem, QHBoxLayout, QWidget, QAbstractItemView, QTableView, \
    QTableWidget


class TableWidgetDragRows(QTableWidget):
    def __init__(self, *args, **kwargs):
        QTableWidget.__init__(self, *args, **kwargs)

        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.viewport().setAcceptDrops(True)
        self.setDragDropOverwriteMode(False)
        self.setDropIndicatorShown(True)

        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)

    def dropEvent(self, event):
        if event.source() == self and (
                event.dropAction() == Qt.DropAction.MoveAction or self.dragDropMode()
                == QAbstractItemView.DragDropMode.InternalMove):
            success, row, col, topIndex = self.dropOn(event)
            if success:
                selRows = self.getSelectedRowsFast()

                top = selRows[0]
                # print 'top is %d'%top
                dropRow = row
                if dropRow == -1:
                    dropRow = self.rowCount()
                # print 'dropRow is %d'%dropRow
                offset = dropRow - top
                # print 'offset is %d'%offset

                for i, row in enumerate(selRows):
                    r = row + offset
                    if r > self.rowCount() or r < 0:
                        r = 0
                    self.insertRow(r)
                    # print 'inserting row at %d'%r

                selRows = self.getSelectedRowsFast()
                # print 'selected rows: %s'%selRows

                top = selRows[0]
                # print 'top is %d'%top
                offset = dropRow - top
                # print 'offset is %d'%offset
                for i, row in enumerate(selRows):
                    r = row + offset
                    if r > self.rowCount() or r < 0:
                        r = 0

                    for j in range(self.columnCount()):
                        # print 'source is (%d, %d)'%(row, j)
                        # print 'item text: %s'%self.item(row,j).text()
                        source = QTableWidgetItem(self.item(row, j))
                        # print 'dest is (%d, %d)'%(r,j)
                        self.setItem(r, j, source)

                # Why does this NOT need to be here?
                # for row in reversed(selRows):
                # self.removeRow(row)

                event.accept()

        else:
            QTableView.dropEvent(event)

    def getSelectedRowsFast(self):
        selRows = []
        for item in self.selectedItems():
            if item.row() not in selRows:
                selRows.append(item.row())
        return selRows

    def droppingOnItself(self, event, index):
        dropAction = event.dropAction()

        if self.dragDropMode() == QAbstractItemView.DragDropMode.InternalMove:
            dropAction = Qt.DropAction.MoveAction

        if event.source() == self and event.possibleActions() & Qt.DropAction.MoveAction and \
                dropAction == Qt.DropAction.MoveAction:
            selectedIndexes = self.selectedIndexes()
            child = index
            while child.isValid() and child != self.rootIndex():
                if child in selectedIndexes:
                    return True
                child = child.parent()

        return False

    def dropOn(self, event):
        if event.isAccepted():
            return False, None, None, None

        index = QModelIndex()
        row = -1
        col = -1
        pointPos = event.position().toPoint()
        if self.viewport().rect().contains(pointPos):
            index = self.indexAt(pointPos)
            if not index.isValid() or not self.visualRect(index).contains(pointPos):
                index = self.rootIndex()

        if self.model().supportedDropActions() & event.dropAction():
            if index != self.rootIndex():
                dropIndicatorPosition = self.position(pointPos, self.visualRect(index), index)

                if dropIndicatorPosition == QAbstractItemView.DropIndicatorPosition.AboveItem:
                    row = index.row()
                    col = index.column()
                    # index = index.parent()
                elif dropIndicatorPosition == QAbstractItemView.DropIndicatorPosition.BelowItem:
                    row = index.row() + 1
                    col = index.column()
                    # index = index.parent()
                else:
                    row = index.row()
                    col = index.column()

            if not self.droppingOnItself(event, index):
                # print 'row is %d'%row
                # print 'col is %d'%col
                return True, row, col, index

        return False, None, None, None

    def position(self, pos, rect, index):
        r = QAbstractItemView.DropIndicatorPosition.OnViewport
        margin = 2
        if pos.y() - rect.top() < margin:
            r = QAbstractItemView.DropIndicatorPosition.AboveItem
        elif rect.bottom() - pos.y() < margin:
            r = QAbstractItemView.DropIndicatorPosition.BelowItem
        elif rect.contains(pos, True):
            r = QAbstractItemView.DropIndicatorPosition.OnItem

        if r == QAbstractItemView.DropIndicatorPosition.OnItem and \
                not (self.model().flags(index) & Qt.ItemFlag.ItemIsDropEnabled):
            r = QAbstractItemView.DropIndicatorPosition.AboveItem if pos.y() < rect.center().y() \
                else QAbstractItemView.DropIndicatorPosition.BelowItem

        return r


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)

        self.table_widget = TableWidgetDragRows()
        layout.addWidget(self.table_widget)

        # setup table widget
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(['Colour', 'Model'])

        items = [('Red', 'Toyota'), ('Blue', 'RV'), ('Green', 'Beetle')]
        for i, (colour, model) in enumerate(items):
            c = QTableWidgetItem(colour)
            m = QTableWidgetItem(model)

            self.table_widget.insertRow(self.table_widget.rowCount())
            self.table_widget.setItem(i, 0, c)
            self.table_widget.setItem(i, 1, m)

        self.show()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())