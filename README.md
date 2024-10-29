# python-package-tests
Small apps testing Flet binary Python packages

To test an app on Android device:
1. In Android studio, add new device with Tools -> Devices
2. In terminal, in the same folder where `pyproject.toml` for your app is, run `flet build apk -v` command. It will create `build` folder with `apk` folder and `app-release.apk` file in it.
3. Install apk on the Android device by draging and dropping `app-release.apk` to the device. 
4. Open the app and click on the button to run the test.

To test an app on iPhone simulator
1. In xCode, open Simulator
2. In terminal, in directory where `pyproject.toml` for your app is, run `flet build ipa -v` command. It will create `build` folder with    `flutter`, `ipa` and `site-packages` folders.
3. Set environment variable `export SERIOUS_PYTHON_SITE_PACKAGES=[Path-to-site-packages]`
4. When in `flutter` folder, run `flutter run` command
5. On prompt, select iPhone simulator as your device -> the app will open in Simulator
4. Open the app and click on the button to run the test.
