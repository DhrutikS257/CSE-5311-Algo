FROM gcc:14.2.0

RUN apt-get update && apt-get install -y cmake

WORKDIR /dy_arr

COPY . /dy_arr/

RUN cmake -S . -B build && cmake --build build

CMD ["./build/dynamic_array"]
