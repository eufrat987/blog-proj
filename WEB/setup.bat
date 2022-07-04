if not exist app docker compose run next npx create-next-app@latest app --typescript
docker compose run next npm --prefix app install @mui/material @emotion/react @emotion/styled @emotion/server
docker compose run next npm --prefix app install