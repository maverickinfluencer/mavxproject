
import axios from 'axios';
import authHeader from './auth-header';

const API_URL = 'http://localhost:8080/api/admin/video-data/';
// const API_URL = process.env.REACT_APP_SERVER_ADDRESS+"/api/user/";

class AdminService {
//   getPublicContent() {
//     return axios.get(API_URL + 'all');
//   }

//   getUserBoard() {
//     return axios.get(API_URL + 'user', { headers: authHeader() });
//   }

//   getModeratorBoard() {
//     return axios.get(API_URL + 'driver', { headers: authHeader() });
//   }

//   getAdminBoard() {
//     return axios.get(API_URL + 'admin', { headers: authHeader() });
//   }
    // createBooking(from, to, user){
    //     console.log("inside createBooking: "+from+to+JSON.stringify(user));
    //     return axios.post(API_URL+'booking',
    //     {
    //         username: user.username, 
    //         from:from,
    //         to:to,
    //         bookingTime: new Date().toDateString()
    //     },
    //     {headers: authHeader()}
        
    // )
    // }   

    // getBookings() {
    //     return axios.get(API_URL + 'booking',{ headers: authHeader() });
    // }

    // async getAllBookings(user){
    //     return await axios.get(API_URL+'bookings',
    //            {
    //                headers: authHeader(),
    //                params: { username:user.username}
    //         },   
    // )}

    createVideoData(){
        return axios.get(API_URL);
    }
}

export default new AdminService();