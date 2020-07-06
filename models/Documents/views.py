"""
HMS Documentation module views
"""
from django.template.loader import render_to_string

header = 'HMS:  Publication'

description = '<p>This is where you will find all manuscripts and presentations about HMS.</p>'\
              '<p><h3>Source Code:</h3></p>'\
              '<ul class="bullet">' \
              '<li><a href="https://github.com/quanted/hms/tree/master" target="_blank"> HMS Documentation on GitHub</a> </li></ul>' \
              '<p></p><br>' \
              '<p></p>' \
              '<p><h3>Manuscripts:</h3></p>' \
              '<ul><li><a href="https://cfpub.epa.gov/si/si_public_record_report.cfm?dirEntryId=339606" target="_blank">Precipitation EPA Report</a></li></ul>'\
              '<ul><li><a href="https://cfpub.epa.gov/si/si_public_record_report.cfm?dirEntryId=339328" target="_blank">Runoff EPA Report</a></li></ul>' \
              '<ul><li><a href="https://cfpub.epa.gov/si/si_public_record_report.cfm?dirEntryId=342907" target="_blank">Streamflow EPA Report</a></li></ul>' \
              '<ul><li><a href="https://www.sciencedirect.com/science/article/pii/S1364815219306279?via%3Dihub" target="_blank"> Demonstration of an online web services tool incorporating automatic retrieval and comparison of precipitation</a></li></ul>' \
    #add in iEMSs website that tracks downloads