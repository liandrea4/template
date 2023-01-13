import './App.css';
import NewComponent from "./NewComponent";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
  return (
      <Router>
        <Routes>
          <Route path="/" element={<NewComponent />} />
        </Routes>
      </Router>
  );
}

export default App;
