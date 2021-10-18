import axios from "axios";

const URL = "https://dapi.kakao.com/v2/vision/face/detect"
const API_KEY = "{jo's KAKAO key}"

// 카카오 비전 api
async function requestFacialData(file) {
  const headers = {
    "Content-Type": 'multipart/form-data',
    'Authorization': `KakaoAK ${API_KEY}`
  }
  return await axios.post(URL, file, {headers: headers})
}

const KakaoApi = {
  requestFacialData: (file) => requestFacialData(file)
}

export default KakaoApi