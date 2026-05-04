const sidebars = {
  tutorialSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Getting Started',
      items: [
        'getting-started/quick-start',
        'getting-started/install-skill',
        'getting-started/fresh-chat',
      ],
    },
    {
      type: 'category',
      label: 'Core Concepts',
      items: [
        'concepts/mental-model',
        'concepts/memory',
        'concepts/handoffs',
        'concepts/artifact-hygiene',
        'concepts/self-improvement',
      ],
    },
    {
      type: 'category',
      label: 'Modes',
      items: [
        'modes/light-mode',
        'modes/specialist-mode',
        'modes/adoption-mode',
        'modes/rd-loop',
      ],
    },
    {
      type: 'category',
      label: 'Operations',
      items: [
        'operations/reference-router',
        'operations/skill-dictionary',
        'operations/skill-composition',
        'operations/agent-work-pack',
        'operations/jarvis-doctor',
        'operations/task-lifecycle',
        'operations/quality-gates',
        'operations/cross-project-contributions',
        'operations/skill-quality-standard',
        'operations/sunset-review-ledger',
        'operations/public-artifacts',
        'operations/release-and-github-pages',
      ],
    },
    {
      type: 'category',
      label: 'Reference',
      items: [
        'reference/folder-structure',
        'reference/capability-index',
        'reference/prompt-library',
        'reference/checklists',
      ],
    },
  ],
};

module.exports = sidebars;
