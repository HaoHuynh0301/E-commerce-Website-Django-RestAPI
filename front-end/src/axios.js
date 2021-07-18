import axios from 'axios';

const baseURL = 'http://127.0.0.1:8000/';

const axiosInstance = axios.create({
    baseURL: baseURL,
    timeout: 5000,
    headers: {
        Authorization: localStorage.getItem('access-token')
            ? 'JWT' + localStorage.getItem('access-token')
            : null,
        'Content-Type': 'application/json',
        accept: 'application/json',
    },
});

axiosInstance.interceptors.response.use (
    (response) => {
        return response;
    },
    async function(error) {
        const originalRequest = error.config;
        if(typeof error.response == 'undefined') {
            alert(
                'A server/network error occurred. ' + 
                    'Look like CORS might be problem. ' +
                    'Sorry about this - we will fixed it shorty'
            );
            return Promise.reject(error);
        }
        if(error.response.status == 401) {
            alert('Email or password is invalid')
            return Promise.reject(error);
        }
        if(error.response.status == 404 &&
        originalRequest.url === baseURL + 'token/refresh/') {
            window.location.href = '/';
            return Promise.reject(error);
        }
        if(
            error.response.data.code === 'token_not_valid' &&
            error.response.data.code === 401 &&
            error.response.statusText === 'Unauthorized'
        ) {
            const refreshToken = localStorage.getItem('refresh-token');
            if(refreshToken) {
                const tokenParts = JSON.parse(atob(refreshToken.split('.')[1]));
                const now = Math.ceil(Date.now() / 1000);
                console.log(tokenParts.exp);
                if(tokenParts.exp > now) {
                    return axiosInstance
                        .post('/token/refresh/', {
                            refresh: refreshToken
                        })
                        .then((response) => {
                            localStorage.setItem('access-token', response.data.access);
                            localStorage.setItem('refresh-token', response.data.refresh);
                            axiosInstance.defaults.headers['Authorization'] = 
                                'JWT' + response.data.access;
                            originalRequest.defaults.headers['Authorization'] =
                                'JWT' + response.data.access;
                            return axiosInstance(originalRequest);
                        })
                        .catch((err) => {
                            console.log('err');
                        }) 
                } else {
                   console.log("Refresh token is not expired");
                   window.location.href = '/';
                }
            } else {
                console.log("Refresh token is not available");
                window.location.href = '/';
            }
            return Promise.reject(error);
        }

    }
);

export default axiosInstance;