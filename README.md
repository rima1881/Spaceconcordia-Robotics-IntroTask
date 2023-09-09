# Space Concordia - Robotics Intro Task - Software

<p>
  This repo contains Intro Task for space concordia Robotics software division. All the info about the task is in task.pdf
</p>


<h2>description</h2>
<p>this repo contains two packages. my_client_package written in python and listener_package written in c++.</p>


<p>my client package contains two nodes (talker,listener). talker and listener use publisher(talker)/subscription(listener) model to send and receive strings under the topic of 'new_message'</p>

<p>listener package only contains listener_cpp node. listener_cpp uses to catch strings send under the 'new_messages' topic.</p>

<h2>Before running</h2>

<p>make sure ROS2 is installed on your system. if not you can follow <a href="https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html">this guide</a> to install it</p>

<p>If you don't have access to linux system you can use wsl on windows. All the commands are the same and tested in wsl. for wsl installaion you can follow <a href="https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview">this guide</a></p>




<h2>runnig the code</h2>

<p>compiling</p>
<p>go to director of the package you want to compile and run the following comand</p>

> colcon build


<p>local installion</p>

> source install/local_setup.bash

<p>running</p>

> ros2 run <package> <node>

<h2>Problems and requests</h2>

<p>
  If you have any question or problem with the code please don't hesitate to contact me

  email : amirmohammadgharibipour@gmail.com
</p>
