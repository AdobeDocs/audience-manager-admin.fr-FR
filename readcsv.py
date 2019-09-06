#!/usr/local/bin/python

import csv
import os
import frontmatter
import re
import urllib2

md_map = {}
xml_map = {}
html_map = {}
machtml_map = {}
uuids = set()

dir_path = os.path.dirname(os.path.realpath(__file__))


# read in html files from docs.adobe.com to get uuid
for root, dirs, files in os.walk(dir_path + '/aem'):
    for file in files:
        if file.endswith('.html'):
            article = root + '/' + str(file)
            article = os.path.relpath(root + '/' + str(file), dir_path)
            htmlfile = open(article, 'r')
            for line in htmlfile:
                if 'name="uuid"' in line:
                    uuid = line.split('"')[3]
                    url = re.sub('^aem', 'https://docs.adobe.com', article)
                    html_map[uuid] = url

            htmlfile.close()


# read markdown files to get uuid
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.md'):
            article = os.path.relpath(root + '/' + str(file), dir_path)
            yaml = frontmatter.load(article)
            if 'uuid' in yaml.keys():
                md_map[yaml['uuid']] = article
                uuids.add(yaml['uuid'])


# read in uuid mapping files
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.csv') and 'uuid_mapping' in str(file):
            with open(root + '/' + str(file)) as uuid_map:
                csv_reader = csv.reader(uuid_map, quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True, delimiter=',')
                for row in csv_reader:
                    if 'UUID' in row[1]:
                        continue
                    xml_map[row[1]] = row[0]  # re.sub('analytics-master', 'https://marketing.adobe.com/resources/help/en_US/reference', row[0])
                    # print(row[0])
                    uuids.add(row[1])


# read in list of urls from marketing.adobe.com
print('"deeplink","uuid","xml src","md src","marketing loc","docs loc"')
with open('aamurls.txt') as macurls:
    for markurl in macurls:
        found = False
        markurl = markurl.rstrip()
        docsurl = ''
        md_map_index = ''
        if '.html' in markurl:
            xmlfilename = markurl.split('/')[-1].replace('.html', '.xml')
            # scrubbed_xmlfilename = re.sub(r"^[tcr]_", "", xmlfilename)
            scrubbed_xmlfilename = xmlfilename

            # search for the uuid for the xmlfile
            for entry in xml_map.values():
                if xmlfilename in entry or scrubbed_xmlfilename in entry:
                    uuid = xml_map.keys()[xml_map.values().index(entry)]
                    if uuid in html_map:
                        docsurl = html_map[uuid]
                        machtml_map[uuid] = markurl
                        # print('    FOUND1: ' + markurl + ': ' + docsurl + ' [' + uuid + ']')
                        print('" ","' + str(uuid) + '","' + str(entry) + '","' + md_map[uuid] + '","' + str(markurl) + '","' + str(docsurl) + '"')

            # search the markdown files
            if docsurl == '':
                for entry in md_map.values():
                    found = False
                    with open(entry, 'r') as markdownfile:
                        contents = markdownfile.readlines()
                        deeplink = ''
                        for s in contents:
                            foundmatch = False
                            z = re.match(r"^#.*?[{](#.*?)[}]", s)
                            if z:
                                if len(z.groups()) > 0:
                                    deeplink = z.group(1)
                            for t in s.split():
                                if t == xmlfilename:
                                    foundmatch = True
                            # if xmlfilename in s or scrubbed_xmlfilename in s:
                            if foundmatch:
                                md_map_index = md_map.keys()[md_map.values().index(entry)]
                                if md_map_index in html_map.keys():
                                    docsurl = html_map[md_map_index] + deeplink
                                    machtml_map[md_map_index] = markurl
                                    # print('    FOUND2: ' + markurl + ': ' + docsurl + '[' + md_map_index + '] deep')
                                    # print(md_map_index + ',' + entry + ',' + md_map[md_map_index] + ',' + markurl + ',' + docsurl)
                                    print('"x","' + str(md_map_index) + '","' + str(xmlfilename) + '","' + str(entry) + '","' + str(markurl) + '","' + str(docsurl) + '"')
                                    found = True
                                else:
                                    if not found:
                                        machtml_map[md_map_index] = ''
            if docsurl == '':
                docsurl = 'NOT FOUND ' + str(found)
            if 'NOT FOUND' in docsurl and md_map_index != '':
                # print(md_map_index + ',' + entry + ',' + md_map[md_map_index] + ',' + markurl + ',' + '""')
                docsurl = ''
                print('" ","' + str(md_map_index) + '","' + str(entry) + '","' + str(md_map[md_map_index]) + '","' + str(markurl) + '","' + str(docsurl) + '"')                    


# exit(0)
# print('"uuid","xml src","md src","marketing loc","docs loc"')
# uuidlist = {uuids.pop()}
for uuid in uuids:
    xmlfile = ''
    mdfile = ''
    docsurl = ''
    markurl = ''
    if uuid in xml_map.keys():
        xmlfile = xml_map[uuid]
    if uuid in md_map.keys():
        mdfile = md_map[uuid]
    if uuid in html_map.keys():
        docsurl = html_map[uuid]
        # if docsurl != '':
        #     try:
        #         ret = urllib2.urlopen(docsurl)
        #         # docsurl = str(ret.code) + ' ' + docsurl
        #     except:
        #         docsurl = 'INVALID: ' + docsurl

    if uuid in machtml_map.keys():
        markurl = machtml_map[uuid]
        # if markurl != '':
        #     try:
        #         ret = urllib2.urlopen(markurl)
        #         # markurl = str(ret.code) + ' ' + markurl
        #     except:
        #         markurl = 'INVALID: ' + markurl
    
    print('" ","' + str(uuid) + '","' + str(xmlfile) + '","' + str(mdfile) + '","' + str(markurl) + '","' + str(docsurl) + '"')
    
    
