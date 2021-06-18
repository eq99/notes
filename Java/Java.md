# Install



Step1. Install Java

```shell
sudo apt install openjdk- # hit tab to choose your version
```



Step2. Install `gradle`

```shell
# https://gradle.org/install/#configure

sudo mkdir /opt/gradle
sudo unzip -d /opt/gradle gradle-7.0-bin.zip
export PATH=$PATH:/opt/gradle/gradle-7.0/bin
gradle -v
```



