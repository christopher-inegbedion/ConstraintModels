from constraint_models.rating_model import RatingModel
from constraints.models.model_parent import Model
from constraint_models.internet_model import InternetModel
from constraints.models.example_models.pause_thread import PauseModel
from constraint_models.product_description_model import ProductDescriptionModel
from constraint_models.order_product_model import OrderProductModel
from constraint_models.product_link_model import ProductLinkModel
from constraint_models.password_model import PasswordModel
from constraint_models.time_range_model import TimeRangeModel
from constraint_models.chat_model import ChatModel
from constraint_models.delivery1_model import DeliveryModel
from constraint_models.face_to_face_payment_model import FaceToFacePayment
from constraints.constraint_main.custom_constraint import CustomConstraint


class CreateConstraintUtil():
    all_constraints = {
        "Exchange rate": CustomConstraint("Exchange rate", "View the current exchange rate between 2 currencies", InternetModel(), False),
        "Pause": CustomConstraint("Pause", "A constraint to pause", PauseModel(), False),
        "Product description": CustomConstraint("Product description", "View the product's basic information", ProductDescriptionModel(), False, constraint_thumbnail_descriptior="https://media.giphy.com/media/otR2O9KOBHOytUBkSn/giphy.gif"),
        "Product link": CustomConstraint("Product link", "Provide a link to a URL for your customer", ProductLinkModel(), False),
        "Password": CustomConstraint("Password", "Requires a secret word/phrase before access can be granted", PasswordModel(), False, completion_data_labels=["Actual password", "Number of attempts"]),
        "Time range": CustomConstraint("Time range", "Set a time for where your task can be accessed.", TimeRangeModel(), False),
        "Chat": CustomConstraint("Chat", "Chat with your customers", ChatModel(), False),
        "Delivery": CustomConstraint("Delivery", "View the current delivery status", DeliveryModel(), True),
        "Face-To-Face payment": CustomConstraint("Face-To-Face payment", "Collect payments from your customers in person",
                                                 FaceToFacePayment(), True, completion_data_labels=["Paid", "Amount", "Currency", "Time paid"], constraint_thumbnail_descriptior="https://media.giphy.com/media/fAEj9oqG6iwApdz0jg/giphy.gif"),
        "Rating and Review": CustomConstraint("Rating and Review", "Rate the service", RatingModel(), False,
                                              completion_data_labels=["Review message", "Review score"], constraint_thumbnail_descriptior="https://media.giphy.com/media/Yr5I3GTYw7qkgJv4OC/giphy.gif")
    }

    def __init__(self) -> None:
        pass

    @classmethod
    def _create_model(cls, name) -> Model:
        if name == "Exchange rate":
            return InternetModel()
        elif name == "Pause":
            return PauseModel()
        elif name == "Product description":
            return ProductDescriptionModel()
        elif name == "Order confirmation":
            return OrderProductModel()
        elif name == "Product link":
            return ProductLinkModel()
        elif name == "Password":
            return PasswordModel()
        elif name == "Time range":
            return TimeRangeModel()
        elif name == "Chat":
            return ChatModel()
        elif name == "Delivery":
            return DeliveryModel()
        elif name == "Face-To-Face payment":
            return FaceToFacePayment()
        elif name == "Rating and Review":
            return RatingModel()

    @classmethod
    def create_constraint(cls, name) -> CustomConstraint:
        if name in cls.all_constraints:
            return CustomConstraint(name, cls.all_constraints[name].description, cls._create_model(name),
                                    cls.all_constraints[name].is_admin_input_required,
                                    completion_data_labels=cls.all_constraints[name].completion_data_labels)
