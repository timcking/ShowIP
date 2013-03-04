import socket
import wx
from wx import xrc


class MyApp(wx.App):

    def OnInit(self):
        self.res = xrc.XmlResource('gui.xrc')
        self.init_frame()
        return True

    def init_frame(self):
        self.frame = self.res.LoadFrame(None, 'frameMain')

        # Bind Controls
        self.lblIP = xrc.XRCCTRL(self.frame, 'lblIP')
        self.btnOK = xrc.XRCCTRL(self.frame, 'wxID_OK')
        self.btnOK.SetDefault()

        # Bind Events
        self.frame.Bind(wx.EVT_BUTTON, self.OnClose, id=xrc.XRCID('wxID_OK'))
        self.lblIP.SetLabel(self.getIP())
        
        self.frame.Show()

    def getIP(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("gmail.com",80))
        ip = s.getsockname()[0]
        s.close()
        return ip
        
    def OnClose(self, evt):
        self.Exit()    

if __name__ == '__main__':
    print "here"
    app = MyApp(False)
    app.MainLoop()