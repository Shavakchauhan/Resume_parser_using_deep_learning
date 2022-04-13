import spacy
import re
class NamedEntityService(object):
    model = None  # Where we keep the model when it's loaded
    
    @classmethod
    def get_model(cls):
        """Get the model object for this instance, loading it if it's not already loaded."""
        if cls.model is None:
            cls.model = spacy.load('generated_model/model-best')
        return cls.model

    
    @classmethod
    def get_entities(cls, input):
        """For the input, get entities and return them."""
        clf = cls.get_model()
        answer_dict = dict()
        for x in clf(input).ents:
            label_name = x.label_
            text_name = re.sub('[^A-Za-z0-9]+', ' ', str(x)).strip()
            answer_dict[text_name] = label_name

        # return dict([(str(x), x.label_) for x in clf(input).ents])
        return answer_dict