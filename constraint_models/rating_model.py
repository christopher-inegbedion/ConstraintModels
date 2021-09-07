from constraints.constraint_main.constraint import Constraint
from constraints.enums.constraint_input_mode import ConstraintInputMode
from constraints.enums.model_family import ModelFamily
from constraints.models.model_parent import Model
from constraints.enums.input_type import InputType
from task_main.task import Task

class RatingModel(Model):
    def __init__(self):
        self.name = "Rating"
        self.model_family = ModelFamily.CONSTRAINT
        self.input_type = InputType.STRING
        self.input_mode = ConstraintInputMode.PRE_DEF
        self.input_count = 2
        self.output_type = InputType.BOOL

        super().__init__(self.name, self.model_family, self.input_type,
                         self.input_mode, self.input_count, self.output_type)
        
    def run(self, inputs, configuration_inputs={}):
        super().run(inputs)
        
        review_msg = inputs[0]
        review_score = inputs[1]
        
        self.add_configuration_input(review_msg, "review_msg")
        self.add_configuration_input(review_score, "review_score")
            
        self._complete(True)

    def _complete(self, data, aborted=False):
        super()._complete(data, aborted)
        constraint: Constraint = self.constraint
        constraint.completion_data = constraint.configuration_inputs
        

