import pytest

import rclpy
from std_msgs.msg import String
from ros2_rclpy_template_package.simple_publisher import SimplePublisher

class Subscriber:
    """
    Subscribes to a topic
    """
    def __init__(self, topic: str, msg_type, node: rclpy.node.Node) -> None:

        self._sub = node.create_subscription(
            msg_type,
            topic=topic,
            callback=self._callback,
            qos_profile=10,
        )

        self._msgs = list()

    @property
    def num_messages(self) -> int:
        """Get the number of messages received"""
        return len(self._msgs)

    def _callback(self, msg) -> None:
        """Subscriber callback method"""
        self._msgs.append(msg)

def test_node():

    rclpy.init(args=None)

    simple_publisher = SimplePublisher()
    sub = Subscriber("topic", String, simple_publisher)

    for _ in range(5):
        rclpy.spin_once(simple_publisher)

    assert sub.num_messages > 0, "Failed to publish messages"

    simple_publisher.destroy_node()
    rclpy.shutdown()