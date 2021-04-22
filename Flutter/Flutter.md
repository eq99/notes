# Install



```shell
# https://flutter.dev/docs/get-started/install/linux
sudo snap install flutter --classic
# https://developer.android.com/studio

flutter sdk-path
which flutter
which flutter dart
```



可能出现的问题：

1. 卡在 `Running "flutter pub get" in flutter_tools...`

```shell
export PUB_HOSTED_URL=https://pub.flutter-io.cn
export FLUTTER_STORAGE_BASE_URL=https://storage.flutter-io.cn
```





[KVM 加速（可选）](https://developer.android.com/studio/run/emulator-acceleration?utm_source=android-studio#vm-linux)

```shell
$ sudo apt-get install cpu-checker
$ egrep -c '(vmx|svm)' /proc/cpuinfo
12
$ kvm-ok
INFO: /dev/kvm exists
KVM acceleration can be used
```



