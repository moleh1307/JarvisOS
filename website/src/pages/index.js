import React from 'react';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';

const operatingLayers = [
  ['Memory', 'projects, decisions, sessions, preferences'],
  ['Handoff', 'current objective, blockers, exact next action'],
  ['Specialist Mode', 'roles, work orders, review gates'],
  ['Artifact Hygiene', 'canonical outputs, proof, caveats'],
  ['Learning', 'candidate, repeated, promoted, rejected'],
];

const systemSignals = [
  ['Local-first', 'Markdown stays on your machine and remains inspectable.'],
  ['Continuity-first', 'Fresh chats inherit project state instead of starting cold.'],
  ['Governed autonomy', 'JARVIS OS can improve, but rules change only with evidence.'],
];

const workflowSteps = [
  ['01', 'Retrieve', 'Load the smallest useful memory before meaningful work.'],
  ['02', 'Operate', 'Use light mode for simple tasks and Specialist Mode when structure earns its keep.'],
  ['03', 'Verify', 'Check artifacts, builds, screenshots, caveats, and release boundaries.'],
  ['04', 'Preserve', 'Write the next useful action back into markdown.'],
];

function ContinuityConsole() {
  return (
    <div className="continuityConsole" aria-label="JarvisOS continuity console">
      <div className="consoleHeader">
        <span className="consoleDot consoleDotHot" />
        <span className="consoleDot consoleDotWarm" />
        <span className="consoleDot consoleDotCool" />
        <span className="consolePath">~/JARVIS</span>
      </div>
      <div className="consoleBody">
        <div className="fileRail">
          <div className="railTitle">memory/</div>
          {operatingLayers.map(([label, detail]) => (
            <div className="fileRow" key={label}>
              <span>{label}</span>
              <small>{detail}</small>
            </div>
          ))}
        </div>

        <div className="engineCore">
          <div className="engineRing">
            <div className="engineMark">JOS</div>
            <div className="engineSub">continuity kernel</div>
          </div>
          <div className="signalLine signalLineOne" />
          <div className="signalLine signalLineTwo" />
          <div className="signalLine signalLineThree" />
        </div>

        <div className="handoffPanel">
          <div className="panelEyebrow">handoff.md</div>
          <p>Goal: redesign landing page</p>
          <p>Scope: landing only</p>
          <p>Next: build, inspect, deploy</p>
          <div className="statusStack">
            <span>build pending</span>
            <span>visual QA pending</span>
          </div>
        </div>
      </div>
      <div className="consoleFooter">
        <span>artifact: canonical</span>
        <span>confidence: verified after checks</span>
      </div>
    </div>
  );
}

export default function Home() {
  return (
    <Layout
      title="Local-first continuity for Codex"
      description="JARVIS OS is a local-first markdown operating system for Codex continuity."
    >
      <main className="landingPage">
        <section className="heroJarvis">
          <div className="heroShell">
            <div className="heroCopy">
              <div className="heroKicker">
                <span>Local-first agent continuity</span>
                <span>for Codex</span>
              </div>
              <h1 className="heroTitle">An operating system for agent memory.</h1>
              <p className="heroLead">
                JARVIS OS turns scattered Codex chats into durable local continuity:
                markdown memory, clean handoffs, Specialist Mode, artifact hygiene,
                and governed self-improvement.
              </p>
              <div className="heroActions">
                <Link className="commandButton commandButtonPrimary" to="/docs/intro">
                  Read the docs
                </Link>
                <Link className="commandButton commandButtonSecondary" to="/docs/getting-started/quick-start">
                  Quick start
                </Link>
              </div>
            </div>
            <ContinuityConsole />
          </div>
        </section>

        <section className="signalStrip" aria-label="JarvisOS operating signals">
          {systemSignals.map(([title, body]) => (
            <article className="signalItem" key={title}>
              <strong>{title}</strong>
              <span>{body}</span>
            </article>
          ))}
        </section>

        <section className="workflowBand">
          <div className="sectionIntro">
            <span className="sectionKicker">The loop</span>
            <h2>Not a persona. A continuity protocol.</h2>
            <p>
              JARVIS OS gives agents a repeatable way to recover context, do the work,
              verify the output, and leave the system easier to continue.
            </p>
          </div>
          <div className="workflowGrid">
            {workflowSteps.map(([number, title, body]) => (
              <article className="workflowStep" key={title}>
                <span>{number}</span>
                <h3>{title}</h3>
                <p>{body}</p>
              </article>
            ))}
          </div>
        </section>
      </main>
    </Layout>
  );
}
