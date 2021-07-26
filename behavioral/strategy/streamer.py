from abc import ABC, abstractmethod

ALLOWED_EXTENSIONS = ['html', 'mp3', 'pdf']


class Renderer(ABC):

    @abstractmethod
    def render(self):
        pass


class HtmlRenderer(Renderer):

    def render(self):
        print('Render using html renderer')


class MP3Renderer(Renderer):

    def render(self):
        print('Render using mp3 streamer')


class PdfRenderer(Renderer):

    def render(self):
        print('Render using pdf renderer')


class FileHandler:

    def __init__(self, filename):
        self.filename = filename

    @property
    def extension(self):
        return self.filename.split('.')[-1]

    @classmethod
    def create(cls, filename):
        extension = filename.split('.')[-1]
        if extension not in ALLOWED_EXTENSIONS:
            print(f'File extension({extension}) not allowed')
        else:
            return cls(filename)

    def render(self):
        extensions = {
            'html': HtmlRenderer,
            'mp3': MP3Renderer,
            'pdf': PdfRenderer
        }

        select_renderer = extensions[self.extension]
        return select_renderer().render()


if __name__ == '__main__':
    f1 = FileHandler.create(filename='index.html')
    f2 = FileHandler.create(filename='app.js')
    f3 = FileHandler.create(filename='music.mp3')
    f4 = FileHandler.create(filename='document.pdf')
    f5 = FileHandler.create(filename='main.py')

    files = [f1, f3, f4]

    for file in files:
        file.render()
