import React, {useRef, useState} from 'react';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import useBaseUrl from '@docusaurus/useBaseUrl';

const launchLinks = [
  ['F01', 'Read the manual', '/docs/intro', 'boot F01 /docs/intro'],
  ['F02', 'Install JarvisOS', '/docs/getting-started/quick-start', 'mount jarvis-os skill'],
  ['F03', 'Open prompts', '/docs/reference/prompt-library', 'cat prompt-library.md'],
  ['F04', 'Specialist Mode', '/docs/modes/specialist-mode', 'boot specialist-mode'],
];

const artifactLinks = [
  ['memory', 'memory/projects/', 'markdown state across chats', '/docs/concepts/memory', 'open memory/projects/'],
  ['handoffs', 'handoffs/*.md', 'fresh context without re-explaining', '/docs/concepts/handoffs', 'tail handoffs/*.md'],
  ['quality', 'operations/quality-gates.md', 'verification before claims', '/docs/operations/quality-gates', 'verify quality-gates.md'],
  ['skill tickets', 'templates/skill-ticket.md', 'turn real projects into reusable upgrades', '/docs/operations/cross-project-contributions', 'new skill-ticket.md'],
];

const defaultCommand = 'Jarvis, use JARVIS OS.';
const defaultArchiveStatus = '4 files mounted';

export default function Home() {
  const hero = useBaseUrl('/img/landing/archive-room-hero.png');
  const seal = useBaseUrl('/img/landing/holo-seal.png');
  const [terminalCommand, setTerminalCommand] = useState(defaultCommand);
  const [terminalStatus, setTerminalStatus] = useState('invoke');
  const [archiveStatus, setArchiveStatus] = useState(defaultArchiveStatus);
  const statusTimer = useRef(null);
  const resetTimer = useRef(null);

  const cancelReset = () => {
    if (resetTimer.current) {
      clearTimeout(resetTimer.current);
      resetTimer.current = null;
    }
  };

  const flashTerminalStatus = (status) => {
    if (statusTimer.current) {
      clearTimeout(statusTimer.current);
    }
    setTerminalStatus(status);
    statusTimer.current = setTimeout(() => setTerminalStatus('invoke'), 1100);
  };

  const copyTerminalCommand = async () => {
    try {
      await navigator.clipboard.writeText(terminalCommand);
      flashTerminalStatus('copied');
    } catch {
      flashTerminalStatus('select');
    }
  };

  const resetTerminal = () => {
    cancelReset();
    setTerminalCommand(defaultCommand);
    setArchiveStatus(defaultArchiveStatus);
  };

  const scheduleReset = () => {
    cancelReset();
    resetTimer.current = setTimeout(resetTerminal, 220);
  };

  const showCommand = (command) => {
    cancelReset();
    setTerminalCommand(command);
  };

  return (
    <Layout
      title="JarvisOS Docs"
      description="JARVIS OS documentation for local-first Codex continuity."
    >
      <main
        className="landing"
        data-command-state={terminalCommand === defaultCommand ? 'idle' : 'active'}
        style={{ '--hero-image': `url(${hero})` }}
      >
        <section className="heroStage">
          <div className="heroShade" />
          <div className="heroContent">
            <div className="heroEyebrow">local markdown memory / codex operating layer</div>
            <h1>JARVIS OS</h1>
            <p>
              A visible filesystem for agent continuity: memory, handoffs, task state,
              artifact discipline, and governed self-improvement.
            </p>
            <nav className="launchDock" aria-label="Primary documentation links">
              {launchLinks.map(([key, label, href, command]) => (
                <Link
                  key={label}
                  to={href}
                  onBlur={scheduleReset}
                  onFocus={() => showCommand(command)}
                  onPointerEnter={() => showCommand(command)}
                  onPointerLeave={scheduleReset}
                >
                  <span>{key}</span>
                  <b>{label}</b>
                </Link>
              ))}
            </nav>
          </div>
          <img className="sealAsset" src={seal} alt="" aria-hidden="true" />
          <div
            className="terminalStrip"
            data-state={terminalCommand === defaultCommand ? 'idle' : 'active'}
            aria-label="JarvisOS invocation"
            role="button"
            tabIndex={0}
            onBlur={scheduleReset}
            onClick={() => void copyTerminalCommand()}
            onFocus={cancelReset}
            onKeyDown={(event) => {
              if (event.key === 'Enter' || event.key === ' ') {
                event.preventDefault();
                void copyTerminalCommand();
              }
            }}
            onPointerEnter={cancelReset}
            onPointerLeave={scheduleReset}
          >
            <span aria-live="polite">{terminalStatus}</span>
            <code key={terminalCommand}>{terminalCommand}</code>
          </div>
        </section>

        <section className="artifactBand" aria-label="JarvisOS documentation routes">
          <div className="artifactIntro">
            <span>docs archive</span>
            <h2>Open the system files.</h2>
            <p>Four durable files that explain how JARVIS keeps continuity inspectable.</p>
          </div>
          <div className="archiveBay">
            <div className="archiveBayHeader">
              <span>volume /JarvisOS</span>
              <code key={archiveStatus} data-state={archiveStatus === defaultArchiveStatus ? 'idle' : 'active'}>
                {archiveStatus}
              </code>
            </div>
            <div className="artifactRows">
              {artifactLinks.map(([name, path, detail, href, command], index) => (
                <Link
                  className="artifactRow"
                  to={href}
                  key={name}
                  onBlur={scheduleReset}
                  onFocus={() => {
                    showCommand(command);
                    setArchiveStatus(`slot ${String(index + 1).padStart(2, '0')} / ${name}`);
                  }}
                  onPointerEnter={() => {
                    showCommand(command);
                    setArchiveStatus(`slot ${String(index + 1).padStart(2, '0')} / ${name}`);
                  }}
                  onPointerLeave={scheduleReset}
                >
                  <span className="fileIndex">{String(index + 1).padStart(2, '0')}</span>
                  <span className="fileMeta">
                    <b>{name}</b>
                    <code>{path}</code>
                  </span>
                  <em>{detail}</em>
                  <span className="fileAction">open</span>
                </Link>
              ))}
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}
