// @ts-check

const config = {
  title: 'JARVIS OS',
  tagline: 'Local-first continuity for Codex agents',
  favicon: 'img/jarvisos-banner.png',
  url: 'https://moleh1307.github.io',
  baseUrl: '/JarvisOS/',
  organizationName: 'moleh1307',
  projectName: 'JarvisOS',
  trailingSlash: false,
  onBrokenLinks: 'throw',
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },
  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.js',
          routeBasePath: 'docs',
          editUrl: 'https://github.com/moleh1307/JarvisOS/tree/main/website/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      },
    ],
  ],
  themeConfig: {
    image: 'img/jarvisos-banner.png',
    navbar: {
      title: 'JARVIS OS',
      logo: {
        alt: 'JARVIS OS',
        src: 'img/jarvisos-banner.png',
      },
      items: [
        { to: '/docs/intro', label: 'Docs', position: 'left' },
        { to: '/docs/getting-started/quick-start', label: 'Quick Start', position: 'left' },
        { to: '/docs/modes/light-mode', label: 'Modes', position: 'left' },
        {
          href: 'https://github.com/moleh1307/JarvisOS',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Learn',
          items: [
            { label: 'Introduction', to: '/docs/intro' },
            { label: 'Quick Start', to: '/docs/getting-started/quick-start' },
            { label: 'Specialist Mode', to: '/docs/modes/specialist-mode' },
          ],
        },
        {
          title: 'Operate',
          items: [
            { label: 'Memory', to: '/docs/concepts/memory' },
            { label: 'Handoffs', to: '/docs/concepts/handoffs' },
            { label: 'Task Lifecycle', to: '/docs/operations/task-lifecycle' },
          ],
        },
        {
          title: 'Project',
          items: [
            { label: 'GitHub', href: 'https://github.com/moleh1307/JarvisOS' },
            { label: 'README', href: 'https://github.com/moleh1307/JarvisOS#readme' },
          ],
        },
      ],
      copyright: `Copyright ${new Date().getFullYear()} JARVIS OS. Built as local-first markdown infrastructure.`,
    },
    prism: {
      additionalLanguages: ['bash'],
    },
  },
};

module.exports = config;
