class News:
    """
    news class to define news objects
    """

    def __init__(self, title, author, description, link, image, publish_time):
        self.title = title
        self.author = author
        self.description = description
        self.link = link
        self.image = image
        self.publish_time = publish_time