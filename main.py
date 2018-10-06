from frame import AppFrame
import sys,os, platform
import wx

if __name__ == '__main__':
    args = sys.argv
    THISPYFILE = args.pop(0)
    argc = len(args)
    path = os.path.dirname(os.path.abspath(__file__))
<<<<<<< HEAD
    print(path)
=======
>>>>>>> 225823ba9bdabedf7d5f053b6dce37bae040cfb3
    app = wx.App(redirect = False)
    appFrame = AppFrame.AppFrame(args, argc,file_path = path)
    import wx.lib.inspection
    app.MainLoop()
