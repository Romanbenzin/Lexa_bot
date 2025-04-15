import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

class ErrorBoundary extends React.Component {
  state = { hasError: false }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, info) {
    console.error("React Error:", error, info);
  }

  render() {
    if (this.state.hasError) {
      return <h1 style={{color: 'red'}}>App Failed to Load</h1>;
    }
    return this.props.children;
  }
}

ReactDOM.render(
  <React.StrictMode>
    <ErrorBoundary>
      <App />
    </ErrorBoundary>
  </React.StrictMode>,
  document.getElementById('root')
);