import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QFormLayout, QComboBox, QCheckBox, QRadioButton, QDateEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import QDate

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Data Management")
        self.setGeometry(500, 500, 500, 500)

        self.form_layout = QFormLayout()

        self.label_name = QLabel("Name:")
        self.line_edit_name = QLineEdit()
        self.form_layout.addRow(self.label_name, self.line_edit_name)

        self.label_age = QLabel("Age:")
        self.line_edit_age = QLineEdit()
        self.form_layout.addRow(self.label_age, self.line_edit_age)

        self.label_gender = QLabel("Gender:")
        self.combo_box_gender = QComboBox()
        self.combo_box_gender.addItems(["Male", "Female"])
        self.form_layout.addRow(self.label_gender, self.combo_box_gender)

        self.label_department = QLabel("Department:")
        self.combo_box_department = QComboBox()
        self.combo_box_department.addItems(["Computer Science", "Mathematics", "Physics"])
        self.form_layout.addRow(self.label_department, self.combo_box_department)

        self.label_enrollment_date = QLabel("Enrollment Date:")
        self.date_edit_enrollment_date = QDateEdit()
        self.date_edit_enrollment_date.setDate(QDate.currentDate())
        self.form_layout.addRow(self.label_enrollment_date, self.date_edit_enrollment_date)

        self.label_status = QLabel("Status:")
        self.check_box_active = QCheckBox("Active")
        self.check_box_inactive = QCheckBox("Inactive")
        self.form_layout.addRow(self.label_status, self.check_box_active)
        self.form_layout.addRow("", self.check_box_inactive)

        self.button_save = QPushButton("Save")
        self.button_clear = QPushButton("Clear")
        self.form_layout.addRow(self.button_save, self.button_clear)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.form_layout)
        self.setCentralWidget(self.central_widget)

        self.button_save.clicked.connect(self.save_data)
        self.button_clear.clicked.connect(self.clear_data)

    def save_data(self):
        name = self.line_edit_name.text()
        age = self.line_edit_age.text()
        gender = self.combo_box_gender.currentText()
        department = self.combo_box_department.currentText()
        enrollment_date = self.date_edit_enrollment_date.date().toString("yyyy-MM-dd")
        status = "Active" if self.check_box_active.isChecked() else "Inactive"

        with open("students.csv", "a") as file:
            file.write(f"{name},{age},{gender},{department},{enrollment_date},{status}\n")

    def clear_data(self):
        self.line_edit_name.clear()
        self.line_edit_age.clear()
        self.combo_box_gender.setCurrentIndex(0)
        self.combo_box_department.setCurrentIndex(0)
        self.date_edit_enrollment_date.setDate(QDate.currentDate())
        self.check_box_active.setChecked(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
