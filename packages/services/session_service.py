class SessionService:

    def __init__(self):

        self.current_session = None

    def set_current(self, session):

        self.current_session = session

    def current(self):

        return self.current_session