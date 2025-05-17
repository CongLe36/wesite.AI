import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './pages/Home';
import DocumentManagement from './pages/DocumentManagement';
import NoteTaking from './pages/NoteTaking';
import MetadataExtraction from './pages/MetadataExtraction';
import Navbar from './components/Navbar';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/documents" component={DocumentManagement} />
          <Route path="/note-taking" component={NoteTaking} />
          <Route path="/metadata-extraction" component={MetadataExtraction} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;