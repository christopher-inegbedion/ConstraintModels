from constraints.enums.constraint_input_mode import ConstraintInputMode
from constraints.enums.model_family import ModelFamily
from constraints.constraint_main.constraint import Constraint
from constraints.enums.input_type import InputType
from constraints.models.model_parent import Model
import requests
import jsonpickle


class PasswordModel(Model):
    def __init__(self):
        self.name = "PasswordModel"
        self.model_family = ModelFamily.CONSTRAINT
        self.input_type = InputType.STRING
        self.input_mode = ConstraintInputMode.PRE_DEF
        self.input_count = 0
        self.output_type = InputType.BOOL
        # self.config_parameters = [
        #     "passcode"]

        super().__init__(self.name, self.model_family, self.input_type,
                         self.input_mode, self.input_count, self.output_type,)
        
        self.attempts = 0

    def listen(self, msg, data):
        super().listen(msg, data)
        
        constraint: Constraint = self.constraint
        if data == constraint.configuration_inputs["passcode"]:
            self.add_configuration_input("result", "pass")
            self.add_configuration_input(self.attemps, "attempts")
            self._notify_config_input_change()
            self._complete(True)
        else:
            self._set_configuration_input_value("result", "fail")
            self._notify_config_input_change()
            self.attempts =+ 1

    def _complete(self, data, aborted=False):
        super()._complete(data, aborted)
