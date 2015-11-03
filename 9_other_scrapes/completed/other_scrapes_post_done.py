#! usr/bin/python

import requests
from bs4 import BeautifulSoup
from datetime import date
import re

# Other common situation: ASP.NET used to dynamically refresh a page or deliver
# data. We can use requests to send the same data payload a browser would when
# we click on a link to download a file.
# http://www.evagoras.com/2011/02/10/how-postback-works-in-asp-net/

# https://www.elections.il.gov/CampaignDisclosure/DownloadList.aspx?DownloadListType=Receipts&LastOnlyNameSearchType=Starts+with&LastOnlyName=&FirstNameSearchType=Starts+with&FirstName=&AddressSearchType=Starts+with&Address=&CitySearchType=Starts+with&City=&State=&Zip=&ZipThru=&ContributionType=All+Types&OccupationSearchType=Starts+with&Occupation=&EmployerSearchType=Starts+with&Employer=&VendorLastOnlyNameSearchType=Starts+with&VendorLastOnlyName=&VendorFirstNameSearchType=Starts+with&VendorFirstName=&VendorAddressSearchType=Starts+with&VendorAddress=&VendorCitySearchType=Starts+with&VendorCity=&VendorState=&VendorZip=&VendorZipThru=&OtherReceiptsDescriptionSearchType=&OtherReceiptsDescription=&PurposeState=Starts+with&Purpose=&Amount=&AmountThru=&RcvDate=10%2f22%2f2015&RcvDateThru=10%2f22%2f2015&Archived=false&QueryType=Contrib&LinkedQuery=false&OrderBy=Date+Received+-+most+recent+first

# In this case a lot of the query to the campaign finance database is being fed
# through the URL.

# Let's get a MM-DD-YYYY for today's date to pass into the URL. We'll replace the
# dates currently in there with {0}.

today_string = date.strftime(date.today(), '%m-%d-%Y')

long_url = 'https://www.elections.il.gov/CampaignDisclosure/DownloadList.aspx?DownloadListType=Receipts&LastOnlyNameSearchType=Starts+with&LastOnlyName=&FirstNameSearchType=Starts+with&FirstName=&AddressSearchType=Starts+with&Address=&CitySearchType=Starts+with&City=&State=&Zip=&ZipThru=&ContributionType=All+Types&OccupationSearchType=Starts+with&Occupation=&EmployerSearchType=Starts+with&Employer=&VendorLastOnlyNameSearchType=Starts+with&VendorLastOnlyName=&VendorFirstNameSearchType=Starts+with&VendorFirstName=&VendorAddressSearchType=Starts+with&VendorAddress=&VendorCitySearchType=Starts+with&VendorCity=&VendorState=&VendorZip=&VendorZipThru=&OtherReceiptsDescriptionSearchType=&OtherReceiptsDescription=&PurposeState=Starts+with&Purpose=&Amount=&AmountThru=&RcvDate={0}&RcvDateThru={0}&Archived=false&QueryType=Contrib&LinkedQuery=false&OrderBy=Date+Received+-+most+recent+first'

# Using Chrome's Developer Tools, we can watch the exchange between the browser
# and the website, than duplicate the response headers that are sent out.

payload = {
    '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$btnText',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': '/wEPDwULLTEyOTE2NTAxMDUPZBYCZg9kFgICAQ9kFhICAw9kFgICAQ9kFgRmDw8WBB4IQ3NzQ2xhc3MFDmxlZnRNZW51SGVhZGVyHgRfIVNCAgJkZAIBDw8WBB8ABRVsZWZ0TWVudUhlYWRlckNvbnRlbnQfAQICFgIeBXN0eWxlBQ1kaXNwbGF5Om5vbmU7ZAIFD2QWAgIBD2QWBGYPDxYEHwAFDmxlZnRNZW51SGVhZGVyHwECAmRkAgEPDxYEHwAFFWxlZnRNZW51SGVhZGVyQ29udGVudB8BAgIWAh8CBQ1kaXNwbGF5Om5vbmU7ZAIHD2QWAgIBD2QWBGYPDxYEHwAFDmxlZnRNZW51SGVhZGVyHwECAmRkAgEPDxYEHwAFFWxlZnRNZW51SGVhZGVyQ29udGVudB8BAgIWAh8CBQ1kaXNwbGF5Om5vbmU7ZAIJD2QWAgIBD2QWBGYPDxYEHwAFDmxlZnRNZW51SGVhZGVyHwECAmRkAgEPDxYEHwAFFWxlZnRNZW51SGVhZGVyQ29udGVudB8BAgIWAh8CBQ1kaXNwbGF5Om5vbmU7ZAILD2QWAgIBD2QWBGYPDxYEHwAFDmxlZnRNZW51SGVhZGVyHwECAmRkAgEPDxYEHwAFFWxlZnRNZW51SGVhZGVyQ29udGVudB8BAgIWAh8CBQ1kaXNwbGF5Om5vbmU7ZAIND2QWAgIBD2QWBGYPDxYEHwAFDmxlZnRNZW51SGVhZGVyHwECAmRkAgEPDxYEHwAFFWxlZnRNZW51SGVhZGVyQ29udGVudB8BAgIWAh8CBQ1kaXNwbGF5Om5vbmU7ZAIPD2QWAgIBD2QWBGYPDxYEHwAFDmxlZnRNZW51SGVhZGVyHwECAmRkAgEPDxYEHwAFFWxlZnRNZW51SGVhZGVyQ29udGVudB8BAgIWAh8CBQ1kaXNwbGF5Om5vbmU7ZAIXDw8WAh4LTmF2aWdhdGVVcmwFHkVsZWN0aW9uSW5mb3JtYXRpb24uYXNweD9JRD0yM2QWAmYPDxYCHgRUZXh0BRdUdWVzZGF5LCBNYXJjaCAxNSwgMjAxNmRkAj4PFgIeCWlubmVyaHRtbAUNRG93bmxvYWQgTGlzdGRkoRQidhsTSMncnEdVcvP+Xmro05Q=',
    '__VIEWSTATEGENERATOR': 'C0457661',
    '__EVENTVALIDATION': '/wEWDAKHkfuRAwKlo/W7AQLQ/PabBgLckKOLAwL3uuXoDAKRh4aQAgLTpeDnCwKbt8nNCAK0ss+BCQL9n+COAgKt7MbzCgLmgNyvCPKcKHXfbl8027eN2h5bYRyzGufA',
    'ctl00$Accordion1_AccordionExtender_ClientState': -1,
    'ctl00$Accordion2_AccordionExtender_ClientState': -1,
    'ctl00$Accordion3_AccordionExtender_ClientState': -1,
    'ctl00$Accordion4_AccordionExtender_ClientState': -1,
    'ctl00$Accordion5_AccordionExtender_ClientState': -1,
    'ctl00$Accordion6_AccordionExtender_ClientState': -1,
    'ctl00$Accordion7_AccordionExtender_ClientState': -1,
    'ctl00$mtbSearch': '',
    'hiddenInputToUpdateATBuffer_CommonToolkitScripts': 1}

page = requests.post(long_url.format(today_string), data=payload)

# The result that comes back is a text file; we'll just send the contents
# along to an outfile.

with open('contributions-{}.txt'.format(today_string), 'wb') as outfile:
    outfile.write(page.content)
