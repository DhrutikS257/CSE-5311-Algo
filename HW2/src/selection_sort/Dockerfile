# Use an official GCC image as the base
FROM gcc:14.2.0

# Install CMake and other build tools
RUN apt-get update && apt-get install -y cmake make

# Set the working directory
WORKDIR /app

# Copy the C++ source files into the container
# Use separate COPY commands for caching purposes
COPY src/selection_sort/CMakeLists.txt /app/src/selection_sort/CMakeLists.txt
COPY src/selection_sort /app/src/selection_sort

# Pre-build step to generate build files
RUN mkdir -p build && cd build && cmake ../src/selection_sort

# Build the C++ code
RUN cd build && make

# Set the default command to run the compiled program
CMD ["./build/main"]
