import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QMenuBar,
    QAction,
)

from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# Create the main window
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Inventory Management System")

# Create the labels
itemLabel = QLabel("Item:")
quantityLabel = QLabel("Quantity:")

# Create the line edits
itemLineEdit = QLineEdit()
quantityLineEdit = QLineEdit()

# Create the buttons
addButton = QPushButton("Add")
removeButton = QPushButton("Remove")

# Create the layout
layout = QVBoxLayout()
layout.addWidget(itemLabel)
layout.addWidget(itemLineEdit)
layout.addWidget(quantityLabel)
layout.addWidget(quantityLineEdit)
layout.addWidget(addButton)
layout.addWidget(removeButton)

# Add the layout to the window
window.setLayout(layout)

# Create the database connection
db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("inventory.db")
db.open()

# Function to add an item to the database
def addItem():
    # Get the item name and quantity from the line edits
    itemName = itemLineEdit.text()
    quantity = quantityLineEdit.text()

    # Create a new query
    query = QSqlQuery()

    # Insert the item into the database
    query.exec_("INSERT INTO items (item_name, quantity) VALUES ('%s', '%s')" % (itemName, quantity))

    # Clear the line edits
    itemLineEdit.setText("")
    quantityLineEdit.setText("")

# Function to remove an item from the database
def removeItem():
    # Get the item name from the line edit
    itemName = itemLineEdit.text()

    # Create a new query
    query = QSqlQuery()

    # Delete the item from the database
    query.exec_("DELETE FROM items WHERE item_name = '%s'" % itemName)

    # Clear the line edit
    itemLineEdit.setText("")

# Function to update the quantity of an item in the database
def updateItem():
    # Get the item name and new quantity from the line edits
    itemName = itemLineEdit.text()
    newQuantity = quantityLineEdit.text()

    # Create a new query
    query = QSqlQuery()

    # Update the item in the database
    query.exec_("UPDATE items SET quantity = '%s' WHERE item_name = '%s'" % (newQuantity, itemName))

    # Clear the line edits
    itemLineEdit.setText("")
    quantityLineEdit.setText("")

# Function to search for an item in the database
def searchItem():
    # Get the item name from the line edit
    itemName = itemLineEdit.text()

    # Create a new query
    query = QSqlQuery()

    # Search for the item in the database
    query.exec_("SELECT * FROM items WHERE item_name = '%s'" % itemName)

    # If the item is found, display its details in the labels
    if query.next():
        itemLabel.setText(query.value("item_name").toString())
        quantityLabel.setText(query.value("quantity").toString())
    else:
        itemLabel.setText("Item not found")
        quantityLabel.setText("")

# Function to display the list of items in the database
def displayItems():
    # Create a new query
    query = QSqlQuery()

    # Select all items from the database
    query.exec_("SELECT * FROM items")

    # Create a table to display the items
    table = QTableWidget()
    table.setRowCount(query.size())
    table.setColumnCount(2)
    table.setHorizontalHeaderLabels(["Item Name", "Quantity"])

    # Iterate over the results of the query and add them to the table
    row = 0
    while query.next():
        item_name = query.value("item_name").toString()
        quantity = query.value("quantity").toString()
        table.setItem(row, 0, QTableWidgetItem(item_name))
        table.setItem(row, 1, QTableWidgetItem(quantity))
        row += 1

    # Display the table
    layout.addWidget(table)

# Connect the buttons to their respective functions
addButton.clicked.connect(addItem)
removeButton.clicked.connect(removeItem)

# Create the main menu
menuBar = QMenuBar()
fileMenu = menuBar.addMenu("File")
newItemAction = QAction("New Item", window)
newItemAction.triggered.connect(addItem)
fileMenu.addAction(newItemAction)
removeItemAction = QAction("Remove Item", window)
removeItemAction.triggered.connect(removeItem)
fileMenu.addAction(removeItemAction)
updateItemAction = QAction("Update Item", window)
updateItemAction.triggered.connect(updateItem)
fileMenu.addAction(updateItemAction)
searchItemAction = QAction("Search Item", window)
searchItemAction.triggered.connect(searchItem)
fileMenu.addAction(searchItemAction)
displayItemsAction = QAction("Display Items", window)
displayItemsAction.triggered.connect(displayItems)
fileMenu.addAction(displayItemsAction)
exitAction = QAction("Exit", window)
exitAction.triggered.connect(app.quit)
fileMenu.addAction(exitAction)

# Add the menu bar to the window
window.setMenuBar(menuBar)

# Show the window
window.show()

# Start the application
sys.exit(app.exec_())
