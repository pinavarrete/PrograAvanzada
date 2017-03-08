import json


class Persona:
    def __init__(self, pid, nombre='default_name', twitter='default_name', instagram='default_name', amigosface=[],
                 seg0twitter=[], seg1twitter=[], seg0instagram=[], seg1instagram=[] ):
        self.pid = pid
        self.nombre = nombre
        self.twitter = twitter
        self.instagram = instagram
        self.amigosface = amigosface
        self.seg0twitter = seg0twitter
        self.seg1twitter = seg1twitter
        self.seg0instagram = seg0instagram
        self.seg1instagram = seg1instagram

