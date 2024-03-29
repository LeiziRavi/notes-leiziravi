
1.  To remove OpenJDK (the one you've already installed)
    
    `sudo apt-get purge openjdk-\*`
    
2.  Make a new directory for your new JDK
    
    `sudo mkdir -p /usr/local/java`
    
3.  Copy the file to the directory (you should be in that file path)
    
    `sudo cp -r jdk-8u45-linux-x64.tar.gz /usr/local/java/`
    
4.  Extract the file
    
    `sudo tar xvzf jdk-8u45-linux-x64.tar.gz`
    
5.  You should add this to your PATH now. To do that:
    
    a. Open /etc/profile : `sudo gedit /etc/profile`
    
    b. Scroll down (the end) and add the path where your jdk was installed
    
    `JAVA_HOME=/usr/local/java/jdk1.8.0_45 PATH=$PATH:$HOME/bin:$JAVA_HOME/bin export JAVA_HOME export PATH`
    
    Save and exit
    
6.  Inform your Linux system where your Oracle Java JDK/JRE is located.
    
    a. Notify the system that Oracle Java JRE is available for use
    
    `sudo update-alternatives --install "/usr/bin/java" "java" "/usr/local/java/jdk1.8.0_45/bin/java" 1`
    
    b. Notify the system that Oracle Java JDK is available for use
    
    `sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/local/java/jdk1.8.0_45/bin/javac" 1`
    
    c. Notify the system that Oracle Java Web start is available for use
    
    `sudo update-alternatives --install "/usr/bin/javaws" "javaws" "/usr/local/java/jdk1.8.0_20/bin/javaws" 1`
    
7.  Inform your Linux system that Oracle Java JDK/JRE must be the default Java.
    
    a. Set the java runtime environment for the system
    
    `sudo update-alternatives --set java /usr/local/java/jdk1.8.0_45/bin/java`
    
    b. Set the javac compiler for the system
    
    `sudo update-alternatives --set javac /usr/local/java/jdk1.8.0_45/bin/javac`
    
    c. Set Java Web start for the system
    
    `sudo update-alternatives --set javaws /usr/local/java/jdk1.8.0_20/bin/javaws`
    
8.  Reload your system wide PATH
    
    `source /etc/profile`
    
9.  Check the new version and you're done!
    
    `java -version`