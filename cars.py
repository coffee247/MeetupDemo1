from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex
from PyQt5.QtWidgets import QMessageBox

""" Reference https://github.com/pyside/pyside2-examples/blob/dev/examples/widgets/itemviews/addressbook """


class carsModel(QAbstractTableModel):
    def __init__(self, Cars=None, parent=None):
        super(carsModel, self).__init__(parent)
        # create Cars list if it does not exist
        if Cars is None:
            self.Cars = []
        else:
            self.Cars = Cars

    # Modal Warning Box
    def issueWarning(self, Message):
        QMessageBox.about(self, "Warning", Message)
        data = list(('test', 'tester')[0].keys())

    def rowCount(self, index=QModelIndex()):
        """ Returns the number of rows the model holds """
        return len(self.Cars)

    def columnCount(self, index=QModelIndex()):
        return 4    #  fields:  projectileType, projoMass, projoDrag

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        if not 0 <= index.row() < len(self.Cars):
            return None

        if role == Qt.DisplayRole:
            carID = self.Cars[index.row()]["carID"]
            make = self.Cars[index.row()]["make"]
            model = self.Cars[index.row()]["model"]
            year = self.Cars[index.row()]["year"]
            color = self.Cars[index.row()]["color"]

            if index.column() == 0:
                return carID
            elif index.column() == 1:
                return make
            elif index.column() == 2:
                return model
            elif index.column() == 3:
                return year
            elif index.column() == 4:
                return color
            return None



    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            if section == 0:
                return "carID"
            if section == 1:
                return "make"
            if section == 2:
                return "model"
            if section == 3:
                return "year"
            if section == 4:
                return "color"
            return None

        # if orientation == Qt.Vertical:
        #     if role == Qt.DisplayRole:
        #         return " --> "


    def insertRows(self, position, rows=1, index=QModelIndex()):
        """Insert a row of range data into RangeModel. """
        self.beginInsertRows(QModelIndex(), position, position + rows - 1)

        for row in range(rows):
            self.Cars.insert(position + row, {"carID": "", "make": "", "model": "", "year": "",  "color": ""})

        self.endInsertRows()
        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        """ Remove a row from  ProjectilesModel. """
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)

        del self.Cars[position:position + rows]

        self.endRemoveRows()
        self.dataChanged.emit(index, index)
        return True

    def addData(self):
        pass


    def setData(self, index, value, role=Qt.EditRole):
        """ Adjust the data (set it to <value>) depending on the given
            index and role.
        """
        if role != Qt.EditRole:
            return False
        a = index.isValid()
        row = index.row()
        length = len(self.Cars)
        if index.isValid() and index.row() < len(self.Cars):
            aCar = self.Cars[index.row()]
            if index.column() == 0:
                aCar["carID"] = f"{value}"
            elif index.column() == 1:
                aCar["make"] = f"{value}"
            elif index.column() == 2:
                aCar["model"] = f"{value}"
            elif index.column() == 3:
                aCar["year"] = f"{value}"
            elif index.column() == 4:
                aCar["color"] = f"{value}"
            else:
                return False

            self.dataChanged.emit(index, index)
            return True

        return False