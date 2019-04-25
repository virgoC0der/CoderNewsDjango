
class dataModel:

    def __init__(self,title,url,imageUrl,category):
        self.title = title
        self.url = url
        self.imageUrl = imageUrl
        self.category = category

    def printIt(self):
        print(self.title,self.url,self.imageUrl,self.category)

