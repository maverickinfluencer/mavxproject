import React from 'react'
import './videodata.css'

function VideoData() {

  const downloadCSV=(e)=>{
    e.preventDefault();
    console.log("aman");
  }
  return (
    <div className="wrapper">
      <div className="card">
  <div className="card-header">
    Video Data V1
  </div>
  <div className="card-body">
    <h4 className="card-title">Last run :</h4>
    <h4 className="card-text">Status :</h4>
    <div className="btns">
    <a href="https://docs.google.com/spreadsheets/d/1pCI31UUBQtMJiH2mAqjeC3siE0Pks3yu1xRupS8a9QY/edit#gid=0" target="_blank" rel="noopener noreferrer" className="btn btn-primary">Open Sheets</a>
    <a href="http://localhost:8080/api/admin/video-data/youtube/downloadCSV" className="btn btn-primary">Download CSV</a>
  </div>
    </div>
</div>
    </div>
  )
}

export default VideoData