from constraints.enums.constraint_input_mode import ConstraintInputMode
from constraints.enums.model_family import ModelFamily
from constraints.models.model_parent import Model
from constraints.enums.input_type import InputType
from task_main.task import Task


class FaceToFacePayment(Model):
    def __init__(self):
        self.name = "FaceToFacePayment"
        self.model_family = ModelFamily.CONSTRAINT
        self.input_type = InputType.STRING
        self.input_mode = ConstraintInputMode.PRE_DEF
        self.input_count = 0
        self.output_type = InputType.BOOL

        super().__init__(self.name, self.model_family, self.input_type,
                         self.input_mode, self.input_count, self.output_type, admin_session_independent=False)

    def run(self, inputs, configuration_inputs={}):
        super().run(inputs)
        task: Task = self.constraint.task_instance
        task.toggle_paid_val(True)
        self._complete(True)


    def _complete(self, data, aborted=False):
        super()._complete(data, aborted)