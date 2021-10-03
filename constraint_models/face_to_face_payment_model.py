from constraints.constraint_main.constraint import Constraint
from constraints.enums.constraint_input_mode import ConstraintInputMode
from constraints.enums.model_family import ModelFamily
from constraints.models.model_parent import Model
from constraints.enums.input_type import InputType
from task_main.task import Task
from datetime import datetime


class FaceToFacePayment(Model):
    def __init__(self):
        self.name = "FaceToFacePayment"
        self.model_family = ModelFamily.CONSTRAINT
        self.input_type = InputType.STRING
        self.input_mode = ConstraintInputMode.PRE_DEF
        self.input_count = 0
        self.output_type = InputType.BOOL

        super().__init__(self.name, self.model_family, self.input_type,
                         self.input_mode, self.input_count, self.output_type,
                         admin_session_independent=False, for_payment=True)
        

    def listen(self, msg, data):
        task: Task = self.constraint.task_instance
        now = datetime.now() 
        
        if msg == "paid":
            task.toggle_paid_val(True)
            self.add_configuration_input(True, "paid")
            self.add_configuration_input(task.price, "amount")
            self.add_configuration_input(task.currency, "currency")
            self.add_configuration_input(now.strftime("%m/%d/%Y, %H:%M:%S"), "time_paid")
            self._complete(True)

    def _complete(self, data, aborted=False):
        super()._complete(data, aborted)
        constraint: Constraint = self.constraint
        constraint.completion_data = constraint.configuration_inputs
        
