class Photo:
    def __init__(self, info_from_db):
        self.id = str(info_from_db[0])
        self.id_8digits = "0" * (8 - len(self.id)) + self.id
        self.title = info_from_db[1]
        self.place = info_from_db[2]
        self.date = info_from_db[3]

    def get_picture(self):
        return self.id_8digits + ".jpg"

    def get_miniature(self):
        return "miniatures/" + self.id_8digits + ".jpg"

    def get_xml(self):
        return self.id_8digits + ".xml"
