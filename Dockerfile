FROM ros:humble

RUN apt-get update -y && apt-get install -y --allow-unauthenticated \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install -U \
    pytest

COPY * /tmp/ros2_rclpy_template_package

RUN rosdep update && rosdep install --from-paths /tmp/ros2_rclpy_template_package --ignore-src -y -r