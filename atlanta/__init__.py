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

    def get_organizations(self):
        return []
