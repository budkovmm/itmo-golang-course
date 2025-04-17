FROM ubuntu:22.04

# Install bash (already included in Ubuntu base image)
RUN apt-get update && apt-get install -y bash

# Copy the script into the container
COPY shuffle.sh /shuffle.sh

# Make the script executable
RUN chmod +x /shuffle.sh

# Set the default command to run the script
CMD ["/shuffle.sh"]