FROM gcc:14.2.0

RUN apt-get update && apt-get install -y cmake

WORKDIR /hw4

COPY src /hw4/src

RUN cmake -S src -B build && cmake --build build

CMD bash -c "g++ --version && cmake --version && ./build/problem1 && ./build/problem2"
