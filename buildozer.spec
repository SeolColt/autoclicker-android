[app]

# App info
title = Auto Clicker
package.name = autoclicker
package.domain = org.autoclicker

# Source code
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Version
version = 4.0

# Requirements
requirements = python3,kivy

# Permissions
android.permissions = INTERNET,ACCESS_SUPERUSER

# Android API
android.api = 30
android.minapi = 21
android.ndk = 23b

# Build settings
android.release_artifact = apk
android.arch = arm64-v8a

# Orientation
orientation = portrait

# Fullscreen
fullscreen = 0

# Android specific
android.allow_backup = True
