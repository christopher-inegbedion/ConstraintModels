from constraints.enums.constraint_input_mode import ConstraintInputMode
from constraints.enums.model_family import ModelFamily
from constraints.enums.input_type import InputType
from constraints.models.model_parent import Model
import requests
import jsonpickle
from task_main.task import Task


class ProductDescriptionModel(Model):
    def __init__(self):

        self.name = "ProductDesctiptionModel"
        self.model_family = ModelFamily.CONSTRAINT
        self.input_type = InputType.STRING
        self.input_mode = ConstraintInputMode.PRE_DEF
        self.input_count = 0
        self.output_type = InputType.ANY

        super().__init__(self.name, self.model_family, self.input_type,
                         self.input_mode, self.input_count, self.output_type)

    def run(self, inputs, configuration_inputs={}):
        super().run(inputs)
        task: Task = self.constraint.task_instance
        properties = task.get_selected_properties()

        for property in properties:
            self.config_parameters.append(property)

        task: Task = self.constraint.task_instance
        self.add_configuration_input(task.name, "Product name")
        self.add_configuration_input(task.description, "Product description")
        self.add_configuration_input(task.price, "Price")
        self.add_configuration_input(task.currency, "Currency")

        for property in properties:
            if properties[property]["denomination"] == None:
                val = properties[property]["value"]
            else:
                val = str(properties[property]["value"]) + \
                    properties[property]["denomination"]

            self.add_configuration_input(val, property)

        self._complete(True)

    def _complete(self, data, aborted=False):
        super()._complete(data, aborted)
