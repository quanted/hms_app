"""
HMS Documentation module views
"""
from django.template.loader import render_to_string

header = 'HMS:  Documentation'

description = '<p>This is where you will find all manuscripts and presentations about HMS.</p>'\
              '<p><h3>Source Code:</h3></p>'\
              '<ul class="bullet">' \
              '<li><a href="https://github.com/quanted/hms_app/tree/master"> HMS Documentation on GitHub</a> </li></ul>' \
              '<p></p><br>' \
              '<p></p>' \
              '<p><h3>Manuscripts:</h3></p>' \
              '<ul><li><a href="https://cfpub.epa.gov/si/si_public_record_report.cfm?dirEntryId=339606">Precipitation EPA Report</a></li></ul>'\
              '<ul><li><a href="https://cfpub.epa.gov/si/si_public_record_report.cfm?dirEntryId=339328">Runoff EPA Report</a></li></ul>' \
              '<ul><li><a href="https://cfpub.epa.gov/si/si_public_record_report.cfm?dirEntryId=342907">Streamflow EPA Report</a></li></ul>' \
              #add in iEMSs website that tracks downloads