FROM node:20-alpine

WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose port 7860 for Hugging Face Spaces compatibility
EXPOSE 7860

# Build at runtime and serve via Vite preview on port 7860
CMD ["sh", "-c", "npm run build && npx vite preview --port 7860 --host 0.0.0.0"]
