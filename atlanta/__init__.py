# encoding=utf-8
from pupa.scrape import Jurisdiction, Organization
from .people import AtlantaPersonScraper


class Atlanta(Jurisdiction):
    division_id = "ocd-jurisdiction/country:us/state:ga/place:atlanta/council"
    classification = "government"
    name = "Atlanta City Council"
    url = "http://citycouncil.atlantaga.gov/"
    scrapers = {
        "people": AtlantaPersonScraper,
    }
    terms = [{
        'name': '2013-2017',
        'start_year': 2013,
        'end_year': 2017,
        'sessions': ['2013'],
    }]

    def get_organizations(self):
        return []
