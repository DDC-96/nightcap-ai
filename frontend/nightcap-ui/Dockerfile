FROM node:18-alpine AS base

FROM base AS deps
WORKDIR /app
RUN apk add --no-cache libc6-compat

# Copy package manager files and install deps
COPY package.json package-lock.json ./
RUN npm ci


FROM base AS builder
WORKDIR /app

# Copy installed node_modules
COPY --from=deps /app/node_modules ./node_modules

# Copy the rest of the frontend app
COPY . .

# Disable telemetry
ENV NEXT_TELEMETRY_DISABLED=1

COPY .env.production .env.production  

# Build the Next.js app
RUN npm run build

# Production runner
FROM base AS runner
WORKDIR /app

ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1
ENV HOSTNAME="0.0.0.0"
ENV PORT=3000

# Create non-root user
RUN addgroup --system --gid 1001 nodejs && \
    adduser --system --uid 1001 nextjs

# Copy assets and build output
COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs
EXPOSE 3000

# Run the production build
CMD ["node", "server.js"]
