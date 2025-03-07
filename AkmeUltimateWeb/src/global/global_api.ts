import axios from 'axios';
import globalEnvSettings from './global_arg';

// Create an Axios instance
const api = axios.create({
  baseURL: globalEnvSettings.server,
  timeout: globalEnvSettings.timeout,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Global GET method
export async function getListData(url: string, params?: any) {
  try {
    const response = await api.get(url, { params });
    return response.data;
  } catch (error) {
    console.error('GET request failed:', error);
    throw error;
  }
};

// Global POST method
export async function postListData(url: string, data?: any) {
  try {
    const response = await api.post(url, data);
    return response.data;
  } catch (error) {
    console.error('POST request failed:', error);
    throw error;
  }
};