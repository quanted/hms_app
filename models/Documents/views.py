"""
HMS Documentation module views
"""
from django.template.loader import render_to_string

header = 'HMS:  Publications'

description = '<p>This is where you will find all EPA reports, manuscripts, presentations, and peer-reviewed articles about HMS.</p>'\
              '<p><h3>Source Code:</h3></p>'\
              '<ul class="bullet">' \
              '<li><a href="https://github.com/quanted/hms/tree/master" target="_blank">HMS Documentation on GitHub</a> </li></ul>' \
              '<p></p>' \
              '<p></p>' \
              '<p><h3>Publications:</h3></p>' \
              '<ul><li><a href="https://scholarsarchive.byu.edu/cgi/viewcontent.cgi?article=4070&context=iemssconference" target="_blank">Hydrologic Micro Services</a></li></ul>' \
              '<ul><li><a href="https://onlinelibrary.wiley.com/doi/full/10.1111/1752-1688.12819" target="_blank">Comparison and Evaluation of Gridded Precipitation Datasets in a Kansas Agricultural Watershed Using SWAT</a></li></ul>' \
              '<ul><li><a href="https://www.sciencedirect.com/science/article/pii/S1364815219306279?via%3Dihub" target="_blank">Demonstration of an online web services tool incorporating automatic retrieval and comparison of precipitation</a></li></ul>' \
              '<ul><li><a href="https://cfpub.epa.gov/si/si_public_record_report.cfm?Lab=NERL&dirEntryId=339606" target="_blank">EPA Report: A survey of Precipitation Data for Environmental Modeling</a></li></ul>'\
              '<ul><li><a href="https://cfpub.epa.gov/si/si_public_record_report.cfm?Lab=NERL&dirEntryId=339328" target="_blank">EPA Report: An Overview of Rainfall-Runoff Model Types</a></li></ul>' \
              '<ul><li><a href="https://cfpub.epa.gov/si/si_public_record_report.cfm?Lab=NERL&dirEntryId=342907" target="_blank">EPA Report: Flow Routing Techniques for Environmental Modeling</a></li></ul>' \
    #add in iEMSs website that tracks downloads