import traceback
from .base import Base
from confapp import conf

if conf.PYFORMS_MODE == 'GUI':
    from AnyQt.QtWidgets import QFileDialog, QMessageBox



class BaseIO(Base):

    ######################################################################################
    #### IO FUNCTIONS ####################################################################
    ######################################################################################

    def save(self, data, project_path=None):
        self._project.save(data, project_path)
        return data

    def load(self, data, project_path=None):
        try:
            self._project.load(data, project_path)
        except Exception as e:
            print(e)
            print(traceback.print_exc())
            QMessageBox.critical(self, "Error", str(e))

    def save_project(self, project_path=None):
        try:
            if project_path is None:
                dialog = QFileDialog()
                dialog.setLabelText(QFileDialog.Accept, 'Save')
                project_path = dialog.getExistingDirectory(self, caption="Select the project directory to save")

            if project_path is not None and str(project_path) != '':
                project_path = str(project_path)
                self.save({}, project_path)
        except Exception as e:
            traceback.print_exc()
            QMessageBox.critical(self, "Error", str(e))

    def load_project(self, project_path=None):
        if project_path is None:
            project_path = QFileDialog.getExistingDirectory(self, caption="Select the project directory to open")

        if project_path is not None and str(project_path) != '':
            self.load({}, str(project_path))
