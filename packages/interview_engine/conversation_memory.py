class ConversationMemory:

    def __init__(self):

        self.history = []


    def add(self, speaker, text):

        self.history.append(
            {
                "speaker": speaker,
                "text": text
            }
        )


    def recent(self, limit=10):

        return self.history[-limit:]