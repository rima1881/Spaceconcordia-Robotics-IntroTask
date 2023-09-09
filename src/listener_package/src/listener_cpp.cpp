
#include <functional>
#include <memory>
#include <iostream>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using std::placeholders::_1;


class listener : public rclcpp::Node
{
  public:

  //public methods
  listener() : Node("listener_cpp") {
    subscription_ = this->create_subscription<std_msgs::msg::String>(
    "new_message", 10, std::bind(&listener::topic_callback, this, _1));
  }

private:

  //private methods
  void topic_callback(const std_msgs::msg::String & msg) const {
    RCLCPP_INFO(this->get_logger(), "> '%s'", msg.data.c_str());
  }

  //private props
  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
};



int main(int argc, char ** argv) {
  
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<listener>());
  rclcpp::shutdown();

  return 0;
}
