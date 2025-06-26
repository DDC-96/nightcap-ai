/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',
  async headers() {
    return [
      {
        source: '/(.*)', // apply to all routes
        headers: [
          {
            key: 'Content-Security-Policy',
            value:
              "default-src 'self'; img-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; connect-src 'self' https://api.cruzdaniel.dev; frame-ancestors 'none';",
          },
        ],
      },
    ];
  },
};

module.exports = nextConfig;

// Add CSP  
// default-src 'self': No external sources unless explicitly allowed
// img-src 'self': Images must come from your own domain
// script-src 'self': No third-party scripts allowed
// style-src 'self' 'unsafe-inline': Styles are local; inline allowed for now (but consider reducing this later)
// connect-src https://api.cruzdaniel.dev: Only your backend can be contacted
// frame-ancestors 'none': No embedding your site via <iframe>


