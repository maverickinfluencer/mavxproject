import React, {useEffect, useState} from 'react'
import './videodata.css'
import axios from 'axios'

function VideoData() {
  const API_URL = process.env.REACT_APP_SERVER_ADDRESS
  const [videoDataResponse, setVideoDataResponse] = useState({})

  const handleTodayData=()=>{
    window.open("https://docs.google.com/spreadsheets/d/1pCI31UUBQtMJiH2mAqjeC3siE0Pks3yu1xRupS8a9QY/edit#gid=0");
  }
  const handleHistoricalData=()=>{
    window.open("https://docs.google.com/spreadsheets/d/1hq-i4YKAGv7HvirtjqL-8TNOH0RPHXUTqyFy8oOLSFE/edit#gid=0");
  }
  useEffect(()=>{
    axios.get(API_URL+"/admin/video-data/status").then((res)=>{
      console.log(res.data);
      setVideoDataResponse(res.data)
    })
  },[])
  console.log(videoDataResponse)

  return (
    <div className="wrapper">
      <div className="card">
  <div className="card-header">
    Video Data V1
  </div>
  <div className="card-body">
    <h4 className="card-title">Last run :{videoDataResponse.last_run}</h4>
    <h4 className="card-text">Status : {videoDataResponse.video_data_status} </h4>
    <div className="btns">
    <button onClick={handleTodayData} className="btn btn-primary" >Today Data</button>
    <button onClick={handleHistoricalData}  className="btn btn-primary" >Historical Data</button>
  </div>
    </div>
</div>
    </div>
  )
}

export default VideoData