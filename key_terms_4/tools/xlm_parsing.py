from lxml import etree


class XmlParser:

    def __init__(self, xml_file_name):

        self.headers = list()
        self.texts = list()
        self.root = etree.parse(xml_file_name).getroot()

        for news in self.root[0]:
            for value in news:
                if value.get('name') == 'head':
                    self.headers.append(value.text)
                elif value.get('name') == 'text':
                    self.texts.append(value.text)
