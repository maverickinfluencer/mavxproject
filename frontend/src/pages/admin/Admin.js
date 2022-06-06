import React from 'react'
import {useNavigate} from 'react-router-dom'

const Admin = () => {
    const navigate = useNavigate();
    const videoDataPage = (e)=>{
        e.preventDefault();
        navigate("/admin/video-data");
    } 
    const descriptionGeneratorPage = (e)=>{
      e.preventDefault();
      navigate("/admin/description-generator");
    }
  return (<>
      <div className="wrapper">
      <div className="card">
  <div className="card-header">
    Video Data V1
  </div>
  <div className="card-body">
    <div className="btns">
    <button onClick={videoDataPage} className="btn btn-primary" >Video Data</button>
    <button onClick={descriptionGeneratorPage}  className="btn btn-primary" >Description Generator Data</button>
  </div>
    </div>
</div>
    </div>
  </>
  )
}

export default Admin