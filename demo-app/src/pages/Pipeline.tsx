import { Link } from 'react-router-dom';
import { usePhaseRoles } from '../data/usePipeline';
import { Phase } from '../data/types';
import './Pipeline.css';

function PhaseNode({ phase }: { phase: Phase }) {
  const roleCount = phase.role_ids.length;
  const to = roleCount > 0 ? `/phase/${phase.id}` : undefined;

  return (
    <div className="pipeline-phase-node">
      {to ? (
        <Link to={to} className="pipeline-phase-link">
          <span className="pipeline-phase-num">{phase.order}</span>
          <h2 className="pipeline-phase-name">{phase.phase}</h2>
          <p className="pipeline-phase-roles">
            {roleCount === 0 ? 'Client handoff' : `${roleCount} role${roleCount !== 1 ? 's' : ''}`}
          </p>
          <p className="pipeline-phase-desc">{phase.description}</p>
          <span className="pipeline-phase-cta">View roles & opportunities →</span>
        </Link>
      ) : (
        <div className="pipeline-phase-link" style={{ opacity: 0.85, cursor: 'default' }}>
          <span className="pipeline-phase-num">{phase.order}</span>
          <h2 className="pipeline-phase-name">{phase.phase}</h2>
          <p className="pipeline-phase-roles">Client handoff</p>
          <p className="pipeline-phase-desc">{phase.description}</p>
        </div>
      )}
    </div>
  );
}

export function Pipeline() {
  const { data, loading, error } = usePhaseRoles();

  if (loading) {
    return (
      <div className="pipeline pipeline--loading" style={{ color: 'var(--df-text)' }}>
        <p>Loading pipeline…</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="pipeline pipeline--error">
        <p>Failed to load pipeline: {error.message}</p>
      </div>
    );
  }

  if (!data) {
    return (
      <div className="pipeline pipeline--error">
        <p>No pipeline data. Check that <code>/mock_data/phase_roles.json</code> exists.</p>
      </div>
    );
  }

  return (
    <div className="pipeline">
      <div className="pipeline-intro">
        <h1 className="pipeline-title">{data.pipeline_name}</h1>
        <p className="pipeline-subtitle">
          Select a phase to see roles and agentic AI opportunities. Use the Claude-to-ClickUp agent (PR-4) to enter task text and log it to ClickUp with tags and dependencies.
        </p>
        <p style={{ marginTop: '0.75rem' }}>
          <Link to="/opportunity/PR-4" className="pipeline-cta-link">Create task with natural language (Claude-to-ClickUp PR-4) →</Link>
        </p>
      </div>

      <div className="pipeline-flow" role="list">
        {data.phases.map((phase) => (
          <PhaseNode key={phase.id} phase={phase} />
        ))}
      </div>
    </div>
  );
}
