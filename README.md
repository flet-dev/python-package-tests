# python-package-tests
Small apps testing Flet binary Python packages

To test an app on Android device:
1. In Android studio, add new device with Tools -> Devices
2. In terminal, while in directory when pyproject.toml for your app is, run `flet build apk -v` command. It will create build folder with apk folder and app-release.apk file in it.
3. Install apk on the Android device by drag and drop `app-release.apk` to the device. 
4. Open the app and click on the button to run the test.
