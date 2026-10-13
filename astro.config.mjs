import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
export default defineConfig({ site: 'https://recruitmentai.org', integrations: [sitemap()], trailingSlash: 'always', build: { format: 'directory' } });
