# Pull official latest Node Docker image
FROM --platform=linux/amd64 node:latest

# Set to use PNPM
RUN npm i -g pnpm

# Set the working directory
WORKDIR /usr/frontend

# Set the server port
EXPOSE 3000

# Install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# Install Node dependencies
COPY ./.npmrc ./package.json ./pnpm-lock.yaml ./
RUN pnpm install

# Copy all files
COPY . .

# Add entrypoint.sh to synchronize the startup with the backend server
COPY ./entrypoint.sh .
RUN chmod +x /usr/frontend/entrypoint.sh

# Execute entrypoint.sh
ENTRYPOINT ["/usr/frontend/entrypoint.sh"]

# Start up the frontend server
CMD [ "pnpm", "start" ]
