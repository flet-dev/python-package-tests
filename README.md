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

| Name          | Version      | Tests |
|---------------|--------------|-----|
| aiohttp       | 3.9.5 |     |
| argon2-cffi-bindings | 21.2.0 | |
| bcrypt | 4.2.0 | |
| bitarray | 2.9.2 | |
| blis | 1.0.0 | |
| Brotli | 1.1.0 | |
| cffi | 1.17.1 | |
| contourpy | 1.3.0 | |
| cryptography | 43.0.1 | |
| fiona | 1.10.1 | |
| GDAL | 3.10.0 | |
| google-crc32 | 1.6.0 | |
| grpcio | 1.67.1 | |
| jq | 1.8.0 | flet==0.25.2 android :white_check_mark: iOS:white_check_mark:  |
| kiwisolver | 1.4.7 | |
| lru-dict | 1.3.0 | |
| lxml | 5.3.0 | |
| MarkupSafe | 2.1.5 | |
| matplotlib | 3.9.2 | |
| msgpack | 1.1.0 | |
| msgspec | 0.8.16 | |
| numpy | 2.1.1 | flet==0.25.2 android :white_check_mark: iOS :x:  |
| numpy | 1.26.4 | |
| opaque | 0.2.0 | |
| opencv-python | 4.10.0.84 | |
| pandas | 2.2.2 | |
| pendulum | 3.0.0 | |
| pillow | 10.4.0 | |
| protobuf | 5.28.3 | |
| pycryptodome | 3.21.0 | |
| pycryptodomex | 3.21.0 | |
| pydantic-core | 2.23.3 | |
| pyjnius (Android only) | 1.6.1 | |
| PyNaCl | 1.5.0 | |
| pyobjus (iOS only) | 1.2.3 | |
| pyogrio | 0.10.0 | |
| pyproj | 3.7.0 | |
| pysodium | 0.7.18 | |
| PyYAML | 6.0.2 | |
| regex | 2024.11.6 | |
| ruamel.yaml.clib | 0.2.12 | |
| shapely | 2.0.6 | |
| SQLAlchemy | 2.0.36 | |
| time-machine | 2.16.0 | |
| websockets | 13.0.1 | |
| yarl | 1.11.1 | |
| zstandard | 0.23.0 | |