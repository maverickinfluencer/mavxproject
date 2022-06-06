import './App.css';

import Navbar from './components/navbar/Navbar'
import VideoData from  './pages/video-data/VideoData'
import Admin from './pages/admin/Admin'

import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate
} from "react-router-dom";
import "../node_modules/bootstrap/dist/css/bootstrap.min.css"
import 'react-toastify/dist/ReactToastify.css';
import HomePage from './pages/home/HomePage';
import DescriptionGenerator from './pages/description-generator/DescriptionGenerator'

function App() {
  return (
    <Router>
    <Navbar/>
      <Routes>
      <Route exact path="/" element={<HomePage/>} />
      <Route exact path="/admin" element={<Admin/>} />
      <Route exact path="/admin/video-data" element={<VideoData/>} />
      <Route exact path="/admin/description-generator" element={<DescriptionGenerator />} />
      {/* <Route  path ="*" element={<Notfound/>} /> */}
    </Routes>
    </Router>
  )
}

export default App;
