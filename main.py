from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from kivy.clock import Clock

class BulkUploadApp(App):
    def build(self):
        self.layout = BoxLayout()
        if platform == 'android':
            # ৩ সেকেন্ড অপেক্ষা করুন যাতে ফোনের জিপিইউ (GPU) রেডি হয়
            Clock.schedule_once(self.load_webview, 3)
        return self.layout

    def load_webview(self, *args):
        from jnius import autoclass
        from android.runnable import run_on_ui_thread

        @run_on_ui_thread
        def create_view():
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            WebView = autoclass('android.webkit.WebView')
            WebViewClient = autoclass('android.webkit.WebViewClient')
            activity = PythonActivity.mActivity
            
            webview = WebView(activity)
            settings = webview.getSettings()
            # ব্ল্যাক স্ক্রিন তাড়াতে নিচের ৩টি লাইন মাস্ট:
            settings.setJavaScriptEnabled(True) 
            settings.setDomStorageEnabled(True)
            settings.setDatabaseEnabled(True)
            
            webview.setWebViewClient(WebViewClient())
            webview.loadUrl("https://akrupsgroupofcompanies.info/")
            activity.setContentView(webview)
            
        create_view()

if __name__ == '__main__':
    BulkUploadApp().run()