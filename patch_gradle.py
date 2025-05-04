import os

def patch_gradle():
    gradle_file = "/home/nikolai/program/program_phone/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/dists/myapp/build.gradle"
    for path in glob.glob(gradle_file):
        with open(path, 'r+') as f:
            content = f.read()
            content = content.replace(
                "implementation ''com.android.tools.build:gradle:7.4.2''",
                "classpath 'com.android.tools.build:gradle:4.2.2'"
            )
            f.seek(0)
            f.write(content)
            f.truncate()

if __name__ == "__main__":
    import glob
    patch_gradle()
