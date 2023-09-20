FROM ros:humble

RUN apt-get update -y && apt-get install -y --allow-unauthenticated \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install -U \
    pytest