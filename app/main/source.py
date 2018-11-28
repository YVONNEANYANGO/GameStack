class Source:
    ''' source class to define Source objects '''
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country

class Source_News:
    ''' source_news to define objects of news from various sources '''

    def __init__(self,author,title,description,url,urlToImage,publishedAt):

        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
