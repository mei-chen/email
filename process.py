import pandas as pd
import xml.etree.ElementTree as ET
import io
import xmltodict

with open('PE-Conservatives-Donation-Subscription.xml') as fd:
    doc = xmltodict.parse(fd.read())

print(doc)