# Factory Method in python

from abc import ABC, abstractmethod


class Section(ABC):

    @abstractmethod
    def describe(self):
        pass


class AlbumSection(Section):

    def describe(self):
        return 'Album Section'


class PatentSection(Section):

    def describe(self):
        return 'Patent Section'


class ProfileSection(Section):

    def describe(self):
        return 'Profile Section'


class SocialFactory(ABC):

    def __init__(self):
        self.sections = list()
        self.create_section()

    @abstractmethod
    def create_section(self):
        pass

    def get_sections(self):
        return self.sections

    def set_section(self, section):
        self.sections.append(section)


class LinkIn(SocialFactory):

    def create_section(self):
        self.set_section(ProfileSection())
        self.set_section(PatentSection())


class SocialNetWork(SocialFactory):

    def create_section(self):
        self.set_section(ProfileSection())
        self.set_section(AlbumSection())


if __name__ == '__main__':
    linkedin = LinkIn()
    social_network = SocialNetWork()

    print(linkedin.get_sections())
    print(social_network.get_sections())
