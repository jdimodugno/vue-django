import axios from 'axios';

const api = {
    getHeaders: () => {
        const myHeaders = {
            'Content-Type': 'application/json'
        };

        if (window.localStorage.getItem('token')) {
            myHeaders['Authorization'] = `Token ${window.localStorage.getItem('token')}`
        }

        return myHeaders;
    },
    encode: (obj) => {
        return Object.entries(obj).map(e =>
            `${encodeURIComponent(e[0])}=${encodeURIComponent(e[1])}`,
        ).join('&')
    },
    post: (url, data, headers) => {
        if (headers) {
            return axios.post(url, data, {headers: headers})
        } else {
            return axios.post(url, data)
        }
    },
    get: (url, headers) => axios.get(url, {headers: headers})
}

export default api;
