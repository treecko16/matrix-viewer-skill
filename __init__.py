from mycroft import MycroftSkill, intent_file_handler


class MatrixViewer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('viewer.matrix.intent')
    def handle_viewer_matrix(self, message):
        self.speak_dialog('viewer.matrix')


def create_skill():
    return MatrixViewer()

