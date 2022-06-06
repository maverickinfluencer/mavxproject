import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import MenuIcon from '@mui/icons-material/Menu';
import Container from '@mui/material/Container';
// import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import MenuItem from '@mui/material/MenuItem';
import { Link,useNavigate } from "react-router-dom";
// import Login from "../../pages/login/Login"
// import "./navbar.css";
// import {useContext} from 'react';
// import {AuthContext} from '../../context/AuthContext';
// import AuthService from "../../services/auth.service";

const pages = ['Products', 'Pricing', 'BookTruck'];
const settings = ['Profile', 'Account', 'Dashboard', 'Logout'];

const Navbar = () => {
  // const {user: currentUser, dispatch } = useContext(AuthContext);
  const navigate = useNavigate();
  const [anchorElNav, setAnchorElNav] = React.useState(null);
  const [anchorElUser, setAnchorElUser] = React.useState(null);

  const handleOpenNavMenu = (event) => {
    setAnchorElNav(event.currentTarget);
  };
  // const handleOpenUserMenu = (event) => {
  //   setAnchorElUser(event.currentTarget);
  // };

  const handleCloseNavMenu = () => {
    setAnchorElNav(null);
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };

//   const handleLogout= (e)=>{
//     e.preventDefault();
//     AuthService.logout();
//     navigate("/login");
//     window.location.reload();
//   }

//   const bookPage= (e)=>{
//     e.preventDefault();
//     navigate("/user/booking")
//   }

//   const bookingsPage=(e)=>{
//     e.preventDefault();
//     navigate("/user/bookings");
//   }
//   const BookingRequestPage=(e)=>{
//     e.preventDefault();
//     navigate("/driver/booking-request")
//   }
//   const routes = (e)=>{
//     e.preventDefault();
//     navigate("/driver/routes");
//   }

    const videoDataPage = (e)=>{
        e.preventDefault();
        navigate("/admin/video-data");
    } 
    const descriptionGeneratorPage = (e)=>{
      e.preventDefault();
      navigate("/admin/description-generator");
    }
    const adminPage =(e)=>{
      e.preventDefault();
      navigate("/admin")
    }

  return (
    <AppBar position="static">
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <Link to="/" className="link" ><Typography
            variant="h6"
            noWrap
            component="div"
            sx={{ color: 'white', mr: 2, display: { xs: 'none', md: 'flex' } }}
          >
            MavX.io
          </Typography>
          </Link>

          <Box sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' } }}>
            <IconButton
              size="large"
              aria-label="account of current user"
              aria-controls="menu-appbar"
              aria-haspopup="true"
              onClick={handleOpenNavMenu}
              color="inherit"
            >
              <MenuIcon />
            </IconButton>
            <Menu
              id="menu-appbar"
              anchorEl={anchorElNav}
              anchorOrigin={{
                vertical: 'bottom',
                horizontal: 'left',
              }}
              keepMounted
              transformOrigin={{
                vertical: 'top',
                horizontal: 'left',
              }}
              open={Boolean(anchorElNav)}
              onClose={handleCloseNavMenu}
              sx={{
                display: { xs: 'block', md: 'none' },
              }}
            >
              {/* { currentUser ? (currentUser?.role === 'ROLE_USER' ? <>
              <MenuItem onClick={bookingsPage}>
                  <Typography textAlign="center">Bookings</Typography>
                </MenuItem>
                <MenuItem onClick={bookPage}>
                  <Typography textAlign="center">BookTruck</Typography>
                </MenuItem>
                </>
                : currentUser.role === 'ROLE_DRIVER' && <>
              <MenuItem onClick={BookingRequestPage}>
                  <Typography textAlign="center">Booking Requests</Typography>
                </MenuItem>
                <MenuItem onClick={routes}>
                  <Typography textAlign="center">Routs</Typography>
                </MenuItem>
                </>
              ):(<>
              <MenuItem onClick="#">
                  <Typography textAlign="center">Blogs</Typography>
                </MenuItem>
                <MenuItem onClick="#">
                  <Typography textAlign="center">About Us</Typography>
                </MenuItem>
                </>
                )} */}

                <MenuItem onClick={adminPage}>
                  <Typography textAlign="center">Admin</Typography>
                </MenuItem>
                <MenuItem onClick="#">
                  <Typography textAlign="center">User</Typography>
                </MenuItem>
            </Menu>
          </Box>
          <Typography
            variant="h6"
            noWrap
            component="div"
            sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' } }}
          >
          <Link to="/" className="link" >
          Mavx.io
          </Link>
          </Typography>
          <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
            {/* {pages.map((page) => (
              <Button
                key={page}
                onClick={handleCloseNavMenu}
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                {page}
              </Button>
            ))} */}
            {/* { currentUser ? (
              currentUser.role === 'ROLE_USER' ? (<>
            <Button
                onClick={bookingsPage}
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                Bookings
              </Button>
            <Button
                onClick={bookPage}
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                BookTruck
              </Button>
              </>):
              (currentUser.role === 'ROLE_DRIVER' && <>
            <Button
                onClick={BookingRequestPage}
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                Booking Requests
              </Button>
            <Button
                onClick={routes}
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                Routes
              </Button>
              </>)
            ):(
              <>
            <Button
                onClick="#"
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                Blogs
              </Button>
            <Button
                onClick="#"
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                About Us
              </Button>
              </>
            )} */}
            <Button
                onClick={adminPage}
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                Admin
              </Button>
            <Button
                onClick="#"
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                User
              </Button>
          </Box>

          <Box sx={{ flexGrow: 0 }}>
            <Tooltip title="Login">
              <IconButton  sx={{ p: 0 }}>
              {/* {currentUser &&
                <Typography
                  onClick={handleLogout}
                  variant="h6"
                  noWrap
                  component="div"
                  sx={{ my: 2, color: 'white', flexGrow: 1, display: { xs: 'flex', md: 'flex' } }}
                  >
                  Logout
                  </Typography>
              } */}
              {/* {
                currentUser ?
                (<Typography
                  onClick={handleLogout}
                  variant="h6"
                  noWrap
                  component="div"
                  sx={{ my: 2, color: 'white', flexGrow: 1, display: { xs: 'flex', md: 'flex' } }}
                  >
                  Logout
                  </Typography>):
                (
                <Link to="/login" className="link">
                <Typography
                  variant="h6"
                  noWrap
                  component="div"
                  sx={{ my: 2, color: 'white', flexGrow: 1, display: { xs: 'flex', md: 'flex' } }}
                  >
                  Login
                  </Typography>
                  </Link>
                )
              
              } */}
              <Typography
                  variant="h6"
                  noWrap
                  component="div"
                  sx={{ my: 2, color: 'white', flexGrow: 1, display: { xs: 'flex', md: 'flex' } }}
                  >
                  Login
                  </Typography>
                {/* <Avatar alt="Remy Sharp" src="/static/images/avatar/2.jpg" /> */}
              </IconButton>
            </Tooltip>
            <Menu
              sx={{ mt: '45px' }}
              id="menu-appbar"
              anchorEl={anchorElUser}
              anchorOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              keepMounted
              transformOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              open={Boolean(anchorElUser)}
              onClose={handleCloseUserMenu}
            >
              {settings.map((setting) => (
                <MenuItem key={setting} onClick={handleCloseUserMenu}>
                  <Typography textAlign="center">{setting}</Typography>
                </MenuItem>
              ))}
            </Menu>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
};
export default Navbar;
