import './App.css';

import Navbar from './components/navbar/Navbar'
import VideoData from  './pages/video-data/VideoData'

import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate
} from "react-router-dom";
import "../node_modules/bootstrap/dist/css/bootstrap.min.css"
import 'react-toastify/dist/ReactToastify.css';
import HomePage from './pages/home/HomePage';

function App() {
  return (
    <Router>
    <Navbar/>
      <Routes>
      <Route exact path="/" element={<HomePage/>} />
      <Route exact path="/admin/video-data" element={<VideoData/>} />
      {/* <Route  path ="*" element={<Notfound/>} /> */}
    </Routes>
    </Router>
  )
}

export default App;
