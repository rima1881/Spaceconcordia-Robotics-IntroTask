# Space Concordia - Robotics Intro Task - Software

<p>
  This repo contains Intro Task for space concordia Robotics software division. All the info about the task is in task.pdf
</p>


<h2>Before running</h2>

<p>make sure ROS2 is installed on your system. if not you can flow <a href="https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html">this guid</a> to install it</p>

<p>If you don't have access to linux system you can use wsl on windows. All the commands are the same and tested in wsl and it worked 100% fine. for wsl installaion you can flow <a href="https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview">this guid</a></p>


<h2>Runnig the code</h2>

<p>setting up the rus enviroment</p>

> source /opt/ros/humble/setup.bash

<p>install required dependencies</p>

> cd ./cpp

> rosdep install -i --from-path src --rosdistro humble -y

> cd ../python

> rosdep install -i --from-path src --rosdistro humble -y


<h2>Problems and requests</h2>

<p>
  If you have any question or problem with the code please don't hesitate to contact me

  email : amirmohammadgharibipour@gmail.com
</p>
