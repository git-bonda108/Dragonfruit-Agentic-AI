import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { ErrorBoundary } from './ErrorBoundary';
import App from './App';
import './index.css';

const rootEl = document.getElementById('root');
if (!rootEl) {
  document.body.innerHTML = '<p style="padding:2rem">No #root element.</p>';
  throw new Error('No #root element');
}

function showError(msg: string): void {
  const el = document.getElementById('root');
  if (!el) return;
  el.innerHTML =
    '<div style="padding:2rem;font-family:system-ui;max-width:560px;">' +
    '<h2 style="color:#c94b62;">App failed to start</h2>' +
    '<pre style="background:#f1f5f9;padding:1rem;overflow:auto;font-size:0.875rem;white-space:pre-wrap;">' +
    String(msg).replace(/</g, '&lt;') +
    '</pre>' +
    '<p><a href="http://localhost:3000" style="color:#E85D75;">Reload</a> · Press F12 → Console for details.</p>' +
    '</div>';
}

try {
  createRoot(rootEl as HTMLElement).render(
    <StrictMode>
      <ErrorBoundary>
        <App />
      </ErrorBoundary>
    </StrictMode>
  );
} catch (e) {
  const msg = e instanceof Error ? (e.message + (e.stack ? '\n\n' + e.stack : '')) : String(e);
  showError(msg);
}
