# Step 1: Build the React application
FROM node:20-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Use BASE_PATH arg to allow overriding vite base path
ARG BASE_PATH=/jumlabaaz/
RUN sed -i "s|base: '/jumlabaaz/'|base: '${BASE_PATH}'|" vite.config.ts
RUN npm run build

# Step 2: Serve the application using Nginx
FROM nginx:alpine

# Copy custom nginx config for flexible port
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy the built assets
COPY --from=build /app/dist /usr/share/nginx/html

# HF Spaces uses 7860, local uses 80
EXPOSE 7860

CMD ["nginx", "-g", "daemon off;"]
