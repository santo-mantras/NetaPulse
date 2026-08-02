# Step 1: Build the React application
FROM node:20-alpine AS build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the application for production
RUN npm run build

# Step 2: Serve the application using Nginx
FROM nginx:alpine

# Copy the built assets from the previous stage
COPY --from=build /app/dist /usr/share/nginx/html/jumlabaaz

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
