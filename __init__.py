from mycroft import MycroftSkill, intent_file_handler


class PY(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('y.p.intent')
    def handle_y_p(self, message):
        self.speak_dialog('y.p')


def create_skill():
    return PY()

