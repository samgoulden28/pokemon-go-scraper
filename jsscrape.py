import sys  
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  
from lxml import html 

#Take this class for granted.Just use result of rendering.
class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()  

url = 'https://pokevision.com/#/@51.07005488929763,-1.3184666633605957'  
r = Render(url)  
result = r.frame.toHtml()
#print(result.encode("utf-8"))

tree = html.fromstring(result.encode("utf-8"))

#Finding all anchor tags in response
pokemon = tree.xpath('//div[@class="leaflet-marker-pane"]/div/img/@src')

print(len(pokemon))
print(pokemon)