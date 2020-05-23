import axios from 'axios';

export const apiURL = 'https://9jsmzaxdn9.execute-api.us-east-1.amazonaws.com/api/'

const api = axios.create({
	baseURL: apiURL,
	timeout: 3000,
})

export const registerURL =
	(url) => api.post('register/', { link: url })
