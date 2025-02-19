FROM gcc:14.2.0 AS build

RUN apt-get update && apt-get install -y cmake

WORKDIR /hw5

COPY src /hw5/src

FROM build AS compile

COPY --from=build /hw5 /hw5

RUN cmake -S src -B build && cmake --build build

CMD bash -c "g++ --version && cmake --version && ./build/min_heap"
