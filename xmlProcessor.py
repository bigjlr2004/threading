import xml.sax
import xml.sax.handler

class XMLHandler(xml.sax.ContentHandler):
   def __init__(self):
      self.CurrentData = ""
      self.model = ""
      self .speed = ""
      self.special = ""
   
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "car":
         print("----CAR----")
         name = attributes["name"]
         print("Name: ", name)
   
   def endElement(self, tag):
      if self.CurrentData == "model":
         print("Model: ", self.model)
      elif self.CurrentData == "speed":
         print("Speed: ", self.speed)
      elif self.CurrentData == "special":
         print("Special: ", self.special)

      self.CurrentData = "" 
   
   def characters(self, content):
      if self.CurrentData == "model":
         self.model = content
      elif self.CurrentData == "speed":
         self.speed = content
      elif self.CurrentData == "special":
         self.special = content
      
if (__name__ == "__main__"):
   parser = xml.sax.make_parser()
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   Handler = XMLHandler()
   parser.setContentHandler(Handler)

   parser.parse("example.xml")