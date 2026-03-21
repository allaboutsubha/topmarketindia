[app]

# (str) Title of your application
title = Akrups Group

# (str) Package name
package.name = akrupsapp

# (str) Package domain
package.domain = com.sathi

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,html,css,js

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3, kivy==2.3.0, pyjnius, android

# (list) Garden requirements
#garden_requirements =

# (list) Supported orientations
orientation = portrait

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, CAMERA, ACCESS_FINE_LOCATION

# (int) Target Android API
android.api = 34

# (int) Minimum API support (Android 9.0)
android.minapi = 28

# (int) Android SDK version to use
#android.sdk = 34

# (str) Android NDK version to use
#android.ndk = 25b

# (bool) Enable AndroidX support
android.enable_androidx = True

# (bool) Automatically accept SDK license
android.accept_sdk_license = True

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name of the Java class that implements Android Activity
android.activity_class_name = org.kivy.android.PythonActivity

# (list) Android app theme
android.apptheme = "@android:style/Theme.NoTitleBar"

# (str) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup
android.allow_backup = True

# (str) Android logcat filters
android.logcat_filters = *:S python:D

# (str) The format used to package the app
android.debug_artifact = apk
android.release_artifact = aab

# (list) Meta-data to add to the AndroidManifest.xml
android.meta_data = android.webkit.WebView.EnableSafeBrowsing=true

# (str) Extra xml to write into the AndroidManifest.xml
android.manifest.application_arguments = android:usesCleartextTraffic="true"

[buildozer]
# (int) Log level (1 = error, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1